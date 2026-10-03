#!/usr/bin/env python3
"""
SAMAN GREY GATE — greyscale render + the 15-check table.

Usage:
    python3 scripts/greygate.py <design.html>

Writes <name>-GREY.png and prints a 15-row table.
Checks 1-10 are MEASURED here. Checks 11-15 print as JUDGE — the model looks at
the grey PNG and verdicts them.

Why grey: colour hides bad structure. If the sheet does not read with the brand
stripped out, no palette will save it. Never show Saman a grey below 15/15 —
fix it first, re-run, then show her.
"""
import pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import embed, launch, CANVAS_W, CANVAS_H  # noqa: E402
from playwright.sync_api import sync_playwright      # noqa: E402

MEASURE = """() => {
  const cv = document.querySelector('.canvas');
  if (!cv) return {error: 'no .canvas'};
  const cr = cv.getBoundingClientRect();
  const R = e => { const b = e.getBoundingClientRect();
    return {t:b.top-cr.top, l:b.left-cr.left, w:b.width, h:b.height,
            b:b.bottom-cr.top, r:b.right-cr.left}; };

  const cards = [...document.querySelectorAll('.card')];
  const boxes = cards.map(R);
  const widths = [...new Set(boxes.map(b => Math.round(b.w * 10) / 10))];
  const overflow = cards.filter(c => c.scrollHeight > c.clientHeight + 2).length;

  // ---- the spine, sampled ----
  const path = document.querySelector('.spine path');
  let len = 0, pts = [];
  if (path) {
    try {
      len = path.getTotalLength();
      const svg = path.ownerSVGElement;
      const sr = svg.getBoundingClientRect();
      // viewBox units -> canvas px
      const vb = svg.viewBox.baseVal;
      const sx = (vb && vb.width  ? sr.width  / vb.width  : 1);
      const sy = (vb && vb.height ? sr.height / vb.height : 1);
      const ox = sr.left - cr.left, oy = sr.top - cr.top;
      for (let i = 0; i <= 400; i++) {
        const p = path.getPointAtLength(len * i / 400);
        pts.push([ox + p.x * sx, oy + p.y * sy]);
      }
    } catch (e) { len = 0; }
  }

  // ---- attachment: every card touches the spine or stubs off it (<=24px) ----
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
  const gaps = pts.length ? cards.map((c, i) => attach(boxes[i], c)) : [];
  const detached = gaps.filter(g => g > 48).length;

  // ---- nodes all one size ----
  const nodes = [...document.querySelectorAll('.node')].map(e => {
    const b = e.getBoundingClientRect(); return Math.round(b.width); });
  const nodeSizes = [...new Set(nodes)];

  // ---- type floor ----
  let minFs = 99, small = [];
  document.querySelectorAll('.canvas *').forEach(el => {
    if (el.children.length === 0 && el.textContent.trim()) {
      const fs = parseFloat(getComputedStyle(el).fontSize);
      if (fs < minFs) minFs = fs;
      if (fs < 12) small.push(el.tagName + ':' + el.textContent.trim().slice(0, 16));
    }
  });

  // ---- vertical fit: body must clear the footer, without a dead band ----
  const fe = document.querySelector('.footer');
  const f = fe ? R(fe) : null;
  let bodyBottom = 0;
  document.querySelectorAll('.content *').forEach(el => {
    const b = R(el); if (b.b > bodyBottom && b.h > 0) bodyBottom = b.b; });

  // ---- edge safety ----
  let edge = 0;
  document.querySelectorAll('.content *').forEach(el => {
    const b = R(el); if (b.l < -1 || b.r > cr.width + 1) edge++; });

  return {
    canvas: {w: +cr.width.toFixed(1), h: +cr.height.toFixed(1)},
    footer: f ? {t: +f.t.toFixed(1), w: +f.w.toFixed(1)} : null,
    widths, overflow, detached, gaps,
    spineLen: Math.round(len),
    nodeSizes, nodeOffSpine: Math.max(0, ...nodeOff, 0), nodeCount: nodes.length,
    pills: document.querySelectorAll('.pill').length,
    minFs: +minFs.toFixed(1), small,
    bodyBottom: Math.round(bodyBottom), edge
  };
}"""

JUDGE = [
    "Hierarchy survives greyscale — the headline wins, then sections, then body",
    "The spine reads as ONE continuous line, start to end, no visual breaks",
    "Air — roughly 60% of the canvas is ground, it does not feel packed",
    "The spine has an obvious start and an obvious end",
    "Nothing floats — every block clearly belongs to the line",
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
        pg.evaluate("window.renderFrame && window.renderFrame(1)")
        m = pg.evaluate(MEASURE)
        pg.evaluate("document.querySelector('.canvas').style.filter='grayscale(1)'")
        pg.wait_for_timeout(200)
        pg.locator(".canvas").screenshot(path=str(out))
        b.close()

    if m.get("error"):
        print("MEASURE FAILED:", m["error"])
        sys.exit(1)

    is_funnel = "funnel" in src.stem.lower()
    dead = 1306 - m["bodyBottom"]
    rows = [
        (1, f"Canvas {CANVAS_W}x{CANVAS_H}",
         abs(m["canvas"]["w"] - CANVAS_W) < 2 and abs(m["canvas"]["h"] - CANVAS_H) < 2,
         f"{m['canvas']['w']}x{m['canvas']['h']}"),
        (2, "Footer pinned at 1306, full width",
         bool(m["footer"]) and abs(m["footer"]["t"] - 1306) < 2
         and abs(m["footer"]["w"] - CANVAS_W) < 2, str(m["footer"])),
        (3, "No card overflows its box", m["overflow"] == 0, f"{m['overflow']} overflowing"),
        (4, "Card widths equal" + (" (funnel exempt)" if is_funnel else ""),
         len(m["widths"]) <= 1 or is_funnel, str(m["widths"])),
        (5, "No text below 12px", len(m["small"]) == 0, f"min {m['minFs']}px {m['small'][:3]}"),
        (6, "Spine present and substantial", m["spineLen"] > 200, f"len {m['spineLen']}"),
        (7, "Every card attached to the spine (<=48px)",
         m["spineLen"] > 200 and m["detached"] == 0,
         f"{m['detached']} detached, gaps {m['gaps'][:8]}"),
        (8, "All nodes one size", len(m["nodeSizes"]) <= 1,
         f"{m['nodeCount']} nodes, sizes {m['nodeSizes']}"),
        (9, "Exactly one Ink Pill", m["pills"] == 1, f"{m['pills']} pills"),
        (10, "Body clears footer, no dead band",
         8 <= dead <= 120 and m["edge"] == 0,
         f"gap {dead}px above footer, {m['edge']} edge breaks"),
    ]

    print(f"\nGREY GATE — {src.name}")
    print("-" * 72)
    passed = 0
    for n, name, ok, detail in rows:
        passed += bool(ok)
        print(f"{n:>3}  {'PASS' if ok else 'FAIL'}  {name:<44} {'' if ok else detail}")
    for i, q in enumerate(JUDGE, start=11):
        print(f"{i:>3}  JUDGE {q}")
    print("-" * 72)
    print(f"MEASURED {passed}/10   grey render -> {out.name}")
    if passed < 10:
        print("Fix the FAILs and re-run. Never show Saman a grey below 15/15.")
    else:
        print("Measured checks clean. Now judge 11-15 on the PNG, then show her.")
    sys.exit(0 if passed == 10 else 1)


if __name__ == "__main__":
    main()
