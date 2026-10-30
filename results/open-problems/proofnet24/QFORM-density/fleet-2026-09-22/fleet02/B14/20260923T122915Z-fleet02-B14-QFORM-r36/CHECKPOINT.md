# fleet02/B14 r36 early mathematical checkpoint

Status: supporting mathematics; full QFORM open.

## Exact full-target localization from partner r34

Let `D_n` be all cap-one product probability laws and `F_n` product indicator laws whose one-dimensional sets are compact finite unions of intervals of total length one. For measurable `P:R^n->R`, define the extended small-ball density functional

`Lambda(P,mu)=sup_{t in R,h>0} h^(-1) mu{t<=P<t+h}`.

Fleet03/B14 r34 proves, for every nonnegative Borel `G`, exact equality of `sup_mu int G dmu` over `D_n` and `F_n`. Apply it to `G_{t,h}=h^(-1)1_{t<=P<t+h}` and commute the suprema:

`sup_{mu in D_n} Lambda(P,mu)=sup_{nu in F_n} Lambda(P,nu)`.

Hence the exact universal QFORM constant (extended-real) is unchanged if every input marginal is restricted to an indicator of a compact finite union of intervals of total length one. The same equality holds simultaneously after taking suprema over arbitrary affine terms. There is no uniform fragment-count, diameter, location, tail, shift or moment bound.

## Global power form of the pair-log compiler

The earlier source-pinned B14 theorem gives, for an invertible indefinite original-coordinate pair with `D=|det B|`, `kappa=sigma_min(B)`, and completed remainder density cap `H`,

`C_log=6[H/(kappa sqrt(D))]^(1/3)` below the transition and
`C_log=D^(-1/2)[3+2 log theta]`, `theta=2 sqrt(2DH/kappa)`, above it.

For every `H>0` the single global inequality

`C_log(D,kappa,H) <= 6 [H/(kappa sqrt(D))]^(1/3)`

holds. In the upper branch put `u=theta^(2/3)>=1`; then the right side is `3u/sqrt(D)` and `3+3 log u<=3u`.

## Random-coefficient protected-anchor consequence

Suppose after the pair completion the remainder, conditional on any other outside original coordinates, has

`R=rho(Z)+2(gamma Z+beta)V`,

where `Z,V` are independent cap-one original coordinates, `rho` is arbitrary measurable, and `gamma!=0`. Conditional on `Z=z`, `R` has density cap

`H(z)=1/[2|gamma z+beta|]`

(the exceptional zero coefficient occurs on a null set). Therefore

`||p_Q||inf <=6(2 kappa sqrt(D))^(-1/3) E|gamma Z+beta|^(-1/3)`.

Since `gamma Z+beta` has density cap `1/|gamma|`, the elementary layer-cake bound

`E|gamma Z+beta|^(-1/3) <= 3*2^(-2/3)|gamma|^(-1/3)`

gives

`boxed: ||p_Q||inf <= 9 [kappa sqrt(D)|gamma|]^(-1/3).`

This is uniform in `beta`, `rho`, arbitrary shifts, fragmented/unbounded supports and all moments. It keeps the protected anchor `V` whole; arbitrary positive fragmentation of `Z` after the pointwise conditional estimate is exactly additive and introduces no normalization loss.

Next: combine this with the Claude physical-coordinate theorem to close an exact-target four-coordinate hyperbolic-plus-zero-self Schur branch, and apply the newest partner square-root critical-budget theorem as an independent uniform-anchor benchmark.
