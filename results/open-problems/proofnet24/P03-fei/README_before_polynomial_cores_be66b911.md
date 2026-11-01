# FEI research: current recovery and continuation

**Full Friedgut–Kalai Fourier entropy–influence conjecture: OPEN.** Last owner-requested research update: 20 September 2026. The newest owner-requested positive continuation proves sharp affine-fibre gluing and a quadratic tag-phase extension. The preceding quadratic-symmetry theorem, Han-overlap obstruction and all earlier research records are retained below. None proves unrestricted FEI.

## Latest owner continuation: sharp affine-fibre gluing

Read the [complete proof](continuations/2026-09-20-affine-fibres/REPORT.md), [handoff and endpoint budget clarification](continuations/2026-09-20-affine-fibres/HANDOFF.md), [exact checker](continuations/2026-09-20-affine-fibres/verify_affine_fibres.py), and [actual output](continuations/2026-09-20-affine-fibres/verification.json).

For existing physical coordinates `(x,y)`, a label map `pi(y)` whose nonempty fibres are affine subspaces, any Boolean `g(y)`, and a quadratic `Q(x)`, set `F_Q=(-1)^{Q(x)+x dot pi(y)}g(y)`. If every section of each fibre parallel to its tangent physical coordinate axes satisfies `H<=C J`, then

    H(F_Q) <= max{4,C} J(F_Q) <= max{4,C} I(F_Q).

The proof uses an exact affine-fibre entropy identity and a half-disagreement payment on physical edges crossing distinct labels. The constant does not grow with cell number, affine geometry, recursive gluing depth, or quadratic tag rank. Intrinsically quadratic cell phases give the sharp class constant four; standard addressing functions show sharpness. Previously certified quadratic-twisted symmetric sections retain 12.04. Disjoint products and zero-cost isospectral splices can be interleaved without worsening that constant.

This does not cover arbitrary Boolean functions. Adding fresh tags to an arbitrary function does not transfer the bound back to it. Fixing tags can merge labels and destroy the hypotheses. Arbitrary mixed quadratic twisting is not asserted to preserve affine fibres. The explicit local certificates must not be removed. These are direct stopping-class certificates, not a universal hereditary allocation theorem.

The same continuation proves that a coefficientwise attempted payment for the dimension-adaptive endpoint potential fails: one Boolean-realizable fibre has charge/minority-mass ratio `n+3/2-2 ln 2+o(1)`. The handoff gives the exact aggregate calculation showing why the full one-point-defect charge/influence still tends to two. This does NOT refute the surviving whole-function endpoint selector. A shared budget between spectral fibres remains necessary for that proof route.

Actual checks passed: 233,530 structured affine-partition/quadratic-cell cases, 700,392 associated physical-coordinate cases, 240 arbitrary-core cases with 3,275 sections, 240 quadratic-tag cases and 240 quadratic-cell/tag cases. These finite families overlap and are not unrestricted Boolean coverage. The code uses integer Walsh transforms, exact rational influence, symbolic logarithm cancellation and outward rational logarithm bounds. Its committed bytes were checked and replay produced byte-identical output. Independent review and publication-priority clearance are not claimed.

Proof commit: `86b5c86b7856e702149f5c0dff1d4bf2bf2105c2`; checker: `80bd8b83f28f6ce5950fa866e90ca85aa4e93e9d`; output: `491a657a03746be4b07de9da72fc0f4687249599`; handoff: `db5befea95c99a72da10db6f5e84c357ce738435`. The missing full-scope step remains a dimension-free allocation for arbitrary dependent restriction branches or a whole-function endpoint selector. No schedules, permissions, visibility settings, or unrelated work were changed.

## Previous positive continuation: arbitrary quadratic twists of symmetric cores

Read the [complete proof](continuations/2026-09-20-quadratic-symmetry/REPORT.md), [research worklog and attempted routes](continuations/2026-09-20-quadratic-symmetry/WORKLOG.md), [worker handoff](continuations/2026-09-20-quadratic-symmetry/HANDOFF.md), [exact checker](continuations/2026-09-20-quadratic-symmetry/verify_quadratic_symmetry.py), and [actual output](continuations/2026-09-20-quadratic-symmetry/verification.json).

For any d-part-symmetric Boolean h and ANY quadratic Q on the same variables, the new proof establishes

    H((-1)^Q h) <= (12.04 + log_2 d) J((-1)^Q h) <= (12.04 + log_2 d) I((-1)^Q h).

