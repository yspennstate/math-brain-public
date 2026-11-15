# Second check of the lumping results of 12 November

Checked: the upper bound K(n) <= max(1, n-2), the four-state family giving K(4) = 2, and the fork comb giving
K(n) >= floor(n/2) (reports `../LUMP/REPORT.md` and `../K5/REPORT.md`).

Route. The two earlier rechecks solved hitting-time systems. Here the stopping-rule mixing time is taken from the
fundamental matrix, tmix = max over i, j of -Z_ij / pi_j with Z = (I - P + 1 pi^T)^{-1} - 1 pi^T, in exact rational
arithmetic, and in floating point it is compared with direct hitting-time solves on every random chain.
Script `audit_lumping.py`, output `audit_lumping_out.txt`.

Results (0 checks failed).

1. Four-state family (w02 = w12 = 1, w03 = w13 = t, loops t^2 - 1 at 0 and 1, t^6 at 3, lump {2,3}). With
   D = t^6 + 2t^2 + 4t + 2 the closed forms tmix(X) = (t+1)(t^6 + t^5 + 4t + 2)/D and
   tmix(quotient) = 2t(t^6 + t^2 + 3t + 2)/D hold exactly at t = 2, 3, 7, 10, 100, 10^6. The ratio is 0.955974842767
   at t = 2 and 1.999996000006 at t = 10^6, below 2 throughout.
2. Fork comb on 2N+4 states, N = 0, 1, 2, 3. Ratios at t = 10^3: 1.998000000002, 2.993012973055, 3.986037899261,
   4.977082713970; at t = 10^5: 1.999980000000, 2.999930001300, 3.999860003800, 4.999770008300. The first three agree
   with the table in `../K5/REPORT.md` to twelve digits; N = 3 (ten states) is new here. The gap to N+2 shrinks about a
   hundredfold between the two values of t and stays positive.
3. Random search, 6,000 reversible chains on 3 to 6 states with weights spread over six orders of magnitude and 32,988
   (chain, partition) pairs: no violation of tmix <= tau0, of tau0 <= (q-1) tau2, of tau2(quotient) <= tau2(X), of
   tau2 <= tmix, or of tmix(quotient) <= (n-2) tmix(X). The two routes to tmix agree on every chain. Largest ratio a
   blind search finds: 1.0000 (n = 3), 1.3326 (n = 4), 1.3249 (n = 5), 1.1967 (n = 6), so the extremal families are
   not found by sampling.

Remarks for the paper.

- The step tau2(quotient) <= tau2(X) is the variational one: a function on the quotient lifts to a function on X with
  the same Dirichlet form and the same variance, so the quotient's spectral gap is at least that of X. No eigenfunction
  of the quotient needs to be an eigenfunction of X.
- tau2 <= tmix is used in discrete time with tau2 = 1/(1 - lambda_2), lambda_2 the second largest eigenvalue (not in
  absolute value). It is an equality for the walk on the complete graph without loops, where both sides are (n-1)/n, so
  the paper should state which relaxation time is meant and cite or prove the inequality in that form.
- K(3) = 1: the bound max(1, n-2) gives 1 and the random search never exceeds 1.0000 on three states.
- K(5): this audit left it between 2 and 3. A later note of the same day (referee_reports/2026-11-12/K5P/REPORT.md) proves that merging one pair at most doubles the mixing time, which gives K(5) = 2. That proof was not checked here.
