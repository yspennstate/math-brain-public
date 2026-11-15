---
name: t115_gotsman_linial_asymptotic_proof_checked_in_full_2026_11_12
description: "Gotsman-Linial asymptotic bound proved (OpenAI, 25 Sep 2026, openai/math): I(f) <= 8 d sqrt(n) for degree-d polynomial threshold functions; 13-page proof read in full, each lemma verified by hand and tested numerically (n up to 8); Lean statement matches; exact form false (Chapman); do not work the row as open"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T02:50:29+02:00
  status: verified
  evidence: "06_math_research/t115_gotsman_linial_agent_2026_11_12/T115_CHECK.md, t115_check.out, t115_lemma3_const.out; push 073c7fcf78dd81c9ba6e79ddbb51a6efefc2f5be"
---

Row T115 (Gotsman-Linial) of the top-200 list is solved in its asymptotic form: OpenAI, "Average sensitivity of polynomial threshold functions", 25 Sep 2026, 13 pages, in the public repository openai/math (commit 1581d4cb, preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/main.pdf; not on arXiv). Theorem: f = sgn(p), p multilinear of degree at most d on {-1,1}^n, sgn(0) = 1, then I(f) <= 8 d sqrt(n). The exact extremal form is false (Chapman 2018, arXiv 2108.02288); symmetric examples give about 0.80 d sqrt(n).

What I did (12 Nov 2026): read Sections 1-5 in full and verified each step by hand; read Corollary 4 and Corollary 5 up to (18). Tested by computer (t115_check.py, n = 2..8, 324 polynomials, 240 random weights): edge entries of the weighted grading at most 1/2 (largest 0.500000), far energy at most diagonal energy, |E_h| <= 2 ||MH+HM||^2 (largest ratio to the bound 0.5), blocks with r + s < n - d vanish, marginals binomial, E(R+S-n)^2 <= 4 d sqrt(n) (largest ratio 0.27), Lemma 2 on 4000 chains (largest ratio 0.30). A hill-climb found no weight and sign function with |E_h| / ||T||^2 above 1 (the lemma proves 2). Lean: the statement file matches Theorem 1; Main.lean has no sorry; other files not fetched, nothing compiled. Chang-Slote-Tseng-Volberg-Zhang (arXiv 2604.08095v3) use the result.

The proof in four lines: (1) equal-law U, V with V - U <= a have E(U-V)^2 <= 8 a sigma, via g(t) = (t-m)|t-m|/2 and E g(U) = E g(V); (2) grade functions on the cube by degree with respect to the weight w = |p|: projections Pi_k of ranks C(n,k), M = sum (k - n/2) Pi_k, coordinate multiplication moves grades by at most one; (3) for a sign function h, the number of equal-sign edges is at most 2 ||MH + HM||_HS^2; (4) h = parity times f turns sensitive edges into equal-sign edges and degree <= d into the vanishing of blocks with r + s < n - d, so ||T||^2 / N = E(R+S-n)^2 with binomial marginals and R + S >= n - d.

How to use: do not work on T115 as open. Reusable: the one-sided coupling lemma; degree grading with respect to an arbitrary positive weight (fixed spectrum, moving matrix entries); anticommutator with a sign multiplication counts equal-sign edges. The catalogue https://sites.pitt.edu/~hajlasz/OpenAI_Math_Catalogue.html indexes the repository's preprints (entry 247 here) and is the place to look for the primary source of any row "credited to OpenAI". When a final bound is trivial at computable sizes, test the lemmas, not the bound.

Open next to it: the best constant between sqrt(2/pi) and 8; the exact maximizers after Chapman; whether the constant 2 in the edge-recovery lemma is 1.

What would change this: an erratum to the preprint, or a failed build of the Lean development.

