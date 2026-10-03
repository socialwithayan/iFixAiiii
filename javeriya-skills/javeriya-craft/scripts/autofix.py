#!/usr/bin/env python3
"""
JAVERIYA CRAFT — AUTO-FIX ENGINE.
measure -> fix -> re-render -> re-measure -> repeat.

Javeriya never sees a failing render. This script owns the loop that is otherwise
done by hand: nudging --rh row heights, shrinking the headline, trimming
padding, re-rendering, eyeballing, repeating.

USAGE
    python3 autofix.py <design.html> [--max-loops 6] [--assets DIR]

WHAT IT FIXES, cheapest edit first:
    1. footer-collision   body overruns the footer      -> shrink row --rh
    2. dead-space         >120px of empty above footer  -> grow row --rh
    3. overflow           a card's content is clipped   -> grow that row
    4. ragged-widths      sibling cards differ in width -> force one width
    5. sub12-text         any text under 12px           -> raise it to 12px
    6. heading-overflow   headline wider than its box   -> step the size down

WHAT IT REFUSES TO FIX, and reports instead:
    spotlight-count  zero or two+ lit blocks       -> a decision about what matters
    fire-count       fire word missing or doubled  -> a copy decision
    pill-count       more than one tag pill        -> a copy decision

Every pass writes back into the SOURCE html, so the delivered file is the fixed
file. The loop stops the moment a full pass is clean, or at --max-loops with an
honest STUCK report.

EXIT: 0 = clean (safe to export)   1 = stuck (report printed, do not ship)
"""
import argparse, pathlib, re, subprocess, sys

CANVAS_W, CANVAS_H = 1080, 1350
FOOTER_TOP = 1306
MIN_FONT = 12.0
DEAD_LIMIT = 120        # px of empty above the footer before rows grow
SAFE_GAP = 8            # px we want between the body bottom and the footer
H1_FLOOR = 44           # headline never steps below this

HERE = pathlib.Path(__file__).resolve().parent
SKILL = HERE.parent


def _design_scripts():
    """Reuse /javeriya-design's embed + launch so both skills render identically."""
    for c in [SKILL.parent / "javeriya-design" / "scripts",
              pathlib.Path.home() / ".claude/skills/javeriya-design/scripts",
              pathlib.Path("/mnt/skills/user/javeriya-design/scripts")]:
        if (c / "build.py").exists():
            sys.path.insert(0, str(c))
            import build
            return build
    print("cannot find /javeriya-design/scripts/build.py — install it next to this skill")
    sys.exit(1)


MEASURE = """() => {
  const cv = document.querySelector('.canvas');
  if (!cv) return {error: 'no .canvas'};
  const cr = cv.getBoundingClientRect();
  const R = e => { const b = e.getBoundingClientRect();
    return {t:b.top-cr.top, l:b.left-cr.left, w:b.width, h:b.height,
            b:b.bottom-cr.top, r:b.right-cr.left}; };

  const rows = [...document.querySelectorAll('.rowband')].map(e => ({
    id: e.id || '', rh: parseFloat(getComputedStyle(e).getPropertyValue('--rh')) || 0,
    ...R(e)
  }));

  const cards = [...document.querySelectorAll('.card')];
  const boxes = cards.map(R);
  const widths = [...new Set(boxes.map(b => Math.round(b.w * 10) / 10))];
  const overflow = cards.map((c, i) => ({i, ov: c.scrollHeight - c.clientHeight}))
                        .filter(o => o.ov > 2);

  // the signature: one lit block, one fire word in the headline
  const h1el = document.querySelector('.h1');

  // type floor
  const small = [];
  document.querySelectorAll('.canvas *').forEach(el => {
    if (el.children.length === 0 && el.textContent.trim()) {
      const fs = parseFloat(getComputedStyle(el).fontSize);
      if (fs < 12) small.push({tag: el.tagName, cls: el.className, fs: +fs.toFixed(1)});
    }
  });

  // headline fit
  const h1 = document.querySelector('.h1, h1');
  const h1over = h1 ? (h1.scrollWidth > h1.clientWidth + 2) : false;
  const h1fs = h1 ? parseFloat(getComputedStyle(h1).fontSize) : 0;

  let bodyBottom = 0;
  document.querySelectorAll('.content *').forEach(el => {
    const b = R(el); if (b.h > 0 && b.b > bodyBottom) bodyBottom = b.b; });

  let edge = 0;
  document.querySelectorAll('.content *').forEach(el => {
    const b = R(el); if (b.l < -1 || b.r > cr.width + 1) edge++; });

  return {
    canvas: {w: +cr.width.toFixed(1), h: +cr.height.toFixed(1)},
    rows, widths, overflow, small, edge,
    n_cards: cards.length,
    spotlights: document.querySelectorAll('.spotlight').length,
    fires: document.querySelectorAll('.fire').length,
    fireInH1: h1el ? h1el.querySelectorAll('.fire').length : 0,
    pills: document.querySelectorAll('.pill').length,
    h1over, h1fs: +h1fs.toFixed(1),
    bodyBottom: Math.round(bodyBottom)
  };
}"""


