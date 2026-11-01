# P0043 round report — 2026-10-10

Found: the September ranking and the local brain still present P0043 as open; their wording omits key hypotheses. Hutchcroft (2016) proves the exponential-growth case. A 24 September 2026 public manuscript claims the full bond result and names a Lean comparator solution. I verified its exact theorem statement and artifact map, but did not run the comparator or independently certify the full proof. Current status is a **public solution claim with verification pending**; no novelty claim is made here.

Changed: saved exact source status in `SOURCE_STATUS.json` and the failed bridge in `ATTEMPT.md`; reviewed w441/w442 in `REVIEW_PACKET.md` and `CLAIMS.jsonl`; queued a two-entry, three-relation DRAFT bundle at `~/math-brain-inbox/w443/bundle_001.json`. The bundle adds the source-backed 2016 theorem and a clearly labeled dated pointer to the 2026 claim. It does not edit the live store. The local hook proposal is in `HOOK_PROPOSAL.jsonl` for coordinator placement under the worker write boundary.

Measurement: `python -X utf8 .\recall_probe.py` against the read-only population store returned **0 theorem cards among the top 5** for `Hutchcroft critical percolation quasi-transitive graph exponential growth theorem`; the raw decision and exact cards are in `RECALL_MEASURE.json` and `CARD_READS.json`. `python -X utf8 -m json.tool drafts/bundle_001.json`, the same check on `SOURCE_STATUS.json`, and parsing all four JSONL claim rows passed. The bundle is not yet ingested, so there is no measured after-recall improvement. This is a measured retrieval failure with a bounded proposed repair.

Review: KEEP the boundary, thinning, corridor and quantifier deductions; FIX w441-L004 to say `q in [0,1)` and w441-L005 to justify `liminf` using every radius. Independently rederived L002 and the load-bearing L004/L006 bounds. The hardest remaining mathematical step for an independent proof is the subexponential case: positive anchored expansion cannot hold in any infinite subgraph there. A partial KEEP does not solve P0043.

Risk: the 2026 general proof claim is not independently checked, and the named Lean configuration's imported axiom closure has not been run locally. The 2016 arXiv license tag is accepted by the draft spec but still needs integrator validation. The local store's older open label needs a status correction only after that review. w441-L002 through L006 currently reside in markdown rather than claim JSONL, so the author should serialize any rows intended for promotion.

Apply: the draft is already in `math-brain-inbox/w443/bundle_001.json`; the coordinator validates and ingests it, then reruns the same recall query. `patches/01_p0043_bundle.diff` mirrors the queued draft for review; no SQLite patch is applied by w443.

NEXT: Coordinator checks the public comparator theorem/axiom closure and the bundle, then remeasures the named retrieval query after ingestion.
