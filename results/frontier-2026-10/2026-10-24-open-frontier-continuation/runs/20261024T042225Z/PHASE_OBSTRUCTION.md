# A prescribed-clock phase obstruction at a positive-time return

**Status.** The deterministic statements and the two rational-grid subsequences below are proved. They concern one row driven by a **prescribed smooth residual**. They are not a construction of, or a limiting law for, the self-consistent simultaneous-GD network. In particular, no random-phase or uniform-phase conclusion follows. The relevant exact last-step invariant and threshold are in `../20261024T032106Z/NEGATIVE_RHO_NEXT.md`; the earlier frozen opposite-sign selector is in `../20261024T002440Z/CONDITIONAL_LAW.md`.

## Left-Euler summation retains an order-one offset

Fix `rho=-a`, `0<a<1`, `z>0`, `gamma>0`, and let `beta=gamma z`. In a prescribed-clock experiment set `r_n=r(nh)` and iterate the strict pre-step projected row map

\[
v_{n+1}=v_n+\beta
\begin{pmatrix}1&-a\\-a&1\end{pmatrix}
\operatorname{diag}(1_{x_n>0},1_{y_n>0})r(nh),
\qquad v_n=(x_n,y_n).
\tag{1}
\]

Suppose the row has remained single-1 through step `n-1`. Its exact invariant is `eta=y_n+a x_n=y_0+a x_0`, and

\[
x_n=x_0+\beta\sum_{k=0}^{n-1}r_1(kh),\qquad y_n=\eta-a x_n.
\tag{2}
\]

For `r_1` of class `C^2` on a fixed compact interval, the left Euler–Maclaurin estimate is uniform over grid nodes therein:

\[
\sum_{k=0}^{n-1}r_1(kh)
=h^{-1}I(nh)+\frac{r_1(0)-r_1(nh)}2+O(h),
\qquad I(t)=\int_0^t r_1(s)\,ds.
\tag{3}
\]

Suppose `I(t)>0` for `0<t<tau`, `I(tau)=0`, and `r_1(tau)<0`. At grid indices with `n-tau/h=O(1)`, (2)–(3) imply

\[
x_n=D-\delta(n-\tau/h)+o(1),\qquad
D=x_0+\frac\beta2\{r_1(0)-r_1(\tau)\},\quad
\delta=-\beta r_1(\tau)>0.
\tag{4}
\]

Thus the crossing is governed by `S_h=tau/h+D/delta`, not merely by the continuous return time `tau/h`. If the fractional part `{S_h}` converges to `p` strictly between zero and one, the first crossing index is `ceil(S_h)` for small `h`, provided the path has remained single-1 and the simple return is its first crossing. At that index,

\[
x_{\rm exit}\longrightarrow-\delta(1-p),\qquad
y_{\rm exit}\longrightarrow\eta+a\delta(1-p).
\tag{5}
\]

For `-a delta<eta<0`, the strict single-2 survival test is therefore

\[
p<1+\frac{\eta}{a\delta},
\tag{6}
\]

away from equality. Equation (6) is a conditional phase formula, not a phase law. Convergence of the scaled incoming path gives `I(t)` but discards both `D` and `{tau/h}`.

## Exact polynomial counterexample

Take `a=1/2`, `beta=1` (equivalently `gamma=z=1`), and the same original mark for every grid:

\[
(x_0,y_0)=(1/4,-3/8),\qquad \eta=y_0+a x_0=-1/4.
\tag{7}
\]

Prescribe the smooth residual for all `t>=0` by

\[
r(t)=(1-2t,1),\qquad I(t)=t-t^2.
\tag{8}
\]

Its first positive return is `tau=1`, with `r_1(tau)=-1` and `r_2(tau)=1`. While the row is single-1, for `L=1/h` exact summation gives

\[
x_n=\frac14+n-\frac{n(n-1)}{L}
=\frac14+L I(n/L)+\frac nL,
\qquad y_n=-\frac14-\frac12x_n.
\tag{9}
\]

The last term `n/L` is **exactly** the Euler correction in (3); it tends to `1` at the return. Here `D=5/4`, `delta=1`, and `S_h=L+5/4`. Choose either rational grid family `L=N` or `L=N+1/2`, with integer `N>=3`. In both families (9) gives `x_n>0` for every `0<=n<=N+1`: as a function of real `n`, (9) is concave, and both endpoint values on `[0,N+1]` are positive. Then `y_n=-1/4-x_n/2<0`, so the one-gate formula was valid through all those steps. The first crossing is exactly the step from `N+1` to `N+2`.

| Grid `L` | Incoming `x_{N+1}` | Exiting `x_{N+2}` | Exiting `y_{N+2}` | Strict terminal sector |
|---|---:|---:|---:|---|
| `N` | `1/4` | `-3/4-2/N` | `1/8+1/N` | single-2 |
| `N+1/2` | `3/4+1/(4L)` | `-1/4-3/(4L)` | `-1/8+3/(8L)` | dead (`L>3`) |

For `L=N`, the exiting state has `x<0<y`; every later step uses only gate 2, whose increment is `(-1/2,1)` because `r_2=1`. Thus single-2 persists forever. For `L=N+1/2`, both exiting coordinates are negative; all later increments vanish. Every inequality is strict for `N>=3`. In the phase notation of (5), `{S_h}=1/4` in the first family and `3/4` in the second, while the threshold in (6) is `1/2`.

Both grid families have **the same** prescribed smooth residual, same original mark and one-gate invariant, same local drift at the return, and the same pre-return scaled path:

\[
\frac{v_{\lfloor tL\rfloor}}L
\longrightarrow (I(t),-\tfrac12I(t)),\qquad 0\le t\le1.
\tag{10}
\]

At `t=1` both scaled rows converge to the collapsed corner `(0,0)`. Yet on `t>1` their scaled continuations differ: the `L=N` family tends to `(-(t-1)/2,t-1)`, and the `L=N+1/2` family tends to `(0,0)`. In particular, identical macroscopic **incoming** convergence and an identical return geometry do not determine the post-return selector. The finite frozen entrance formula from time zero cannot be transplanted to this moving return after dropping the original mark and the grid phase.

This phase split is compatible with the usual width clock at the level of deterministic schedules. For any fixed `alpha>0`, set `L_m=(log m)^{1/alpha}`, `h_m=1/L_m`, and choose integers `m_N^{(phi)}` nearest to `exp((N+phi)^alpha)`, for `phi=0,1/2`. Then `L_{m_N^{(phi)}}=N+phi+o(1)`. Since the displayed exit signs have nonzero limits, the same two terminal sectors hold on these width-index subsequences for the **prescribed** recursion. This embedding asserts no actual-network residual path or mark probability.

## Scope of the obstruction

The example proves that a positive-time matching argument needs more than macroscopic residual and row convergence: it must carry the order-one incoming state, the exact one-gate invariant, the Euler correction, and the fractional return phase jointly. It does **not** prove that the actual simultaneous-GD phase has two subsequential laws, is nonuniform, or fails to converge. Actual residuals are coupled to all rows, and their return times may move with width in a way that changes or randomizes the phase. A network theorem must establish that joint moving-time law and a threshold-null property before applying (6), then control selected masses and small atoms.

The exact-Fraction checker `code/phase_obstruction_check.py` and executed output `outputs/phase_obstruction_check.txt` verify the two rational-grid trajectories and all displayed exit signs. The proof above does not depend on floating-point output.
