---
name: saman-design
description: "Saman Ahmed's one-command cheatsheet factory (@ScaleWthAI — AI systems and workflows for busy founders). She says a topic, this runs the whole chain: research and live fact-check, content written in her voice, three design notes off the Spine Bank, the GREY GATE (structure approved before any colour), the colour build, the /saman-craft win matrix as a hard stop, then a 4K PNG plus an animated GIF and MP4, then launch posts for X and LinkedIn, then the memory log. Pauses for her at exactly two points: which design note, and does the grey read. Ships bundled Inter, her avatar, ten spine templates and the build, grey-gate and export scripts — no other skill required. Fire it on '/saman-design', 'make a cheatsheet on X', 'design a sheet about', 'run the factory', 'build the sheet', 'infographic on', or any topic she wants turned into a post-ready graphic. /saman-brand holds the locked style rules. /saman-craft scores and repairs the build."
---

# SAMAN-DESIGN — the cheatsheet factory

One command in, a finished sheet out. She approves twice; everything else is automatic.

**Read `/saman-brand` first, every run.** This skill executes; that skill decides what is
allowed. If the two ever disagree, `/saman-brand` wins.

---

## The chain

```
1  TOPIC        sharpen it into one claim
2  RESEARCH     real sources, live fact-check, a fact ledger
3  CONTENT      written in her voice, cut to fit the canvas
4  DESIGN NOTES three notes, three frames                 ← SHE PICKS
5  GREY BUILD   structure only, no colour                 ← SHE APPROVES
6  COLOUR BUILD tokens applied, motion wired
7  CRAFT GATE   /saman-craft win matrix + autofix          ← HARD STOP
8  EXPORT       4K PNG + feed GIF + MP4
9  POSTS        X and LinkedIn launch copy in her voice
10 LOG          what shipped, so the next run does not repeat it
```

Two pauses. Not three, not zero. Everything between them runs without asking.

---

## Stage 1 — Topic

Turn whatever she said into **one claim a founder can act on.**

- "AI tools" is not a topic. "The 5 systems that save a founder 10 hours a week" is.
- Her audience is busy founders, not AI hobbyists. Every sheet answers *what do I do Monday*.
- If the topic has no number, no verb and no outcome, sharpen it before going further.

Idea bank, the eight content lanes and the method for generating new topics:
**`references/topic-ideas.md`**. Rotate lanes, not just topics — four sheets from one lane
makes a feed look narrow even when every sheet is good.

Check the log (`references/shipped-log.md`) before starting. If she shipped something close in
the last month, say so and offer a genuinely different angle rather than a near-duplicate.

## Stage 2 — Research and fact-check

**Nothing goes on a sheet that has not been checked this run.** Her whole positioning is that
her systems actually work; one wrong number costs more than the sheet earns.

- Search for current sources. Model names, pricing, feature availability and limits move fast.
- Build a short fact ledger: claim → source → date. Keep it beside the build.
- **Time savings must be honest.** "Saves 2 hours" is a claim about a real workflow, not a
  round number that makes the total land on ten. If the honest total is 7 hours, the headline
  says seven.
- Anything you cannot source does not go on the sheet. Not softened — cut.

## Stage 3 — Content

Write it before you design it. Layout follows content; content never gets padded to fill a
layout. Voice, sentence shapes and the words she does not use: **`references/voice.md`**.

Cut to the canvas as you write:

| Slot | Budget |
|---|---|
| Headline | 8–12 words, one pill word |
| Deck | one line, 10–16 words |
| Card title | 3–6 words |
| Card body | 18–30 words, two lines |
| Stat chip | 3–4 words |
| Verdict | 15–25 words + one figure |

If a card needs 40 words, the idea is two cards or it is not a card.

## Stage 4 — Design notes  ← GATE 1

**Three notes, three different frames**, in the format from
`/saman-brand → references/design-note-format.md`. Pick frames from the Spine Bank
(`/saman-brand → references/spine-frames.md`) and check the log so she is not handed Rail for
the fourth week running.

Present A / B / C, name the frame up front, add a one-line recommendation and why.
**Stop. She picks.** Do not build ahead of her answer.

## Stage 5 — Grey build  ← GATE 2

Pick the component variants from `/saman-brand → references/style-kit.md` — header, card,
node, chip and closer. One variant each. That table is what stops ten Rail sheets looking like
the same sheet ten times.

