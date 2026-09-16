# THE SPINE BANK — ten frames

Every Saman sheet picks one. The frame decides the shape of the spine; the content decides
the frame. Geometry below is for the locked **1080 × 1350** canvas with content inset
`56px` left/right, `48px` top, footer at `y=1306`.

Usable content box: **x 56 → 1024 (968 wide) · y 48 → 1290 (1242 tall)**.

Read the law first: `../SKILL.md` §2. One continuous line, everything attached, obvious
start and end.

---

## How to read an entry

- **Spine path** — the actual SVG `d`, ready to paste. Drop it into `<svg class="spine" viewBox="0 0 1080 1350">`.
- **Capacity** — how many content blocks the frame holds before it gets cramped. Going over is
  the most common cause of a failed craft gate.
- **Stub** — where a card sits off the line, a drawn 4px Blue bar joins the two. Draw it from
  the card (a `::before`), never as fixed coordinates in the spine path: hardcoded stubs
  detach the moment a row height changes.
- **Motion** — how the spine draws, in `renderFrame(t)` terms.

---

## 1. RAIL — the workhorse

A single vertical line down the left. Nodes step off it to the right, each carrying a card.

**Use when:** a numbered list of things. Tools, systems, prompts, mistakes, steps.
**Capacity:** 5–9 cards. Seven is the sweet spot. Ten is a different frame.

```
Spine path   M 100 262 L 100 1180
Nodes        x=100, y = 262 + i*((1180-262)/(n-1))
Cards        x 148 → 1024, height (918/n) - 16, vertically centred on its node
Head band    --rh 200px   (headline + deck, full width)
Closer       Ink verdict strip, x 148 → 1024, attached to the spine end at y=1180
```

**Why it works:** the eye reads down the line and the cards are just what hangs off it.
It is the frame that most obviously says *system* with the least effort.

**Motion:** line draws top→bottom 0–36%, nodes pop in order 36–85%, verdict 85–100%.

---

## 2. PIPELINE — before and after

A horizontal line running left→right through stage gates. Cards sit above and below it.

**Use when:** a process with a real start and a real end. "Brief → draft → review → ship."
**Capacity:** 3–5 stages. Four is ideal. Six will not fit at a readable size on 968px.

```
Spine path   M 56 700 L 1024 700
Gates        x = 56 + (i+0.5)*(968/n), y=700, 28px nodes on the line
Cards        alternating: odd stages y 430→672, even stages y 728→970
             width (968/n) - 24, centred on the gate
Head band    --rh 300px
Closer       full-width Ink strip y 1010 → 1130, stub connecting up to the spine
```

**Motion:** line draws left→right 0–40%, gates land in order 40–78%, cards fade with their
gate, closer 85–100%.

---

## 3. LOOP — the thing that repeats

A closed circuit. The line leaves the start, passes every node, and returns to where it began.

**Use when:** a weekly routine, a daily cycle, a feedback loop. Anything where "and then you
do it again" is the point.
**Capacity:** 4–6 nodes. A loop with 8 stops reads as a maze.

```
Spine path   M 250 360 H 830 Q 900 360 900 430 V 1010 Q 900 1080 830 1080
             H 250 Q 180 1080 180 1010 V 430 Q 180 360 250 360 Z
Nodes        distributed around the path, evenly by arc length
Cards        outside the loop on the long sides; the centre stays EMPTY except for
             one Ink hub block (the name of the loop) at 400 520 → 680 920
Head band    --rh 260px
```

**The centre must stay quiet.** A loop with a busy middle loses the shape that makes it a loop.

**Motion:** circuit draws clockwise from the top-left 0–45%, hub fades 45–55%, nodes 55–90%.

---

## 4. RIVER — the journey

An S-curve winding top to bottom. Cards sit on alternating banks.

**Use when:** a timeline, a story, a "how I got from A to B" with 4–6 beats.
**Capacity:** 4–6 beats. The curve needs room to bend; more beats flatten it into a Rail.

```
Spine path   M 300 280
             C 300 430 780 430 780 580
             C 780 730 300 730 300 880
             C 300 1030 780 1030 780 1180
Nodes        at each inflection: (300,280) (780,580) (300,880) (780,1180)
             plus midpoints if 5–6 beats
Cards        on the outside of each bend — left node → card x 56→560,
             right node → card x 520→1024
Head band    --rh 230px
```

**Motion:** the curve draws head to foot 0–45% (this is the best-looking draw in the bank),
beats land as the line passes them 45–90%.

---

## 5. LADDER — levels and tiers

Two vertical uprights with rungs between them. Each rung is a level.

**Use when:** maturity levels, skill tiers, pricing tiers, beginner→expert.
**Capacity:** 3–5 rungs. Five is the ceiling.

```
Spine path   M 170 300 V 1180   M 910 300 V 1180
             (plus one rung per level: M 170 Y H 910)
             — drawn as ONE path with subpaths; it still counts as one spine
Rungs        y = 300 + (i+0.5)*(880/n)
Cards        sit ON the rung, x 200 → 880, height (880/n) - 20
Level badge  Ink numbered node on the LEFT upright at each rung height
Head band    --rh 250px
```

Bottom rung is the goal state and carries the Ink treatment. The climb has to have a top.

**Motion:** uprights draw bottom→top 0–30%, rungs fill in bottom→top 30–80%, top rung's Ink
card lands last 80–100%. Climbing upward reads better than falling downward.

