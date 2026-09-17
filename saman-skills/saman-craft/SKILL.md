---
name: saman-craft
description: "The quality gate and auto-repair engine for Saman Ahmed's designs (@ScaleWthAI). The hard stop before any sheet exports: scores it against the 12-aspect win matrix (hierarchy, spine integrity, density, contrast, type rhythm, alignment, colour ratio, icons, edges, motion, footer, facts), runs the anti-generic gate that catches 'this looks like AI made it', checks the Blue Spine law is honoured, then runs scripts/autofix.py — a measure, fix, re-render, re-measure loop that adjusts row heights, card heights and the headline by itself until every measurement passes, so Saman only ever sees the clean version. It tells the truth when a fault is a design decision rather than a nudge, and refuses to fake a pass. Fire it on '/saman-craft', 'score this sheet', 'is this good enough', 'audit this design', 'fix my sheet', 'why does this look generic', 'run the gate', after a colour build, and always before export. /saman-brand holds the laws it enforces. /saman-design runs the pipeline it sits inside."
---

# SAMAN-CRAFT — the gate

Nothing exports until this passes. Not "nearly", not "she is in a hurry" — the sheets that
get skipped through this gate are the ones that underperform in the feed, and they are always
the ones that looked fine.

Two halves:

1. **Measured** — `scripts/autofix.py` renders the sheet, measures it, and repairs what can be
   repaired by arithmetic.
2. **Judged** — the win matrix. You look at the render and score it. A script cannot tell you
   the hierarchy is wrong.

The laws being enforced live in `/saman-brand`. This skill does not invent rules; it checks
them.

---

## Run the loop first

```bash
python3 scripts/autofix.py <sheet>.html [--max-loops 6]
```

Exit `0` = clean, safe to export. Exit `1` = stuck, and the report says exactly what is wrong.

**What it repairs by itself:**

| Fault | Fix |
|---|---|
| `footer-collision` | body overruns the footer → shrink rows, then the headline, then the cards |
| `dead-space` | >120px of empty above the footer → grow the same, in the same order |
| `overflow` | a card's content is clipped → grow the card box, 12px a loop |
| `ragged-widths` | sibling cards differ in width → force one width |
| `sub12-text` | anything under 12px → raise it to 12px |
| `heading-overflow` | headline wider than its box → step it down 4px at a time, floor 44px |

**What it refuses to touch, and reports instead** — these are decisions, not nudges:

| Fault | Why it is yours |
|---|---|
| `no-spine` | there is no `.spine path`. This is not a Saman sheet yet. |
| `detached-card` | a card is more than 48px off the line with no stub — a layout call |
| `node-off-spine` | a node is not on the line — the geometry is wrong, not the size |
| `pill-count` | zero or two Ink Pills — a copy decision |
| `mixed-nodes` | node sizes differ — pick one and mean it |
| `edge-break` | something crosses the canvas edge — the content is too big for the frame |

It writes fixes back into the **source** file, so the delivered file is the fixed file. Every
edit is announced. Nothing happens silently.

Escalation order matters: whitespace first (free), then the headline (cheap), then card
heights (costs the content room). It never shrinks type to solve a space problem — that is the
fix that makes a sheet unreadable at feed size.

---

## Sanity-check the four numbers

Before the matrix, check the sheet against the shipped-work benchmarks in
**`references/craft-benchmarks.md`**: movers (1–2, chrome still), words (180–320), colour
families (5–7), loop (under 8s), and frame one not being blank. A sheet far outside a band
usually has its real problem there.

## Then score the win matrix

Twelve aspects, scored 1–5 on the rendered PNG. Full criteria and what each score looks like:
**`references/win-matrix.md`**.

| # | Aspect | The question |
|---|---|---|
| 1 | Hierarchy | Does the eye land on the headline, then the structure, then the detail? |
| 2 | Spine integrity | One line, unbroken, everything attached, obvious start and end? |
| 3 | Density | Roughly 60% ground? Does it breathe at phone size? |
| 4 | Contrast | Does every piece of text clear its floor? Is Blue carrying any meaning? |
| 5 | Type rhythm | Consistent scale, no orphan line, no cramped wrap? |
| 6 | Alignment | Does everything sit on the grid, or is something 3px out? |
| 7 | Colour ratio | 60 Sky / 30 fills / 10 Ink? Blue on the spine only, Bright in three places? |
| 8 | Icon discipline | Does every icon add information, or restate the title? |
| 9 | Edge safety | Nothing clipped, nothing crowding the margin? |
| 10 | Motion legibility | Does the spine draw read at feed size, at a glance? |
| 11 | Footer | Locked wording, avatar present, pinned correctly? |
| 12 | Fact integrity | Is every number on the sheet sourced and honest? |

**The bar: no aspect below 4, and 2, 11 and 12 must be 5.** Spine integrity, the footer and
the facts are pass/fail dressed as a score — a 4 on any of them is a fail.

Score honestly. A generous 4 on a weak sheet costs more than the ten minutes of rework it
saves, because it ships.

---

## The anti-generic gate

Ten checks that catch a sheet that looks like every other AI design on the timeline.
Full list and the fix for each: **`references/design-laws.md`**.

The short version — any of these is an automatic fail:

1. Cards floating with no spine
2. An icon on every card that just repeats the title
3. Gradients, glass, glow, or a second shadow
4. A colour outside the named set, or a swapped role (Bright filling, pastel as text)
5. Type below 12px, or more than four sizes on one sheet
6. Filler cards — a seventh item that says nothing
7. Emoji anywhere on the canvas
8. A headline that could sit on anyone's sheet ("Powerful AI Tools You Should Know")
9. Centre-aligned body text
10. **Anything that reads as a neighbouring account's system** — an Object Frame, terracotta,
    a drawn physical object. Her sheet is a line, not a thing.

---

## When it fails

Do not negotiate with the gate. Fix the sheet.

Common faults and the actual fix: **`references/fix-recipes.md`**.

The three that account for most failures:

- **Too much content.** Six cards, not eight. Cut the weakest, do not shrink the type.
- **The spine is decoration.** The line is there but the content does not hang off it. Redraw
  the layout around the line instead of adding a line to a layout.
- **The headline is vague.** No number, no verb, no outcome. That is a content problem and no
  amount of layout fixes it.

## What never happens here

1. Never pass a sheet to "save time". The gate exists because that instinct is wrong.
2. Never edit the laws to make a sheet pass.
3. Never report a score you did not actually check on the render.
4. Never let `autofix` shrink type below 12px — it will not, and neither should you by hand.
5. Never skip fact integrity because the sheet looks good. A wrong number is the one mistake
   that costs her credibility, and credibility is the whole business.
