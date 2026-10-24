# Early substantive checkpoint — banked-square half-Riesz splice

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `account02/B11`  
Run: `20260923T042112Z-account02-B11-QFORM-2f47d35a`

First unpaid implication attacked: the remaining opposite-sign/two-sheet branch when an indefinite two-coordinate core is quantitatively good but the third spectral direction is spread over many original coordinates, so every one-coordinate 3x3 determinant is small. The goal here is to aggregate the third direction **before** paying a local determinant.

## Calculation

Let `U=(X_1,X_2)` be two independent cap-one original coordinates. Let `B` be any invertible real symmetric `2x2` matrix and

`P=U^T B U+ell^T U+c`.

The completed rank-two affine half-Riesz theorem recorded in account03/B11 r24, sourced from `math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, gives

`sup_s E |P-s|^(-1/2) <= 16 sqrt(30) |det B|^(-1/4)`.

Now let `W` be independent of `U`, with density cap `||p_W||inf<=L`, and let `d!=0`. Completing the linear term in `W`, the conditional density of `d(W-w0)^2` obeys

`k_d(y) <= L |d|^(-1/2) |y|^(-1/2) 1_{sign(d)y>0}`.

Therefore for

`Q=P+d(W-w0)^2`

(and also after adding any independent noise),

`p_Q(t) <= L |d|^(-1/2) E |P-t'|^(-1/2)`

for the appropriate translated target `t'`, hence

`||p_Q||inf <= 16 sqrt(30) L |det B|^(-1/4)|d|^(-1/2)`.          (E.1)

This is dimension-free and does not require `p_P` to be bounded. In the indefinite case the rank-two density may retain its genuine logarithmic singularity; the third square consumes exactly its half-order potential.

If `W=sum_{j=3}^{m+2} b_j X_j` is a normalized linear form on a disjoint bank (`sum b_j^2=1`), the standard Ball--Rogozin one-dimensional product-projection bound gives `L<=sqrt(2)`, so

`||p_Q||inf <=16 sqrt(60)|det B|^(-1/4)|d|^(-1/2)`.              (E.2)

The required Claude source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `COUNTEREXAMPLE_SEARCH.md`, is already applicable to the same exact-rank-three subclass on the majority one-sheet side: when the three nonzero eigenvalue magnitudes are at least one, its ruled Theorem C gives `p_Q(t)<=pi sqrt(2)` on the one-sheet side. Thus (E.1)--(E.2) are needed only for the opposite two-sheet side in the sign-specific splice, although they actually bound all target values.

Next: record the exact near-null/diffuse-third family showing why selecting one third physical coordinate before applying the partner scalar compiler loses a power of the bank size, while (E.2) remains uniform.
