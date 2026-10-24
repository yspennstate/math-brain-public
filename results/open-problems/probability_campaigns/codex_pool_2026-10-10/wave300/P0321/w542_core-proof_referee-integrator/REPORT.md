# P0321 referee report — 2026-10-10

**Found.** The dated tier-5 ranking is qualitative. Lewin's source describes fast translational and slow sixfold orientational correlations, but does not fix a full theorem statement. Its Theorem 47 assumes s>d, so it cannot establish translation invariance for the chosen d=2,s=1 subtarget. Current openness remains UNKNOWN after a bounded primary-literature check.

**Reviewed.** I independently rederived w541's Gaussian surrogate calculation and w540's L1-L3 conditional lemmas and C1-C2 counterexamples. All five w540 claims and w541's special case receive scoped KEEP verdicts in CLAIMS.jsonl. The Gaussian surrogate has algebraic positional order and a positive orientational plateau, so it is not itself a hexatic state. w540's microscopic defect/insertion estimate M remains conjectural. The hardest missing step is to prove that estimate for an actual neutralized 1/r Gibbs process on a nonempty temperature interval, including particle observables and positional disorder.

**Brain draft.** `brain_bundle_001.json` contains four entries and four supported semantic relations: source scope, two conditional/auxiliary lemmas, and the explicitly unproved bottleneck. `HOOK_PROPOSAL.jsonl` contains one narrow source-scope reminder. These are prepared locally, not submitted, ingested, or retrievable. w542 is one independent reviewer of w540/w541; a second independent review is pending under the wider two-auditor rule. No live store or recall control was changed.

**Measurement and checks.** The worker folder began with zero files and zero referee verdict rows. `python -X utf8 ~/brain_workers/w542/check_artifacts.py` returned `valid: 10 claim rows; 4 entries; 4 relations; 1 hook`. Mathematical checks are in REVIEW_PACKET.md and ATTEMPT.md; a JSON parse is not a proof. No numerical experiment is used to claim a phase result.

**Risk.** The primary source's qualitative phase language needs a separately specified observable and exponent. The conditional cumulant lemma could mislead if its hypotheses are dropped. The draft uses `owner-own-work` sources for this campaign's calculations; the coordinator should check source policy and obtain the remaining audit before ingestion.

**Apply.** After that audit, apply `patches/01_brain_bundle.diff` to create `~/math-brain-inbox/w542/bundle_001.json` and run the validating coordinator's draft integration; apply `patches/02_hook_proposal.diff` for the hook audit queue. The same payloads are in the local source files for manual copy if a patch utility cannot handle Windows absolute paths.

**Next.** Test a concrete volume-uniform connected-defect estimate for s=1 jellium, including rare disclination sectors and a well-defined pair-angle lift; keep the parent problem unproved until a genuine Gibbs observable estimate is checked.
