# BRAND KIT — JAVERIYA A.

Copy-paste CSS. This is the contract every template and every build honours. Rules and
reasoning live in `../SKILL.md`; this file is the values.

---

## The root block

```css
:root{
  /* ---- the stage ---- */
  --night:  #070606;                 /* ground: warm near-black, never #000 */
  --char:   #141312;                 /* quiet cards                         */
  --char-2: #1C1A19;                 /* closer strip, raised panels         */
  --line:   rgba(255,255,255,.09);   /* hairlines on charcoal               */

  /* ---- type on dark ---- */
  --white:    #F9F9F9;               /* 17.6:1 on --char */
  --white-70: #BDB8B4;               /*  9.4:1 on --char */
  --white-45: #8C8682;               /*  5.2:1 on --char */

  /* ---- fire: her one colour ---- */
  --fire-red:    #D60802;
  --fire-orange: #FD4F02;
  --ember:       #EE4510;            /* solid midpoint, 5.3:1 on --night */
  --crimson:     #930405;            /* deep wells, pressed states       */
  --fire: linear-gradient(100deg, var(--fire-red) 0%, var(--fire-orange) 100%);
  --glow: 0 18px 60px rgba(238,69,16,.30), 0 0 0 1px rgba(253,79,2,.45);

  /* ---- space, radius ---- */
  --s1:4px; --s2:8px; --s3:12px; --s4:16px; --s5:24px; --s6:32px; --s7:48px;
  --r-card:18px; --r-panel:22px; --r-round:999px;
}
```

## Fonts

```css
@font-face{font-family:Geist;font-weight:400;font-style:normal;font-display:block;src:url({{GEIST_400}}) format('woff2')}
@font-face{font-family:Geist;font-weight:500;font-style:normal;font-display:block;src:url({{GEIST_500}}) format('woff2')}
@font-face{font-family:Geist;font-weight:600;font-style:normal;font-display:block;src:url({{GEIST_600}}) format('woff2')}
@font-face{font-family:Geist;font-weight:700;font-style:normal;font-display:block;src:url({{GEIST_700}}) format('woff2')}
@font-face{font-family:Geist;font-weight:800;font-style:normal;font-display:block;src:url({{GEIST_800}}) format('woff2')}
@font-face{font-family:Fraunces;font-weight:900;font-style:italic;font-display:block;src:url({{FRAUNCES_900I}}) format('woff2')}

*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Geist,system-ui,sans-serif;-webkit-font-smoothing:antialiased;
     font-variant-numeric:tabular-nums}
```

`font-display:block` matters: with `swap`, the renderer can screenshot a frame before the
fonts load and ship a sheet set in the fallback.

The tag pill uses Geist **italic** at 700. Geist has no true italic, so the browser slants it,
which matches the slanted sans in her banner's "Be in the Top 10%". That is deliberate.

## The stage

```css
.canvas{position:relative;width:1080px;height:1350px;overflow:hidden;background:var(--night)}
/* the ember glow: her banner's light streaks, turned down and kept behind */
.canvas::before{content:'';position:absolute;inset:0;pointer-events:none;z-index:0;
  background:radial-gradient(70% 45% at 100% 100%,rgba(214,8,2,.22),transparent 70%),
             radial-gradient(45% 30% at 0% 0%,rgba(253,79,2,.08),transparent 70%)}
.content{position:relative;z-index:1;padding:52px 56px 0}
```

Move the glow's origin to sit behind the spotlight's half of the sheet if that helps the eye,
but keep it one glow. Two glows read as two light sources, and then the sheet has no focus.

## The headline

```css
.h1{font:400 58px/1.06 Geist;letter-spacing:-.035em;color:var(--white)}
.h1 b{font-weight:700}                      /* the subject: bold opens   */
.fire{font-family:Fraunces;font-style:italic;font-weight:900;letter-spacing:-.015em;
      background:var(--fire);-webkit-background-clip:text;background-clip:text;
      color:transparent;padding-right:.08em}  /* the outcome: one per sheet */
```

```html
<h1 class="h1"><b>6 AI Workflows</b> That Get You <span class="fire">Noticed</span> On LinkedIn</h1>
```

Keep `.h1{font:400 NNpx/...}` in exactly that shorthand form: the autofix engine steps the
size down by matching it.

## The tag pill

```css
.pill{display:inline-block;background:var(--fire);color:#fff;border-radius:12px;
      font:italic 700 20px/1 Geist;letter-spacing:-.01em;padding:10px 16px 11px}
```

One at most. It sits above the headline, the way "Be in the Top 10%" sits above hers.

## Cards and the spotlight