For a product of independently supported cores h_t, the constant uses the MAXIMUM number of symmetry parts in one core, not the total number of cores. In particular, products of arbitrarily many symmetric Boolean functions, with unrestricted quadratic interactions within and between their blocks, have the single constant 12.04. There is no fresh-control, low-density, quadratic-rank, or bounded-degree hypothesis on the symmetric cores. Their physical coordinate groups must remain disjoint in the product theorem; arbitrary overlapping high-degree cores and arbitrary input-affine mixing are not covered.

The new payment is j_i>=1/4 for quadratic rows mixing a symmetry part, and j_i=1/2 for rows meeting another independently supported core. Removing those coordinates restores a character times a product of part-symmetric functions. Physical deletion costs at most two entropy bits per coordinate; average remaining folded influence cannot increase. The published O'Donnell–Wright–Zhou theorem supplies the leaf constant, unchanged by the new argument. Its original symmetric result and constant are explicitly credited, and publication priority for the extension is not cleared.

The report also proves the universal pair budget j_i(h)+j_i((-1)^Q h)>=1/2 on every nonzero quadratic row, and a low-folded-influence transfer criterion with explicit leaf-certificate assumptions. Those assumptions are not an unrestricted theorem. A rare higher-degree monomial shows why simply counting nonsymmetric coordinates cannot extend the quarter-influence payment to arbitrary phases.

Actual exact checks: 67,732 symmetric-core/graph cases through dimension five; 29,896 partition/core/graph/linear cases through dimension three; 840 sampled product cases through dimension ten; 108,506 graph-structure checks; 171,150 physical restriction leaf tables; and 4,640 universal pair coordinate checks. All passed. The families overlap and are not exhaustive unrestricted Boolean coverage. Logarithms are rationally enclosed, with exact cancellation for an entropy-deletion equality. The exploratory floating-point search and its original witness output are separately preserved and labeled.

Proof commit: `6cc02bb1fc64bb20a99c5a878d4bc27c8dc6bf56`; checker commit: `c48bcf31b0599d23c534c4a8eda4aa259dcd2d8b`; output commit: `094a855a659a95f9e6fc7f518f303ff53347642a`. Report blob `11605492453c978a7cb45261eb563d006fee2db0`, checker blob `1df3886613c255c4c75502050b2d3b2300945ace`, and output blob `b7638c92126e34529f42af4cc2b82acdfe43db3e` were checked against local bytes. The exact committed checker was replayed and produced byte-identical verification output.

This is an additional certified stopping class for the hereditary entropy program, not its missing universal allocation bound. The earlier constant-four affine-clause results retain their stronger constants on their stated classes. No schedules, ownership, or native atlas metrics were changed. Delivery is not evidence that a later worker has already read these files.

The [complete preceding index](README_before_2026-09-20-shifted-thresholds.md) is preserved byte-for-byte, using original Git blob `5a092c58a61ec79413646405c4cb7dafb8457199`. Its relative links still work. Its historical claims about which drift coefficients have been refuted must be read with the separate recovery warning below. Existing research reports, checkers, ownership, schedules and native finite-dimensional metrics are unchanged.

## Current result: Han's all-coordinate overlap criterion is false

Read the [worker handoff](handoffs/2026-09-20__shifted-thresholds-refute-han.md), [complete analytical proof](continuations/2026-09-20-shifted-thresholds/REPORT.md), [exact integer checker](continuations/2026-09-20-shifted-thresholds/verify_threshold_obstruction.py), and [actual output](continuations/2026-09-20-shifted-thresholds/verification.json).

For m>=2, n=m^2+1 and f_m(x)=sgn(sum_j x_j-m), put

    O_i(f)=sum_{S not containing i} |fhat(S) fhat(S+i)|.

The new theorem proves, for every coordinate,

    O_i(f_m)/I_i(f_m) >= (1/(2 pi^2)) ln(n) - C_0,
    I_i(f_m)=2^(-m^2) binom(m^2,(m^2-m)/2)>0.

All coordinates are equivalent. Hence no finite universal C allows every Boolean function to select a coordinate satisfying O_i<=C I_i. This is a negative answer to Xiao Han, Combinatorica 45:4 (2025), Question 3.1. A different coordinate cannot repair the example. The functions are fully symmetric monotone thresholds, and the published O'Donnell–Wright–Zhou theorem already gives H<=12.04 I for them. This is an obstruction to the stronger proposed proof criterion, **not a counterexample to FEI**. The lower logarithmic coefficient is not claimed sharp.