---

## 6. FORK — the decision

One line that splits into two paths and does not rejoin.

**Use when:** a this-or-that. "Do it manually / build the system." Two outcomes, one choice.
**Capacity:** 2 paths × 3–4 points each.

```
Spine path   M 540 300 V 520
             M 540 520 C 540 620 300 620 300 720 V 1180
             M 540 520 C 540 620 780 620 780 720 V 1180
Split node   540,520 — the biggest moment on the sheet, Ink filled, labelled
Path nodes   x=300 and x=780, y = 780 + i*130
Cards        left path x 56→520, right path x 560→1024
Head band    --rh 240px
Closer       two Ink outcome strips at the foot of each path, y 1120→1180
```

The two outcomes must be **genuinely different lengths of good** — a fork where both sides
are fine is not a fork.

**Motion:** trunk draws 0–20%, split flashes 20–26%, both branches draw simultaneously
26–60%, points land 60–92%.

---

## 7. TWO-STATE BOARD — manual vs system

One vertical line splitting the canvas into a left state and a right state.

**Use when:** before/after, manual vs automated, what most founders do vs what works.
**Capacity:** 4–7 paired rows. Pairs must match — if the left has six items the right has six.

```
Spine path   M 540 300 V 1240
Node         one Ink node at 540,300 carrying the divider label ("vs")
Rows         y = 320 + i*((920)/n), each row a matched pair
Cards        left  x 56 → 512   (the manual way — Sky-deep wells, --ink-70 text)
             right x 568 → 1024 (the system way — Paper cards, --ink text, blue rings)
Head band    --rh 250px
```

**The asymmetry is the argument.** Left side is flatter and quieter; right side is Paper,
ringed and crisp. The reader should feel which side wins before reading a word.

**Motion:** divider draws top→bottom 0–30%, left rows fade in 30–58%, right rows land with a
small scale pop 58–92%.

---

## 8. FUNNEL — cutting down

A line that narrows through stages.

**Use when:** filtering, qualifying, "100 tools → 5 that matter."
**Capacity:** 3–5 stages, always ending in one.

```
Spine path   M 140 330 L 420 1160 M 940 330 L 660 1160
             (two converging lines, one path with subpaths)
Stages       horizontal bands between the walls, y = 330 + i*(830/n)
Cards        inset 24px from the walls at that y — so each card is NARROWER than
             the one above it. This is the whole point; do not equalise them.
Head band    --rh 280px
Closer       the survivor, Ink block at the neck, x 420→660, y 1180→1250
```

Card widths shrinking down the sheet is the one place the equal-width law is suspended —
`/saman-craft` knows about this frame and will not flag it.

**Motion:** both walls draw downward 0–40%, bands fill top→bottom 40–86%, survivor 86–100%.

---

## 9. ORBIT — one hub, many satellites

A ring with a hub in the middle and satellites sitting on the ring.

**Use when:** one core tool or idea with things connected to it. "Claude + the 6 connectors."
**Capacity:** 5–8 satellites.

```
Spine path   M 540 340 A 260 260 0 1 1 539.9 340 Z      (r=260, centre 540,600)
Hub          Ink circle r=96 at 540,600 — the one thing everything connects to
Spokes       hub → each satellite node, 4px --blue, part of the same spine layer
Satellites   node at angle θ = -90° + i*(360/n), on the ring
Cards        outside the ring, radially placed; the lower third of the canvas
             (y 900 → 1250) carries a full-width Paper panel for the detail
Head band    --rh 260px
```

If the satellites need more than one line of text each, use Rail instead — Orbit is for short
labels and a strong centre.

**Motion:** ring draws from 12 o'clock clockwise 0–40%, hub scales in 40–50%, spokes shoot out
with their satellite 50–92%.

---

## 10. CLOCK — the time-boxed day

A vertical line marked out in time blocks of proportional height.

**Use when:** a schedule, a routine, a 30-minute setup, a day plan.
**Capacity:** 4–7 blocks.

```
Spine path   M 200 300 V 1220
Ticks        a 20px --blue-mid stub left of the spine at every block boundary
Blocks       height PROPORTIONAL to the real duration — a 10-min block is half the
             height of a 20-min block. This is the frame's honesty rule.
Time label   left of the spine, x 56→180, .meta, tabular-nums, right-aligned
Cards        x 248 → 1024
Head band    --rh 230px
```

Proportional heights are not optional. A clock where every block is the same size is a Rail
wearing a watch.

**Motion:** line draws top→bottom with ticks appearing as it passes 0–40%, blocks fill in time
order 40–90%.

---

## Picking the frame

Ask what shape the content already is:

| The content is… | Frame |
|---|---|
| a countable list | Rail |
| a process with an end | Pipeline |
| something that repeats | Loop |
| a journey over time | River |
| levels to climb | Ladder |
| a choice between two | Fork |
| a comparison of two states | Two-State Board |
| a filter down to a few | Funnel |
| one thing with many parts | Orbit |
| a schedule | Clock |

**If two frames fit, pick the one she shipped least recently.** The log in `/saman-design`
holds the history. Rail is the default and will quietly eat the rotation if nobody checks.

**If no frame fits,** the content is not ready — go back and sharpen it. Do not invent an
eleventh frame to rescue vague content. New frames get added to this bank deliberately, with
geometry, not improvised mid-build.
