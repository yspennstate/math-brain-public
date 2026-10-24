# Early checkpoint — account02/B15

Programme `QFORM-DENSITY-3EIG-20260922`; run `20260924T030155Z-account02-B15-auto11-62cf32`.

The full universal problem remains open. I am attacking the local Schur remainder left after an invertible indefinite physical pair, with height paid before continuity.

## Scalar quadratic logarithmic potential

Let `V` have a probability density bounded by one, `b != 0`, and allow arbitrary affine terms. For

`Y=b(V-h)^2+c`

put `q=L/|b|`. For every centre `t`, layer cake and the exact interval-preimage estimate

`Leb{x: |x^2-a|<rho} <= 2 sqrt(2 rho)`

give

`E log_+(L/|Y-t|) <= Psi(q)`,

where

`Psi(q)=4 sqrt(2q)` for `0<q<=1/8`,

`Psi(q)=2+log(8q)` for `q>=1/8`.

Indeed `P(|(V-h)^2-a|<rho) <= min(1,2 sqrt(2rho))`, hence

`int_0^infty min(1,2 sqrt(2q) e^{-v/2}) dv`

is exactly the displayed piecewise bound. This is translation-uniform, requires no smoothness, and is a logarithmic-potential estimate rather than a continuity claim.

Combining it with the completed physical-pair envelope

`p_Q(t) <= 2sqrt(2)/r + Delta^(-1/2) E log_+(2r^2/[kappa|t-R|])`

shows that when the Schur remainder has a physical diagonal coefficient `b != 0`, then with `q=2r^2/(kappa|b|)`,

`||p_Q||_infinity <= 4(kappa|b|)^(-1/2) q^(-1/2) + Delta^(-1/2) Psi(q)`.

Optimizing gives the global convenient form

`||p_Q||_infinity <= Delta^(-1/2) [4 + log_+(32 Delta/(kappa|b|))]`.

For `kappa|b|>=32 Delta` the small-q optimizer yields the stronger quarter-power branch `2^(13/4)(Delta kappa |b|)^(-1/4)`; at the transition both equal `4/sqrt(Delta)`.

This improves the previous all-purpose square-root-small-ball averaging from polynomial to logarithmic dependence when a nonzero Schur diagonal is weak. The remaining structural problem is still to obtain a dimension-free aggregate certificate from `s_3(A)>=1`, not to infer height from continuity.
