# Prepublication addendum — late Pluecker correction and independent peer interface

After `REPORT.md` was committed, the fresh control/correction refresh reached `math-research-brain@3ab471deaeaab69f7494d32110b9884b705249f7`, still on owner revision `2026-09-22.5`, and added `QFORM-PLUCKER-PIVOT-SUPPORT-DISJOINT-v1` from fleet02/B06. That correction refutes direct averaging of a two-pivot endpoint certificate against same-sign Pluecker weights in a Sylvester--Hadamard family. It does **not** invalidate `QFORM-SPAN-ALIGNED-PLUCKER-AGGREGATION-v1`: the new theorem first aggregates the original product law into a two-dimensional block projection and only then pays curvature, rather than averaging reciprocal physical-pair certificates.

The same fleet02/B06 report proves `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`: if `R` has orthonormal columns and the original coordinates have density caps one, then `R^T X` has density at most `exp(k/2)`. For `k=2` this gives exactly the aggregate cap `e` used in equation (2.1) of `REPORT.md`. After whitening a non-orthonormal two-row block with Gram determinant `D_L`, it gives

`||p_(y_L.X_L,z_L.X_L)||_infinity <= e D_L^(-1/2)`.

Therefore the late completed worker result independently supplies the same actual inequality used in the main proof. Source: `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

The refresh also contains `QFORM-ONE-HEAVY-ROW-SAME-SQUARE-ABSORPTION-FALSE-v1`. The main theorem does not use the refuted one-heavy-row absorption step; it requires the exact block-span identity `s_L=alpha y_L+beta z_L` and performs a valid two-dimensional output-square completion. Thus its stated scope is unchanged.

**Status after correction refresh:** supporting theorem remains proved in its stated exact-rank-three/span-aligned scope; full QFORM and continuity remain open. The first unpaid implication remains a three-projection product-origin coarea estimate for nonzero triple-Pluecker defect `E_L>0`.
