# C0047 referee report — 2026-10-10

The 1996 source states Conjecture 6 for connected locally finite almost transitive graphs with positive Cheeger constant. It uses site percolation by default and says the nonplanar question has a bond form. The September 2026 OpenAI manuscript claims the full bond result, including every fixed finite symmetric Cayley generating set. I verified its theorem scope, not its 53-page proof. Its public Lean comparator has `sorry` in the three main theorem bodies. Current site status is UNKNOWN; bond status is a public claimed resolution awaiting independent mathematical validation.

The strongest immediate correction is to C0047-A001: the published sufficient condition is `D*rho*p_c<1`, where `rho` is the normalized random-walk spectral radius and `D=|S|`. The old `p_c<1/rho` omitted `D` and is automatic for a nonamenable Cayley graph. I prepared an append-only correction diff, retaining the historical row. Its failure as a necessary condition is witnessed by both peers' independently derived nonamenable Cayley examples; those are counterexamples to an auxiliary bridge, not to C0047.

I checked w558's six rows and w559's four rows in [REVIEW_PACKET.md](REVIEW_PACKET.md), recording ten scoped KEEP verdicts in [REVIEW_VERDICTS.jsonl](REVIEW_VERDICTS.jsonl). I also proved a classical sharp **site** regular-tree special case in [ATTEMPT.md](ATTEMPT.md), pending w563's independent review. No parent-problem proof or novelty claim is made.

Local measurements: `python -X utf8 ~/brain_workers/w560/verify_referee.py` passed 6 exact checks and validated 10 verdicts, 4 claims, 2 draft entries, 1 relation, and 1 staged hook in 0.001731 seconds. `python -X utf8 ~/brain_workers/w560/validate_patch.py` applied the diff to an isolated copy, preserving 142 original rows and adding exactly 1 correction row. See [MEASUREMENTS.json](MEASUREMENTS.json). The draft [bundle](draft_bundle_001.json) is staged inside this worker folder: submitted=false, reviewed=false, ingested=false, retrievable=false. The live store and intake file were not changed.

Apply: from `~/<private-repo>`, the reviewer runs `git apply ~/brain_workers/w560/patches/01_c0047_spectral_correction.diff`; after second-account review, copy the complete draft to `~/math-brain-inbox/w560/bundle_001.json` and let the validating coordinator run its normal integrator. The hook proposal is staged as [HOOK_PROPOSAL.jsonl](HOOK_PROPOSAL.jsonl) for the allowed hooks pipeline.

Risk: the public 2026 bond proof was not independently validated, and the linked comparator has admitted placeholders. Served model identity and second-account mathematical review are unverified. The site-tree lemma is withheld from the draft bundle until w563 audits it.

NEXT: Audit the load-bearing critical-boundedness Theorem 2.6 of the bond manuscript and obtain w563's review of the site-tree lemma.
