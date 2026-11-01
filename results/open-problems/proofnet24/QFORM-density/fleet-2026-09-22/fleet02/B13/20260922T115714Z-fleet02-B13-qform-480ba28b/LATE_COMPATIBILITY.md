# Late compatibility note — fleet01/B15 rank-3/4 local closure

After the main B13 report was frozen, fresh main exposed fleet01/B15's completed handoff and canonical report:

`yspennstate/math-open-problems@47dc925729bbf269333cc6e1256178a538d2f553`
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B15/20260922T120320Z-fleet01-B15-qform/REPORT.md`.

It proves that every real symmetric matrix of rank at least three has an invertible original-coordinate principal block of order 3 or 4, and consequently every fixed target matrix has an instancewise bounded output density

\[
\|p_{X^TAX}\|_\infty\le {4\pi+8\over \kappa_{34}(A)},
\]

where `kappa_34(A)` is the maximum smallest singular value over invertible principal blocks of order 3 or 4. This is fully compatible with the B13 bang-bang reduction: for every product set of one-dimensional measure one,

\[
|\{x\in\prod_iE_i:a\le x^TAx\le a+\varepsilon\}|
\le {4\pi+8\over\kappa_{34}(A)}\,\varepsilon.
\]

Thus, after the exact arbitrary-density-to-product-set reduction, **absolute continuity and finite `L^infinity` for each fixed rank>=3 matrix are already closed**. The remaining owner-level difficulty is only the dimension- and matrix-independent constant, i.e. removal of the factor `1/kappa_34(A)` by an aggregate/delocalized mechanism.

This sharpens but does not alter the main report's unpaid implication. In `QFORM-AGGREGATE-BANGBANG-SLAB-v1`, “every fixed low-dimensional principal block is quantitatively weak” should be read as including both 3x3 and 4x4 principal blocks. Flat/delocalized rank-three frames show that `kappa_34(A)` may be small even when three spectral eigenvalues have magnitude at least one, so selecting one local block cannot by itself provide the universal constant.

No full solution is claimed.
