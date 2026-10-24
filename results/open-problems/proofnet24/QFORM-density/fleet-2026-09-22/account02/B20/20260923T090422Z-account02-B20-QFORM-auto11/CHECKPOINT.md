SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B20, 2026-09-23T09:04:22Z.
attacking: the account03/B20 r29 HC finite-core obstruction by sequential original-coordinate Fresnel peeling.

# Early substantive checkpoint

Fresh designated partner: account03/B20 r29, canonical math-open-problems commit `b1f862a5685a726b0eb2e3c348b22ee9eaf7a782`. In its exact-rank-three rank-two-cross HC chamber, the normalized-heavy original-coordinate core `K0` has `|K0|<=31`. With frame rows `r_i` of `R`, `R^T R=I_3`, coefficient matrix `M=M^T` having `sigma_min(M)>=1`, and

`S0=I-sum_{j in K0} r_j r_j^T`, `delta0=lambda_min(S0)`,

the partner pays the `delta0>=1/64` branch only when all residual whitened leverages are <=1/32, leaving a <=126 dangerous core otherwise.

New mechanism: use the proved Fresnel--Brascamp--Lieb Theorem F from `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`. For any conditioned original-coordinate set K with residual Gram `S=sum_{i notin K} r_i r_i^T>0`, put `U=R_{K^c}S^{-1/2}` and `B=S^{1/2}MS^{1/2}`. Then `U^TU=I_3`, residual row leverage is `r_i^T S^{-1}r_i`, and if every such leverage is <=1/2,

`||p_Q||_infinity <= 12 |det B|^(-1/3) = 12 (det S |det M|)^(-1/3)`.

Thus if `lambda_min(S)>=1/64`, this branch is paid by `< = 768`.

If instead some residual row has whitened leverage `ell>1/2`, condition that ORIGINAL coordinate. The residual Gram becomes `S'=S-r r^T` and the matrix determinant lemma gives exactly

`det S' = det S (1-ell) < (1/2) det S`.

As long as `lambda_min(S)>=1/64`, one has `det S >= 64^(-3)=2^(-18)`. Therefore 18 successive >1/2 leverage removals are impossible while staying above the `1/64` spectral floor. Consequently the partner's entire HC finite-core branch reduces exhaustively to:

1. a paid conditioned-Fresnel state with `||p_Q||_infinity <=768`; or
2. an original-coordinate set K with `|K|<=31+18=49` and `lambda_min(I-sum_{j in K}r_jr_j^T)<1/64`, hence for some unit v,
   `sum_{j in K}<r_j,v>^2>63/64`.

This eliminates the partner's separate <=126 dangerous-core state; the first unpaid HC implication becomes payment of a <=49-coordinate near-coloop core. No post-rotation independence, pointwise quadratic-phase decay, fiber supremum, moment bound, or small-random-perturbation claim is used.
