# R15 idea-before-code note: fixed-ray feasible-corridor attack on the last F0111 cells

Status: **PENDING / SELF_CHECK_ONLY / NOT CLAIMED** retained F0111 screening only. Native Burdzy--Scheutzow Problem 7.2 / I0076 remains **OPEN / PARTIAL / RETIRED-HANDOFF** and is not reopened.

Actual runtime model for this run: **GPT-5.6 Sol; reasoning level UNVERIFIED, not GPT-6 maximum.**

Immediate predecessor: `runs/R15/20260920_1354Z_successor_screen_f0111_smallscale_interiors_w108e.md`.

Section-B moves for this route: **#8 GO THE OTHER WAY AND DISCRETIZE, #20 FIND WHY THE ALGORITHM FAILS, #30 DO ONE SCALE / ONE DIRECTION AT A TIME.** All thirty move numbers already occur somewhere in older R15 history, so these are nonconsecutive reuses on the newly reduced object, not claims of globally unused move numbers.

## Why the previous full-cell interval algorithm failed

The preceding run proved the complete arbitrary-heterogeneity interiors for `0<s=z-1<=10^-4`, but its direct two-dimensional exact `Fraction` interval attempt on the rest of the scalar cells over-refined because it boxed the whole outer `(delta,s)` strips. That loses the decisive fact that a scalar survivor must lie in the thin feasible corridor

\[
U_K(\delta,s)>N\ge L_K(\delta,s),\qquad N\in\{12,13\}.
\]

Both `U_K` and `L_K` are already proved strictly increasing in both variables. Thus, for fixed `s`, if `d_U(s)` solves `U_K=N` and `d_L(s)` solves `L_K=N`, every survivor satisfies

\[
d_U(s)<\delta\le d_L(s),
\]

and both root functions decrease with `s`. On a rational slab `[s_0,s_1]`, the entire feasible set therefore lies in the **one corridor box**

\[
[d_U(s_1),d_L(s_0)]\times[s_0,s_1].
\]

This should remove most interval dependency. Exact dyadic bisection can bracket both roots without floating-point decisions.

## Fixed ray instead of an adaptive ray

The earlier adaptive-ray theorem is valid whenever

\[
t=1+\frac c{\log S},\qquad 0<c\le 7/100.
\]

For the remaining range `s>=10^-4`, choose instead the constant

\[
\varepsilon=1/400,\qquad t=401/400.
\]

Since the carried scalar bound gives `S<20/s<=200000` and `200000<e^{28}`, one has

\[
c_{\rm eff}:=\varepsilon\log S<28/400=7/100.
\]

Thus the already-proved adaptive-ray split monotonicity applies pointwise with `c=c_eff`: the arbitrary `J` distribution is still maximized at the same heavy-cap two-coordinate profile.

For `C_12=15`, `C_13=17`, put

\[
A=1-C_Ns,\qquad D=S^{-1}=-k/29,\qquad \eta=U_K-N.
\]

The two-heavy second coordinate has the exact simplification

\[
B:=x-1+C_Ns-(M-2)D
   =C_Ns+(1-\eta)D,
\]

because `x=1-k-y`, `-k=29D`, `y=U_KD`, and `M=30-N`. Hence

\[
A+B-D=1-\eta D.
\]

This is the fixed-ray mass-defect identity to exploit.

## A stable lower bound with no fractional-power interval evaluation

The carried coarse necessary gap is

\[
\overline\Gamma_N
=-\frac1t\log(A^t+B^t-D^t)
-\varepsilon U_{\max}q_1q_2
-\left(1+\frac\eta2\right)\eta Dc_K,
\]

where

\[
q_1=\log(A/D),\qquad q_2=\log(B/D),\qquad c_K=U_K/L_K.
\]

Every survivor must have `overlineGamma_N<=0`.

For `0<A,B,D<1`, use

\[
e^u\le1+u+u^2/2\quad(u\le0),\qquad e^u\ge1+u,
\]

on the `A,B,D` powers. With

\[
E=-A\log A-B\log B+D\log D,
\qquad
V=A\log^2A+B\log^2B,
\]

we obtain

\[
\boxed{
 t\overline\Gamma_N\ge
 \eta D+\varepsilon E-\frac{\varepsilon^2}{2}V
 -t\varepsilon U_{\max}q_1q_2
 -t\left(1+\frac\eta2\right)\eta Dc_K.
}
\]

This expression contains only rational functions and ordinary logarithms. The logarithms can be enclosed exactly by the atanh series with a rational geometric tail, as in the already archived `v107d` boundary certificate.

The plan is now exact and one-dimensional:

1. split `10^-4<=s<=s_N` into rational slabs;
2. bracket `d_U(s_1)` and `d_L(s_0)` by exact dyadic bisection;
3. evaluate the displayed lower bound with outward rational interval arithmetic on that thin corridor box;
4. subdivide only a slab whose lower bound is nonpositive.

If every slab certifies positive, then `overlineGamma_N>0` throughout both remaining scalar cells for `s>=10^-4`. Combined with the preceding exact small-scale theorem, this would eliminate **all** `N=12,13` full-support two-level Hessian-null exact contacts in dimension 30, with arbitrary within-block heterogeneity. It would still be only a restricted F0111 theorem, not a solution of Talagrand's full discrete Convexity Conjecture.

No numerical scan is evidence for the theorem. Code comes only after this route note.