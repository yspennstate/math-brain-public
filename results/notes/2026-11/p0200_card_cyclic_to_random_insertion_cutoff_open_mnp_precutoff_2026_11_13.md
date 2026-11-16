---
name: p0200_card_cyclic_to_random_insertion_cutoff_open_mnp_precutoff_2026_11_13
description: "[PROVISIONAL] P0200 (LPW 2nd ed. Ch. 26 Question 6(c)): does card-cyclic-to-random insertion have cutoff? Still open 13 Nov 2026; Morris-Ning-Peres 1207.3406 prove pre-cutoff, 0.1619 n log n <= t_mix <= 6.5866 n log n, and name cutoff as open; Jonasson 1501.05485 (relabeling variant) also n log n; no later paper settles it"
metadata:
  node_type: memory
  status: provisional
  type: project
  modified: 2026-11-13T21:27:13.070Z
---

P0200, our 200-list rank 63. The shuffle: at time t remove the card with LABEL t mod n and reinsert it at a uniform position.
Question (Levin-Peres-Wilmer, 2nd ed., Chapter 26, Question 6(c)): does it show cutoff?

Literature state, checked 13 Nov 2026 (arXiv API searches "card-cyclic", "cyclic-to-random", systematic-scan shuffles,
insertion-shuffle cutoff; the 13 Semantic Scholar citers of 1207.3406):
- Pinsky 2011 (1105.3618): introduced it; one sweep of n insertions does not mix.
- Morris, Ning, Peres 2012 (1207.3406): Theorem 1, t_mix(eps) >= c n log n for every c < c0 = 1/(2+2a) = 0.161875...
  (a the smallest positive solution of b = e^a sin b, a = e^a cos b - 1); Theorem 2, t_mix(eps) <= C(n log n - 2n log eps)
  with C = 1/(log 2 - log(e-1)) = 6.58664655... Their remark after Theorem 2: pre-cutoff holds, "an interesting open
  problem to determine if cutoff occurs". Lower bound comes from a one-card position statistic f converging to a
  constant at an oscillating (complex-root) rate; upper bound from a coupling.
- Jonasson 2015 (1501.05485): the variant that relabels by position after each round also mixes in order n log n.
- Later citers (1703.06210 and 1805.10508 random-to-random / cyclic adjacent transpositions, 2609.13570 q-deformed
  shuffles, 2601.20020) cite it as background; none proves or refutes cutoff for this chain.
- The 6.59 constant is the MNP upper bound for THIS shuffle; P0199 (cyclic-to-random transpositions) is a different chain
  with bounds ~0.12 and 1 - see [[p0199_cyclic_to_random_transposition_cutoff_open_mps04_pymar_2026_11_13]].

Prior brain work: Codex P0200-A001 (6 Sep 2026): after one full sweep on three cards the law is 5/27 on 123,132,312 and
4/27 on the rest, distance 1/18 from uniform, so "every label updated once" is not a strong stationary time. Rechecked by
hand 13 Nov: correct.
Gap: the constants differ by a factor of about 40. A cutoff proof needs a lower bound from a statistic that sees many cards
at once (the one-card f gives only 0.16), or an upper bound near the lower one. What would change this note: a paper
giving either, or a computation of the second eigenvalue of one round as n grows.
