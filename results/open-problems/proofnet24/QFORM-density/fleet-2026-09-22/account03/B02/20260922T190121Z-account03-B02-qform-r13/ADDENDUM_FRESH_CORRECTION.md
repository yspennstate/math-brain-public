# Fresh correction addendum — near-zero half-Riesz alone is not enough

After the main report and initial receipt were written, fresh control merged `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1` from account01/B06 (`yspennstate/math-open-problems@b74210c7e963a11c1f0532f98f5d705278967cd1`).

The correction states: exact zero Schur diagonal can admit a product-preserving affine half-Riesz bound, but replacing the zero by merely `|S_ii|` small while retaining only a cross-row norm is false. The rank-one family `[[epsilon,1],[1,epsilon^(-1)]]` has fixed cross-row norm but divergent half-Riesz potential.

This does **not** invalidate `QFORM-RANK3-OVERLAP1-INTEGRATED-FOURIER-v1`: that theorem uses a genuinely nonzero scalar pivot and a second, independent residual resource `d_i`, the disjoint-pair exterior mass, to construct two full two-dimensional physical banks before applying any Fourier bound.

It **does** sharpen the next unpaid implication. The next mechanism may not use only

`sum_{j!=i} A_ij^2 >= c_i-A_ii^2`

plus `|A_ii|` small. It must retain additional product-preserving transverse geometry, for example the residual disjoint-pair mass `d_i`, a quantitative two-bank Gram determinant, or a pair-log certificate. In particular the new target is:

`QFORM-NEAR-ISOTROPIC-OVERLAP1-OFFDIAGONAL-v2`: on the overlap-one mass with `|A_ii|` small, combine the forced off-diagonal row energy **and** the nontrivial residual two-bank exterior mass `d_i` before any reciprocal small-pivot or half-Riesz payment. Treat the exact-zero pivot separately from merely small pivots.

Full QFORM remains OPEN. Essential boundedness in the scope of the main theorem is unchanged; continuity remains unproved.
