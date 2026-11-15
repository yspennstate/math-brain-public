---
name: perceptron_capacity_source_numbering_ding_sun_huang_nakajima_2026_11_12
description: "[VERIFIED] Citing Ding-Sun, Huang or Nakajima on Ising perceptron capacity? Exact numbers read from the arXiv PDFs 12 Nov: Ding-Sun 1809.07742 Lemma 7.1 stationarity, Cor 7.2 G* decreasing, Lemma 7.3 P and R nondecreasing (NOT 7.2), eq (4) plus sign; Huang 2404.18902 Cond 1.3 two-variable, 3.1 fixed point, 3.3 AMP, 3.4 local concavity, Thm 3.6 general kappa, display (14) has a sign typo, Lemma 7.15 tilt identity; Nakajima eq (18) is the dR/dq formula, stated for kappa>=0, sign-free"
metadata:
  type: reference
  created: 2026-11-12
  created_at: 2026-11-12T10:40:13+02:00
  status: provisional
  evidence: ""
---

Read from the three arXiv PDFs on 12 Nov 2026 while rewriting the margin paper (yspennstate/ising-perceptron-margin, commit b73eff6).

- Ding and Sun, arXiv:1809.07742: Lemma 7.1 is stationarity of the free energy on the fixed-point branch; Corollary 7.2 says G_star is decreasing in alpha; Lemma 7.3 says P and R are nondecreasing (the paper had cited 'Lemma 7.2' for monotonicity of R - wrong). Their eq. (4) carries the plus sign on the alpha E log Psi term.
- Huang, arXiv:2404.18902: Condition 1.3 = the two-variable inequality; 3.1 = fixed point and contraction on a rectangle; 3.3 = AMP stability; 3.4 = local concavity, where ell is defined; Theorem 3.6 = the general-kappa upper bound under 1.3, 3.1, 3.3, 3.4. Display (14) has -alpha E log Psi, a sign typo (the fixed-point equations need +). Lemma 7.15 is the tilt identity. Proposition 3.2 is the author's kappa=0 instantiation with a 1e-9 interval.
- Nakajima (nakajima2025) eq. (18): B'(q) for B=(1-q)E[E(u)^2], R = alpha B/(1-q)^2; stated for kappa>=0, but the computation does not use the sign of kappa.
- Gordon 1941 (Ann. Math. Statist. 12, 364-366) gives V < E(V) < V+1/V for the inverse Mills ratio; Sampford 1953 gives 0 < E' < 1. Talagrand's capacity <= 1-eps is Ann. Probab. 28 (2000) 725-758 (talagrand2000), not the 1999 RSA paper.

How to apply: cite with these numbers; if a later arXiv version renumbers, re-read the PDF rather than trusting this list. Related: [[paper_commit_inputs_an_untracked_file_builds_locally_only_2026_11_12]] [[pw1k_thousand_paper_writing_rules_one_word_one_thing_2026_11_12]]
