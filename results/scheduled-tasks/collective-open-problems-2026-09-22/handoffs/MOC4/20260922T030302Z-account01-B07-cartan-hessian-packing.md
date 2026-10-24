# MOC4 handoff — account01/B07 Cartan Hessian packing

Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Run: `20260922T030302Z-b07-moc4-r11`  
Outcome: `ESSENTIAL_STEP_APPLIED`; parent MOC4 remains **OPEN**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

Canonical scientific report:
- private repo: `yspennstate/math-open-problems`
- commit: `2589e5051a26c2f214174200cd9dab1c10c1e813`
- path: `proofnet24/collective-MOC4/account01/B07/20260922T030302Z-b07-moc4-r11/REPORT.md`
- report blob: `b3dbfc1ff3b7bf397e51c6c7ccb08ab4595cac5b`

## Named OTHER-account inputs actually applied

- Assigned partner account02/B08: `MOC4-BOUNDARY-SUPPORT-FACE-REDUCTION-v3` (`B08-20260922T023618Z-7e3c2a`). Repeated-spectrum and proper common-block faces are handled exactly; the residual all-pairs core is simple-spectrum/invertible/irreducible apart from the partner's explicit collinear supported-face boundary.
- account02/B09: `MOC4-CARTAN-POLARIZATION-v1`. For every entry, at a global support maximizer `h(t)=h(c)-Gamma_ij(t-c)^2`, with exact zero/common-block endpoint drops.
- account02/B07: `MOC4-PAIR-HESSIAN-TRACE-v1`, giving `Tr H_pair=-8{2k+3(x-cbar)}`.

## New exact theorem — `MOC4-CARTAN-HESSIAN-PACKING-v1`

Let a global true-unitary support maximizer have target gap `gamma>0`. If all sixteen exact one-entry zero endpoints are target-safe, then each radial Cartan direction has curvature

`-h''(0) >= 6 gamma`.

The proof first uses both endpoint drops:

`Gamma c^2 >= gamma`, `Gamma(1-c)^2 >= gamma`.

Since the angular Cartan curvature is `2 Gamma(1-c^2)` and

`min_{0<c<1} max{(1-c^2)/c^2,(1-c^2)/(1-c)^2}=3`,

each entry pays at least `6 gamma`.

For a fixed column `j`, phase-adjust the orthonormal vectors `U*e_i` and write

`q_i=c_ij e_j+s_ij y_ij`.

Completeness gives the exact tight-frame identity

`sum_i s_ij^2 y_ij y_ij^* = I_(e_j^perp)`.

For the unit Cartan generators `K_ij=y_ij e_j^*-e_j y_ij^*`, this implies the real frame operator bound `S_j<=P_(V_j)`. Summing over four columns gives `S<=2P_off`, while `sum_ij s_ij^2=12`. Since `A=-H` is positive semidefinite at a global maximizer,

`72 gamma <= tr(A S) <= 2 tr(A P_off) = -2 Tr H_pair`.

Therefore

`-Tr H_pair >= 36 gamma`

and, using the exact pair-Hessian trace identity,

`2k+3(x-cbar) >= (9/2) gamma`.

So every hypothetical MOC4 support violation obeys the exact dichotomy:

1. a genuine zero-entry endpoint is already violating; or
2. the strict interior branch has the quantitative Hessian payment above, strengthening the previous qualitative `>=0` condition.

## First remaining implication

`MOC4-STRICT-INTERIOR-GAP-PAYMENT-v1`: on the no-zero-face-escape branch, combine exact stationarity, strict odd-overlap collars, structured spectral `(K,X)` coefficients, and

`k>=0`, `2k+3(x-cbar)>=(9/2)gamma`

to derive a structured upper bound on the same off-diagonal Hessian trace that contradicts the lower bound `36 gamma`.

The separate zero-entry support branch remains unpaid. No arbitrary bistochastic surrogate, benchmark material, credentials, machine-local data, email/Drive data, public release, paid model/API/Codex or remote workflow was used.
