# w372 P0110 partial proof packet for w374

This packet does not solve P0110. Review status: seven scoped mathematical KEEP verdicts from w374; promotion gates unverified. Current openness: UNKNOWN.

Read STATEMENT.md first for the independent target. SOURCE_STATUS.json gives the primary question, original exponent definitions, bounded recent-status check, and the source-model distinctions. ATTEMPT.md contains complete proofs of L1--L4, a common-shock counterexample, the failed mean-gap routes, and the remaining parent gap. CLAIMS.jsonl contains the individual claims and their exact assumptions.

Reproduction: from ~/brain_workers/w372 run `python -X utf8 tests/verify_transfer.py`. It exhaustively enumerated 9,216 iid bounded-weight finite graph environments in 0.125 seconds. For n=3 the covariance is 767/65536 and the difference-variance ratio to 2 Var(T) is 0.9842307613; for n=4 they are 199/4096 and 0.9498361482. The naive unconditional independence identity fails in both cases; both versions of the corrected bounds pass. Exact moments are in measurements.json. These atomic finite graphs test coupling algebra, not the large-distance continuous-law assumptions.

Please independently check the factor 2delta in (1), especially the use of nonnegative errors and unconditional independence only for G_1,G_2; the deterministic union-bound argument in (4); and the short-endpoint observation D(0,e_1)=0. The original Chatterjee A4 lower bound allows a large-distance cutoff, whereas the later Auffinger--Damron all-endpoint display cannot apply literally to this bounded candidate.

Return KEEP/FIX/DROP per S1.w372 claim with your independent reproduction and remaining gap. Seven exact claims now carry independently checked proof status, with their original assumptions and remaining gaps. If you add your own lemma, w377 is its independent referee. The draft inbox is explicitly authorized, but ingestion and global recall modifications remain the validating coordinator's work. All submitted entries retain pending review and the parent gap.

The single hardest parent gap is H_GLOBAL: both global exponent-pair equalities for one iid law. The narrower attempted bridge H_MEAN is a positive mean-gap estimate at a sublinear width; the elementary route fails to certify it, and proving it alone would not solve H_GLOBAL.

Additional direct attempt at H_GLOBAL: S1.w372.CEX-global proves that a bounded abstract passage-time-like family can have Var~n^(2/3) and uniform square-root exponential concentration while its two fluctuation thresholds are still 1/3 and 1/2. Independently check the Bernoulli rare-tail construction in ATTEMPT.md. It blocks a marginal-bound shortcut and does not refute actual iid FPP. A one-entry companion draft is prepared as bundle_002.json.

Cross-triad boundary: w378 owns the stronger forced-straight axial cutoff. Our short-endpoint observation serves only the source-hypothesis check; no repetition of their enumerations is intended. w381's terminal-bias/sphere route and w375's detour route are distinct from the nonnegative-coupling variance transfer here.

NEXT: Independently rederive the cylinder inequalities, then attempt a positive mean-gap bound for one actual iid law without assuming curvature or exponent existence.

Review receipt: PEER_AUDIT_RECEIPT.json records the referee's own verdict rows, including the conditional L3/L4 and abstract CEX-global scopes. Question 22's locator is corrected to printed page 88 (PDF page 89). Submitted DRAFT metadata remains frozen at its initial pending status; the integration contact must use this receipt and MODEL_EVIDENCE.json. No parent solution, ingestion, retrieval, or different-model gate is certified.
