#!/usr/bin/env python3
"""
JAVERIYA GREY GATE — greyscale render + the 15-check table.

Usage:
    python3 scripts/greygate.py <design.html>

Writes <name>-GREY.png and prints a 15-row table.
Checks 1-10 are MEASURED here. Checks 11-15 print as JUDGE — the model looks at
the grey PNG and verdicts them.

Why grey: her sheets live on fire and black, and colour that strong hides weak
structure. With the brand stripped out, the spotlight has to win on size,
position and contrast alone. If it does not win in grey, the fire is doing the
designer's job. Never show Javeriya a grey below 15/15 — fix it, re-run, then
show her.
"""
import pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import embed, launch, CANVAS_W, CANVAS_H  # noqa: E402
from playwright.sync_api import sync_playwright      # noqa: E402

FOOTER_TOP = 1306

# Read at t=0, before anything animates: a paused feed shows frame one.
FRAME_ONE = """() => {
  const op = s => { const e = document.querySelector(s);
    return e ? parseFloat(getComputedStyle(e).opacity) : 0; };
  return {h1: op('.h1'), footer: op('.footer')};
}"""

MEASURE = """() => {
  const cv = document.querySelector('.canvas');
  if (!cv) return {error: 'no .canvas'};
  const cr = cv.getBoundingClientRect();
  const R = e => { const b = e.getBoundingClientRect();
    return {t:b.top-cr.top, l:b.left-cr.left, w:b.width, h:b.height,
            b:b.bottom-cr.top, r:b.right-cr.left}; };

  const cards = [...document.querySelectorAll('.card')];
  const widths = [...new Set(cards.map(c => Math.round(R(c).w * 10) / 10))];
  const overflow = cards.filter(c => c.scrollHeight > c.clientHeight + 2).length;

  // ---- the signature: one lit block, one fire word in the headline ----
  const spots = [...document.querySelectorAll('.spotlight')];
  const h1 = document.querySelector('.h1');
  const spotIsCard = spots.length === 1 && spots[0].classList.contains('card');

  // ---- type floor ----
  let minFs = 99, small = [];
  document.querySelectorAll('.canvas *').forEach(el => {
    if (el.children.length === 0 && el.textContent.trim()) {
      const fs = parseFloat(getComputedStyle(el).fontSize);
      if (fs < minFs) minFs = fs;
      if (fs < 12) small.push(el.tagName + ':' + el.textContent.trim().slice(0, 16));
    }
  });

  // ---- vertical fit ----
  const fe = document.querySelector('.footer');
  const f = fe ? R(fe) : null;
  let bodyBottom = 0;
  document.querySelectorAll('.content *').forEach(el => {
    const b = R(el); if (b.b > bodyBottom && b.h > 0) bodyBottom = b.b; });

  let edge = 0;
  document.querySelectorAll('.content *').forEach(el => {
    const b = R(el); if (b.l < -1 || b.r > cr.width + 1) edge++; });

  return {
    canvas: {w: +cr.width.toFixed(1), h: +cr.height.toFixed(1)},
    footer: f ? {t: +f.t.toFixed(1), w: +f.w.toFixed(1)} : null,
    widths, overflow,
    spotlights: spots.length, spotIsCard,
    fires: document.querySelectorAll('.fire').length,
    fireInH1: h1 ? h1.querySelectorAll('.fire').length : 0,
    pills: document.querySelectorAll('.pill').length,
    minFs: +minFs.toFixed(1), small,
    bodyBottom: Math.round(bodyBottom), edge
  };
}"""

JUDGE = [
    "Hierarchy survives greyscale — headline first, then the spotlight, then the rest",
    "The spotlight is the obvious first stop even with the fire stripped out",
    "The dark stage reads clean — glow behind, never muddying text",
    "Fire appears in four places at most: fire word, spotlight, tag pill, send circle",
    "Nothing competes with the spotlight — no second loud block",
]


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    src = pathlib.Path(sys.argv[1]).resolve()
    out = src.parent / (src.stem + "-GREY.png")
    final = embed(src)

    with sync_playwright() as p:
        b = launch(p, ["--force-device-scale-factor=2", "--high-dpi-support=1"])
        pg = b.new_page(viewport={"width": CANVAS_W + 40, "height": CANVAS_H + 50},
                        device_scale_factor=2)
        pg.goto(f"file://{final}")
        pg.wait_for_timeout(2400)
        pg.evaluate("window.renderFrame && window.renderFrame(0)")
        f1 = pg.evaluate(FRAME_ONE)
        pg.evaluate("window.renderFrame && window.renderFrame(1)")
        m = pg.evaluate(MEASURE)
        pg.evaluate("document.querySelector('.canvas').style.filter='grayscale(1)'")
        pg.wait_for_timeout(200)
        pg.locator(".canvas").screenshot(path=str(out))
        b.close()

    if m.get("error"):
        print("MEASURE FAILED:", m["error"])
        sys.exit(1)

    sized = any(k in src.stem.lower() for k in ("ladder", "podium"))
    dead = FOOTER_TOP - m["bodyBottom"]
    rows = [
        (1, f"Canvas {CANVAS_W}x{CANVAS_H}",
         abs(m["canvas"]["w"] - CANVAS_W) < 2 and abs(m["canvas"]["h"] - CANVAS_H) < 2,
         f"{m['canvas']['w']}x{m['canvas']['h']}"),
        (2, "Footer pinned at 1306, full width",
         bool(m["footer"]) and abs(m["footer"]["t"] - FOOTER_TOP) < 2
         and abs(m["footer"]["w"] - CANVAS_W) < 2, str(m["footer"])),
        (3, "No card overflows its box", m["overflow"] == 0, f"{m['overflow']} overflowing"),
        (4, "Card widths equal" + (" (sized frame, exempt)" if sized else ""),
         len(m["widths"]) <= 1 or sized, str(m["widths"])),
        (5, "No text below 12px", len(m["small"]) == 0, f"min {m['minFs']}px {m['small'][:3]}"),
        (6, "Exactly one spotlight, and it is a card",
         m["spotlights"] == 1 and m["spotIsCard"], f"{m['spotlights']} spotlights"),
        (7, "Exactly one fire word, in the headline",
         m["fires"] == 1 and m["fireInH1"] == 1,
         f"{m['fires']} fire words, {m['fireInH1']} in headline"),
        (8, "At most one tag pill", m["pills"] <= 1, f"{m['pills']} pills"),
        (9, "Frame one is not blank (headline + footer at t=0)",
         f1["h1"] > 0.99 and f1["footer"] > 0.99, str(f1)),
        (10, "Body clears footer, no dead band",
         8 <= dead <= 120 and m["edge"] == 0,
         f"gap {dead}px above footer, {m['edge']} edge breaks"),
    ]

    print(f"\nGREY GATE — {src.name}")
    print("-" * 72)
    passed = 0
    for n, name, ok, detail in rows:
        passed += bool(ok)
        print(f"{n:>3}  {'PASS' if ok else 'FAIL'}  {name:<46} {'' if ok else detail}")
    for i, q in enumerate(JUDGE, start=11):
        print(f"{i:>3}  JUDGE {q}")
    print("-" * 72)
    print(f"MEASURED {passed}/10   grey render -> {out.name}")
    if passed < 10:
        print("Fix the FAILs and re-run. Never show Javeriya a grey below 15/15.")
    else:
        print("Measured checks clean. Now judge 11-15 on the PNG, then show her.")
    sys.exit(0 if passed == 10 else 1)


if __name__ == "__main__":
    main()
