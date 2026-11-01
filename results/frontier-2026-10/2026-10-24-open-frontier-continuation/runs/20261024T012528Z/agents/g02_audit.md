# T384 audit: varying-residual relay, grazing, release, and phase uniqueness

**Scope and status.** The statements below are deterministic local results for one two-input endpoint while one projected coordinate remains strictly positive. They apply to the actual Euler projected update with its changing output weight, provided the resulting coefficients have the stated limit. The countable-atom statement is a conditional uniqueness theorem for a prescribed common phase. Neither result supplies the phase entrance rule or proves that a network remains in that phase.

## Exact finite-grid identities with changing `W/a`

Let `G=[[1,rho],[rho,1]]`, `|rho|<1`, let `h` be the physical time step, and write the projected endpoint state scaled by `L` as `(x_n,y_n)=V_n/L`, the actual scaled output weight as `z_n=W_n/a`, and the current common residual as `r_n=(r_{1,n},r_{2,n})`. Assume `y_n>0` at every node and throughout the polygonal segment under consideration. Standard simultaneous GD gives exactly

\[
 x_{n+1}=x_n+h[c_n+a_n s_n],\qquad
 y_{n+1}=y_n+h[z_n r_{2,n}+\rho a_n s_n],
 \quad s_n={\bf1}_{x_n>0},
 \quad a_n=z_n r_{1,n},\quad c_n=\rho z_n r_{2,n}.
 \tag{1}
\]

The identity

\[
 y_N-\rho x_N=y_0-\rho x_0
 +(1-\rho^2)h\sum_{n<N}z_n r_{2,n}                 \tag{2}
\]

is exact for every grid, with no frozen-residual, slowly varying, or gate-occupation hypothesis. It is the robust part of `e03_discrete.md`, equation (10a), after replacing its frozen `z` by the actual `z_n`. In particular it controls the tangential coordinate even when the normal gate chatters. It does **not** by itself give a fixed-weight Schur formula for the actual finite-grid output `z_n(x_n^+,y_n)`: changing `z_n` contributes a product-rule term. In the macroscopic regime of `MACRO_COMPACTNESS.md`, each retained atom has `sup_{n\le T/h}|z_n-z_0|=o_P(1)`, so this extra term vanishes for the limiting endpoint contribution. If `z(t)` had order-one variation instead, then on a sliding path `p_2=z(t)y(t)` would satisfy `p_2'=z^2(1-rho^2)r_2+z' y`, rather than the Schur term alone.

Put `d_n=-a_n-c_n`; the on-side normal drift is `-d_n`, the off-side drift is `c_n`. If, on an interval, `0\le c_n\le C`, `0\le d_n\le D` and `x_0\in[-hD,hC]`, the entire interval obeys

\[
 -hD\le x_n\le hC.                                      \tag{3}
\]

Indeed an off step moves right by at most `hC` and an on step moves left by at most `hD`. This remains true at **grazing**, when `c` or `d` reaches zero; strict lower margins are needed for uniform *capture from a fixed off-face distance*, not for persistence of an already trapped `O(h)` orbit. From (2), on such a trapped interval,

\[
 y_N-y_0=(1-\rho^2)h\sum_{n<N}z_n r_{2,n}
              +\rho(x_N-x_0),                                \tag{4}
\]

with endpoint error at most `2|rho|h max(C,D)` relative to the integrated tangential drift. No slow variation is required for this estimate. At a face with `a<0`, `c>0`, and `d>0`, the normal balance is `theta=-c/a=c/(c+d)\in(0,1)` and the limiting output action is the Schur action from `FACE_SCHUR.md`. At `d=0`, `theta=1` can still describe a grazing contact. It ceases to be an admissible face fraction when `d<0`: the formal quotient exceeds one, and both normal drifts point to the positive side. Similarly `c<0`, with `d>0`, releases to the negative side. The face formula must stop at such a release.

## A monotone relay selector through grazing and release

