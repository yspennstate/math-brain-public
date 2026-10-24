# MOC4 handoff — account01/B09 nonsingular stationary strict-pair lift no-go

Run `b09-20260922T054641Z-moc4-r11`. Outcome: **CANDIDATE_REFUTED** for `MOC4-STATIONARY-STRICT-PAIR-PROJECTED-LIFT-v1`; parent MOC4 remains **OPEN**. Execution: `WITHOUT_VERIFIED_BRAIN`.

Canonical scientific artifact: `yspennstate/math-open-problems/proofnet24/collective-MOC4/account01/B09/b09-20260922T054641Z-moc4-r11/REPORT.md`; report blob `b12c5f150c244bcb5c6111233a8dcac845ee07b3`; verifier blob `cc4df5d49b2a3864a1a0ddab86443197e7d0aa3b`; captured PASS blob `bfb2838cbe9978f13b71a6bf2e6077c93a27a888`.

## Inputs actually consumed

- Latest lead account03/B07 `MOC4-MIXED-CONFORMAL-HESSIAN-GATE-v1`, shared handoff `f81667d2ddb67bfa45c96cae39320b078c3e4c4c`, and authoritative proof tree `e8eaccf8e3393ae7a5b75f12310d54ef92c15775`.
- Assigned OTHER-account partner account02/B07 run `20260922T053424Z-b07-45eeecdd`: `MOC4-PAIR-CURVATURE-SANDWICH-v1` and `MOC4-CONJUGACY-CASIMIR-BALANCE-v1`, report commit `44dc01b869c00bf7446d254586d97b6754ee6961`.
- Existing B09 dense rational coefficient-lift witness from run `20260922T035002Z-b09-moc4-r11`.

## New exact result

For the same dense rational orthogonal unitary `U` whose true level-one plus nine anchored level-two marginals violate the necessary common-permutation facet by exactly

`-10349074315776/1167289931640625`, fix `b=(-4,-2,3,-1)` and define

`a=(x0+7i/4, x1-11i/10, x2+i y2, x3+i y3)`.

There is a **unique exact algebraic spectrum** in the infinity box of radius `1e-8` around

`(-1.306978760847276,-2.311269351538912,-0.169908501435229,0.635994359385863,-1.418141008695427,0.390813072733030)`

solving all six nontrivial real-skew first-variation equations. A rational Krawczyk/Banach certificate has contraction bound `<7.45614e-7`. The other ten `U(4)` tangent equations vanish identically from complex-symmetry/skew-symmetry, so `U` is a **full first-order stationary point** for `h(V)=Re det(D_a+V D_b V*)`.

The certified spectrum is simple/nonreal, `A+B` is nonsingular, and all twelve row/column swap gaps are strictly positive: the smallest row lower bound is `1.8532332438`; the smallest column lower bound is `0.2214895014`. By the retained pair-Rayleigh/Bloch theorem this makes `U` strict top-Rayleigh on every one of the twelve genuine pair orbits. The verifier also checks the assigned partner's Casimir balance `sum row gaps = sum column gaps` as an exact polynomial identity.

Nevertheless the projected positive common-permutation lift still fails by the exact facet above. This refutes the proposed strengthening “full first-order stationarity + twelve strict pair tops restores the projected common lift.”

Crucially, this is **not** an MOC4 counterexample: the determinant lies rigorously inside the triangle of target vertices for permutations `(1,0,2,3)`, `(1,2,3,0)`, `(2,3,1,0)`, with barycentric weights bounded below by `0.3061186`.

## Direct mixed-Hessian application

For the genuine unitary tangent `K=K_01-K_23`, exact determinant multilinearity gives

`105.1141873378 < d^2/dt^2 h(exp(tK)U)|_{t=0} < 105.1141957551`.

So this highly constrained coefficient-lift adversary is a **saddle**: every individual pair orbit is strict top, but an off-diagonal mixed pair direction has positive curvature. This is a concrete source-valid demonstration that the lead's new mixed-Hessian layer is essential and that pairwise Rayleigh optimality cannot replace it.

## Updated obligation

A coefficient-lift adversary that actually threatens the surviving MOC4 proof tree must now pass the **full** mixed left/right Hessian gates, global roofs, exact `P/R/D` or Spin(6) same-unitary identities, and carry a positive support gap—or directly violate the target hull. The current first target-level gap remains `MOC4-FLAT-PAIR-MIXED-RIGIDITY-v1` plus the nonsaturated full-Hessian residual.
