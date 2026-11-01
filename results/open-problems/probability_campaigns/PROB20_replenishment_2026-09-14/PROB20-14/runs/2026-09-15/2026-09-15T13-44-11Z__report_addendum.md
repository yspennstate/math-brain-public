# PROB20-14 — addendum / correction to 2026-09-15T13:44:10Z report

**SOLUTION STATUS: PARTIAL (unchanged).**

This addendum corrects one sentence in Section 7 of the immediately preceding report. The report said that on the non-negligible prefix region both `N=o(n)` and `L=o(n)`. The argument established earlier does **not** require or generally prove `N=o(n)`.

The correct statement is:

- the small-remainder contribution `m=n-N<delta n` is negligible for a fixed sufficiently small `delta=delta(k)>0` by the factor-two downward-jump argument;
- hence on the remaining non-negligible region one may assume `m>=delta n`;
- the universal escape theorem gives `L<c_n` outside a negligible contribution, with `c_n=o(n)`;
- therefore `L=o(n)=o(m)` on this region because `m>=delta n`.

This is exactly what Theorem 4.1 needs. No claim `N=o(n)` is used.

Thus the fixed-level consequence of the canonical recentering theorem remains valid in the form intended: after discarding the already-proved negligible regions `m<delta n` and `L>=c_n`, every remaining prefix has a residual allocation with sample size `m` and deficit `L=o(m)`, so its exact conditional law can be recentered by a one-site law converging to the original offspring law in `W_q`.

No other statement in the report is changed by this correction.
