# FEI research: current recovery and continuation

## New continuation: shared rare controls and affine entropy-excess contraction

Read [the rare-control handoff](handoffs/2026-09-19__rare-controls-excess.md), [complete proof report](continuations/2026-09-19-rare-controls/REPORT.md), [exact checker](continuations/2026-09-19-rare-controls/verify_rare_controls.py), [included dependency](continuations/2026-09-19-rare-controls/prior_exact_entropy.py), and [actual output](continuations/2026-09-19-rare-controls/verification.json). The research package was merged to master in `8e3fa19aaaf89061d8a82f96aafa515f5d35e211`, preserving concurrent worker commits. Full FEI remains OPEN.

For Phi_C=H-C M and Gamma_c f(z,y)=1-1{z=0}(1-f(y)), the report proves `Phi_C((-1)^Q Gamma_c f)<=2^(-c)Phi_C(f)` for EVERY Boolean f, c>=4 fresh independent bits, arbitrary quadratic Q on all old/new variables, and C>=17/4+1/(2 ln2)<5. From certified seeds this gives a depth-independent constant-below-five FEI class with high-degree terms sharing control blocks, arbitrary quadratic coupling at each controlled stage, disjoint products, and surjective affine changes. The operation adds variables and is NOT a transition in the fixed-domain multiplicative-derivative chain. A positive unknown seed excess is not proved nonpositive by contracting it. Do not drop freshness or seed certification.

The independent rank theorem applies to EVERY Boolean base g of negative density delta<=1/8, with no degree or internal factorization hypothesis: `M(g(-1)^Q)>=M(g)+(1/2-4delta)rank(B_Q)`, while the entropy changes by at most that rank. Its coefficient is sharp on one-point bases. For delta<=1/16, quadratic twisting cannot increase H-CM when C>=4. Exact controlled influence uses the UNFOLDED basis minimum M_0, not M: `M(Gamma_c f)=2^(-c)[M_0(f)+c(1-Ef)]`. The report also proves explicit bounds for unstructured exponentially rare errors around quadratic phases and explains why a fixed rare gate around unrestricted unknown seeds still preserves the full FEI difficulty.

## Active hourly task alignment — stale targets removed

The existing hourly `FEI proof continuation` task (`6aaec3d268808191814212175ff425aa`) was successfully updated on 19 September 2026, with its enabled hourly cadence retained and no new task created. Its stale prompt describing the already-refuted full-resolvent estimate as live was replaced. Its current instructions require current-master reads, full proofs, actual blob hashes, `superseded_targets_checked`, exact reused hypotheses, and substantive new mathematics rather than repeated unchanged certificates. This current correction supersedes older prompt excerpts in the historical scheduled contract.

Both all-constant resolvent targets remain retired; the resource potential M<=a v+b delta_M is refuted for all fixed nonnegative coefficients; the entropy potential with coefficient FOUR is refuted, but all possible entropy-drift constants have NOT been refuted. Retain the valid D_cross<=6M and earlier payments. Future reports must explicitly record which new files were consumed and how their actual research plan changed. No post-update consumption is asserted merely from successful configuration or delivery. The latest inspected committed run was the older 18:46:55Z report; later progress requires an actual newer report.

## Current positive continuation: arbitrary quadratic coupling and cubic cores

Read [the new handoff](handoffs/2026-09-19__quadratic-coupling-positive-results.md), [complete theorem and proofs](continuations/2026-09-19-quadratic-coupling/REPORT.md), [exact checker](continuations/2026-09-19-quadratic-coupling/verify_quadratic_coupling.py), [included dependency](continuations/2026-09-19-quadratic-coupling/prior_exact_entropy.py), and [actual output](continuations/2026-09-19-quadratic-coupling/verification.json). The full research package was committed as `d7aca6265040d979c623b70a4bd813b0b1a336bb`.

The positive theorem is `H(F)<=4 Ifrak(F)<=4J(F)<=4I(F)` for jointly independent affine one-point clauses with ARBITRARY quadratic coupling on the same variables. It also permits an arbitrary independent cubic core coupled quadratically to every clause/free coordinate. Constant four is sharp over the stated class. A bounded-degree-d core gives constant 2^(d-1), not a uniform constant as d grows. The proof conserves Fourier-coset masses and bounds the additional affine influence by the appropriate polar rank. Jointly dependent higher-degree clauses and cubic terms sharing the wide-clause parameters remain outside the hypotheses. Full FEI remains OPEN.

