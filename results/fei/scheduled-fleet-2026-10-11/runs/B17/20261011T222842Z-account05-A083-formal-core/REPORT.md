# exact target, quantifiers, hypotheses and units

A083, stream B17, run 20261011T222842Z-account05-A083-formal-core. Target: remove the signed interval-division risk identified in the B09 exact logarithm certificate. For all rational a,b,c,d,x,y with 0<c, c<=y<=d and a<=x<=b, x/y lies between the minimum and maximum of the four corner quotients a/c,a/d,b/c,b/d. No dimension, Boolean-function or entropy-unit hypothesis enters this arithmetic lemma. The FEI target remains all Boolean functions in all dimensions, Shannon entropy in bits, with one absolute constant; this run supplies no bound on that constant.

# sources actually read, revisions and theorem locators

Read EXECUTION_PROTOCOL.json completely, revision 2026-10-11-execution-v2, and campaign README, CURRENT_STATUS, CLAIM_REGISTRY, OBSTRUCTION_REGISTRY, PACKET_STATUS, STREAM_NEXT_ACTIONS and the plan TeX. Assignment acceptance tests are plan lines 1036-1040. Read supplement CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and NATIVE_MAPPING and its twelve source notes. Read the four specified current/earlier paper text files and available original run reports. out/source_inventory.json contains 37 source-byte hashes, 1,934,580 bytes in total; out/source_reading.txt records relevant line excerpts. Source loading and focused inspection do not constitute independent acceptance of every paper theorem.

The relevant original source is verification/B09_interval_repair_20261011/REPORT.md, sections Defect and Why the repaired calculation is rigorous; CHECK.py is preserved in the shared read-only source. Its registry pin is a1ff93577685acd461b154b04e0c1aa0c65645c8. It corrects the original B09 run at adb671ffcda143fa68347806bb96e8c305621a7d. The repair reports a certified fixed margin J_A-M_A>1195/10000 bits; this run does not reproduce or extend that margin. A081's local REPORT.md and independent_interval.py were inspected: they already independently reconstruct it by dyadic range reduction. Thus repeating that numerical baseline would not advance this packet.

Threshold interfaces remain scoped: current Proposition 5.5 retains complete whole-set witness costs; composition identities do not permit unpaid shared-support interference. Percolation Theorems 1.1 and 1.3 concern their stated lattice crossing classes and discrete singularity, not all Boolean functions. Earlier versions are separate source hashes, not interchangeable hypotheses. BOARD.md was read at stage start; B17/STREAM_NOTES.md was absent, so no lead-specific universal target was available.

# complete derivation or exact first unsupported line

For positive rationals c<=d, inversion reverses order. Multiply c<=d by positive 1/c to get 1<=(1/c)d, then cancel the positive factor d to conclude 1/d<=1/c. Multiplication by a nonnegative x preserves this order, hence x/d<=x/c. Multiplication by negative x reverses it; the proof obtains this by negating x and then negating the resulting quotient inequality. For each fixed positive y, a<=x<=b implies a/y<=x/y<=b/y.

Split on the sign of x. If x>=0, then a/d<=x/d<=x/y<=x/c<=b/c. If x<=0, then a/c<=x/c<=x/y<=x/d<=b/d. The minimum of all four corners is below either lower bound and the maximum is above either upper bound. `positive_denominator_enclosure` checks the two-case proof; `four_corner_enclosure` instantiates its bounds with nested min/max. Closed regression propositions check that the old rule reverses endpoints on [-1,-1]/[1,2], and that the correct corners for [-2,-1]/[1,2] give [-2,-1/2].

The successful formal artifact is code/RationalDivision.lean. Earlier Mathlib ordered-field drafts are retained as unchecked attempts. No theorem relies on them. The rational statement has no unproved line when the saved compiler output is PASS and its axiom list excludes sorryAx. The real-number extension is outside the formal scope: the same ordered-field argument applies over the reals, or one passes from rational approximants inside the closed intervals using quotient continuity on y>=c>0. Applying this to ln(x)/ln(2) still requires independently proved real logarithm enclosures and strictly positive ln(2) bounds.

