---
name: javeriya-brand
description: "Javeriya A.'s locked visual brand system for cheatsheets and infographics (the trusted voice in AI and tech on LinkedIn: practical insights on products, no-code workflows and founder growth). The frozen reference every other Javeriya skill reads: the dark stage, her fire gradient (#D60802 to #FD4F02) on near-black, THE SPOTLIGHT law that makes a sheet hers, the Fire Word headline device in Fraunces Black Italic, the bold-to-regular weight split in Geist, the fire budget, the eight-frame bank, the component style kit, her design-note format, her locked footer with her real photo, and the do-not list. Never builds and never renders; it is the spec. Fire on '/javeriya-brand', 'my style', 'my brand', 'brand kit', 'what are my colours', 'is this on brand', 'frame ideas', 'design notes', 'what font', 'spotlight law', or whenever a design needs her rules before anything is drawn. /javeriya-design runs the pipeline. /javeriya-craft scores the result."
---

# JAVERIYA-BRAND — the locked style system

**Javeriya A. · "The trusted voice in AI & Tech" · "Get noticed by the right people on LinkedIn."**

This is the frozen reference. Design notes, builds, gates and exports all read it. It does not
render anything. If you are here to *make* a sheet, go to `/javeriya-design`.

**Rule zero: nothing in this file is a suggestion.** If a build breaks a law here, the build is
wrong, not the law.

Everything here is drawn from her own banner: the black stage, the red-to-orange pill that says
"Be in the Top 10%", the headline that switches from bold to regular mid-line, and "On
LinkedIn." set in a heavy italic serif that burns. Her sheets should look like that banner
grew into a page.

---

## 1. The palette

**THE STAGE — dark, always.**

| Token | Hex | Job |
|---|---|---|
| **Night** | `#070606` | the ground. Warm near-black, never pure `#000`. |
| **Char** | `#141312` | quiet cards: everything that is not the spotlight. |
| **Char-2** | `#1C1A19` | the closer strip and raised panels. |
| **Line** | `rgba(255,255,255,.09)` | hairlines on charcoal. |

**TYPE ON DARK.**

| Token | Hex | Job | On Char |
|---|---|---|---|
| **White** | `#F9F9F9` | headlines, card titles | 17.6:1 |
| **White-70** | `#BDB8B4` | body copy | 9.4:1 |
| **White-45** | `#8C8682` | labels, meta, numbering | 5.2:1 |

**FIRE: her one colour.**

| Token | Hex | Job |
|---|---|---|
| **Fire** | `#D60802 → #FD4F02` | the gradient, at 100°. The fire word, the tag pill, the send circle. Lit cards use the text-safe **Fire-lit** (below). |
| **Ember** | `#EE4510` | the solid midpoint, for one figure and one label where a gradient cannot go. 5.3:1 on Night. |
| **Crimson** | `#930405` | from her Jav & Co mark. Deep wells and pressed states only. |

Every value was sampled from her banner, not picked. The pill in her banner runs `#D60802` on
the left to `#FD4F02` on the right; that gradient is the brand.

**One contrast rule matters.** White on her gradient starts at 5.39:1 on the red end but falls
below 4.5:1 about 42% of the way across, reaching 3.34:1 at full orange. So fire comes in two
strengths:

| Token | Run | Use |
|---|---|---|
| **Fire** | `#D60802 → #FD4F02` | the fire word, the tag pill, the send circle: text on black, or large bold text |
| **Fire-lit** | `#D60802 → #E62602` | **every lit card.** White body copy stays at 4.52:1 or better across the whole card |

The lit card reads a touch deeper and redder than the pill, which is right: it carries reading
text, and the pill carries five large words.

---

## 2. THE SPOTLIGHT: her signature law

> **Every sheet is a dark stage, and exactly one block is lit. The lit block wears the fire
> gradient. Everything else is quiet charcoal.**

Her whole promise is *get noticed, be in the top 10%*. The Spotlight puts that promise into
the layout: every sheet picks a winner. A reader sees, at a glance and before reading a word,
which one thing matters most.

