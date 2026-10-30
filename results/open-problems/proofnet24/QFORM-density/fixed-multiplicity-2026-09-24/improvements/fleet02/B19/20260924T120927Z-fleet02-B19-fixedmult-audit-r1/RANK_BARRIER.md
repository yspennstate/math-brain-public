# B19 counterexample note — no-pivot completion rank saturation

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T120927Z-fleet02-B19-fixedmult-audit-r1`  
Baseline manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Status: **exact proof-mechanism obstruction; no lower-multiplicity theorem claimed.**

The baseline completion lemma (manuscript lines 531–584) gives, for a sampled disjoint seed of order `r`,

\[
\operatorname{rank}R\le 3r,
\qquad
\operatorname{rank}R[L,L]\le r.
\]

Neither rank can be universally reduced merely by adding the manuscript's local no-pivot inequalities.

For `r=1`, take

\[
A_0=\begin{pmatrix}
-3&1&-3&-3\\
1&-3&-3&-3\\
-3&-3&10&9\\
-3&-3&9&9
\end{pmatrix},
\qquad S=\{1\},\quad T=\{2\},\quad L=\{3,4\}.
\]

Here `B=A0[S,T]=[1]`. With

\[
P=A_0[:,T]B^{-1}A_0[S,:],
\]

the `L x L` residual is

\[
A_0[L,L]-P[L,L]=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]

Therefore the completion has `E=0`,

\[
D=\operatorname{diag}(0,0,1,0),
\qquad R=A_0-D.
\]

Exact elimination gives

\[
\det A_0=144,
\quad \operatorname{rank}A_0=4,
\quad \operatorname{rank}R=3,
\quad \operatorname{rank}R[L,L]=1,
\quad \operatorname{rank}D=1.
\]

Thus the global/restricted rank pair `(3r,r)` is simultaneously sharp, and `D+R` can have rank `4r` with only `r` diagonal residual directions.

Now scale by

\[
\alpha=1/20000,
\qquad A=\alpha A_0.
\]

The largest physical diagonal is `10 alpha=0.0005<1/100`. The six principal `2 x 2` determinants of `A0` have absolute values at most `39`, hence every principal pair determinant of `A` has absolute value at most

\[
39\alpha^2=9.75\times10^{-8}<1/100.
\]

So `A` lies strictly in the baseline no-pivot class, while the same completion still has `E=0`, global rank `3`, restricted rank `1`, and diagonal rank `1`. Direct sums give the same rank saturation for arbitrary `r` while preserving the no-pivot inequalities after the same sufficiently small scaling.

This does **not** refute a `16`- or `13`-eigenvalue density theorem: after the small scaling the witness does not have unit-size singular values. It does refute the proposed proof shortcut

> local no-pivot inequalities alone force an improvement of `rank R<=3r` or `rank R[L,L]<=r`.

Consequently any threshold reduction below 17 must use information beyond local entry smallness and the present rank bookkeeping. Viable targets are a quantitative conversion of same-index bordered-minor mass into disjoint crossing volume, or a new analytic receiver at order four.
