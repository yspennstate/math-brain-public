# r41 boundary erratum

This is a clerical endpoint correction to `REPORT.md`; no theorem or constant changes.

In the designated-partner application, the anisotropic exact-rank-two family has cross singular values `s1=LR`, `s2=L/R`, `s3=0`. Under the r41 taxonomy

- R1 means `s2<L/8`;
- R2 means `s2>=L/8` and `s3<L/64`.

Therefore the correct split is

- `3<=R<=8`: R2;
- `R>8`: R1.

The report/handoff/memory/receipt wording `3<=R<8` for R2 and `R>=8` for R1 misclassified only the single boundary value `R=8`. At `R=8`, `s2=L/8`, so it is R2. The partner bound `||p||infinity<7.251/L`, the r41 paid-rank-three bound `<47.067/L`, and the unresolved leakage-stability implication are unchanged.
