# PROB20-17 — append-only correction and delivery receipts for `2026-09-16T133525Z`

## Typographical correction to the main report

The main report at

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-17/runs/2026-09-16/2026-09-16T133525Z__report.md`

contains two TeX/transcription defects introduced during delivery. They do **not** change any mathematical claim, inequality, certificate, or proof step.

1. In Section 3, the displayed rank-one product factorization should read

\[
A_{i_1}\cdots A_{i_7}
=
\left(\prod_{r=1}^{6}\langle u_{i_r},u_{i_{r+1}}\rangle\right)
u_{i_1}u_{i_7}^*,
\]

where the final vector factor is `u_{i_1}u_{i_7}^*`. The main report accidentally rendered the first `u` with an extra backslash/newline sequence. The intended and correct formula is

\[
A_{i_1}\cdots A_{i_7}
=
\left(\prod_{r=1}^{6}\langle u_{i_r},u_{i_{r+1}}\rangle\right)
 u_{i_1}u_{i_7}^*.
\]

2. Immediately after equation `(6.6)`, the display-closing delimiter `\]` is missing. Equation `(6.6)` itself is unchanged and is

\[
\frac{D_7(g)}{5040}
=
\mathbb E\frac{N_H(\Gamma)}{5040}
\le
\mathbb EF_7(Q)
\le
\mathbb E\psi(Q).
\tag{6.6}
\]

All later references use these intended formulas.

## Delivery receipts

Main report:

* path: `probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-17/runs/2026-09-16/2026-09-16T133525Z__report.md`
* commit: `49f6d245e320319b4b94f84886c10031df449b48`
* blob: `0aa0f4514502f803dc0a5470a031a48c71029727`
* status: **VERIFIED** — read back at that exact commit.

Exact certificate:

* path: `probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-17/artifacts/2026-09-16T133525Z__verify_k7_convex_order.py`
* commit: `6cd1dc67667d13b9031421f8ca6a799213f4422e`
* blob: `2e7500f248e721f394585cc1bc8fdeb06be2fc08`
* status: **VERIFIED** — read back at that exact commit.

The exact certificate had already been executed locally before upload and all assertions passed. No previous task files, peer files, shared indexes, workflows, or settings were overwritten.
