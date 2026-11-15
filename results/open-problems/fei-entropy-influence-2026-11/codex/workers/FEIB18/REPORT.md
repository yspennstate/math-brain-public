# FEIB18 report

Part 1: PROVED. The section-11 theorem and each requested proof step stand. The unused Gaussian formula in 11(e) is FALSE. The M=0 case of 11(c) needs a non-strict inequality in one intermediate line.

Part 2: CHECKED. No proved bound failed in 18,308 exact-cube cases through dimension 16, including 15,396 rational-grid cases. There were 15,597 nonconstant cases, 686,268 fixed-correlation evaluations and 11,414 numerical stationary-root candidates. The finite scope and numerical qualifications are in RESULTS.md; these counts come from attack_summary.json.

Part 3: PROVED. PROOFS.md gives a complete mathematical section with K_0=3, M_cs=80, M=101913/100 and

    C = 3/ln(2) + 4 + 2 log2(1 + 2*101913/100) < 30.316 < 31.

The explicit concentration bound is proved with a squared-sinc kernel. No numerical Kolmogorov–Rogozin constant is assumed. constants.py supplies exact rational certificates for the final decimal bound and the required rounded constants. This validates the supplied second proof; it is not a new claim that the threshold class was previously open, or an improvement over the earlier constants cited in FLOW.

The Gaussian error is isolated. For independent centered Gaussians and a centered slab of mass delta, Cross Stay/delta^2=(1-delta)^2/2 tends to 1/2, rather than 1/pi. At half-width 0.001, verification.json gives 0.49920243388195795 versus 0.3183098861837907. Delete that illustration. The proof uses only the independently proved Cross-Stay inequality. In the two-sequence proof, replace the source's strict inequality by <= when multiplying by a possibly zero M; the lemma and constant are unchanged.

The largest observed ratios were:

| Quantity | Observed maximum |
|---|---:|
| Lemma A interval/window | 1 |
| Lemma B tail/[(1+sigma/a) window] | 0.487160987160987 |
| Cross Stay/delta^2 | 0.312466740608215 |
| Product, positive K | 0.879499851167202 |
| Product, including K=0 | 0.999969482421875 |
| L_1/Inf_1 | 2.829398713717108 bits |
| Erasure/Inf_1 | 2.796711220761027 bits |

All maxima and full extremizers are in attack_summary.json. In particular L_1/Inf_1 is attained at weights [3,2,2,2,2,2,2,2,2,2,2,1] and threshold 17/2. The positive-level product maximum is attained at 16 unit weights, threshold 5/2, K=1. These exceed the source's earlier sample records 2.73 and 0.74, without violating a theorem. The distinction between K>=1 and K>=0 matters.

The independent validator recounts extremal lemma probabilities with exact Fraction comparisons, recomputes full truth-table spectra and influences by edge counting, and applies noise by direct two-point coordinate averaging. It also checks 108 joint pair laws with exact rational probabilities and 5,000 separate two-sequence instances. Direct pair-law residuals are zero; the largest noise-identity residual in the main run is 5.551115123125783e-16. The deliberately false open-window and omitted-K=0 variants are detected, and their clean controls pass. Sources are verification.json and attack_summary.json.

The final attack ran for 32.427 seconds, with peak resident memory 103,415,808 bytes (98.625 MiB), at actual nice 10 and one numerical thread. The verification peak was 85,688,320 bytes (81.719 MiB). These are command-recorded measurements in the same JSON files. The scripts allocate no full joint cube-pair array. The folder is well below the 1 GB cap; final_audit.json records its final artifact totals.

Deliverables are REFEREE.md, PROOFS.md, RESULTS.md, LEARNINGS.md, attack.py with cube_rows.jsonl/attack_summary.json/attack.log, verify.py with verification.json/verification.log, and constants.py with constants.json/constants.log. FLOW_SNAPSHOT.md and SOURCE_SHA256.txt identify the audited source. final_audit.py/final_audit.json check file completeness, numerical provenance, row counts and resource limits.

Brain recall helped locate the exact current proof memory and confirmed that it awaited this referee. It was used as a pointer, not as proof. The math store was unavailable, and the startup slug named by its navigation view was missing. No subagents or additional model workers were started. All authored files remain in this worker folder; no publishing, mesh or shared-memory updates were made. LEARNINGS.md is ready for the launching session to incorporate selectively.

What remains open is optimization of the constants and extension of the method beyond thresholds. The continuous-rho stationary roots were searched numerically, and the finite rational grids do not exhaust all real weights; neither limitation affects the all-dimensional proof in PROOFS.md. No task item is blocked or awaiting further computation.

Task: “You are the referee of section 11” — FEIB18 brief, launch 10 November 2026 at 06:41 local (+04).