Here is a stronger local statement that does not need a preassigned strict sliding cone. Let `a,c` be bounded measurable functions on `[t_0,T]` with `a(t)\le0` almost everywhere. Define the relay graph

\[
 H(x)=\begin{cases}\{0\},&x<0,\\[0,1],&x=0,\\\{1\},&x>0.\end{cases}
\]

For any initial `x(t_0)`, the differential inclusion

\[
 x'(t)=c(t)+a(t)\theta(t),\qquad \theta(t)\in H(x(t)) \quad\text{a.e.}                \tag{5}
\]

has **at most one normal path**. In fact, for two solutions with coefficients `(a,c)` and `(\tilde a,\tilde c)`, both with relay fractions in `H` and with `a\le0`, monotonicity of `H` gives `(x-\tilde x)(\theta-\tilde\theta)\ge0`. Writing the difference equation with `a(\theta-\tilde\theta)+(a-\tilde a)\tilde\theta` and differentiating a smooth approximation of `|x-\tilde x|` yields

\[
 \sup_{t_0\le s\le t}|x(s)-\tilde x(s)|
 \le |x(t_0)-\tilde x(t_0)|
 +\int_{t_0}^t (|c-\tilde c|+|a-\tilde a|)\,ds.       \tag{6}
\]

This is a pathwise input-stability estimate. It remains valid if `a` merely touches zero. It does not identify `theta` on a zero set where `a=0`; that nonidentifiability has no effect on the path or the output action.

For existence and Euler selection, take grids `h_m\downarrow0`, uniformly bounded held coefficients `a_m,c_m` converging in `L^1([t_0,T])` to `a,c`, and initial nodes converging to `x_0`. Let the Euler polygon use `s_{m,n}=1_{x_{m,n}>0}` in (1). Uniform derivative bounds give uniformly convergent subsequences of the polygons; the held gates admit weak-star subsequential limits `theta\in[0,1]`. The node-to-polygon discrepancy is `O(h_m)`. On compact subintervals where the limiting `x` is strictly positive or negative, all sufficiently fine node gates have the corresponding fixed value. Thus `theta\in H(x)` almost everywhere. The `L^1` coefficient convergence passes `a_m s_m` through the integral equation, so every subsequential path solves (5). Estimate (6) makes all subsequential paths identical, proving uniform convergence of the entire Euler sequence. This argument allows bounded-variation residuals and weight paths with jumps as long as their held coefficients converge in `L^1`; continuity is available in the actual macroscopic residual limit and is stronger than needed. It also permits small finite-grid violations of `a_m\le0` if the limiting `a\le0`, because uniqueness is applied only to the limit.

The second coordinate is then forced by (2): if `z_m r_{2,m}\to z r_2` in `L^1`, its polygon converges uniformly to

\[
 y(t)=y(t_0)+\rho[x(t)-x(t_0)]
       +(1-\rho^2)\int_{t_0}^t z(s)r_2(s)\,ds.         \tag{7}
\]

The proof is conditional on `y` retaining a positive margin; then the Euler `y_m` is positive on a slightly smaller interval for all sufficiently fine grids. In the actual endpoint regime `z_m\to z_0` uniformly on fixed physical horizons, so the limit uses the constant mark `z_0`. Equation (5) gives an unambiguous path through strict sliding, grazing, and release **for a fixed residual input**. It does not establish that the self-consistent residual input is unique without the coupled estimate below.

There is an explicit form when `c\ge0` and `x(t_0)\ge0`. Put `g=c+a` and `w(t)=x(t_0)+\int_{t_0}^t g(s)\,ds`. The unique relay path is the one-sided Skorokhod reflection

\[
 x(t)=w(t)+K(t),\qquad
 K(t)=\max\left\{0,-\inf_{t_0\le s\le t}w(s)\right\}.       \tag{7a}
\]

