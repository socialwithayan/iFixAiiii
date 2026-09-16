# Saman's design skills — install

Three skills. She types one command and gets a finished sheet.

| Skill | What it is |
|---|---|
| `/saman-brand` | her locked style system — colours, type, the Blue Spine law, the frame bank |
| `/saman-design` | the factory — topic to researched, built, exported sheet plus launch posts |
| `/saman-craft` | the gate — scores the sheet and auto-repairs it before anything exports |

They are self-contained: bundled Inter, bundled avatar, bundled scripts. They do not depend on
anyone else's skills.

---

## 1. Install

Drop all three folders into her skills directory:

```
~/.claude/skills/saman-brand/
~/.claude/skills/saman-design/
~/.claude/skills/saman-craft/
```

Or install the `.skill` files from `bundles/` if her setup takes packaged skills.

Keep the three side by side — `/saman-design` and `/saman-craft` find each other by looking in
the neighbouring folder.

## 2. Dependencies

```bash
pip install playwright pillow
python -m playwright install chromium

pip install imageio-ffmpeg     # optional: adds the MP4. GIF works without it.
```

## 3. Her avatar

The bundle ships an "SA" monogram placeholder. To use her real photo, replace this file:

```
saman-brand/assets/saman-avatar.png
saman-design/assets/saman-avatar.png
saman-craft/assets/saman-avatar.png
```

Square PNG, 300×300 or larger. Nothing else to change — every build picks it up.

## 4. Her voice

One thing needs her input before the launch posts sound right:

```
saman-design/references/voice.md   →   section "Her lines, verbatim"
```

Paste 15–20 of her real posts there. Until that is filled, the voice rules are an informed
approximation built from her bio and positioning, not from her actual writing. Everything else
works out of the box.

---

## 5. Use it

```
/saman-design  5 AI systems that save founders 10 hours a week
```

It runs the chain and stops twice:

1. **Which design note** — three layouts, three different frames. She picks one.
2. **Does the grey read** — structure with the colour stripped out. She approves.

Then it builds, gates, exports the 4K PNG and the GIF/MP4, and writes the X and LinkedIn posts.

Other entry points:

```
/saman-brand    what are my colours · is this on brand · frame ideas
/saman-craft    score this sheet · why does this look generic · fix my sheet
```

## Running the scripts directly

```bash
cd <folder with the html>
python3 ~/.claude/skills/saman-design/scripts/greygate.py sheet.html   # 15-check grey gate
python3 ~/.claude/skills/saman-craft/scripts/autofix.py  sheet.html    # measure-fix loop
python3 ~/.claude/skills/saman-design/scripts/build.py   sheet.html static   # 4K PNG
python3 ~/.claude/skills/saman-design/scripts/build.py   sheet.html motion   # GIF + MP4
```

## If something goes wrong

| Message | Fix |
|---|---|
| `ASSET MISS` | `assets/` is missing from that skill folder, or set `SAMAN_ASSETS=<dir>` |
| `no Chromium found` | `python -m playwright install chromium`, or set `SAMAN_CHROMIUM=/path/to/chrome` |
| `no full ffmpeg` | `pip install imageio-ffmpeg` — the GIF ships either way |
| `STUCK — design decisions` | the sheet needs a layout or copy change; the report names which |
| sheet renders in the wrong font | the fonts did not embed — check `assets/fonts/` has five `.woff2` files |

## What is in the box

```
saman-brand/   SKILL.md · brand-kit.md · spine-frames.md · design-note-format.md
               assets/ (Inter x5, avatar)
saman-design/  SKILL.md · build.py · greygate.py · 2 templates + specs for 8 more
               voice.md · post-formats.md · shipped-log.md · assets/
saman-craft/   SKILL.md · autofix.py · win-matrix.md · design-laws.md · fix-recipes.md
               assets/
```
