# FIX RECIPES

What to actually do when the gate fails, ordered by how often each comes up.

---

## "The spotlight is not earned"
*Symptoms: aspect 2 below 5; the lit card feels arbitrary; it only wins on colour.*

1. Write `WHY LIT` in one sentence. If you cannot, nothing deserves the light; re-cut the
   content until one item clearly matters most.
2. Move it off the top-left. In first position it reads as "first", not "chosen".
3. Give it a tag that says why: "Start here", "Biggest gap", "#1".
4. Check the grey render. If it disappears without colour, give it position (centre of the
   grid, top of a podium) and size, not more glow.

## "Too much content"
*Symptoms: `footer-collision`, `overflow`, autofix STUCK.*

1. **Cut a card.** Four strong beat six with passengers.
2. **Cut words, not size.** Card body is 14–24 words.
3. Only then adjust heights, and autofix already tried that before it gave up.

## "The fire is everywhere"
*Symptoms: aspect 7 below 5; the sheet feels loud but nothing stands out.*

Count the gradient: fire word, spotlight, tag pill, send circle. Anything beyond those four
goes back to Char or White. Card titles in Ember are the usual leak; set them back to White.

## "The stage looks muddy"
*Symptoms: aspect 3 below 5; the black reads grey or brown.*

The ember glow is too strong or too large. Keep it to one radial at about 20% opacity, from a
corner, and never behind body text. Two glows read as two light sources and kill focus.

## "The headline is generic"
*Symptoms: anti-generic law 8; aspect 5 at 3.*

- Bold the subject, keep the promise regular.
- The fire word is the **outcome**: Noticed, Chosen, Booked, Seen. Not "AI", not "LinkedIn".
- Swap test: put a competitor's name on it. Still fits? Rewrite.

## `spotlight-count`
Zero: pick the card that matters most and add `spotlight` to its class. Two or more: keep the
one with the strongest `WHY LIT`, demote the rest to quiet cards.

## `fire-count`
The fire word is missing, doubled, or outside `.h1`. One `<span class="fire">` inside the
headline, with any punctuation inside the span so it does not sit detached.

## `ragged-widths`
Grid columns must be `repeat(2, minmax(0, 1fr))`. Podium and Ladder differ on purpose and are
exempt when the frame name is in the filename.

## `dead-space`
Usually one card too few for the frame. A Spotlight Grid with three cards should be Hero + Stack.

## `edge-break`
A long unbroken string, usually a URL or a model name. Add `overflow-wrap:anywhere` to that
card, or shorten the string.

---

## The rule under all of these

**The gate is not the problem.** When a sheet fails, the fault is in the content, the frame or
the copy. Loosening the gate to pass one sheet makes the next forty worse.
