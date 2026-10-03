---
name: javeriya-design
description: "Javeriya A.'s one-command cheatsheet factory (the trusted voice in AI and tech on LinkedIn: products, no-code workflows, founder growth). She says a topic, this runs the whole chain: research and live fact-check, content written in her voice, three design notes off her eight-frame bank, the GREY GATE (structure approved before any fire), the build on her dark stage with exactly one spotlight, the /javeriya-craft win matrix as a hard stop, then a 4K PNG plus an animated GIF and MP4 where the spotlight ignites, then LinkedIn and X launch posts, then the shipped log. Handles sponsored brand-collaboration sheets honestly. Pauses for her at exactly two points: which design note, and does the grey read. Ships bundled Geist, Fraunces, her real photo, templates and the build, grey-gate and export scripts, no other skill needed. Fire on '/javeriya-design', 'make a cheatsheet on X', 'design a sheet about', 'build the sheet', 'infographic on', 'topic ideas', or any topic she wants turned into a post-ready graphic."
---

# JAVERIYA-DESIGN — the cheatsheet factory

One command in, a finished sheet out. She approves twice; everything else is automatic.

**Read `/javeriya-brand` first, every run.** This skill executes; that skill decides what is
allowed. If the two ever disagree, `/javeriya-brand` wins.

---

## The chain

```
1  TOPIC        sharpen it into one claim
2  RESEARCH     real sources, live fact-check, a fact ledger
3  CONTENT      written in her voice, cut to fit the canvas
4  DESIGN NOTES three notes, three frames                 ← SHE PICKS
5  GREY BUILD   structure only, no fire                   ← SHE APPROVES
6  BUILD        the stage, the fire word, the spotlight, motion
7  CRAFT GATE   /javeriya-craft win matrix + autofix       ← HARD STOP
8  EXPORT       4K PNG + feed GIF + MP4
9  POSTS        LinkedIn and X launch copy in her voice
10 LOG          what shipped, so the next run does not repeat it
```

Two pauses. Not three, not zero.

---

## Stage 1 — Topic

Turn whatever she said into **one claim her audience can act on.** Her audience is founders,
operators and creators who want to grow on LinkedIn and use AI properly. They do not want AI
news; they want to know what to *do* with it.

- "AI tools" is not a topic. "6 AI workflows that get you noticed on LinkedIn" is.
- A topic has a number, a verb and an outcome. Sharpen it until it does.

Idea bank, her eight content lanes and the method for new topics:
**`references/topic-ideas.md`**. Check **`references/shipped-log.md`** before starting; if she
shipped something close in the last month, offer a genuinely different angle.

## Stage 2 — Research and fact-check

**Nothing goes on a sheet that has not been checked this run.** She is "the trusted voice in
AI & Tech"; one wrong feature, price or model name costs more than the sheet earns.

- Search for current sources. Model names, features, pricing and limits change monthly.
- Keep a short fact ledger beside the build: claim → source → date.
- Numbers must be honest. If a stat cannot be sourced, it does not go on the sheet.
- LinkedIn algorithm claims especially: most "the algorithm now rewards X" posts are guesses.
  If it is a guess, either cut it or say plainly that it is her observation.

## Stage 3 — Content

Write it before you design it. Voice rules: **`references/voice.md`**.

| Slot | Budget |
|---|---|
| Tag pill | 3–6 words |
| Headline | 6–11 words: bold subject, regular promise, one fire word |
| Deck | one line, 10–16 words |
| Card title | 3–6 words |
| Card body | 14–24 words, two lines |
| Spotlight tag | 1–3 words: "Start here", "Biggest gap", "#1" |
| Closer | 12–22 words + one figure |

**Decide what gets lit while writing, not while designing.** The spotlight is a content
decision: which card matters most and why. If you cannot say why, re-cut the content.

## Stage 4 — Design notes  ← GATE 1

**Three notes, three different frames**, in the format from
`/javeriya-brand → references/design-note-format.md`, picked from
`/javeriya-brand → references/frames.md`. Every note includes `WHY LIT`.

Present A / B / C, name the frame up front, add a one-line recommendation.
**Stop. She picks.** Do not build ahead of her answer.

