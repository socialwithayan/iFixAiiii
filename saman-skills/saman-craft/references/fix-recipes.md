# FIX RECIPES

What to actually do when the gate fails. Ordered by how often each one comes up.

---

## "Too much content"
*Symptoms: `footer-collision`, `overflow`, density scored 3, autofix reports STUCK.*

The instinct is to shrink something. Do not.

1. **Cut the weakest card.** There is always one that says less than the others. Six strong
   beats seven with a passenger, and the gate is telling you which one it is.
2. **Cut words, not size.** Card body is 18–30 words. If a card needs 40, it is two ideas.
3. **Only then** adjust heights — and the autofix already tried that before it gave up.

Shrinking type to fit is the single fastest way to make a sheet unreadable in the feed, which
is the only place it will be seen.

## "The spine is decoration"
*Symptoms: `detached-card`, spine integrity scored 4 or below, it "looks fine but generic".*

The line was added to a layout instead of the layout being built around the line.

1. Pick the frame from the Spine Bank **first**, then place content on it.
2. Every block attaches: on the line, or stubbed to it with a drawn 4px Blue bar under 48px.
3. Draw the stub from the card (`::before`), never as fixed coordinates in the spine path —
   hardcoded stubs detach the moment a row height changes.
4. If the content genuinely does not hang off a line, it is the wrong frame. Change the frame,
   not the law.

## "The headline is vague"
*Symptoms: hierarchy scored 3, anti-generic law 8 failed, the sheet feels flat.*

No layout fix will touch this. It is a content problem.

- One number, one verb, one outcome, 8–12 words.
- The pill goes on the number or the outcome, never a filler word.
- Swap test: put a competitor's name on it. If it still fits, rewrite it.

## "It looks like AI made it"
*Symptoms: anti-generic gate fails, but nothing measurable is wrong.*

Work down design-laws.md in order. It is almost always one of the first three:
floating cards, an icon per card that restates the title, or a gradient.

## `ragged-widths`
Sibling cards must share a width. In a flex column, `align-items:stretch`. In a grid,
`minmax(0, 1fr)`. The one legal exception is the Funnel frame, where cards narrow on purpose —
both checkers know about it.

## `dead-space`
*More than 120px of empty above the footer.*

Autofix grows rows, then the headline, then the cards. If it is stuck, the real answer is
usually that the sheet has one card too few for the frame — or the frame is too big for the
content. A Rail with three cards should be a different frame.

## `node-off-spine`
The node's centre is not on the line. Nodes are positioned relative to their card, so this
means the card column and the spine x-coordinate disagree.

Check: node `left` offset + half the node width must land exactly on the spine's x. In the
Rail template, card left is 148, node `left:-62px`, node width 28 → centre at 100 = the spine.

## `pill-count`
Zero pills: the headline has no pill word — pick the number or the outcome.
Two or more: delete all but the most important. Emphasis that repeats is not emphasis.

## `sub12-text`
Autofix raises it to 12px automatically. If it reappears, something is overriding the rule
further down the stylesheet — find that, do not patch it twice.

## `edge-break`
Something crosses the canvas edge. Usually a long unbroken string (a URL, a model name) in a
card. Add `overflow-wrap:anywhere` to that card, or shorten the string.

---

## The rule under all of these

**The gate is not the problem.** Every time a sheet fails, the fault is in the sheet — the
content, the frame choice, or the copy. Changing the gate to make a sheet pass means the next
forty sheets get worse, and nobody notices until the whole feed looks tired.