## Current correction: two scheduled affine potentials are false

The scheduled report below was read and its new proposals were tested. Read [the exact response](continuations/2026-09-19-quadratic-coupling/SCHEDULED_POTENTIAL_CHECK.md), [checker](continuations/2026-09-19-quadratic-coupling/check_scheduled_potentials.py), and [output](continuations/2026-09-19-quadratic-coupling/scheduled_potential_checks.json).

Writing M=Ifrak, v=1-max Fourier mass, and delta=2M-E M(f_z): `M<=C(v+delta)` fails for EVERY fixed C on one-point defects. Coefficient one already fails on five variables by 13/256. The proposed `D_cross<=4(v+delta)` fails on the 66-variable product w_3 tensor power 22, with a rigorously positive gap greater than 0.044368942168. No 2^66 truth table was enumerated; exact seed checks and proved tensor identities give the certificate. Adding a bounded mode-defect term cannot repair a universal additive drift bound after tensor amplification. This does NOT refute all possible entropy-drift coefficients, and neither example refutes FEI.

Preserve the worker's universal D_cross<=6 Ifrak theorem and all earlier valid payments. Do not keep trying its false resource potential or coefficient-four entropy potential because an older prompt labels them UNPROVED. The independent constant-four coupled-class theorem does not rely on those candidates. Current-master readers should record this correction and the exact source blobs they use; successful delivery is not proof of subsequent worker uptake. No schedules, ownership, visibility, or native finite-dimensional metrics were changed.

## Scheduled mathematical result preserved: universal affine one-step bound

Read [the affine one-step handoff](handoffs/2026-09-19__affine-one-step-bound.md), [the complete scheduled run report](scheduled-continuation/runs/2026-09-19/2026-09-19T18-46-55Z__report.md), [self-contained checker](scheduled-continuation/artifacts/2026-09-19T18-46-55Z/check_affine_onestep.py), and [recorded output](scheduled-continuation/artifacts/2026-09-19T18-46-55Z/verification.json).

The all-dimensional auxiliary theorem is `D_cross(f) <= 6 Ifrak(f)`, where `Ifrak` is minimum total influence under invertible binary input changes and character multiplication. This does **not** close FEI: on one-point defects the discounted derivative-chain sum of `Ifrak` is an unbounded factor larger than its initial value. Its two stronger potential proposals survived the reported dimension-at-most-three tests but have since been refuted as specified in the current correction above. The original report is preserved rather than silently rewritten.

## Delivered positive continuation: affine variance and constant-four class

Read [the affine-variance handoff](handoffs/2026-09-19__affine-variance-positive-results.md), [full proof report](continuations/2026-09-19-affine-variance/REPORT.md), [checker](continuations/2026-09-19-affine-variance/verify_affine_variance.py), [included dependency](continuations/2026-09-19-affine-variance/prior_exact_entropy.py), and [recorded output](continuations/2026-09-19-affine-variance/verification.json). The [delivery recovery record](continuations/2026-09-19-affine-variance/DELIVERY_RECOVERY.md) identifies the exact source bytes and successful replay. Failed-upload statements inside the original report and handoff refer to their creator session; the package is now included in the same commit as this index entry.

The saved report gives a sharp universal accumulated-variance bound V<=2I, exact tensorization and a monotone formula for minimum affine influence, and H<=4J for the specified product class after jointly surjective affine mixing. Its allocation chain satisfies T<=8J on that class. These are not unrestricted FEI, independent audits, or a novelty clearance. Joint surjectivity cannot be dropped, and variance alone does not bound general allocation entropy.

Scheduled continuations must read this complete report and retain its hypotheses, consult newer neighboring reports, and record actual paths/blob hashes consumed and substantive mathematical changes. Build on the stated positive results without reviving the disproved scalar or full-resolvent estimates below. Repository availability does not prove that a scheduled run has already consumed the files. Existing schedules, ownership and native metrics are unchanged.

