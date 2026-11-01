# P0117 referee report

I checked the original survey question, the dated P0117 intake, and Theorem 1.1 of a September 24, 2026 primary preprint that claims the full planar nonatomic result under the minimum-of-four second-moment condition. Its 39-page proof was not audited here. Current openness and proof acceptance remain unverified; the September 7 `attempted_un` label is not a current-status verdict.

I independently rederived w390's high-slab/cheap-bypass counts, independent trap supports, summable dyadic failure bound, and simultaneous-ray quantifier. **KEEP** its thin-tube partial theorem and w391's constant-law boundary. I separately audited w389's stationary occupation identity and the one-sided shell floor: **KEEP** both, with one wording correction in a relation rationale. The full P0117 gap remains: neither route excludes arbitrary wandering bigeodesics or proves the needed occupation decay.

I added a new zero-atom counterexample to a weakened definition allowing repeated vertices. It is clearly scoped outside the injective target and awaits w395's independent verdict; it is absent from the brain draft. The local draft contains two reviewed concept records and two supported links to the existing P0117 node. No live store or global control was changed.

Validation command: `python -X utf8 validate_artifacts.py` returned `{"claim_rows": 10, "kept_peer_rows": 7, "draft_entries": 2, "draft_relations": 2, "hook_proposals": 1}`. Patch staging command: `python -X utf8 make_patch.py` returned 65 bundle lines and one hook row. These measure the saved packet and format, not a change in brain retrieval. Submitted: no; reviewed here: yes for the peer claims and local draft scope; ingested: no; retrievable: untested.

Apply: the coordinator can copy `draft_bundles/bundle_001.json` into `~/math-brain-inbox/w392/` as a complete `.part` file and rename it to `bundle_001.json`, then run the usual draft validator/integrator. `patches/01_p0117_review_bundle.diff` names the same target. `hook_proposals/math-w392.jsonl` and `patches/02_p0117_proof_status_hook.diff` stage the one evidence-backed hook for its normal pair audit. `PROGRESS_EVENT.json` stages the one-line progress entry. I kept these inside the worker folder because this brief permits no external writes except its two named test-file exceptions.

Risk: the 2026 preprint may be sound or flawed; this packet checks its statement only. The accessible survey's p. 86 locator may differ from the intake's edition. The zero-atom boundary must not be promoted until w395 checks it.

NEXT: w395 audits the zero-edge boundary; the coordinator applies the reviewed draft and records submission, ingestion and retrieval separately.
