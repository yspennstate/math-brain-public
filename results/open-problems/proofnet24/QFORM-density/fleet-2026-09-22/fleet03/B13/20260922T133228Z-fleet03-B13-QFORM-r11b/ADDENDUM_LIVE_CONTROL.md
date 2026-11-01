# Addendum — fresh QFORM continuation and residual chamber

After the main report was committed, fresh owner control added `QFORM-EXCLUSIVE-CONTINUE-20260922T131746Z`: continue exclusively on the full QFORM target; auxiliary results do not end the assignment. The programme/revision remain `QFORM-DENSITY-3EIG-20260922` / `2026-09-22.5`. Full QFORM remains **OPEN**.

I consumed the newly source-pinned regularized-determinant handoff `math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`. It proves, among other things, a bounded continuous density `<27` when the projection onto the **entire** range of `A` has every coordinate leverage at most `1/32`, while allowing arbitrary extra small eigenvalues. This does not remove the heavy-coordinate remainder.

I also consumed the completed rank-three bilinear-cut theorem `QFORM-RANK3-VOLUME-CUT-v1` and definite closure `QFORM-RANK3-DEFINITE-UNIVERSAL-v1` from fleet01/B09, plus the heavy-row trichotomy `QFORM-RANK3-HEAVY-TRICHOTOMY-v1` from fleet01/B10.

Combining those completed results with the new theorem in `REPORT.md` gives the following exact synthesis corollary.

## Corollary — residual rank-three chamber after the present run

Any exact-rank-three instance not already paid by the cited source theorems and this run can be assumed to satisfy **all** of the following:

1. the signature is indefinite (the all-same-sign rank-three class is already universally bounded by fleet01/B09);
2. the maximum physical spectral-row leverage is strictly greater than `1/2` (the diffuse rank-three theorem closes leverage `<=1/2`);
3. after selecting such a heavy row, the instance lies in one of the two hard alternatives of the heavy-row trichotomy: either a second residual-heavy direction exists, or the heavy row is near-isotropic with the certified strong cross coupling; the residual-diffuse non-isotropic alternative is already bounded;
4. the spectral-frame rows use an **unbounded** number of projective directions along any putative counterexample sequence, because `QFORM-RANK3-FINITE-PROJECTIVE-BANKS-v1` proves a finite bound `2(2*pi+3*sqrt(3))*binom(m,3)` for every fixed direction count `m`.

Thus the rank-three frontier is not merely “localized indefinite.” It is localized indefinite **and** projectively high-complexity. Any next B13 extremal-law attack should preserve that high-cardinality geometry rather than return to a finite-bank or single-minor argument.

For arbitrary rank, the fresh regularized-determinant theorem gives a separate necessary condition on any remaining counterexample: the projection onto the entire nonzero spectral range must have some coordinate leverage greater than `1/32` (unless another already-paid branch applies). This is not a reduction from arbitrary rank to rank three; the extra-spectrum interaction remains unpaid.

## Next mechanism

The next useful B13 attack is therefore a heavy/high-cardinality product-law inequality: combine the exact bang-bang finite-fragment reduction with an aggregate determinant/cross-cut functional **before** any reciprocal local-minor payment, on the indefinite rank-three chamber above. A successful inequality must be stable under arbitrary fragment separation and must not condition on projected leakage variables whose conditional density caps are known to blow up.
