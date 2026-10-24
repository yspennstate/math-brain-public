# A diffuse rank-three family obstructing three simple receivers

Status: exact matrix calculation and method obstruction. This is **not** a counterexample to the product-input density conjecture.

Let \(m\ge4\) be divisible by \(4\), with original coordinates indexed by a hub \(h\) and \(m\) light indices \(j=0,\ldots,m-1\). Put \(\theta_j=2\pi j/m\) and define light vectors
\[
\ell_j=m^{-1/2},\qquad
v_j=(2/m)^{1/2}\cos\theta_j,\qquad
p_j=(2/m)^{1/2}\sin\theta_j.
\]
Then \(\ell,v,p\) are orthonormal. For \(0\le\varepsilon\le1\), set
\[
A_{m,\varepsilon}
=h\ell^T+\ell h^T+vv^T+\varepsilon(\ell p^T+p\ell^T).
\]
Here \(h\) is the distinguished standard basis vector, and \(\ell,v,p\) have zero hub component. The associated homogeneous quadratic is \(X^T A_{m,\varepsilon}X=2HL+V^2+2\varepsilon LP\), for \(L=\ell\cdot X_{\rm light}\), \(V=v\cdot X_{\rm light}\), \(P=p\cdot X_{\rm light}\).

## Exact spectrum

In the orthonormal basis \((h,\ell,v,p)\), the only nonzero part of \(A\) is
\[
\begin{pmatrix}
0&1&0&0\\
1&0&0&\varepsilon\\
0&0&1&0\\
0&\varepsilon&0&0
\end{pmatrix}.
\]
Its nonzero eigenvalues are \(\sqrt{1+\varepsilon^2},-\sqrt{1+\varepsilon^2},1\). Hence \(A\) has exact rank three and \(s_3(A)=1\) for every \(\varepsilon\), including arbitrarily small positive values.

## Every light singleton coupling is small

For a light index \(i\), orthonormality of \(\ell,v,p\) gives
\[
\sum_{j=0}^{m}|A_{ij}|^2
=\ell_i^2+v_i^2+\varepsilon^2(\ell_i^2+p_i^2)
\le (3+3\varepsilon^2)/m\le6/m.
\]
The sum includes the hub column and the diagonal. Therefore the off-diagonal coupling norm of every light original coordinate to any other physical bank is at most \(\sqrt{6/m}\). Among any three distinct original singleton hubs, at least two are light. In particular, \(s_3(A)\ge1\) does not force three physical singleton stars with fixed positive cross coefficients.

## No uniformly conditioned principal triple

The hub row restricted to two light indices has squared Euclidean norm \(2/m\). Each light row restricted to any triple has squared norm at most \(6/m\). Thus every physical principal three-by-three submatrix obeys
\[
\|A_{II}\|_F^2\le18/m,\qquad |I|=3.
\]
This family has no principal three-coordinate core with a dimension-independent smallest singular value, despite its global \(s_3=1\).

Its physical diagonal entries satisfy \(|A_{ii}|\le(2+2\sqrt2\,\varepsilon)/m\) for light \(i\), while \(A_{hh}=0\). The hub-light principal pair determinant is \(-1/m\).

## Every rank-three physical cross cut degenerates as ε tends to zero

For any partition \(S\sqcup T\) of original coordinates, the cross block at \(\varepsilon=0\) has rank at most two. If \(h\in S\), explicitly
\[
(A_{m,0})_{ST}=h_S\ell_T^T+v_Sv_T^T;
\]
if \(h\in T\), use \(\ell_Sh_T^T+v_Sv_T^T\). The perturbation \(\varepsilon(\ell p^T+p\ell^T)\) has operator norm \(\varepsilon\), and compression to a cross block cannot increase it. The singular-value perturbation inequality gives
\[
s_3\big((A_{m,\varepsilon})_{ST}\big)\le\varepsilon
\]
for **every** physical cut. Choosing \(\varepsilon=\varepsilon_m\to0\) rules out a uniform rank-three cross-cut receiver as a consequence of \(s_3(A)\ge1\) alone.

The \(\varepsilon=0\) endpoint has a separate two-light Fourier/coarea receiver. The estimate here identifies the unresolved stability regime: exact product light coordinates, overlapping \(P\), and small \(\varepsilon\). It does not show that the density grows with \(m\) or \(\varepsilon\).
