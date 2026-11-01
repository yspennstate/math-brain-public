# P0043 referee report — w440, 2026-10-10

I recovered the original 1996 site-percolation Conjecture 4, including the connected/local-finite, almost-transitive and p_c<1 hypotheses, and separated its bond analogue. The historical P0043 ranking omitted the model and p_c<1. I independently checked the w438 and w439 special-case proofs and issued scoped KEEP verdicts in REVIEW_PACKET.md and REVIEW_RECEIPT.md. I also verified w439's correction of a specific old C0084 method sentence against the exact read-only store card and Hutchcroft's proof.

My distinct author result is an exact cyclic-block special case: replacing each edge of the 3-regular tree by m>=2 parallel two-edge paths yields a quasi-transitive graph with p_c=sqrt(1-2^(-1/m)) and critical one-arm constant 12 along even radii. The proof is in ATTEMPT.md; w443 review is requested in REVIEW_FOR_W443.md. It is not in the submitted brain draft. The full P0043 conclusion is not claimed here.

Measured with `python -X utf8 measure_bundle.py` in this folder: the dated ranking row explicitly had 0 model and 0 p_c<1 qualifiers; the two submitted concept entries each specify both (2/2 each), with 1 evidence-backed relation. The JSON audit reports 7 claim rows and an exact 3,388-byte match between the local draft and inbox file. This measures draft completeness, not live recall gain. The mathematical claims are proved analytically; no finite experiment is used as proof.

**Apply:** coordinator reviews `~/math-brain-inbox/w440/bundle_001.json` and, if accepted, runs the normal draft integrator; the source correction receipt identifies the exact old card for a separately reviewed update. No live store, memory, service or repository was changed by this worker.

Risks: the 2026 full-bond formal claim has not been rebuilt or axiom-audited here; the source paper license and draft-source policy should be checked at ingestion; the new cyclic-block result is author-only pending w443. Brain states: prepared=true, submitted=true for bundle_001, reviewed=false for bundle_001, ingested=false, retrievable=false. Hook proposal `math-w440.jsonl` is submitted for the next audit round.

NEXT: w443 checks the cyclic-block reduction and one-arm constant; coordinator then reviews the source correction and integrates only accepted draft concepts.
