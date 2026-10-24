# QFORM completion-rank sharpness counterexample — account02/B13

Run: `20260924T132744Z-account02-B13-fixedmult-auto11`  
Source theorem audited: manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

## Claim

The two rank bounds in manuscript Lemma `lem:completion`,

\[
\operatorname{rank}R\le3r,
\qquad
\operatorname{rank}R[L,L]\le r,
\]

are simultaneously sharp for the **same nonsymmetric interpolation completion**, even inside the manuscript's no-`eta`-pivot coefficient chamber. Hence the threshold 17 cannot be reduced merely by replacing either universal rank bound by a smaller one while keeping this completion unchanged.

This is an obstruction to one proof-improvement strategy, not a counterexample to the density theorem and not a proof that 17 is optimal.

## One-block construction (`r=1`)

Fix `0<delta<1/10` and set

\[
A_0=
\begin{pmatrix}
0&\delta&\delta/2\\
\delta&0&\delta/3\\
\delta/2&\delta/3&0
\end{pmatrix}.
\]

Take seed sets `S={1}`, `T={2}`, `L={3}`. Then

\[
B=A_{S,T}=(\delta)
\]

is invertible. Every diagonal entry of `A_0` is zero and every principal `2x2` determinant has modulus in

\[
\{\delta^2,\delta^2/4,\delta^2/9\}<1/100=\eta,
\]

so `A_0` has no manuscript `eta`-pivot.

The interpolation

\[
P=A_{\cdot,T}B^{-1}A_{S,\cdot}
\]

has

\[
P_{33}=\frac{(\delta/3)(\delta/2)}{\delta}=\frac\delta6.
\]

Since `L` is a singleton, the off-diagonal residual `E` on `L x L` is exactly zero. The completion therefore takes

\[
D_{33}=A_{33}-P_{33}=-\frac\delta6,
\qquad D_{11}=D_{22}=0,
\]

and

\[
R=A_0-D=
\begin{pmatrix}
0&\delta&\delta/2\\
\delta&0&\delta/3\\
\delta/2&\delta/3&\delta/6
\end{pmatrix}.
\]

Its determinant is

\[
\det R
=\delta\cdot\frac\delta2\cdot\frac\delta3
=\frac{\delta^3}{6}\ne0.
\]

Hence

\[
\operatorname{rank}R=3=3r,
\qquad
\operatorname{rank}R[L,L]=1=r.
\]

Thus both rank inequalities are equalities simultaneously.

For the concrete manuscript-scale choice `delta=1/100`, the three nonzero principal pair determinants have moduli `1/10000`, `1/40000`, `1/90000`, all strictly below `eta=1/100`.

## Every order `r`

Take the orthogonal/direct sum of `r` copies of `A_0`. In each copy label the three coordinates `(s_a,t_a,l_a)` and choose

\[
S=\{s_1,\dots,s_r\},\quad
T=\{t_1,\dots,t_r\},\quad
L=\{l_1,\dots,l_r\}.
\]

Then

\[
B=A_{S,T}=\delta I_r
\]

is invertible. The interpolation and completion decompose blockwise. There are no off-diagonal `L x L` residuals, so again `E=0`; moreover

\[
R[L,L]=(\delta/6)I_r.
\]

Each `3x3` completion block has determinant `delta^3/6`, so

\[
\boxed{
\operatorname{rank}R=3r,
\qquad
\operatorname{rank}R[L,L]=r.
}
\]

The direct sum still has no `eta`-pivot because cross-block principal pairs have determinant zero and within-block pair determinants are the same `O(delta^2)` quantities above.

## Consequence for threshold reduction

The manuscript's spectral-to-volume contradiction uses two independent counts: the global rank `3r` to force large entries of the diagonal `D`, then the restricted rank `r` to contradict an `(r+1)x(r+1)` strictly diagonally dominant block. The displayed family shows that neither rank number can be universally decreased inside the present completion construction, even after imposing the no-pivot coefficient inequalities.

For the order-five endpoint the bad ratio may occur at `r=4`; the existing count therefore needs

\[
m-3r\ge r+1,
\]

i.e. `m>=17`. A genuine reduction below 17 must change something more substantial: seed selection, the completion itself, the analytic endpoint (for example an order-four receiver), or a different structural mechanism. The example does **not** rule out any such alternative.
