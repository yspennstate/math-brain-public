# r18 arithmetic / diagnostic checks

These checks corroborate constants only; the proofs are in `REPORT.md`.

1. For the optimized general-row concentration bound, with `L>=4`, `delta=2/L`, the exact logarithmic ratio is

`log(B/sqrt(x L)) = (L+log L-2log2)/(2L-2)`.

The report proves analytically that this is at most `2/3`: equivalently

`3 log L-6log2+4 <= L`,

which is equality at `L=4` and whose left-minus-right derivative is `3/L-1<=-1/4` for `L>=4`.

A numerical grid of 100000 points on `[4,1000]` gave maximum ratio-log `0.6666666666666666`, hence maximum multiplicative ratio `1.9477340410546757 = exp(2/3)` to displayed precision.

2. For iid `Uniform[-1/2,1/2]`, `T=2XU` has

`p_T(t)=log(1/(2|t|)) 1_{0<|t|<1/2}`,

and the density normalizes because

`2 int_0^(1/2) log(1/(2t)) dt = 1`.

The centered interval probability of length `ell` is exactly

`ell [1+log(1/ell)]` for `0<ell<1`.

3. For iid `Uniform[-1/2,1/2]`, `S=X+U` has triangular density `(1-|s|)1_{|s|<1}`. Therefore `S^2` has density `(1-sqrt(y))/sqrt(y)` on `(0,1)`, whose square is nonintegrable at zero. This exactly witnesses failure of a general physical-row `L^2` endpoint.

STATUS: PASS for the finite arithmetic diagnostic; no numerical check is used as a universal proof.
