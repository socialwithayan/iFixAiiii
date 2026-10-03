# CRAFT BENCHMARKS

Numbers from a study of 30+ shipped LinkedIn sheets that consistently win the lightbox, both
animated and static. Structure only: none of their colour, type or wording belongs to Javeriya.

Use these to sanity-check a sheet before the win matrix. A number far outside its band is
usually the real reason a sheet feels off.

---

## The four numbers

| | Benchmark | Javeriya's system |
|---|---|---|
| **Movers per sheet** | 1–2, chrome still | 2: quiet cards arrive, the spotlight ignites ✓ |
| **Words per sheet** | 180–320 typical | Spotlight Grid 164, Versus 194 (footer included) |
| **Colours per sheet** | 5–7 | the stage (3 darks) + white + one fire = 5 ✓ |
| **Loop length** | 5–8 seconds | 9s + 4.5s hold; the hold is the readable rest frame |

**Her sheets run lighter on words than the band**, and that is deliberate: dark-stage sheets
with one lit block read best with space around the light. Do not pad toward 300 words. If a
sheet goes over 260, it probably wants to be two sheets.

## Movers

**Two moving things per sheet. The chrome never moves.**

Hers are fixed: the quiet cards arrive, then the spotlight ignites. That is the budget, fully
spent. A pulsing glow, a shimmering background, a bouncing tag: any third mover makes the sheet
cheaper, not livelier.

## Colours

Count her sheet honestly:

```
Night · Char · Char-2 · White · Fire = 5
```

Ember and Crimson are shades of Fire, so they do not add to the count. A blue link or a green
tick does. That is a sixth colour, and it competes with the one thing that is lit.

## The first frame

**A paused feed shows frame one.** Headline, tag pill and footer are present at `t=0` in her
templates, and the grey gate measures it (check 9). Never animate them in.

The spotlight must **not** be lit in frame one. Its ignition is the payoff of the motion. If
it starts lit, the GIF has nothing to show.

---

## Running the check

```
movers           ___ / 2 max
words            ___ / 150-260 for her
colour families  ___ / 5
loop             ___ / under 8s of motion
frame one        headline + pill + footer visible, spotlight NOT yet lit?   Y / N
```

Outside a band is a question you have to answer, not an automatic fail.
