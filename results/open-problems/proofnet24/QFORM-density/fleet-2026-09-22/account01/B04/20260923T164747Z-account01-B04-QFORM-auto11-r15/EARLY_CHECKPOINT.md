SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-23T16:47:47Z.
attacking: derive the exact q-dependent Hausdorff--Young marginal factor in the third-volume Fourier compiler, optimize it on a regular-simplex rank-four cross block, and compare with the projection-tail gate and account02/B04 support-defect exit.

# Early substantive checkpoint

Starting from `math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba:proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`, keep the row/column Hausdorff--Young factors in equation (14) instead of replacing them by `e^3`.

For a probability weight `w` on positive physical 3x3 minors, row/column marginals `alpha_i,beta_j`, and determinant/entropy currency

`G(w)=exp(sum w_ST log(det(M[S,T])^2/w_ST))`,

define, for `1<=q<3/2` with `alpha_i<=q/2`,

`R_q(w)=prod_i (1-alpha_i/q)^(-(q-alpha_i)/2) * prod_j (1-beta_j)^(-(1-beta_j)/2)`.

The unchanged BL+sharp-HY calculation gives

`E F_t^q <= q^(-3/2) (pi/|t|)^3 G(w)^(-1/2) R_q(w)`.

Hence with `b=3/(2q)`,

`|phi_Q(t)| <= min(1,K|t|^-b)`,
`K=[q^(-3/2) pi^3 G(w)^(-1/2) R_q(w)]^(1/(2q))`,

and exact inversion should yield

`||p_Q||inf <= 3 R_q(w)^(1/3) G(w)^(-1/6) / ((3-2q)sqrt(q))`.

This strictly sharpens the existing `3e/((3-2q)sqrt(q))*G^(-1/6)` whenever the actual marginal product is below `e^3`.

Stress matrix under construction: `M=2U`, where `U` is the first four columns of the Householder orthogonal matrix sending `e_5` to `(1,...,1)/sqrt(5)`. Then `U^T U=I_4`, every row leverage is `4/5`, every entry of `U` is nonzero, and the canonical third-volume law has row marginals `3/5`, column marginals `3/4`, and `G=E3(M)=256`. Thus the smallest admissible canonical exponent is `q=6/5`; the exact marginal factor is `R_q=2^(5/2)`, leading to the candidate explicit bound `5 sqrt(15)/6 = 3.2274861218...` for the full ambient form.

Remaining work this run: write the full derivation; prove the matrix identities without numerical assumptions; show the newest projection-tail sufficient gate fails for every admissible projection on this block; apply the completed account02/B04 support-defect theorem to the same ambient matrix after conditioning one original row; refresh corrections and publish a source-pinned handoff. Full QFORM remains open.