# P0162 referee packet — w512

## Verdict 001: w511 source row

KEEP the narrow historical metadata claim in `~/brain_workers/w511/CLAIMS.jsonl` row `P0162-w511-source-001`. Reproduction: the ranking CSV at line 553 reads `5,P0162,Fourier entropy versus total influence,attempted_un,Fourier entropy versus influence conjecture`. This proves only what the dated ranking recorded. It does not prove the current open status or a mathematical result. The row itself correctly states that limitation.

Independent reviewer: w512. Remaining gap: exact primary statement, recent literature, and owner's solved/retired records.

## Mathematical verdicts

KEEP w510 C001-C004 and w511 C001-C004 at their stated narrow scopes. `VERDICTS.jsonl` records each independent reproduction and remaining gap. For w511 C003 I independently checked the derivative inequality and the order-p expansion; `audit_split.py` gives the finite-n numeric check. For w511 C004 `check_proxy.py` uses integer Walsh sums and exact fractions. These checks support the written proofs and do not certify priority or the universal FEI conjecture.

The single hardest parent gap is a dimension-free entropy budget for arbitrary Boolean spectra. The affine proof uses uniform dual-subspace weights. The bent selector disproves any bound for every prescribed splitting coordinate, while an existential choice of coordinate remains possible.

## Brain bundle review

The submitted w510 bundle_001 has six entries and five relations. Its affine theorem and counterexamples match C001-C004. Its `depends_on` edges cite the exact coefficient, influence, and entropy ends proved in C001; the `gap` association preserves the mass factor from C003. The submitted w511 bundle_002 supersedes bundle_001 and has seven entries and six relations. Its proof-bearing lemma nodes match the checked C001-C004 claims. Its `point-flip -> bad-bridge` edge refutes only the all-coordinate version, and its coordinate-choice edges explicitly retain the existential quantifier. The coordinator must check account separation and the served model before treating these as final referee approval; do not ingest both w511 drafts.

`DRAFT_BUNDLE.json` in this folder adds two scope cards and four evidence-backed relations to the peer cards. It is prepared only. Copy it into the inbox after accepted peer bundles have been ingested so the cross-bundle targets exist; record submission, ingestion and retrievability separately.

The local numeric scripts ran before a fresh resource sample and are exploratory. A later gate denied further experiments (see `COMPUTE_GATE.json`); the verdicts rely on the independent algebra above. `HANDOFF.json` pins the exact reviewed peer bundle bytes and marks served-model/account evidence unavailable to this worker.
