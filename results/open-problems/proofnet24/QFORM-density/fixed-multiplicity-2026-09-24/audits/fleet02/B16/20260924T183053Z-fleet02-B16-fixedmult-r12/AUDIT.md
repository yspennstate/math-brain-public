# fleet02/B16 independent audit

Objective: QFORM-FIXED-MULTIPLICITY-AUDIT-20260924. This is one independent end-to-end B16 reconstruction, not release status and not a claim about the unrestricted three-eigenvalue conjecture.

## Exact source pins

Historical 17 baseline: source commit 7c0d6e60946b19423e6400a12d34b473cf0591e2; manuscript git blob 183ccd294763214e6a707e8d4749ff9a8cf7006d; package-recorded SHA-256 9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69.

Latest 9/400 source: source commit eeb752c8943536541b34b42b8bf48e924f4d3d2f; paper git blob 19fb119877426b640b2c0dae19ec2f78a399fe11; package-recorded SHA-256 bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3.

Separate 9 reconstruction: source commit d3b12e27dc682a7fac0aa7edc1bd70de59cba8b1; paper git blob 823201f05363fcc60c38cce0feb5abb636f081d7; manifest SHA-256 ea56bc35cff9815db71a9f5a620e0160e3a39cf53ff60c789707294d53240eba.

The git blobs were fetched at the pinned commits. The SHA-256 values are package-recorded and were not independently recomputed in this connector-only run.

I read all 790 baseline source lines, all 955 latest-nine source lines, all 710 mathematical lines plus terminal newline of the separate-nine source, and the requested support packages.

## Line ledger

| Source/range | Status | Independent finding |
|---|---|---|
| baseline 1-435 | PASS | theorem quantifiers; Fourier/Riesz; singular-value/Schur; BL/projections; decoupling/determinant; square and definite pair checked |
| baseline 436-482 | GAP_REPAIRABLE_LOCAL | hyperbolic proof chooses an original coordinate large for the positive exponential vector and reuses it for the negative vector; equal vector norms do not make the same coordinate large |
| baseline 484-790 | PASS after repair | concentration; sampling/completion; spectral-to-volume; kernels; pivot assembly; scaling |
| latest-nine 1-562 | PASS | includes grouped mollified-L2 compiler, finite-measure weighted Holder/entropy, literal-row promotion; no projected independence used |
| latest-nine 563-608 | GAP_REPAIRABLE_LOCAL | same hyperbolic two-tail coordinate issue |
| latest-nine 610-921 | PASS after repair | concentration, separate pivots, exact rank margins, full pair half-potential, theorem assembly, overlap-tail theorem |
| latest-nine 923-955 | PASS / novelty UNCHECKED | limitations accurate; exhaustive priority not checked |
| separate-nine 1-439 | PASS | independent compiler and structural reconstruction checked |
| separate-nine 440-467 | GAP_REPAIRABLE_LOCAL | same two-tail coordinate issue |
| separate-nine 469-710 | PASS after repair | concentration, pair half-potential, minor interpolation, theorem assembly |

## Exact local repair

On a hyperbola branch write w(t)=u exp(t)+v exp(-t), with |u|=|v|. Choose i_plus with |u_i_plus| at least |u|/sqrt(2) for the positive tail and, independently, i_minus with |v_i_minus| at least |v|/sqrt(2) for the negative tail. Run the same one-coordinate monotonicity/change-of-variable estimate separately. The cutoff bounds and constants are unchanged because |u|=|v|. No downstream step requires i_plus=i_minus.

Thus the literal source files are GAP_REPAIRABLE_LOCAL, while the 17- and 9-eigenvalue theorem chains pass after this repair. I found no FALSE mathematical statement.

## Package findings

The root baseline verify.py is source-bound: it reads manuscript.tex and checks the pinned SHA before finite tests. Its supplied checks.json is consistent with the inspected code. Fresh execution is UNCHECKED.

The latest-nine verify_new.py has a reproducibility GAP: it does not read/hash paper.tex against the pinned SHA, so it can emit PASS after source changes. This is not a proof defect because this audit is against the pinned git blob. Repair: bind the checker to the paper SHA or label it source-detached diagnostics. Fresh checker execution, PDF rendering, and Lean compilation are UNCHECKED in this run.

## Dependency graph actually checked

Fourier/Gaussian/Riesz -> heat-flow BL -> product projections/Fourier powers -> literal decoupling -> grouped mollified L2 + weighted Holder/entropy -> row promotion -> crossing-volume density/half-potential.

Volume sampling -> nonsymmetric completion -> global/restricted rank -> spectral-to-volume -> physical cut.

Square/definite/repaired-hyperbolic pivots -> log and half-potential estimates -> five-direction half-potential -> nine-direction theorem.

Imported only as non-proof metadata: package build/render claims, finite-test execution claims, Lean execution claims, literature priority.

## Verdict

FALSE: none found.
GAP: the local hyperbolic negative-tail coordinate selection above, repaired without changing constants.
UNCHECKED: fresh checker/PDF/Lean execution and exhaustive novelty.
Impact: no theorem failure after repair; the literal source should not be called gap-free until amended.
Next obligation: any threshold below nine needs a complete source-preserving replacement proof with explicit constants and dependencies.
