# fleet02/B18 r27 — early checkpoint

Full QFORM remains OPEN. This run attacks the circular nonplanar Schur-isotropic survivor and asks whether the newest fleet03/B18 rank-two Schur compiler can pay it uniformly.

Let
\[
v_j=m^{-1/2}(1,\sqrt2\cos(2\pi j/m),\sqrt2\sin(2\pi j/m)),\quad j=0,\dots,m-1,
\]
so \(V^TV=I_3\). Put \(u_0=r e_1\), let the other rows of \(U\) be the \(v_j\), set \(s=\sqrt{1+r^2}\), and
\[
D_r=\begin{pmatrix}0&s^{-1}&0\\s^{-1}&0&0\\0&0&1\end{pmatrix},\qquad A_{m,r}=U D_r U^T.
\]
Then the nonzero spectrum is exactly \(\{-1,1,1\}\), because \(U^TU=\operatorname{diag}(s^2,1,1)\) and \(D_rU^TU\) has eigenvalues \(-1,1,1\).

For a residual physical pivot \(i\), \(a_i=(A_{m,r})_{ii}=v_i^TD_rv_i\), hence \(|a_i|\le\|v_i\|^2=3/m\). If \(a_i\ne0\), let \(S=A_{m,r}/a_i\) be its scalar Schur complement. For any partition \(L\sqcup R\) of the remaining physical coordinates, write \(B=S_{L,R}\). Since \(\operatorname{rank}S=2\), if \(B\) has rank two then
\[
(\sigma_1(B)\sigma_2(B))^2=\sum_{p<q\in L}\sum_{k<\ell\in R}\det B_{\{p,q\},\{k,\ell\}}^2.
\]
The Schur-minor identity and \(A=UD_rU^T\) give
\[
\det B_{\{p,q\},\{k,\ell\}}
=\frac{\det D_r}{a_i}\det(u_i,u_p,u_q)\det(u_i,u_k,u_\ell).
\]
Thus, with \(T_i=\sum_{p<q;\ p,q\ne i}\det(u_i,u_p,u_q)^2\),
\[
\sigma_1(B)\sigma_2(B)\le \frac{|\det D_r|}{2|a_i|}T_i.
\]
Cauchy--Binet/leverage gives exactly
\[
T_i=\det(U^TU)\,u_i^T(U^TU)^{-1}u_i=\frac{3+2r^2}{m}.
\]
Since \(|\det D_r|=(1+r^2)^{-1}\),
\[
|a_i|\,|\det D_r|\,T_i\le \frac9{m^2}.
\]
Applying the completed fleet03/B18 rank-two Schur certificate
\[
8|a_i|^{-1/2}(\sigma_1\sigma_2)^{-1/4}
\]
therefore yields a certificate no smaller than
\[
\frac{8\,2^{1/4}}{\sqrt3}\sqrt m=5.492712\ldots\sqrt m.
\]
So every applicable one-pivot rank-two certificate diverges on this exact target family; if the cross rank is below two the theorem is unavailable. Because the ambient rank is exactly three, two successive nonzero scalar Schur pivots leave rank at most one, so the partner's nested compiler cannot terminate in a rank-two cross block after two or more pivots.

This is a method obstruction, not a QFORM counterexample. Next: combine it with the pinned single-Theorem-D cross-volume barrier and source-audit the only external product-marginal theorem used by the partner.