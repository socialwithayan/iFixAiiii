# DESIGN LAWS — the anti-generic gate

Ten checks that catch a sheet that looks like every other AI design on the timeline.
Any single fail is a fail. Each law is here because it is a specific way a sheet stops being
hers and starts being wallpaper.

---

### 1. No floating cards
**Fail:** a grid of cards with no line connecting them.
**Why:** that is the default AI infographic. It is the shape every template tool produces.
**Fix:** the spine is not decoration added to a layout — the layout is built around the line.
If the content does not hang off a line, pick a different frame from the Spine Bank.

### 2. No icon that restates the title
**Fail:** an envelope icon on the card titled "Inbox triage".
**Why:** it is the fastest tell of a generated design. It fills space and adds nothing.
**Fix:** delete it. An icon earns its place by adding information — a state, a direction, a
count — or it does not appear. No icons at all is a correct answer.

### 3. No gradients, glass, glow, or a second shadow
**Fail:** a gradient card, a frosted panel, a soft glow behind a number, stacked elevation.
**Why:** her system gets its depth from one hairline and one shadow. Everything else is 2021.
**Fix:** `--shadow` on Paper panels. Nothing else. Ever.

### 4. No colour outside the named set, and no swapped roles
**Fail:** a hex that is not one of the three locked, the two brights, or the five fills. Or a
role swap — Bright filling a card, a pastel carrying text, Blue leaving the spine.
**Why:** the set is deliberately wide enough to be warm and narrow enough to stay one brand.
It only reads as five colours while the fills stay pale and the roles stay separate. A
saturated fill or a Bright card breaks both at once.
**Fix:** meaning is carried by weight, fill and position — not by inventing a hue. The system
way is a warm pastel card; the manual way is a flat Sky-deep well. That contrast reads
instantly with no new colour.

**Count it:** at most one Bright per role on a sheet — rings, chip text, closing figure. Three
places. A fourth is decoration.

### 5. No type below 12px, no more than four sizes
**Fail:** an 11px caption. Seven different sizes on one canvas.
**Why:** 12px is the floor at feed scale. More than four sizes is not hierarchy, it is drift.
**Fix:** cut words. Never shrink type to fit — the autofix will not do it and neither should you.

### 6. No filler cards
**Fail:** a seventh item that exists because six looked odd.
**Why:** a reader finds the weak one immediately and it discounts the rest.
**Fix:** six good cards. The sheet is as long as the content is, not as long as the frame allows.

### 7. No emoji on the canvas
**Fail:** any emoji, anywhere, at any size.
**Why:** it is not her register, and it renders differently on every device.
**Fix:** delete. If it was carrying meaning, that meaning needs words or a node.

### 8. No anonymous headline
**Fail:** "Powerful AI Tools Every Founder Should Know."
**Why:** it could sit on anyone's sheet. A headline that works for anyone works for no one.
**Fix:** one number, one verb, one outcome. If you can swap her name for a competitor's and
the headline still fits, it is not a headline yet.

### 9. No centre-aligned body text
**Fail:** a centred paragraph inside a card.
**Why:** ragged left edges destroy the scan, which is the only thing a cheatsheet is for.
**Fix:** left-align everything except a single figure in a closer.

### 10. Nothing that reads as a neighbouring account's system
**Fail:** an Object Frame (the sheet drawn as a phone, a folder, a terminal, a receipt),
terracotta or orange, a navy ground by default, a brand-coloured pill word.
**Why:** each of those is the signature of a larger account in an adjacent niche. Borrowing one
makes her look derivative of the thing she is competing with.
**Fix:** her sheet is a **line**, not a **thing**. Her pill is Ink on light, and that inversion
is deliberate.

---

## Running the gate

Score each law PASS / FAIL on the render. One FAIL stops the export.

```
1  floating cards        PASS / FAIL
2  redundant icons       PASS / FAIL
3  gradients & glass     PASS / FAIL
4  fifth colour          PASS / FAIL
5  type floor & scale    PASS / FAIL
6  filler cards          PASS / FAIL
7  emoji                 PASS / FAIL
8  anonymous headline    PASS / FAIL
9  centred body          PASS / FAIL
10 someone else's system PASS / FAIL
```

## The test behind all ten

**Cover the footer. Could this be anyone's sheet?**

If yes, the sheet has failed regardless of what the checks said. The spine, the Ink Pill and
the air are supposed to make that question answer itself.
