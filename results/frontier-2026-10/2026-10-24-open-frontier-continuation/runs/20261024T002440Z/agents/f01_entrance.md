# T384: exact finite-step entrance selector in a nonorthogonal cone

**Status.** Proved deterministic theorem for one endpoint with frozen residual and fixed Euler multiplier `gamma`. It identifies a genuine finite-step versus Filippov entrance discrepancy, on open sets of marks and residuals. The marked-PPP implication is conditional on this frozen endpoint model and supports the already-proved finite boundary grid. It is **not** a long-time theorem for the actual residual-coupled network, nor a full T384 or novelty claim. Exact-rational executable checks are in `../code/f01_entrance_check.py`, with executed output in `../outputs/f01_entrance_check.txt`.

## Complete selector for the cone

Take `G=[[1,rho],[rho,1]]`, `-1<rho<0`, `z != 0`, and a constant residual `r` such that `A=z r1<0<B=z r2`. Write `a=-A>0`, `b=B>0`, `k=-rho in (0,1)`, and `v_n=(x_n,y_n)`. Use the actual strict pre-step gates in

\[
v_{n+1}=v_n+\gamma G(A1_{x_n>0},B1_{y_n>0})^T. \tag{1}
\]

The four step velocities (before multiplying by `gamma`) are

| Sector | `--` | `+-` | `-+` | `++` |
|---|---:|---:|---:|---:|
| velocity | `(0,0)` | `(-a,ka)` | `(-kb,b)` | `(-(a+kb),ka+b)` |

Consequently, every nonzero step strictly decreases `x` and strictly increases `y`. Once the path enters `--` it stays there, and once it enters `-+` it stays there. Every path with `x>0,y>0` reaches `-+` in finitely many steps; the same holds for `x<=0,y>0`. The only choice is an initial `x>0,y<=0` mark. Put

\[
N_x=\left\lceil\frac{x}{\gamma a}\right\rceil,
\qquad H_\gamma(x,y)=y+\gamma k a N_x. \tag{2}
\]

Then the **exact all-mark selector**, including equality under the strict-gate convention, is

\[
P_\gamma(x,y)=
\begin{cases}
(-kb,b),&x\le0,\ y>0,\\
(-kb,b),&x>0,\ y>0,\\
(-kb,b),&x>0,\ y\le0,\ H_\gamma(x,y)>0,\\
(0,0),&\text{otherwise}.
\end{cases} \tag{3}
\]

Here `P_gamma` is the eventual **velocity per unit boundary time**: if the orbit escapes, `v_n=c+n gamma(-kb,b)` for all sufficiently large `n`; if it dies, `v_n` is eventually constant. To prove (3), while in `+-` one has `(x_n,y_n)=(x-n gamma a,y+n gamma ka)`. If that velocity continued, the first `x<=0` step would be `N_x`. If `H_gamma<=0`, no earlier `y>0` step occurred, and that step enters `--`. If `H_gamma>0`, `y` becomes positive at or before that step. An earlier positive `y` gives `++`, which must reach `-+`; a simultaneous positive `y` gives `-+` immediately. This argument also covers exact grid landings at `x=0` or `y=0`.

The finite transient itself is explicit. From `++`, the first `x<=0` step is `ceil(x/[gamma(a+kb)])`. From `+-`, the first `y>0` step under its initial velocity is `N_y=floor((-y)/(gamma ka))+1`; when `N_y<N_x`, it arrives in `++` at `(x-N_y gamma a,y+N_y gamma ka)` and then uses the preceding `++` count. When `N_y=N_x`, it enters `-+` directly; when `N_y>N_x`, it enters `--`. All later steps use the stationary or `-+` velocity above.

For fixed `gamma`, mark, and cone parameters, the transient has finitely many steps. Thus, with `q_L(t)=L^{-1}v_{floor(Lt/gamma)}`,

\[
\sup_{0\le t\le T}\|q_L(t)-tP_\gamma(x,y)\|\le C(\gamma,x,y,A,B,\rho)/L \tag{4}
\]

for every fixed `T`; the same holds for polygonal interpolation. The eventual frozen endpoint output contribution has velocity `z(P_gamma)_+`, namely `(0,z b)=(0,z^2r_2)` in the escape case, and zero in the dead case. This is a single-endpoint statement, not a network output equation.

## Exact step-size thresholds and the continuous selector

For an interior `+-` mark put `t_x=x/a` and `t_y=(-y)/(ka)`. Equation (3) is equivalently

\[
\gamma\left\lceil t_x/\gamma\right\rceil>t_y. \tag{5}
\]

