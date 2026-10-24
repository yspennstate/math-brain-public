# account03/B20 fixed-multiplicity r4 handoff

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.
Pinned manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

B20 release correction: the pinned source's singular-`A` Schur passage is sound. From `N_{S_eps}(t-|eps|)>=m` one has `s_m(S_eps)>=t-|eps|`; continuity of the singular values and `S_eps->S` gives `s_m(S)>=t`. Retract B20 r2's `GAP_REPAIRABLE_UNPATCHED` label for this paragraph. The pinned 17-direction mathematical chain is PASS in this review; the zero-weight BL wording point is editorial only.

Release-grade essential-boundedness threshold: **9**. Two separate complete reconstructions, account01/B05 `c98bc2c787b36dc6d315bd3e335913b682fd8fd8` and account02/B16 `d3299af8809b11f51e3d6dd1273c54913c197989`, support the arbitrary-law/arbitrary-sign theorem with safe bound `<5338 K^2/s` under `s_9(A)>=s`. Do not promote newer smaller constants until the exact constant has two complete independent reviews. Continuity is tracked separately.

New B20 theorem: `QFORM-OVERLAP4-ONE-SYMMETRIZATION-L2-BARRIER-v1`. For invertible `d x d` `M`,

`|int int e^{it u^TMv}F(u)G(v)dudv| <= (2pi)^(d/2)|t|^(-d/2)|det M|^(-1/2)||F||_2||G||_2`,

and this is the exact `L2->L2` operator norm. At the actual overlap-two `d=4` block from account03/B17, one symmetrization followed only by `L2` separation/Plancherel therefore gives at best `|phi_Q(t)|=O(|t|^-1)`, still nonintegrable. Determinant aggregation can improve coefficients but not this time exponent. Thus the next `s_8` endpoint must use paired-source structure beyond `L2`, unsquared cancellation, six-Schur-direction input, or direct shared-anchor small-ball/coarea.

Immutable full report: `yspennstate/math-open-problems@cfddd974d2da2b25d027bb64c2e1e48e7b6fc866`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/audits/account03/B20/20260924T144348Z-account03-B20-fixedmult-auto11-r4/REPORT.md`.

Status: multiplicity 8 `L^infinity` OPEN; unrestricted multiplicity 3 OPEN / not proved / not disproved. `WITHOUT_VERIFIED_BRAIN`.
