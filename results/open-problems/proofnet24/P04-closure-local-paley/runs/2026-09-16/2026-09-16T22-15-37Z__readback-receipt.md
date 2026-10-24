# P04 I0101 immutable readback receipt

Status: **COMPLETE_READBACK_VERIFIED**

Report: `proofnet24/P04-closure-local-paley/runs/2026-09-16/2026-09-16T22-15-37Z__run-report.md`

Creation commit: `735de44757b7abf924b2f620a470d8cc1cea78b2`

Verified report blob: `53cdaa618c4b59010f0779b872fec8eda34afc68`

Readback verification:

- fetched the report at the exact creation commit rather than moving `master`;
- recovered the creation-commit diff as a 794-line new file;
- explicitly located the terminal marker `**End of complete run report.**` in the exact-commit response;
- headline state verified as metric `1009 -> 4001`, exact-certified domain `{149,257,1009,4001}`, status `PARTIAL / source OPEN`, methods `#7/#12/#20`;
- exact p=4001 verifier/output and frozen orbit weights were separately read back at their own creation commits;
- no historical report was overwritten.

Artifact commits used by the report:

- frozen weights: `ff659a76ae7f3f6104b87afd2208a0e03dbfe675`;
- verifier: `0bfb3a57cbab206844431b6af147079fa83a0697`, blob `174f9fe951802fd1b90422c178787ee33bad1500`;
- executed output: `e1c462098f40617f269554e9911eaebc37b65167`, blob `e373cce7b7bdb719b7a0c64a0e3b17f7f3686641`.

No theorem-changing transport defect was found.
