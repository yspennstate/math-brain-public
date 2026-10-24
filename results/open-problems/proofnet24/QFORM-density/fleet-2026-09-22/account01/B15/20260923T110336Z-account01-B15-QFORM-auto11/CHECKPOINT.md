# Early substantive checkpoint — fixed unit Gaussian heat is an exact sharp normal form

Let `gamma_epsilon(u)=(sqrt(2*pi)*epsilon)^(-1) exp(-u^2/(2 epsilon^2))` and, for a probability measure `mu` on R, let

`H(mu)=inf{C: mu<=C dx}` in `[0,infinity]`.

## Measure-level heat identity

For every probability measure,

`H(mu)=sup_{epsilon>0} ||mu*gamma_epsilon||_infinity = lim_{epsilon downarrow 0} ||mu*gamma_epsilon||_infinity`.

Proof sketch: if `mu<=C dx`, convolution gives `||mu*gamma_epsilon||inf<=C`. Conversely, if all heat regularizations have height at most `M`, then `mu*gamma_epsilon dx -> mu` weakly, so for every nonnegative `phi in C_c`, `int phi dmu <= M int phi dx`; hence `mu<=M dx`. Monotonicity in epsilon follows from the Gaussian semigroup and Young's inequality.

## Exact target scaling

Write `s=s_3(A)` and `Q=X^TAX`. The sharp owner constant equals both

`C_* = sup_target H(mu_Q) = sup_target s H(mu_Q)`

and

`C_* = sup_target s ||mu_Q*gamma_1||_infinity`.

Indeed, for `0<epsilon<=1`, replace `A` by `A/epsilon`. Then `s_3(A/epsilon)=s/epsilon` and

`(mu_(Q/epsilon)*gamma_1)(y/epsilon)=epsilon (mu_Q*gamma_epsilon)(y)`.

Hence

`(s/epsilon)||mu_(Q/epsilon)*gamma_1||inf = s||mu_Q*gamma_epsilon||inf`.

Taking `epsilon downarrow 0` recovers `s H(mu_Q)` exactly. Therefore the universal raw density theorem is equivalent, with the same sharp constant and without assuming raw continuity, to one fixed-scale positive smooth inequality

`sup_target s_3(A) sup_y E gamma_1(X^TAX-y) < infinity`.

This checkpoint will be combined with the completed account02/B15 random-critical-value posterior bridge in the final report.
