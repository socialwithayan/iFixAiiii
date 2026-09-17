# BRAND KIT — SAMAN AHMED

Copy-paste CSS. This is the contract every template and every build honours.
Rules and reasoning live in `../SKILL.md` — this file is the values.

---

## The root block

Paste this whole block into every sheet. Do not add a variable to it mid-build; if a sheet
needs a colour that is not here, the sheet is wrong.

```css
:root{
  /* ---- ground & surface ---- */
  --sky:       #EBF6FF;
  --sky-deep:  #DCEEFC;
  --paper:     #FFFFFF;

  /* ---- structure (never text, never large fills) ---- */
  --blue:      #90CAF8;
  --blue-mid:  #6FB6F0;
  --blue-pale: #C9E4FB;

  /* ---- ink ---- */
  --ink:       #051D2F;
  --ink-70:    #40566A;
  --ink-45:    #7D8D9C;

  /* ---- BRIGHT: the one saturated colour. It points, nothing else does ---- */
  --bright:      #F2506A;   /* node rings, the closing figure               */
  --bright-deep: #B0243C;   /* chip text, small emphasis (4.5:1 on --p1)    */

  /* ---- SOFT FILLS: the pastel family. Card backgrounds only ---- */
  --p1: #FFE4DE;   /* peach   */
  --p2: #FFF2D6;   /* cream   */
  --p3: #FFE9F3;   /* rose    */
  --p4: #F4EBFF;   /* orchid  */
  --p5: #E3F2FD;   /* pale sky (Material Blue 50 — her blue's own family)   */

  /* ---- the only shadow ---- */
  --shadow:    0 2px 10px rgba(5,29,47,.07);

  /* ---- space scale ---- */
  --s1: 4px;  --s2: 8px;  --s3: 12px; --s4: 16px;
  --s5: 24px; --s6: 32px; --s7: 48px; --s8: 64px;

  /* ---- radius: soft. Nothing on her sheets has a hard corner ---- */
  --r-card: 20px; --r-panel: 24px; --r-round: 999px;

  /* ---- stroke ---- */
  --w-hair: 1px; --w-ring: 3px; --w-spine: 4px;
}
```

## Fonts

Five weights ship as subset `.woff2` in `assets/fonts/`. The build base64-embeds them via the
`{{INTER_400}}`…`{{INTER_800}}` placeholders, so a finished sheet is one portable HTML file
with no network dependency.

```css
@font-face{font-family:Inter;font-weight:400;font-style:normal;font-display:block;
  src:url({{INTER_400}}) format('woff2')}
@font-face{font-family:Inter;font-weight:500;font-style:normal;font-display:block;
  src:url({{INTER_500}}) format('woff2')}
@font-face{font-family:Inter;font-weight:600;font-style:normal;font-display:block;
  src:url({{INTER_600}}) format('woff2')}
@font-face{font-family:Inter;font-weight:700;font-style:normal;font-display:block;
  src:url({{INTER_700}}) format('woff2')}
@font-face{font-family:Inter;font-weight:800;font-style:normal;font-display:block;
  src:url({{INTER_800}}) format('woff2')}

*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased;
     font-variant-numeric:tabular-nums}
```

`font-display:block` matters: with `swap`, the renderer can screenshot a frame before Inter
loads and ship a sheet set in the fallback.

## Type scale

```css
.h1     {font:800 56px/1.18 Inter; letter-spacing:-.025em; color:var(--ink)}
.deck   {font:500 20px/1.45 Inter; letter-spacing:-.005em; color:var(--ink-70)}
.seclab {font:700 15px/1   Inter; letter-spacing:.08em; text-transform:uppercase; color:var(--ink)}
.ctitle {font:600 20px/1.3  Inter; letter-spacing:-.01em; color:var(--ink)}
.body   {font:400 16px/1.5  Inter; color:var(--ink-70)}
.meta   {font:500 13px/1.4  Inter; letter-spacing:.02em; color:var(--ink-45)}
```

Headline drops to 52px only when the line would otherwise wrap to three lines. Below 52px,
cut words instead.

## The palette in one picture

```
LOCKED           Sky #EBF6FF      Blue #90CAF8     Ink #051D2F
   the ground       the spine        the type

BRIGHT           #F2506A          #B0243C
   points          rings, figure    chip text

SOFT FILLS       #FFE4DE  #FFF2D6  #FFE9F3  #F4EBFF  #E3F2FD
   card backgrounds only, never text, never the spine
```

**Counting colours.** The craft benchmark for this kind of sheet is 5–7 colours. Hers reads as
five: ground, type, spine, bright, and the pastel family — because the five fills sit at the
same value and register as one family, not five decisions. That only holds while they stay
pale. A saturated fill breaks the count and the sheet starts to look busy.

**Roles are not swappable.** Bright never fills a card. A pastel never carries text. Blue never
leaves the spine. That separation is what keeps ten named colours reading as five.

## The Ink Pill

```css
.pill{background:var(--ink); color:var(--sky); border-radius:var(--r-round);
      padding:.08em .42em; letter-spacing:-.01em; white-space:nowrap}
```

Exactly one per sheet, in the headline only.

## The spine

One SVG path in a layer behind the cards.

```css
.spine{position:absolute; inset:0; width:100%; height:100%;
       pointer-events:none; z-index:0}
.spine path{fill:none; stroke:var(--blue); stroke-width:var(--w-spine);
            stroke-linecap:round; stroke-linejoin:round}
.spine .accent{stroke:var(--blue-mid)}
.content{position:relative; z-index:1}     /* cards sit ON the spine */
```

On the Ink canvas the spine goes to `stroke-width:6px` — 4px disappears against `#051D2F`.