To verify it directly, the negative part of any solution cannot increase: on `x<0` its derivative is `-c\le0`, while on `x=0` its derivative is zero almost everywhere. Thus `x\ge0`. Since `x'=g` when `x>0`, the regulator `K=x-w` is nondecreasing and can grow only on `x=0`; there `x'=0` almost everywhere and hence `K'=-g\ge0`. These properties uniquely give the running-minimum formula. At a positive-measure sliding zero set with `g\le0`, the required fraction is `theta=-c/a` whenever `a<0`. At an outward release with `g>0`, the path immediately enters `x>0` and then uses `theta=1` almost everywhere. This formula permits repeated release and recapture for an arbitrary prescribed residual, subject to `c\ge0`, `a\le0`, and continued positivity of the other support. If `rho>0`, `x(t_0)=0`, `y(t_0)>0`, and `z r_2>0` throughout, then (7) gives `y(t)=y(t_0)+rho x(t)+(1-rho^2)\int z r_2>0`, so that support condition is self-consistent. This observation begins after a positive-support phase has already been identified; it does not select the original marked entrance at `(0,0)`.

## What happens at loss of strict inward margin

Assume `c(t)\ge c_0>0`, `a(t)<0`, and `x(t_*)=0`. Suppose `d=-a-c\ge0` immediately before `t_*` and `d<0` immediately after. The pre-exit solution stays on `x=0` if it was already captured. For `t>t_*`, both the off drift `c` and on drift `-d` point right; (5) therefore releases into `x>0`. Once positive, the normal trajectory is

\[
 x(t)=\int_{t_*}^t [-d(s)]\,ds                              \tag{8}
\]

for the first interval on which `d<0`. This **integrated drift**, not an instantaneous continuation of `theta=-c/a`, matches the exit. If `d(t_*)=0` and `d'(t_*)=-\kappa<0`, then `x(t)=\kappa(t-t_*)^2/2+o((t-t_*)^2)`: macroscopic onset is quadratic and has zero right derivative at release. A grid path trapped in (3) just before exit is `O(h)` from the face. Once `d_n\le0`, it crosses from any negative position in the strip after at most `\lceil D/c_0\rceil+1` off steps and then stays positive; its subsequent on drift sums `-h d_n`. Its path therefore converges to (8), regardless of microscopic phase. If approximate coefficients have imperfect signs very near `t_*`, apply the relay convergence theorem, or bracket the event outside `[t_*-\delta,t_*+\delta]` and let `\delta\downarrow0`.

Loss of strictness alone is **not** release. For example `c=1`, `d(t)=(t-t_*)^2` gives `a=-1-d<0` and a trapped path converging to `x\equiv0`; `theta=c/(c+d)` merely touches one. In contrast, `c=1`, `d(t)=-(t-t_*)` on a short interval with `a=-1-d<0` gives the rightward release (8). The microscopic time of the *last* on/off switch need not converge at order `h`: a positive `O(h)` phase near a transversal zero of `d` can survive for an `O(\sqrt h)` interval on the attracting side, since the cumulative inward drift there is quadratic. The path error remains `O(h)` in that example. Accordingly, switch-time convergence and path convergence are different claims.

This also changes the tangential output after release. Take `rho=1/2`, `z=1`, `r_2=2`, and `r_1(t)=-1+t` near `t_*=0`. Then `c=1`, `d=-t`, and for `t>0` the relay gives `x=t^2/2`. Formula (7) gives `y(t)=y(0)+(3/2)t+t^2/4`; incorrectly continuing the sliding Schur drift gives only `y(0)+(3/2)t`. The formal continuation `theta=1/(1-t)>1` exposes the invalid step. Symmetrically, if `d\ge d_0>0` and `c` crosses from nonnegative to negative at `t_*`, the path releases left with `x(t)=\int_{t_*}^t c(s)\,ds<0` on the first negative interval. A transversal `c'(t_*)<0` again gives quadratic onset; the support coordinate then follows its off-side drift, not the Schur drift.

