# Positive-correlation mixed double cone: exact frozen entrance and finite sliding certificate

**Status: deterministic theorem for a frozen endpoint.** This proves a finite-step dead-or-certified-sliding classification and its stability under strict parameter and mark perturbations. It does not identify the residual-coupled network after a cone exit, nor does finite-grid convergence by itself justify taking an increasing number of boundary steps.

## The frozen grid and the four velocities

Fix `0<rho<1`, `gamma>0`, `z>0`, and a frozen mixed residual `r=(-R,S)` with

\[
 S>0,\qquad \rho S<R<S/\rho.
\tag{1}
\]

For `v_n=(x_n,y_n)` use the exact strict pre-step gates

\[
v_{n+1}=v_n+\gamma z
 \begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}
 \operatorname{diag}(\mathbf1_{x_n>0},\mathbf1_{y_n>0})r.
\tag{2}
\]

Equivalently, set `a=zR`, `b=zS`, `c=rho*b`, `d=a-c`, `e=b-rho*a`, and `kappa=(1-rho^2)b`. By (1), all six of `a,b,c,d,e,kappa` are positive. The velocity in `--` is `(0,0)`; in `+-` it is `(-a,-rho*a)`; in `-+` it is `(c,b)`; and in `++` it is `(-d,e)`. Each velocity is multiplied by `gamma` in the update. In particular, while `y>0`, its increment is either `gamma*b` or `gamma*e`, both strictly positive. While `y<=0,x>0`, both coordinates strictly decrease. These facts hold at an exact hit of an axis because the gate at zero is off.

## Exact all-mark classification

**Dead branch.** If `y_0<=0,x_0<=0`, the row is dead immediately. If `y_0<=0,x_0>0`, put `N=ceil(x_0/(gamma*a))`. For `0<=n<=N`,

\[
(x_n,y_n)=(x_0-n\gamma a,\;y_0-n\gamma\rho a).
\tag{3}
\]

Here `x_n>0` for `n<N`, and `y_n<=0` throughout; at `N`, `x_N<=0` and `y_N<0`. The row then stays exactly fixed. This covers `y_0=0` under the prescribed strict gate.

**Sliding branch.** If `y_0>0`, induction using the two positive support drifts proves `y_n>0` for every `n`. Put `s_n=1_{x_n>0}` and `eta_n=y_n-rho*x_n`. For every step, including normal-axis hits,

\[
x_{n+1}-x_n=\gamma[c-(c+d)s_n],\qquad
\eta_{n+1}-\eta_n=\gamma\kappa>0.
\tag{4}
\]

Thus `eta_n=eta_0+n gamma*kappa`. The normal coordinate enters the invariant strip

\[
I_\gamma=[-\gamma d,\gamma c]
\tag{5}
\]

in finitely many steps. More precisely, the first entry index is at most

\[
E(x_0)=\begin{cases}
0,&x_0\in I_\gamma,\\
\left\lceil (x_0-\gamma c)/(\gamma d)\right\rceil,&x_0>\gamma c,\\
\left\lceil (-\gamma d-x_0)/(\gamma c)\right\rceil,&x_0<-\gamma d.
\end{cases}
\tag{6}
\]

Indeed, above the strip each step subtracts `gamma*d`; below it each adds `gamma*c`. The crossing step cannot jump across its opposite endpoint. Inside the strip, a nonpositive point adds `gamma*c` and a positive point subtracts `gamma*d`, so the strip is invariant. Formula (6) is in fact the first entry index when `x_0` is outside the strip.

For any `C_*>c` and `D_*>d`, define the enlarged strip `J_gamma=[-gamma*D_*,gamma*C_*]`. After the entry index `E`, choose any finite integer `N>=E` satisfying

\[
\eta_N>\rho\gamma D_*.
\tag{7}
\]

Such an `N` exists by (4), for example `N=E+max(0, floor((rho*gamma*D_*-eta_E)/(gamma*kappa))+1)`. At `N`, the two strict conditions `x_N` in the **interior** of `J_gamma` and (7) certify `y_N=eta_N+rho*x_N>0`, and certify persistent positive support and normal trapping under the perturbations described next. The first condition follows automatically from `x_N in I_gamma` since `C_*>c,D_*>d`.

Consequently the exact frozen selector, including the strict-gate axis convention, is

\[
\sigma_\gamma(x_0,y_0;z,r)=
\begin{cases}\text{sliding on support 2},&y_0>0,\\
\text{dead},&y_0\le0.
\end{cases}
\tag{8}
\]

In this double cone it is independent of `x_0` and of `gamma`. The original mark and `gamma` still determine the finite transient, capture index, and oscillating normal phase; (8) does not assert an eventually fixed binary gate.

## Perturbation-robust meaning of the certificate

Choose a compact neighborhood of `(z,r)` within the **larger attracting cone**, so that at all later steps its possibly varying coefficients obey

\[
0<c_*\le c_n\le C_*,\quad
0<d_*\le d_n\le D_*,\quad
b_n=z_nr_{2,n}\ge b_*>0.
\tag{9}
\]

