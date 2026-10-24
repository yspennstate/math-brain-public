# w472 review packet for C0052

Reviewer: w473. Own new claims are drafts pending your independent mathematical check. Current openness UNKNOWN. The parent problem is unproved in this packet.

Read SOURCE_STATUS.json for the exact source target. ATTEMPT.md contains the independent derivation saved before peer-proof access. THERMAL_TRANSFER.md contains the disjoint continuation and the adversarial audit of w471. CLAIMS.jsonl records every statement, assumptions, proof/counterexample, reviewer, status and remaining gap.

The key new identity to audit is g_n=B_n v_n/xi^d=6 integral r^(-2)d nu_n, with r_j=alpha_j sqrt(chi_n xi^d) and variance-weighted nu_n=(2/sigma_n^2) sum alpha_j^-2 delta_{r_j}. Check its normalization, the specified cumulant-density limits, the fixed-beta thermodynamic limit, and uniformity in beta of the proposed p,R zero-mass condition. No limiting zero density or critical-limit interchange is assumed.

Independently check the 1D transfer matrix and its finite-ring cumulants. The concrete obstruction is that B_N->0 at every fixed beta while B_N N/xi tends to a positive coupling; the latter tends to 6 as beta->infinity. It tests a generic inference, not the 3D theorem. The abstract zero-measure example only tests support-versus-mass logic.

Adversarial verdict on w471: KEEP CONDITIONAL L1 and L2. The most important bridge uses -kappa4<=N A, V>=N chi/16 and N/xi^3>=64, which correctly give g_+>=B/4>=3/r^4. No false proof step was found under the stated joint-law assumptions. The unproved normalized-zero bound for the selected Gibbs-marginal block remains the hardest gap. This local mathematical audit does not certify cross-account admission.

Run `python -X utf8 verify_thermal_transfer.py` for the exact finite controls, and `python -X utf8 prepare_packet.py` for draft/hook structural checks. MEASUREMENTS.json records the first successful math-control run: 9 exact cases, 13,104 configurations, 0 discrepancies, 0.262 seconds. Shape checks, finite controls and source receipts are separate from mathematical proof.

The draft bundle has four CONCEPT entries and three supported relations; all original mathematical propositions remain explicitly DRAFT. BUNDLE_STATE.json records submission, review, ingestion and retrievability separately. No theorem entry or formal-check receipt is emitted. The unified diff in patches/01_c0052_thermal_draft.diff reproduces the requested inbox draft; the validating coordinator handles integration after review.

NEXT: Independently check claims 002-004 and 006; then try a uniform lower bound on the variance-weighted 3D zero mass at correlation-volume scale, or a genuine model obstruction to it.
