# Scope addendum for `QFORM-COLLINEAR-BANK-CAPPED-BASIS-v1`

This addendum is part of the final r22 mathematical bundle and sharpens one boundary case in `REPORT.md`.

In Theorem 4.1, the finite capped-basis conclusion is asserted only when the optimized score `Z_B` is positive. Equivalently:

- if `h<=L/2`, the theorem applies with `Z_B=L`;
- if `h>L/2`, it applies provided `s=L-h>0`, with `Z_B=2 sqrt(hs)`.

If `h=L` (the collinear bank has only one nonzero physical row), then there is no probability distribution supported only on one-bank-plus-two-complement bases whose bank-coordinate marginal is at most `1/2`. The displayed formula gives `Z_B=0`; the capped-basis construction makes **no finite assertion** in that boundary case. That case is precisely part of the single-hub survivor isolated later in the report.

Nothing in Sections 5.1 or 5.2 is affected: Section 5.1 has `h<=L/2`, and Section 5.2 assumes `s>=1/64`. The survivor statement in Section 5.3 remains valid and explicitly includes `s=0`.

No other claim is changed.
