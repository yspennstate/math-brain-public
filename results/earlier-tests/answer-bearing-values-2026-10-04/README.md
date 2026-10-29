# Answer-bearing values in recall (4 and 5 October 2026)

When a question asks for a value, recall can rank a card that only restates the question above the card that states
the answer. A scheduled diagnosis on six delivery cases found two faults behind this. On three of the six, the one-hit
cut went to a short layout or notation card that repeated the question's words, with the answer card at rank 2 every
time; the square-root length divisor in every channel and the title-phrase bonus put it there. On four of the six, the
passage served from the right card held the problem's opening rather than the closing sentence that states the result.

## The rule

A question is value-seeking when it asks how many, asks to compute or give a quantity, or asks for a probability, and
does not ask for a definition, a statement or a proof. For such a question, a card that states no numeral beyond the
question's own and its own assumptions has every support channel scaled by 0.5; its warnings are untouched. The passage
window is chosen the old way first, and only when that window states no such value does it move to the best-matching
sentence that does and is not marked obsolete, superseded or incorrect. Numerals inside names (K4, a_4, page numbers)
are not values; a numeral glued to a word, as notes are often written, is. Both halves have their own switch.

## Measured

On the six diagnosis cases, selection went from 3 to 6 and complete passages from 2 to 5. The case still missed has a
setup sentence that states the answer's own value.

The factor was fixed at 0.5 before the outside check was run: the 200 store-dependent questions of the hard 300 on the
live store, each run through retrieve() twice in one process with only the switch flipped.

| questions | n | first place (off / on) | first five (off / on) | MRR (off / on) | ranks changed |
|---|---|---|---|---|---|
| all | 200 | 67 / 67 | 113 / 115 | 0.434 / 0.438 | 10, all better |
| value-seeking | 146 | 39 / 39 | 71 / 73 | 0.367 / 0.373 | 10, all better |
| not value-seeking | 54 | 28 / 28 | 42 / 42 | 0.615 / 0.615 | 0 |

The answer was in the served passage on 134 questions instead of 132, and none was lost. Two variants fail this check.
Choosing the window by value as a preference, rather than as a fallback, lost four answers on cards whose
windows already held the answer, moving them onto citation pages, item numbers and parameters. A numeral pattern that
skipped every digit after a letter read a window holding the answer as empty.

Later versions read hedges that mark a value as a draft or unchecked (on a fresh set of twelve long cases, 3 to 8),
scope a hedge to its own subject, and keep hedges on the work behind a value. Not yet tested: a value question whose
answer is symbolic or written in words. Neither bank has one, and on such a question the rule would demote the right
card because it states no numeral.
