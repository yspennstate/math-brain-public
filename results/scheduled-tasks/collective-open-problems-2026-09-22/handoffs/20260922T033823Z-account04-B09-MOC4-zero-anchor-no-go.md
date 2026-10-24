# MOC4 handoff — account04/B09 zero-anchor marginal lift refuted

Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Worker/run: account04/B09 `20260922T033823Z-b09-moc4-r33`  
Outcome: `CANDIDATE_REFUTED`; full MOC4 remains OPEN.  
Scientific source: `yspennstate/math-open-problems/proofnet24/collective-MOC4/account04/B09/20260922T033823Z-b09-moc4-r33/REPORT.md`, report blob `1bf0fbe7d01f0fe659df5ecc12bbd9b5d98667b5`.

Consumed source-bound results:
- campaign lead account03/B07 `20260922T013930Z-account03-B07-MOC4-r11`, `MOC4-ZERO-ENTRY-COMMON-LIFT-v1`;
- required OTHER-account partner account01/B07 `20260922T030302Z-b07-moc4-r11`, `MOC4-CARTAN-HESSIAN-PACKING-v1`;
- account03/B20 `20260922T025001Z-B20-moc4-r12`, `MOC4-PAIR-TWIRL-TWO-POINT-v1`;
- account04/B08 `20260922T021352Z-account04-B08-moc4-r43`, `MOC4-ZERO-FACE-GAP-v1`.

New exact result: even the following strictly weaker positive-lift shortcut fails on a genuine zero-entry orthogonal matrix. Require a probability law on `S_4` to match only (i) all singleton marginals `P_rc=|u_rc|^2` and (ii) the nine zero-anchored two-set marginals `Q_ij=|det U[{0,i},{0,j}]|^2=x_i y_j`. Every such law must satisfy

`P13+P21+P32-P12-P23-P31 + y1*x2+2*y1*x3+2*y2*x1+y2*x3+y3*x1+2*y3*x2 >= 0`.

The lead's exact rational zero-entry orthogonal witness makes this left side exactly

`-121344/2640625 < 0`.

The proof is pointwise over the 18 permutations with `sigma(0)!=0`; the verifier records only values `0` and `3` for the pointwise slack. Exact verifier output is at the scientific run path, blob `adbd262e4dde11ee3246234675d92bb19ac58a4e`.

Interpretation: the zero-face rank-one factorization cannot be turned into a classical hidden matching even after discarding all non-anchored middle-compound marginals. This does NOT refute MOC4 or the exact zero-face support inequality. Surviving work must stay support-specific: retain the `X`-dependent zero-face fiber gaps / Cartan support geometry and the pair-twirl/Hessian collar. A genuine violating Cartan zero endpoint remains a target-level branch; otherwise the strict compact interior remains the other branch.

Execution remained `WITHOUT_VERIFIED_BRAIN`; no benchmark material, credentials, email/Drive data, remote workflow, scheduler mutation, or notification enabling was used.
