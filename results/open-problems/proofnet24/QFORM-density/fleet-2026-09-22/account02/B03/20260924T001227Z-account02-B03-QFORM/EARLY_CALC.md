# account02/B03 early calculation — collision determinant to quarter-Riesz

Let `Q=X^T A X+b^T X+c`, with independent scalar input densities at most one, and let `Q'` be an independent whole copy. Fix two genuine original coordinates `I={i,j}` and write `B=A[I,I]`, `Delta=|det B|>0`.

Condition on all coordinates outside `I` in both copies. The conditional difference `Q-Q'` is a quadratic polynomial in the four mutually independent cap-one scalars `(X_i,X_j,X_i',X_j')` with quadratic matrix `diag(B,-B)` and arbitrary affine terms, hence determinant modulus `Delta^2`.

Applying the completed literal four-coordinate determinant receiver (`||p||_infinity<93|det M|^{-1/4}`) conditionally and averaging gives

`||p_{Q-Q'}||_infinity < 93 Delta^{-1/2}`.

Therefore

`P(|Q-Q'|<=eps) < 186 Delta^{-1/2} eps`.

A Gaussian-mollifier argument then yields `Q` itself has an `L^2` density with

`||p_Q||_2^2 <= 93 Delta^{-1/2}`.

For any probability density `p` with `||p||_2=L`, splitting `|x-s|^{-1/4}` at radius `R` gives

`sup_s int |x-s|^{-1/4}p(x)dx <= 2 L R^{1/4}+R^{-1/4}`,

so after optimization

`H_{1/4}(Q) <= 2 sqrt(2L) <= 2 sqrt(2) 93^{1/4} Delta^{-1/8}`.

This is the intended splice currency for the pinned coordinate-hyperbola peel. It uses the independent-copy identity only at the level of the whole scalar difference and does not split any conjugate sum/difference variables.