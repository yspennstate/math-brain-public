# T384 nonorthogonal Euler boundary: an exact frozen-residual sliding calculation

**Status.** The statements below are deterministic theorems for one frozen output-weight endpoint and a *fixed residual* while the second gate stays positive. They identify a real obstruction to identifying a macroscopic network kernel by averaging its pre-step tangent matrix. They are not a finite-width or full-network convergence theorem. The derivation is analytic; a separate exact-rational check is in `../code/e03_chatter_check.py`, with its executed stdout in `../outputs/e03_chatter_check.txt`.

## Model and sliding cone

Let

\[
G=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},\qquad |\rho|<1,\qquad
v_{n+1}=v_n+\gamma zG D(v_n)r,
\qquad D(v)=\operatorname{diag}(1_{v_1>0},1_{v_2>0}),
\]

where `gamma>0`, `z ne 0`, and `r=(r1,r2)` does not change with `n`. Write `x=v1`, `y=v2`, `A=z r1`, `B=z r2`, and suppose `y_n>0` throughout the interval under discussion. Assume the attracting sliding inequalities

\[
c:=\rho B>0,\qquad d:=-A-\rho B>0.
\tag{1}
\]

Thus `A=-(c+d)`, the off-side normal drift is `+c`, and the on-side normal drift is `-d`. The exact recurrence is

\[
x_{n+1}=x_n+\gamma c-\gamma(c+d)s_n,
\qquad
y_{n+1}=y_n+\gamma B+\gamma\rho A s_n,
\qquad s_n=1_{x_n>0}.
\tag{2}
\]

The requested instance `rho=1/2,z=1,r=(-1,1)` has `c=d=1/2`. Condition (1) is equivalently `0<rho B<-A`; in this notation `theta=c/(c+d)=-rho B/A` lies strictly between zero and one.

## Exact occupation and output bounds

The strip

\[
I_\gamma=(-\gamma d,\gamma c]
\tag{3}
\]

is invariant under (2). If `x_n<=0`, then `x_{n+1}=x_n+gamma c`; if `x_n>0`, then `x_{n+1}=x_n-gamma d`, which verifies both ends of (3). Any finite initial `x0` enters it after finitely many steps. Summing the first equation in (2), for any `k<l` whose endpoints are in the strip,

\[
\sum_{n=k}^{l-1}(s_n-\theta)
=-\frac{x_l-x_k}{\gamma(c+d)},
\qquad
\left|\sum_{n=k}^{l-1}(s_n-\theta)\right|<1.
\tag{4}
\]

The strict bound follows from the strip width `gamma(c+d)`. In particular the fraction of on steps among `N` consecutive steps differs from `theta` by less than `1/N`, independent of rationality or phase. The much stronger tangential identity follows by eliminating `s_n` **before** taking a limit:

\[
y_n-\rho x_n=y_0-\rho x_0+\gamma B(1-\rho^2)n.
\tag{5}
\]

For `x0=0`, all iterates lie in (3), so with `M=max(c,d)`

\[
|x_n|\le\gamma M,
\qquad
|y_n-y_0-\gamma B(1-\rho^2)n|\le |\rho|\gamma M.
\tag{6}
\]

These bounds also hold between grid points for polygonal interpolation, with `n gamma` replaced by continuous boundary time `t`, because the left side of (5) advances by the same constant amount in each step. Hence from `x0=0` the vanishing-step limit is the sliding path

\[
x(t)=0,\qquad y(t)=y_0+B(1-\rho^2)t,
\tag{7}
\]

uniformly on every interval on which the second gate remains positive. The gate convention at exactly `x=0` is `s=0`; it changes the microscopic orbit but not (4)--(7).

There is also a global error bound for an arbitrary fixed `x0`. Define the continuous sliding candidate `x_*(t)` to move toward zero at speed `d` from positive `x0` or speed `c` from negative `x0`, then remain zero. Put

\[
y_*(t)=y_0+\rho[x_*(t)-x_0]+B(1-\rho^2)t.
\]

Before its first crossing the Euler polygonal path agrees exactly with the linear part of `x_*`; after crossing it lies in (3). Consequently, as long as the `y>0` sector is valid,

\[
\sup_{t\ge0}|x_\gamma(t)-x_*(t)|\le \gamma M,
\qquad
\sup_{t\ge0}|y_\gamma(t)-y_*(t)|\le |\rho|\gamma M.
\tag{8}
\]

