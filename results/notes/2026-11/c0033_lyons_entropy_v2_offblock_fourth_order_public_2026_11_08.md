---
name: c0033_lyons_entropy_v2_offblock_fourth_order_public_2026_11_08
description: "[VERIFIED] C0033 Lyons DPP entropy concavity v2 public 8 Nov: off-block second derivative 0 at reducible Q, entropy drops at t^4 (quartic inf 2/1/0.5), exact-Hessian max 0 to rounding n<=4; repo 68c26982, ledger f5236816"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T07:49:07+02:00
  status: verified
  evidence: "github.com/yspennstate/lyons-determinantal-entropy-two-points main 68c26982 (ls-remote); open-problems-repo master f5236816; six regenerated outputs in papers_agent/C0033 matched main.tex"
---

C0033 (Lyons, Publ. IHES 2003 Conj. 9.2 = ICM 2014 Conj. 2.6: Ent(P_Q) concave in Q). Version 2 public 8 Nov 2026.

- Repo yspennstate/lyons-determinantal-entropy-two-points, main 68c26982713a4c82c362ea739f682fc36efbca2e (v1 was 678294046a).
- Ledger: open-problems-repo master f5236816d6fd295ea47245681988939f7181293f [skip ci]; POSTED.md row C0033 text updated, a new C0033 record appended to probability_1000_intake_agent/problems.jsonl (status partial_2026_11_08).
- New mathematics in v2: at a reducible kernel Q = Q1 (+) Q2 the second derivative vanishes in every off-block direction D, and Ent(Q+tD) = Ent(Q) - (t^4/2) sum_S r_S^2/p_S + O(t^6). So the Hessian is singular there, and concavity is decided at fourth order. Infimum of the quartic coefficient: 2 (n=2), 1 (n=3, blocks 1+2), 0.5 (n=4, blocks 2+2), real and complex.
- Numerics: the exact Hessian (p_S = det M_S, Jacobi's formula) maximised by Nelder-Mead over Q = U diag(sigma(x)) U*. Largest eigenvalue at most 7.1e-15 (real) and 4.1e-15 (complex) for n <= 4, and every maximiser is reducible. At 40 random kernels the medians are -0.10 (n=3) and -0.034 (n=4). No counterexample.
- Audit: all six cited outputs were regenerated from scratch (run_v2_outputs.py) and matched the paper's text digit for digit. paper_release_guard ok, 0 Overfull, secret scan clean on both pushes.
- Open: general |E|. An n=5 complex search is running (start 0 top eigenvalue 2.4e-15) and is not in the repo yet; build_repo.py skips _n5_ files until it finishes.
- Lesson: the honest picture of the near-counterexample is "the Hessian maximum is 0 at reducible kernels", not "the Hessian is negative". Any concavity search that reports a top eigenvalue near 0 should test reducibility before calling it evidence of a violation.

Builds on [[c0033_lyons_entropy_concavity_2x2_proved_2026_10_30]] and [[prob1000_claude_intake_ledger_and_lyons_partials_2026_09_07]].

