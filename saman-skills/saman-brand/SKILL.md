---
name: saman-brand
description: "Saman Ahmed's locked visual brand system for cheatsheets and infographics (@ScaleWthAI — AI systems and workflows for busy founders). The frozen reference every other Saman skill reads: her four brand tokens (Sky #EBF6FF, Blue #90CAF8, Ink #051D2F, Inter), THE BLUE SPINE law that makes a sheet hers, the Ink Pill headline device, the 60/30/10 colour ratio, the three canvases, the Inter-only type and spacing scales, the ten-frame Spine Bank, her design-note format, her locked footer, and the do-not list that stops a sheet drifting into generic AI design or into somebody else's system. This skill never builds and never renders — it is the spec. Fire it on '/saman-brand', 'my style', 'my brand', 'brand kit', 'what are my colours', 'is this on brand', 'frame ideas', 'design notes', 'what font', 'spine law', or whenever a design needs her rules before anything is drawn. /saman-design runs the pipeline. /saman-craft scores the result."
---

# SAMAN-BRAND — the locked style system

**Saman Ahmed · @ScaleWthAI · "AI systems and workflows for busy founders."**

This is the frozen reference. `design-note` picks, builds, gates and exports all read it.
It does not render anything. If you are here to *make* a sheet, go to `/saman-design`.

**Rule zero: nothing in this file is a suggestion.** If a build breaks a law here, the build
is wrong, not the law.

---

## 1. The four tokens

Everything on every sheet is made of these four things. There is no fifth colour and no
second typeface.

| Token | Hex | What it is for |
|---|---|---|
| **Sky** | `#EBF6FF` | the ground. The canvas, the page, the air between things. |
| **Blue** | `#90CAF8` | **structure only.** The spine, rules, borders, node rings, arrows. |
| **Ink** | `#051D2F` | type, and the one dark element per sheet. |
| **Paper** | `#FFFFFF` | panel fills that sit on Sky. Not a brand colour — a surface. |

Derived tints. Use these named values, never eyeball a new one:

```css
:root{
  --sky:      #EBF6FF;   /* ground                                   */
  --sky-deep: #DCEEFC;   /* ground, one step down: alt rows, wells   */
  --paper:    #FFFFFF;   /* panel surface                            */
  --blue:     #90CAF8;   /* the spine, structure                     */
  --blue-mid: #6FB6F0;   /* spine emphasis, active node, arrowheads  */
  --blue-pale:#C9E4FB;   /* hairlines, dividers, grid, ghost states  */
  --ink:      #051D2F;   /* type, the dark element                   */
  --ink-70:   #40566A;   /* body text on Sky, labels                 */
  --ink-45:   #7D8D9C;   /* captions, meta, footer secondary         */
  --shadow:   0 2px 10px rgba(5,29,47,.07);   /* the ONLY shadow     */
}
```

**Contrast floors, non-negotiable.** `--ink` on `--sky` = 15.4:1. `--ink-70` on `--sky` = 6.2:1.
`--ink-45` is for text at 14px+ only and never for anything that carries meaning.
`--blue` on `--sky` is 1.5:1 — which is exactly why **Blue never carries text and never carries
meaning on its own.** It is a shape. If a reader has to read the blue, the sheet is broken.

---

## 2. THE BLUE SPINE — her signature law

> **Every sheet has exactly one continuous Blue line, and every piece of content is attached
> to it. The spine bends. The spine never breaks. Nothing floats free of it.**

This is the single thing that makes a design hers at a glance in the feed. Her whole brand
is *systems and workflows* — a spine draws a system as a system. A reader should be able to
put a finger on the start of the line and trace the entire sheet without lifting it.

**What the spine actually is:** a 4px `--blue` stroke (6px on the Ink canvas) that enters the
content area, passes every node in reading order, and exits or closes. Drawn as one SVG
`<path>` in the `.spine` layer behind the cards, so a card can sit on it without a seam.

**The three tests a sheet must pass:**

1. **Continuity.** One path. Trace it start to end without lifting. Gaps are only legal where
   a card body deliberately crosses the line, and the line resumes on the other side.
2. **Attachment.** Every card, stat, or block touches the spine, or hangs off it by a drawn
   stub of at most 48px — a visible 4px Blue bar, never empty space. Draw the stub from the
   card itself (a `::before`), not as fixed coordinates in the spine path, or it detaches the
   moment a row height changes. A card floating in the middle of nowhere is the one failure
   that makes a Saman sheet look like everyone else's.
3. **Direction.** The spine has an obvious start and an obvious end. A reader knows where to
   begin without being told.

**What the spine is not:** a decorative squiggle in the background, a border around the whole
canvas, or a divider between unrelated sections. Those are wallpaper. The spine is the
skeleton the content hangs on.

