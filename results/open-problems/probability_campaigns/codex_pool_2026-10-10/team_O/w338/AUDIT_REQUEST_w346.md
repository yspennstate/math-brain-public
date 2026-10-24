# w338 -> w346: blind mathematical check

Please audit all eleven entries in ~/math-brain-inbox/w338/bundle_001.json. Ten assigned problems are covered; P0090 has two separate lemmas. Every claim is author-checked and provisional, and none is a claimed full solution or novelty result.

Read the statements, assumptions and proof text, independently reach a verdict, then write one KEEP/FIX/DROP row per entry key with a reason. Your own folder is the appropriate verdict destination: ~/brain_workers/w346/audits/w338_bundle_001.jsonl. Do not read or review earlier audit verdicts. In particular, the P0266 claim here is a scalar moment calculation; its old parent-reported review receipts are not evidence for your decision.

C0021 is the strongest measured result. Independently compute the nine-bit decision-tree cost or verify the integer Bellman certificate before using the author's measurements or policy as your reference. Check every partial assignment's terminal condition, the optimized action, all full-input outputs, transitive symmetrization, and independence in recursive composition. The claims concern uniform bits, zero error, and achievable revealment. The exact asymptotic exponent and present literature status are not claimed.

For the remaining entries, especially check: finite-horizon versus infinite-horizon stopping in P0266; unrestricted spatial versus timed excursions in C0133; reachable type classes and deterministic critical cycles in P0090; exponential memorylessness and survivor costs in P0427; potential sign in C0032; joint rare-event tests in C0077; the explicit unproved variance hypothesis in C0119; boundary closure versus cluster reachability in P0010; and the distinction between general trees and actual geodesic Cayley spanning trees in P0036.

Evidence lives in this folder: PROOFS.md, check_majority.py, majority_policy.json, majority_measurements.json, check_special_cases.py, special_case_measurements.json, edge_evidence.jsonl, problem_statuses.jsonl, bundle_validation.json. CoreChecks.lean is prepared, but lean_result.json records SETUP_UNVERIFIED; nothing in the packet is called Lean-checked.

The reviewer should integrate only entries that survive your KEEP and the required proof check. A KEEP on a partial lemma does not resolve its parent open problem. Mesh sends were not used because the worker brief explicitly forbids them.

NEXT: Independently audit the eleven entry keys and return verdicts for the reviewer to apply.
