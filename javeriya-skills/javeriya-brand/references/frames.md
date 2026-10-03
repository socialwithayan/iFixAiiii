# THE FRAME BANK — eight layouts, one spotlight each

Every Javeriya sheet picks one frame. The frame decides the shape; the content decides the frame.
In every frame exactly one block is lit, and the frame decides *which* one.

Geometry is for the locked **1080 × 1350** canvas: content inset 56px left/right, 52px top,
footer at `y=1306`. Usable box: **x 56 → 1024 (968 wide) · y 52 → 1290**.

**Built and tested** templates are marked ✓. The rest are specified here and built on demand
from the nearest built one (see `javeriya-design/templates/README.md`).

---

## 1. SPOTLIGHT GRID ✓ — the workhorse
`templates/spotlight-grid.html`

A 2-column grid of quiet charcoal cards. One is lit.

**Lit:** the one to start with. Tag: "Start here".
**Use when:** 4–6 parallel things: tools, workflows, habits, mistakes.
**Capacity:** 4 or 6 cards. Five leaves a hole; use Hero + Stack instead.

```
Head band   --rh 262   pill · h1 · deck
Grid        2 cols, gap 18, card 474 × 256
Card        numeral (Fraunces 40) top · title + body pushed to the bottom
Spotlight   position 2 (top-right) or 3: never 1, or it is just the first card
Closer      112 tall, Char-2, sentence + Ember figure
```

**Motion:** cards rise in order 0–55% · spotlight ignites 58–82% · closer 84–100%.

---

## 2. VERSUS ✓ — most people vs the top 10%
`templates/versus.html`

Two columns. Left is dimmed on purpose (dashed outline, no fill, muted type); right is solid
charcoal. One right-hand card is lit.

**Lit:** the single change that closes the biggest gap. Tag: "Biggest gap".
**Use when:** a comparison where one side is clearly right.
**Capacity:** 4–6 matched rows. The pairs must match: five left means five right.

```
Labels      "MOST PEOPLE" White-45 · "THE TOP 10%" Ember
Rows        2 cols, column-gap 18, row-gap 14, card 475 × 150
Left        .card.quiet: transparent, 1px dashed rgba(255,255,255,.12)
Right       .card.win: Char, 1px Line
Spotlight   one right-hand card, never the first row
```

**Motion:** left column fades in dim 0–30% · right column slides in 32–62% · spotlight ignites
64–84% · closer 86–100%. You see the problem before you see the fix.

---

## 3. PODIUM — a ranking

A vertical list where #1 is lit and visibly bigger than the rest.

**Lit:** #1. Tag: "#1".
**Use when:** a ranking: best tools, best hooks, top mistakes.
**Capacity:** 5–7 entries.

```
#1          full width, 220 tall, fire, numeral 64px
#2–#n       full width, 104 tall each, Char, numeral 40px White-45, gap 12
            (heights differ on purpose; the grey gate exempts "podium" in the filename)
```

**Motion:** #n up to #2 rise from the bottom 0–55% · #1 lands last and ignites 58–85%.

---

## 4. LADDER — levels and tiers

Rungs stacked bottom to top, each one wider than the one below. The top rung is lit.

**Lit:** the top level, the goal state.
**Use when:** maturity levels, beginner → expert, a growth path.
**Capacity:** 3–5 rungs.

```
Rungs       bottom 620 wide → top 968 wide, centred, 150 tall, gap 14
            (widths differ on purpose; "ladder" in the filename exempts the width check)
Label       Fraunces numeral left of each rung, White-45
```

**Motion:** rungs build bottom→top 0–60% · top rung ignites 62–85%.

---

## 5. HERO + STACK — one big idea

A large lit hero card under the headline carries the claim; quiet cards below support it.

**Lit:** the hero. Tag: "The one that matters".
**Use when:** one strong idea plus 3–4 supporting points.

```
Hero        968 × 300, fire, title 30px, body 18px
Stack       3 cards in a row (310 × 260) or 2×2 (474 × 200), Char
```

**Motion:** hero ignites first 0–30% (it is the point), stack rises 32–80%.
This is the one frame where the spotlight comes first, because here it *is* the headline.

---

## 6. TIMELINE — a journey

Steps left to right in rows of three, joined by thin Line connectors. The turning point is lit.

**Lit:** the step where things changed. Tag: "Turning point".
**Use when:** a 30-day plan, how she grew, a before → after story.
**Capacity:** 5–6 steps.

```
Steps       3 per row, 304 × 230, gap 28, connectors 1px Line between them
Labels      "DAY 1", "WEEK 2"…, 13px caps White-45, above each card
```

The connectors are thin, quiet and broken between rows. They are never a continuous line
threading the whole sheet, because that is another account's signature.

---

## 7. PROMPT STACK — prompts and templates

Cards that hold copy-ready prompts, each in a Night inset well. The best prompt is lit.

**Lit:** the prompt to use if you only use one. Tag: "Use this one".
**Use when:** prompts, scripts, message templates. Her AI audience saves these.
**Capacity:** 3–4 prompts. They are long, so fewer is better.

```
Card        968 wide, 200–240 tall, Char
Well        prompt text in Geist 400 15px White-70 on Night, radius 12, padding 16
Lit card    the well goes rgba(7,6,6,.35) on fire, text stays white
```

---

## 8. CHECKLIST ✓ — an audit
`templates/checklist.html`

7–10 short checks in a single column of slim rows. The most-skipped check is lit.

**Lit:** the one almost everyone skips. Tag: "Most skipped".
**Use when:** a profile audit, a pre-post checklist, a launch list.

```
Row         968 × 84, Char, a 22px check circle (Line ring) left, title 19px
Lit row     fire, the check circle filled white
```

**Motion:** rows tick in 0–60% · the lit row ignites 62–82%.

---

## Picking the frame

| The content is… | Frame |
|---|---|
| several parallel things | Spotlight Grid |
| a comparison with a clear winner | Versus |
| a ranking | Podium |
| levels to climb | Ladder |
| one claim with support | Hero + Stack |
| a journey or plan over time | Timeline |
| prompts or templates | Prompt Stack |
| a list of checks | Checklist |

**If two frames fit, pick the one she shipped least recently.** The log in `/javeriya-design`
holds the history.

**If no frame fits,** the content is not ready. Sharpen it; do not invent a ninth frame to
rescue vague content.
