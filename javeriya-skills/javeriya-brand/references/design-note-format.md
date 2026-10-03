# THE DESIGN NOTE

The plain-English description of a sheet, written and approved **before anything is drawn**.
An approved note is cheap to change; a built sheet is not.

**The test:** if the note cannot be written, the content is not ready.

---

## The format

Ten lines, always these fields, always this order.

```
FRAME     which of the eight frames
HEADLINE  the real headline: <b>bold subject</b> regular promise [fire word]
FIRE      the fire word, alone
TAG       the tag pill text, or "none"
CARDS     how many · what is in each · how they sit
LIT       which card is the spotlight · its tag
WHY LIT   one sentence: why this card, and not the others
CLOSER    the closer line · its figure
MOTION    what moves when
WHY       one sentence: why this frame suits this content
```

**`WHY LIT` is the field that matters most.** It is her whole signature in one line. If the
answer is "it looked balanced there", the spotlight is decoration and the note goes back.

No mood words, no colour talk. The colours are locked; a note that spends a line on them is
padding.

---

## Worked example: Spotlight Grid

```
FRAME     Spotlight Grid
HEADLINE  <b>6 AI Workflows</b> That Get You [Noticed] On LinkedIn
FIRE      Noticed
TAG       "The top 10% do this"
CARDS     6 · numeral + title + 2 lines · 2×3 grid
LIT       #2 "Rewrite your headline first" · tag "Start here"
WHY LIT   every other workflow sends people to the profile; a weak headline wastes all of it
CLOSER    "Pick one. Run it every day for a month." · "30 days"
MOTION    cards rise quiet 0-55% · spotlight ignites 58-82% · closer 84-100%
WHY       six parallel workflows; the reader wants to scan, then know where to start
```

## Worked example: Versus

```
FRAME     Versus
HEADLINE  <b>Most People Post.</b> The Top 10% Get [Chosen.]
FIRE      Chosen.
TAG       "Same platform. Different results."
CARDS     5 matched pairs · left ghost cards, right charcoal
LIT       right row 2 "Write for one buyer" · tag "Biggest gap"
WHY LIT   the other four habits only work once the posts are written for someone specific
CLOSER    "None of these need more time." · "Top 10%"
MOTION    left fades dim · right slides in · spotlight ignites · closer
WHY       the argument is the gap between two columns, so the sheet should be that gap
```

## Worked example: Podium

```
FRAME     Podium
HEADLINE  <b>5 AI Tools</b> Ranked For LinkedIn [Creators]
FIRE      Creators
TAG       none
CARDS     5 · #1 tall and lit, #2-#5 slim rows
LIT       #1 · no tag, the podium already says it
WHY LIT   it is the ranking's answer
CLOSER    none; #1 is the closer
MOTION    #5 to #2 rise from the bottom · #1 lands last and ignites
WHY       a ranking; the reader wants the answer, then the runners-up
```

---

## Three notes per topic

Every run produces **three notes, three different frames**: not three colour variants of one
layout. She picks a shape, not a coin flip. Present them as A / B / C with the frame named up
front, then a one-line recommendation.

## After she picks

The approved note goes into the grey build unchanged. It becomes the spec:

- FRAME → the template from `javeriya-design/templates/`
- HEADLINE, FIRE, TAG → the head band
- CARDS, LIT → the grid and the one `.card.spotlight`
- CLOSER → the closer strip
- MOTION → `window.renderFrame(t)`

**Anything in the build that is not in the note is scope creep.** If the build wants something
the note does not have, amend the note and say so.
