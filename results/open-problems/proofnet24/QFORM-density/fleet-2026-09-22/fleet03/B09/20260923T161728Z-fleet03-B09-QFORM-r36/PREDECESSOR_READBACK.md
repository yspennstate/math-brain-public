# Predecessor readback note

After the r36 core proof was written, the worker-owned `LATEST.json` was refreshed and showed a newer same-slot predecessor than r35:

`20260923T155027Z-fleet03-B09-QFORM-auto11`, canonical mathematics `yspennstate/math-open-problems@039a804cf1971a2f5b3922a761e61d2bc44ec3d8`.

That run proved `QFORM-ONEANCHOR-TWOVOLUME-HALFRIESZ-v1` and a nonzero-scalar-pivot interpolation theorem. Its explicit remaining debt was the near-zero / degenerate-residual-anchor case, where one must spend the pair-row wedge `Delta` and anchored third volume `V` before reciprocal scalar/pair payment.

The r36 theorem is complementary and directly addresses that debt in the opposite-bank diffuse subbranch: for the same r35/r-auto11 localized cut `M=A[{a,b} union S,T]`, the anchored third volume satisfies `Z_3(M)>=V>=27G_*/400`; whenever `max diag P_range(M^T)<=1/2`, regularized-determinant smoothing yields

`||p_Q||_infinity < 8.864 G_*^(-1/6)`

with no scalar pivot, no residual anchor and no pair-core denominator at all. Hence r36 closes the near-zero/degenerate-anchor survivor whenever the column-side range is diffuse. The remaining same-slot debt is the high-column-leverage case.