**Node rules.** Where content joins the spine, put a node: a `--paper` filled circle with a
3px `--blue` ring, 28px on a standard sheet. Numbered nodes use `--ink` fill with `--sky`
numerals. Nodes are always the same size on one sheet — a bigger node means a bigger idea,
and if all your ideas are the same size, all your nodes are the same size.

---

## 3. The Ink Pill

**One word of the headline sits in a filled `--ink` pill with `--sky` text.** Exactly one, on
every sheet, never two.

On a light sheet the darkest object on the page is a promise about where to look. Spend it on
the word the whole sheet is about — the number, the verb, the outcome. Never on a filler word.

```
The 7 Systems That Save Founders [ 10 HOURS ] A Week
                                  ^^^^^^^^^^
                                  ink pill, sky text
```

Pill spec: `--ink` background, `--sky` text, radius 999px, padding `.08em .42em`, same font
size and weight as the headline around it, letter-spacing `-0.01em`.

**The pill is not a highlighter.** It does not appear in body text, in card titles, or twice.
If a second phrase needs emphasis, it gets `--ink` weight 700 and no pill.

---

## 4. The 60 / 30 / 10 ratio

Measured by area of the finished canvas:

- **60% Sky** — the ground. Air is the brand. A cramped Saman sheet is off-brand even if every
  colour is right.
- **30% Paper** — the panels the content actually lives in.
- **10% Ink** — type, the pill, the footer, numbered nodes.
- **Blue is not in the ratio.** It is structure: strokes, rings, hairlines. If Blue is filling
  a large area, you have used it as a colour instead of as a line. Fix it.

Practical floor: at least 90px of clear Sky across the top of the content area, and at least
40px of Sky gutter on the left and right of every card.

---

## 5. The three canvases

| Canvas | Ground | When |
|---|---|---|
| **Sky** | `--sky` | the default. Eight sheets in ten. |
| **Paper** | `--paper` + a `--blue-pale` 32px grid at 40% | dense data, tables, comparison matrices. The grid gives dense content something to sit on. |
| **Ink** | `--ink` | rare. One sheet in ten, for a hard-truth or "stop doing this" topic. Spine goes `--blue` 6px, panels go `rgba(255,255,255,.06)`, text goes `--sky`. |

The Ink canvas is a **change of register, not a dark mode**. If she starts shipping Ink sheets
weekly it stops meaning anything, so the rule is one in ten and it has to earn it.

---

## 6. Type — Inter, and only Inter

One family. Every weight comes from the five bundled `.woff2` files in `assets/fonts/`.

| Role | Size | Weight | Tracking | Colour |
|---|---|---|---|---|
| Headline | 52–60px | 800 | −0.025em | `--ink` |
| Deck / subtitle | 20px | 500 | −0.005em | `--ink-70` |
| Section label | 15px | 700 | +0.08em, UPPERCASE | `--ink` |
| Card title | 20px | 600 | −0.01em | `--ink` |
| Body | 16px | 400 | 0 | `--ink-70` |
| Meta / caption | 13px | 500 | +0.02em | `--ink-45` |
| Node numeral | 15px | 700 | 0 | `--sky` on `--ink` |

**Line height:** 1.18 on the headline, 1.5 on body, 1.3 on card titles.
**Nothing renders below 12px, ever.** If it does not fit at 12px, cut words, do not shrink type.

**Tabular numerals are mandatory on every figure** — `font-variant-numeric: tabular-nums`.
Her content is full of numbers and hours and percentages; they have to align in a column.