def measure(build, src: pathlib.Path):
    from playwright.sync_api import sync_playwright
    final = build.embed(src.resolve())
    with sync_playwright() as p:
        b = build.launch(p, ["--force-device-scale-factor=1"])
        pg = b.new_page(viewport={"width": CANVAS_W + 40, "height": CANVAS_H + 50})
        pg.goto(f"file://{final}")
        pg.wait_for_timeout(1600)
        pg.evaluate("window.renderFrame && window.renderFrame(1)")
        m = pg.evaluate(MEASURE)
        b.close()
    final.unlink(missing_ok=True)
    return m


def faults(m):
    """Everything wrong with this render, in escalation order."""
    f = []
    dead = FOOTER_TOP - m["bodyBottom"]
    if dead < SAFE_GAP:
        f.append(("footer-collision", f"body reaches {m['bodyBottom']}, footer at {FOOTER_TOP}"))
    elif dead > DEAD_LIMIT:
        f.append(("dead-space", f"{dead}px empty above the footer"))
    if m["overflow"]:
        f.append(("overflow", f"{len(m['overflow'])} card(s) clipped"))
    if len(m["widths"]) > 1:
        f.append(("ragged-widths", str(m["widths"])))
    if m["small"]:
        f.append(("sub12-text", str(m["small"][:3])))
    if m["h1over"]:
        f.append(("heading-overflow", f"headline at {m['h1fs']}px does not fit"))
    # refuse-to-fix: these are decisions, not nudges
    if m["spotlights"] != 1:
        f.append(("spotlight-count", f"{m['spotlights']} lit blocks, need exactly 1"))
    if m["fires"] != 1 or m["fireInH1"] != 1:
        f.append(("fire-count", f"{m['fires']} fire words ({m['fireInH1']} in headline), need exactly 1 in the headline"))
    if m["pills"] > 1:
        f.append(("pill-count", f"{m['pills']} tag pills, at most 1"))
    if m["edge"]:
        f.append(("edge-break", f"{m['edge']} element(s) cross the canvas edge"))
    return f


UNFIXABLE = {"spotlight-count", "fire-count", "pill-count", "edge-break"}


def scale_rows(html, delta_total, rows):
    """Spread a height change across the rowbands that can absorb it.

    --rh is a MIN-height, so a row whose content already exceeds it will not
    shrink — spread the delta over the rows that have slack.
    """
    movable = [r for r in rows if r["rh"] > 0]
    if not movable:
        return html, False
    per = delta_total / len(movable)
    changed = False
    for r in movable:
        new = max(60, round(r["rh"] + per))
        if new == round(r["rh"]):
            continue
        pat = re.compile(r'(--rh:\s*)' + re.escape(str(int(r["rh"]))) + r'(px)')
        html2, n = pat.subn(rf'\g<1>{new}\g<2>', html, count=1)
        if n:
            html, changed = html2, True
    return html, changed


def _card_height(html):
    mt = re.search(r'(\.card\{[^}]*?height:\s*)(\d+(?:\.\d+)?)(px)', html, re.S)
    return (mt, float(mt.group(2))) if mt else (None, None)


def fix_card_height(html, delta_px, n_cards):
    """Grow or shrink the fixed card height. Floor at 96px — below that a card
    with a title, two lines and a chip cannot breathe, and the answer is fewer
    cards or fewer words, not a shorter box."""
    mt, cur = _card_height(html)
    if not mt:
        return html, False
    new = max(96, round(cur + delta_px / max(1, n_cards)))
    if new == round(cur):
        return html, False
    return html[:mt.start(2)] + str(new) + html[mt.end(2):], True


def _step_h1(html, m, by=-4):
    cur = m["h1fs"]
    if not cur or cur + by < H1_FLOOR:
        return html, False
    html2, n = re.subn(r'(\.h1\{font:\s*\d{3}\s+)' + str(int(cur)) + r'(px)',
                       rf'\g<1>{int(cur) + by}\g<2>', html, count=1)
    return html2, bool(n)


def _resize(html, m, delta):
    """delta < 0 removes height, delta > 0 adds it. Three escape hatches, in
    order of how little they cost the design:
      1. rowbands whose --rh is the binding constraint (free — pure whitespace)
      2. the headline, when the head band has outgrown its own band
      3. the card height (last: it costs the content room)
    """
    binding = [r for r in m["rows"] if r["rh"] > 0 and abs(r["h"] - r["rh"]) < 2]
    if binding:
        html2, ok = scale_rows(html, delta, binding)
        if ok:
            return html2, ok, "rows"
    head = next((r for r in m["rows"] if r["h"] > r["rh"] + 2), None)
    if delta < 0 and head is not None and m["h1fs"]:
        html2, ok = _step_h1(html, m)
        if ok:
            return html2, ok, "headline"
    n = max(1, len(m.get("widths", [])) and len([r for r in m["rows"]]) or 1)
    html2, ok = fix_card_height(html, delta, m.get("n_cards", 6))
    return html2, ok, "cards"