For a fixed horizon `T`, a sufficient condition for sector validity at small steps is `inf_{[0,T]} y_*(t)>0`; (8) then makes the discrete `y` positive for all sufficiently small `gamma`. For the requested `rho=1/2,B=1,x0=0`, `y0>0` and (6) suffice for every finite horizon once `gamma<4y0` (the bound `|rho|gamma M=gamma/4`).

The frozen endpoint's scaled output is `p_n=z((x_n)_+,y_n)` while `y_n>0`. Starting at `x0=0`, (6) gives the exact output-error bound

\[
\left|p_n-\bigl(0,z[y_0+B(1-\rho^2)n\gamma]\bigr)\right|_2
\le |z|\gamma M\sqrt{1+\rho^2}.
\tag{9}
\]

Thus the constrained output law along the sliding cone has velocity

\[
\dot p=\begin{pmatrix}0\\z^2(1-\rho^2)r_2\end{pmatrix}
=z^2\begin{pmatrix}0&0\\0&1-\rho^2\end{pmatrix}r.
\tag{10}
\]

The matrix in (10) is the Schur-complement *representation of this constrained vector field*. It is not a pointwise or `L1` limit of the tangent kernel, nor necessarily the Cesaro limit of a secant matrix. Its derivation uses the sliding relation `theta=-rho B/A`, so it cannot be extended as a linear response to arbitrary residual perturbations without checking that the perturbed path remains in the cone.

There is one useful conditional extension with a changing residual but still a frozen `z`. Let `A_n=z r1,n`, `B_n=z r2,n`, `c_n=rho B_n`, and `d_n=-A_n-c_n`. Suppose throughout an interval that `0<c_n<=C_*`, `0<d_n<=D_*`, and `y_n>0`. Then `[-gamma D_*,gamma C_*]` is invariant for `x_n`, by the same one-step check as (3). More importantly, without any slow-variation assumption,

\[
y_N-\rho x_N=y_0-\rho x_0+\gamma z(1-\rho^2)\sum_{n<N}r_{2,n}.
\tag{10a}
\]

If `x0=0`, the endpoint output therefore differs from `(0,z y0+gamma z^2(1-rho^2)sum_{n<N}r2,n)` by at most `|z|gamma max(C_*,D_*)sqrt(1+rho^2)` in Euclidean norm. This is a conditional discrete sliding estimate, not a network result: actual output weights change, and it remains necessary to prove that a network endpoint enters and stays in such a cone with the second gate positive.

## Secant matrix versus the pre-step tangent matrix

Let `Delta v_n=v_{n+1}-v_n`, and define the exact fraction of the line segment with the first gate active by

\[
\lambda_n=\int_0^1 1_{x_n+t\Delta x_n>0}\,dt.
\]

Assuming the second coordinate remains positive along the segment, the ReLU secant identity is

\[
p_{n+1}-p_n=\gamma K_n^{\rm sec}r,
\qquad
K_n^{\rm sec}=z^2\operatorname{diag}(\lambda_n,1)
 G\operatorname{diag}(s_n,1)
=z^2\begin{pmatrix}s_n\lambda_n&\rho\lambda_n\\
\rho s_n&1\end{pmatrix}.
\tag{11}
\]

For an on step, `lambda_n=min(1,x_n/(gamma d))`. For an off step, `lambda_n=max(0,(x_n+gamma c)/(gamma c))`. Endpoints of the segment have zero measure, so these formulas include exact landings at zero. In contrast, the pre-step tangent contribution is

\[
K_n^{\rm pre}=z^2 D(v_n)G D(v_n)
=z^2\begin{pmatrix}s_n&\rho s_n\\\rho s_n&1\end{pmatrix}.
\tag{12}
\]

For each `N`, let `phi_N=N^{-1}sum_{n<N}lambda_n`. Since `x_{n+1,+}-x_{n,+}=gamma(c+A s_n)lambda_n`, the boundedness of `x_+` and (4) give, when `x0` is in (3),

\[
\frac1N\sum_{n<N}s_n\lambda_n
=\theta\phi_N+O(N^{-1}),
\qquad
\frac1N\sum_{n<N} s_n=\theta+O(N^{-1}).
\tag{13}
\]

The first error has absolute value at most `c/[N(c+d)]` when `x0=0`, because then `0<=x_N^+<=gamma c`; the second has absolute value less than `1/N`. Consequently, if `phi_N->phi`,

