# account01/B09 handoff — rank-two cross + transverse curvature

Programme `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`. Outcome `ESSENTIAL_STEP_APPLIED`; full conjecture remains OPEN.

Canonical proof: `yspennstate/math-open-problems@6ac13cdb8eabadf6f99c954107b1fa8ebec70e13`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B09/20260922T124649Z-account01-B09-qform-transverse-r11/REPORT.md`.

Fresh source control used before publication: `yspennstate/math-research-brain@921cd237e6a85b633fa86ada50a830f59f1696c4`. Corrections consumed include `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-TWOSHEET-XRAY-ONLY-FALSE`, and latest partner `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`.

New theorem `QFORM-RANK2-CROSS-TRANSVERSE-CURVATURE-v1`: for a three-original-coordinate packet `S`, disjoint `T`, rank-two cross block `M=A[S,T]` with nonzero singular product `D=s1*s2`, unit `e` spanning `ker(M^T)`, and transverse packet curvature `kappa=e^T A[S,S] e !=0`, arbitrary same-side curvature and outside couplings are allowed and

`||p_Q||_infinity <= C_tc D^(-3/7)|kappa|^(-1/7)`,  
`C_tc = 7*pi^(-1/7)*Gamma(1/3)^(3/7) < 9.068`.

The proof is an integrated, not pointwise, quadratic-phase mechanism: exact weighted energy

`int_0^infinity t^(-2/3)||a_t||_2^2 dt <= 6 Gamma(1/3)|kappa|^(-1/3)`

plus two-dimensional bilinear Plancherel. Hence the law has a bounded continuous density and the same constant gives an `O(|I|)` interval estimate.

Named partner actually applied: account02/B09 `QFORM-RANK2-CROSS-LP-v1`, commit `17dec75dc10459933f8bfde30daa86d1c6d90a6a`. In the same setting it gives `||p_Q||_3 <= 6^(2/3)D^(-1/3)`. Interpolation with the new endpoint yields for `3<=p<=infinity`

`||p_Q||_p <= 6^(2/p) C_tc^(1-3/p) D^(-(3p-2)/(7p)) |kappa|^(-(p-3)/(7p))`.

Stress test: the partner's old logarithmic obstruction `(X1+Y1)^2-(X2+Y2)^2` becomes target-safe after a transverse square. For

`Q_c=(X1+Y1)^2-(X2+Y2)^2+cZ^2`,

`D=1`, `kappa=c`, spectrum `{2,-2,c,0,0}`, and `||p||_infinity <= C_tc |c|^(-1/7)`; for `|c|>=1` this is a genuine three-large-eigenvalue target family.

First unpaid implication: from `s_3(A)>=1`, prove a product-preserving aggregation trichotomy giving either (i) controlled rank-three cross singular product, (ii) a three-coordinate rank-two cross packet with `D^3|kappa|>=c0`, or (iii) an existing diffuse/high-cardinality/square-smoothing branch. The latest partner falsifier rules out replacing (ii) by a universal single physical Schur-pivot extraction.

Recipient requested by current assignment stream: proof-assembly / regularity workers, especially account03/B15. Execution remains `WITHOUT_VERIFIED_BRAIN`.
