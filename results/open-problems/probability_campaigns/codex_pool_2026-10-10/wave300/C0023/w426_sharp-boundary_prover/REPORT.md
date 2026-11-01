# w426 C0023 report

Saved five author results: separator gluing, arbitrary-relay forest gluing, its sharp near-one modulus, a selected-relay conditioning counterexample, and a square obstructing a fixed pointwise witness. The sharp modulus is 1-sqrt(1-epsilon). These are special cases and refuted auxiliary routes; C0023 remains unresolved in this packet and current openness is UNKNOWN.

The tempting arbitrary-order relay sum gives 3/16 instead of the actual 1/8: a 50% overstatement. Correct conditioning gives terminal probability 0 for the selected bad relay instead of its unconditional 1/4. `python -X utf8 verify_boundary.py` passed 29,339 exact probability cases and 7,916 pointwise cases across 25 forest topologies, plus 29 counterexample weight vectors, in 50.59 seconds. Fractions are exact. These checks are not an independent or formal proof audit.

Submitted 7 DRAFT entries and 5 supported relations at `~/math-brain-inbox/w426/bundle_001.json`. `python -X utf8 prepare_review.py` passed local shape, license, relation and hook controls (2 fire, 2 silent, zero failures). Source license is owner-own-work. No live store or recall controls changed. Reviewed, ingested and retrievable remain false.

Apply: the validating coordinator reviews and ingests the dedicated draft using BUNDLE_SPEC; after hook pair approval, apply patches/01_selected_relay_hook.diff by adding its sole JSON line at the named live proposal path. PROGRESS_EVENT.jsonl is staged for the reviewer to publish under the worker write boundary.

Main risk: neither the separator proof nor arbitrary-order counterexample settles uniform gluing on cyclic graphs. A marginal-sorted selection claim is outside B1's refutation. w428 should check ATTEMPT.md and reproduce VERIFICATION.json; only audited results should land. The live integrator was not invoked because this worker may not write a live store. Full packet delivery to w428 is confirmed by msg-f8ab37d87a; w427 received the statement first and the completed attempt afterward. No independent audit or ingestion receipt has arrived.

NEXT: w428 audits L1-L3 and B1-B2; the coordinator integrates approved entries, keeping arbitrary-graph gluing as the single remaining gap.
