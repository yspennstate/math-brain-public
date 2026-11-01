# HARD8-02 — verification addendum — 2026-09-16T13:17:00Z

This append-only note records exact execution and GitHub receipts for the q=2 endpoint-rooted `P_3` absorber checkpoint.

## Main report

Path:

`hard8_2026-09-16/HARD8-02/runs/2026-09-16/2026-09-16T13-06-53Z__report.md`

Creation commit:

`a26cc5ce756a920e233ff1a092c672f5d9b4dc91`

Exact readback at that creation commit returned blob:

`6225f01347ace45b138367989182e0ce6af677ff`

The report was read back at its creation commit, including the theorem statement, parity-dependent trade formulas, verification section, claim ledger, and next-attack section.

Status: **VERIFIED**.

## Exact verifier

Path:

`hard8_2026-09-16/HARD8-02/artifacts/2026-09-16T13-06-53Z__p3_q2_closed_form_verifier.py`

Creation commit:

`a003bcd53b1d3326b2db4820623a4bf1a89a5413`

Exact readback at that creation commit returned blob:

`da8f86d87bb5b45428d04ffce4c14215f1b77687`

Status: **VERIFIED**.

The reviewed script uses only Python integer/set arithmetic. It contains no random sampling, floating-point acceptance criterion, external solver, or timeout-based inference.

## Archived execution output

Path:

`hard8_2026-09-16/HARD8-02/artifacts/2026-09-16T13-06-53Z__p3_q2_closed_form_output.txt`

Creation commit:

`a6bf91395018f99ba9c2f07aca0a7bf0be42bfc9`

Exact readback at that creation commit returned blob:

`61b98f05e1d6a6ecd3c87ef6c10cf528c12b1824`

Status: **VERIFIED**.

The bounded execution returned exactly:

```
Q2_ABSORBERS_VERIFIED 2000
TOTAL_PATHS_CHECKED 4004000
TOTAL_EDGE_DIFFERENCES_CHECKED 8008000
ALL_CHECKS_PASSED
```

The finite loop checks `h=1,...,2000`. The universal q=2 theorem is proved symbolically in the report and is not inferred by extrapolation from these cases.

## Prior checkpoint dependency

The report depends on the previous q=1 checkpoint

`hard8_2026-09-16/HARD8-02/runs/2026-09-16/2026-09-16T12-18-00Z__report.md`

creation commit

`debffffbf7d901a51b767bcbb3545cdc2fd808e1`

blob

`9345324a1b05da351e58a09de5ab5d67c53d1e68`,

and on the earlier defect-identity checkpoint referenced inside that report.

## Review posture

The exact formulas and deterministic checks establish internal consistency of this project checkpoint. This is self-review rather than independent external verification. The full graceful tree conjecture remains open.