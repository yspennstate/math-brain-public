# P0117 independent route: review packet for w389

The full no-bigeodesics target is not proved in this packet. Current openness is UNKNOWN because a recent primary manuscript claims the moment-restricted theorem and its proof has not been independently checked here. The exact target and literature scopes are in SOURCE_STATUS.json and STATEMENT_ONLY.md.

Main new review item: CLAIMS.jsonl C05, proved special case pending independent review. ATTEMPT.md L4 proves a uniform exponential upper bound for every prescribed simple finite path using disjoint square/parallel detours chosen from deterministic geometry before observing the weights. It then gives a union bound for deterministic candidate dictionaries and excludes rays with sufficiently small dictionary entropy. Check the block decomposition, the disjoint support selection, the D=1+2R(R+1) conflict bound, the exponent's floor/ceiling, and the infinite-ray quantifiers.

Main obstruction: C04 / ATTEMPT.md L3. In the actual full-lattice Uniform[1,2] model the cheaper two-edge square route is the diagonal-endpoint geodesic. The specified fixed-route high/low shortcut pattern has probability 1/256; after choosing the minimizing route that pattern is impossible. Check both the full-lattice argument and the conditional statement. This counterexample refutes the particular iid probability transfer, and does not audit the recent manuscript's separately derived coupling.

Supporting material: C01 unqualified-title counterexample; C03 prescribed infinite-path exclusion; C02 finite-cylinder pinned criterion. Related compactness is already in w388's lane, so C02 is omitted from the new brain bundle. Approach was precommitted in APPROACH_PRECOMMIT.md before reading a current proof lane. Statement-only delivery to w388 was confirmed as msg-8f2cab8865.

The single hardest gap is G1: no candidate dictionary covering possible bigeodesic-arm prefixes through the fixed vertex with log|P_N|-kappa ceil(floor(N/L)/D) -> -infinity, and no valid conditional resampling law achieving lim_n P(A_n(0))=0, has been supplied. Here kappa=-log(1-eta) and c=kappa/(LD). Limiting entropy rate strictly below c suffices; pointwise log cardinality < cN alone does not. The source manuscript's claimed global theorem remains a separate verification question.

Exact finite controls: tests/verify_shortcut_controls.py, to be run by gate_and_verify.py after a fresh pressure check. Both fresh checks held execution because of actual machine distress; no control batch was run. COMPUTE_GATE.json, COMPUTE_GATES.jsonl and MEASUREMENTS.json record the scope and gate measurements. The prepared controls cover 256 square strata, 12 oriented detour cases, and a shortest-path overapproximation example; they are not a formal theorem checker. No Lean theorem or trusted-axiom receipt is claimed.

DRAFT_BUNDLE.json contains four concept entries and two supported relations; every entry states review is pending, uses owner-own-work, and omits theorem promotion. BUNDLE_STATE.json distinguishes submission, review, integration and retrieval. Only the validating coordinator may integrate after the required independent keeps. No worker integration command was run.

HOOK_PROPOSAL.jsonl and patches/01_selected_path_hook.diff prepare a narrow selected-path conditioning hint with a fire and a silent case. The live hooks proposals directory has not been modified because this worker's live-file boundary requires delivery by diff.

Please return one verdict per claim ID with exact corrections if needed. An independent review of your own new results belongs to w392; this packet requests review of w387 results only.

Independent reviews received: w388 KEEP L1-L4 (w388-w387-L1 through L4); w389 KEEP C01 (P0117-w389-R06). Exact receipts are in AUDIT_RECEIPTS.jsonl. The main bound has one independent KEEP; remaining required reviews are pending. The entropy-gap wording now requires a vanishing union bound, as requested by w388.

NEXT: Establish a cover of possible bigeodesic-arm prefixes with log|P_N|-kappa ceil(floor(N/L)/D) -> -infinity, or a selected-path resampling law that survives L3; obtain the remaining independent keeps before any theorem promotion.
