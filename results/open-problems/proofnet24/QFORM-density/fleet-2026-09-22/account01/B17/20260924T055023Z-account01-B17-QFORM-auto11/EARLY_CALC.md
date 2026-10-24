# account01/B17 early calculation — strict-threshold principal delocalization

Status: QFORM only. Full unrestricted theorem remains OPEN. Continuity remains separate. Execution context: WITHOUT_VERIFIED_BRAIN.

Let
\[
B_H=I_3-\frac23\mathbf1\mathbf1^T
=\frac13\begin{pmatrix}1&-2&-2\\-2&1&-2\\-2&-2&1\end{pmatrix},
\qquad B_H^2=I_3,
\]
so its eigenvalues are \(1,1,-1\). For integer \(m\ge2\), let \(R_m\in\mathbb R^{3m\times3}\) have every row in bank \(j\) equal to \(e_j/\sqrt m\). Then \(R_m^TR_m=I_3\). Define
\[
A_m=\left(1+\frac1m\right)R_mB_HR_m^T.
\]
Hence the exact nonzero spectrum is
\[
\{1+1/m,\;1+1/m,\;-(1+1/m)\}.
\]
All physical entries are nonzero: same-bank entries are \((m+1)/(3m^2)\), cross-bank entries are \(-2(m+1)/(3m^2)\).

For a physical coordinate subset \(S\), let \(k_j\) be its count in bank \(j\). Then
\[
R_S^TR_S=\operatorname{diag}(k_1/m,k_2/m,k_3/m),
\]
and therefore
\[
\|A_m[S]\|_{op}\le\left(1+\frac1m\right)\|R_S\|_{op}^2
=\left(1+\frac1m\right)\frac{\max_jk_j}{m}
\le\left(1+\frac1m\right)\frac{|S|}{m}.
\]
In particular, if \(|S|\le m-1\),
\[
\|A_m[S]\|_{op}\le1-\frac1{m^2}<1.
\]
Thus every principal submatrix on at most \(m-1\) original coordinates is strictly sub-threshold although the full matrix has three strict target eigenvalues.

Also \(A_m^2=(1+1/m)^2P_m\), where \(P_m=R_mR_m^T\) and \((P_m)_{ii}=1/m\). Hence
\[
\|A_me_i\|_2=(1+1/m)m^{-1/2}\to0,
\]
while \(\max_{ij}|(A_m)_{ij}|=2(m+1)/(3m^2)\to0\).

With independent \(X_i\sim U[-1/2,1/2]\), \(Y_m=R_m^TX\) has three independent normalized bank sums and \(Y_m\Rightarrow N(0,I_3/12)\). Therefore
\[
Q_m=X^TA_mX\Rightarrow G_1^2+G_2^2-G_3^2,
\]
whose density at zero is \(3\sqrt2\). The final report will phrase the lower bound via small-ball derivatives, not a continuity assumption.

Partner input selected: account02/B17 at math-open-problems@96940cec9f8a2d4ca231a77d1324cfb7c59a87ad proves globally for arbitrary cap-one product laws
\[
\|p_{\beta Y^2+2aXY+2aYZ+\kappa(X-Z)^2}\|_\infty\le\frac{2\sqrt2}{\sqrt{|\kappa a|}}.
\]
I will apply it at \((\beta,a,\kappa)=(1/2,1,1)\), whose matrix has spectrum \(2,(1\pm\sqrt{33})/4\), all three magnitudes >1.
