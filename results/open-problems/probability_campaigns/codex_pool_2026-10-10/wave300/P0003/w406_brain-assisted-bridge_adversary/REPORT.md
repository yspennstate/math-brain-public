# w406 P0003 review handoff

The recorded problem is Grimmett Question 2.2: uniform n-step SAW from the hexagonal-lattice origin. I corrected an initial substitution of the related chordal critical-fugacity problem. No equivalence of those ensembles, P0003 solution, current-openness certification, or novelty claim is made.

I saved an independent cycle-kernel proof before reading w405: the vertex relation admits a zero-boundary hexagon mode of norm 1, with jump 1 at distance sqrt(3)*delta/2. Thus boundedness and boundary data do not supply mesh-uniform regularity. A separate C6 example gives total variation x^4/(1+x^4)>0 between fixed-length and fugacity endpoint-conditioned laws. Both submitted proofs require w407's independent check.

My audit keeps w405's finite restriction, positive outer-buffer lemma, and contact counterexample under their stated assumptions. The chordal identification remains conditional on T/B/C. Applying it to the recorded rooted fixed-length target also requires a length/endpoint-conditioning transfer. The audit covers the original L1/L2/R1/C1 packet; w405's subsequently announced L3/R2 are not assigned a verdict here.

Measurements: `python -X utf8 bounded_recall.py` returned zero rows at a configured 60-second timeout, with 70.707 seconds including cleanup. `python -X utf8 -B retrieve_bridge.py` returned five incompatible finite square-lattice computations in five top hits from the scoped 80-card candidate pool. `python -X utf8 narrow_source_lookup.py` recovered the original target among eight exact-title cards in 0.125 seconds. These are single scoped runs, not a benchmark of full-store recall or a deployed improvement.

The bounded repair is a per-target hypothesis contract: recover the primary target first, then compare lattice, ensemble, endpoints, length regime and convergence specification. Apply `patches/01_p0003_bridge_requirements.diff` to its named live metadata-fixture path only after review; a runtime consumer remains a proposal. The existing retrieval/recall code and SQLite store were not changed.

Five DRAFT concept/definition entries and four exact edges were submitted to `~/math-brain-inbox/w406/bundle_001.json`. Submission is confirmed; independent review, ingestion and retrieval are separate unconfirmed stages. The validating coordinator may integrate only within the reviewed scope. An evidence-backed ensemble warning was submitted as `hooks1000/proposals/math-w406.jsonl`; no hook was activated.

Local draft-schema checks passed. STUCK: the small exact checker was held twice by fresh pressure gates: physical headroom was 2996 MB, then 2782 MB, below the guarded 4096 MB requirement. Its runnable test and both gate receipts are included; no numerical checker pass or formal proof receipt is claimed. I completed the algebraic audit instead of waiting or weakening the gate.

NEXT: Independently verify the cycle proof and C6 counterexample, then specify and prove the fixed-n length/endpoint transfer; keep the chordal partition-ratio and curve-tightness gaps explicit.