## Nodes

```css
.node{width:28px;height:28px;border-radius:var(--r-round);
      background:var(--paper); border:var(--w-ring) solid var(--blue);
      display:grid;place-items:center}
.node.num{background:var(--ink); border-color:var(--ink);
          font:700 15px/1 Inter; color:var(--sky)}
```

All nodes on one sheet are the same size. Always.

## Cards and panels

Cards rotate through the pastel fills down a sheet. Use `--paper` when the content needs to
stay neutral (dense tables, a matrix) and the pastels when the sheet wants warmth.

```css
.card{background:var(--p1); border-radius:var(--r-card);
      border:var(--w-hair) solid rgba(5,29,47,.07);
      box-shadow:var(--shadow); padding:var(--s5)}
.rail > .card:nth-of-type(1){background:var(--p1)}
.rail > .card:nth-of-type(2){background:var(--p2)}
.rail > .card:nth-of-type(3){background:var(--p3)}
.rail > .card:nth-of-type(4){background:var(--p4)}
.rail > .card:nth-of-type(5){background:var(--p5)}

/* BRIGHT does the pointing, and only these three things */
.node{border-color:var(--bright)}
.chip{background:var(--p1); color:var(--bright-deep)}
.verdict .vnum{color:var(--bright)}

.card--neutral{background:var(--paper); border-color:var(--blue-pale)}
.panel{background:var(--paper); border-radius:var(--r-panel);
       border:var(--w-hair) solid var(--blue-pale); padding:var(--s6)}
.well{background:var(--sky-deep); border-radius:var(--r-card); padding:var(--s4)}
.verdict{background:var(--ink); color:var(--sky); border-radius:var(--r-panel);
         padding:var(--s5) var(--s6)}
```

## The three canvases

```css
/* 1. SKY — the default, 8 sheets in 10 */
.canvas.sky{background:var(--sky)}

/* 2. PAPER — dense data, tables, matrices */
.canvas.paper{background:var(--paper);
  background-image:linear-gradient(var(--blue-pale) 1px,transparent 1px),
                   linear-gradient(90deg,var(--blue-pale) 1px,transparent 1px);
  background-size:32px 32px; background-blend-mode:normal; opacity:1}
.canvas.paper .content{--grid-alpha:.4}

/* 3. INK — one sheet in ten, hard-truth topics only */
.canvas.ink{background:var(--ink); color:var(--sky)}
.canvas.ink .card,.canvas.ink .panel{background:rgba(255,255,255,.06);
  border-color:rgba(144,202,248,.32); box-shadow:none}
.canvas.ink .body{color:#B9CBD8}
.canvas.ink .spine path{stroke-width:6px}
.canvas.ink .node{background:var(--ink); border-color:var(--blue)}
```

---

## The DOM skeleton — required by the build scripts

`build.py`, `greygate.py` and `autofix.py` measure by these exact class names. A template that
renames them silently loses its geometry audit and its autofix.

```html
<div class="canvas sky">          <!-- 1080 x 1350, the screenshot target -->
  <svg class="spine">…one path…</svg>
  <div class="content">
    <div class="rowband" id="head" style="--rh:200px">…headline + deck…</div>
    <div class="rowband" id="body" style="--rh:1020px">
      <div class="card">…</div>   <!-- siblings must share a width -->
      <div class="card">…</div>
    </div>
  </div>
  <div class="footer">…</div>      <!-- pinned y=1306, h=44, full width -->
</div>
```

```css
.canvas{position:relative; width:1080px; height:1350px; overflow:hidden}
.content{padding:48px 56px 0}
.rowband{min-height:var(--rh)}
.footer{position:absolute; top:1306px; left:0; right:0; height:44px;
        background:var(--ink); display:flex; align-items:center;
        justify-content:space-between; padding:0 24px}
```

**`--rh` is a min-height, not a fixed height.** That is what lets `autofix.py` grow and shrink
rows to resolve a footer collision or dead space without touching the content.

## The footer markup — locked

```html
<div class="footer">
  <div style="display:flex;align-items:center;gap:10px">
    <img src="{{AVATAR}}" style="width:28px;height:28px;border-radius:999px">
    <span style="font:600 15px Inter;color:var(--sky)">Follow Saman Ahmed For More</span>
  </div>
  <span style="font:600 15px Inter;color:var(--blue)">@ScaleWthAI</span>
</div>
```

## Motion contract

The renderer steps `t` from 0 to 1 and screenshots each frame. **No CSS keyframes** — they do
not advance under a stepped screenshot and the GIF comes out frozen.

```js
window.renderFrame = function(t){          // t in 0..1
  const L = spinePath.getTotalLength();
  const draw = Math.min(1, t/0.36);        // spine draws over the first 36%
  spinePath.style.strokeDasharray  = L;
  spinePath.style.strokeDashoffset = L*(1-ease(draw));
  nodes.forEach((n,i)=>{                   // then nodes land in order
    const start = 0.36 + i*0.055, p = clamp01((t-start)/0.12);
    n.style.opacity   = p;
    n.style.transform = `scale(${0.82+0.18*ease(p)})`;
  });
};
```

Budget: 12–16 seconds total. Spine draw 0–36%, nodes 36–85%, closer 85–100%.

## Quick reference

```
Sky #EBF6FF · Blue #90CAF8 · Ink #051D2F · Inter
Canvas 1080x1350 → exports 2160x2700
One spine · one pill · one shadow · one typeface
60% Sky / 30% Paper / 10% Ink · Blue is structure, not colour
Footer: "Follow Saman Ahmed For More" · @ScaleWthAI
```
