# TEMPLATES

One working sheet per spine frame. Copy the closest one, swap the content, keep the skeleton.

## Built and tested

| File | Frame | Use for |
|---|---|---|
| `rail.html` | 01 Rail | a numbered list of things — the workhorse, 5–9 items |
| `two-state-board.html` | 07 Two-State Board | manual vs system, before vs after, 4–7 matched pairs |

Both pass `greygate.py` at 10/10 and `autofix.py` clean, in static and motion.

## Specified, built on demand

The other eight frames are fully specified — spine path, node placement, card geometry,
capacity and motion timing — in `/saman-brand → references/spine-frames.md`:

Pipeline · Loop · River · Ladder · Fork · Funnel · Orbit · Clock

Build one by starting from `rail.html` (single-axis frames: Pipeline, Ladder, Clock) or
`two-state-board.html` (split and 2D frames: Loop, River, Fork, Funnel, Orbit), swapping in the
spine path from the spec and re-laying the cards against it. Then run the grey gate and the
craft gate exactly as you would for a pre-built one — they do not care which template it came
from, only that the skeleton holds.

When a frame gets built and passes both gates, save it here and add a row to the table above.

## The skeleton — do not rename these

```
.canvas   1080x1350, the screenshot target
.spine    absolute SVG layer, z-index 0, one <path>
.content  z-index 1, padding 48px 56px 0
.rowband  --rh min-height, what autofix adjusts
.card     siblings must share a width (Funnel excepted)
.node     all one size on a sheet, centre on the line
.pill     exactly one per sheet
.footer   pinned top 1306, height 44, full width
```

The scripts measure by these names. Rename one and the sheet silently loses its geometry
audit and its autofix.

## Stubs

Where a card sits off the line, join it with a drawn 4px Blue bar under 48px — and draw it
**from the card** as a `::before`/`::after`, never as fixed coordinates in the spine path.
Hardcoded stubs detach the moment autofix changes a row height.

## The sample copy

Placeholder. It is there so the file renders on day one. It is not researched and must never
ship.
