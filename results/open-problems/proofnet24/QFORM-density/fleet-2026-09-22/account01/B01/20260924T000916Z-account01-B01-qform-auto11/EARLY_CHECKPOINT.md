# Early checkpoint — three original-coordinate square chain

Run: `20260924T000916Z-account01-B01-qform-auto11`.

The pointwise scalar Fresnel estimate remains false and is not used. I am testing a distribution-function/fractional-potential replacement that is stable under arbitrary later-variable shifts.

Let `X` have density at most `M`, let `m,T` be measurable with respect to variables independent of `X`, and let `c!=0`. For every `0<beta<1/2`,

`H_beta(c(X+m)^2+T) <= (8 M^2/|c|)^beta/(1-2 beta)`.

Proof: for every center `s` and `eps>0`, the preimage in `x` of
`|c(x+m)^2-(s-T)|<eps` has Lebesgue length at most
`2 sqrt(2 eps/|c|)`. Hence its conditional probability is at most
`min(1,K sqrt(eps))`, `K=2 sqrt(2) M |c|^(-1/2)`. Layer cake gives

`beta int_0^infty eps^(-beta-1) min(1,K sqrt(eps)) d eps
 = K^(2 beta)/(1-2 beta)`.

Combining this with the already proved square-fractional upgrade from the preceding B01 run gives the following candidate theorem. For mutually independent original scalar coordinates `X0,X1,X2` with density caps `M0,M1,M2`, arbitrary outside source `W`, triangular shifts
`m2=m2(W)`, `m1=m1(X2,W)`, `m0=m0(X1,X2,W)`, arbitrary `R(W)`, and nonzero `a0,a1,a2`,

`Q=a0(X0+m0)^2+a1(X1+m1)^2+a2(X2+m2)^2+R(W)`

has an essentially bounded density, with for every `0<beta<1/2`

`||p_Q||_inf <= M0 |a0|^(-1/2)
 [ M1 |a1|^(-1/2) J_beta (8 M2^2/|a2|)^beta/(1-2 beta) ]^(1/(1+2 beta))`,

where
`J_beta=max{B(1/2,beta), B(1/2,1/2-beta)+B(1/2-beta,beta)}`.

At `beta=1/4` and cap-one inputs the constant is
`12.194582301486...`, with coefficient exponents
`|a0|^(-1/2)|a1|^(-1/3)|a2|^(-1/6)`.

This is immediately relevant to the account02/B01 zero-triple-currency finite-leak endpoint: if one support coordinate is completed and the exact cancellation makes its scalar Schur residual diagonal, any nonzero remaining diagonal coefficient supplies the third original scalar square. Under the target rank>=3 hypothesis such a coefficient must exist if the first two pivots are nonzero, otherwise congruence would force quadratic rank at most two.

This is an early checkpoint, not the final theorem statement or a full-QFORM claim.
