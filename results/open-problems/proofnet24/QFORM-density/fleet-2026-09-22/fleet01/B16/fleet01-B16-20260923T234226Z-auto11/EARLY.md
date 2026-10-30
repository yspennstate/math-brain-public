# fleet01/B16 early calculation — conditional minority-sign discriminant receiver

Programme `QFORM-DENSITY-3EIG-20260922`; full unrestricted target remains OPEN.

Pinned inputs actually used: fleet03/B16 true-near-coloop coordinates `math-open-problems@bdbe6e38a3ee3d586e8e6119e518c573310253fb`; the product-projection bound in `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`; newest completed designated partner fleet02/B16 r37 `math-open-problems@c9c865f02890e5fe7108c49759ee82b84f42ee38`. I also checked fleet02/B16's newer EARLY minority-sign calculation `657894f2d914b3f901cdfcff16ca97ba5c94e38e`; it is not treated as a completed partner result.

## New dependence-safe extension

Let `Z in R^2` have density `rho` with `||rho||_infinity<=M`. Let `Y` have a regular conditional density given `Z=z` bounded by `L` a.e.; `Y` need not be independent of `Z`. For

`Q=aY^2+2Y u^T Z+Z^T C Z+rY+s^T Z+c`,

put `B=[[a,u^T],[u,C]]`, with `a!=0`, and assume `a det B>0`. Then

`boxed: ||p_Q||_infinity <= 2 L sqrt(pi M) (a det B)^(-1/4).`

For target level `q`, the half-discriminant is

`D_q(z)=(u^Tz+r/2)^2-a(z^TCz+s^Tz+c-q)`.

Every real root in `Y` has derivative magnitude `2 sqrt(D_q(z))`, so the conditional root sum is at most `L D_q(z)^(-1/2)`. The quadratic matrix of `D_q` is `K=uu^T-aC`, and in dimension two

`det K=a det B>0`.

Thus `K` is definite. After completing the square, for every `eta>0`, irrespective of the sign of `K`,

`Leb{z:0<D_q(z)<eta} <= pi eta/sqrt(a det B)`.

Layer cake therefore gives

`p_Q(q)<=L integral_0^infinity min(1, pi M tau^(-2)/sqrt(a det B))d tau`
`      =2L sqrt(pi M)(a det B)^(-1/4)`.

No projected-coordinate independence is used. The key strengthening over the current fleet02/B16 EARLY calculation is that the scalar receiver may be conditionally dependent on the planar projection; only an actual conditional density cap is needed.

## Near-coloop insertion

In the source-pinned exact-rank-three near-coloop coordinates,

`Q=a(sqrt(c)X0+S)^2+2b(sqrt(c)X0+S)U+uU^2+2vUV+wV^2`,

set

`Y=X0+S/sqrt(c)+bU/(a sqrt(c))`.

Given `(U,V)`, `Y` is an average of translates of the untouched original-coordinate density of `X0`, hence `p_(Y|U,V)<=1`. The actual two-dimensional product-projection theorem gives `||p_(U,V)||_infinity<=2`. Also

`Q=acY^2+(U,V)^T B_a(U,V)`,
`B_a=[[u-b^2/a,v],[v,w]]`,
`det B_a=det Lambda/a`.

Therefore, on the minority-sign branch `a det Lambda>0`,

`boxed: ||p_Q||_infinity <= 2 sqrt(2pi)c^(-1/2)(|a| |det Lambda|)^(-1/4).`

This improves the previous sign-free half-Riesz prefactor `4 sqrt(2e)` to `2 sqrt(2pi)` on this sign branch while allowing the genuinely shared leaf shift `S`.
