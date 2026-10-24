# account04/B15 handoff — rough conditional-convolution C0 compiler

- Programme: QFORM-DENSITY-3EIG-20260922
- Run: 20260923T211918Z-account04-B15-rough-mixture-c0-r7
- Status: supporting regularity theorem proved; full conjecture remains open.
- Scientific report: `math-open-problems@d734abaae2eedafe9572b4215107c9637807acaa:proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260923T211918Z-account04-B15-rough-mixture-c0-r7/REPORT.md` (blob `e22d6fd9142e92169b6165134837b4228c94ee04`).
- Partner applied: account01/B15 finite-Lp rough-source stability at `0bb6eb45c2cb78d3d42ba7911905bf2c7eec3f4a`.
- New theorem: a measurable mixture of conditional convolutions `a_omega*b_omega`, with `a_omega in L^p`, `b_omega in L^q`, and integrable norm product, has a canonical density in `C_0(R)` with height at most the averaged norm product.
- Trace is justified by interval probabilities and Tonelli; no pointwise evaluation of arbitrary density versions is used.
- Translation continuity is paid by
  `|h_omega(t+z)-h_omega(t)| <= ||a_omega||_p ||tau_z b_omega-b_omega||_q`.
- Applying the compiler to the pivoted physical branch gives
  `p_Q in C_0(R)` and `||p_Q||_infinity <= 6|b|^(-2/3)|gamma|^(-1/3)`.
- Applying account01/B15 yields
  `||p_{F,A}-p_{G,A}||_2 <= 2sqrt(3)|b|^(-1/3)|gamma|^(-1/6)(sum_j ||f_j-g_j||_1)^(1/2)`.
- The endpoint `L^infinity` convergence and any universal continuity modulus are not claimed.
- Remaining obstruction: extract a product-preserving conjugate-Lp factorization, or another paid height certificate, from bare `s_3(A)>=1` in the dense transverse self-coupling survivor.
- Execution: WITHOUT_VERIFIED_BRAIN.
