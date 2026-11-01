# fleet03/B11 r22 — substantive checkpoint

Run `20260923T021243Z-fleet03-B11-QFORM-r22`.

Status: supporting theorem proved below; full QFORM target remains OPEN.

## Minority-sign physical-pivot cone compiler

Let
\[
A=R\Lambda R^T,\quad R^TR=I_3,\quad
\Lambda=\operatorname{diag}(\lambda_1,\lambda_2,-\mu),
\]
with \(\lambda_1,\lambda_2,\mu\ge1\), and let \(L=\max(\lambda_1,\lambda_2,\mu)\). Write \(r_i\) for the i-th row of R, \(q_i=\|r_i\|\le1\). Assume one ORIGINAL physical coordinate has minority-sign diagonal
\[
A_{ii}=r_i^T\Lambda r_i=-c_i<0.
\]
For the two-sheet spectral-gradient cone
\[
\mathcal C_-:=\{z\ne0:z^T\Lambda^{-1}z<0\},
\]
put \(D=\operatorname{diag}(\sqrt{\lambda_1},\sqrt{\lambda_2},\sqrt\mu)\), \(z=Du\),
\[
a=\sqrt\mu |r_{i3}|,\qquad
b=\sqrt{\lambda_1r_{i1}^2+\lambda_2r_{i2}^2}.
\]
Then \(c_i=a^2-b^2>0\). For \(z\in\mathcal C_-\), \(|u_3|>\|(u_1,u_2)\|\), so
\[
|r_i\cdot z|=|(Dr_i)\cdot u|
\ge(a-b)|u_3|
\ge \frac{a-b}{\sqrt2}\|u\|
\ge \frac{a-b}{\sqrt{2L}}\|z\|.
\]
Also
\[
a-b=\frac{c_i}{a+b},\qquad a+b\le\sqrt2|Dr_i|\le\sqrt{2L}q_i.
\]
Hence the cone margin
\[
m_i:=\inf_{z\in\mathcal C_-}\frac{|r_i\cdot z|}{\|z\|}
\]
satisfies
\[
\boxed{m_i\ge \frac{c_i}{2Lq_i}.}\tag{1}
\]

Apply `QFORM-CURVATURE-WEIGHTED-PHYSICAL-FIBER-COVER-v1` from fleet01/B06, source snapshot `yspennstate/math-open-problems@ac50e5d5f2c3030c4bd87d5188117d92ceaf55a1`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B06/20260922T233555Z-qform-r19-b06/REPORT.md`. Its cone-only form permits the single weight \(a_i=m_i^{-2}\), and gives
\[
\operatorname*{ess\,sup}_{t<0}p_Q(t)
\le \frac{2\sqrt\pi}{\sqrt{|\det\Lambda|}}
 m_i^{-2}\sqrt{q_i|\Lambda r_i|}\sqrt{M_i},\tag{2}
\]
where the genuine two-dimensional ORIGINAL-product projection factor satisfies \(M_i\le e\). Since \(|\det\Lambda|\ge L\) and \(|\Lambda r_i|\le Lq_i\),
\[
\frac{\sqrt{q_i|\Lambda r_i|}}{\sqrt{|\det\Lambda|}}\le q_i\le1.
\]
Combining with (1),
\[
\boxed{
\operatorname*{ess\,sup}_{t<0}p_Q(t)
\le 8\sqrt{\pi e}\left(\frac{L}{c_i}\right)^2.
}\tag{3}
\]
Therefore, if \(-A_{ii}=c_i\ge\eta L\), then the two-sheet side is bounded by \(8\sqrt{\pi e}\eta^{-2}=23.3782589226\ldots\eta^{-2}\). The completed ruled one-sheet theorem gives \(\operatorname*{ess\,sup}_{t\ge0}p_Q(t)\le\pi\sqrt2\), so
\[
\boxed{\|p_Q\|_\infty\le\max\{\pi\sqrt2,8\sqrt{\pi e}\eta^{-2}\}.}\tag{4}
\]
For signature \((+,-,-)\), apply this to \(-Q\): the pivot has the sign of the unique minority eigenvalue.

## Designated partner applied at the exact-null boundary

The latest completed fleet04/B11 result is `yspennstate/math-open-problems@4110bbfd21beffa0260a017d468b0a486af56db1`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B11/20260922T222040Z-fleet04-B11-cone-envelope-r3/REPORT.md`. For
\[
H_0=\begin{pmatrix}0&0&1\\0&1&0\\1&0&0\end{pmatrix},\qquad Q=2X_1X_3+X_2^2,
\]
we have spectrum \(\{1,1,-1\}\), and its theorem applies with \(L=M=|\alpha|=|\beta|=1\), yielding
\[
\boxed{\|p_Q\|_\infty\le3\,2^{2/3}=4.7622031559\ldots.}\tag{5}
\]
This is an actual opposite-sign exact-null case not covered by (3), using genuine disjoint scalar/pair provenance.

## Current-source volume exit applied

The owner-required current package `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, path `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`, proves that any ORIGINAL-coordinate cross block \(M=M_0+E\) with \(s_3(M_0)\ge a\), maximum row-range leverage at most \(1/2\), and \(\|E\|_{op}\le a/16\) pays the full ambient form by
\[
\boxed{\|p_Q\|_\infty<23/a}\tag{6}
\]
with a continuous \(C_0\) representative, retaining all self blocks, outside couplings and affine terms. Thus after (3) the exact-rank-three indefinite residual can be restricted simultaneously to near-null minority physical diagonals and failure of this near-diffuse cross-volume certificate at every fixed universal scale.

Remaining implication: aggregate the near-null, low-cross-rank/hub residual without treating a conditional density cap as independence. Essential boundedness is proved only in the stated branches; continuity is obtained in the volume-stability branch, not from (3) itself.
