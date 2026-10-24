# R15 idea note w108e — coarse K gate and small-scale interior exclusion route

Status: **PENDING / SELF_CHECK_ONLY / NOT CLAIMED** retained F0111 screening. This does not reopen Burdzy–Scheutzow Problem 7.2 / I0076.

Immediate predecessor: `runs/R15/20260920_1316Z_successor_screen_f0111_boundary_curve_v107d.md`.

Methods for this run: **#6 DEFORM TO A POINT YOU CAN SOLVE, #19 MAKE IT AN ALGORITHM, #25 COUNT THE SAME THING TWICE.** The preceding completed report used #7/#12/#29.

This note is deliberately committed before any new validation code.

## 1. Pivot away from the false monotonicity target

The predecessor suggested trying to prove monotonicity in `delta` of the exact two-variable necessary gate

\[
\widehat\Gamma_N=\log S-\left(1+\frac\eta2\right)K_{\rm sec}-H_J^*,\qquad N\in\{12,13\}.
\]

Private route-finding calculations show that a global `partial_delta widehatGamma_N >= 0` statement is not the right invariant: the derivative can turn slightly negative near the opposite scalar boundary even while the gap remains positive. This scratch observation is not evidence and is not promoted to a theorem. The new route is to replace the K term by a slightly coarser but much more algebraic majorant and then attack a genuine endpoint/concavity problem.

## 2. A coarser necessary gate with no logarithm of the K cap

Write

\[
D=S^{-1}=-k/29,\qquad \eta=U_K-N,\qquad c_K=U_K/L_K.
\]

The previous theorem gives

\[
K_{\rm sec}=\eta D\,\frac{c_K\log c_K}{c_K-1}.
\]

For `c_K>=1`, `log c_K <= c_K-1`, hence

\[
\frac{c_K\log c_K}{c_K-1}\le c_K.
\]

Therefore every survivor of the retained screen must satisfy the **coarse gate**

\[
\boxed{
\overline\Gamma_N(d,s)
:=\log S-H_J^*(d,s)-\left(1+\frac\eta2\right)\eta D c_K\le0.
}
\]

Indeed `widehatGamma_N >= overlineGamma_N`, so proving `overlineGamma_N>0` is enough for a contradiction. The gain is that the last K term is now rational apart from the logs already present in the adaptive J ray.

For this run use the adaptive constant

\[
c=3/100,\qquad \varepsilon=c/\log S,\qquad t=1+\varepsilon,
\]

which is allowed by the earlier adaptive-ray monotonicity proof because that proof was certified at `c=7/100` and only improves when `c` decreases.

## 3. Exact double-counting identity

With `C_12=15`, `C_13=17`, `M=30-N`, define the scaled two-heavy variables

\[
A=1-C_Ns,
\qquad
D=1/S,
\qquad
B=x-1+C_Ns-(M-2)D.
\]

Then `u_1=SA`, `u_2=SB`. The carried exact identities

\[
x=1-k-y,\qquad y=U_KD,\qquad -k=29D
\]

give

\[
\begin{aligned}
A+B-D
&=x-(M-1)D\\
&=1+29D-U_KD-(29-N)D\\
&=1-(U_K-N)D.
\end{aligned}
\]

Thus

\[
\boxed{A+B-D=1-\eta D.}
\]

This is the conserved mass defect that was hidden when the J and K estimates were written separately.

Writing

\[
F=A^t+B^t-D^t,
\qquad q_1=\log(SA),\qquad q_2=\log(SB),
\]

the coarse gap has the stable cancellation form

\[
\boxed{
\overline\Gamma_N
=-\frac1t\log F-\varepsilon U_{\max}q_1q_2
-\left(1+\frac\eta2\right)\eta D c_K.
}
\]

No large `log S` terms are subtracted numerically.

## 4. Small-scale attack, uniformly over the full interiors

Target first the entire interior strip

\[
0<s\le 10^{-4}.
\]

From the exact formula for `x`, direct simplification gives

\[
\frac{x-1}{s}
=
\frac{d^2+3ds+4d+2s^2+9s+7}
{2(d+1)(d+3s+3)}.
\]

On the carried outer cells

\[
N=12:\quad d>49/100-s/4,
\qquad
N=13:\quad d>53/100-s/5,
\]
this will imply `(x-1)/s<9/10` by a one-line rational sign check.

Also `U_K` is increasing in both scalar variables. The upper cell walls imply

\[
N=12:\quad \eta<1/4,
\qquad
N=13:\quad \eta<1/4
\]
for `s<=10^{-4}`. The carried monotonicity of `L_K`, together with `L_K(d,0)=6/(1-d)`, then gives

\[
c_K<21/20
\]
in both cells.

The two-heavy smaller coordinate satisfies

\[
u_2<S(x-1+C_Ns)<20(C_N+9/10),
\]
using the carried `S<20/s`. Hence the planned exact exponential checks are

\[
q_2<29/5\quad(N=12),
\qquad q_2<59/10\quad(N=13).
\]

Finally the carried `S>232/(13s)` gives `L=log S>12`, hence `eps<1/400` and `t<401/400`.

## 5. Entropy lower bound for the coarse gap

Because `D^t=De^{-c}` exactly and `e^u<=1+u+u^2/2` for `u<=0`, let

\[
\mathcal E=-A\log A-B\log B+D\log D,
\qquad
\mathcal V=A\log^2A+B\log^2B.
\]

The identity `A+B-D=1-eta D` gives

\[
1-F\ge \eta D+\varepsilon\mathcal E
-\frac{\varepsilon^2}{2}\mathcal V
+D(c-1+e^{-c}).
\]

The last term is nonnegative. Moreover

\[
\mathcal E=-A\log A+(C_Ns-\eta D)\log S-Bq_2.
\]

Therefore, whenever the right side forces `F<1`, `-log F>=1-F` yields

\[
\begin{aligned}
t\overline\Gamma_N
\ge{}&
\varepsilon\left(\mathcal E-\frac\varepsilon2\mathcal V-tU_{\max}q_1q_2\right)\\
&+\eta D\left[1-t\left(1+\frac\eta2\right)c_K\right].
\end{aligned}
\]

The carried bounds `Umax<(9/8)s` and `-k/s<13/8` now make every negative term linear in `s` with an explicit rational coefficient. The intended checker will validate only these finite rational comparisons and Taylor lower bounds for `exp(29/5)` and `exp(59/10)`. If the resulting margins are positive, this will exclude **the full N=12 and N=13 interiors for every `0<s<=10^{-4}`**, not merely the lower scalar boundary.

## 6. Route after the small-scale theorem

For `s>=10^{-4}`, private route-finding suggests the coarse gap is concave in `d` on each exact scalar cell. If that can be certified, its minimum is at one of the two scalar boundaries. The lower boundary `U_K=N` is already excluded exactly by v107d. The remaining finite task would be the opposite `L_K=N` boundary plus a concavity certificate. This is only the next route; it is not claimed here.