**What the spotlight is:** a `.card.spotlight`. Fire-lit gradient fill, white type, a soft ember
glow, and usually a small Night tag ("Start here", "Biggest gap", "#1") in its corner.

**The three tests:**

1. **One.** Exactly one lit block. Two lit blocks is two answers, and that is no answer.
2. **Earned.** The lit block is the most important thing on the sheet: the start point, the
   biggest gap, the winner. It is never lit for balance or decoration. If you cannot say in
   one sentence why *this* card is lit, the content is not ready.
3. **Wins in grey.** Strip the colour and the spotlight must still be the first stop, through
   its position, its tag and its contrast against charcoal. If it only wins because it is
   orange, the layout is leaning on the colour.

**Where to put it:** almost never top-left. A spotlight in reading-order position one is just
the first card. Put it second, or in the middle of the grid, so the eye *jumps* to it; that
jump is what makes it a spotlight.

---

## 3. The Fire Word

**One word or short phrase in the headline is set in Fraunces Black Italic and filled with the
fire gradient.** Exactly one, on every sheet.

```
6 AI Workflows That Get You  Noticed  On LinkedIn
                             ^^^^^^^
                             Fraunces 900 italic, fire gradient
```

It is the outcome word: *Noticed, Chosen, Booked, Hired, Seen*. Never a filler word, never the
topic noun. Put the punctuation inside the span, or it sits detached after the gradient.

The fire word is the only serif on the sheet apart from card numerals and the closer figure.

---

## 4. The weight split

Her banner reads **"Get Noticed By** The Right People" — bold opens, regular finishes. Every
headline does the same:

```
<b>6 AI Workflows</b> That Get You <fire>Noticed</fire> On LinkedIn
 ^ bold 700, the subject   ^ regular 400, the promise
```

Bold carries the subject (what), regular carries the promise (why), and the fire word carries
the outcome. Three voices in one line, and that line is her typographic fingerprint.

---

## 5. The fire budget

The gradient appears in **four places at most**:

1. the fire word
2. the spotlight card
3. the tag pill (one, optional)
4. the send circle in the footer

Solid **Ember** may also appear once as a figure (the closer number) and once as a column label.
That is the whole allowance. Fire on a fifth thing stops being a spotlight and starts being
decoration, and then nothing on the sheet is lit.

---

## 6. The stage

- Ground is Night `#070606`, never a light canvas. The dark stage is half her identity.
- Behind everything sits the **ember glow**: one low radial of `rgba(214,8,2,.20)` from a
  corner, the light streaks of her banner turned down. It never sits behind body text at full
  strength, and it never becomes a visible shape.
- Quiet cards are Char with a 1px Line border. No shadows on quiet cards; only the spotlight
  glows.

---

## 7. Type: Geist and Fraunces

| Role | Font | Size | Weight | Colour |
|---|---|---|---|---|
| Headline | Geist | 54–60px | 400 + **700** split | White |
| Fire word | Fraunces | same as headline | 900 italic | fire gradient |
| Tag pill | Geist | 20px | 700 italic | white on fire |
| Deck | Geist | 20px | 400 | White-70 |
| Card numeral | Fraunces | 40px | 900 italic | White-45 |
| Card title | Geist | 21–23px | 600 | White |
| Body | Geist | 15–16px | 400 | White-70 |
| Label | Geist | 13px | 700, +.12em, CAPS | White-45 |
| Closer figure | Fraunces | 44–46px | 900 italic | Ember |

Headline tracking −0.035em. **Nothing below 12px, ever.** Tabular numerals on every figure.

Both fonts ship as subset `.woff2` in `assets/fonts/`: Geist at five weights, Fraunces at 900
italic. Both are OFL licensed, and the licences ship alongside them.

---

## 8. Space, radius, depth

```
Spacing scale (px):  4 · 8 · 12 · 16 · 24 · 32 · 48
Radius:              card 16–18 · panel 22 · pill 12 · tag 999
Canvas margins:      56 left/right · 52 top · footer pinned at y=1306
Depth:               quiet cards are flat. Only the spotlight glows.
```

