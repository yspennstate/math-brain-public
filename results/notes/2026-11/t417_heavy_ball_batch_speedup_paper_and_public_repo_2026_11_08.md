---
name: t417_heavy_ball_batch_speedup_paper_and_public_repo_2026_11_08
description: "[VERIFIED] T417 momentum vs SGD at batch B: paper + public repo yspennstate/heavy-ball-batch-speedup (1dbf756), 8 Nov"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T11:26:18+02:00
  status: provisional
  evidence: ""
---

T417 (heavy-ball momentum vs SGD, Gaussian streaming least squares, batch B) is now a paper with a public repo: https://github.com/yspennstate/heavy-ball-batch-speedup (head 1dbf7562, 8 Nov 2026, papers loop T-20261107-015). Result: max(1,m/16) <= (1-rho_HB*)/(1-rho_SGD*) <= (128/3)m, m=min(max(1,B hmax/trH),sqrt kappa); explicit tuning delta=min(1,2/sqrt kappa,B hmin/trH), sqrt beta=1-delta/2, eta=delta^2/(4hmin) gives rho<=1-delta/4; exact mean-square stability edge (D_j>0, S<1). Attribution: the upper bound on the HB gap is Thm 1 of Morwani-Meterez-Nair-Kakade arXiv:2606.19179 (they left achievability open). Proof re-audited by hand and by new code checks.py (2000 random instances pass). Table 1 comes from the October grid runs (grid_powerlaw.py). Ledger: brain_math_loop_1e0a/papers1107/LEDGER.jsonl. Status verified; what would change it: a counterexample to Lemma 5.2's endpoint polynomials (checked symbolically). Related: [[t417_tuned_heavy_ball_speedup_theta_min_bhmax_trh_sqrt_kappa_proved_2026_10_18]]
