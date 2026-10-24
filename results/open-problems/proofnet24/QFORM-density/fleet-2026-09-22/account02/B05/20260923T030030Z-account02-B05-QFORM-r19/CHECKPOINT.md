SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B05, 2026-09-23T03:00:30Z.
attacking: the exact-rank-three indefinite two-sheet heavy-near-null branch via a product-preserving fixed-gap coarea/local-L1 estimate

# Early substantive checkpoint — fixed-gap hub/pair coarea and the first perturbative loss

Run `20260923T030030Z-account02-B05-QFORM-r19`. Full QFORM remains open.

## 1. A fixed-gap two-sheet lemma that does not take a curved-fiber supremum

Let `H` be independent of a pair `(V,U)`. Assume `H` has probability density `f_H` with `||f_H||_infinity<=L`, while `(V,U)` has an arbitrary joint probability density `rho` with `||rho||_infinity<=K`. Let `c!=0`, `d>0`, and

`Q=2cHV+dU^2`.

Then for every `a>0`, the density on the minority/two-sheet side obeys

`p_Q(-a) <= sqrt(pi*K*L/(2|c|)) * (a*d)^(-1/4)`.             (1.1)

Translations and affine terms that are removable by translating `H,V,U` preserve the same estimate relative to the corresponding critical value.

Proof. Integrating first in the genuinely independent scalar `H` gives, with `C(u)=(a+d u^2)/(2|c|)`,

`p_Q(-a) = (1/(2|c|)) int_R int_R rho(v,u) f_H(-C(u)/v) |v|^(-1) dv du`.

For fixed `u`, Cauchy-Schwarz in `v`, `rho<=K`, and `f_H^2<=L f_H` give

`int rho(v,u) f_H(-C/v) |v|^(-1) dv`
` <= p_U(u)^(1/2) [K L int f_H(-C/v) v^(-2) dv]^(1/2)`.

The reciprocal substitution `x=-C/v` is exact and uses the mass, not the supremum, of `f_H`:

`int_R f_H(-C/v) v^(-2) dv = C^(-1) int_R f_H(x) dx = C^(-1)`.

Therefore

`p_Q(-a) <= sqrt(KL/(2|c|)) int_R p_U(u)^(1/2) (a+d u^2)^(-1/2) du`.

A second Cauchy-Schwarz uses only `int p_U=1`:

`int p_U(u)^(1/2)/(a+d u^2)^(1/2) du`
` <= [int_R du/(a+d u^2)]^(1/2)`
` = sqrt(pi) (a d)^(-1/4)`.

This proves (1.1). The proof is an interval/coarea calculation through a reciprocal change of variables; it never bounds a curved fiber by its unrestricted supremum.

For an orthonormal two-dimensional projection `(V,U)` of an original cap-one product law, the source-valid Ball/Livshyts-Paouris-Pivovarov projection theorem used in the required Claude package gives `K<=2`. Thus with a cap-one independent hub and `c=d=1`,

`p_Q(-a) <= sqrt(pi) a^(-1/4)`, and in particular `p_Q(y)<=sqrt(pi)` for every `y<=-1`.               (1.2)

This applies directly to the exact null-hub normal form `2 X_h V+U^2`, including dependent projected `(V,U)`; genuine independence is used only between the original physical hub `X_h` and the leaf pair.

## 2. Actual application of the required newest-Claude source

The required source `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`, proves the ruled one-sheet estimate for exact-rank-three signature `(2,1)` and, crucially, supplies the cap-two two-dimensional projection theorem at the place used above. Hence on the normalized null-hub target form the source pays the majority side by `pi sqrt(2)`, while (1.2) pays the fixed-gap two-sheet side by `sqrt(pi)`. The account01/B15 fixed-gap reduction shows why the latter is the correct positive-volume object: the sharp scaled minority problem is equivalent to unit windows centered at levels `<=-1`.

This is not a claim that exact rank three is now fully proved: the heavy row of leverage `l in (1/2,1)` produces the perturbed hub `T=sqrt(l)X_h+epsilon Z`, `epsilon=sqrt(1-l)`, with `Z` generally sharing the leaf product coordinates with `(V,U)`.

## 3. The first perturbative attempt and its exact missing factor

Consider the near-null normal form

`Q_epsilon = 2c (X+epsilon Z) V + d U^2`,                    (3.1)

where `X` is an original cap-one coordinate independent of the leaf triple `(Z,V,U)`, but that triple may be a dependent three-dimensional product projection. Let its joint density be `rho_3<=K_3`, and let

`m(z,u)=int rho_3(z,v,u) dv`

be the `(Z,U)` marginal density. Repeating the fixed-gap Cauchy calculation **before** integrating `z` gives, for `a>0`,

`p_{Q_epsilon}(-a)`
` <= sqrt(K_3/(2|c|)) * int_R int_R sqrt(m(z,u))/(a+d u^2)^(1/2) dz du`.       (3.2)

The translation `-epsilon z` disappears from the reciprocal Jacobian, so no factor of `epsilon` is gained. Equation (3.2) isolates the exact loss of this natural perturbative extension: the uncontrolled Hellinger-spread functional

`H_a(m)=int int sqrt(m(z,u))/(a+d u^2)^(1/2) dz du`.             (3.3)

This factor is not uniformly bounded under the owner hypotheses. Even in a completely source-valid disjoint-bank target family, take `Z` independent of `U` with `Z~Unif[0,R]` (density `1/R<=1`) and `U~Unif[0,1]`. Then

`m(z,u)=R^(-1) 1_[0,R](z) 1_[0,1](u)`,

so for every fixed `a,d>0`,

`H_a(m)=sqrt(R) int_0^1 (a+d u^2)^(-1/2) du -> infinity`.      (3.4)

Yet in this disjoint-bank example `X+epsilon Z` is genuinely independent of `(V,U)` and its density cap is at most one, so Theorem (1.1) applies directly after aggregating `X+epsilon Z` **before** the reciprocal payment and gives a uniform two-sheet bound. Thus the blow-up in (3.4) is a proof artifact, not a QFORM counterexample.

The exact lesson is source-valid and narrower than the already-known generic fiber-supremum correction: slicing the additive leaf correction `Z` before reciprocal integration loses a factor measuring the square-root spread of the `(Z,U)` marginal. A successful near-null argument must aggregate the additive noise with the hub first when independence permits, or use a genuinely overlap-sensitive product-coordinate estimate when `Z` shares coordinates with `(V,U)`.

## 4. Partner interface

The newest completed designated-partner report available at the fresh lookup is account03/B05 r20, theorem `QFORM-THREE-ARM-FROBENIUS-COAREA-v1`. Its proof conditions on an entire coefficient side and averages the reciprocal of the **maximum of three independent coefficient resources**, paying the third diffuse arm through a Hilbert--Schmidt small-ball bound before any local inversion. This is precisely the compatible escape from the Hellinger loss above when the troublesome correction can be routed to a disjoint third arm. The remaining two-sheet debt is therefore the genuinely overlapping case: the near-null correction `Z`, the hub arm `V`, and the transverse square `U` share original physical coordinates, so neither (1.1) nor the partner's disjoint three-arm tensorization may be invoked by pretending post-rotation independence.

Next step: attack that overlap directly, preferably at the fixed-gap unit-window level, or construct a product-law falsifier to a proposed overlap inequality. Full QFORM remains OPEN.
