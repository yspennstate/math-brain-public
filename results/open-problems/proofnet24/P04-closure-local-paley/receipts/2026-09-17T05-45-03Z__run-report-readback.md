# P04 / I0101 readback receipt — 2026-09-17T05:45:03Z

Report path: `proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T05-45-03Z__run-report.md`

Creation commit: `534303105bce1394e989f1a228ffaf8637d0cbc1`

Verified report blob SHA: `7e00639496a5205478f5d4359a85d0b704325153`

Readback: complete, from line 1 through the terminal marker `**End of complete run report.**`, at the exact creation commit.

Status: `COMPLETE_READBACK_VERIFIED_WITH_ONE_DISPLAY_TYPO`.

One immutable transport/display typo was found in equation (5.10): the factor intended as LaTeX `\frac6{64}` was stored as the text `rac6{64}` because a single backslash was interpreted as a form-feed escape during the create-file call. The report is not overwritten. The exact canonical mathematical formula is

\[
2^{-6}\sum_E\left(a_E^2+|s_E|^2+2\|U_E\|_F^2\right)
=36+\frac6{64}\sum_E\sum_{g\notin E}(b_E(g)+1)^2.
\]

This correction is already forced by the correctly stored general identity (5.8), the correctly stored proof (5.14)--(5.15), and the correctly stored abbreviation (6.2)--(6.3), where the same term is written as `6V`. No mathematical claim, metric value, or conclusion changes.

No other readback discrepancy was found.