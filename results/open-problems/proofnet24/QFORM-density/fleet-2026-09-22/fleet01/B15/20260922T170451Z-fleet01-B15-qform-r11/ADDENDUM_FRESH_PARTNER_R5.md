# Fresh partner-r5 consequence for the B15 affine/normal-form theorem

After the main report was committed, fresh control exposed the completed `fleet02/B15` run `20260922T170424Z-fleet02-B15-qform-r5`, canonical source

`yspennstate/math-open-problems@42920d321a16b9393856cfb0ed78d8557170ad38`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260922T170424Z-fleet02-B15-qform-r5/REPORT.md`.

Its target-valid family is

`A_T=diag(1,1,1,T^{-3})`,

with three iid `Uniform[0,1]` coordinates and `X_4~Uniform[T^2,T^2+1]`. It proves, for `T>=17`, at

`t_T=T+1/4+(2/T+T^{-3})/2`,

that

`p_{Q_T}(t_T) >= pi*sqrt(3)/16 > 0.34008`,

while `t_T->infinity`.

This result applies directly to the main report's spectral normal form because

`boxed(s_3(A_T)=1)`

for every `T`. Hence even after the exact reduction `s_3(A)=1`, there is **no** target-uniform tail envelope `g(R)->0` and no automatic reduction of the peak search to a fixed compact output interval.

This does not alter the affine-homogenization theorem or the equality of sharp homogeneous and affine constants. It sharpens the nonclaim: the `s_3=1` normal form removes spectral scale, not output-location escape. Any universal height proof must remain local in height and pay product-coordinate curvature/aggregation directly.