**Owner-requested update, 19 September 2026. Full FEI: PARTIAL, not solved.**

This entry point preserves the frozen-session state and links the substantive continuation. Existing FEI material remains in place. It does not change a native worker's current assignment, undo a rotation, reset the finite-dimension atlas, or certify that a scheduled worker has already consumed these files.

## Latest mathematical correction — the full-resolvent pointwise estimate is also false

Read [the new handoff](handoffs/2026-09-19__balanced-substitution-refutes-resolvent.md), [complete proof](continuations/2026-09-19-balanced-substitution/REPORT.md), [executed checker](continuations/2026-09-19-balanced-substitution/verify_next_step.py), and [actual output](continuations/2026-09-19-balanced-substitution/verification.json) before reusing the earlier next-step target.

The previously unproved candidate `D_cross <= K(C+Q_log)` is **disproved for every finite K**, even for balanced monotone transitive Boolean functions. An explicit majority-of-recursive-majorities family has C tending to four, Q_log tending to zero, and D_cross bounded below by a divergent harmonic sum. Its H/I tends to four, so this is NOT a counterexample to FEI. The same obstruction defeats every fixed finite logarithmic power on the squared marginals.

Positive continuation results: exact pivotal-resolvent and allocation-entropy substitution identities; the unconditional bound `A <= D_cross <= 2A+(4+2/ln2)Q_log`; and the uniform pointwise theorem `D_cross <= (3/2)C+(4+2/ln2)Q_log` for read-once ternary-majority formulas, including unequal depths. The subclass is not asserted to be closed under multiplicative differentiation, and known FEI results for bounded-arity formulas are not reclassified as new.

Here `A=H(S | S triangle T, S intersection T)` for independent spectral samples. Its accumulated derivative-chain quantity T satisfies `T/2 <= H <= T+(5+5/(2ln2))J`; a uniform bound on T/J remains UNPROVED and is equivalent at the level of universal constants to FEI. Do not present that reformulation as a solution. The hereditary erasure route remains live. Preserve the earlier valid packet and discounted-budget results; only the indicated pointwise candidate is refuted.

## Scheduled uptake and continuation — owner update

[Scheduled continuation contract](scheduled-continuation/README.md) records the new hourly **FEI proof continuation** task accepted on 19 September 2026. The existing P03 task rejected edits from this session and was left unchanged. This is one additional linked research continuation, not a claim that every worker's prompt was modified.

The new task must fetch this index from current master, read the latest full proof report and checks, critically reconstruct the steps it relies on, and build on the newest FEI reports. Each substantive report must record `consumed_updates` with actual path/blob SHA/sections read, `reused_results` with hypotheses, `new_mathematical_delta`, `actual_checks`, and `remaining_full_scope_gap`. Put these receipts inside the research report, not in separate acknowledgement-only commits. New reports belong under `scheduled-continuation/runs/`; relevant existing workers should consult them to avoid duplicating work. The current correction above supersedes the historical description of the full-resolvent inequality as merely unproved; do not keep attacking that false pointwise statement because it appears in an older prompt or handoff.

The core files below are available in GitHub independently of expired chat attachments. Configuration and file availability do not establish completed execution, reading, or mathematical progress; those require an actual report. No source-closure or model/effort guarantee follows from this deployment.

## Earlier scalar-budget continuation — retain its proofs and corrected scope

[Earlier handoff](handoffs/2026-09-19__coded-budget-obstruction.md) and [complete proof report](continuations/2026-09-19-coded-budget/REPORT.md), with [executed rational verifier](continuations/2026-09-19-coded-budget/verify_continuation.py) and [output](continuations/2026-09-19-coded-budget/verification.json).

The candidate `D_cross <= K(R+Q_log)` from `continuation-2026-09-19/RESEARCH_NOTE.md` is **disproved for every constant K**. The best scalar-budget constant in dimension n is at least `n/[40(log_2 n)^3]` for n>=2040. An explicit 2,040-variable example has certified ratio greater than 13.716; this is a proof-method obstruction, NOT an FEI counterexample.

