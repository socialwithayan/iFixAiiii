# THE DESIGN NOTE

The plain-English description of a sheet, written and approved **before anything is drawn**.

Why it exists: an approved note is cheap to change and a built sheet is not. Most wasted
design time is a build that was never going to be right, and a note catches that in ten
seconds of reading.

**The test:** if the note cannot be written, the content is not ready. Go back to the content.

---

## The format

Eleven lines, always these fields, always this order.

```
FRAME     which of the ten spine frames
CANVAS    Sky | Paper | Ink
HEADLINE  the real headline, with the pill word in [brackets]
PILL      the word inside the brackets, alone
SPINE     where the line enters, what it does, where it ends
NODES     how many, numbered or plain
CARDS     how many · what is in each one · where they sit
CLOSER    what lands at the end of the spine
MOTION    what draws when, in seconds
WHY       one sentence: why this shape suits this content
```

Nothing else. No mood words, no "clean modern aesthetic", no colour talk — the colours are
already locked, and a note that spends a line on them is padding.

---

## Worked example — Rail

```
FRAME     Rail
CANVAS    Sky
HEADLINE  The 7 Systems That Save Founders [10 HOURS] A Week
PILL      10 HOURS
SPINE     enters top-left under the deck, runs straight down at x=100,
          passes 7 nodes, ends in the verdict strip
NODES     7, numbered
CARDS     7 · system name + the hours it saves + one line on what it replaces ·
          Paper cards stepping right off each node, x 148 → 1024
CLOSER    Ink verdict strip: the total, tabular figures, attached to the spine end
MOTION    spine draws 0-4s · nodes pop in order 4-9s · verdict lands 9-11s
WHY       seven separate countable things — the reader wants to scan, pick two
          and save the image
```

## Worked example — Two-State Board

```
FRAME     Two-State Board
CANVAS    Sky
HEADLINE  Manual Founder vs [SYSTEM] Founder
PILL      SYSTEM
SPINE     one vertical line at x=540, top to bottom, "vs" node at the head
NODES     1, the divider node
CARDS     6 matched pairs · left the manual way in Sky-deep wells, right the
          system way in Paper cards with blue rings
CLOSER    one Ink strip across the foot: the time difference over a year
MOTION    divider draws 0-4s · left rows fade 4-7s · right rows pop 7-11s
WHY       the whole argument is the gap between two columns, so the sheet
          should be that gap
```

## Worked example — Clock

```
FRAME     Clock
CANVAS    Paper
HEADLINE  Set Up Your First AI System In [30 MINUTES]
PILL      30 MINUTES
SPINE     vertical at x=200, ticks at each block boundary, top to bottom
NODES     5, plain
CARDS     5 · what to do + why it matters · x 248 → 1024, heights proportional
          to the real minutes (10/5/5/5/5)
CLOSER    Ink block: what she has running at the end of the 30 minutes
MOTION    line draws with ticks 0-5s · blocks fill in time order 5-11s
WHY       it is a schedule, and a schedule should look like time passing
```

---

## Three notes per topic

Every run produces **three notes, three different frames.** Not three colour variants of the
same layout — three genuinely different readings of the content.

The point is that she picks a shape. If all three notes propose Rail, the run has failed and
the content needs re-cutting, not the notes re-writing.

Present them as A / B / C with the frame named up front, then a one-line recommendation and
why. She picks one, or asks for a mix, and only then does anything get drawn.

---

## After she picks

The approved note goes straight into the grey build, unchanged. It becomes the spec:

- FRAME and SPINE → the SVG path from `spine-frames.md`
- NODES and CARDS → the `.rowband` / `.card` skeleton
- HEADLINE and PILL → the head band
- CLOSER → the Ink block at the spine end
- MOTION → `window.renderFrame(t)`

**Anything in the build that is not in the note is scope creep.** If the build wants something
the note does not have, amend the note and say so — do not quietly add it.
