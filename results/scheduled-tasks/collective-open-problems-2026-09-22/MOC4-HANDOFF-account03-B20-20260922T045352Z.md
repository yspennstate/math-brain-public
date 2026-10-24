# MOC4 source-bound handoff — account03/B20

Run: `20260922T045352Z-b20-moc4-r11`  
Outcome: **ESSENTIAL_STEP_APPLIED**. Parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

Canonical report: `yspennstate/math-open-problems/proofnet24/collective-MOC4/account03/B20/20260922T045352Z-b20-moc4-r11/REPORT.md`, report blob `7cfcd7357212df088a490a612f8ac6aab193768a`. Exact verifier blob `f406a2a3c688be8f5a25b7a13707bb992bce528c`; captured output blob `fe16bf9847b65f3c47e58a047eed10d69172c9ea`.

Consumed assigned other-account partner: account04/B09 run `20260922T041453Z-b09-moc4-r34`, theorem `MOC4-STANDARD-CHANNEL-CEILING-v1` (report blob `faaf77b4fcebb8fed6a6c9763251acc1042105ac`). Also uses campaign-lead `MOC4-V4-PAIR-GAP-CEILING-v1` and account03/B09 exact `D=(1/4)E^TPE`, `R>=|D|` compatibility.

## New theorem: `MOC4-STANDARD-PR-LOCKING-v1`

Fix spectra/support direction. Let `kappa_sigma=H_sigma-B_{rho_sigma}`, `K=max kappa`, `Delta=M-Q`, and suppose `sigma_*` is the unique `kappa` maximizer. Define

- `delta = K - max_{sigma != sigma_*} kappa_sigma > 0`,
- `r = K-Delta`,
- `d_* = M-H_{sigma_*}`,
- `L_P=max_sigma <C,P_sigma>-<C,P_sigma_*>`,
- `L_R=max_rho <J,R_rho>-<J,R_rho_*>`,
- `L=L_P+2L_R`.

Then every genuine true-unitary support violation `h(U)=M+gamma`, `gamma>0`, satisfies

`gamma <= Gamma_* := max(0, r-delta/2, (L*r-delta*d_*)/(L+delta))`.

If `r>0`, `Gamma_*<r`; if `r=0`, the partner theorem already closes the direction.

Proof bridge: partner standard convexity plus the lead lower bound gives, in any Birkhoff decomposition of the same `P=|U|^2`, `1-lambda_* <= (r-gamma)/delta`. On the branch `gamma>r-delta/2`, `lambda_*>1/2`. Exact common-unitary compatibility then forces the same pair quotient to decompose as

`R=(2 lambda_*-1)R_{rho_*}+2(1-lambda_*)R'`

with `R'` doubly stochastic. The exact support decomposition gives `gamma+d_* <= (1-lambda_*)L`, yielding the displayed ceiling. No independent bistochastic `(P,R)` lift is used.

Exact application: for `a=(0,-5,3,2)`, `b=(-1,2,4,3)`, `eta=1`, the partner standard ceiling is `gamma<=8`, whereas the new theorem gives

`gamma <= 1556/247 ~= 6.2995951417`.

The exact lead pair ceiling on the same datum is `197/4`, so the new bound is the active reduction.

First remaining obligation: `MOC4-STANDARD-FACE-LOCK-v2` — extend the same-unitary locking payment to non-unique standard-maximizer faces and eliminate the residual positive `Gamma_*` in the unique-max branch using Cartan stationarity and/or odd-Weyl square-root constraints. A genuine normal-matrix counterexample is an alternative; arbitrary bistochastic/coefficient-hull witnesses do not count.