The complete proof uses exact Krawtchouk slice coefficients, a self-contained Hermite ODE asymptotic, harmonic divergence of adjacent absolute products, and a quantitative comparison through degree floor((n-1)^(1/4)). The growing-degree comparison is essential for the logarithmic-in-dimension estimate. The qualitative divergence persists for every fixed nonzero Gaussian threshold shift; exact balance and uniformity as the shift tends to zero are not claimed.

Actual checks: all 55 nonconstant symmetric thresholds in dimensions 1--10 were compared against complete integer Walsh transforms, each coordinate separately; Parseval and influence identities were checked. Exact rational intervals were computed through dimension 4097. The 32-variable witness has ratio 2314378859/1073741824>2 at every coordinate. Finite tests do not replace the all-dimensional proof. Independent review, comprehensive priority clearance and Lean formalization are outstanding.

Proof commit: `23a638dd764b093bbc16b405c0d577d941d5aba4`; checker: `ebd84a64906f22c4e989a9e2873acf69920e7367`; output: `a80ffd25adb73d48ebe22e9998b5054ca4d30d30`. Report blob `6b092f3b051e2fc6b085a99905866e1c2c41d9bc` and checker blob `5d889fdabcd00c6341914cf5e90de5f540a6e7af` were read back and match the local files.

## Preserve the entropy-weighted target, not the failed absolute majorant

For p_S=fhat(S)^2 define

    K(f)=sum_{cube edges {S,T}} min(p_S,p_T) |log_2(p_S/p_T)|,
    B(f)=sum_i H(S_i | S_{-i}).

The universal estimate K(f)<=C I(f), with C independent of dimension and f, remains **UNPROVED**. So does the equivalent-at-the-level-of-finite-constants universal/hereditary erasure route. The new threshold family does not refute these targets: K<=B<=H<=12.04 I on that family, while the summed absolute overlap divided by I diverges.

Read [the exact erasure reduction](solo-2026-09-17/ERASURE_REDUCTION.md) and [the corrected frozen-session handoff](handoffs/2026-09-19__FROZEN_SESSION_RECOVERY.md). Do not use the false pointwise shortcut H(f)<=B(f)+(2/ln2)I(f). The valid implication quantifies B/I over all Boolean functions or the appropriate physical restrictions. Do not count restating this implication as new progress or FEI closure.

## Separate recovered prior work: all-constant affine-drift warning

Read [the recovery notice with exact source identity and limitations](continuations/2026-09-20-shifted-thresholds/RECOVERED_STATUS.md). The Library file `FEI_Sharp_Stability_and_Drift_2026-09-19.patch` was recovered. Its Section 1--9 majority argument bounds Delta_M=2M-E M(f f^z) by an absolute constant while D_cross=2H-E H(f f^z) diverges. This extends the older coefficient-four obstruction to every fixed coefficient and supersedes the historical index's statement that other coefficients were not refuted. The valid D_cross<=6M theorem is unaffected.

**Delivery scope:** the recovery notice is in this repository; the entire 352937-byte raw patch is not uploaded here by this continuation. Its original bytes are preserved in the conversation backup. The sharper limits, fixed-depth/stopping claims and stability results in that prior package must be retrieved and reconstructed before use; they were not independently audited or all replayed in this continuation. The new Han-overlap theorem does not depend on those recovered results.

## Retain the earlier positive results with their hypotheses

The [rare-control report](continuations/2026-09-19-rare-controls/REPORT.md) proves the stated affine entropy-excess contraction for fresh independent controls and arbitrary quadratic coupling. Its constant-below-five generated class requires certified seeds; a contracted positive unknown excess is not made nonpositive. The [quadratic-coupling report](continuations/2026-09-19-quadratic-coupling/REPORT.md) retains the jointly independent-clause/cubic-core hypotheses. Neither is unrestricted FEI.

The [balanced-substitution report](continuations/2026-09-19-balanced-substitution/REPORT.md) retires the all-constant full-resolvent pointwise target and preserves the conditional-entropy identities and valid discounted budgets. The [preceding full index](README_before_2026-09-20-shifted-thresholds.md) links every earlier correction, proof and checker, including the scalar-budget, coding, boundary-decomposition and affine-variance work.

## Continuing workers

Fetch this entrypoint from current master, then read the full reports actually used. Record actual source paths/blob hashes, reused hypotheses, superseded targets checked, new mathematical delta, executed checks and remaining full-scope gap inside each substantive report. Do not revive the absolute-overlap criterion, the retired resolvent inequalities, or a fixed-coefficient affine-drift payment. Preserve valid earlier statements. Repository delivery alone does not demonstrate subsequent worker uptake.
