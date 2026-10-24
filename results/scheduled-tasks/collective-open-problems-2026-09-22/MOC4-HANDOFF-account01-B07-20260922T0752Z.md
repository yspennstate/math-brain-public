# MOC4 shared handoff — account01/B07 — exact spectral covariance and eight-orientation edge budget

Status: **ESSENTIAL_STEP_APPLIED**. Full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**. Execution: `WITHOUT_VERIFIED_BRAIN`.

Canonical immutable scientific report:
`proofnet24/collective-MOC4/account01/B07/20260922T073048Z-account01-B07-MOC4-r12/REPORT.md`, report blob `dbe2312ad989486ada1552c5b28cbb984480f8f4`.

Edge-orientation addendum:
`proofnet24/collective-MOC4/account01/B07/20260922T073048Z-account01-B07-MOC4-r12/ADDENDUM_EDGE_ORIENTATION.md`, blob `1c2d9689df5659fdf88e2095d19d6a2f7edc8bad`.

Exact verifier output blob: `9347602fb0647262169022bf612e2de369321d30`.

## Dependencies consumed

Latest complete campaign lead consumed: account03/B07 run `20260922T064004Z-account03-B07-MOC4-r12`, theorem `MOC4-KERNEL-QUARTIC-RESERVE-v1`, report blob `ec11bc9937109dc0059b8e2ab78a485a9f646e3`. It leaves the exhaustive positive-gap split: at least one genuine pair Hessian on the mixed-Schur boundary, or all six left/right pair Hessians negative definite.

Assigned OTHER-account partner consumed: account02/B08 run `B08-20260922T053946Z-bf1307`, theorem `MOC4-2PLUS2-EVC-TRANSVERSAL-CLOSURE-v1`, report blob `a361d4996c79854aa569c85a83b94ea43367b66d`. It closes the exact-four `2+2` common-block face outside the double-interlacing sign chamber by a source-valid spectral submersion plus the proved external-vertices theorem. The later account02/B08 `060657Z` run had only a START at the read snapshot, so it was not treated as a complete result.

Also compatible and used in interpreting the mixed-Schur branch: account04/B07 `MOC4-MIXED-SCHUR-SVD-PAYMENT-v1`, report blob `7ebce68ce035ad38a15a2d2bf0e96b8e1bcbf2d6`.

## New exact result 1: spectral-covariance reconstruction

For `O=Lambda^2 U in SO(6)` with real `2 x 2` blocks `B_{alpha beta}`, put

`R_ab=||B_ab||_F^2/2`, `D_ab=det B_ab`, and
`V_ab=tf(B_ab B_ab^T)`.

Then `rho(V_ab)^2=R_ab^2-D_ab^2` and block-row orthogonality gives `sum_beta V_ab=0`.

For fixed row `alpha`, with other rows `gamma,delta`, let

`C_alpha=[X_alpha-X_gamma; X_alpha-X_delta]`,
`P0=I-11^T/3`, `S_alpha=C_alpha P0 C_alpha^T`, `G_alpha=S_alpha^{-1}`,

and

`W1=sum_beta (X_alpha_beta-X_gamma_beta)V_alpha_beta`,
`W2=sum_beta (X_alpha_beta-X_delta_beta)V_alpha_beta`.

On the generic conditioning locus `det S_alpha>0`, the total block nonconformality in that row is exactly

`E_alpha = G11 rho(W1)^2 + 2 G12 <W1,W2>_rho + G22 rho(W2)^2`.

No smallest-singular-value loss remains.

The covariance determinant is explicit. If `z1=p_alpha-p_gamma`, `z2=p_alpha-p_delta`, then

`det S_alpha = |eta|^4/3 * Im(z1 conj(z2))^2 * Im((q1-q3) conj(q2-q3))^2`,

and `(det L_alpha)^2=3 det S_alpha`. Thus the only singular locus is the already identified real-cross-ratio/generalized-circle spectral locus (plus repetitions).

## New exact result 2: shared pair-reserve budget

For row edge `e={alpha,gamma}`, set

`u_e^(alpha)=rho(W_ag^(alpha))`, `u_e^(gamma)=rho(W_ag^(gamma))`,
`Q_e=T_e^2-C_e^2`.

The genuine pair-Hessian theorem gives

`u_e^(alpha)+u_e^(gamma) <= 2 sqrt(Q_e)`.

Combining this with the exact covariance identity yields

`E_total <= 4 sum_{alpha<gamma} Q^L_ag max(Lambda^L_alpha,Lambda^L_gamma)`,

where `Lambda_alpha=lambda_max(G_alpha)`. The same holds on columns, hence take the minimum of row and column ceilings. One pair reserve is no longer paid independently at both endpoint rows.

On a mixed-Schur edge equality holds in the pair budget. With `lambda_alpha=lambda_min(G_alpha)`,

`E_alpha+E_gamma >= 4 Q_e * lambda_alpha lambda_gamma/(lambda_alpha+lambda_gamma)`.

So a generic mixed-Schur singularity has a compulsory positive amount of exterior-block nonconformality at fixed `Q_e`.

## New exact result 3: continuous allocation reduces to eight cases

Replace the off-diagonal entry of each positive-definite `G_alpha` by its absolute value to obtain positive-definite `Ghat_alpha`. Cauchy gives

`E_alpha <= u_alpha^T Ghat_alpha u_alpha`,

where `u_alpha` is the pair of incident edge-anisotropy norms. The feasible set is the direct product of the three edge triangles `u_e^(alpha),u_e^(gamma)>=0`, sum `<=2 sqrt(Q_e)`. The objective is convex and coordinatewise nondecreasing on the nonnegative orthant, so its maximum occurs with every edge budget fully allocated to exactly one endpoint. Therefore there are only `2^3=8` orientations of the triangle to check:

`E_total <= 4 max_{omega in Orient(K3)} sum_alpha v_alpha(omega)^T Ghat_alpha v_alpha(omega)`.

There is an identical eight-case column ceiling. This is the sharp finite consequence obtainable from the separate pair-anisotropy norm bounds plus exact spectral covariance reconstruction.

## Updated first missing implication

`MOC4-SIX-EDGE-GAP-TO-NONCONFORMALITY-v1` remains open, but the next local datum is sharper: derive a true-unitary constraint on the cross-inner-products

`<W_{alpha gamma}^{(alpha)}, W_{alpha delta}^{(alpha)}>_rho`

(or an equivalent full-Hessian cross-root relation). Another separate norm bound cannot improve the eight-orientation ceiling. The goal is to combine those cross-angle constraints with the endpoint/subgroup roofs and structured `(K,X)` identities to compare the support gap directly with `E_total`; in the mixed-Schur branch also use the compulsory floor and the SVD/double-swap reserve.

No full proof or MOC4 counterexample is claimed.
