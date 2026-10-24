# P0282 idea before validation — sixth-order Plancherel centering and a possible n^(7/8) defect window

Date: 2026-09-19 UTC  
Track: `proofnet24/NM13-07`  
Canonical claim: `P0282`  
Entry frozen metric: `N_exact = 95`

The predecessor proved the `n^(6/7)` long-LIS defect window by expanding

`G_j(t)=log E_Plancherel(j)[exp(F_mu(t))]`, `t=1/n`,

through order five and bounding the analytic tail by Cauchy on `|t|<=1/(6j)`.

This run first tries to **refute** the natural next-step hypothesis: that the sixth Taylor coefficient `D_6(j)` still has favorable Chen discrete curvature. If the curvature changes sign, record the obstruction rather than forcing another exponent claim.

The sixth coefficient should require only two new Plancherel moments beyond the predecessor:

- `E[S_2^2]`, because `Var(B_3)` enters at total order six;
- `E[C S_3]`, because `Cov(B_2,B_4)` enters at total order six.

Both should admit exact regular-representation counts. The expected route is:

1. write `P_2=sum_i X_i^2 = binom(j,2)e + K_3`, where `K_3` is the sum of all 3-cycles; then the identity coefficient of `P_2^2` gives `E[S_2^2]`;
2. count length-three star-transposition words in `P_3=sum_i X_i^3` that reduce to a transposition; multiplying by the transposition class sum gives `E[C S_3]`;
3. substitute these moments into the exact cumulant formula for `D_6(j)` and factor the Chen second difference;
4. only if that factor is positive for all relevant `j`, reuse the predecessor's analytic disk to bound the post-sixth-order tail and test an `n^(7/8)` theorem;
5. independently move the frozen finite metric by adapting the archived Gessel/Toeplitz low-seam checker from row 95 to row 96.

Actual Section-B moves planned/used in this route:

- **#2 ATTACK THE NEGATION FIRST** — search exactly for a sign failure in the sixth-order discrete curvature before attempting a theorem;
- **#25 COUNT THE SAME THING TWICE** — identify the needed Plancherel moments both as tableau-content expectations and as identity coefficients / class-word counts in the regular representation;
- **#7 TAKE THE LIMIT** — if the new coefficient stays favorable, convert one more analytic Taylor order into a larger growing-defect asymptotic window.

All three are RECYCLED because all thirty numbered methods have already been genuinely used on P0282, but this triple differs from the predecessor's `#5/#21/#4`.

No theorem claim is made in this note. Production checking and archival claims follow only if the exact algebra survives falsification.