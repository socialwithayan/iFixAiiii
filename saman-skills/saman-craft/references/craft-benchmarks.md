# CRAFT BENCHMARKS

Numbers from a study of 32 shipped designs by two creators who consistently win the LinkedIn
lightbox — 20 animated sheets and 12 static ones. Structure only; none of their colour, type
or wording belongs to Saman.

Use these to sanity-check a sheet before the win matrix. If a number is far outside the band,
that is usually the real reason a sheet feels off.

---

## The four numbers

| | Benchmark | Saman's system |
|---|---|---|
| **Movers per sheet** | 1–2 | 2 — the spine draws, then content lands ✓ |
| **Words per sheet** | 180–320 typical | Rail template ≈ 220 ✓ |
| **Colours per sheet** | 5–7 | 5 families: ground, type, spine, bright, fills ✓ |
| **Loop length** | 5–8 seconds | 9s + 4.5s hold — slightly long, see below |

Her system already lands inside three of four bands. That is not luck — it is what the laws in
`/saman-brand` were built to produce. The value of this file is catching drift.

## Movers — the one that gets broken

**One to two moving things per sheet. The chrome stays still.**

Across all 20 animated designs in the study, not one animated more than two elements. The
frame, the title and the container never move — only the content lands.

Her two movers are the spine drawing and the cards arriving in order. **That is the budget,
fully spent.** Adding a third — a pulsing figure, a rotating icon, a shimmering background —
does not make a sheet livelier, it makes it cheap. This is the most common way a good sheet
gets ruined in the last ten minutes.

## Words — the density band

180–320 words on a normal sheet. The study's outliers are instructive:

- A dense reference wall ran 450–650 words. It works because it is *meant* to be zoomed into
  and saved, not read in the feed.
- A cartoon ran 40–60 words. It works because the picture carries everything.

**Saman's sheets are feed-read, not zoom-read.** Stay in 180–320. Over 400 means the content
wanted to be two sheets.

## Colours — count families, not swatches

5–7 is the band. Sheets that ran 10+ were taxonomy walls where colour *is* the index — every
category needs its own hue to be findable.

Hers is not that. Count her sheet honestly:

```
ground (Sky) · type (Ink) · spine (Blue) · bright (Coral) · the pastel family = 5
```

The five fills count as **one** because they sit at the same value. Saturate one and it stops
being a family member and starts being a sixth colour — and the count is suddenly 9.

## Loop length

5–8 seconds in the study. Hers runs 9s of animation plus a 4.5s hold.

That is deliberate: the hold is the readable rest frame, which is what a scrolling feed
actually shows most of the time. But **if a sheet's motion is not readable inside 8 seconds,
it is too busy** — cut a mover or slow the stagger, do not extend the loop.

## The first frame

The study's sheets all keep their chrome visible from frame one. Hers must too.

**A paused feed shows frame one.** If frame one is nearly empty — spine not drawn, no cards —
the sheet shows a blank rectangle to anyone who does not wait. Headline, deck and footer are
present at `t=0` in her templates for exactly this reason. Never animate them in.

---

## Running the check

```
movers        ___ / 2 max        (spine draw + content land = 2, that is the ceiling)
words         ___ / 180-320
colour families ___ / 5-7
loop          ___ / 8s animation
frame one     headline + deck + footer visible?   Y / N
```

Outside a band is not automatically a fail — it is a question you have to answer. "Why does
this sheet need 400 words?" has a good answer sometimes. It usually does not.
