---
name: writing_hook_fired_on_negated_and_far_apart_words_2026_11_14
description: "The writing-brain hook decided whether a prompt asked for writing by finding a write verb anywhere and a writing noun anywhere. It fired on negated asks ('don't keep rewriting ...') and on prompts where the two words sat 300 characters apart. Fixed by dropping negated phrases and requiring the verb within 60 characters of the noun; 17 times faster as well."
metadata:
  type: project
  created: 2026-11-14
  status: verified
---

The writing-brain hook adds writing-craft cards to a session when a prompt asks for writing. It decided this with
two regular-expression look-aheads over the whole prompt: a write verb anywhere, and a writing noun (paper,
chapter, script, draft, and so on) anywhere. Two faults:

1. Negated asks fired. A standing loop prompt that told agents not to keep rewriting a draft pushed literature
   cards into every tick of every session it ran in: 14 of 72 fires over the owner's last 1,000 prompts. Now a
   negated phrase (don't, do not, never, stop, no more, quit, followed by the verb and up to four words) is removed
   before matching.
2. Far-apart words fired. A prompt that said "fix bugs in the brain" and, 300 characters later, mentioned images
   for a chapter, fired; so did a request for an email draft that mentioned a script elsewhere. Now the verb must
   sit within 60 characters of the noun. Plurals (papers, preprints) and common misspellings of "reword" were added
   so that "writing papers" still fires.

Measured on a frozen snapshot of the last 1,000 prompts: 61 fires before, 53 after, and the spans that still fire
read as real writing asks. The look-ahead form was also slow, 0.40 seconds on a 600-character prompt against
0.024 seconds now, paid on every prompt in every session.

How to apply: when a hook keys on words in a prompt, test it on the real prompt history (snapshot it first, since
the store rebuilds hourly), and read the matched span, not just the count of fires. A loop prompt repeats dozens of
times, so one wrong fire on it multiplies. A known remaining miss: a request to open browser tabs that mentions
"the chapter written" still fires.
