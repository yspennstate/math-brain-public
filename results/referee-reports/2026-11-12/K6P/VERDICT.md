# Q2 (r merges raise mixing time by at most r+1): check of the Codex run, 12 Nov 2026

Run: Codex gpt-6.1-sol (high, normal speed) on Mac mini 1, 21:58-22:2x +04, folder ~/agent_run/K6P. Its result: PARTIAL.

What it establishes (checked):
- Rank-r update (3): Fhat = F - F C (C^T F C)^{-1} C^T F, C the r boundary-difference columns. Matches direct hitting-time
  solves of the quotient to machine precision on 400 random 5-7 state chains with weights in 10^[-1,1]
  (indep_check_mild.py); with weights spanning 10^[-3,3] the mismatch is 7e-5 of T, which is float conditioning.
- Lemma (4), one non-singleton block B of any size: Fhat_{B,f(j)} <= t_j <= T. Proof read by hand: h = E.T_B,
  nu = (d - L h)/W is a probability on B, h - E_pi h = sum_b nu_b F_{.b} (same Laplacian, both mean zero), and the left
  side is the quotient's F entry because the chains agree off B; F symmetric for reversible chains. No gap.
  Numerically the max of (Fhat_{B,j} - t_j)/T over 400 chains is 0.0 (attained, never exceeded).
- Bound (6), two disjoint pairs: entries touching either merged pair are <= 2T (lemma 4 after Q1). Worst seen 1.06 T.
- Bound (7)/(9): the minimum-potential argument goes through for any partition when the two boundary vectors
  beta_i, beta_j are proportional. Read; not independently re-run beyond the run's own q2_audit (78,800 checks).
- Exact near-sharp families: r=2 reaches R_3 -> 3 at n=6,7,8; r=3 reaches R_4 -> 4 at n=8 (fork comb + clone padding).

What stays open: singleton-to-singleton entries with non-proportional boundary vectors (an exact 7-state witness shows
the proof method fails there; it is not a counterexample). So K(7) in {3,4}, K(8) = 4 unchanged; Q2 has no counterexample
in 2.36 M representative-level checks plus 296k optimizer evaluations, all candidates re-verified in exact arithmetic.
Also refuted inside the run: the shortcut That <= T + kappa - kappa_hat (Kemeny constant), exact counterexample.

Verdict: SOUND as a partial result. Lemma (4) is new usable content for lumping v2 (a single merged block of any size
cannot push its own row past T); the conjecture itself stays a conjecture.
