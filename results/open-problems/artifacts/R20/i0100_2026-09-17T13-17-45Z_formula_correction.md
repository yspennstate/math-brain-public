# R20 / I0100 formula correction for the 2026-09-17T13-17-45Z immutable report

The immutable report

`runs/R20/2026-09-17T13-17-45Z_i0100_projected_simplex_balance_7a4c2e.md`

contains one Markdown/escape typo in equation (4.10): the `\frac` command was damaged in serialization. The intended and proved formula is

\[
\boxed{
a_Z\ge -\frac{\sum_{x\ne0} c_x f_x}{\sum_{x\ne0} f_x}.
}
\tag{4.10 corrected}
\]

No mathematical statement, proof step, metric, status, or ledger entry changes. The report remains immutable; this artifact is the canonical correction.