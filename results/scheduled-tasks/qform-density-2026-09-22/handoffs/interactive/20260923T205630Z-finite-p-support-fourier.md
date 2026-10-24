# Finite-P-support Fourier receiver handoff

Date: 2026-09-23. Proven report: https://github.com/yspennstate/math-open-problems/blob/44cd716d0814a830c27feeba380a03f62da38c6b/proofnet24/QFORM-density/interactive/20260923T205630Z-finite-p-support-fourier/REPORT.md

For the canonical form with beta=0, Q=2HL+V²+2epsilon LP, take H independent cap-one and light A+B with independent 3D bank densities a,b capped by M_A,M_B. If bank P supports are arbitrary measurable sets of finite measures R_A,R_B, then

  ||p_Q||_infinity <= 3 (R_A R_B M_A M_B)^(1/3),

uniformly in epsilon, hub fragmentation, and locations of P supports.

Key bound: F=a*b and B(F)=int dp ||Fourier_{L,V}F_p||_1 <= (2pi)^2 sqrt(R_A R_B M_A M_B). At fixed p, Fourier invert the LV slice, integrate V by Fresnel and L against physical cap-one H via a Gaussian delta approximate identity. This gives |phi_Q(t)| <= B(F)/(4 sqrt(pi)) |t|^-3/2. No absolute Fourier norm of H enters. Optimize the inversion split at |t|=[B(F)/(4 sqrt(pi))]^(2/3), giving the stated homogeneous constant. Rough densities justified by Gaussian cutoff and dominated convergence.

For beta nonzero and epsilon nonzero, shearing P'=P+beta L/(2epsilon) applies only with a finite-measure support assumption for each P'_bank. Original P support alone is insufficient when L is unrestricted.

Full QFORM remains open: arbitrary original-coordinate supports allow the bank P projection support to have infinite measure, and B(F) is not controlled by two-bank 3D caps alone. The arbitrary measurable-E bilinear-offset restricted inequality is also still unproved. Earlier outer-target and regular-hub reports remain separate.

Two extensions in the updated report: (1) arbitrary real bank-local phases R_H(H)+R_A(Ω_A)+R_B(Ω_B) preserve the result because their complex projected densities have modulus below the original bank densities; (2) for unit P bins with masses m_Ak,m_Bj, finite Renyi 2/3 sums give ||p_Q||∞ <= 3(M_A M_B)^(1/3)(sum m_Ak^(2/3))(sum m_Bj^(2/3)). Both retain uniformity in epsilon. Arbitrary P marginals need not have finite sums.
