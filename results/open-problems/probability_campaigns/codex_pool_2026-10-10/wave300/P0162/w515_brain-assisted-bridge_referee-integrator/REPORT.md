# P0162 report — 2026-10-10

Found: the dated ranking and math-brain card both record P0162 as attempted/unsolved, while current openness and any owner retirement remain unverified. The exact uniform Boolean target is checked against arXiv:2606.00246v2. Recent primary papers prove only partial classes or an extra-term upper bound.

Changed: submitted draft `~/math-brain-inbox/w515/bundle_001.json` with three typed nodes and three evidence-backed relations. It links a properly scoped Li-Han theorem to a false absorption route and an exact conjunction witness. It is a draft; reviewer validation, ingestion, and retrieval are separate pending states. `REVIEW_VERDICTS.jsonl` gives twelve peer verdicts (eleven KEEP, one FIX), with analytic reproductions; none proves P0162.

Measurement: `python -X utf8 math_recall_gate.py` took 14.1097 s and returned 0 Han/Li-Han theorem titles among eight direct hits for the query naming Han's correction bridge. `python -X utf8 verify_selector.py` independently checked 32 and 128 input points: bad-coordinate ratios 8.030013847 (n=4) and 10.255970235 (n=6), while full-function H/I was 1.800892435 and 1.952643846. This validates the finite examples; the all-n verdict rests on the convexity proof in REVIEW_PACKET.md. No after-ingestion recall result exists, so retrieval gain is a proposal, not a measured improvement.

Risk: the new conjunction row awaits w518 independent audit; duplicate or unresolved cross-link handling belongs to the coordinator integrator. The remaining theorem-sized gap is an aggregate conditional-entropy bound or an existential good-coordinate rule for all Boolean functions. Current openness stays UNKNOWN.

Apply: coordinator validates the submitted draft against BUNDLE_SPEC.md, obtains w518's verdict on the own-work row, then integrates the draft and repeats the exact recall query. `patches/01_bundle_001.diff` records the proposed inbox change for review; the file is already submitted, so do not apply it twice. No live code or store file was changed. The local hook proposal, progress line, and review request are staged here because this worker's write boundary permits no hooks-proposals, progress-page, or peer-feedback writes.

NEXT: w518 audits P0162-w515-001; coordinator integrates only after validation, then reruns the saved recall query.
