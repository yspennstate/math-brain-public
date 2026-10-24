# Early calculation — receiver-budget localization

Let `(Z,nu)` be a probability space, let `U=(U_1,...,U_m)` have independent cap-one probability densities `f_i`, and let `F(z,u)` be any measurable scalar core map. Push `nu(dz) prod_i f_i(u_i)du_i` by `(z,u)->(z,F(z,u))`; relative to `rho=nu tensor Lebesgue`, define

`B_p(f_1,...,f_m)=||dM_f/d rho||_Lp(rho)^p`, with value `+infinity` if no such Lp density exists.

Key proposed exact localization identity, for every `p>1`:

`sup_{0<=f_i<=1, int f_i=1} B_p(f_1,...,f_m)`
` = sup_{E_i bounded finite unions of intervals, |E_i|=1} B_p(1_{E_1},...,1_{E_m}).`

Reason: every cap-one probability density is an `L1` limit of finite convex mixtures of indicators of bounded finite-union sets of measure one. For compactly supported `f`, average it on a grid of cell length `1/K`; its occupancy vector `a_j in [0,1]` obeys `sum_j a_j=K`, hence lies in the hypersimplex, the convex hull of the `0/1` vectors with exactly `K` ones. Arbitrary `f` is first compactified without renormalization: `f 1_{[-R,R]}` plus an indicator of a disjoint interval whose length equals the missing tail mass; the `L1` error is at most twice that tail mass.

For a finite convex mixture of product extreme laws, the pushed joint measure is the same convex mixture. The functional `mu -> ||dmu/d rho||_p^p` (with `+infinity` off `L^p(rho)`) is convex and lower semicontinuous under total variation: a bounded liminf gives a weakly compact `L^p` density subsequence, and total variation identifies its weak limit with the target measure. Product `L1` approximation gives total-variation convergence of the joint source and hence of the pushforwards. This proves the identity with zero constant loss.

Composition target: account02/B14 r41 proves for `4/3<r<2`, `p=r/(r-1)`,

`||p_Q||_infty <= 2^{3(r-1)/(2r)} (2-r)^(-1/r) R0^{-(r-1)/r} B_p^{1/p}`

for `Q=T_Z+s(Z)+dW^2+(2b^T Z+e)W`, `R0=sqrt(d^2+||b||_2^2)`, with `W` independent cap-one. Therefore any uniform extreme-law bound `B_p<=K^p` transfers to all arbitrary cap-one core laws with the *identical* receiver constant; active score fragmentation is not needed.

Concrete quadratic family for the final check:

`Q=2cXY+2(u^T Z)X+2(v^T Z)Y+Z^T HZ+dW^2+2(b^T Z+e/2)W`.

Conditional on `Z=z`, complete the first three terms as

`2c (X+(v^Tz)/c)(Y+(u^Tz)/c) - 2(u^Tz)(v^Tz)/c`.

For every `p>1`, the translated hyperbolic product has

`||p_{2c(X-a)(Y-b)}||_p <= p |c|^{-1+1/p}`

by Minkowski plus the cap-one bathtub bound `E|Y-b|^{-alpha}<=2^alpha/(1-alpha)`, `alpha=1-1/p`. At `r=3/2`, `p=3`, account02/B14 r41 gives the full-score bound

`||p_Q||_infty <= 3*2^(7/6) |c|^(-2/3) (d^2+||b||^2)^(-1/6)`.

If `d!=0`, its whole-score-anchor corollary improves this to

`||p_Q||_infty <= 6 |c|^(-2/3)|d|^(-1/3)`.

For `|c|,|d|>=1`, the `(X,Y,W)` principal block has spectrum `{c,-c,d}`, so arbitrary `Z` curvature/couplings remain inside the exact three-large-eigenvalue target by interlacing. Full unrestricted QFORM is not claimed.
