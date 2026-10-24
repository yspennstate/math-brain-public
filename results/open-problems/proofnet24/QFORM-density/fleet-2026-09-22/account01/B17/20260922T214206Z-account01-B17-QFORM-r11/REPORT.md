SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B17, 2026-09-22T21:42:06Z.
attacking: sharp constant and source-valid rotated/heavy-row witnesses; in this run, the collinear two-heavy minority-sign branch after adding one independent minority-sign diffuse spectral mode.

# QFORM-COLLINEAR-HEAVY-PLUS-MINORITY-MODE-SHARP-v1

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260922T214206Z-account01-B17-QFORM-r11`  
Status: `SUPPORTING_SHARP-WITNESS_THEOREM / FULL QFORM OPEN`  
Execution memory: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact source and partner dependency

Fresh control source: `yspennstate/math-research-brain@a5b23d98a887d4065cb42c2d54b3ce7086a3934a`, OWNER CONTROL revision `2026-09-22.15`; a prepublication refresh later observed the same QFORM-only target and no B17 stop.

Completed designated partner result actually applied: account02/B17 run `20260922T204449Z-account02-B17-QFORM-r19`, canonical proof

`yspennstate/math-open-problems@50913ed00c5943aaf2772473cbf17ddcb5bed090:proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/20260922T204449Z-account02-B17-QFORM-r19/REPORT.md`.

That result proves that one additional independent minority-sign Gaussian mode of coefficient `delta>0` multiplies the exact Gaussian `(1,1,-1)` peak by `(1+delta)^(-1/2)`. The theorem below shows that *the same exact multiplicative loss* persists for the much more concentrated collinear two-heavy branch, for all symmetric-decreasing cap-one heavy laws; this is a direct application of the partner Laplace factor to a non-Gaussian heavy-core inequality.

Standing corrections preserved: no post-rotation independence, no arbitrary-joint coarea bound, no conditional-density cap/moment, no law-uniform pointwise stationary-phase estimate, no one-minor structural shortcut, and no claim that a branch result solves full QFORM.

## 2. Main theorem

Let `X,Y` be independent real random variables with probability densities `f,g` satisfying

- `0<=f,g<=1`,
- `f(x)=f(-x)` and `g(x)=g(-x)`,
- `f,g` are nonincreasing on `[0,infinity)`.

Let `G1,G2,G3` be iid standard Gaussians, independent of `X,Y`, and let `delta>0`. Define

`T_delta = G1^2+G2^2 - 6(X+Y)^2 - delta G3^2`.

Then `T_delta` has a bounded continuous density whose global maximum is attained at zero and

`||p_{T_delta}||_infinity = p_{T_delta}(0)`

`= [1/(2 sqrt(1+delta))] E exp[-3(X+Y)^2]`

`<= B0/sqrt(1+delta)`,

where

`B0 = int_0^1 (1-u) exp(-3u^2) du`

`   = [sqrt(pi)/(2sqrt(3))] erf(sqrt(3)) - [1-e^(-3)]/6`

`   = 0.34597473829274946420...`.

The upper bound is attained by `X,Y iid Uniform[-1/2,1/2]`. Thus the sharp standardized constant in this limiting class is

`B0/sqrt(1+delta)`.

After the physical variance-`1/12` scaling used by the QFORM diffuse-bank witnesses, the sharp constant is

`C_col(delta) = 12 B0/sqrt(1+delta)`

`= [2sqrt(3pi) erf(sqrt(3)) -2+2e^(-3)]/sqrt(1+delta)`.

Numerically,

`C_col(0)=4.1516968595129935704... < 3sqrt(2)=4.2426406871192851464...`,

and

`C_col(1)=2.9356930027925308825...`.

Therefore one fixed minority-sign diffuse spectral mode gives the exact strict multiplicative loss `(1+delta)^(-1/2)` from the already-subcritical collinear two-heavy branch.

## 3. Proof: the negative radial component has decreasing density

Put `V=X+Y`. Since `f` and `g` are even decreasing, their convolution `h=f*g` is also even decreasing. Set

`S = 6V^2 + delta G3^2`.

Consider the two-dimensional vector

`R=(sqrt(6)V, sqrt(delta)G3)`.

Its joint density is

`rho(x,y) = [1/sqrt(6)] h(x/sqrt(6)) * [1/sqrt(delta)] phi(y/sqrt(delta))`,

where `phi` is the standard Gaussian density. This density is even and coordinatewise nonincreasing in `(|x|,|y|)`.

Since `S=|R|^2`, polar coordinates give, for `s>0`,

`h_S(s) = (1/2) int_0^(2pi) rho(sqrt(s)cos(theta), sqrt(s)sin(theta)) dtheta`.   (3.1)

For every fixed angle, both absolute coordinates on the right increase as `s` increases. Hence the integrand is nonincreasing in `s`; therefore `h_S` is nonincreasing on `(0,infinity)`.

This is the key two-dimensional radial monotonicity step. It is source-valid because `V` is produced from the two original independent heavy coordinates and `G3` is the limit of an independent original-coordinate diffuse bank. No independence is asserted after an arbitrary spectral rotation.

## 4. Exponential-positive-core lemma

Let

`U=G1^2+G2^2`.

Then `U` is exponential with density

`g_U(u)=(1/2)e^(-u/2) 1_{u>=0}`,

and `U` is independent of `S`. Thus `T_delta=U-S`.

For `t>=0`,

`p_T(t)=(1/2)e^(-t/2) int_0^infinity e^(-s/2) h_S(s) ds`

`      = e^(-t/2) p_T(0)`,

so the nonnegative half-line is maximized at zero.

For `a>=0`,

`p_T(-a)=(1/2)e^(a/2) int_a^infinity e^(-s/2)h_S(s) ds`.

Define

`F(a)=e^(a/2) int_a^infinity e^(-s/2)h_S(s) ds`.

`F` is absolutely continuous and, for almost every `a`,

`F'(a)=F(a)/2-h_S(a)`.