Here `c_n=rho*b_n` and `d_n=-z_n(r_{1,n}+rho*r_{2,n})`; the neighborhood need not retain the extra inequality `e_n>0` after certification. Use the same fixed `gamma` in this boundary-grid statement. Whenever `y_n>0`, equations (4) remain true with step-dependent coefficients and `kappa_n=(1-rho^2)b_n`. The strip `J_gamma` is forward invariant: a point with `x<=0` gains at most `gamma*C_*`, while one with `x>0` loses at most `gamma*D_*`. If `x_n in J_gamma` and `eta_n>rho*gamma*D_*`, then `y_n>0`; after the step, `eta` increases by at least `gamma*(1-rho^2)b_*`, so the same strict certificate holds inductively. Thus a **single finite state certificate** gives support persistence and normal trapping for every future coefficient sequence satisfying (9). In the actual macroscopic scaling `q=v/L`, the identical statement uses `h=gamma/L` and strip `[-hD_*,hC_*]`.

There is a corresponding finite robust dead certificate. A strictly negative terminal pair `x_N<0,y_N<0` remains dead exactly, regardless of later residual changes, because both gates are off. For initial `x_0>0,y_0<0`, (3) gives such a pair except when `x_N=0`; that equality is a threshold-null event for continuous marks. For initial `x_0<0,y_0<0`, the certificate holds at step zero. The finite gate history and either strict terminal certificate persist under sufficiently small perturbations of the initial mark, `z,r,rho`, and `gamma`, provided the perturbed coefficients stay in the displayed strict cones. For a retained finite collection of generic marked atoms, one can take a common perturbation radius and a common finite stopping index (the maximum of their individual indices).

## Sliding occupation and limiting frozen ray

On the captured strip let `theta=c/(c+d) in (0,1)`. Summing the exact normal recurrence gives, for every `E<=k<ell`,

\[
\gamma\sum_{j=k}^{\ell-1}(s_j-\theta)
=-(x_\ell-x_k)/(c+d),\qquad
\left|\gamma\sum_{j=k}^{\ell-1}(s_j-\theta)\right|\le\gamma.
\tag{10}
\]

This is a bounded occupation primitive, not pointwise gate convergence. Also `y_n=eta_0+n gamma*kappa+rho*x_n`, with bounded `x_n` after `E`. For fixed frozen mark and `gamma`, the held or polygonal rescaled path `q_L(t)=L^{-1}v_{floor(Lt/gamma)}` therefore satisfies, uniformly on compact time intervals,

\[
q_L(t)\longrightarrow
\begin{cases}(0,\kappa t),&y_0>0,\\(0,0),&y_0\le0,\end{cases}
\tag{11}
\]

at `O(1/L)` for that fixed mark. The corresponding frozen endpoint output `z(q_L)_+` has support-2 slope `z*kappa=z^2(1-rho^2)r_2` on the sliding branch. This matches the conditional changing-weight Schur action in the previous run's `g01_sliding.md`; (11) itself freezes the weight and residual and is not a network theorem.

## Generic thresholds, mirror sign, and limits of transfer

For fixed `(z,r,gamma,rho)` and any finite gate history, `v_n=Xu+constant`. Thus either coordinate equality at any integer step is an affine hyperplane in the original mark `u` (the relevant row of the full-rank input matrix `X` is nonzero). A projected stable mark has a density, so the countable union over steps and finite histories has probability zero. Under the boundary-grid model's independent marked Poisson process and residual, almost surely every atom avoids every finite-step threshold. On this full-measure set the selector (8) is locally constant in all strict parameters and in the mark. In particular, the threshold `y_0=0`, the only possible change of selector within this double cone, is null. This facilitates finite-cutoff boundary-grid transfer, but a bound uniform as the number of steps grows or as infinitely many small atoms are restored requires separate network estimates.

For `z<0` under the same residual cone, swap coordinates 1 and 2 and replace the normal/support labels accordingly. The support is now coordinate 1, with selector `sliding` exactly when `x_0>0` and `dead` when `x_0<=0`; the support-1 output slope is `z^2(1-rho^2)r_1` (negative because `r_1<0`). The coordinate-1 support increases as a projection, but the output `z(x)_+` decreases. This mirrored statement uses the same strict-gate convention and is likewise independent of `gamma`.

**Scope:** The proof gives exact frozen finite-step entrance, open certificates, and a short-time path for any retained endpoint while the residual stays in the indicated coefficient cone. It neither extends the already-proved fixed finite-grid theorem to `O(L)` network steps nor resolves a transition after the evolving residual leaves that cone. In particular, the positive-correlation double cone has a simple mark selector, while subsequent release/recapture can still require the reflected-integral dynamics of `REFLECTION_SELECTOR.md`.

`../code/h01_entrance_check.py` uses only exact `Fraction` arithmetic. Its actual executed output is `../outputs/h01_entrance_check.txt`: 3,362 double-cone rational mark/step cases passed the finite death/certificate and occupation identities; the same script checks an exact reflected release/recapture path against its Schur/full-`G` output segments, and another 3,362 cases of the broader all-mixed classifier.
