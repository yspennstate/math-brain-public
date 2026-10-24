# QFORM account01/B01 early substantive checkpoint

Run: `20260923T083643Z-account01-B01-qform-auto11`.
Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: supporting averaged-frequency derivation in progress; full QFORM OPEN.

## New route: leverage-free rank-two cross + exact three-dimensional receiver curvature

Split ORIGINAL independent coordinates into disjoint banks `I,J`. Let the physical cross block have rank two

`K=A_{IJ}=U diag(kappa1,kappa2) V^T`, `Delta=kappa1*kappa2>0`,

and assume the entire receiver self-curvature is supported on the three-dimensional subspace `S=span(V,w)`, where `w` is a unit vector orthogonal to `range(V)`. Write, in the orthonormal coordinates `(y,z)=(V^T X_J,w^T X_J)`,

`X_J^T A_{JJ} X_J = q(y,z)`

with nonzero transverse coefficient `a = (1/2) partial_z^2 q = w^T A_{JJ} w !=0`. No leverage bound on `S` is imposed.

The first essential estimate is a genuinely frequency-averaged replacement for the failed pointwise scalar Fresnel bound. Push the `I`-bank complex amplitude through `K^T X_I`; its density has `L2` norm at most `sqrt(2/Delta)`. Let `rho(y,z)` be the ordinary three-dimensional product projection density on `S`; the source LPP bound gives `rho<=M3=2^(3/2)`. For

`h_t(y)=int rho(y,z) exp(i t q(y,z)) dz`,

fixing `y` leaves a one-dimensional quadratic phase `a(z+b_y)^2+const`. The previously proved cubic quadratic-phase budget, applied to the unnormalised slice of mass `m(y)=int rho(y,z)dz`, gives

`int_R |h_t(y)|^3 dt <= 72*pi*M3^2*m(y)/|a|`.

Hence, with `G(t)=||h_t||_3`,

`int G(t)^3 dt <= 576*pi/|a|`.

On the other hand two-dimensional Plancherel in the random cross coefficient gives

`|phi_Q(t)| <= pi*sqrt(2/Delta)*|t|^(-1)*||h_t||_2`

and `||h_t||_2 <= ||h_t||_1^(1/4)||h_t||_3^(3/4) <= G(t)^(3/4)`. Therefore

`|phi_Q(t)| <= pi*sqrt(2/Delta)*|t|^(-1)*G(t)^(3/4)`.

This is not a law-uniform pointwise power envelope because `G(t)` is allowed to spike. But `G^3` is integrable, so Holder on the tail gives an `L1_t` bound for `phi_Q`; the phase-aligned fragmented-support counterexample is therefore preserved rather than contradicted.

Optimising the split `|t|<=T` / `|t|>T` yields the provisional constant

`||p_Q||_infinity <= (15/2^(1/5)) * Delta^(-2/5) * |a|^(-1/5)`

`= 13.0582584495... * Delta^(-2/5) * |a|^(-1/5)`.

Next steps in this same run: check every Fourier/Plancherel constant, state exact affine/support scope, apply the completed account02/B01 grouped-rank-two/Fresnel theorem to the common low-leverage branch, and build a strict-N3 high-leverage stress family where the partner leverage gate fails but this mixed-time estimate remains uniform.
