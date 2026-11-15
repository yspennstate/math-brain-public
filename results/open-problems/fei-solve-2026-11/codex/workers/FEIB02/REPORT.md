# FEIB02 report

The closed forms, exhaustive census and both dense structured-family sweeps are complete. The new direct bounds for every symmetric Boolean function are

    B <= 3.459354 I,
    Gamma <= (8/5) I.

The proof uses no FEI upper bound. Above dimension 24 it is analytic; below it an integer-only certificate verifies B<=2.18I on every representative, which is more than enough for both conclusions. PROOFS.md contains the full argument, including the derivative-envelope lemmas and rational constant certificates. PROOF_REVIEW.md is a short reading guide.

These bounds do not improve the supplied symmetric FEI constant 4.650431 through Theorem 1. Three-variable AND has B/I=15/4-(3/2)log_2 3=1.3725562489182657..., above the required 1.3252155. witness_check.log checks it by the census, exact finite differences, a direct truth-table transform and the closed expression. Majority gives the stronger asymptotic obstruction B/I->2/ln 2. This limits that sufficient estimate; it is not a lower bound of 7.77 for the FEI constant.

## What was computed

Every symmetric value vector in dimensions 1 through 24 was covered: 67,108,860 vectors, represented by 33,554,430 global-sign representatives. The nonconstant representative count is 33,554,406. These counts come from census_01.json through census_24.json and are collected in census_counts.csv and run_summary.json. Constants and balanced I=1 cases have undefined ratios and are handled separately.

RESULTS.md gives the per-dimension A/I, B/I, Gamma/I and balanced ratios over I-1. extrema.csv supplies all extremal value vectors, including P and all high-precision ties up to global sign. The dimension-24 maxima are A/I=2.833333224058, B/I=2.097299030274, Gamma/I=0.937865587423 and P/I=0.999999880791 (census_24.json and suprema_certified.json).

All 2,001,000 nonconstant thresholds in every dimension 1 through 2000 were evaluated. All 2,000,999 parity-times-threshold vectors in dimensions 2 through 2000 were also covered; at dimension 1 these products are constant. Reflection and global-sign invariance cover the omitted equivalent vectors. thresholds_dense.jsonl, parity_dense.jsonl, majority.csv and parity_family.csv contain the dimension tables. The parity convention is f_t=(-1)^t times a threshold. Ordinary parity itself has I=n and A=B=Gamma=P=0 exactly.

At n=2000 the threshold-family maxima are B/I=2.739944660108 and Gamma/I=1.306820733839. The parity-family maxima are B/I=0.048514103332 and Gamma/I=0.024228058366. The separate convolution outputs retain log2 ratios for tiny positive values that underflow ordinary floating point.

Bounded value-vector searches on the saved dimension grid through 2000 give B/I=2.740359543644 and Gamma/I=1.347607298037 at n=2000 (hill_2000.json, gamma_refinement_2000.json and refinement_high_precision.json). These are lower bounds from finite searches, not certified optima. A separate A search retained corner AND/OR and gives A/I=2.998 at n=2000, consistent with its exact formula. Balanced paired-coordinate searches use the objective over I-1 directly; at n=1999 they give B/(I-1)=2.744446594676 and Gamma/(I-1)=1.360500539114 (balanced_hill_v2_1999.json and balanced_high_precision.json).

All logs are base 2. Functionals are in bits, I is total influence, and the ratios are bits per unit influence. functional_ratios.png and functional_ratios.pdf plot the census, dense threshold maxima, search witnesses and proved bounds.

## Why the digits are reliable

The finite census computes every derivative triangle, Fourier coefficient, absolute sum, support count and squared sum as exact integers. Only the final logarithms use floating point. An independent integer-interval census retains every possible maximizer. Exact rational logarithm expressions prove all remaining ties, and a positive-series calculation certifies all 188 defined suprema to 100 decimal places. suprema_certified.json stores the values, outward bounds and all extremal vectors; suprema_certificate_verification.log records the independent certificate replay. The original floating-point discovery agrees, with a smallest excluded-candidate gap of 5.52931572972426e-7 (candidates_audit.log). The finite proof bound is stronger evidence of a different kind: quantlog.h encloses every logarithm by exact rational inequalities, and unsigned 128-bit arithmetic checks the finite proof bound on every representative. The tighter census_interval.c scan additionally certifies the actual suprema; its log enclosures are independent of libm. generate_quantlog.py verifies all table entries without transcendental calls.

The large sweeps use exact GMP recurrences. Thresholds were independently calculated in Python by a different traversal; parity thresholds were independently calculated by exact integer polynomial convolution. dense_audit.log and parity_dense_audit.log compare the implementations. audit.log and candidates_audit.log include direct truth-table restriction checks, exact Parseval/influence/up-transform identities and independent balanced counts. large_audit.log, balanced_audit.log, parity_v3_audit.log, gamma_audit.log and final_audit.log record high-precision checks, random attempts to break the lemmas, and direct numerical checks of the Bessel integrals.

Rare spectra require care even with arbitrary precision. symmetric.py takes log1p of exact integer differences instead of subtracting nearly equal logs. stable_log_check.log verifies both AND_2000 and parity times AND_2000 at 80 and 720 decimal digits. Positive values below binary64 range are stored in logarithmic form rather than silently reported as zero. The reported precision errors are measured in the audit logs; no extrapolation from a low-precision cancellation is used.

## Mathematical conclusions and what remains open

The optimal uniform constants satisfy

    3 <= c_A <= 3.3252155,
    2/ln 2 <= c_B <= 3.459354,
    1/ln 2 <= c_Gamma <= 8/5.

The A upper bound additionally uses the supplied H<=4.650431I theorem and Theorem 1; it is not a new direct proof for A. The lower limits follow from AND/OR and majority, with a proof and exact finite majority-law checks in PROOFS.md and majority_law_check.json.

For B the computed extremizers are mostly biased tails with small additional sign runs; they need not be monotone. For Gamma they are oscillatory across the binomial bulk, with several sign runs on a scale comparable to sqrt(n). RESULTS.md gives a paragraph and explicit witnesses for each. The exact all-dimension extremizers and the sharp constants remain open. No search beyond dimension 24 is called exhaustive over all symmetric functions.

## Files and resources

The principal deliverables are PROOFS.md, RESULTS.md, extrema.csv, the two dense JSONL tables, majority.csv, parity_family.csv, balanced_large.csv, and this report. Scripts and verification logs remain beside them. run_summary.json collects the load-bearing counts and large-dimensional values with their source data.

The dense computations ran as single-threaded C processes with GMP. The parity run records inherited nice 10; its measured maximum resident set was 1,872,035,840 bytes (1.743 GiB), below the 3 GiB limit (parity_dense.metrics.json). Its matrix allocation was sized before allocation. The worker's saved file size was 5,065,230 bytes at final audit, below the 1 GB cap (run_summary.json).

Brain recall helped: it supplied the earlier symmetric derivative-envelope method and the distinction between within-level entropy and the up-ratio B. The final new learnings are saved locally in LEARNINGS.md for the parent session. Deliverable writes stayed in this worker folder; there was no publishing, git push, mesh post, trading-stack action or shared-memory edit.

Task: “Do the brief fully and carefully” — FEIB02, started 10 Nov 2026 at 01:09 +04.
