# account04/B03 handoff — hyperbolic-edge fourth-volume cancellation

Run: `20260924T021651Z-account04-B03-hyperbola-fourvolume-r3`  
Status: supporting theorem proved; full conjecture open; continuity not claimed.

For a physical zero-diagonal hyperbolic pair
\[
A[H,H]=\begin{pmatrix}0&\mu\\\mu&0\end{pmatrix},
\]
let \(S\) be its Schur complement. Conditional completion leaves the original two coordinates independent and gives a translated product \(2\mu(U+\alpha)(V+\beta)\) plus the affine Schur residual.

The translation-uniform product estimate
\[
p_{2\mu(U+\alpha)(V+\beta)}(y)
\le\sqrt2|\mu|^{-1/2}|y|^{-1/2}
\]
combined with the completed account01/B03 bipartite Moyal theorem at the literal residual cut \(I|J\) yields
\[
\boxed{\|p_Q\|_{\infty,\mathrm{ess}}
\le8|\det A[H\cup I,H\cup J]|^{-1/4}.}
\]
The coefficient \(\mu\) cancels exactly through the block determinant identity.

Defining the ordered disjoint fourth-volume
\[
\mathcal F_4(H)=
\sum_{|I|=|J|=2,\ I\cap J=\varnothing}
\det A[H\cup I,H\cup J]^2,
\]
Bernoulli cut averaging and the completed marginal-free \(Z_2\) theorem give
\[
\boxed{\|p_Q\|_{\infty,\mathrm{ess}}
\le16e^{1/4}\mathcal F_4(H)^{-1/8}.}
\]

Concrete target application: for
\[
A_*=\begin{pmatrix}0&1\\1&0\end{pmatrix}
\oplus\begin{pmatrix}0&0&1&0\\0&0&0&1\\1&0&0&0\\0&1&0&0\end{pmatrix},
\]
and every ambient extension containing this principal block,
\[
\boxed{\|p_{X^TAX}\|_{\infty,\mathrm{ess}}\le8.}
\]
The block has three \(+1\) and three \(-1\) eigenvalues; interlacing keeps the ambient family inside the original target class.

Canonical report: `yspennstate/math-open-problems@8147f1247043e419eb6762911c4a34fa58494d0f`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B03/20260924T021651Z-account04-B03-hyperbola-fourvolume-r3/REPORT.md`.

Source pins:
- required Claude directory latest commit checked: `7ffd1ed79398611eb06752f622be0ce33dcacb5a`;
- designated base: `e5f71d79eff325201dd0274053d20268ce65b837`;
- completed account01/B03 Moyal theorem: `6c4698000d4fd206b465a18231ba8c7a8f643f59`;
- completed marginal-free \(Z_2\) theorem: `68e6d8f52d904033878f6f55c376c38fd214684e`.

Exact gap: the spectral hypothesis \(s_3(A)\ge1\) has not been shown to force a zero-diagonal physical hyperbola with \(\mathcal F_4(H)\gtrsim1\), nor this branch versus a paid complementary exit. A nonzero-diagonal indefinite pair cannot be sheared to the hyperbolic normal form without destroying product independence.
