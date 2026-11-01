# The true normalized near-coloop spectrum restricts beta and pays diffuse large epsilon

Status: a rigorous application of the existing Fresnel–Brascamp–Lieb Theorem F to an exact-rank-three canonical branch. The full arbitrary-rank QFORM target remains open.

Let \(H\) be a physical cap-one source independent of leaf originals, and let \(L=\ell\cdot X\), \(P=p\cdot X\), \(V=v\cdot X\) be three orthonormal leaf forms. Consider
\[
Q=2HL+\beta L^2+V^2+2\epsilon LP.
\tag{1}
\]
Its exact active matrix in the orthonormal linear coordinates \((H,L,V,P)\) is
\[
A_*=
\begin{pmatrix}
0&1&0&0\\
1&\beta&0&\epsilon\\
0&0&1&0\\
0&\epsilon&0&0
\end{pmatrix}.
\]
The nonzero eigenvalues are \(1\) and
\[
\lambda_\pm=\frac{\beta\pm\sqrt{\beta^2+4(1+\epsilon^2)}}2.
\]
Since \(\lambda_+>0>\lambda_-\), the **exact** condition \(s_3(A_*)\ge1\) is
\[
\boxed{|\beta|\le\epsilon^2.}\tag{2}
\]
Indeed the smaller absolute root \((\sqrt{\beta^2+4(1+\epsilon^2)}-|\beta|)/2\ge1\) if and only if (2) holds. This restriction follows from the *specified normalized exact-rank-three matrix*, not from an arbitrary canonical model with a different hub coefficient or arbitrary extra spectrum.

Condition on the physical \(H\). The residual leaf quadratic matrix is
\[
B=\beta\ell\ell^T+\epsilon(\ell p^T+p\ell^T)+vv^T.
\]
For \(\epsilon\ne0\), it has exact rank three and nonzero eigenvalues \(1\) and
\[
\mu_\pm=\frac{\beta\pm\sqrt{\beta^2+4\epsilon^2}}2.
\]
The smallest singular value is
\[
s_3(B)=\min\left\{1,\frac{\sqrt{\beta^2+4\epsilon^2}-|\beta|}{2}\right\}.
\]
Under (2) and \(|\epsilon|\ge1\), this is at least
\[
\tau_*:=\frac{\sqrt5-1}{2}>0.618.
\tag{3}
\]
To check (3), for fixed \(x=\epsilon^2\ge1\) the smaller root decreases with \(|\beta|\), so its minimum over \(|\beta|\le x\) occurs at \(|\beta|=x\) and equals \(h(x)=(\sqrt{x^2+4x}-x)/2\). The function \(h\) increases for \(x>0\), and \(h(1)=\tau_*\).

The exact leaf eigenframe differs from the orthonormal frame \((\ell,p,v)\) only by a \(3\times3\) orthogonal rotation. Hence its original-coordinate row leverage equals \(\ell_i^2+p_i^2+v_i^2\). If
\[
\max_i(\ell_i^2+p_i^2+v_i^2)\le\tfrac12,
\tag{4}
\]
the already proved [Theorem F and its rank-three corollary](https://github.com/yspennstate/math-open-problems/blob/e5f71d79eff325201dd0274053d20268ce65b837/proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md) apply to \(B\) with arbitrary original-coordinate affine term \(2HL\). For every conditioned \(H=h\), its density is bounded by \(12/s_3(B)\). Averaging conditional interval probabilities yields
\[
\boxed{\|p_Q\|_\infty\le\frac{12}{\tau_*}
=6(\sqrt5+1)<19.42}
\tag{5}
\]
whenever (2), (4), and \(|\epsilon|\ge1\) hold, **even if every V source overlaps L or P**.

More generally \(|\epsilon|\ge\eta>0\) under (2) gives \(s_3(B)\ge h(\eta^2)>0\), hence \(\|p_Q\|_\infty\le12/h(\eta^2)\). The remaining diffuse canonical bottleneck can therefore be restricted to \(\epsilon\to0\) with \(\beta=O(\epsilon^2)\), along with heavy-leaf/non-diffuse patterns outside (4). This statement does not pay the limiting \(\epsilon=0\) by Theorem F, but that limit has a separate two-light coarea receiver; proving uniformity *through* zero for fully overlapping sources is the missing step.
