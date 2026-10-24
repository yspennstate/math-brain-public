# Supplement — positive-measure scalar fibers

This strengthens the report's scalar-conditioning obstruction so it is independent of regular-conditional versions at a single conditioning value.

Keep the exact family from `REPORT.md` and write

`d = X1-X4 = 2+s`, `0<=s<=delta/2`.

Then `Y4=d/sqrt(2)` and

`b(s)=Q'=3Y4^2 = 3(2+s)^2/2`.

The support constraints force

`X4 in [1-delta,1-s]`,

whose length is

`w=delta-s in [delta/2,delta]`.

The negative root `Y4=-d/sqrt(2)` has no support. Hence, for every such `s`, the natural conditional law is

`X4 | {Q'=b(s)} ~ Unif[1-delta,1-s]`.

Consequently

`Y1=(2X4+d)/sqrt(2)`

is uniform on

`[(4+s-2delta)/sqrt(2), (4-s)/sqrt(2)]`,

of length `sqrt(2)w`. Put `Z=Y1^2`. Its upper endpoint is

`z_+(s)=(4-s)^2/2`,

and its support width is exactly

`L_s = z_+(s)-z_-(s)=w(8-2delta)`.

Since `z<=8`, throughout this support

`p_(Z|Q'=b(s))(z) >= 1/(8w)`.

The independent opposite-sign pair `D=2(X2^2-X3^2)` still satisfies, for `0<r<=1/4`,

`p_D(r) >= (1/4) log(1/(2r))`.

Because `delta<=1/64`, `L_s<1/4`. Evaluating the conditional core density at `z_+(s)` gives

`p_(Q3|Q'=b(s))(z_+(s))`

` >= (1/(32w)) int_0^(L_s) log(1/(2r)) dr`

` = [(4-delta)/16] [log(1/(4w(4-delta)))+1]`

` >= [(4-delta)/16] [log(1/(4delta(4-delta)))+1].`

The right side tends to infinity like `(1/4)log(1/delta)` uniformly for every `s in [0,delta/2]`.

Moreover the scalar remainder density is strictly positive throughout this whole interval. Indeed

`p_(Q')(b(s)) = w/[3(2+s)] >= delta/[6(2+delta/2)] >0`.

Therefore the bad conditional density occurs on a positive-measure interval of `b` values, not merely at one fiber. In particular even the **essential** supremum in the scalar conditioning variable diverges across this admissible target family:

`ess sup_b ||p_(Q3|Q'=b)||_infinity -> infinity` as `delta->0`.

Thus `QFORM-SCALAR-SPECTRAL-CONDITIONAL-SUP-UNIVERSAL-v1` is refuted in the version-invariant sense relevant to the integral identity for the full density. The replacement obligation remains: keep `p_(Q')(b)` inside the integral and aggregate before taking any worst-fiber supremum.
