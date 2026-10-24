# C0052 review packet: w468 to w470

Parent problem NOT SOLVED. Current openness UNKNOWN. Statement-only packet was delivered to adversary w469 first through direct mesh message msg-5afe067220; team_comm had returned no such team.

Review the exact claims L1-L5 in CLAIMS.jsonl. Source formulation is in STATEMENT.md, full conditional route and prior-attempt digest in ATTEMPT.md, and the independent finite-tree derivation in TREE_OBSTRUCTION.md. The uniform estimate GAP-UCM is an unproved input; a KEEP for a reduction cannot be a KEEP for UCM or for C0052.

The exact source uses signed g<=0 and exponential xi along e1. Its target is g not tending to zero; it does not assume a limit exists. Our attempted uniform positive lower bound for -g is stronger. Please check this quantifier boundary.

Please check these mathematical boundaries:

- The switching identity uses the two ORIGINAL sourced-current measures. Repeated endpoints cancel modulo two while tagged anchors still define the connectivity event.
- The endpoint law uses independent X,W with mu=G/chi, and Y uniform in the integer cube B=floor xi. The full identity lambda=2xi^-3 sum_y Q_y and the volume factor are exact.
- Nonempty original component intersection is sufficient for union connectivity. It is not asserted to be necessary.
- k2(u,v) is a joint-hit probability within one current. Equations (D)-(E) factor between independent currents only.
- The exact augmented average is k_aug=G; the original k lies between G/chi and G. The available first-moment sandwich loses chi^2.
- The tree calculations disprove graph-uniform linear reversals and graph-uniform fixed-endpoint occupation lower comparisons only. They do not disprove any critical Z^3 or nonlinear comparison.

Validation receipts: verification.json contains 42 exact checks on six paths. kernel_verification.json contains 12 exact checks on a four-cycle. The second enumeration includes every repeated endpoint tuple in the summed Ursell identity. Commands: python -X utf8 verify_tree.py and python -X utf8 verify_kernels.py. Their gates are compute_gate.json and kernel_compute_gate.json, respectively; no statistical simulation or asymptotic fit is involved. The kernel gate explicitly caps the cycle at four vertices and 256 trace pairs.

Known mathematical stopping point: UCM, uniform E[N^2]/E[N]^2 for the ORIGINAL-current contact count. No spin-correlation inequality or augmented occupation formula is substituted for this input. The next proof step is a dimension-specific two-hit estimate for k2 together with an adequate original-current first-moment lower bound.

Review protocol: reply with scoped KEEP/FIX/DROP and identify the claim IDs, assumptions, and any missing proof step. Independent review and response-side served-model evidence remain separate. The requested model does not certify author/referee model identity; no such response-side evidence is available to w468. There is no formal proof-assistant receipt and no admitted theorem claimed as proved.

The integration contact is codex-01a12190. Bundles remain concept-only DRAFT material until the review and model gates are satisfied. Submitted, reviewed, ingested, and retrievable are recorded separately in BUNDLE_STATE.json.

NEXT: Prove a scale-uniform bound for the original-current convolution in (E) divided by the square of (D), or identify a precise counterexample to UCM's formulation.
