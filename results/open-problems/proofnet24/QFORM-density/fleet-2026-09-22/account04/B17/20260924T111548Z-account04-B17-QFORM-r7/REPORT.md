SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B17, 2026-09-24T11:15:48Z.
attacking: three-macro non-collinear compensated witness; exact spectrum and symbolic cone-tip coefficient.

# QFORM-THREEMACRO-NONCOLLINEAR-RIGIDITY-v1

Status: **ESSENTIAL_STEP_APPLIED; the full conjecture remains open.**

## Result

Let
\[
J=\operatorname{diag}(1,1,-1),
\]
and choose
\[
v_1=e_3,\qquad
v_2=\frac{e_1+e_3}{\sqrt2},\qquad
v_3=\frac{e_2+e_3}{\sqrt2}.
\tag{1}
\]
Give each direction compensated macroscopic weight \(\alpha_j=1/3\). The completed account01/B17 theorem QFORM-MULTIMACRO-SECONDORDER-RIGIDITY-v1, source-pinned at math-open-problems commit fe1dbd3c9532e3ffdd75fcce2af6e550d8f1d585, states that for
\[
Y_q=G_q+\sqrt{\frac q3}\sum_{j=1}^3v_jU_j,
\qquad
G_q\sim N\!\left(0,\frac{I-H_q}{12}\right),
\qquad
H_q=\frac q3\sum_{j=1}^3v_jv_j^\top,
\tag{2}
\]
with independent \(U_j\sim\operatorname{Unif}[-1/2,1/2]\),
\[
\frac{p_{Y_q^\top JY_q}(0)}{3\sqrt2}
=
1-\frac{3q^2}{80}\sum_{j=1}^3\alpha_j^2F(t_j)+O(q^3),
\quad
F(t)=\frac{19+2t-13t^2}{8},
\quad
t_j=(v_j\cdot e_3)^2.
\tag{3}
\]

For (1),
\[
t_1=1,\qquad t_2=t_3=\frac12,
\qquad
F(1)=1,\qquad F(1/2)=\frac{67}{32}.
\]
Therefore
\[
\sum_{j=1}^3\alpha_j^2F(t_j)
=
\frac19\left(1+2\frac{67}{32}\right)
=
\frac{83}{144},
\]
and
\[
\boxed{
\frac{p_{Y_q^\top JY_q}(0)}{3\sqrt2}
=
1-\frac{83}{3840}q^2+O(q^3).
}
\tag{4}
\]

Three equal collinear minority-axis macro rows have coefficient \(1/80=48/3840\). Thus forcing this three-direction hybrid geometry incurs the strict symbolic penalty
\[
\boxed{
\frac{83}{3840}-\frac1{80}=\frac7{768}.
}
\tag{5}
\]
So splitting fixed compensated macroscopic variance among these three non-collinear shared directions cannot overshoot the \(3\sqrt2\) cone-tip at the first nonvanishing order.

## Exact finite target realization

Let
\[
V=\frac12
\begin{pmatrix}
1&1&1\\
1&-1&1\\
1&1&-1\\
1&-1&-1
\end{pmatrix},
\qquad V^\top V=I_3,
\tag{6}
\]
and put \(S_q=(I-H_q)^{1/2}\). For every \(m\ge2\), define a \((4m+3)\times3\) synthesis matrix \(R_{m,q}\) whose first three rows are
\[
\sqrt{\frac q3}v_1^\top,\quad
\sqrt{\frac q3}v_2^\top,\quad
\sqrt{\frac q3}v_3^\top,
\]
and whose remaining rows are \(m\) copies of each row of \(VS_q/\sqrt m\). Then
\[
R_{m,q}^\top R_{m,q}=H_q+S_q^2=I_3.
\tag{7}
\]
Consequently
\[
A_{m,q}=R_{m,q}JR_{m,q}^\top
\tag{8}
\]
has exact nonzero spectrum
\[
\boxed{\operatorname{spec}_{\ne0}(A_{m,q})=\{1,1,-1\}}
\tag{9}
\]
for every finite \(m\) and every \(q\) with \(I-H_q>0\).

Take all \(4m+3\) original coordinates independently uniform on \([-1/2,1/2]\). These laws are normalized and have density exactly one on their supports. For fixed sufficiently small \(q>0\), \(R_{m,q}^\top X\) converges to (2). The macro leverages are \(q/3\), and every diffuse leverage is at most \(3/(4m)\). For \(q\le1\) and \(m\ge2\), all are at most \(1/2\). Claude's completed Fresnel--Brascamp--Lieb estimate at math-open-problems commit e5f71d79eff325201dd0274053d20268ce65b837 gives a common integrable characteristic-function majorant. Fourier inversion yields
\[
\|p_{X^\top A_{m,q}X}-p_{Y_q^\top JY_q}\|_\infty\longrightarrow0
\quad(m\to\infty)
\tag{10}
\]
for fixed \(q\).

Combining (4) and (10), for every \(\eta>0\) one can choose \(q>0\) and then finite \(m\) so that
\[
\boxed{
\|p_{X^\top A_{m,q}X}\|_\infty
\ge p_{X^\top A_{m,q}X}(0)>3\sqrt2-\eta.
}
\tag{11}
\]
Thus \(C_{\rm univ}\ge3\sqrt2\) survives an exact finite, genuinely three-direction hybrid macro geometry. This certificate is analytic, not histogram-based.

## Scope

This does not disprove the conjecture and does not raise the known lower obstruction above \(3\sqrt2\). It excludes one plausible overshoot mechanism to second order and supplies an exact-spectrum stress family. Fixed positive macro leverage away from \(q\downarrow0\), and the full shared-bank convex/two-sheet endpoint, remain open.