---

## 9. The frame bank: eight layouts

Every frame has exactly one lit block. The frame decides *which* block it is.

| # | Frame | What gets lit | Use when the content is |
|---|---|---|---|
| 1 | **Spotlight Grid** | the one to start with | 4–6 parallel items |
| 2 | **Versus** | the biggest gap on the winning side | most people vs the top 10% |
| 3 | **Podium** | the #1 | a ranking |
| 4 | **Ladder** | the top rung | levels, a climb |
| 5 | **Hero + Stack** | the big idea, up top | one claim with supporting points |
| 6 | **Timeline** | the turning point | a journey, a 30-day plan |
| 7 | **Prompt Stack** | the best prompt | prompts, templates, scripts |
| 8 | **Checklist** | the most-skipped item | an audit, 7–10 checks |

Geometry and capacity for each: **`references/frames.md`**. Component variants (headers,
cards, tags, closers): **`references/style-kit.md`**.

**Rotation:** never the same frame twice in a row. Spotlight Grid is the workhorse and will
quietly eat the rotation if nobody watches it.

---

## 10. The footer: locked

Pinned at `y=1306`, height 44px, full width, `#0D0B0B` with a top hairline.

```
[her photo 28px]  Follow Javeriya A. For More          DM FOR COLLABORATIONS [send]
                  Geist 600 15px, White                Geist 500 13px caps,
                                                       "collaborations" Ember italic,
                                                       26px fire circle, paper-plane
```

The right side is lifted straight from her banner's own CTA. The wording does not change.

**Her photo** ships in `assets/javeriya-avatar.png`, cropped from her profile picture. To
swap it, replace that file with a square PNG, 300×300 or larger.

---

## 11. The design note

Before anything is drawn, the sheet is described in plain English in this shape:

```
FRAME     Spotlight Grid
HEADLINE  <b>6 AI Workflows</b> That Get You [Noticed] On LinkedIn
FIRE      Noticed
TAG       "The top 10% do this"   (or none)
CARDS     6 · numeral + title + 2 lines · 2×3 grid
LIT       #2 "Rewrite your headline first" — tag "Start here"
WHY LIT   it is the one change every other workflow depends on
CLOSER    "Pick one. Run it for a month." · figure "30 days"
MOTION    cards rise quiet 0-55% · spotlight ignites 58-82% · closer 84-100%
```

`WHY LIT` is mandatory. If it cannot be written, nothing on the sheet deserves the light yet.
Full format and examples: **`references/design-note-format.md`**.

---

## 12. The do-not list

**Brand**
1. No light canvas. Her stage is dark; that is half of what makes a sheet hers at a glance.
2. No second accent colour. No blue, no green, no purple. Fire is the only colour.
3. Fire in four places at most (§5). Never on body text.
4. Never two lit blocks. Never zero.
5. Never two fire words. Never zero.
6. Never edit the footer wording.

**Not a neighbouring account's system**
7. No structural line threading the cards together. That device belongs to another account
   in the same niche. Her cards stand on a stage; they do not hang off a line.
8. No pastel card families. Same reason, and pastels on Night look muddy anyway.
9. No Object Frame: the sheet is never drawn as a phone, a folder or a terminal. That device
   already belongs to a large account in an adjacent niche.

**Not generic AI design**
10. No glassmorphism, no neon outlines, no glow on anything but the spotlight.
11. No icon that restates its card title.
12. No emoji anywhere on the canvas.
13. No filler card. Five strong cards beat six with a passenger.
14. No type under 12px, and no fixing an overflow by shrinking type before cutting words.

---

## 13. Reading order for the other skills

- Building a sheet → `/javeriya-design`
- Scoring or fixing one → `/javeriya-craft` (enforces §2, §3, §5, §7, §12)
- Picking a layout → `references/frames.md`
- Picking how the parts look → `references/style-kit.md`
- Writing the note she approves → `references/design-note-format.md`
- Every token, in copy-paste CSS → `references/brand-kit.md`
