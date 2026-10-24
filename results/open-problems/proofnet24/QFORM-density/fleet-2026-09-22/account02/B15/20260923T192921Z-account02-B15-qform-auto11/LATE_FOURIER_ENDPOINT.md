# Late Fourier-endpoint obstruction

A later compatible frontier handoff recorded the sharp product-Fourier endpoint (`math-open-problems@f34ca21deff2e7fdae04b4b238fdd249ba7f0c80`): if `g` is the density of `HL` for independent cap-one `H,L`, then

\[
\|g\|_2^2\le4,
\qquad
\int_{\mathbb R}|\mathbb E e^{itHL}|^2dt\le8\pi,
\]

with equality at the density endpoint for iid `Uniform[-1/2,1/2]`; after the `e^{2itHL}` normalization the Fourier `L^2` integral is at most `4\pi`.  Uniform Fourier `L^p` control holds for `p>=2` and fails for every `p<2`.

This sharpens the current leakage obstruction.  A one-dimensional quadratic Fresnel factor is only of generic size `|t|^{-1/2}` at high frequency.  To prove absolute integrability of a factorized product by Hölder, one would need

\[
\|\widehat{\mathcal L(HL)}\|_{L^p}<\infty,
\qquad
\||t|^{-1/2}\|_{L^q(1,\infty)}<\infty,
\qquad
1/p+1/q=1.
\]

The Fresnel term belongs to `L^q(1,infty)` only for `q>2`, which forces `p<2`.  The sharp endpoint theorem says exactly that no uniform cap-one estimate is available there.  At the endpoint `p=q=2`, Cauchy--Schwarz sees the logarithmic divergence

\[
\left(\int_1^T |\phi_{HL}(2t)|^2dt\right)^{1/2}
\left(\int_1^T t^{-1}dt\right)^{1/2}
\lesssim \sqrt{\log T},
\]

so it cannot produce a uniform `L^1_t` characteristic-function bound.

Therefore the new sharp `L^2` theorem is a genuine route obstruction: the missing high-leverage/diffuse-light receiver cannot be obtained by separating the bilinear `HL` factor and the quadratic `V^2` Fresnel factor and then applying absolute Hölder norms.  One must retain signed cancellation in the complete phase, use the full diffuse product provenance (for example the open twisted-Wiener estimate), or trigger another structural receiver.  This conclusion is compatible with the owner-pinned ruled majority-side estimate and does not affect its rough-input total-variation passage.
