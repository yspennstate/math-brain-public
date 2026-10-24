# Diffuse two-light Fourier receiver with local potentials

Published/read-back one-coordinate theorem: https://github.com/yspennstate/math-open-problems/blob/88488cf951d2c9552608f8d1dd8776f2bcf678d2/proofnet24/QFORM-density/interactive/20260923T205600Z-diffuse-two-light-local-potentials/REPORT.md

Published/read-back two-bank extension and balanced-ratio leakage corollary: https://github.com/yspennstate/math-open-problems/blob/cbd0e29add7c75d966d5101d249bb802f39a58fd/proofnet24/QFORM-density/interactive/20260923T205600Z-diffuse-two-light-local-potentials/TWO_BANK_ADDENDUM.md

If H and light X_i are independent cap-one, L,V are an orthonormal light two-frame with every row leverage ℓ_i²+v_i²≤1/2, and τλ≠0, then Q=2τHL+λV²+R_H(H)+Σ_iR_i(X_i) has bounded continuous density with ||p_Q||∞≤3e^(2/3)(|τ|√|λ|)^(-2/3), for arbitrary measurable source-local real potentials. This includes arbitrary original-coordinate affine terms, hub self-square, and diagonal light quadratic terms with no coefficient dependence. The proof uses the uniform 2D Wiener/BL-HY bound under separate source phases, one Fresnel transform in V, and hub cap.

More generally, if two independent light banks B,C have joint density caps M_B,M_C on (L_j,V_j), then arbitrary bank-local measurable potentials R_B(X_B),R_C(X_C) are allowed. Plancherel gives J0≤(2π)²√(M_BM_C), yielding ||p_Q||∞≤3(M_BM_C)^(1/3)(|τ|√|λ|)^(-2/3). This includes arbitrary within-bank quadratic tails but excludes extra cross-bank quadratic terms. In particular, P_B=αL_B and P_C=−αL_C imply LP=α(L_B²−L_C²), so the bound covers arbitrary 2εLP leakage uniformly; with M_B,M_C≤2 and τ=λ=1 it is <4.77.

Parameter-matched extension: if P_B=α_B L_B and P_C=α_C L_C, then βL²+2εLP is bank-local when β+ε(α_B+α_C)=0, because its cross coefficient is 2[β+ε(α_B+α_C)]. Boundary: outside this exact cancellation, global βL² and arbitrary LP ratios introduce cross-bank quadratic terms. The negative-target overlapping leakage remains open; neither theorem closes unrestricted QFORM.