**Banned:** italics (Inter's italic is not bundled and the synthetic slant looks cheap), any
second family, letter-spacing on body text, all-caps on anything longer than four words.

---

## 7. Space, radius, stroke

```
Spacing scale (px):   4 · 8 · 12 · 16 · 24 · 32 · 48 · 64      (nothing in between)
Radius:               card 14 · panel 18 · node 999 · pill 999
Stroke:               hairline 1 (--blue-pale) · spine 4 (--blue) · node ring 3 (--blue)
Canvas margins:       56 left/right · 48 top · footer pinned at y=1306
```

**One shadow only** (`--shadow`), on Paper panels sitting on Sky. Never on the Ink canvas,
never on a node, never stacked. Elevation is not a design system — the spine is.

---

## 8. The Spine Bank — ten frames

Every sheet picks one frame. The frame decides the shape of the spine; the content decides
which frame. Ten is enough to never repeat inside a month.

| # | Frame | The spine is | Use when the content is |
|---|---|---|---|
| 1 | **Rail** | one vertical line down the left, nodes stepping right | a numbered list, 5–9 items, the default workhorse |
| 2 | **Pipeline** | a horizontal line left→right with stage gates | a process with a clear before and after |
| 3 | **Loop** | a closed circuit that returns to its start | a weekly or daily cycle, something that repeats |
| 4 | **River** | an S-curve winding top to bottom, cards on alternating banks | a journey or timeline with 4–6 beats |
| 5 | **Ladder** | two uprights with rungs between them | levels, tiers, a maturity or skill climb |
| 6 | **Fork** | one line that splits into two paths | a decision, a this-or-that, a branch point |
| 7 | **Two-State Board** | one vertical line splitting the canvas | manual way vs system way, before vs after |
| 8 | **Funnel** | a line narrowing through stages | filtering, qualifying, cutting down |
| 9 | **Orbit** | a ring with a hub, satellites on the ring | one core tool with things connected to it |
| 10 | **Clock** | a line marked out in time blocks | a schedule, a day plan, a time-boxed routine |

Full geometry, node counts and content capacity for each frame:
**`references/spine-frames.md`**.

**The repeat rule:** never ship the same frame twice in a row, and never three times in one
week. The log in `/saman-design` tracks what shipped. Rail is the workhorse and will drift to
overuse if nobody is watching it.

---

## 9. The footer — locked

Pinned at `y=1306`, height `44px`, full canvas width, `--ink` background.

```
[avatar 28px circle]  Follow Saman Ahmed For More            @ScaleWthAI
        ^                      ^                                  ^
   assets/saman-avatar.png   --sky, Inter 600, 15px        --blue, Inter 600, 15px
```

The wording does not change. Not per sheet, not per topic, not per platform.
A locked footer is what makes forty sheets read as one body of work.

**Her avatar:** `assets/saman-avatar.png` ships as an "SA" monogram placeholder.
**To use her real face:** replace that file with a square PNG, 300×300 or larger, and every
skill picks it up automatically on the next build. Nothing else to change.

---

## 10. The design note — the format she approves

Before anything is drawn, a sheet is described in plain English in exactly this shape. If a
design note cannot be written, the sheet is not ready to build.

```
FRAME     Rail
CANVAS    Sky
HEADLINE  The 7 Systems That Save Founders [10 HOURS] A Week
PILL      10 HOURS
SPINE     enters top-left, runs straight down, 7 nodes, exits into the verdict block
NODES     7, numbered
CARDS     7 · title + 2 lines each · Paper panels stepping right off the spine
CLOSER    one Ink verdict strip at the foot, attached to the spine end
MOTION    spine draws top to bottom 0-4s, nodes pop in sequence 4-9s, verdict lands 9-11s
WHY       a straight countable list of systems — the reader wants to scan and save
```

Three notes per topic, three different frames, so she picks a shape and not a coin flip.
The full format and worked examples: **`references/design-note-format.md`**.

---

## 11. The do-not list

These exist because each one is a specific way a sheet stops being hers.

**Brand**
1. No colour outside the four tokens and their named tints. No red, no green, no gradient.
2. No second typeface. Inter does all of it.
3. Blue never carries text, and never fills a large area.
4. Never two Ink Pills. Never zero.
5. Never edit the footer wording.

**Structure**
6. Never a sheet without a spine. A grid of cards with no line is not a Saman sheet.
7. Never a broken spine or a floating card.
8. Never mixed node sizes on one sheet.
9. Never a card width that differs from its siblings.
10. Never below 12px, and never fix an overflow by shrinking type before cutting words.

**Not somebody else's system**
11. **No Object Frame.** The sheet is never drawn as a physical object — not a phone, a
    folder, a receipt, a terminal window, a notebook. That is Ayan's signature and it is the
    single fastest way to make her look derivative. Her sheet is a *line*, not a *thing*.
12. No terracotta, no orange, no deep navy ground pretending to be Ink. Her Ink is `#051D2F`
    and it is used sparingly on light, not as a dark canvas by default.
13. No brand-coloured Pill Word in Blue — hers is Ink, and that inversion is the point.

**Not generic AI design**
14. No stock 3D blobs, no glassmorphism, no neon glow, no drop shadows on everything.
15. No icon on a card that just restates the title. An icon earns its place by adding
    information or it does not appear.
16. No emoji anywhere on the canvas.
17. No filler. If a card has nothing to say, the sheet has six cards, not seven.

---

## 12. Reading order for the other skills

- Building a sheet → `/saman-design` (it reads this file first, then the frame bank)
- Scoring or fixing a sheet → `/saman-craft` (it enforces sections 2, 4, 6, 7, 11)
- Picking a layout → `references/spine-frames.md`
- Writing the note she approves → `references/design-note-format.md`
- Every token, in copy-paste CSS → `references/brand-kit.md`
