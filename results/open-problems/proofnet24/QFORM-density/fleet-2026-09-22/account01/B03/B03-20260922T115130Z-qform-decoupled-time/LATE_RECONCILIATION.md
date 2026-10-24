# Late reconciliation — concurrent B09 convergence

After the B03 immutable report/finish was committed, a concurrent account01/B09 result became visible on `main` and was read from its canonical source:

- `yspennstate/math-open-problems@6dc9ff8894e196a28a48c3eb6ce917103722f0ec`
- `proofnet24/QFORM-density/fleet-2026-09-22/account01/B09/20260922T114609Z-account01-B09-qform-bilinear-v1/REPORT.md`
- blob `e457aea7bfc58bc2e79cb2a9836399c93e3d241b`.

This independently proves and strictly generalizes the main B03 mixed-minor theorem to arbitrary disjoint coordinate cuts of cross rank `r>=3`; when both blocks have size exactly `r`, B09 recovers exactly B03's sharp square-block constant

`||p_Q||_infinity <= [r/(r-2)] |det A[I,J]|^(-1/r)`.

Therefore B03's theorem should be treated as an independent concurrent derivation / exact-square-block specialization, not as a uniquely new fleet result.

More importantly, B09 partially pays B03's stated first unpaid implication. For exact rank three `A=R Lambda R^T`, B09 defines `w_I=det(R_I)^2`, leverage `ell_i=||R_i||^2`, and proves disjoint basis-pair mass

`M_disj >= 1-sum_i ell_i^2 >= 1-3 delta`, `delta=max_i ell_i`.

A random coordinate cut then yields a rank-three cross block with singular-value product

`D >= sqrt(M_disj)/8`,

so the bilinear-cut theorem gives

`||p_Q||_infinity <= 12 M_disj^(-1/6)`

whenever `M_disj>0` (in particular `delta<1/3`). B09 further closes the **exact-rank-three definite** branch universally with an explicit constant `<13.5` by combining this diffuse cut with a high-leverage local smoother.

Thus the next blocker is narrower than B03's original finish record: determinant-mass aggregation is already available for the exact-rank-three diffuse branch. The live unpaid bridge is now the **localized indefinite exact-rank-three branch and/or stability under additional spectral components**. In particular, one must show that the full hypothesis with at least three large eigenvalues either produces a controlled rank-3 cross cut/local smoother after extra spectral components are included, or find a different product-coordinate mechanism robust to their cancellation.

Full QFORM target remains OPEN. This note does not rewrite the immutable B03 report or finish receipt; it records the later concurrent dependency closure honestly.