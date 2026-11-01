# HARD10-03 — receipt and finite-state certificate addendum

This is an append-only receipt/certificate addendum for the substantive report

`proofnet24/HARD10-03/runs/2026-09-15/2026-09-15T23-22-30Z__report.md`.

## Mathematical report receipt

The report was created on branch `master` at commit

`2c048f5b172e698f96f9134b651a66c7a998fc8d`.

It was read back at that exact commit. GitHub returned blob SHA

`aee46db6b7efb3c19c46d523cd34475d38430bc0`.

Delivery status: **VERIFIED**.

The full target remains open; the report proves only the fixed-lag full-phase contact theorem NEW-L40 and supporting lemmas NEW-L38--NEW-L39.

## Finite-state checker receipt

Checker path:

`proofnet24/HARD10-03/artifacts/2026-09-15T23-35-00Z__fixed_lag_entry_phase_check.py`

Commit:

`c672efb13e1ce1219db5549df2b1371440885e8c`

Readback blob:

`6433674a891d9b3b0764093cac08c09029e8ecee`

Delivery status: **VERIFIED**.

The checker enumerates the full interchange semigroup on `C5` and computes the exact finite-state Campbell entry intensity for the anticipatively selected pair `(0,P^r0)` at several phases. It is a sanity check, not a proof.

## Executed output receipt

Output path:

`proofnet24/HARD10-03/artifacts/2026-09-15T23-35-00Z__fixed_lag_entry_phase_check_output.json`

Commit:

`35804ed1f9b323e30a428285f4e89a3d8314784f`

Readback blob:

`0d9450b73f258e9b02b08b192497014b1b85e81a`

Delivery status: **VERIFIED**.

At `beta=1.2` and phases `0,0.2,0.6,1.0,1.2`, the computed entry intensities were phase-independent to floating-point matrix-exponential precision:

* `r=1`: approximately `0.71861345230394`, maximum spread `3.1641e-14`;
* `r=2`: approximately `0.52243847895475`, maximum spread `9.1038e-15`;
* `r=3`: approximately `0.50540787332870`, maximum spread `1.1546e-14`.

These numbers certify only the finite `C5` calculation and do not establish the infinite-lattice theorem.

No prior or peer file was overwritten. No GitHub approval/security denial occurred in these writes. No Gmail/email or Google Drive delivery was attempted.
