---
name: p0199_cyclic_to_random_transposition_cutoff_open_mps04_pymar_2026_11_13
description: "[PROVISIONAL] P0199 (LPW 2nd ed. Ch. 26 Question 6(a)): does cyclic-to-random transpositions have cutoff? Still open 13 Nov 2026; order n log n (MPS04), upper n log n + O(n) (SCZ07, Ganapathy 07), lower about 0.12 n log n (Pymar 1302.2601); no 2018-2026 paper settles it"
metadata:
  node_type: memory
  status: provisional
  type: project
  modified: 2026-11-13T20:53:27.402Z
---

P0199, our 200-list rank 62. The shuffle: at step t, transpose card position t mod n with a uniform random position.
Question (Levin-Peres-Wilmer, 2nd ed., Chapter 26 open problems, Question 6(a)): does it show cutoff, and where?

Literature state, checked 13 Nov 2026 (arXiv API, the 25 Semantic Scholar citers of math/0404438, the 2026 Monte shuffle paper):
- Mossel-Peres-Sinclair 2004 (math/0404438): mixing time Theta(n log n) for any semi-random transposition shuffle.
- Saloff-Coste and Zuniga 2007, and Ganapathy 2007: upper bound n log n + O(n), optimal over all fixed position sequences (star transpositions attain it), not shown sharp for the cyclic sequence.
- Pymar 2013 (arXiv 1302.2601): best lower constant, about 0.12 n log n for cyclic-to-random; says cutoff is open.
- Pinsky 2012 (1204.2081): related lower-bound work.
- 2018-2026 citers: 1805.10508 (cyclic ADJACENT transpositions, a different model), 2102.08002, 2609.13570, 2611.03959 (Random-Pair Monte shuffle, public schedule; cites MPS04, SCZ07, Gan07 only as background). None settles cyclic-to-random.
- Do not confuse with Morris-Ning card-cyclic-to-random (a different shuffle, constant 6.59 there).

Prior brain work: one Codex attempt 2026-09-06 (P0199-A001), the one-card marginal update; no cutoff result.
Gap to close: the leading constant lies somewhere in [~0.12, 1]; cutoff needs matching bounds. What would change this note: a paper giving a lower bound near the upper constant, or a test-function lower bound beyond the untouched-card count.
