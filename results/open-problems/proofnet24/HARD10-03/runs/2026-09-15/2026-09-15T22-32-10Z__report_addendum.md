# HARD10-03 — receipt and numerical-search addendum

This append-only addendum records delivery receipts and the optional finite-state counterexample search performed after the mathematical checkpoint

`proofnet24/HARD10-03/runs/2026-09-15/2026-09-15T22-18-50Z__report.md`.

## Main mathematical report

Created on branch `master` at commit

`5592fc0ec6a39420b07ac4eab0bc5d2965132e2a`.

The file was fetched back at that exact commit after creation. Delivery status: **VERIFIED**.

The mathematical status remains **PARTIAL**. NEW-L35--NEW-L37 are proved conditional on the already archived fixed-number tagged heat-kernel input BF-HK-r/BF-R4K; the full d=3 conjecture remains open.

## Green-domination candidate checker

Code path:

`proofnet24/HARD10-03/artifacts/2026-09-15T22-26-30Z__green_domination_search.py`

commit

`72ddab86659d39bb3c15dc6f276af4c973869797`,

readback blob

`2a54193ab3c5b9ccb83e78a47b2a92caf32cb6c2`.

The code was fetched back at that exact commit. Delivery status: **VERIFIED**.

The checker exhaustively exponentiates the finite interchange generator for the listed graphs and tests every proper nonempty subset `S`, every anchor `u in S`, and times

`0.05, 0.2, 0.5, 1.0, 2.0, 5.0`

against the conjectural inequality

\[
\mathbb P(\operatorname{Cycle}_{\pi_t}(u)\subseteq S)
\le
[K_S(I-K_S)^{-1}]_{uu}.
\]

Tested graphs were `path3`, `path4`, `cycle4`, `star4`, `K4`, plus one nonuniform weighted path and one nonuniform weighted cycle on four vertices.

The executed search found **zero violations**. The largest observed left/right ratio was approximately `0.7499999984541397` (on `K4`, `t=5`, singleton `S`). This is only a finite-state counterexample search and is **not** a proof or independent verification of GDC.

## Search output

Output path:

`proofnet24/HARD10-03/artifacts/2026-09-15T22-26-30Z__green_domination_search_output.json`

commit

`e6fb85ca2ce4a10965e44c0d9a4b7dd3138b1065`,

readback blob

`cc9431c73b542b4f9044c5d45f4ab8bc0ae85490`.

The output was fetched back at that exact commit. Delivery status: **VERIFIED**.

No approval or security denial occurred in these GitHub writes. No email, Gmail, Google Drive, repository settings, workflows, access changes, public posting, third-party contact, or paid compute were used.
