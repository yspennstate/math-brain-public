# account02/B13 handoff — support-free near-null hyperbolic interpolation

Programme `QFORM-DENSITY-3EIG-20260922`; full target remains **OPEN / NOT PROVED**. Execution: `WITHOUT_VERIFIED_BRAIN`.

Canonical mathematics is read back at:

`yspennstate/math-open-problems@94bb5d8d6a87b78d1cdda3e8db9f00d07c494e5c`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260922T172625Z-account02-B13-productset-r13/REPORT.md`

Checker source/output are in the same immutable run root and the output ends `QFORM_NEAR_NULL_CHECK_PASS`.

## New result actually closing the designated-partner gap

Apply account03/B13's completed null-product theorem at `math-open-problems@a7594ff13b36fbc1819f60ec287e8232bd39974d` and account03/B16's weak-`L^2` logarithmic-ridge theorem at `math-open-problems@c301be6b21f382934962aeb4c019b713377eac2f`.

For independent cap-one `U,V` and

`q(u,v)=a u^2+2buv+c v^2`, `b!=0`, `|a|,|c|<=|b|/2`,

define `D=b^2-ac`, `delta=sqrt(D)`, `kappa=(|b|+delta)/2` after reflecting one variable, `r=c/(2kappa)`, `s=a/(2kappa)`, and `theta=1+(|r|+|s|)/2`. After arbitrary affine terms, with `t_*` the critical value,

`p_q(t) <= (2/delta) asinh(theta sqrt(2kappa/|t-t_*|))`

and therefore

`boxed(p_q(t) <= (2sqrt(3)/|b|) Psi((t-t_*)/(2|b|)))`.

The proof parameterizes the actual perturbed hyperbola. On each sign branch `x=e^t`, the inverse physical coordinates have multiplicity at most two and satisfy the exact derivative identities `x=U'+rV'`, `y=-(sU'+V')`. This bounds the two exponential moments of the incidence density, after which the partner's centered-cosh rearrangement yields the asinh envelope. No matrix/slab continuity, support localization, moments, or bounded fragment count is used.

Combining this with the B16 weak-`L^2` ridge theorem gives: if an arbitrary ambient symmetric matrix has a physical principal triple

`B=[[a,b,p],[b,c,q],[p,q,gamma]]`, `det B!=0`, `|a|,|c|<=|b|/2`,

then, with arbitrary outside quadratic coefficients/cross couplings,

`boxed(||p_Q||_infinity <= 33.740479511421 (|b||det B|)^(-1/4))`.

For an exact-rank-three spectral frame, replacing the third physical coordinate by the normalized original-coordinate tail aggregate gives

`||p_Q||_infinity <=43.323633263897 (|b||det Lambda| Delta)^(-1/4)`,

where `Delta=||r_i wedge r_j||^2`, under the same near-null condition on the pair compression.

Together with account03/B16's nonzero-diagonal pivot theorem, every invertible physical `3x3` block has the pivot-free local bound

`boxed(||p_Q||_infinity <=73.692469625551 (m |det B|)^(-1/4))`,

where `m=max_{i<=j}|B_ij|`.

By account02/B13's exact bang-bang reduction at `math-open-problems@604a08009638981da254a72f09a24dd50e3a3c94`, all these estimates transfer with identical constants to arbitrary unit-measure product-indicator slab volumes.

## Remaining implication

`QFORM-AGGREGATE-NEAR-NULL-DETERMINANT-PAYMENT-v1`: convert the current finite-heavy-core/grouped-coordinate determinant packets into a dimension-free payment without selecting and reciprocating one tiny fixed triple. Aggregate the diffuse bordered-minor bank in the original independent coordinates before the reciprocal fourth-root step; use the new near-null pair envelope on hyperbolic fibers and the existing orientation-free rank-two affine half-Riesz theorem on complementary orientations. Arbitrary additional spectrum remains part of the obligation.

Fresh owner control/corrections were reread before publication; no refuted pointwise-decay, post-rotation-independence, conditional-cap, fixed-minor dichotomy, bounded-diameter, fixed-fragment, fiber-sup, or operator-norm slab-continuity premise is used.