\[
\frac1N\sum_{n<N}K_n^{\rm sec}
\longrightarrow z^2\begin{pmatrix}\theta\phi&\rho\phi\\\rho\theta&1\end{pmatrix},
\qquad
\frac1N\sum_{n<N}K_n^{\rm pre}
\longrightarrow z^2\begin{pmatrix}\theta&\rho\theta\\\rho\theta&1\end{pmatrix}.
\tag{14}
\]

The secant average can be nonsymmetric and phase-dependent. Its product with **the particular fixed residual** is phase-independent:

\[
z^2\begin{pmatrix}\theta\phi&\rho\phi\\\rho\theta&1\end{pmatrix}r
=\begin{pmatrix}0\\z^2(1-\rho^2)r_2\end{pmatrix}.
\tag{15}
\]

The pre-step average in (14), when multiplied by the same `r`, predicts the wrong first-coordinate velocity, namely `z theta(A+rho B)=-z theta d`. The missing positive output on an **off-to-on** Euler step is precisely the post-step ReLU secant correction. Averaging `DGD` is therefore not the same operation as averaging `D(v_n+t Delta v_n)G D(v_n)`. Nor can one identify the effective matrix merely by replacing both `D` factors with their average: `diag(theta,1)Gdiag(theta,1)` has the correct product with this `r`, but need not equal the actual secant average because `phi` need not equal `theta`.

The existence and phase dependence of `phi` have a simple dynamical description. On the interval (3), `t_n=x_n/gamma+d` takes values on the circle of length `c+d`, and (2) is rotation by `c` (with the representative `c+d` used for zero). If `c/(c+d)` is rational, every orbit is periodic, so `phi` is its finite-cycle average and may depend on the initial phase. If it is irrational, equidistribution of circle rotations applied to the piecewise continuous function `lambda` gives

\[
\phi=
\begin{cases}
c/(2d),&c\le d,\\
1-d/(2c),&c\ge d.
\end{cases}
\tag{16}
\]

The two formulas agree at `c=d`. For example, when `c=d=1/2`, `x0=0`, and any `gamma>0`, the exact cycle is `x=0,gamma/2,0,...`, with `(s,lambda)=(0,1),(1,1),...`; hence `theta=1/2`, `phi=1`. In the requested `z=1,r=(-1,1),rho=1/2` case, the two-cycle averages are

\[
\overline K^{\rm sec}=
\begin{pmatrix}1/2&1/2\\1/4&1\end{pmatrix},
\qquad
\overline K^{\rm pre}=
\begin{pmatrix}1/2&1/4\\1/4&1\end{pmatrix},
\qquad
\overline K^{\rm sec}r=(0,3/4),\quad
\overline K^{\rm pre}r=(-1/4,3/4).
\tag{17}
\]

Starting instead at `x0=gamma/4` gives the cycle `gamma/4,-gamma/4,...` and `lambda=1/2` on both steps. Then `phi=1/2` and the secant average is `[[1/4,1/4],[1/4,1]]`, still with product `(0,3/4)`. Both families of initial conditions tend to the same boundary point as `gamma->0`; the matrix limit retains their phases.

## What kind of kernel convergence is available?

For the frozen toy and `x0` in (3), the held pre-step matrix (12) has a weak time average with a **uniform primitive error**. For any complete grid interval `[k gamma,l gamma]`, (4) gives

\[
\left\|\gamma\sum_{n=k}^{l-1}
 \left(K_n^{\rm pre}-z^2\begin{pmatrix}\theta&\rho\theta\\\rho\theta&1\end{pmatrix}\right)\right\|
\le \gamma z^2\left\|\begin{pmatrix}1&\rho\\\rho&0\end{pmatrix}\right\|.
\tag{18}
\]

This yields convergence of the time primitives as `gamma->0` and hence weak temporal convergence. It does **not** give `L1` convergence of the pre-step matrix path to its average. Indeed, for any fixed `T>0`,

\[
\int_0^T |(K_{\lfloor t/\gamma\rfloor}^{\rm pre})_{11}-z^2\theta|\,dt
\longrightarrow 2z^2\theta(1-\theta)T>0.
\tag{19}
\]

Thus a macroscopic nonorthogonal network theorem with sliding cannot simply inherit the orthonormal proof's `L1` tangent-kernel compactness and irreversible gate populations. The full network has changing residuals, changing weights, multiple coupled gates, and a finite-width selection problem; (4)--(19) neither prove its sliding regime nor a global effective kernel law. Fixed `gamma` can retain a grid phase as in (17), while `gamma->0` removes the path error in (8)--(10) but not the secant-matrix phase. One must specify whether the desired limit concerns output, a secant response, pre-step tangent kernels, or a weak time-integrated kernel.