def fix_footer_collision(html, m):
    over = (FOOTER_TOP - SAFE_GAP) - m["bodyBottom"]     # negative
    html2, ok, how = _resize(html, m, over - 2)
    if ok:
        print(f"           (via {how})")
    return html2, ok


def fix_dead_space(html, m):
    gap = (FOOTER_TOP - SAFE_GAP) - m["bodyBottom"]      # positive
    html2, ok, how = _resize(html, m, gap)
    if ok:
        print(f"           (via {how})")
    return html2, ok


def fix_overflow(html, m):
    """Grow the card box a step at a time. A big single jump overshoots into a
    footer collision and the loop then oscillates between the two faults."""
    html2, ok = fix_card_height(html, 12, 1)
    if ok:
        return html2, ok
    return scale_rows(html, 12 * max(1, len(m["overflow"])), m["rows"])


def fix_ragged_widths(html, m):
    """Sibling cards must share a width. Force the flex column to stretch."""
    if ".rail{" in html and "align-items" not in html.split(".rail{")[1][:200]:
        return html.replace(".rail{", ".rail{align-items:stretch;", 1), True
    if re.search(r'\.card\{', html):
        return re.sub(r'(\.card\{)', r'\g<1>width:100%;', html, count=1), True
    return html, False


def fix_sub12(html, m):
    changed = False
    for s in m["small"]:
        for mt in re.finditer(r'font:\s*(\d{3})\s+(\d+(?:\.\d+)?)px', html):
            if float(mt.group(2)) < MIN_FONT:
                html = html[:mt.start(2)] + str(int(MIN_FONT)) + html[mt.end(2):]
                changed = True
                break
    if not changed:
        for mt in re.finditer(r'font-size:\s*(\d+(?:\.\d+)?)px', html):
            if float(mt.group(1)) < MIN_FONT:
                html = html[:mt.start(1)] + str(int(MIN_FONT)) + html[mt.end(1):]
                changed = True
                break
    return html, changed


def fix_heading(html, m):
    """Step the headline down 4px at a time. Below the floor it is a copy problem."""
    cur = m["h1fs"]
    if cur <= H1_FLOOR:
        return html, False
    new = int(cur) - 4
    html2, n = re.subn(r'(\.h1\{font:\s*\d{3}\s+)' + str(int(cur)) + r'(px)',
                       rf'\g<1>{new}\g<2>', html, count=1)
    return html2, bool(n)


FIXERS = {
    "footer-collision": fix_footer_collision,
    "dead-space":       fix_dead_space,
    "overflow":         fix_overflow,
    "ragged-widths":    fix_ragged_widths,
    "sub12-text":       fix_sub12,
    "heading-overflow": fix_heading,
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("--max-loops", type=int, default=6)
    ap.add_argument("--assets", default=None)
    a = ap.parse_args()

    if a.assets:
        import os
        os.environ["JAVERIYA_ASSETS"] = a.assets
    build = _design_scripts()
    src = pathlib.Path(a.html).resolve()
    if not src.exists():
        print("no such file:", src)
        sys.exit(1)

    print(f"AUTOFIX  {src.name}")
    for loop in range(1, a.max_loops + 1):
        m = measure(build, src)
        if m.get("error"):
            print("  measure failed:", m["error"])
            sys.exit(1)
        f = faults(m)
        if not f:
            print(f"  loop {loop}: CLEAN — safe to export")
            sys.exit(0)

        blocked = [x for x in f if x[0] in UNFIXABLE]
        fixable = [x for x in f if x[0] not in UNFIXABLE]
        print(f"  loop {loop}: " + ", ".join(n for n, _ in f))

        if blocked and not fixable:
            print("\nSTUCK — these are design decisions, not measurements:")
            for name, detail in blocked:
                print(f"  {name}: {detail}")
            print("\nFix them in the layout or the copy, then re-run.")
            sys.exit(1)

        html = src.read_text()
        did = False
        for name, _ in fixable:
            html2, ok = FIXERS[name](html, m)
            if ok:
                html, did = html2, True
                print(f"           fixed {name}")
                break                      # one edit per loop, then re-measure
        if not did:
            print("\nSTUCK — no automatic edit left for:", ", ".join(n for n, _ in f))
            sys.exit(1)
        src.write_text(html)

    final = faults(measure(build, src))
    if not final:
        print(f"  CLEAN after {a.max_loops} loops — safe to export")
        sys.exit(0)
    print(f"\nSTUCK after {a.max_loops} loops:")
    for name, detail in final:
        print(f"  {name}: {detail}")
    sys.exit(1)


if __name__ == "__main__":
    main()
