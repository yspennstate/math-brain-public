# r20 correction-refresh addendum

Fresh prepublication main exposed the source-valid counterexample `QFORM-ARBITRARY-SELF-CROSS-FROBENIUS-SCALE-FALSE-v1`, proved in

`yspennstate/math-open-problems@3a3525d72f9f5b6f5e1e107a6e05793b57352e31`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260922T211507Z-account02-B03-QFORM-r12/REPORT.md`.

That correction refutes the **critical half-Riesz** extension

`H_(1/2)(R) <= C ||C||_F^(-1/2)`

under arbitrary active self curvature. It does **not** refute the r20 result. The r20 theorem deliberately works at the strictly subcritical exponent `alpha=1/8<1/4`, where the already-proved regularized-determinant/Riesz integral is convergent:

`H_(1/8)(R) <= C_R ||C||_F^(-1/8)`.

The counterexample itself is a useful stress test. There

`R_eta=[(X+Y)^2+eta(X-Y)^2]/(2eta)`,

with cross Frobenius scale `F_eta=(1-eta)/(2eta)`. Then

`R_eta^(-1/8)=(2eta)^(1/8)(u^2+eta v^2)^(-1/8)`

in the diamond variables `u=X+Y`, `v=X-Y`. Multiplying by `F_eta^(1/8)` leaves

`(1-eta)^(1/8) E (u^2+eta v^2)^(-1/8)`,

which stays bounded as `eta->0` because `(u^2+eta v^2)^(-1/8)<=|u|^(-1/4)` and the diamond law has finite `E|u|^(-1/4)`. Thus the fresh counterexample separates the invalid critical endpoint from the valid subcritical mechanism used in r20.

Accordingly the new conclusions remain:

1. endpoint indefinite pair plus any nonzero Schur cross block `C`:

`||p_Q||_infinity <11.021 D^(-2/5) kappa^(-1/10)||C||_F^(-1/10)`;

2. the complementary logarithmic form:

`||p_Q||_infinity <=D^(-1/2)[22.648+log_+(4D/(kappa||C||_F))]`;

3. exact rank-one residual cross curvature is analytically sufficient once quantitative endpoint-pair parameters are exposed.

The full target remains OPEN, and continuity is not proved by this branch.
