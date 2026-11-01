# fleet02/B14 early calculation — whole-product logarithmic envelope and square closure

Run `20260923T235641Z-fleet02-B14-QFORM-auto11b`. Full QFORM remains open.

First unpaid implication: the newest fleet03/B14 smooth-connected construction proves that an interval-only half-Frostman frozen-slice profile does not control the overlapping rank-two receiver `2L(X-X')`; its density at zero can grow logarithmically. Instead of normalizing those slices, keep the entire product structure and pay the third independent curvature afterwards.

## Product envelope

Let `U,V` be independent probability densities bounded by one and put `Z=UV`. For `z!=0`,

`p_Z(z)=int f_U(u) f_V(z/u) du/|u|`.

If `0<|z|<1`, split into `|u|>=1`, `|z|<=|u|<1`, and `|u|<|z|`. The first part is at most one. The middle part is at most `2 log(1/|z|)`. In the last part substitute `v=z/u`; it becomes an integral over `|v|>1` and is at most one. If `|z|>=1`, the split `|u|>=1` / `|u|<1` gives one plus one. Hence

`p_Z(z) <= 2+2 log_+(1/|z|)`.

Therefore for `H=2aUV`, `a!=0`,

`p_H(x) <= |a|^(-1) [1+log_+(2|a|/|x|)]`.                                      (E1)

Arbitrary affine terms `alpha U+beta V` are harmless because

`2aUV+alpha U+beta V = 2a(U+beta/(2a))(V+alpha/(2a)) - alpha beta/(2a)`,

and translations preserve independence and the cap-one hypothesis.

## Independent-square closure

Let also `Y` be independent with density at most one, `lambda!=0`, and include arbitrary `gamma Y`. Completing the square reduces to bounding

`R=H+lambda Y^2`.

From (E1),

`p_R(t) <= |a|^(-1) [1 + E log_+(2|a|/|t-lambda Y^2|)]`.

For any `A,c>0`, any real `t`, and any cap-one density of `Y`,

`E log_+(A/|t-cY^2|) <= 4 sqrt(2A/c)`.                                             (E2)

Indeed layer cake gives an integral over `s>=0` of the Lebesgue measure of

`{y: |t-cy^2| < A e^{-s}}`.

For every `delta>0` and real `tau`,

`|{y: |tau-y^2|<delta}| <= 2 sqrt(2delta)`;

the maximum occurs when the interval in `y^2` starts at zero. Thus the layer measure is at most `2 sqrt(2A/c)e^{-s/2}`, whose integral is `4 sqrt(2A/c)`.

Taking `A=2|a|`, `c=|lambda|`,

`||p_R||_infinity <= |a|^(-1) + 8 / sqrt(|a lambda|)`.                             (E3)

In particular, if `|a|>=1` and `|lambda|>=1`, then

`||p_R||_infinity <= 9`.                                                           (E4)

The same bound is uniform over every deterministic affine coefficient in `(U,V,Y)` and hence survives arbitrary conditioning on outside original coordinates whenever the retained quadratic block is exactly `[[0,a,0],[a,0,0],[0,0,lambda]]`.

## Newest partner obstruction repaired by a genuine third resource

In fleet03/B14 run `20260923T233929Z-fleet03-B14-QFORM-auto11`, smooth strict-subcap connected-support laws were built so that `T=2L(X-X')` has `p_T(0) >= (3/16) log(1/(2 epsilon)) -> infinity`, despite uniform frozen-slice half-Frostman constants.

But `D=X-X'` has density at most one by Young and is independent of `L` and of an independent cap-one `Y`. Applying (E4) to

`Q=2LD+Y^2 = 2L(X-X')+Y^2`

gives

`||p_Q||_infinity <= 9`,                                                         (E5)

uniformly in the partner's support diameter, bridge floor, smoothing scale, translations and fragment geometry. In original variables `(L,X,X',Y)` the quadratic matrix has spectrum `{sqrt(2),-sqrt(2),1,0}`, so (E5) lies inside the exact owner target. The third independent square cures the logarithmic rank-two singularity only when the whole product is aggregated before slice normalization.

## Required fixed-source comparison

The completed Theorem A in `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `COUNTEREXAMPLE_SEARCH.md`, applies to the aggregated independent triple `(L,D,Y)` because its matrix has eigenvalues `{1,-1,1}` and all three laws have density at most one. It gives

`||p_Q||_infinity <= 6 sqrt(pi) = 10.634723105433...`.

Thus (E5) is a direct elementary sharpening on this source-valid exact-target family, while preserving the required arbitrary rough laws and affine translations.

Candidate theorem name: `QFORM-HYPERBOLIC-LOG-PLUS-SQUARE-CLOSURE-v1`.
