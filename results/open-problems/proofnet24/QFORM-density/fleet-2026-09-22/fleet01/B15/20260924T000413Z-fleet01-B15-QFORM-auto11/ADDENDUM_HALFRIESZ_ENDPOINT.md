# Addendum: a bare half-Riesz small-ball certificate plus one square is still endpoint-critical

Programme: QFORM-DENSITY-3EIG-20260922.  
Run: `20260924T000413Z-fleet01-B15-QFORM-auto11`.  
Status: rigorous obstruction to an abstract proof interface; **not** a QFORM counterexample.

The fresh fleet01/B04 handoff isolates a remaining currency of the form

`sup_t P(|R-t|<rho) <= H sqrt(rho)`.

The `p>2` square-kernel theorem in this run shows exactly why this cannot be fed into a bare independent square by a black-box argument: the exponent `1/2` is critical.

## Proposition — `QFORM-HALFRIESZ-PLUS-BARE-SQUARE-NOT-SUFFICIENT-v1`

There exist a real random variable `R` and an independent cap-one random variable `V` such that

1. `R` has a probability density `g in L^1(R) cap L^2(R)`;
2. for one finite constant `H`,
   `sup_t P(|R-t|<rho) <= H sqrt(rho)` for every `rho>0`;
3. `V` has the triangular `C_0` probability density `h(v)=(1-|v|)_+`;
4. the density of `R+V^2` is unbounded.

### Construction and proof

On `-e^(-2)<r<0`, set

`g_0(r)=c/[sqrt(-r) log(1/(-r))]`

with `c>0` small enough that `m=int g_0<1`, and complete it to a probability density by adding a bounded compactly supported density of mass `1-m` away from zero.

First,

`int_0^(e^-2) du/[u log^2(1/u)]<infinity`,

so `g in L^2`; `g in L^1` is immediate.

For the small-ball estimate, on the singular piece and `0<rho<=e^-2/2`, any interval of length `2rho` has no more mass than the interval adjacent to zero, and

`int_0^(2rho) c du/[sqrt(u) log(1/u)] <= c sqrt(2rho)`

because `log(1/u)>=2` there. The bounded completion contributes at most `2M rho`, where `M` is its finite height. For larger `rho`, probability normalization gives `1<=C sqrt(rho)` after increasing the constant. Hence a finite global `H` exists.

Now let `V` be independent with `h(v)=(1-|v|)_+`. For `tau>0`, the density of

`T=R+V^2`

at `-tau` is

`p_T(-tau)=int h(v) g(-tau-v^2) dv`.

For small `tau`, restrict to positive `v` with `sqrt(tau)<=v<=e^(-1)/2`. On this range `h(v)>=1/2`, `tau+v^2<=2v^2`, and the singular part gives

`p_T(-tau) >= c_1 int_(sqrt(tau))^(e^-1/2) dv/[v log(1/v)]`.

The right side grows like `c_1 log log(1/tau)` and tends to infinity as `tau downarrow0`. Thus `||p_T||_infinity=infinity`.

## Consequence for current QFORM assembly

A generic half-Riesz / square-root small-ball estimate is **not by itself** enough to combine with one independent square and obtain bounded density. A successful splice must use more than the endpoint mass estimate: for example an `L^p` residual bound with some `p>2` (as in this run), a positive exponent gain `rho^(1/2+epsilon)`, or additional product/cancellation structure retained jointly with the square.

This does not challenge any completed QFORM theorem whose proof uses richer structure. In particular the exact null-pair-plus-square arguments retain more information than the black-box half-Riesz certificate.
