#!/usr/bin/env python3
"""
SAMAN CRAFT — AUTO-FIX ENGINE.
measure -> fix -> re-render -> re-measure -> repeat.

Saman never sees a failing render. This script owns the loop that is otherwise
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
    detached-card    a card is off the spine       -> a layout decision, not a nudge
    no-spine         no .spine path at all         -> the sheet is not hers yet
    pill-count       zero or two+ Ink Pills        -> a copy decision

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
    """Reuse /saman-design's embed + launch so both skills render identically."""
    for c in [SKILL.parent / "saman-design" / "scripts",
              pathlib.Path.home() / ".claude/skills/saman-design/scripts",
              pathlib.Path("/mnt/skills/user/saman-design/scripts")]:
        if (c / "build.py").exists():
            sys.path.insert(0, str(c))
            import build
            return build
    print("cannot find /saman-design/scripts/build.py — install it next to this skill")
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

  // spine
  const path = document.querySelector('.spine path');
  let len = 0, pts = [];
  if (path) { try {
    len = path.getTotalLength();
    const svg = path.ownerSVGElement, sr = svg.getBoundingClientRect(), vb = svg.viewBox.baseVal;
    const sx = (vb && vb.width ? sr.width / vb.width : 1);
    const sy = (vb && vb.height ? sr.height / vb.height : 1);
    const ox = sr.left - cr.left, oy = sr.top - cr.top;
    for (let i = 0; i <= 300; i++) {
      const q = path.getPointAtLength(len * i / 300);
      pts.push([ox + q.x * sx, oy + q.y * sy]);
    }
  } catch (e) { len = 0; } }
  const gapTo = b => { let best = 1e9;
    for (const [x, y] of pts) {
      const dx = x < b.l ? b.l - x : (x > b.r ? x - b.r : 0);
      const dy = y < b.t ? b.t - y : (y > b.b ? y - b.b : 0);
      const d = Math.hypot(dx, dy); if (d < best) best = d;
    } return best; };
  // A card counts as attached if it touches the spine directly OR through its
  // own node sitting on the line. Without this, any layout that hangs cards off
  // a stub reads as detached even though it is correctly joined.
  const nodeEls = [...document.querySelectorAll('.node')];
  const nodeOff = nodeEls.map(n => Math.round(gapTo(R(n))));
  const attach = (b, el) => {
    let g = gapTo(b);
    const own = el.querySelector('.node');
    if (own) {
      const nb = R(own);
      if (gapTo(nb) <= 8) g = Math.min(g, Math.hypot(
        nb.l > b.r ? nb.l - b.r : (b.l > nb.r ? b.l - nb.r : 0),
        nb.t > b.b ? nb.t - b.b : (b.t > nb.b ? b.t - nb.b : 0)));
    }
    return Math.round(g);
  };
  const detached = pts.length ? cards.map((c, i) => ({i, g: attach(boxes[i], c)}))
                                     .filter(o => o.g > 48) : [];

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
    rows, widths, overflow, detached, small, edge,
    n_cards: cards.length,
    spineLen: Math.round(len),
    nodeOffSpine: Math.max(0, ...nodeOff, 0),
    nodeSizes: [...new Set([...document.querySelectorAll('.node')]
                  .map(e => Math.round(e.getBoundingClientRect().width)))],
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
    if m["spineLen"] < 200:
        f.append(("no-spine", "no .spine path — this is not a Saman sheet yet"))
    if m["detached"]:
        f.append(("detached-card", f"cards {[d['i'] for d in m['detached']]} off the spine"))
    if m["pills"] != 1:
        f.append(("pill-count", f"{m['pills']} Ink Pills, need exactly 1"))
    if m["edge"]:
        f.append(("edge-break", f"{m['edge']} element(s) cross the canvas edge"))
    if len(m["nodeSizes"]) > 1:
        f.append(("mixed-nodes", f"node sizes {m['nodeSizes']}"))
    if m.get("nodeOffSpine", 0) > 8:
        f.append(("node-off-spine", f"a node sits {m['nodeOffSpine']}px off the line"))
    return f


UNFIXABLE = {"no-spine", "detached-card", "pill-count", "mixed-nodes",
             "edge-break", "node-off-spine"}


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
        os.environ["SAMAN_ASSETS"] = a.assets
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
