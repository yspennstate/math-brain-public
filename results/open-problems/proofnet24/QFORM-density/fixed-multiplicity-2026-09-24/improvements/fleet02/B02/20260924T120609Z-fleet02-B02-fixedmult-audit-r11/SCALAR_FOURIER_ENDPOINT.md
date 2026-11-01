# Scalar-Fourier endpoint obstruction for the current 17-direction architecture

Run: `20260924T120609Z-fleet02-B02-fixedmult-audit-r11`
Source manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

## Exact exponent obstruction

For the admissible cap-one Gaussian

\[
f_G(x)=e^{-\pi x^2},
\]

we have `\int f_G=1`, `\|f_G\|_\infty=1`, and under the manuscript convention

\[
\widehat f_G(t)=e^{-t^2/(4\pi)}.
\]

Therefore, for every real `p>0`,

\[
\int_{\mathbb R}|\widehat f_G(t)|^pdt
=\int e^{-pt^2/(4\pi)}dt
={2\pi\over\sqrt p}.
\]

Consequently any law-uniform estimate of the form

\[
\int|\widehat f|^p\le C p^{-\alpha}
\]

for every probability density `0\le f\le1` forces `\alpha\le1/2`. The manuscript's `p^{-1/2}` exponent is therefore exact; only its constant `2\pi\sqrt{2e}` can be reduced by a sharper scalar inequality.

## Consequence for the determinant envelope

The present graph/regularizer calculation feeds this `p^{-1/2}` law into a fourth-power decoupling estimate and yields

\[
|\phi_Z(t)|\le\det\left(I+{t^2\over\pi^2e^2}M^TM\right)^{-1/8}.
\]

If one discards all determinant coefficients except `Z_k(M)`, the resulting tail is

\[
|\phi_Z(t)|\le \left({\pi e\,Z_k(M)^{-1/(2k)}\over |t|}\right)^{k/4}.
\]

Thus `k=4` is the exact Fourier-`L^1` endpoint `|t|^{-1}`, with logarithmic divergence. Merely improving scalar constants, the convolution cap, or the projection constant cannot turn order four into a direct density estimate while the determinant exponent remains `-1/8`.

The structural part of the current proof forces a lower crossing volume of order `k` from `4k-3` large singular directions. Since the current analytic density step requires `k=5`, the present closed chain lands at `4*5-3=17`.

## What would constitute a real threshold reduction

A rigorous threshold below 17 therefore needs a replacement argument that changes an exponent or structural count, not a constant-only optimization. Credible targets include: retaining several determinant degrees simultaneously and proving an integrable order-four endpoint; strengthening the decoupling/determinant exponent through an additional physical-coordinate mechanism without assuming rotated independence; or replacing the `rank(R)<=3r`/restricted-rank contradiction by an interpolation argument with a smaller global rank loss. Each route must retain arbitrary affine terms, arbitrary rough independent coordinate laws, arbitrary signature, and all nonzero coefficient tails.

This note is an obstruction to one proof-improvement strategy, not a theorem that 16 directions are insufficient and not a claim about the unrestricted three-eigenvalue conjecture.