```css
.card{position:relative;height:256px;background:var(--char);border:1px solid var(--line);
      border-radius:var(--r-card);padding:26px 28px}

/* THE SPOTLIGHT — exactly one per sheet */
.card.spotlight{background:var(--fire);border-color:transparent;box-shadow:var(--glow)}
.card.spotlight .ctitle,.card.spotlight .body{color:#fff}

.tag{position:absolute;top:24px;right:24px;background:var(--night);color:#fff;
     border-radius:var(--r-round);font:700 12px/1 Geist;letter-spacing:.12em;
     text-transform:uppercase;padding:8px 12px}
```

`.card{...height:NNNpx...}` must keep a literal pixel height: the autofix engine grows and
shrinks cards by matching it.

## The closer

```css
.closer{height:112px;background:var(--char-2);border:1px solid var(--line);
        border-radius:var(--r-panel);padding:0 32px;display:flex;align-items:center;
        justify-content:space-between}
.closer .cnum{font:italic 900 46px/1 Fraunces;color:var(--ember)}
```

---

## The DOM skeleton: required by the build scripts

```html
<div class="canvas">                       <!-- 1080 x 1350, the screenshot target -->
  <div class="content">
    <div class="rowband" id="head" style="--rh:262px">  pill · h1 (with one .fire) · deck </div>
    <div class="rowband" id="body" style="--rh:920px">
      <div class="grid"> .card × n, exactly one .card.spotlight </div>
      <div class="closer"> … </div>
    </div>
  </div>
  <div class="footer"> … </div>            <!-- pinned y=1306, h=44, full width -->
</div>
```

| Class | The scripts check |
|---|---|
| `.canvas` | 1080×1350 |
| `.rowband` | `--rh` is a min-height autofix can grow and shrink |
| `.card` | siblings share a width (Podium and Ladder exempt), nothing overflows |
| `.spotlight` | exactly one, and it is a `.card` |
| `.fire` | exactly one, inside `.h1` |
| `.pill` | at most one |
| `.h1` + `.footer` | fully visible at `t=0`: frame one is never blank |
| `.footer` | top 1306, height 44, full width |

## The footer: locked

```html
<div class="footer">
  <div class="who">
    <img src="{{AVATAR}}" alt="">
    <span class="name">Follow Javeriya A. For More</span>
  </div>
  <div class="dm">DM for <b>collaborations</b>
    <span class="send"><svg width="13" height="13" viewBox="0 0 24 24" fill="#fff">
      <path d="M2.5 11.2 21 3.4c.7-.3 1.4.4 1.1 1.1l-7.8 18.5c-.3.8-1.5.7-1.7-.1l-1.9-7.1-7.1-1.9c-.8-.2-.9-1.4-.1-1.7z"/>
    </svg></span>
  </div>
</div>
```

```css
.footer{position:absolute;top:1306px;left:0;right:0;height:44px;z-index:2;
        background:#0D0B0B;border-top:1px solid var(--line);
        display:flex;align-items:center;justify-content:space-between;padding:0 24px}
.footer .who{display:flex;align-items:center;gap:10px}
.footer img{width:28px;height:28px;border-radius:999px;display:block}
.footer .name{font:600 15px/1 Geist;color:var(--white)}
.footer .dm{display:flex;align-items:center;gap:10px;font:500 13px/1 Geist;
            letter-spacing:.06em;color:var(--white-70);text-transform:uppercase}
.footer .dm b{font-style:italic;font-weight:700;color:var(--fire-orange)}
.footer .send{width:26px;height:26px;border-radius:999px;background:var(--fire);
              display:grid;place-items:center}
```

## Motion contract

The renderer steps `t` from 0 to 1 and screenshots each frame. **No CSS keyframes**: they do
not advance under a stepped screenshot and the GIF comes out frozen.

**Two movers, chrome still.** The cards arrive in quiet, then the spotlight *ignites*: it starts
as a charcoal card and catches fire. The ignition is her motion signature.

```js
window.renderFrame = function(t){            // t in 0..1
  cards.forEach((c, i) => {                  // 1. quiet cards rise
    const p = cl((t - i*0.07) / 0.16);
    c.style.opacity = p;
    c.style.transform = `translateY(${(1-ease(p))*22}px)`;
  });
  const g = ease(cl((t - 0.58) / 0.24));     // 2. the spotlight ignites
  spot.style.background = g < 1
    ? `linear-gradient(100deg, rgba(214,8,2,${g}), rgba(253,79,2,${g})), #141312` : '';
  spot.style.boxShadow = `0 18px 60px rgba(238,69,16,${.30*g}), 0 0 0 1px rgba(253,79,2,${.45*g})`;
};
```

The headline, pill and footer are **never** animated in. A paused feed shows frame one, and
frame one must already be a sheet.

## Quick reference

```
Night #070606 · Char #141312 · White #F9F9F9 · Fire #D60802 → #FD4F02 · Ember #EE4510
Geist 400/700 split headline · one Fraunces 900 italic fire word
Exactly one lit card · fire in four places max · one tag pill max
Canvas 1080x1350 → exports 2160x2700
Footer: "Follow Javeriya A. For More" · "DM for collaborations"
```
