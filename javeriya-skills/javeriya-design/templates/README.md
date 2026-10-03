# TEMPLATES

One working sheet per frame. Copy the closest, swap the content, keep the skeleton.

## Built and tested

| File | Frame | Use for |
|---|---|---|
| `spotlight-grid.html` | 01 Spotlight Grid | 4–6 parallel items, one lit: the workhorse |
| `versus.html` | 02 Versus | most people vs the top 10%, one gap lit |

Both pass `greygate.py` at 10/10 and `autofix.py` clean, in static and motion.

## Specified, built on demand

The other six frames (Podium, Ladder, Hero + Stack, Timeline, Prompt Stack, Checklist) are
fully specified in `/javeriya-brand → references/frames.md`: geometry, what gets lit, capacity,
motion.

Build one from the nearest template:
- **single-column frames** (Podium, Ladder, Checklist, Prompt Stack): start from `versus.html`,
  drop to one column
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

Placeholder. It is there so the file renders on day one. It is not researched and must never
ship.
