The C0056 intake asks for both weak-disorder absolutely continuous spectrum and finite-volume GOE statistics. The original primary source specifies centered variance-one iid potentials, periodic boxes, and volume-scale microscopic statistics. This packet chooses the uniform law with an explicit coupling rescaling and addresses only the spectral component. A 2026-09-23 primary preprint claims a spectral result; its proof is not audited here, so current openness is UNKNOWN.

ATTEMPT.md proves five scoped author lemmas and one implication counterexample. The central reduction replaces inverse-power cavity estimates by a logarithmic entropy condition and carefully derives almost-sure spectral purity from it. The single hardest missing input for this route is the infinite-volume, fixed-positive-lambda bound LG uniform as eta tends to zero. The GOE component remains separate and unaddressed.

Measured with `python -X utf8 ~/brain_workers/w480/check_scalar.py`: 24 identity cases and 12 conditional-density cases PASS; maximum identity relative error 2.746210297965927e-13; 23020 function evaluations; 0.03125 CPU seconds. For a 3-by-3 diagonal cavity matrix, the integrated logarithm rose from 4.2185 at eta=1e-2 to 30.9724 at eta=1e-8, and its ratio to log(1/eta) moved from 0.9160 to 1.6814 toward the analytic limit 2. Floating-point checks are not proof of LG or a formal-check receipt. No brain performance improvement is claimed without ingestion and retrieval measurements.

Before this round: a dated attempted-unsolved record without a checked exact source convention. After: primary conventions recovered, five scoped proof lemmas saved, LG isolated, one exact counterexample, and seven concept-only draft entries with six supported relations. BUNDLE_VALIDATION.json records local schema checks only. No live code or store was changed.

Brain handoff: the validating coordinator reviews `~/math-brain-inbox/w480/bundle_001.json`; apply no code patch and promote no theorem before independent KEEP and provenance gates. The old bundle-spec suggestion to run the integrator is overridden by this task's explicit prohibition on unreviewed live-store writes. Submitted, reviewed, ingested, and retrievable remain separate states.

Risks: LG could fail even for an absolutely continuous model, because this sufficient entropy criterion is stronger than plain spectral purity. The regulated perturbation bound cannot reach eta=0 at fixed lambda. The uniform-law statement is a scoped instance, not a theorem for every iid law. Author and referee served-model identities cannot be certified from requested settings. External proof claims and source hashes are not proof audits.

The local HOOK_PROPOSAL.jsonl and patches/01_log_cavity_hook.diff prepare one narrowly triggered limit-order hint for the reviewer to land; the assigned worker write boundary keeps the live hook file untouched.

To apply the hook proposal, the reviewer creates ~/primary_directive/hooks1000/proposals/probability-w480.jsonl from the single row in HOOK_PROPOSAL.jsonl after checking the destination; patches/01_log_cavity_hook.diff names that exact live path. No live file was edited by w480.

NEXT: Independently audit L1-L5/C1 and attempt the infinite-volume LG bound below the sqrt(lambda) regulator cutoff; keep GOE and parent solved status unclaimed.
