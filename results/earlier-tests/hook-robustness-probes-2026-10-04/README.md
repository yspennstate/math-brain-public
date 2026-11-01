# Three probes of the math hook (4 October 2026)

The math hook reads a prompt, decides whether it is a mathematical question the store can help with, and if so serves a
block of a few cards. Three probes on 3 and 4 October asked how it behaves away from the banks it was tuned on: under
rewrites that keep a question's meaning, on claims the store's own graph says are refuted, and whether the meaning channel
could let through prompts the entry gate refuses. All three ran the live hook in-process with its 30-second clock lifted.

## 1. Meaning-preserving rewrites

218 questions of the fresh bank (178 with a known card, 40 whose answer is not in the store) were each
rewritten in up to seven ways, 1,427 prompts counting the originals. On the originals the hook served the known card on 158 of
178, first on 139, and fired on 27 of the 40 absent-target questions. A break is a question
whose original served the known card and whose rewrite did not.

| rewrite | answerable | served | first | breaks | same top card | absent fires |
|---|---|---|---|---|---|---|
| real misspellings from a reviewed list | 100 | 91 | 79 | 0 | 98 | 11 of 15 |
| lower case, no punctuation | 178 | 156 | 134 | 2 | 166 | 26 of 40 |
| a polite wrapper ("can you tell me ...") | 178 | 155 | 136 | 3 | 163 | 20 of 40 |
| clauses swapped | 4 | 3 | 3 | 0 | 4 | 0 of 0 |
| synthetic character typos on content words | 178 | 96 | 80 | 66 | 78 | 20 of 40 |
| instruction text before the question | 178 | 129 | 112 | 30 | 135 | 11 of 40 |
| instruction text after the question | 178 | 137 | 121 | 23 | 141 | 14 of 40 |

Real misspellings, lower case and polite wrappers are harmless. Synthetic typos and instruction text are not: typos
dropped the served count from 158 to 96, and instruction text before or after the question broke 30 and
23. The instruction-text failures come from the coverage gates, which silence the whole prompt, answerable or not;
the same text also quieted the false fires on absent-target questions (from 27 to 11 and 14).

Both weaknesses were checked against real use before anything was changed. A spelling corrector over the store's
vocabulary, with guards against correcting English words and names, restored every misspelt word in 84 of the 218 typo
questions. Run over an archive of 18,900 real prompts it changed 3,132 of them, mostly common words, altered LaTeX and
code tokens (bigsqcup to bigcup, readonly to readily) and opened the gate on 19 prompts it had refused, nearly all
instructions that mention mathematics rather than questions. The coverage gates, joined to the production silence log,
had silenced four real prompts in 30 days, all of them instructions. Neither change was made. A weakness a rewritten
bank shows is a hypothesis about real traffic until it is found there.

## 2. Refuted targets

The store records 47 REFUTES edges. Read one by one with their rationales, about 23 refute the target claim or
answer its open problem in the negative, about 19 leave the target standing (a failed route to a proved result, a
refuted citation, a hypothesis shown necessary, a counterexample to a weakening, one setting where an estimator does
badly), and 3 point the wrong way. Fekete's subadditive lemma is a REFUTES target. An edge of this kind therefore does
not mean its target is false, and no status or warning may be keyed on the kind alone.

The hook was asked about each of the 34 targets in two framings ("is it true that ...", "what is known about ...").
It served a block on 42 of the 68 calls and the target itself on 34 (first on 6), each time with its refuter beside it; on
22 of those the block contained a word of refutation. The hook does not label a card refuted, which on this
reading of the edges is the right behaviour.

## 3. Could the meaning channel open the gate?

For each prompt the probe recorded the meaning channel's winning card, its cosine in standard deviations above the mean
over all claims (z1), the margin to the runner-up, and the winner's rank in the lexical pool. Three populations: 32
reworded questions that the gate refuses and whose card is known, the 4 absent-target questions it refuses, and
13,351 real prompts it refuses. A threshold set would admit a refused prompt when all three numbers clear it.

| z1 at least | margin at least | lexical rank at most | right winner, of admitted | absent fires | real prompts admitted |
|---|---|---|---|---|---|
| 4.0 | 0.0 | 10 | 5 of 13 | 2 | 307 |
| 4.0 | 0.0 | 300 | 5 of 17 | 2 | 1307 |
| 4.0 | 1.0 | 10 | 2 of 5 | 0 | 36 |
| 4.0 | 1.0 | 300 | 2 of 5 | 0 | 100 |
| 5.0 | 0.0 | 10 | 3 of 9 | 1 | 64 |
| 5.0 | 0.0 | 300 | 3 of 11 | 1 | 235 |
| 5.0 | 1.0 | 10 | 2 of 4 | 0 | 27 |
| 5.0 | 1.0 | 300 | 2 of 4 | 0 | 65 |
| 6.0 | 0.0 | 10 | 1 of 2 | 0 | 14 |
| 6.0 | 0.0 | 300 | 1 of 2 | 0 | 33 |
| 6.0 | 1.0 | 10 | 1 of 2 | 0 | 9 |
| 6.0 | 1.0 | 300 | 1 of 2 | 0 | 18 |
| 7.0 | 0.0 | 10 | 0 of 0 | 0 | 3 |
| 7.0 | 0.0 | 300 | 0 of 0 | 0 | 7 |
| 7.0 | 1.0 | 10 | 0 of 0 | 0 | 3 |
| 7.0 | 1.0 | 300 | 0 of 0 | 0 | 7 |
| 8.0 | 0.0 | 10 | 0 of 0 | 0 | 1 |
| 8.0 | 0.0 | 300 | 0 of 0 | 0 | 1 |
| 8.0 | 1.0 | 10 | 0 of 0 | 0 | 1 |
| 8.0 | 1.0 | 300 | 0 of 0 | 0 | 1 |

No threshold separates the right winners from the wrong ones. The loosest sets recover 5 of the 32 with 8 to 12 wrong
winners beside them and admit 300 to 1,300 refused real prompts; the strictest that still admit a right card admit one,
with one wrong winner and 9 to 33 real prompts; above z1 = 7 nothing right gets through. The confidence of the meaning
channel says no more about whether its winner is right than its raw cosine does. The existing route for these
questions, which admits a prompt holding two or more of the store's own terms, already reaches 20 of the 32, so the
gate is not where most of them are lost. The meaning channel was not turned into an entry route.

## Files

`SUMMARY.json` holds every count above: each rewrite's counts, the refuted-target counts, and all 45 threshold cells.
Each was recomputed from the per-prompt rows and matches the run's own summary or log. The rows themselves are not
published, because they carry the questions, the store's card ids and the real prompts.
