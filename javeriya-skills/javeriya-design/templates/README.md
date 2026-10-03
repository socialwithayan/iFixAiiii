# TEMPLATES

One working sheet per frame. Copy the closest, swap the content, keep the skeleton.

## Built and tested

| File | Frame | Use for |
|---|---|---|
| `spotlight-grid.html` | 01 Spotlight Grid | 4–6 parallel items, one lit: the workhorse |
| `versus.html` | 02 Versus | most people vs the top 10%, one gap lit |
| `checklist.html` | 08 Checklist | an audit, 7–10 checks, the one to fix first lit |

All three pass `greygate.py` at 10/10 and `autofix.py` clean, in static and motion.

## Specified, built on demand

The other five frames (Podium, Ladder, Hero + Stack, Timeline, Prompt Stack) are
fully specified in `/javeriya-brand → references/frames.md`: geometry, what gets lit, capacity,
motion.

Build one from the nearest template:
- **single-column frames** (Podium, Ladder, Prompt Stack): start from `checklist.html`
- **grid frames** (Hero + Stack, Timeline): start from `spotlight-grid.html`

Then run the grey gate and the craft gate as for any other sheet. They check the skeleton, not
which template it came from. When a new frame passes both, save it here and add a row above.

For Podium and Ladder, put the frame name in the filename (`podium-tools.html`): card widths
or heights differ on purpose there, and the scripts read the filename to exempt them.

## The skeleton: do not rename these

```
.canvas     1080x1350, the screenshot target
.content    z-index 1, padding 52px 56px 0
.rowband    --rh min-height: what autofix adjusts
.card       siblings share a width (Podium, Ladder excepted); literal px height
.spotlight  exactly one, and it is also a .card
.fire       exactly one, inside .h1
.pill       at most one
.h1         font shorthand "400 NNpx/…": autofix steps it down
.footer     pinned top 1306, height 44, full width
```

## The sample copy

`spotlight-grid.html` and `versus.html` carry placeholder copy: it is there so the files render
on day one, it is not researched, and it must never ship.

`checklist.html` carries real, fact-checked copy (a LinkedIn profile audit, sources checked
2026-10). It shipped as a finished sheet. Re-check its numbers before reusing it, because
LinkedIn changes them.