# executed validation with domain, arithmetic, commands and outputs

Frozen specification: out/FROZEN_SPEC.json. This is one universal rational interval theorem, one auxiliary interface and two concrete kernel-decided regressions, rather than a finite Boolean search. Arithmetic is Lean's exact Rat arithmetic. Compiler is the installed Lean 4.33.1 executable; only Init.Data.Rat.Lemmas is imported. Final compiler exit was 0 in 2.431 seconds, with 530,251,776 bytes peak process commit. All four printed propositions depend only on propext, Classical.choice and Quot.sound; out/LEAN_CHECK.txt contains no sorryAx. The finalizer rejects errors and sorryAx before writing final claims. It does not use native_decide or add target axioms.

Commands from the agent folder:

```text
python -X utf8 runs/20261011T222842Z-account05-A083-formal-core/code/read_sources.py
python -X utf8 ~/brain_workers/FEI100_20261011/tools/memok.py
python -X utf8 runs/20261011T222842Z-account05-A083-formal-core/code/check_lean.py
python -X utf8 runs/20261011T222842Z-account05-A083-formal-core/code/finalize.py
```

Resource and failure evidence: two Mathlib import attempts reached the 1400 MiB process cap and failed while reading imported .olean files; their result JSON is retained. Narrowing to the core rational library used about 503 MiB on the first core check. That check exposed a reversed transitivity argument in pos_transport; out/LEAN_ATTEMPT3.txt preserves the error and resulting sorryAx output. The source was corrected before final checking. A subsequent memok exit 1 delayed the retry; no job was started while that rejection applied. The closed regressions initially failed elaborator reduction; `decide +kernel` proved them by direct kernel reduction. The final compiler exit, elapsed time and measured peak commit are recorded in out/LEAN_RESULT.json. Every proof job has a 60-second timeout and 1400 MiB process-commit cap, with termination on timeout. There is no automatic dimension escalation, search, GPU job, package install or shared-tree mutation.

# proof dependencies and changed downstream conclusions

The new lemma has no campaign claim dependencies. Its library dependencies are the installed Lean core rational lemmas, and its foundational dependencies are exactly those printed by Lean. The original B09 repair is motivation and application context, not an assumption proving the arithmetic theorem. The claim hash is SHA256 of compact sorted JSON with keys exact_statement and hypotheses, UTF-8 encoded.

No shared registry was edited. B09's fixed counterexample remains at its established scope; B09's full analytic theorem and universal FEI remain separate obligations. A085/A073 can use this theorem to audit a changed signed-quotient certificate. Python Fraction correctness, implementation equivalence, real series error bounds and final decimal outward rounding are not inferred from this formal result. Formal rational coverage is universal over the stated rational interval domain, not an all-real or all-dimensional FEI certificate.

# one next mathematical action and independent reviewer

A090 should reconstruct the sign-split theorem and inspect its exact axiom list; A094 is the alternate independent reviewer. A085 should apply it to one newly changed signed logarithm certificate and identify its first remaining analytic step. This avoids repeating A081's already certified fixed margin and avoids building unrelated formalization infrastructure.

# actual persistence receipts or precise save blocker

All run artifacts and rolling STATUS.md, WORKLOG.md and LEARNED.md are written only inside A083. out/ARTIFACT_RECEIPTS.json records local file sizes and SHA256 values after schema validation. The run provides REPORT.md, CLAIMS.json, PROGRESS.json and its identical PACKET_DELTA.json compatibility copy; progress and claim field sets are checked against the protocol. Local persistence is distinct from independent acceptance, supervisor GitHub copy, Brain mirror and downstream use; those external receipts remain pending.

**Universal bridge:** This stage supports C019 stopping-tree payment and C018 erasure payment only at the certificate-soundness layer: it removes a known signed-quotient arithmetic risk but pays zero additional entropy or influence. The universal erasure/stopping debt and terminal entropy remain unbounded by this lemma. The shortest next route is to audit a new certificate attached to an actual unpaid payment inequality, using this small checked core, rather than repeat a solved finite margin or formalize a broad library.