## Stage 5 — Grey build  ← GATE 2

Pick component variants from `/javeriya-brand → references/style-kit.md`, one each. Build the
structure, then:

```bash
python3 scripts/greygate.py <sheet>.html
```

Ten measured checks, five judged on the grey PNG. **Never show her a grey below 15/15.**

Why grey matters more for her than for most: fire on black is so strong it hides weak
structure. In grey, the spotlight must still be the first stop through position, size and
contrast. If it only wins because it is orange, the layout is leaning on the colour.

**Stop. She approves the grey.**

## Stage 6 — Build

Start from the nearest template in `templates/`. They already honour the DOM contract the
scripts measure by.

Wire the motion in the same pass: `window.renderFrame(t)`, `t` in 0..1, **no CSS keyframes**.
Quiet cards arrive, then the spotlight **ignites**: it starts as charcoal and catches fire.
That ignition is her motion signature. Headline, pill and footer are never animated in.

## Stage 7 — Craft gate  ← HARD STOP

```bash
python3 scripts/build.py <sheet>.html audit     # runs the /javeriya-craft autofix loop
```

Then run the win matrix in `/javeriya-craft`. **Nothing exports below the bar.**

## Stage 8 — Export

```bash
python3 scripts/build.py <sheet>.html static    # <name>-4k.png   2160x2700
python3 scripts/build.py <sheet>.html motion    # <name>-feed.gif + <name>-motion.mp4
```

**Where to post what:** LinkedIn is her home, so the MP4 goes there (it autoplays and holds the
fire gradient far better than a GIF). The GIF is for X. The still PNG is for a carousel or a
static post.

## Stage 9 — Launch posts

Write the LinkedIn post first (her main platform), then the X version. Shapes:
**`references/post-formats.md`**.

## Stage 10 — Log

Append to `references/shipped-log.md`: date, topic, lane, frame, what was lit and why,
sponsored or not, what to avoid repeating.

---

## Sponsored sheets — brand collaborations

She has worked with 50+ brands, so some sheets feature a sponsor's product. The rules:

1. **Disclose it.** In the post, plainly. Never on the canvas as small print.
2. **The sponsor is lit only if it earns it.** If the sponsor's tool genuinely is the best
   answer, it can be the spotlight. If it is not, it sits as a quiet card with a fair
   description. Lighting a weaker tool because it paid is exactly the move that ends a
   "trusted voice".
3. **Same fact-check, same bar.** A sponsor's own claims are sources to check, not facts.
4. **Real logos only,** cropped from the brand's own assets, never redrawn.
5. Log it as sponsored, so the feed never runs two sponsored sheets back to back.

---

## Running the scripts

```bash
python3 scripts/greygate.py  sheet.html          # 15-check grey gate
python3 scripts/build.py     sheet.html audit    # autofix loop (via /javeriya-craft)
python3 scripts/build.py     sheet.html static   # 4K PNG
python3 scripts/build.py     sheet.html motion   # GIF + MP4
```

Run them from the folder holding the HTML; output lands next to it.

**Assets are bundled.** Geist (five weights), Fraunces 900 italic and her photo live in
`assets/` and get base64-embedded at build, so a finished sheet is one portable file. Never ask
her to upload a font or a photo.

**Overrides** (rarely needed): `JAVERIYA_ASSETS`, `JAVERIYA_CHROMIUM`, `JAVERIYA_FFMPEG`.

**Dependencies:** `pip install playwright pillow && python -m playwright install chromium`.
`pip install imageio-ffmpeg` adds the MP4; without it the GIF still ships.

---

## The rules that get broken when a run is rushed

1. **Never skip the fact-check.** Her credibility is the product.
2. **Never skip the grey gate.** Fire on black hides weak structure better than anything.
3. **Never skip the craft gate**, especially when the sheet looks good.
4. **Never build past a gate she has not answered.**
5. **Never light a card for balance.** Every spotlight has a `WHY LIT`.
6. **Never light a sponsor that has not earned it.**
7. **Never ship placeholder copy**, not even one card.
8. **Never edit the footer.**
9. **Never fix an overflow by shrinking type**; cut words first.
10. **Never repeat last week's frame** without saying why.
