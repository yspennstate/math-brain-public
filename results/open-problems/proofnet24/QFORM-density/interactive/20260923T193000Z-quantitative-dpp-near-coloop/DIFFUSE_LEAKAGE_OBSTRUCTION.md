# Explicit small-volume frame with no affordable rank-preserving deletion

This family shows that the quantitative near-coloop theorem in REPORT.md does **not** imply the low-frame-energy deletion hypothesis in the companion rank-preserving deletion receiver. It is **not** a counterexample to the bounded-density conjecture.

Fix \(n=1024\), \(0<\eta\leq1/2\), and \(\theta_j=2\pi j/n\) for \(j=0,\ldots,n-1\). There are \(n+1\) physical coordinates: a hub \(h\) and light coordinates indexed by \(j\). Define the rows of an \((n+1)\times3\) frame \(U\) by
\[
 u_h=\sqrt{1-\eta}\,(1,0,0),\qquad
 u_j=\left(\sqrt{\frac\eta n},
            \sqrt{\frac2n}\cos\theta_j,
            \sqrt{\frac2n}\sin\theta_j\right).
\tag{1}
\]
The discrete trigonometric identities give \(U^{\mathsf T}U=I_3\). Let
\[
 \Lambda=\begin{pmatrix}0&1&0\\1&0&0\\0&0&1\end{pmatrix},
 \qquad A=U\Lambda U^{\mathsf T}.
\tag{2}
\]
Then \(A\) has exact rank three and three singular values exactly one.

## Physical no-pivot verification

The hub diagonal is \(a_{hh}=0\). For a light coordinate \(j\),
\[
 a_{hj}=\sqrt{\frac{2(1-\eta)}n}\cos\theta_j,
\quad
 a_{jk}=\frac{\sqrt{2\eta}}n(\cos\theta_j+\cos\theta_k)
          +\frac2n\sin\theta_j\sin\theta_k .
\]
Consequently \(|a_{hj}|\leq\sqrt{2/n}\) and \(|a_{jk}|\leq M_n:=(2+2\sqrt2)/n\). At \(n=1024\), \(M_n<1/64\), so every physical diagonal has modulus less than \(1/64\). For a hub-light principal pair,
\[
 |a_{hh}a_{jj}-a_{hj}^2|=a_{hj}^2\leq2/n=1/512<1/64.
\]
For two light indices,
\[
 |a_{jj}a_{kk}-a_{jk}^2|\leq2M_n^2
 =\frac{2(2+2\sqrt2)^2}{1024^2}<1/64.
\]
Thus \(A\) satisfies the unambiguous physical N3(1/64) condition uniformly over \(\eta\in(0,1/2]\).

## Vanishing third disjoint volume

The DPP one-point inclusion probability for \(h\) is \(\ell_h=\|u_h\|^2=1-\eta\). For iid volume-sampled bases \(S,T\), the event that both contain \(h\) precludes disjointness. Since \(\det\Lambda=-1\), the exact DPP identity yields
\[
 0\leq V_3(A)=\Pr(S\cap T=\varnothing)
 \leq1-(1-\eta)^2=2\eta-\eta^2\longrightarrow0.
\tag{3}
\]

## Why low-energy deletion cannot make any physical hub essential

For \(\eta>0\), any three **distinct light rows** span \(\mathbb R^3\): multiplying each row by a common nonzero diagonal matrix reduces their determinant to the determinant of \((1,\cos\theta_j,\sin\theta_j)\) at three distinct points on the unit circle. No line intersects the circle in three distinct points, so this determinant is nonzero.

Every light row has the same frame leverage \(\ell_j=(2+\eta)/n\). Let \(S\) be any deleted original-coordinate set with total frame energy
\[
 \sum_{i\in S}\|u_i\|^2<1.
\tag{4}
\]
Then \(S\) contains fewer than \(n/(2+\eta)\leq n/2\) light coordinates. More than \(n/2\) light rows remain. After excluding **any single proposed physical hub** from the retained set, at least three distinct light rows still remain and span \(\mathbb R^3\). Therefore the retained frame has no physical coloop, while its row rank stays three. No set of frame energy below one can trigger the exact rank-preserving deletion receiver, even though \(V_3(A)\to0\), \(\ell_h\to1\), and \(A\) approaches an exact-coloop model in rank-two Frobenius leakage.

This only disproves the proposed **structural shortcut** from small third volume to affordable exact-coloop deletion. The density of \(X^{\mathsf T}AX\) is not analyzed or refuted by this example. An analytic receiver stable under overlapping transverse light leakage is still needed.
