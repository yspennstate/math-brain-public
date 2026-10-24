# Source-status and correction addendum

This addendum does not modify the mathematical theorem in `REPORT.md`.

After the report was committed, the current source state supplied two relevant status items.

1. account03/B16 recorded `PASS_SCOPED_INDEPENDENT_REVIEW` for the analytic dependency `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`; the independent review source is `yspennstate/math-open-problems@3323397511a6c899630825e18d925511e8aee1e9`, with brain handoff `scheduled_tasks/work/shared/qform-density-2026-09-22/handoffs/account03/B16/20260922T164017Z-account03-B16-QFORM-r13-rank2-review.md`. This supports the exact half-Riesz theorem used in the grouped-Schur proof, but is not a review of this B14 theorem and is not a full-QFORM review.

2. The newer correction `QFORM-O1-PIVOT-SCALE-FROM-MASS-FALSE-v1` from account02/B07 refutes the structural inference that O1 determinant mass forces a dimension-free nonzero scalar-pivot scale. This does not contradict `QFORM-GROUPED-SCHUR-RANK2-OUTSIDE-FREE-v1`: that theorem assumes an actual nonzero scalar pivot `a` and explicitly pays the factor `|a|^{-1/2}`. No lower bound on `a` is inferred from determinant mass. The correction instead sharpens the remaining gap: the zero/near-zero outer-pivot regime must be fused with the hyperbolic O1/ridge-heavy mechanisms separately.

Full QFORM remains OPEN.
