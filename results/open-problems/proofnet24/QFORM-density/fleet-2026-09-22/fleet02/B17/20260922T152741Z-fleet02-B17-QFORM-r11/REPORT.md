# B17 sharp-witness report — semigaussian mixed-leverage endpoint

Run: `20260922T152741Z-fleet02-B17-QFORM-r11`
Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`.
Status: **supporting theorem proved in stated scope; full conjecture remains OPEN / NOT PROVED**.
Execution state: `WITHOUT_VERIFIED_BRAIN`.

## Target and source pins

Full target: independent real physical coordinates with densities bounded by one, arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, and one universal bound for the density of `X^T A X`.



## Theorem: exact cap-one semigaussian endpoint

Let `Z_1,Z_2` be independent standard normals, let `X` be independent of them with an arbitrary probability density `f` satisfying `0 <= f <= 1`, and let

`d_1,d_2 >= 1/12`, `c >= 1`.

Set

`Q = d_1 Z_1^2 + d_2 Z_2^2 - c X^2`.

Then `Q` has a bounded density and

`||p_Q||_infinity <= C_SL`,

where

`C_SL = sqrt(6*pi) erf(sqrt(3/2))`

`     = 3.980105675042008833977028419721609826...`.

The constant is **sharp in this semigaussian class**: equality is attained at level zero for

`d_1=d_2=1/12`, `c=1`, `X ~ Uniform[-1/2,1/2]`.

In particular

`C_SL < 3 sqrt(2) = 4.242640687119285146405066172629094235...`,

with gap

`3 sqrt(2)-C_SL = 0.262535012077276312428037752907484409...`.

This theorem is not the full QFORM conjecture; the Gaussian variables here represent diffuse projection limits and are not being asserted to be physical cap-one coordinates.

## Proof

Write `Y=d_1 Z_1^2+d_2 Z_2^2`, `D=max(d_1,d_2)` and

`A_0 = 1/(2 sqrt(d_1 d_2))`.

The convolution of the two scaled chi-square-one laws is explicit. For `s>=0`,

`p_Y(s) = A_0 exp[-s(1/d_1+1/d_2)/4] I_0(s|1/d_1-1/d_2|/4)`,

where `I_0` is the modified Bessel function. Since `I_0(u) <= exp(|u|)`,

`p_Y(s) <= A_0 exp[-s/(2D)]`.                                            (1)

Conditioning on `X=x` therefore gives, for every real `t`,

`p_Q(t) = int p_Y(t+c x^2) 1_{t+c x^2>=0} f(x) dx`.                        (2)

### Nonnegative levels

For `t>=0`, (1)-(2) and `c>=1` give

`p_Q(t) <= A_0 int exp[-x^2/(2D)] f(x) dx`.

The kernel is even and decreases with `|x|`. Among all probability densities bounded by one, the bathtub principle maximizes the integral by `f=1_[-1/2,1/2]`. Hence

`p_Q(t) <= 2 A_0 int_0^(1/2) exp[-u^2/(2D)] du`.                            (3)

### Negative levels

Write `t=-r`, `r>0`, and `L=sqrt(r/c)`. From (1)-(2),

`p_Q(-r) <= A_0 exp[r/(2D)] int_{|x|>=L} exp[-c x^2/(2D)] f(x) dx`.

On the allowed set `|x|>=L`, the even decreasing kernel is maximized under `0<=f<=1`, `int f=1` by filling the nearest total unit length,

`[-L-1/2,-L] union [L,L+1/2]`.

Thus, after `x=L+u` and using `cL^2=r`,

`p_Q(-r)`
` <= 2 A_0 int_0^(1/2) exp[-sqrt(c r) u/D - c u^2/(2D)] du`
` <= 2 A_0 int_0^(1/2) exp[-u^2/(2D)] du`.                                 (4)

So (3)-(4) reduce the full level supremum to one scalar expression. If `d=min(d_1,d_2)>=1/12`, then

`2 A_0 = 1/sqrt(Dd) <= sqrt(12/D)`.

Therefore

`||p_Q||_infinity`
` <= sqrt(12/D) int_0^(1/2) exp[-u^2/(2D)] du`
` = sqrt(12) int_0^(1/(2 sqrt(D))) exp[-y^2/2] dy`.

Because `D>=1/12`, the last upper integration endpoint is at most `sqrt(3)`, so

`||p_Q||_infinity <= sqrt(12) int_0^sqrt(3) exp[-y^2/2]dy`
` = sqrt(6*pi) erf(sqrt(3/2)) = C_SL`.

All inequalities are equalities for `d_1=d_2=1/12`, `c=1`, `t=0`, and the centered unit interval density. This proves sharpness within the stated semigaussian class.

## Actual source-valid mixed-leverage family

The theorem is the exact endpoint of an **actual target-valid finite construction**. For each `m`, take `2m+1` independent physical coordinates, all `Uniform[-1/2,1/2]`. Let

`S_{1,m}=m^(-1/2) sum_{k=1}^m U_{1,k}`,
`S_{2,m}=m^(-1/2) sum_{k=1}^m U_{2,k}`,

and retain one independent coordinate `X_0`. Let `r_1,r_2` be the normalized block-average vectors and `e_0` the last coordinate vector, and set

`A_m = r_1 r_1^T + r_2 r_2^T - e_0 e_0^T`.

Then `A_m` has exactly three nonzero eigenvalues `(1,1,-1)` and

`Q_m = S_{1,m}^2 + S_{2,m}^2 - X_0^2`.

The one-dimensional local CLT for normalized sums of bounded uniforms gives uniform convergence of the densities of `S_{j,m}` on compact sets to `N(0,1/12)`. If `q_m` is the density of `S_{1,m}^2+S_{2,m}^2`, polar coordinates give

`q_m(s) = (1/2) int_0^(2*pi) h_m(sqrt(s) cos theta) h_m(sqrt(s) sin theta) d theta`.

Thus uniformly for `0<=s<=1/4`, `q_m(s) -> 6 exp(-6s)`. Consequently

`p_{Q_m}(0) = int_{-1/2}^{1/2} q_m(x^2) dx -> 12 int_0^(1/2) exp(-6x^2) dx = C_SL`.

Hence the mixed-leverage endpoint is genuinely source-valid: two spectral modes are fully diffuse across growing physical blocks while the opposite-sign mode stays on one physical coordinate. Its limiting peak is nevertheless strictly below `3 sqrt(2)`.

## Application of the partner result

The completed fleet03/B17 theorem proves that every fixed-frame repeated-uniform fully diffuse stress approaches `3 sqrt(2)` from **below**, with an explicit positive first-order penalty. The present family deliberately escapes that fixed-frame regime by making one opposite-sign eigenvector maximally localized. The exact endpoint calculation shows that this escape moves the limiting peak *down* to `C_SL=3.9801056750...`, approximately `93.8119904%` of `3 sqrt(2)`.

Therefore neither of the two endpoint mechanisms now tested can exceed the current lower-bound scale:

1. fixed-frame fully diffuse repeated-uniform arrays: approach `3 sqrt(2)` from below (partner theorem);
2. two fully diffuse same-sign modes plus one maximally localized cap-one opposite-sign mode: sharp ceiling `C_SL<3 sqrt(2)` (this report).

A witness above `3 sqrt(2)`, if one exists, must use a genuinely intermediate/mesoscopic leverage profile, a nonperturbative fragmented source, multiple interacting localized modes, or an off-zero maximum not covered by this endpoint argument.

## Why a projected-density cap alone is insufficient

The same proof with only `||f_X||_infinity<=M` gives the sharp endpoint bound

`C_SL(M)=12 M int_0^(1/(2M)) exp(-6u^2)du`

at `d_1=d_2=1/12`, `c=1`. It increases from `C_SL(1)` toward `6` as `M` grows. The unique numerical crossing

`C_SL(M_*) = 3 sqrt(2)`

occurs at

`M_* = 1.1079013713103109840...`.

Thus once a projected mesoscopic mode has density cap above about `1.108`, a proof that remembers only that one-dimensional cap cannot certify the `3 sqrt(2)` scale. Any sharp argument in the remaining mixed-leverage regime must exploit the mode's **source provenance / convolution shape**, not merely its projected `L^infinity` norm. This is a proof-design obstruction, not a counterexample to QFORM.

## Remaining implication

The full target is still open. The sharp-witness search should now attack the genuinely mesoscopic bridge between the two endpoint regimes, with source-valid finite product constructions and exact off-zero density checks. The most diagnostic next family is: two growing diffuse same-sign blocks and an opposite-sign block whose support size `k=k(m)` grows sublinearly, allowing fragmented cap-one physical marginals. One must determine whether its output peak can exceed `3 sqrt(2)` or prove a source-provenance contraction before taking any projected-density cap.