For `n>=2`, the set of step sizes with `N_x=n` is `[t_x/n,t_x/(n-1))`; for `n=1`, it is `[t_x, infinity)`. Intersecting with `gamma>t_y/n` gives the exact escape intervals. In particular, when `t_y>t_x` (the continuous path dies), interval `n` is nonempty precisely when

\[
n<\frac{t_y}{t_y-t_x}, \tag{6}
\]

so only finitely many, possibly disconnected, step-size intervals produce escape. The selector need not be monotone in `gamma`.

The continuous `+-` path reaches `x=0` at time `t_x` with height `y+kx`. Excluding the origin-hit equality, the Filippov selector escapes iff `y+kx>0` and dies iff `y+kx<0`. Let `delta_gamma=gamma a ceil(x/(gamma a))-x in [0,gamma a)`. The discrete condition is

\[
y+kx+k\,\delta_\gamma>0. \tag{7}
\]

Therefore every continuously escaping interior mark escapes discretely, but the discrete scheme also escapes from the open overshoot band

\[
-k\,\delta_\gamma<y+kx<0. \tag{8}
\]

For fixed `gamma>0` this band has positive area in every full `x` grid cell: at `x in ((n-1)gamma a,n gamma a)`, its `y`-width is `k(n gamma a-x)`. It shrinks locally as `gamma->0`. This cone has no sliding: at each reachable positive face the adjacent velocities cross the face in the same direction. The mismatch is entirely a finite Euler overshoot at the corner.

## Requested exact instance and robust neighborhoods

Set `rho=-1/2`, `z=1`, `r=(-1,1)`, and `(x,y)=(.14,-.12)`. Then `a=b=1`, `k=1/2`, `t_x=.14`, `t_y=.24`, and the continuous path hits `x=0` at `y=-.05`, so it dies. At `gamma=1`, the first step is `(-.86,.38)` and the orbit follows the escape ray `(-.5,1)`. At `gamma=.1`, the first two steps are `(.04,-.07)`, `(-.06,-.02)`, so it dies. Equation (6) gives **all** escaping step sizes for this mark: `gamma in (.24,infinity) union (.12,.14)`. Thus `gamma=.13` escapes, while `gamma=.14` dies by landing exactly at `(0,-.05)`.

This is not an equality artifact at the two requested multipliers. Let the projected mark lie in

\[
M=(.13,.15)\times(-.13,-.11),
\]

and let `A in (-1.02,-.98)`, `B in (.98,1.02)`, `rho in (-.51,-.49)`. At `gamma=1`, uniformly over this box, `x_1<-.83` and `y_1>.3502`; every orbit escapes. At `gamma=.1`, uniformly, `x_1>.028`, `y_1<-.05798`, `x_2<-.046`, and `y_2<-.00596`; every orbit dies. These strict bounds also allow small variations of either multiplier. The exact-rational script checked the central trajectories, these interval bounds, and the formula against 25,000 direct sector iterations.

## Marked stable-PPP consequence and its limit

In the previous run's boundary-grid model, `N(dz,du)` has intensity `alpha c |z|^{-1-alpha} dz P_U(du)` and the frozen boundary residual `r=y-F` is independent of `N`. For a concrete Gram matrix with `rho=-1/2`, choose unit inputs `x1=(1,0)`, `x2=(-1/2,sqrt(3)/2)`. The projected mark `Xu=(U1,-U1/2+sqrt(3)U2/2)` has a strictly positive density, hence `P(XU in M)>0`. Choose `z in I=(.995,1.005)` and `r1 in (-1.005,-.995)`, `r2 in (.995,1.005)`; then `A` and `B` lie in the robust box above. The residual event has positive probability for arbitrary fixed labels because `F` has full support (here its two coordinates contain independent nondegenerate symmetric stable terms). The number of atoms in the selected mark set is Poisson with mean

\[
\lambda=c\bigl(.995^{-\alpha}-1.005^{-\alpha}\bigr)P(XU\in M)>0. \tag{9}
\]

By independence, the event that `r` lies in the displayed neighborhood and at least one such atom exists has strictly positive probability. On it, **the same marked atom** has the escape ray for frozen `gamma=1` and the dead ray for frozen `gamma=.1`; also its first one or two boundary-grid iterates have the displayed robust gate patterns. The finite-grid convergence theorem in `BOUNDARY_GRID.md` transfers those finite-step patterns to actual simultaneous GD in its stated fixed-step boundary limit. It does **not** transfer the eventual frozen rays over `O(L)` evolving-residual steps. The macroscopic selector and residual-coupled uniqueness remain unpaid, as in `MACRO_COMPACTNESS.md`.
