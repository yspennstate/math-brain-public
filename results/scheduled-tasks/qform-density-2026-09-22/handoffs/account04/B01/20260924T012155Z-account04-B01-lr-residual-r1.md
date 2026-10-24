# account04/B01 handoff — \(L^r\) residual interpolation

Run: \`20260924T012155Z-account04-B01-lr-residual-r1\`  
Math commit: \`f7e82d169badc671968036252d351b8533cdd425\`

The completed account01/B01 critical two-hub estimate
\[
|\phi_{Q_0}(t)|\le\min\{1,\pi P|t|^{-1}\}
\]
has been extended from an independent \(L^2\) residual to every independent residual density \(p_Z\in L^r\), \(1<r\le2\). With
\[
\alpha=(r-1)/r,\qquad \theta=r/(2r-1),
\]
Hausdorff--Young and a weighted frequency split give
\[
\|p_{Q_0+Z}\|_\infty
\le
\frac{1+\alpha}{\pi\alpha}
\left[
\frac{\alpha\pi}{2}
\left(\frac2{r-1}\right)^{1/r}
(2\pi)^\alpha P\|p_Z\|_r
\right]^\theta.
\]

For a source-disjoint hyperbolic edge \(Z=2cUV+\) affine terms,
\[
\|p_Z\|_r\le2^\alpha|c|^{-\alpha}.
\]
Hence the strict-N3 family with \(\det(BB^T)=k^4\) and \(c=k^{-q}\) remains uniformly bounded for every fixed \(q\ge2\) by choosing \(r=q/(q-1)\). Account01/B01 was the endpoint \(q=2,r=2\), with constant \(3\).

Full QFORM remains open. The exact residual obstruction is entanglement: a generic conditional density cap cannot replace the source-disjoint factorization.

Sources: owner revision \`2026-09-22.15\`; Claude base \`e5f71d79eff325201dd0274053d20268ce65b837\`; account01/B01 \`8d7d0ff65e86e787e8da9cb04afe3bfdf5401a59\`.
