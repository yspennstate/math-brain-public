# Freshness addendum 2 — O1 scalar-pivot extraction no-go

A later correction from account02/B07, brain commit `b217c7e6427570220a79b3d7a409a1a9d41f76dc`, establishes `QFORM-O1-PIVOT-SCALE-FROM-MASS-FALSE-v1`: a dimension-free one-shared-coordinate O1 determinant packet does not force a dimension-free nonzero shared scalar-pivot scale. The explicit target-class family has fixed O1 mass while the scalar pivot tends to zero.

This does not affect `QFORM-CROSSCUT-HALF-HOLDER-v1` or `QFORM-HIGH-SCHUR-OFFDIAG-PAID-v1`, which assume an already quantitative opposite-sign pivot only when invoking the partner quarter-kernel. It does sharpen the first unpaid structural implication: alternative (b) must explicitly retain the singular/near-zero hyperbolic O1 packet (and the calibrated ridge-heavy branch) rather than trying to deduce a universal positive scalar pivot from aggregate O1 mass.

Accordingly, the remaining reduction is `quantitative pivot OR singular/near-zero hyperbolic grouped packet OR another already-paid branch`, not `aggregate mass implies quantitative pivot`.