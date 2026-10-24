# ProofNet24 P20 immutable readback correction — 2026-09-16 00:12:59 Asia/Jerusalem

Canonical report:

`proofnet24/P20-kernel-hard-edge/runs/2026-09-16/2026-09-16_00-12-59__run-report.md`

Creation commit:

`88a0d315b181d22e2a32be1b729c28a01bfbdea2`

Report blob:

`b793fe636e7386197478b006bedac41cbaed8fab`

The canonical report was read back from the exact creation commit in complete contiguous ranges `1-260`, `261-520`, `521-780`, `781-1040`, and `1041-end`.

Readback exposed one notation-only serialization artifact in equation (3.4). The immutable report contains the rendered fragment

`s^2-1+` followed by `rac{12(s-2)}s\mathcal A(P)`

where the intended and mathematically used term is

` s^2-1+\frac{12(s-2)}s\mathcal A(P)`.

The corrected complete equation (3.4) is

\[
\overline R_s(P)=\frac{\alpha_d}{s-1}
\left[
 s^2-1+\frac{12(s-2)}s\mathcal A(P)
 +12b(P)-\frac{4(s-2)}s\delta(P)
\right].
\]

All subsequent algebra in the report already uses this intended coefficient, including the cancellation leading to equations (3.5)--(3.8). No theorem, constant, proof dependency, audit verdict, status, or next attack changes.

The original immutable report was not overwritten. No email/Gmail action was used.