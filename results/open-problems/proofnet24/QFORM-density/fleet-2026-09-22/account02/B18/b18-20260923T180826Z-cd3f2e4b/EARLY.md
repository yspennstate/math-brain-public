# account02/B18 — early punctured-edge obstruction

Programme `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN.

First unpaid local implication: in the exact-rank-three null-hub heavy branch, control a heavy witness `q_i>1/2` with `0<|g_i|<1/64` and source-entangled twist, without deleting the small edge or inferring post-rotation independence.

## Completed partner applied at a real inequality

Account03/B18 r31 proves the full-matrix exact-zero-edge receiver

`T=2U(<g,Z>+eta)+aV^2+B(Z)V+C(Z)`,

for mutually independent original cap-one `U,V,Z_j`, `a!=0`, with

`||p_T||_infinity <= 6 e^(-1/3) (|a| ||g||_2^2)^(-1/3)`.

Apply it with `g=1`, `eta=0`, `a=1`, `B=0`, and, for a fixed `0<c<=1`,

`C(W)=-W^2/c^2`,

where `U,V,W` are independent Uniform[-1/2,1/2]. The exact-zero-edge companion

`Q_(0,c)=2UW+V^2-W^2/c^2`

therefore has a continuous `C_0` density with

`||p_(Q_(0,c))||_infinity <= 6 e^(-1/3)`.

## New obstruction: an arbitrarily small nonzero edge can stack the saddle

Turn on only the physical `U-V` edge `c`:

`Q_c=2U(W+cV)+V^2-W^2/c^2`.

Then

`Q_c=(V+W/c)(2cU+V-W/c)=:ST`.

The coefficient matrix is

`A_c=[[0,c,1],[c,1,0],[1,0,-c^(-2)]]`.

It has determinant zero. Its two nonzero eigenvalues are the roots of

`x^2-((c^2-1)/c^2)x-(c^4+c^2+1)/c^2=0`.

At `x=1` the polynomial equals `-(1+c^2)<0`; at `x=-1` it equals `-(c^4-c^2+2)/c^2<0`. Hence one root is `>1` and the other is `<-1`: this is a genuine two-large-eigenvalue, rank-two configuration.

The output density is nevertheless unbounded. Indeed the rank-two linear image `(S,T)` of the cube has a joint density `rho`. Holding `w` fixed, the map `(u,v)->(s,t)` has Jacobian magnitude `2c`, while

`v=s-w/c`,
`u=(t-s)/(2c)+w/c^2`.

Put `delta=c^2/16`. If `|s|,|t|<=delta` and `|w|<=c^2/8`, then `|u|,|v|,|w|<1/2`. Therefore

`rho(s,t) >= (c^2/4)/(2c)=c/8`

throughout the square `[-delta,delta]^2`. For `0<|z|<delta^2`, the product pushforward formula gives

`p_(Q_c)(z)=integral rho(s,z/s) ds/|s|`
`          >= (c/8) log(delta^2/|z|)`.

Thus

`||p_(Q_c)||_infinity=infinity`

for every `0<c<=1`, although the exact-zero-edge companion is uniformly bounded by the completed account03/B18 theorem and the matrix difference is only the off-diagonal edge `c` (operator norm `c`).

This is NOT a QFORM counterexample: `A_c` has only two nonzero eigenvalues. It is a source-valid counterexample to the tempting punctured transfer "replace `A_uv=0` in the partner theorem by sufficiently small `|A_uv|` while leaving the residual quadratic function arbitrary." The exact-zero-edge theorem is genuinely singular at this level of generality.

## Why the target can still escape this obstruction

For the actual exact-rank-three null-hub target, completing the physical pair `(0,i)` gives the exact rank-one critical remainder

`R_i=lambda_i (u_i dot Z)^2`,
`lambda_i=d gamma^2 q_i/g_i^2`,

and target normalization gives

`g_i^2 |lambda_i|=|d| gamma^2 q_i=h D q_i>1/10`

on the heavy branch. LPP on the normalized original-source projection gives

`sup_t P(|R_i-t|<rho) <= 4 |g_i| (hDq_i)^(-1/2) sqrt(rho)`
`                         < 4 sqrt(10) |g_i| sqrt(rho)`.

So the true target has an improving `O(|g_i|)` anti-stacking constant precisely where the rank-two counterexample has zero Schur curvature. Existing generic pair-log smoothing spends this but still loses `kappa_i^(-1/4)`.

The sharpened debt is therefore: prove a zero-pivot triangular pair smoothing estimate for `B_i=[[0,g_i],[g_i,a_i]]` that combines the `O(|g_i|)` critical-value anti-concentration with the pair singularity without paying `kappa_i^(-1/4)`, or construct a target-valid counterexample. Any proof that only says the edge is small is impossible by the construction above.