Build the structure with the brand stripped out, then:

```bash
python3 scripts/greygate.py <sheet>.html
```

Ten measured checks, five she and you judge on the grey PNG. **Never show her a grey below
15/15** — fix, re-run, then show her.

Why grey: colour flatters bad structure. If the hierarchy, the spine and the air do not work
in greyscale, no palette rescues them — and finding that out after the colour pass means doing
the colour pass twice.

**Stop. She approves the grey.**

## Stage 6 — Colour build

Apply the tokens. Start from the closest template in `templates/` rather than from nothing —
they already honour the DOM contract the scripts measure by.

Wire the motion in the same pass: `window.renderFrame(t)`, `t` in 0..1, **no CSS keyframes**
(a stepped screenshot does not advance them). Spine draws 0–36%, content lands 36–85%, closer
85–100%.

## Stage 7 — Craft gate  ← HARD STOP

```bash
python3 scripts/build.py <sheet>.html audit     # runs the /saman-craft autofix loop
```

Then run the win matrix in `/saman-craft`. **Nothing exports below the bar.** This is the step
that gets skipped when a sheet is nearly right, and a nearly-right sheet is what the feed
punishes.

## Stage 8 — Export

```bash
python3 scripts/build.py <sheet>.html static    # <name>-4k.png   2160x2700
python3 scripts/build.py <sheet>.html motion    # <name>-feed.gif + <name>-motion.mp4
```

Deliverables: the 4K PNG, the GIF, the MP4. `-preview.png` is a self-check, not a deliverable.

**Which to post where:** the PNG for a carousel or a static post, the MP4 on LinkedIn (it
autoplays and beats a GIF on quality), the GIF on X. Post the still to both if the motion adds
nothing — motion is not mandatory, it is a weapon for the sheets that earn it.

## Stage 9 — Launch posts

Write the X post and the LinkedIn post in her voice. Shapes and examples:
**`references/post-formats.md`**.

The post carries the idea; the sheet carries the detail. A post that just describes the image
wastes the slot.

## Stage 10 — Log

Append to `references/shipped-log.md`: date, topic, frame, canvas, what worked, what to avoid
repeating. This is what keeps the frame rotation honest and stops the same topic shipping
twice in a quarter.

---

## Running the scripts

```bash
python3 scripts/greygate.py  sheet.html    # 15-check grey gate
python3 scripts/build.py     sheet.html audit    # autofix loop (via /saman-craft)
python3 scripts/build.py     sheet.html static   # 4K PNG
python3 scripts/build.py     sheet.html motion   # GIF + MP4
```

Run them from the folder holding the HTML — output lands next to it.

**Assets are bundled.** Inter (five weights) and her avatar live in `assets/` and get
base64-embedded at build, so a finished sheet is one portable HTML file with no network
dependency. Never ask her to upload a font or an avatar.

**Her real photo:** replace `assets/saman-avatar.png` with a square PNG, 300×300 or larger.
Nothing else changes.

**Environment overrides** (rarely needed): `SAMAN_ASSETS`, `SAMAN_CHROMIUM`, `SAMAN_FFMPEG`.

**Dependencies:** `pip install playwright pillow && python -m playwright install chromium`.
`pip install imageio-ffmpeg` adds the MP4 — without it the GIF still ships.

---

## Templates

`templates/` holds one working sheet per spine frame. Copy the closest one, swap the content,
keep the skeleton. The class names are the contract the scripts measure by:

```
.canvas  .spine  .content  .rowband  .card  .node  .pill  .footer
```

Rename them and the sheet silently loses its geometry audit and its autofix.

Sample copy in the templates is placeholder. It is there so the file renders on day one — it
is not researched and must never ship.

---

## The rules that get broken when a run is rushed

1. **Never skip the fact-check.** Not for a "simple" topic, not when she is in a hurry.
2. **Never skip the grey gate.** It is twenty seconds and it saves a rebuild.
3. **Never skip the craft gate.** Especially when the sheet looks fine.
4. **Never build past a gate she has not answered.**
5. **Never invent a number** to make a total land neatly.
6. **Never add a card to fill space.** Six good cards beat seven with a passenger.
7. **Never ship placeholder copy**, not even one card of it.
8. **Never edit the footer.**
9. **Never fix an overflow by shrinking type** — cut words first, always.
10. **Never repeat last week's frame** without saying why.
