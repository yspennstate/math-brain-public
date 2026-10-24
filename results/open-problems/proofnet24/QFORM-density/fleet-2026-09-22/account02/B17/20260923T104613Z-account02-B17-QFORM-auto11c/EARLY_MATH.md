# Early substantive checkpoint — non-lightlike two-partial-heavy exact-spectrum stress family

Programme `QFORM-DENSITY-3EIG-20260922`; account02/B17. Full QFORM remains open.

Fix `u in S^2` and `B_u=I_3-2uu^T`, so `spec(B_u)={1,1,-1}`. For `0<=ell<1` and integer `m`, take a synthesis matrix `C_{m,ell}` whose physical columns are `sqrt(ell)e1`, `sqrt(ell)e2`, then `m` copies each of `sqrt((1-ell)/m)e1`, `sqrt((1-ell)/m)e2`, and `m` copies of `e3/sqrt(m)`. Thus `C C^T=I_3`. Hence `A_{m,ell,u}=C^T B_u C` has exact nonzero spectrum `{1,1,-1}` for every finite `m`. Put independent `Uniform[-1/2,1/2]` laws on every physical coordinate; all input densities are exactly one.

For fixed `ell`, as the three banks diffuse,

`Y_ell=(sqrt(ell)U1+sqrt(1-ell)G1, sqrt(ell)U2+sqrt(1-ell)G2, G3)`,

with independent centered unit intervals `U1,U2` and iid `G_j~N(0,1/12)`. The output is `Q_{ell,u}=Y_ell^T B_u Y_ell`.

Using the already proved one-dimensional variance-matched expansion from the preceding B17 partial-heavy theorem,

`f_ell(y)=gamma(y)[1-(ell^2/20)H4(y/sigma)]+O(ell^3)(1+|y|)^(-8)`, `sigma^2=1/12`,

the product law gives the signed second-order perturbation only in axes 1 and 2. Cone integration at output zero yields

`p_{ell,u}(0)=3sqrt(2)[1-c12(u)ell^2+O(ell^3)]`,

`c12(u)=[114+6(u1^2+u2^2)-39(u1^4+u2^4)]/640`.

This coefficient is uniformly positive. Writing `s=u1^2+u2^2 in [0,1]` and using `u1^4+u2^4<=s^2`,

`640 c12 >=114+6s-39s^2 >=81`,

so `c12(u)>=81/640` for every orientation.

For the fully coupled non-lightlike orientation `u=(1,1,1)/sqrt(3)`, one has diagonal entries `1/3`, off-diagonal entries `-2/3`, so the residual third bank has genuine quadratic curvature and couples to both heavy axes; here exactly `c12=41/240`.

Remaining step for this run: upgrade the central expansion to the GLOBAL output maximum and transfer it back to finite exact witnesses. The intended transfer uses the pinned completed Fresnel–Brascamp–Lieb theorem at `math-open-problems@e5f71d79...`: for `ell<=1/2,m>=2`, every physical leverage is at most `1/2`, hence `|phi_m(t)|<=min(1,(4pi)^(3/2)|t|^(-3/2))`. This is an actual integrable inequality on the present matrices and should give uniform density convergence from the bank CLT.
