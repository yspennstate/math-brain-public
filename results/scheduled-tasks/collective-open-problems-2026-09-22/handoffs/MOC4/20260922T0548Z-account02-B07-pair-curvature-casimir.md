# MOC4 handoff — account02/B07 pair-curvature / Casimir balance

Run `20260922T053424Z-b07-45eeecdd`; outcome `ESSENTIAL_STEP_APPLIED`; parent MOC4 remains **OPEN**; execution `WITHOUT_VERIFIED_BRAIN`.

Canonical report: `proofnet24/collective-MOC4/account02/B07/20260922T053424Z-b07-45eeecdd/REPORT.md`, creation commit `44dc01b869c00bf7446d254586d97b6754ee6961`. Exact finite verifier commit `3a684a880128d84bea943175c490fa84fdc0784d`; exact Cayley reconstruction helper/verifier commits `acb543f342065071db252ae8b1d6cdaa8f0a343d`, `799017acbfe2692d989e92851cca5f281651f8e3`; captured output commit `88e3fffed08f28ba636d869799c125e03c2f133f`.

Consumed latest complete lead account03/B07 `MOC4-TRANSPOSE-SUBGROUP-CUBATURE-v1` (report blob `c286ea3e5ec5a72902fbff82e94db343f2bbc543`) and named partner account03/B08 `MOC4-PAIR-BLOCH-ENVELOPE-v1` (report blob `f39236fa1e63c1af4ebeb89a1f243a49a9aa44a6`). Also used account04/B08 `MOC4-PAIR-SYMMETRIZED-COMMON-LIFT-v1` (report blob `ccc5358d81a9432f3764a9a89be9a01c6bb54e26`).

## New exact steps

`MOC4-PAIR-CURVATURE-SANDWICH-v1`: normalize `|eta|=1`, put `R=max|a_i|+max|b_j|`. For any row pair `(r,s)` and column pair `(p,q)`, a hypothetical global support violation `h(U)=M+gamma` obeys

`2 gamma <= h(U)-h(tau U) <= 2 R^3 |a_r-a_s|`,

`2 gamma <= h(U)-h(U tau) <= 2 R^3 |b_p-b_q|`.

The upper bound is the singular-safe identity

`det(X0+(delta/2)H)-det(X0-(delta/2)H)=delta tr(adj(X0)H)`

with `rank(H)=2`, `||H||_*=2`, `||adj X0||<=R^3`. Combining with the named partner's pair-Bloch theorem gives, in each of the two genuine `SU(2)` axes for that pair,

`4 gamma <= -h''(0) <= 4 R^3 |spectral gap|`.

**Immediate closure:** if either spectrum has a repeated eigenvalue, the corresponding swap leaves the determinant unchanged, while the pair-symmetrized common lift places that unchanged value in the target hull. Thus *all repeated-spectrum MOC4 cases are proved exactly*, including singular determinant values; no repeated-spectrum limiting branch remains.

`MOC4-CONJUGACY-CASIMIR-BALANCE-v1`: for every `S4` conjugacy class `C`,

`sum_{g in C} D(P_g U)=sum_{g in C}D(U P_g)`.

Proof: in the Cauchy-Binet expansion, `W_1,W_3` are bistochastic and commute with every natural-module class sum; `W_2` is bistochastic and commutes with complement by Jacobi, while every six-two-subset class sum lies in `span{I,J,C}`. Consequently the six-transposition gap sums satisfy `G_out=G_in=G`, and the two pair-Hessian trace budgets agree exactly:

`sum_row_pair_axes h'' = -4G = sum_column_pair_axes h''`.

At a positive-gap maximizer `G>=12 gamma`, so both traces are at most `-48 gamma`. The same central representation yields the exact identity `h(e)=3 A_trans h-2 A_3cycle h`, hence `G=4(h-A_3cycle h)`.

Exact regression on the named partner's dense rational Cayley datum reproduces its support gap and verifies all five class balances; there

`G=1575414455627672838774521982/431850208768934029`.

## Sharpened remaining branch

It is now enough to exclude a **simple-spectrum** positive-gap global maximizer with both spectra quantitatively `gamma/R^3` separated, all pair curvatures strictly negative as above, equal row/column Hessian trace budgets, and the lead subgroup/V4 plus current same-unitary `P-R-D`/Spin(6) stationarity constraints. Singular sums themselves create no inverse debt in these formulas. A disproof still requires actual complex spectra and a true unitary in one common support direction.