Since `h_S` is nonincreasing,

`int_a^infinity e^(-s/2)h_S(s) ds <= h_S(a) int_a^infinity e^(-s/2)ds = 2e^(-a/2)h_S(a)`,

so `F'(a)<=0`. Hence the negative half-line is also maximized at zero. Therefore

`||p_T||_infinity=p_T(0)`.

## 5. Exact zero density and the partner factor

At zero,

`p_T(0)=(1/2) E exp[-S/2]`

`       =(1/2) E exp[-3V^2] * E exp[-delta G3^2/2]`

`       =[1/(2sqrt(1+delta))] E exp[-3(X+Y)^2]`.   (5.1)

The factor `(1+delta)^(-1/2)` is exactly the minority-sign Gaussian-mode factor proved by the completed account02/B17 partner theorem. Equation (5.1) is its direct insertion into the collinear heavy-core branch rather than a citation-only use.

It remains to maximize the heavy-core Laplace term within the stated symmetric-decreasing cap-one class.

## 6. Sharp cap-one extremizer inside the symmetric-decreasing class

Let `k(v)=e^(-3v^2)`, which is even decreasing. For fixed `g`,

`H_g(x)=int g(y)k(x+y)dy`

is even decreasing because it is the convolution of two even-decreasing functions. Under the constraints `0<=f<=1`, `int f=1`, the bathtub principle therefore gives

`int f(x)H_g(x)dx <= int_(-1/2)^(1/2) H_g(x)dx`.

Now fix `f=1_[-1/2,1/2]`. The analogous function of `y` is again even decreasing, so a second bathtub step gives

`E e^(-3(X+Y)^2)`

`<= int_(-1/2)^(1/2) int_(-1/2)^(1/2) e^(-3(x+y)^2) dx dy`.

For two centered unit intervals, `X+Y` has triangular density `(1-|u|)1_{|u|<=1}`. Hence

`E e^(-3(X+Y)^2) <= 2 int_0^1 (1-u)e^(-3u^2)du =2B0`,

with equality for the centered unit intervals. Combining with (5.1) proves the theorem.

## 7. Source-valid finite target family

For each integer `m>=1`, use three disjoint blocks of `m` physical coordinates, all iid `Uniform[-1/2,1/2]`, plus two independent heavy coordinates having the chosen symmetric-decreasing cap-one laws `f,g`.

Let `u_1,u_2,u_4` be the normalized all-ones vectors on the three diffuse blocks. Let `u_3` be the vector supported on the two heavy coordinates with entries `(1/sqrt(2),1/sqrt(2))`. These four vectors are orthonormal. Define

`A_{m,delta}=u_1u_1^T+u_2u_2^T-u_3u_3^T-delta u_4u_4^T`.

Every finite matrix has exact nonzero spectrum

`{1,1,-1,-delta}`,

so the original QFORM hypothesis (at least three eigenvalues of magnitude at least one) holds for every `delta>0` and every `m`.

If `Q_{m,delta}=X_phys^T A_{m,delta} X_phys`, then, writing the standardized diffuse block sums as `H_{j,m}`,

`12 Q_{m,delta}=H_{1,m}^2+H_{2,m}^2-6(X+Y)^2-delta H_{4,m}^2`.

The ordinary local CLT gives `H_{j,m}` converging to standard Gaussians. For each fixed `delta>0`, this convergence upgrades to uniform convergence of the output densities: the normalized Irwin-Hall densities are symmetric unimodal with uniformly bounded total variation, and the standard quadratic van-der-Corput/BV estimate gives

`|E exp(it H_{j,m}^2)| <= C min(1,|t|^(-1/2))`

uniformly in `m`; the fourth-bank factor gives the same estimate with `|delta t|`. The product of the three diffuse square factors is therefore bounded by an integrable `C_delta min(1,|t|^(-3/2))`. Dominated Fourier inversion yields

`||p_{12Q_{m,delta}}-p_{T_delta}||_infinity ->0`.

Thus the theorem is the exact asymptotic sharp constant for a genuine finite-dimensional original-coordinate QFORM family, not for an arbitrary dependent spectral relaxation.

## 8. Consequence for sharp-witness search

The existing lower obstruction `3sqrt(2)` comes from the fully diffuse `(1,1,-1)` Gaussian limit. The completed partner result showed a fixed extra minority-sign Gaussian mode lowers that diffuse peak by `(1+delta)^(-1/2)`. The present theorem shows the same exact factor survives even after replacing the minority direction by the much more concentrated collinear two-heavy physical construction, and it remains sharp over all symmetric-decreasing cap-one heavy laws.

Therefore a witness exceeding `3sqrt(2)` cannot arise from this architecture. In particular, arbitrary centered/unimodal reshaping of the two collinear heavy laws plus one independent minority-sign diffuse spectral mode is excluded. A larger witness must use a mechanism outside this class: non-symmetric/fragmented heavy laws, genuinely non-collinear heavy rows, multiple interacting macroscopic rows across spectral signs, non-Gaussian residual banks, finite/mesoscopic overshoot, off-zero geometry not reducible to a decreasing negative radial density, or a coupled spectral tail.

This is a supporting sharp-witness theorem only. It does not prove the full arbitrary-matrix conjecture and does not settle the separate continuity target.
