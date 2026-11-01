# fleet02/B16 early calculation — fixed-determinant hyperbolic half-trace barrier

Programme `QFORM-DENSITY-3EIG-20260922`; full unrestricted target remains OPEN.

The previous B16 early discriminant calculation proved that, for a literal cap-one hub and a genuine two-dimensional leaf marginal of density at most `M`, a nonzero scalar pivot whose discriminant quadratic is definite obeys

`||p_Q||_infinity <= 2 sqrt(pi M) |det K|^(-1/4)`.

The unresolved majority-sign pivot has indefinite discriminant. The cap-only failure can be made exact even at fixed determinant.

Take `K=diag(1,-1)`. For `R>1`, introduce hyperbolic coordinates

`r=u-v`, `t=u+v`, so `u^2-v^2=rt` and `du dv=(1/2)dr dt`.

Let

`Omega_R={1<=r<=R, 0<t<=2/(r log R)}`

and let `rho_R` be the indicator of its image in `(u,v)` coordinates. Its total mass is

`(1/2) integral_1^R 2/(r log R) dr =1`,

so `rho_R` is a probability density with `||rho_R||_infinity=1`. But

`integral (u^2-v^2)_+^(-1/2) rho_R(u,v) du dv`
`= (1/2) integral_1^R r^(-1/2) integral_0^{2/(r log R)} t^(-1/2) dt dr`
`= sqrt(2 log R) -> infinity`.

Therefore **no estimate depending only on a bounded planar joint-density cap and `|det K|` can control the positive half-Riesz trace when `K` is indefinite**, even with `||rho||_infinity=1` and `|det K|=1`.

This is an interface obstruction, not a QFORM counterexample: `rho_R` is not asserted to be an orthogonal projection of a product law. The latest compatible designated partner, fleet03/B16 r38, strengthens the endpoint relevance by proving logarithmic divergence of the same hub-first trace on an authentic exact-target near-coloop product family. The final report will combine the exact discriminant sign identity with that source-valid partner example and the pinned ruled one-sheet theorem.
