SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B10, 2026-09-23T03:48:36Z.
attacking: the exact-rank-three near-null small-Pluecker-mass hub/star collar; preserve the original hub density rather than paying the scalar square kernel before the leaf geometry.

# Early substantive checkpoint: a target-valid logarithmic obstruction to raw near-null square peeling

Fresh source state before this calculation: brain main `fb1cd73d0912a1ef24d1ecea573c6c27780579dd`, OWNER CONTROL revision `2026-09-22.15`. Required Claude package read at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`. Latest designated partner read: account03/B10 `20260923T023946Z-account03-B10-QFORM-r23b`.

The partner reduces the genuine exact-rank-three debt to the collar `0<d<1/64` where one original row has leverage `c>1/4`, normalized Rayleigh quotient `<1/16`, and fixed aggregate star norm, unless a paid scalar-pivot or ruled branch applies. I test the tempting next step: complete the small nonzero physical square and try to bound its half-Riesz envelope uniformly.

For `0<eps<=1/64`, put `delta=eps^2`, `s=sqrt(1-eps^2)`. In an orthonormal spectral basis `(u,w,v)` let

```
M_eps = [[-eps, 0, s],
         [0,    1, 0],
         [s,    0, eps]].
```

The eigenvalues are exactly `{1,1,-1}` because the `(u,v)` block has trace zero and determinant `-1`.

Use the six-row Parseval frame

```
r1=u/sqrt(2),  r2=u/sqrt(2),
r3=sqrt(1-delta) w, r4=sqrt(delta) w,
r5=sqrt(1-delta) v, r6=sqrt(delta) v.
```

Then `R^T R=I_3`, so `A_eps=R M_eps R^T` is an exact target matrix with nonzero spectrum `{1,1,-1}`. Take all six original inputs iid `Uniform[-1/2,1/2]`; every input density is exactly one on its support.

Only triples selecting one row from each spectral line have positive Pluecker weight. Hence the probability that two independent Pluecker bases are disjoint is exactly

`d_eps = (1/2) [2 delta(1-delta)]^2 = 2 eps^4(1-eps^2)^2`,

so `0<d_eps<1/64`. The selected physical hub `r1` has leverage `c=1/2` and pivot

`A_11=-eps/2`.

Moreover `M_eps^2=I_3`, so

`sum_(j!=1) A_1j^2 = (A^2)_11-A_11^2 = 1/2-eps^2/4`.

Thus this is genuinely inside the near-null, fixed-star-resource survivor rather than a low-star degeneration.

Define the independent bank linear forms

`U=(X1+X2)/sqrt(2)`,
`W=sqrt(1-delta)X3+sqrt(delta)X4`,
`V=sqrt(1-delta)X5+sqrt(delta)X6`.

The quadratic form is exactly

`Q_eps=-eps U^2+2sUV+W^2+eps V^2`.

Completing only the ORIGINAL hub coordinate `X1` gives

`Q_eps=-(eps/2)[X1+X2-sqrt(2)sV/eps]^2 + R_eps`,

where the remainder is the positive rank-two form

`R_eps=W^2+V^2/eps`.

The standard cap-one conditional square change of variables therefore has the raw envelope at output zero

`B_eps = sqrt(2/eps) E[R_eps^(-1/2)]`.

This envelope is not uniformly bounded. Restrict the expectation to

`|X4|,|X6|<=1/4`, `|X3|<=1/4`, and `sqrt(eps)/2 <= |X5| <=1/4`.

On this set, writing `y=|X5|`, one has for `eps<=1/64`

`|W| <= 1/4+eps/4 <= y/sqrt(eps)`,

`|V| <= y+eps/4 <= (17/16)y`.

Hence

`sqrt(R_eps) <= (3/2)y/sqrt(eps)`,

and therefore `R_eps^(-1/2) >= (2/3)sqrt(eps)/y`. Integrating over the displayed rectangle (all source densities equal one) yields

`E[R_eps^(-1/2)] >= (sqrt(eps)/6) log(1/(2sqrt(eps)))`.

Consequently

`boxed: B_eps >= (sqrt(2)/6) log(1/(2sqrt(eps))) -> infinity.`

This is an explicit target-valid falsifier of the intermediate claim that the near-null branch can be closed by completing the physical square and then uniformly bounding the resulting unconditional half-Riesz square envelope. It does NOT refute QFORM. In fact the completed ruled one-sheet theorem in the required Claude package applies to this same exact-rank-three family and gives the real inequality

`p_(Q_eps)(0) <= pi sqrt(2)`.

Thus the logarithmic loss is created by discarding the location of the original hub density before integrating the transverse product geometry; it is not a real output-density singularity.

First unpaid implication after this checkpoint: obtain a minority-sign/two-sheet estimate in the partner's `0<d<1/64` near-null hub/star collar that keeps the original hub density factor coupled to at least one transverse bank (or an equivalent cross-transverse/Fresnel object). A scalar half-Riesz envelope depending only on the Schur remainder cannot be the final interface.

Status: rigorous supporting counterexample to an intermediate mechanism; full QFORM remains OPEN.
