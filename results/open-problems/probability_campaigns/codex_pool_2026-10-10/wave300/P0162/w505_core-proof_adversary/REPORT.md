# w505 P0162 report

Found an explicit Boolean counterexample to a universal restriction-deficit bound for every coordinate. Referee w506 independently re-derived it and filed KEEP, receipt P0162-REVIEW-W505-004. This is a check of a proof input; full FEI and the suitable-coordinate premise remain unproved. Current global openness is UNKNOWN; no novelty claim is made.

The exact statement and original source pointer are recovered in SOURCE_STATUS.json: O'Donnell, arXiv:1204.6447, printed p.5. The original P0162 card and its failed singleton-spectrum attempt were retrieved read-only; relevant owner FEI memories and two recent primary papers were checked for scope.

For F_m(u,v,y)=(-1)^(u dot v)-(1-y)1{u=v=0}, I_y=2^(-2m) and Delta_y/I_y>=log_2((2^m-1)^2+1). The measured ratio rises from 4.8676687468 at m=1 to 20.3280154117 at m=8. The entire displayed family also has H/I<=2, now explicitly kept by w506. C001-C005 have separate scoped KEEPs in INDEPENDENT_REVIEW_UPDATE.json. C006 retains status conjecture: only the conditional induction was checked. The remaining hardest input is a uniform suitable-coordinate bound when every influence is below 1/16.

w504's core proof was audited after the independent derivation was saved. Its exact entropy identity, conditional reduction, and base-coordinate family bound check out. The audit found two wrong literal control-block signs; the correct nonzero coefficients are -2t,+2t,+2t. w504's current proof has the corrected phase and w506 records a corrected draft. The historical patch remains audit evidence; do not reapply it to corrected text.

Validation commands:

- python -X utf8 -B ~/brain_workers/w505/verify_obstruction.py --gate cpu20s-n9
- python -X utf8 -B ~/brain_workers/w505/validate_packet.py

The final mathematical check passed in 6.652632s within its fresh 20-second gate: four exact family truth tables, 276 Boolean functions through dimension three, independent direct character sums for m<=3, and the base-coordinate formula on 20 restrictions. Packet validation passed with 8 result rows, four entries, five relations, and two relation rows quoting both supporting ends. No formal proof-assistant check was claimed.

The latest DRAFT is ~\math-brain-inbox\w505\bundle_003.json. It has one independently kept lemma, one definition, and two concepts. The earlier drafts are retained; the coordinator should validate this latest revision. Submitted, scoped mathematical review, full-bundle review, ingestion, and retrieval states are separate in BUNDLE_STATE.json. No ingestion or retrieval receipt is available.

Apply: codex-01a12190 validates bundle_003.json and the scoped referee receipts; live promotion waits for the corresponding model-review gates. MODEL_EVIDENCE.json records author and referee served models as UNKNOWN, because no response-side evidence was supplied. INTEGRATION_HANDOFF.json provides exact artifact paths and file SHA-256 hashes. Hashes establish identity only. No peer/live proof or math store was changed; no services or agents were started. Global hook/progress requests remain staged in the worker folder.

Main risk: promoting the family result or conditional reduction to a universal theorem, or treating a finite numerical run or source hash as a proof. The peer packet leaves the missing input explicit. The staged hook targets that precise quantifier mistake.

NEXT: Attempt the positive-influence suitable-coordinate inequality for arbitrary Boolean spectra with max_i Inf_i<1/16; retain the unproved input label.
