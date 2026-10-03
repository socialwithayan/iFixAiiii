# STYLE KIT — component variants

The Spine Bank decides the *shape* of a sheet. This file decides how the parts inside it look.

Ten frames × these variants is why forty sheets can share one system without forty sheets
looking identical. **Every variant here already obeys the laws** — the palette, the type scale,
the soft radii. Mixing them cannot take a sheet off-brand.

Pick one variant per component per sheet. Do not mix two card styles on one sheet.

---

## Headers — 5 variants

**H1 · Stacked** *(default)*
Headline, then deck under it. Full width. Nothing else.
→ Use when the headline is the whole hook.

**H2 · Headline + counter**
Headline left, a large Ink figure right (`72px/800`, tabular). The number the sheet is about.
→ Use when there is one dominant figure: "10 hrs", "£4,200", "40×".

**H3 · Headline + two column labels**
Headline, deck, then a label row that names the two sides.
→ The Two-State Board's header. Also works on Fork.

**H4 · Eyebrow + headline**
A `.seclab` eyebrow above the headline ("THE FRIDAY PROBLEM"), then headline, then deck.
→ Use when the topic needs one line of framing before the claim lands.

**H5 · Headline bar**
Line one plain Ink, line two inside a full-width Ink bar in `--sky` caps.
→ Use when the whole second line is the claim, not one word of it. Heavier and more
declarative than the inline pill. **Pill or bar, never both on one sheet.**

---

## Cards — 6 variants

**C1 · Tonal family** *(default)*
Pastel fill, 2px border in the same hue one step deeper, card title in that family's name
tone, soft shadow. Cards rotate through the five families down the sheet.
→ The workhorse, and the variant that carries most of the craft.

**C2 · Neutral**
`--paper` fill, `--blue-pale` hairline.
→ Dense content, tables, matrices — anywhere the pastels would add noise to data.

**C3 · Quiet well**
`--sky-deep` fill, no border, no shadow.
→ The losing side of a comparison. Flat on purpose.

**C4 · Ink**
`--ink` fill, `--sky` text. One per sheet, at the end of the spine.
→ The closer. Never more than one.

**C5 · Split card**
Tonal fill, with a strip down the right third in the same family's edge tone, holding a figure
or a before-value.
→ Use when every card carries a number worth isolating.

**C6 · Dense tile**
Tonal family card at half height, no body copy — title plus one line. Six to nine in a grid.
→ For a reference sheet people will save and zoom. Density is the point; keep the tonal
borders or it turns into a wall.

---

## Node styles — 3 variants

**N1 · Numbered** *(default)*
`--ink` fill, `--sky` numeral, `--bright` ring. 28px.
→ Anything ordered.

**N2 · Open**
`--paper` fill, `--bright` ring, empty. 28px.
→ Unordered stops, or the terminal node at the end of a spine.

**N3 · Icon**
`--paper` fill, `--bright` ring, one 14px Ink glyph.
→ Only when the icon adds information the title does not. If it restates the title, use N1.

All nodes on one sheet are the same size and the same variant. Always.

---

## Chips — 3 variants

**P1 · Stat chip** *(default)*
`--paper` fill, `--bright-deep` text, uppercase 13px/600, pill radius. "SAVES 2.5 HRS".

**P2 · Tag**
`--sky-deep` fill, `--ink-70` text, same shape. Category or tool name, no emphasis.

**P3 · Bare figure**
No chip. Just the number in `--bright-deep`, 20px/700, tabular.
→ When every card has a figure and five chips would be five blobs.

---

## Closers — 4 variants

**X1 · Verdict strip** *(default)*
Ink block, sentence left, big `--bright` figure right.

**X2 · Total bar**
Ink block, a row of the sheet's figures adding to one total.
→ When the sheet's whole argument is that the parts sum.

**X3 · One line**
Ink block, one sentence centred, no figure.
→ When the payoff is a statement, not a number.

**X4 · Next step**
Ink block, one instruction and a time box: "Start with #2. Twenty minutes."
→ The most useful closer for the setup lane, and underused.

---

## Dividers and rules

- Section break: 1px `--blue-pale`, full content width, `--s5` above and below.
- Never a heavy rule. Never a dotted or dashed one — the only dash on her sheets is the spine
  drawing itself in the animation.

---

## Mixing guide — combinations that work

| Sheet type | Header | Card | Node | Chip | Closer |
|---|---|---|---|---|---|
| Numbered systems list | H1 | C1 | N1 | P1 | X1 |
| Big-number sheet | H2 | C1 | N1 | P3 | X2 |
| Manual vs system | H3 | C3 + C1 | N2 | P2 | X1 |
| Step-by-step setup | H4 | C1 | N1 | P1 | X4 |
| Dense reference | H5 | C6 | N1 | P2 | X3 |
| Hard truth (Ink canvas) | H4 | C1 | N2 | P3 | X3 |

---

## The one rule

**One variant per component per sheet.** Two card styles on one sheet reads as indecision, not
range. The variation belongs *between* sheets — that is what makes a feed look deep instead of
repetitive.
