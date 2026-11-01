# Exact-coloop truncation with controlled rank-two leakage

This addendum builds on [REPORT.md](REPORT.md). All indices here are original physical coordinates.

Let \(A=U\Lambda U^{\mathsf T}\) have exact rank three, \(U^{\mathsf T}U=I_3\), \(s_3(A)\geq1\), and N3(1/64). Put
\[
 V=V_3(A),\qquad C_*=\kappa^{-1}=22.89696698\ldots,
\]
where the quantitative DPP theorem in REPORT.md gives a physical coordinate \(h\) with
\[
 m:=\|u_h\|^2\geq1-C_*V/\det(\Lambda)^2.
\]
For the useful small-volume case \(C_*V/\det(\Lambda)^2<1\), choose \(v=u_h/\sqrt m\), \(J=[n]\setminus\{h\}\), and set
\[
 \eta=1-m,\quad z=U_Jv,\quad
 E=\begin{pmatrix}0\\z\end{pmatrix}v^{\mathsf T},\quad
 U_0=U-E,\quad A_0=U_0\Lambda U_0^{\mathsf T}.
\tag{1}
\]
Then \(\|z\|^2=\eta\) and the \(J\)-rows of \(U_0\) lie in \(v^\perp\), a two-dimensional space. Also
\[
 U_0^{\mathsf T}U_0=I_3-\eta vv^{\mathsf T}.
\tag{2}
\]
Thus \(\|U_0\|=1\); whenever \(m>0\), \(A_0\) has rank three and \(h\) is an **exact physical coloop** of its row frame. Its physical hub diagonal is unchanged:
\[
 (A_0)_{hh}=A_{hh},\qquad |(A_0)_{hh}|<1/64.
\tag{3}
\]
The difference has an explicit rank-two form. Writing \(\tilde z=(0,z)\) and \(q=U_0\Lambda v\),
\[
 A-A_0=q\tilde z^{\mathsf T}
       +\tilde z q^{\mathsf T}
       +(v^{\mathsf T}\Lambda v)\tilde z\tilde z^{\mathsf T}.
\tag{4}
\]
In particular, \(\operatorname{rank}(A-A_0)\leq2\), and
\[
 \|A-A_0\|_F
 \leq(2\sqrt\eta+\eta)\|\Lambda\|
 \leq(2+\sqrt\eta)\sqrt{C_*V}
 \leq3\sqrt{C_*V}<14.36\sqrt V.
\tag{5}
\]
The key spectral cancellation is \(\|\Lambda\|/|\det\Lambda|
 =1/(s_2(\Lambda)s_3(\Lambda))\leq1\). Equation (5) holds uniformly even as \(\|\Lambda\|\to\infty\). Weyl's inequality yields
\[
 s_3(A_0)\geq1-3\sqrt{C_*V}.
\tag{6}
\]

**A paid model within the truncation.** If \(V\leq10^{-3}\), (5)–(6) give \(s_3(A_0)>0.546\). The independent physical coordinate \(X_h\) has density cap one, while the two-dimensional light projection belonging to the two-dimensional row space of \((U_0)_J\) has joint density cap two. The general three-dimensional-core four-region coarea receiver applies to \(Q_{A_0}\), uniformly in affine terms: after scaling by \(\sigma=s_3(A_0)\geq1/2\), its hub coefficient satisfies \(|a|/\sigma<1/32\). The proof of GENERAL_3D_CORE.md works unchanged with threshold \(1/32\): \(t\geq\sqrt{1-(1/32)^2}\), the central region lies inside radius \(2.48\), and the same Gaussian comparison bounds its central shell volume by \(<27\delta\). The four regions give \(1+[2/t+29]M<1+32M\leq65\), for \(M\leq2\). Thus
\[
 \|p_{Q_{A_0}+\text{affine}}\|_\infty
 <\frac{65}{s_3(A_0)}
 \leq\frac{65}{1-3\sqrt{C_*V}}
 <120\quad(V\leq10^{-3}).
\tag{7}
\]
No global no-pivot condition is imposed on \(A_0\); only its inherited small physical hub diagonal is needed for this receiver.

**Precise remaining gap.** Equation (7) bounds the exact-coloop model \(A_0\), not the original matrix \(A\). The error (4) has rank at most two and arbitrarily small Frobenius norm when \(V\to0\), but the random inputs may have unbounded support. Thus \(X^{\mathsf T}(A-A_0)X\) is not uniformly small as a random variable, and the density estimate does not transfer merely by perturbing the matrix. A uniform product-law stability theorem for this special rank-two leakage would close the small-volume exact-rank-three case. Nothing here addresses extra nonzero eigenvalues of \(A\).
