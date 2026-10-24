# Diffuse exact-rank-three QFORM theorem: arbitrary affine, dimension-free

**New theorem (2026-09-23):** Independent cap-one (X_i), exact-rank-three symmetric (A=U\Lambda U^T), (U^TU=I_3), (s_3(A)\ge\sigma), and (\max_i\|U_{i,*}\|^2\le1/12) imply
\[
\|p_{X^TAX+b^TX+c}\|_\infty\le24/\sigma
\]
for **every** affine (b,c) and every signature. Full proof and constant: https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T193700Z-diffuse-rank-three-fourier/REPORT.md (commit a5961e3a9ebd3da5bbc316722ef77507331f1a33).

Random sign partition (S,T) of physical coordinates: (H=\sum_i\varepsilon_i u_i u_i^T) has (\mathbb E\|H\|_F^2=\sum_i\|u_i\|^4\le3\delta\le1/4); choose a signing with (\|H\|\le1/2). Both Gram matrices (U_S^TU_S,U_T^TU_T\succeq I_3/4). Independent 3D projections (Z=U_S^TX_S,W=U_T^TX_T) have (L^\infty) densities (\le2^{3/2}(1/4)^{-3/2}) by LPP projection cap. For each frequency (t), absorb within-bank quadratic forms and **arbitrary affine terms including null leakage** into complex amplitudes (\alpha_t(z)=p_Z(z)\mathbb E[e^{itq_S(X_S)}|Z=z]), similarly (\beta_t), with modulus controlled by their 3D marginal densities. Cross phase is exactly (e^{2itZ^T\Lambda W}). Cauchy–Schwarz/Plancherel yields ( |\varphi_Q(t)|\le\min\{1,(2\pi)^{3/2}(c\sigma|t|)^{-3/2}\}); integration gives (6/(c\sigma)=24/\sigma).

**Scope:** Exact rank three and diffuse 3-frame, or more generally any rank-three frame admitting a two-bank split with both Gram matrices (\succeq cI_3) (constant (6/(c\sigma))). High-leverage near-coloop frames and additional indefinite eigendirections remain outside this proof. Independent audit of constants and all-affine handling completed.

Another scoped exact-rank-three theorem, with **no** leverage restriction but dimension factor (51(n-2)/\sigma) for arbitrary affine terms, is at https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T193238Z-exact-rank-three-affine/REPORT.md (commit bfd9de120db53ccf212a90deb5d6486c3c0f7674).
