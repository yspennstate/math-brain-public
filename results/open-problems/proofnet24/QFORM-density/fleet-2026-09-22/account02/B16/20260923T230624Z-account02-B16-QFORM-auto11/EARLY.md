# account02/B16 early calculation — minority-sign pivot discriminant receiver

Programme `QFORM-DENSITY-3EIG-20260922`; full unrestricted target remains OPEN.

Pinned source actually used: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, especially the completed bounded two-dimensional product-projection marginal used in `COUNTEREXAMPLE_SEARCH.md` and the source-integrity warnings in `RESULTS.md` / `FOURIER_ROUTE_REPORT.md`. Latest compatible designated partner read: account03/B16 `20260923T210312Z-account03-B16-QFORM-r34`, whose fixed-P Minkowski mixed norm diverges for authentic fragmented product projections.

## First implication

Let `H` be an untouched original coordinate with density cap one, independent of a random pair `Z=(L,V)` having joint density `rho` with `||rho||_infinity<=M`. No independence between `L` and `V` is assumed. Consider the affine quadratic

`Q = a H^2 + 2 H u^T Z + Z^T C Z + r H + s^T Z + c`,

where `a!=0`, `u in R^2`, and `C=C^T`. Let

`B = [[a,u^T],[u,C]]`

be the 3x3 quadratic coefficient matrix, and define the conditional half-discriminant

`D_q(z) = (u^T z+r/2)^2 - a(z^T C z+s^T z+c-q)`.

For fixed `z`, every real root in `H` has derivative magnitude `2 sqrt(D_q(z))`, so the sum of the two root contributions is at most `D_q(z)^(-1/2)`. Hence

`p_Q(q) <= integral rho(z) [D_q(z)]_+^(-1/2) dz`.

The quadratic matrix of `D_q` is

`K = u u^T - a C`,

and the 3x3 Schur determinant identity gives exactly

`det K = a det B`.

If `a det B>0`, then the symmetric 2x2 matrix `K` is definite. Completing the square, for every `tau>0` and every `q`,

`Leb{z: 0 < D_q(z) < tau^(-2)} <= pi tau^(-2) / sqrt(a det B)`.

Therefore the layer-cake bound and `rho<=M` give

`p_Q(q) <= integral_0^infinity min(1, pi M tau^(-2)/sqrt(a det B)) d tau`

`= 2 sqrt(pi M) (a det B)^(-1/4)`.

Thus

**`||p_Q||_infinity <= 2 sqrt(pi M) (a det B)^(-1/4)` whenever `a det B>0`.**

For a genuine orthonormal two-dimensional projection of a disjoint original-coordinate product bank, the pinned product-projection theorem gives `M<=2`, so

`||p_Q||_infinity <= 2 sqrt(2 pi) (a det B)^(-1/4)`.

This is a curved use of the JOINT two-dimensional marginal only; it never upgrades `(L,V)` to independence or to a conditional density cap.

For a signature `(+, +, -)` carrier, `det B<0`, so the gate `a det B>0` means the physical hub diagonal `a` has the minority (negative) sign. For signature `(+, -, -)`, it likewise means the hub diagonal has the minority positive sign. Thus a minority-sign nonzero hub pivot plus a two-dimensional product marginal is a fully paid global branch.

The gate is structural, not cosmetic. If `a det B<0`, then `K` is indefinite and the discriminant level tubes are hyperbolic; a mere bounded joint pair density has no finite-area weak-L2 control. This is the same geometry behind the live prohibition on arbitrary-joint/two-sheet shortcuts.

Next: connect this endpoint to the partner-r34 shared-P survivor. The new receiver pays the entire two-dimensional leaf endpoint but cannot condition on the third projected coordinate `P`; r34 proves that freezing `P` and integrating its slice norm by Minkowski is not uniform. The unpaid object is therefore genuinely vector-valued/TT* in `P`, not the two-dimensional discriminant trace itself.
