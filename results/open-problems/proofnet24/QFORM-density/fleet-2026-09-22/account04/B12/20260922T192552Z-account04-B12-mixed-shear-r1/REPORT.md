# QFORM additional-eigenvalue control: mixed-norm shear compiler

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B12, 2026-09-22T19:25:52Z.

attacking: a dependence-safe compiler for adjoining arbitrary quadratic remainder eigenvalues.

## Status

This report proves a target-level reduction and applies the completed account01/B12 result to an actual inequality. It does not prove or disprove the full conjecture. The full universal bound remains open. The result concerns essential boundedness; continuity requires the separate translation-modulus condition stated below.

## The mixed-norm shear theorem

Let `(U,Z)` be an absolutely continuous random vector on `R x R^m` with joint density `h(u,z)`. Define

`M(h)=integral_{R^m} esssup_{u in R} h(u,z) dz`.

For every measurable `psi:R^m->R`, the random variable

`T=U+psi(Z)`

has density

`p_T(t)=integral h(t-psi(z),z) dz`

and

`||p_T||_infinity <= M(h)`.

The bound is uniform over `psi`; in particular it is uniform over all coefficients, signs, degeneracies and coincidences appearing inside a quadratic remainder `psi(Z)`.

### Proof

The shear map `(u,z)->(u+psi(z),z)` preserves Lebesgue measure in the first coordinate. Hence its joint density is

`h_psi(t,z)=h(t-psi(z),z)`.

Marginalizing in `z` gives the displayed density. For almost every `t`,

`p_T(t) <= integral esssup_u h(u,z) dz=M(h)`.

No independence of `U` and `Z` is used. Equivalently, the shear is an isometry of the mixed space `L^1_z(L^infinity_u)`, and marginalization is a contraction from that mixed space to `L^infinity_t`.

This also explains why the normalized worst conditional fiber is the wrong interface. Writing `g(z)=integral h(u,z)du`,

`M(h)=integral g(z)||p_{U|Z=z}||_infinity dz`,

so rare fibers are weighted before normalization. The quantity `esssup_z ||p_{U|Z=z}||_infinity` may be infinite while `M(h)` is finite.

## Continuity criterion

Define the mixed translation modulus

`Omega_h(a)=integral esssup_u |h(u+a,z)-h(u,z)| dz`.

Then

`||p_T(.+a)-p_T||_infinity <= Omega_h(a)`.

Consequently, if `Omega_h(a)->0` as `a->0`, then `p_T` has a bounded uniformly continuous representative, uniformly for every measurable remainder `psi`. This condition is sufficient and genuinely stronger than `M(h)<infinity`; an `L^infinity` density need not be continuous.

## Quadratic-form compiler

Let `X` be the original independent vector and decompose a quadratic form, without rotating the input law, as

`Q(X)=Q_core(X)+Q_rem(X)`.

Suppose there is an original-coordinate statistic `Z=Z(X)` for which `Q_rem(X)=psi(Z)` and `(Q_core(X),Z)` has a joint density `h` satisfying `M(h)<=C`. Then `Q(X)` has a density bounded by `C`, regardless of the number, sizes, signs or repetitions of the eigenvalues contributing to `Q_rem`.

This is dependence-safe: `Q_core` and `Q_rem` need not be independent. The price is exact and explicit: one must control the unnormalized scalar/vector level-set mixed norm `M(h)`. A bounded marginal density for the spectral projection, or a worst normalized conditional-density cap, does not supply this quantity.

## Application of the completed account01/B12 theorem

The designated partner result `QFORM-SCALAR-QREST-UNIFORM-CONDITIONAL-CAP-FALSE-v1` and its corrected Hadamard-cube calculation consider iid `X_i~Uniform[0,1]`,

`S=sum_i X_i`, `Y=S/2`, `R=X^T(I-J/4)X`.

It proves for the joint density of `(R,Y)` that

`||p_(R,Y)(.,y)||_infinity <=2 pi`, `0<=y<=2`.

Therefore the new compiler gives, for every measurable `psi:[0,2]->R`,

`||p_(R+psi(Y))||_infinity <= integral_0^2 2 pi dy =4 pi`.

In particular, for every real added eigenvalue `tau`, including either sign, zero and arbitrarily large magnitude,

`||p_(R+tau Y^2)||_infinity <=4 pi`.

This is a strict strengthening of the partner's stated one-parameter use: the same paid joint mixed norm controls every measurable scalar remainder of `Y`, not just `tau Y^2`. It demonstrates precisely how one extra dependent eigen-direction can be added without convolution.

The partner also proves that

`esssup_b ||p_(R|tau Y^2=b)||_infinity=infinity`

on edge fibers. Thus the compiler uses the strongest source-valid quantity and cannot be replaced by the refuted worst-fiber gate.

## Scope and remaining implication

This theorem does not show that every three-large-eigenvalue matrix admits a statistic `Z` with universally bounded `M(h)`. That is the remaining product-geometric task. A complete proof would need a dimension-free construction of a protected core/remainder statistic satisfying

`integral esssup_u p_(Q_core,Z)(u,z) dz <=C`

for every admissible matrix and every cap-one product input. Once that is obtained, all additional eigenvalues of arbitrary sign and magnitude are absorbed for free by the shear compiler. Continuity additionally requires a uniform mixed translation modulus.

The result respects all current corrections: it does not use pointwise van der Corput decay, an arbitrary-joint coarea bound, a bounded spectral-projection density alone, a worst normalized conditional fiber, or independence after rotation.

## Provenance

Partner source: `yspennstate/math-open-problems@75cc1919cc36254668f765d96357f41c4c91bcb6`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B12/20260922T182048Z-account01-B12-QFORM-r15/REPORT.md`, with correction addendum at `a2e722f65ccc60e5fddc764c7aa429127fee1bf5`.


Repository transport is not native brain ingestion. Status: `WITHOUT_VERIFIED_BRAIN`.
