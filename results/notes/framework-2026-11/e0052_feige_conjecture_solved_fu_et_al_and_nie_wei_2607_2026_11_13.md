---
name: e0052_feige_conjecture_solved_fu_et_al_and_nie_wei_2607_2026_11_13
description: "E0052 (Bandeira 42 problems, Open Problem 4.6 / Conjecture 4.33 = Feige's conjecture: independent X_i >= 0 with E X_i = 1 have P(S < n+1) >= 1/e) is solved in two July 2026 preprints: Fu-Han-Wang-Yan-Zhang-Zhou arXiv 2607.23980 (sharp (1-1/(n+delta))^n for delta >= 1) and Nie-Wei arXiv 2607.24528 ((n/(n+1))^n); both AI-assisted (GPT 5.6) and both built on Vlassis-Thomas's proof of Gaffke's conjecture; unrefereed"
metadata:
  node_type: memory
  status: provisional
  type: project
  originSessionId: agent-66b6-4575-b3c4-a8807fd17369
  modified: 2026-11-13T15:02:35.100Z
---

E0052, rank 34 on the 200 list. Source: Bandeira, "Ten lectures and forty-two open problems in the mathematics of data
science", Open Problem 4.6 / Conjecture 4.33, which is Feige's conjecture (Feige 2004/2006): X_1..X_n independent,
X_i >= 0, E X_i = 1, then P(S < n+1) >= 1/e. The list entry words the event as "P(sum <= n+1) >= 1 - 1/e", but its own
extremal example (X_i = n+1 with probability 1/(n+1)) has P(S >= n+1) = 1 - (n/(n+1))^n, so the intended statement is
P(S >= n+1) <= 1 - 1/e, i.e. Feige's. Our R7-03 run (17 Sep) had already untangled the same event mix-up.

Solved, abstracts read 13 Nov 2026 (neither paper refereed; both say the proof was found with GPT 5.6):
- Fu, Han, Wang, Yan, Zhang, Zhou, "Sharp small-deviation inequalities for sums of independent nonnegative random
  variables", arXiv 2607.23980 (27 Jul 2026): with E X_i <= 1, P(S < E S + delta) >= delta (n/(n+delta))^n for
  0 < delta < 1 and >= (1 - 1/(n+delta))^n for delta >= 1, sharp for every n and delta >= 1. Delta = 1 gives Feige with the
  sharp finite-n constant (n/(n+1))^n. Ingredients: Vlassis-Thomas 2026 (exact Dirichlet calibration, which settles
  Gaffke's conjecture), Grunbaum's centroid theorem, Letwin-Yaskin 2024.
- Nie, Wei, "On Feige's conjecture", arXiv 2607.24528 (same day): a short proof of P(S < n+1) >= (n/(n+1))^n >= 1/e, also
  from Vlassis-Thomas.
Before these the best constants were Feige 1/13, Garnett about 0.14, and later moment and Berry-Esseen improvements
(arXiv 2003.03197 and others; their exact constants, about 0.18, are from memory and were not re-read). A 2025 claim attributed to Durr is only an equivalent reformulation with a sketch, not a proof.

The intake ledger already had this as resolved (12 Nov). The abstract claims sharpness only for delta >= 1; whether the
delta < 1 bound is sharp is a possible follow-up, not the list's question.
Related: [[p0015_vinzant_4m_minus_5_phase_retrieval_solved_li_2606_17922_2026_11_13]] (another 200-list item settled by an
AI-assisted July 2026 preprint).