Positive additions in that earlier report: an entropy-stable code-separated spectral-product theorem, direct discounted bounds for R and Q_log, and an explicit discounted full-pivotal-resolvent bound below 16J. The full resolvent C survived that particular coded counterexample, and the report proposed `D_cross <= K(C+Q_log)` as a sufficient next step. The balanced-substitution continuation above now refutes that next step for every finite K; it does not contradict the discounted bounds. The report credits the older September 13 resolvent-payment and conjunction arguments; it does not present them as newly discovered or claim an exhaustive reread of the archive.

Full FEI and the universal erasure inequality remain open. Preserve the distinct recovery/partition work below and the native worker metric.

## Earlier recovery and partition work

1. [Frozen-session recovery](handoffs/2026-09-19__FROZEN_SESSION_RECOVERY.md): actual recoverable state, existing proofs, and the correction to the false pointwise erasure inequality.
2. [Continuation with proofs](continuations/2026-09-19-recovery/CONTINUATION.md): collision-free orthogonal-support patching, every-sublinear-scale coding hardness, a positive spectral-separation bound, and the signed entropy-excess identity.
3. [Boundary-decomposition obstruction](continuations/2026-09-19-recovery/BOUNDARY_OBSTRUCTION.md): an explicit 27-variable ternary NAND function has H/I>4.4265. Therefore a universal boundary-separated signed-subcube-parity decomposition is FALSE, not a missing theorem to attempt again.
4. [Dated run report and ledger delta](runs/2026-09-19/2026-09-19T16-28-42Z__OWNER_FEI_RECOVERY_CONTINUATION.md): before/after changes, scope and continuation priorities.

## What the next FEI worker should change

For boundary-separated signed-subcube-parity pieces, replace the old H<=4 Lambda I_x estimate by H<=4 I_x. The stronger bound is an application of the published tensor/typical-support partition method; do not claim that method as new. The bound holds with arbitrary repeated labels and does not assume flat incoherent mixtures.

Do not attempt to prove that every Boolean function has such a zero-debt representation. The NAND certificate rules it out. The live extension is a paid artificial-boundary cost, more general cells with controlled local Fourier complexity, or global signed cancellation.

The systematic-code obstruction now covers every prescribed sublinear erasure profile k_D=o(D), not only o(D/log D). Even simultaneous vanishing of all those spectral-block conditional entropies retains the unrestricted worst FEI ratio. Physical restriction does not preserve that separation, so the correctly quantified hereditary erasure argument is not contradicted.

The old direct logarithmic target K(f)<=C I(f) remains open. Do not reinstate H(f)<=B(f)+(2/ln 2)I(f) pointwise; the recovery handoff identifies the counterexample and the correct quantifiers.

## Reproducibility

In `continuations/2026-09-19-quadratic-coupling/`, run `python verify_quadratic_coupling.py --output verification.json` and `python check_scheduled_potentials.py`. Both exact checkers have been executed; the separate exploratory drift probe is labeled floating-point evidence only. Full FEI, independent audit, Lean verification, and novelty clearance are not claimed.

In `continuations/2026-09-19-balanced-substitution/`, run `python3 verify_next_step.py --part all --output verification.json`. The recorded self-checks include 1,850 rationally certified entropy comparisons, exact substitution identities, and the proof-based symbolic witness. No huge-dimensional truth table was or Lean proof was executed.

In `continuations/2026-09-19-recovery/`, run:

```sh
python3 check_recovery.py > checks.json
python3 check_boundary_obstruction.py > boundary_checks.json
```

Both earlier programs use only the standard library. The first checks 404 Boolean functions, 3205 atom inequalities, two exact code lifts and their 415 small erasure blocks, plus structured examples. The second certifies the explicit 27-variable function by exact product/complement recurrences, without exhaustive enumeration.

All acceptance comparisons use rational arithmetic and rational logarithm enclosures. The numerical `lower`/`upper` fields in the earlier recovery's `checks.json` are rounded display values, not outward-decimal endpoint certificates; `boundary_checks.json` supplies explicitly outward-rounded decimal endpoints. JSON whitespace may differ when regenerated; compare parsed values.

Independent audits, comprehensive novelty review and full FEI closure have not been completed. No email, public posting, new schedule or force-push was performed for the earlier recovery or balanced-substitution continuation. The separately accepted hourly continuation is recorded in the scheduled contract above.