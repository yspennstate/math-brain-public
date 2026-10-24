# Exact-rank physical crossing gives arbitrary-rank QFORM density

**Proved 2026-09-23.** If a physical coordinate cut (S,T) has crossing block (A_{S,T}) of **exact rank (k\ge3)** and smallest nonzero singular value (\beta>0), independent cap-one inputs satisfy
\[
 \|p_{X^TAX+b^TX+c}\|_\infty\le\frac{2k}{(k-2)\beta}\le\frac6\beta
\]
for all within-bank matrices and unrestricted affine coefficients. Full proof:
https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T194300Z-exact-cross-rank-fourier/REPORT.md
(commit 51d2edb29d7a4c150e4d47ed3a6685875a8483ae).

Proof in one line: thin SVD (A_{S,T}=R D W^T); each independent bank's (k)-projection density ≤(2^{k/2}) by LPP; internal quadratic and affine phases produce complex amplitudes dominated by these densities; (k)-D Plancherel on cross phase (e^{2it(R^TX_S)^TD(W^TX_T)}) gives (|\varphi_Q(t)|\le\min\{1,(2\pi/(\beta|t|))^{k/2}\}), integrable for (k>2).

**Critical scope:** exact rank of the entire crossing block. If crossing rank exceeds three and later singular values are tiny, one cannot simply retain the top three; residual cross terms couple the banks and break separation. No current argument shows every (s_3(A)\ge1) indefinite matrix admits a cut with controlled smallest nonzero singular value.
