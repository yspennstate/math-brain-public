# r41 checker correction

The proof in `REPORT.md` is unchanged. Its final numerical-regression sentence was written from an earlier local draft of the checker and is superseded by the committed `CHECK.py` and `CHECK_OUTPUT.txt` in this same immutable run directory.

The corrected checker does **not** alter the pivot coefficient when the sampled scalar pivot is too small; it skips that sample, preserving the exact algebraic relation being tested. It checks 3,854 non-small-pivot random instances out of 4,000 draws.

Correct committed regression values:

- `max_algebra_residual = 1.541783e-15`;
- `min_observed_area_ratio = 1.000078258116`;
- `area_violations = 0`;
- terminal marker: `QFORM_B19_R41_CHECK_PASS`.

The finite constants in the report are unchanged:

- `S0 = 2.3856699607287348e-05`;
- `K = 11.010263449046631`;
- defect-circuit live bound `< 11990.370228314221 < 11991`;
- self-defect operator collar `< 0.074466706`;
- full structured coefficient collar `< 0.090091706 < 0.091`;
- designated-partner interval bound `< 103.785056 < 104`.

This file records a checker-regression correction only. It is not a mathematical correction to `QFORM-PHYSICAL-PIVOT-DEFECT-AREA-v1` or the structural compiler proved in `REPORT.md`.
