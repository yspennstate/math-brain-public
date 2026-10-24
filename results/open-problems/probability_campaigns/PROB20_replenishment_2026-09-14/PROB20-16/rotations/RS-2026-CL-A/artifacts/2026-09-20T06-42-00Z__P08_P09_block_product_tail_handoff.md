# RS-2026-CL-A handoff — block-product chaos tail lemma for P08/P09

Owner/source remains `RS-2026-CL-A`, native slot `6aa7b4b639a08191b893e2b7dd6cdf59`. This is a reusable lemma handoff only; it does not claim P08/P09 source ownership.

## Exact lemma

Let the reference law factor across disjoint blocks,

`R = tensor_{j=1}^m R_j`,

and on each block let `{psi_{j,a}}` be an orthonormal chaos basis with nonnegative integer degree `deg(a)`. For

`h_j = sum_a c_{j,a} psi_{j,a}`

define the absolute coefficient generating function

`H_j(s)=sum_a |c_{j,a}| s^{deg(a)}`.

For the block product

`H = product_j h_j`,

tensorization gives an exact coefficient factorization, hence

`sum_alpha |Hhat(alpha)| s^{deg(alpha)} = product_j H_j(s)`.     (1)

If a product semigroup `T_rho` acts diagonally by

`T_rho psi_alpha = rho^{deg(alpha)} psi_alpha`,

then for every `z>=1` for which the right side is finite,

`sum_{deg(alpha)>D} |widehat{T_rho H}(alpha)|`

`<= z^{-(D+1)} product_j H_j(rho z)`.                           (2)

Proof: the left side is the tail of a nonnegative coefficient-generating series. Multiply every degree-`k>D` term by `z^k >= z^{D+1}`, use (1), and divide by `z^{D+1}`.

## Gaussian/Hermite form

For standard Gaussian blocks and normalized multivariate Hermites, Ornstein--Uhlenbeck has exactly the eigenvalue rule above. Thus any block-factorized Gaussian statistic whose local Hermite absolute-generating functions can be bounded at one radius `rho z>rho` receives an exponentially small high-chaos tail once

`log product_j H_j(rho z) = o(D)`.

This can be useful for P08/P09 when a hard-edge, minor, tensor-contraction, or surrogate decision statistic factorizes after conditioning or blocking. It is especially natural when each block event has a small local generating function even though the global raw Hermite support is enormous.

## Relation to the current RS theorem

The RS-2026-CL-A 06:42 report applies (2) exactly to complements of disjoint conjunction/cylinder events. In the Boolean binary case the local factor is

`H_j(rho z)=1-2*2^{-w_j}+2^{-w_j}(1+rho z)^{w_j}`,

which is at most `1+((1+rho z)/2)^{w_j}`. The same product-tail mechanism is therefore not specifically Boolean; only the local generating-function estimate is.

No novelty claim is made for tensorized coefficient-generating functions. The value of the handoff is the exact tail form (2) and the instruction to search for small local Hermite generating functions rather than a global Gram lower bound.