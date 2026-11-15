---
name: p0050_fsf_wsf_singularity_open_bounded_cycles_partial_2026_11_13
description: "[PROVISIONAL] P0050 (Lyons-Peres Q10.58 in the 19 Aug 2026 edition, Q10.59 earlier): FSF != WSF => mutually singular? Still open; known for trees, infinite automorphism orbit, and bounded simple cycles (Shi-Sidoravicius-Song-Wang-Xiang 2018)"
metadata:
  type: project
status: provisional
---
P0050, rank 3 on the 200 list. Question: if the free and wired uniform spanning forests of an infinite network differ, must they be mutually singular?

Literature, checked 13 Nov 2026 (two web searches, the arXiv PDF read):
- Still printed as open in Probability on Trees and Networks, 19 Aug 2026 edition, Question 10.58 (p.385). The book itself gives the known cases: trees, and networks with an infinite automorphism orbit (so every transitive graph is settled).
- The question goes back to Benjamini-Lyons-Peres-Schramm, Uniform spanning forests (Ann. Probab. 29, 2001).
- Shi, Sidoravicius, Song, Wang, Xiang, arXiv 1805.01615 (2018), Theorem 4.3: if the simple cycles of G have uniformly bounded length, the FSF is a.s. one tree, for any positive conductances. Remark 4.4: if in addition G minus a ball has two disjoint transient components, the WSF has at least two trees a.s., so FSF and WSF are mutually singular. Their Section 4.2 notes that the general DPP version (distinct closed subspaces give singular determinantal measures) is false (Lyons, DPP paper, p.203), so no abstract argument settles it.
- Related, not an answer: arXiv 2006.06387 (the FSF is disconnected on some virtually free groups, depending on the generators), and Hutchcroft-Nachmias indistinguishability, arXiv 1506.00556 (FSF != WSF implies every FSF tree is transient).
- No paper found that settles the general case.

What is left open: networks with only finite automorphism orbits and unbounded cycles. A natural route is through tree counts: two measures whose a.s.-constant numbers of trees differ are singular. But the FSF tree count is not known to be a.s. constant in general (Lyons-Peres Q10.28), so this route is blocked at the same place.

Where this sits: 200-list LITERATURE_UPDATES row 13 Nov (open). No attempt beyond the literature. How to apply: before working P0050, start from the 2018 bounded-cycle theorem and the finite-orbit gap above; do not re-search the abstract DPP route.
