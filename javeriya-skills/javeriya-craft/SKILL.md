---
name: javeriya-craft
description: "The quality gate and auto-repair engine for Javeriya A.'s designs (the trusted voice in AI and tech on LinkedIn). The hard stop before any sheet exports. It scores the sheet against the 12-aspect win matrix (hierarchy, spotlight earned, stage, contrast, type split, alignment, fire budget, icons, edges, motion, footer, facts) and runs the anti-generic gate that catches 'this looks like AI made it'. It also checks the Spotlight law (exactly one lit block, exactly one fire word in the headline), then runs scripts/autofix.py: a measure, fix, re-render, re-measure loop that adjusts row heights, card heights and the headline by itself until every measurement passes, so Javeriya only ever sees the clean version. It says plainly when a fault is a design decision rather than a nudge, and never fakes a pass. Fire on '/javeriya-craft', 'score this sheet', 'is this good enough', 'audit this design', 'fix my sheet', 'why does this look generic', 'run the gate', after a build, and always before export."
---

# JAVERIYA-CRAFT — the gate

Nothing exports until this passes. The sheets that slip through on "nearly" are the ones the
feed ignores, and they are always the ones that looked fine at a glance.

Two halves:

1. **Measured**: `scripts/autofix.py` renders the sheet, measures it and repairs what can be
   repaired by arithmetic.
2. **Judged**: the win matrix. You look at the render and score it.

The laws being enforced live in `/javeriya-brand`. This skill checks them; it does not invent
them.

---

## Run the loop first

```bash
python3 scripts/autofix.py <sheet>.html [--max-loops 6]
```

Exit `0` = clean, safe to export. Exit `1` = stuck, and the report names exactly what is wrong.

**What it repairs by itself:**

| Fault | Fix |
|---|---|
| `footer-collision` | body overruns the footer → shrink rows, then the headline, then the cards |
| `dead-space` | >120px empty above the footer → grow the same, in the same order |
| `overflow` | a card's content is clipped → grow the card, 12px a loop |
| `ragged-widths` | sibling cards differ in width → force one width |
| `sub12-text` | anything under 12px → raise it to 12px |
| `heading-overflow` | headline wider than its box → step down 4px, floor 44px |

**What it refuses to touch**, because these are decisions, not nudges:

| Fault | Why it is yours |
|---|---|
| `spotlight-count` | zero or two lit blocks. Deciding what matters most is the whole design. |
| `fire-count` | the fire word is missing, doubled, or outside the headline. A copy decision. |
| `pill-count` | more than one tag pill. Pick the one that says it. |
| `edge-break` | something crosses the canvas edge. The content is too big for the frame. |

Every fix is written back into the **source** file and announced. Escalation runs whitespace
first, then the headline, then card heights. It never shrinks type to solve a space problem.

---

## Check the four numbers

Before the matrix, check the sheet against the shipped-work bands in
**`references/craft-benchmarks.md`**: movers (2), words (150–300), colour (one fire + the stage),
loop (under 8s of motion), frame one not blank.

## Then score the win matrix

Twelve aspects, 1–5, on the rendered PNG. Full criteria: **`references/win-matrix.md`**.

| # | Aspect | The question |
|---|---|---|
| 1 | Hierarchy | Headline, then the spotlight, then the rest, without effort? |
| 2 | Spotlight earned | Exactly one lit block, and is it the right one? Does it win in grey? |
| 3 | Stage | Dark, clean, the glow behind and never muddying text? |
| 4 | Contrast | Every text clears its floor? Anything on fire is 19px bold or larger? |
| 5 | Type split | Bold subject, regular promise, one fire word, and is it the outcome word? |
| 6 | Alignment | Card edges, numerals and baselines exactly on the grid? |
| 7 | Fire budget | Gradient in four places at most? No fire on body text? |
| 8 | Icon discipline | Every icon adds information, or there are none? |
| 9 | Edge safety | Nothing clipped, nothing crowding the margins? |
| 10 | Motion | Frame one is a full sheet; the ignition reads at feed size? |
| 11 | Footer | Her photo, locked wording, DM line, pinned correctly? |
| 12 | Fact integrity | Every claim, model name, price and stat checked this run? |

**The bar: nothing below 4, and 2, 11 and 12 must be 5.** The spotlight, the footer and the
facts are pass/fail wearing a score.

---

## The anti-generic gate

Ten checks that catch a sheet that looks like every other AI graphic on the feed. Full list
with fixes: **`references/design-laws.md`**. Any one is a fail:

1. No spotlight, or more than one
2. An icon on every card that restates its title
3. Neon outlines, glassmorphism, or glow on anything but the spotlight
4. A second accent colour: blue, green, purple, anything but fire
5. Type under 12px, or more than five sizes
6. A filler card that says nothing
7. Emoji on the canvas
8. A headline that could sit on anyone's sheet
9. A light canvas
10. A device that reads as a neighbouring account's system: a line threading the cards,
    pastel card families, or the sheet drawn as a physical object

## When it fails

Do not negotiate with the gate. Fix the sheet. Common faults and their real fixes:
**`references/fix-recipes.md`**.

## What never happens here

1. Never pass a sheet to save time.
2. Never edit the laws to make a sheet pass.
3. Never score from memory; open the PNG.
4. Never let type go under 12px to make something fit.
5. Never skip fact integrity because the sheet looks good. "The trusted voice in AI & Tech"
   is the business, and one wrong number spends it.
