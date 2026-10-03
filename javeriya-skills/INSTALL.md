# Javeriya's design skills — install

Three skills. She types one command and gets a finished sheet.

| Skill | What it is |
|---|---|
| `/javeriya-brand` | her locked style: the dark stage, the fire gradient, the Spotlight law, the frame bank |
| `/javeriya-design` | the factory: topic to a researched, built, exported sheet plus launch posts |
| `/javeriya-craft` | the gate: scores the sheet and auto-repairs it before anything exports |

Self-contained: bundled Geist, Fraunces, her photo and the scripts. They depend on no other
skills.

---

## 1. Install

```bash
cd ~/.claude/skills
unzip javeriya-design-skills.zip
```

That gives her `javeriya-brand/`, `javeriya-design/` and `javeriya-craft/`. Keep them side by
side: `/javeriya-design` and `/javeriya-craft` find each other in the neighbouring folder.

## 2. Dependencies

```bash
pip install playwright pillow
python -m playwright install chromium

pip install imageio-ffmpeg     # optional: adds the MP4. The GIF works without it.
```

## 3. Her photo

Already in. It is cropped from her LinkedIn profile picture and lives at:

```
javeriya-brand/assets/javeriya-avatar.png   (and the same file in the other two)
```

To use a sharper original, replace that file in all three folders with a square PNG, 300×300
or larger.

## 4. Her voice

One thing improves with her input: paste 15–20 of her real LinkedIn posts into

```
javeriya-design/references/voice.md   →   section "Her lines, verbatim"
```

Until then the voice rules are built from her profile and banner, not her actual posts.
Everything else works out of the box.

---

## 5. Use it

```
/javeriya-design 6 AI workflows that get you noticed on LinkedIn
```

It runs the chain and stops twice:

1. **Pick the layout.** Three design notes, three different frames, each saying which card gets
   lit and why. She picks one.
2. **Approve the grey.** The structure with the fire stripped out. If the lit card still wins
   in grey, the design is sound.

Then it builds, runs the craft gate, and exports:

- `<name>-4k.png`: 2160×2700, the sheet
- `<name>-motion.mp4`: the spotlight igniting, for LinkedIn
- `<name>-feed.gif`: the same, for X
- the LinkedIn post and the X post, written and ready to paste

No topic in mind?

```
/javeriya-design give me topic ideas
```

Other entry points:

```
/javeriya-brand    what are my colours · is this on brand · frame ideas
/javeriya-craft    score this sheet · why does this look generic · fix my sheet
```

## Running the scripts directly

```bash
cd <folder with the html>
python3 ~/.claude/skills/javeriya-design/scripts/greygate.py sheet.html          # 15-check grey gate
python3 ~/.claude/skills/javeriya-craft/scripts/autofix.py  sheet.html           # measure-fix loop
python3 ~/.claude/skills/javeriya-design/scripts/build.py   sheet.html static    # 4K PNG
python3 ~/.claude/skills/javeriya-design/scripts/build.py   sheet.html motion    # GIF + MP4
```

## If something goes wrong

| Message | Fix |
|---|---|
| `ASSET MISS` | `assets/` is missing from that skill folder, or set `JAVERIYA_ASSETS=<dir>` |
| `no Chromium found` | `python -m playwright install chromium`, or set `JAVERIYA_CHROMIUM=/path/to/chrome` |
| `no full ffmpeg` | `pip install imageio-ffmpeg`; the GIF ships either way |
| `STUCK — design decisions` | the sheet needs a layout or copy change; the report names which |
| `spotlight-count` | zero or two lit cards; light exactly the one that matters most |

## What is in the box

```
javeriya-brand/   SKILL.md · brand-kit.md · frames.md · style-kit.md · design-note-format.md
                  assets/ (Geist ×5, Fraunces 900 italic, OFL licences, her photo)
javeriya-design/  SKILL.md · build.py · greygate.py · 2 templates + specs for 6 more
                  topic-ideas.md · voice.md · post-formats.md · shipped-log.md · assets/
javeriya-craft/   SKILL.md · autofix.py · win-matrix.md · design-laws.md
                  fix-recipes.md · craft-benchmarks.md · assets/
```
