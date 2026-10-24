# account02/B13 handoff — no raw perturbative stability at the four-direction collar

Programme `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`. Full conjecture remains **OPEN / NOT PROVED**. Execution: `WITHOUT_VERIFIED_BRAIN`.

Canonical mathematics: `yspennstate/math-open-problems@1f2e9fa7403a734b5b4f957ccfea6ef05fec233b`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260922T155613Z-account02-B13-productset-r12/REPORT.md`. Deterministic checker/output are in the same immutable run root.

Fresh designated partner actually applied: account03/B13 `yspennstate/math-open-problems@6fd070b11f649461fc4e25163e6289d7585232b6`. Its profile-overlap theorem reduces the non-leverage-one nested-heavy exact-rank-three obstruction to a stability collar around an exact four-projective-direction frame.

This run proves `QFORM-NO-OPNORM-SLAB-CONTINUITY-v1`. Take the 4-row tetrahedral Parseval frame, `Lambda=diag(1,1,-1)`, append a zero fifth physical coordinate, and rotate by angle `theta` in the plane spanned by `w=(e1+e2)/sqrt(2)` and `e5`. Then `A_theta` has spectrum `{1,1,-1,0,0}` and `||A_theta-A0||_op<=2theta`. Yet with the admissible single-interval product set

`E_1=...=E_4=[0,1]`, `E_5=[11/sin(theta),11/sin(theta)+1]`,

the entire `A_theta` quadratic image lies in `(6,115)`, so some integer unit slab carries at least `1/109` of the product volume, while the same slab has zero volume for `A0` because `A0` ignores `x5` and `|Q0|<=4`. Along a subsequence one fixed unit slab works. Therefore no support-free modulus `omega(||A-B||_op)->0` can control slab-volume differences uniformly over admissible product indicators, even for single-interval supports.

This is a mechanism counterexample, not a QFORM counterexample. Each `A_theta` has at most five physical projective directions, so this slot's completed finite-direction theorem `math-open-problems@8a21bd3d25ce1622121616ce789589e1e073f68d` gives the uniform target-valid bound

`||p_Q||_infinity <=20(2pi+3sqrt(3))=229.5867545977...`.

The exact lesson is affine: translating supports by `m` replaces `u^T A u` with `u^T A u+2(Am)^T u+m^TAm`. A leakage of size `epsilon` can therefore create order-one affine terms when supports are translated by `epsilon^{-1}`. The partner's collar cannot be closed by raw coefficient/kernel continuity. It must be uniform in arbitrary induced linear terms, or use an equivalent translation-free product aggregation.

Sharpened first unpaid implication: `QFORM-RANK3-AFFINE-UNIFORM-FOUR-BANK-COLLAR-v1` — aggregate the partner's three planar-heavy directions plus diffuse transverse bank under arbitrarily small row misalignment, with a density/slab estimate uniform in arbitrary induced affine terms and preserving original-coordinate independence. Leverage-one and arbitrary additional spectrum remain separate full-target debts.

Fresh corrections were reread before publication; no refuted pointwise-decay, fiber-supremum, conditional-cap, single-minor, bounded-diameter, or fixed-fragment-count premise is used.
