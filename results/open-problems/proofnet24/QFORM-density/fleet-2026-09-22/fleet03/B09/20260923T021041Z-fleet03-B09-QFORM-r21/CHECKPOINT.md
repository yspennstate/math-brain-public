# fleet03/B09 r21 — substantive checkpoint

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN. This checkpoint attacks the current B09 hub/star survivor with arbitrary within-bank quadratic curvature.

## New calculation: rectangular two-sided null-hub smoothing

Let `x,u_1,...,u_r,v_1,...,v_m` be distinct original coordinates, `r>=2`, all independent with marginal densities at most one. Write `u in R^r`, `v in R^m`. Consider

`q = a x^2 + 2x(beta+r0^T u+s^T v) + u^T C u+2 gamma^T u + 2u^T Bv + G(v)`,

where `C` is symmetric, `G` is an arbitrary quadratic-plus-affine function, and `B` is `r x m` of full row rank. Assume the opposite hub coupling is aligned, `s=B^T kappa`. Make the determinant-one shear `u'=u+kappa x`. Put

`a_L=a-2 r0^T kappa+kappa^T C kappa`,
`r_L=r0-C kappa`, `beta_L=beta-gamma^T kappa`.

In the double-null-curvature chamber `a_L=0`, `r_L!=0`, the form becomes

`q=2x(beta_L+r_L^T u')+F(u')+2u'^T Bv+G(v)`.

The sheared density is exactly

`h(x,u')=f_x(x) prod_i f_i(u'_i-kappa_i x)`.

For fixed `u'` set `m(u')=int h(x,u')dx<=1`, `c(u')=beta_L+r_L^T u'`, and

`K_{u'}(t)=int h(x,u') exp(2it c(u')x)dx`.

Hausdorff-Young gives

`||K_{u'}||_4 <= pi^(1/4)|c(u')|^(-1/4)m(u')^(3/4)`.

Hence, with `H(t)^2=int |K_{u'}(t)|^2du'`, Minkowski gives

`||H||_4^2 <= pi^(1/2) E_m |c(U')|^(-1/2)`.

Under `m`, `U'=U+kappa X`, so

`c(U')=beta_L+r_L^T U+(r_L^T kappa)X`.

Define

`w=[||r_L||_2^2+(r_L^T kappa)^2]^(1/2)`.

Applying the completed affine-fiber/product-projection density theorem (`math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`, fleet02/B06) to this actual scalar projection gives density cap `L<=sqrt(e)/w`; the bathtub estimate then yields

`||H||_4 <= 2^(3/4) pi^(1/4) L^(1/4)`.

Let `Delta_r(B)=prod_{j=1}^r sigma_j(B)`. If `Z` is the orthogonal projection of `v` onto `range(B^T)`, the same peer theorem gives `||p_Z||infinity=N<=e^(r/2)`. Thin-SVD bilinear Plancherel, with no independence asserted among the projected coordinates, gives

`|phi_q(t)| <= pi^(r/2)|t|^(-r/2) Delta_r(B)^(-1/2) N^(1/2) H(t)`.

For `T>0`, Holder `(4/3,4)` gives

`int_(|t|>T)|phi_q(t)|dt <= D_r T^(-(2r-3)/4)`,

`D_r=pi^(r/2) Delta_r(B)^(-1/2)N^(1/2) * 2^(3/4)pi^(1/4)L^(1/4) * [6/(2r-3)]^(3/4)`.

Together with `|phi|<=1` on `|t|<=T`, optimization yields a finite `L^1` characteristic function for every `r>=2`, therefore a continuous density and a genuine `O(|I|)` interval bound. The coefficient has exact scaling

`C_r N^(2/(2r+1)) L^(1/(2r+1)) Delta_r(B)^(-2/(2r+1))`.

After the peer projection caps, this is

`C_r sqrt(e) [ w Delta_r(B)^2 ]^(-1/(2r+1))`,

where

`beta_r=(2r-3)/4`,
`C_r=((beta_r+1)/(pi beta_r))*(beta_r/2)^(1/(beta_r+1))*[pi^(r/2+1/4) 2^(3/4)(6/(2r-3))^(3/4)]^(1/(beta_r+1))`.

Numerically `C_2=4.2073317954`, so the rectangular rank-two physical bound with an arbitrary opposite bank is `<6.937 [w Delta_2(B)^2]^(-1/5)`. For `r=3`, `C_3=2.4131915266`, giving `<3.979 [w Delta_3(B)^2]^(-1/7)`.

This strictly extends the preceding B09 five-coordinate `2x2` double-null theorem to a full-row-rank physical bank against an arbitrary-size opposite bank, while retaining arbitrary quadratic curvature on both banks. It avoids square-root small-ball decoupling; smoothing is Fourier `L^4` slice mass plus rank-r bilinear Plancherel.

## Newest-source splice already identified

The current volume-stability theorem at `math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba` applies directly to the same physical cross block `B`: if its third-volume row marginals satisfy `alpha_i<=2/3`, then (conditioning only the hub scalar) the ambient form has

`||p_Q||infinity <= (9 sqrt(3)e/2) e_3(B^T B)^(-1/6)`.

Thus the new hub theorem is complementary to the current diffuse three-volume exit; it attacks aligned high-leverage/full-row-rank packets rather than re-proving that paid branch.

Remaining gap: no claim is made that three large eigenvalues force a universal-scale `w Delta_r(B)^2`, or that the aggregate `e_2` Schur currency from the newest four-hub result contains one such fixed-row packet dimension-free. That extraction/aggregation is still open.
