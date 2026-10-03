# STYLE KIT — component variants

The frame bank decides the *shape* of a sheet. This file decides how the parts inside it look.
Eight frames × these variants is how forty sheets share one system without looking like one
sheet forty times. **Every variant here already obeys the laws**, so mixing them cannot take a
sheet off-brand.

**One variant per component per sheet.** Two card styles on one sheet reads as indecision.

---

## Headers: 4 variants

**H1 · Pill + split headline** *(default)*
Fire tag pill, then the bold/regular headline with its fire word, then the deck.
→ Her banner, as a page.

**H2 · Split headline, no pill**
Headline and deck only.
→ When the headline is strong enough alone, which is most of the time. The pill is optional.

**H3 · Big number**
A Fraunces 900 italic figure at 120px in Ember, then the headline under it.
→ "73%", "10×", "30 days": when one number is the whole hook.

**H4 · Column labels**
H1 or H2, then a label row naming two sides.
→ The Versus header.

---

## Cards: 5 variants

**C1 · Numeral card** *(default)*
Char, Fraunces numeral top-left in White-45, title and body pushed to the bottom.
→ The workhorse. The empty middle is deliberate; it gives the card a held, editorial pace.

**C2 · Compact card**
Char, no numeral, title + body vertically centred, 150 tall.
→ Dense frames: Versus, Checklist.

**C3 · Ghost card**
Transparent, 1px dashed `rgba(255,255,255,.12)`, muted type.
→ The losing side of a comparison only. Never anywhere else.

**C4 · Prompt card**
Char with a Night inset well holding copy-ready text.
→ Prompt Stack.

**C5 · Stat card**
Char, a large Ember figure (Fraunces 900 italic, 48px) in place of the numeral.
→ When every card carries a number worth reading first.

The **spotlight** is not a variant: it is whichever card the frame lights, in fire.

---

## Tags: 3 variants (on the spotlight only)

**T1 · Night chip** *(default)*: `#070606` fill, white caps 12px, top-right of the spotlight.
"Start here", "Biggest gap", "#1", "Most skipped", "Use this one".

**T2 · Inline label**: white caps 12px with no chip, above the spotlight's title.
→ When the spotlight is short and a chip would crowd it.

**T3 · None**
→ When the frame already says why it is lit (Podium #1 does not need "#1").

---

## Closers: 4 variants

**X1 · Verdict strip** *(default)*: Char-2 strip, sentence left with its first clause bold,
Ember Fraunces figure right.

**X2 · One line**: Char-2 strip, one sentence, no figure.
→ When the payoff is a statement, not a number.

**X3 · Next step**: "Start with #2. Ten minutes today." The most useful closer, and underused.

**X4 · None**: the spotlight *is* the closer (Podium, Hero + Stack).

---

## Mixing guide

| Sheet type | Header | Card | Tag | Closer |
|---|---|---|---|---|
| AI tools / workflows list | H1 | C1 | T1 | X1 |
| Most people vs top 10% | H4 | C3 + C2 | T1 | X1 |
| Ranked tools | H2 | C2 | T3 | X4 |
| Prompts she shares | H1 | C4 | T1 | X3 |
| Profile audit | H2 | C2 | T1 | X3 |
| One big stat | H3 | C5 | T2 | X2 |

---

## The one rule

**One variant per component per sheet.** The variation belongs *between* sheets; that is what
makes a feed look deep instead of repetitive.