## Conditional uniqueness of a coupled countable phase

Fix countably many endpoint marks `z_i` with `\sum_i z_i^2<\infty`. On a common interval `[t_0,T]`, assign to each atom one boundary index `b_i` and the other index `p_i`. Suppose two candidate macroscopic systems have the same initial endpoint states and residual, the same fixed `C`, and the same assignments; every assigned `p_i` coordinate remains positive in both systems, and `z_i r_{b_i}(t)\le0` in both systems almost everywhere. Each endpoint obeys the two-coordinate inclusion (5) for its boundary coordinate, with `a_i=z_i r_{b_i}`, `c_i=\rho z_i r_{p_i}`, and the Schur identity (7) for its positive coordinate. Suppose also that both candidates satisfy the absolutely convergent residual Volterra equation

\[
 r(t)=R-C\int_{t_0}^t r(s)\,ds
  -\sum_i z_i\bigl[(q_i(t))_+-(q_i(t_0))_+\bigr].       \tag{9}
\]

For `D(t)=\sup_{t_0\le s\le t}\|r(s)-\tilde r(s)\|`, (6) gives

\[
 |q_{i,b_i}(t)-\tilde q_{i,b_i}(t)|
 \le |z_i|(1+|\rho|)\int_{t_0}^t D(s)\,ds.
\]

Equation (7) and `|rho|(1+|rho|)+(1-rho^2)=1+|rho|` give the same bound for the positive coordinate. Therefore

\[
 \|z_i[(q_i)_+-(\tilde q_i)_+]\|
 \le \sqrt2(1+|\rho|)z_i^2\int_{t_0}^t D(s)\,ds.
\]

The square-mass assumption makes the endpoint sum finite, and (9) yields

\[
 D(t)\le\left(\|C\|+\sqrt2(1+|\rho|)\sum_i z_i^2\right)
                 \int_{t_0}^t D(s)\,ds.
\]

Gronwall gives `D=0`, then all endpoint paths agree. This pays uniqueness **within the shared sign/support phase**, even with countably many coupled atoms and grazing/release of their designated boundary gates. It does not prove that actual GD selects the common assignments, that every `p_i` stays positive, or that `z_i r_{b_i}\le0` globally. In particular the phase hypotheses can be incompatible across marks of opposite signs, so this is not a global network uniqueness theorem.

## Audit points for any proposed stronger statement

1. A changing finite-grid `z_n` is harmless for (2), but a Schur formula for the actual output needs either `z_n\to z` uniformly or its product-rule contribution retained.
2. Strict inward margins can be relaxed to nonnegative margins for *persistence* of an already trapped strip. They cannot be dropped for uniform capture from a fixed off-face distance.
3. At `d<0` the formal face fraction exceeds one. The valid continuation is a positive-side relay path with integrated on drift. A tangential zero of `d` may graze without release.
4. Normal relay uniqueness uses the sign `a=z r_b\le0`. If that sign fails, the comparison argument reverses, and the origin/face selection can again be nonunique.
5. Countable coupled uniqueness assumes the same local support and sign phase for both candidates. It does not supply entrance or phase validity from initial marks.

## Review of companion arguments in this run

I checked `agents/g01_sliding.md` and `PHASE_UNIQUENESS.md` against the exact update. The former's changing-weight recursion, strip entry and invariance, summation-by-parts occupation bound, product-rule output remainder, and `O(L^2/a^2)` weight-variation bound are consistent with (1)--(4). Its strict margins correctly restrict its capture and Schur conclusion to that phase. The latter's countable Volterra comparison is valid under its common support/sign assumptions; its infinity-norm constant `(1+rho)\sum z_i^2` is sharper than the Euclidean constant used above for `0<rho<1`. Neither companion establishes initial marked entrance or phase validity, which they explicitly leave open. The reflection formula above strengthens only the prescribed-residual local selector after the positive support has been secured.
