# Diffuse near-coloop with leakage at least one: direct Theorem F corollary

Status: source-checked application of an existing theorem. The full QFORM problem remains open.

Let \(H,X_1,\ldots,X_n\) be independent real variables with probability densities at most one. Set
\[
L=\sum_i\ell_iX_i,\qquad V=\sum_i v_iX_i,\qquad P=\sum_i p_iX_i,
\]
where the three coefficient vectors are orthonormal. Assume
\[
\max_i(\ell_i^2+v_i^2+p_i^2)\leq\tfrac12.
\]
For arbitrary real \(\beta\), nonzero \(\varepsilon\), and arbitrary affine terms, put
\[
Q=2HL+\beta L^2+V^2+2\varepsilon LP.
\]
Then \(Q\) has a bounded density satisfying
\[
\|p_Q\|_\infty\leq 12|\varepsilon|^{-2/3}.
\]
In particular \(|\varepsilon|\geq1\) gives the bound 12 at every level, including negative levels approaching zero. No independence among \(L,V,P\) is asserted.

Proof. On the original leaf coordinates, the rank-three part of the matrix is the orthonormal-frame lift of
\[
C=\begin{pmatrix}\beta&0&\varepsilon\\0&1&0\\\varepsilon&0&0\end{pmatrix}.
\]
Its eigenvalue product is \(\det C=-\varepsilon^2\). The normalized original-coordinate row leverages of this eigenspace are precisely \(\ell_i^2+v_i^2+p_i^2\leq1/2\), and its frame Gram is \(I_3\). Put \(I=\{1,\ldots,n\}\) in Theorem F of the source below. The coupling \(2HL\) and any terms involving only \(H\) lie in the arbitrary complementary matrix \(B\), with \(B_{II}=0\); conditioning on \(H\) gives an allowed affine leaf phase. Theorem F therefore gives \(12(|\det C|\det I_3)^{-1/3}=12|\varepsilon|^{-2/3}\), uniformly in affine parameters. Averaging over \(H\) preserves the bound.

Source: Theorem F (Fresnel-Brascamp-Lieb), math-open-problems commit e5f71d79eff325201dd0274053d20268ce65b837, path proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md. Its exact statement permits arbitrary symmetric complementary \(B\) with \(B_{II}\) diagonal and gives \(12(|\lambda_1\lambda_2\lambda_3|\det G_I)^{-1/3}\).

For the exact canonical full matrix (ordered \(H,L,V,P\)), the three-eigenvalue target gate is \(|\beta|\leq\varepsilon^2\); this corollary itself does not need that gate. The estimate deteriorates as \(\varepsilon\to0\) and does not apply to a leaf frame with leverage above \(1/2\). The full independent-product QFORM conjecture remains open.
