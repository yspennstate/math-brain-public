# General convex-functional localization meta-lemma

This file records the abstract form underlying `REPORT.md`. It is stronger than the conditional `L^p` specialization and gives an exact law-class reduction for the full QFORM density constant.

## Theorem G.1 — `QFORM-CONVEX-TV-EXTREME-LOCALIZATION-v1`

Fix masses `m_i in (0,1]`. Let

`C_{m_i}={f:R->[0,1] measurable: int f=m_i}`.

Let `(Omega,nu)` be any finite measure space, let `S` be a measurable output space, and let

`T: Omega x R^n -> S`

be measurable. For `f=(f_1,...,f_n)` write

`mu_f = T_#(nu(domega) prod_i f_i(x_i)dx_i)`.

Let `Phi` be any extended-real functional on finite positive measures on `S` that is

1. convex, and
2. lower semicontinuous for total-variation convergence.

Then

`sup_{f_i in C_{m_i}} Phi(mu_f)`

is exactly

`sup Phi(mu_{1_{E_1},...,1_{E_n}})`,

where each `E_i` is a bounded finite union of intervals with `|E_i|=m_i`.

No common support radius, diameter bound, fragment-count bound, location bound, or moment bound is introduced.

### Proof

For each coordinate, the fixed-mass cap-one class is the `L^1` closure of the convex hull of indicators of bounded finite-union sets of the same mass.

First truncate `f` on `[-R,R]` and replace the missing tail mass `delta_R` by the indicator of any interval disjoint from `[-R,R]` of length `delta_R`. This preserves the cap and the mass exactly, and changes `f` in `L^1` by at most `2 delta_R`, which tends to zero.

Now let `g` be compactly supported, cap one, and have mass `m`. Fix an integer `K` and partition the line into cells of length `h=m/K`. Average `g` on the finitely many relevant cells. If `a_j` denotes the cell average, then `0<=a_j<=1` and `sum_j a_j=K`. Thus `a=(a_j)` lies in the hypersimplex

`P={a in [0,1]^N: sum_j a_j=K}`.

Every extreme point of `P` is a `0/1` vector with exactly `K` ones: if two coordinates were strictly fractional one could perturb them by `(+eps,-eps)`, while an extreme point cannot have exactly one fractional coordinate because the coordinate sum is the integer `K`. Hence `P` is the convex hull of its `0/1` points. Therefore the cell-average density is an exact finite convex mixture of indicators of unions of exactly `K` cells, each union having total measure `Kh=m`. Letting the mesh tend to zero gives the desired `L^1` approximation.

Tensor the coordinatewise finite mixtures. The resulting product density is a finite convex mixture of product extreme densities. Product `L^1` convergence implies total-variation convergence of the source measures, and pushforward by `T` contracts total variation. If `S_ext` denotes the extreme-law supremum, convexity gives `Phi(mu_{g^(k)})<=S_ext` for every finite mixture approximation, while total-variation lower semicontinuity gives

`Phi(mu_f)<=liminf_k Phi(mu_{g^(k)})<=S_ext`.

The reverse inequality is immediate because the extreme laws are admissible. QED.

## Corollary G.2 — exact full-QFORM law localization

For a finite positive measure `mu` on `R`, define

`D(mu)=sup_{a<b} mu((a,b))/(b-a)`.

For each fixed interval, `mu -> mu((a,b))/(b-a)` is linear and continuous for total variation, hence `D` is convex and total-variation lower semicontinuous. Moreover `D(mu)<infinity` if and only if `mu` is absolutely continuous with essentially bounded density, and in that case

`D(mu)=||dmu/dx||_infinity`.

Indeed, one direction is immediate. Conversely, `mu(I)<=C|I|` for every open interval implies the same inequality for every open set by decomposing it into countably many disjoint intervals; outer regularity then yields `mu(E)<=C|E|` for every Borel set, so Radon--Nikodym gives a density bounded by `C`.

Take `T_A(x)=x^T A x`. Theorem G.1 therefore gives, for every fixed symmetric `A`,

`sup_{independent X_i, density<=1} D(Law(X^T A X))`

` = sup_{|E_i|=1, E_i bounded finite-union} D(Law(X_E^T A X_E))`,

where `X_E` has independent densities `1_{E_i}`.

Taking the supremum also over every symmetric `A` having at least three eigenvalues of modulus at least one yields the exact identity

`C_QFORM(all cap-one laws) = C_QFORM(bounded finite-union extreme laws)`

in `[0,+infinity]`.

Thus the unrestricted rough-law QFORM theorem has exactly the same optimal universal constant as the theorem restricted to bounded finite-union indicator marginals. This removes translations, tails, unbounded supports, and missing moments as separate law-class issues. It does **not** give any common bound on the number of intervals or on the support diameter; an extremizing sequence may have fragment count and separation tending to infinity.

The same conclusion holds for affine quadratic maps

`x^T A x + ell^T x + c`

uniformly over arbitrary `ell,c`, because `T` in Theorem G.1 is arbitrary.

## Corollary G.3 — conditional L^p budget

Take `S=Omega x R`, `T(omega,x)=(omega,F(omega,x))`, reference measure `rho=nu tensor Lebesgue`, and

`Phi_p(mu)=||dmu/d rho||_p^p`

with value `+infinity` if no `L^p` density exists. For every `p>1`, `Phi_p` is convex and total-variation lower semicontinuous. Theorem G.1 therefore recovers `QFORM-CONDITIONAL-LP-BUDGET-EXTREME-LOCALIZATION-v1` from `REPORT.md`: the integrated conditional `L^p` density budget has exactly the same supremum over arbitrary cap-one product laws as over bounded finite-union extreme product laws.

This is the form that composes without constant loss with completed `account02/B14` r41.

## Proof-order warning

The theorem localizes to **whole finite-union extreme sets**. It does not license splitting such a set into its connected interval components, normalizing each component, taking absolute-value/Fourier/reciprocal certificates separately, and summing. Partner `account02/B14` r41 gives an exact-target example where that latter proof order creates an `N^(5/12)` artificial loss. The meta-lemma and that obstruction are consistent: the correct extreme object is the whole set of prescribed mass, however disconnected it is.

Full unrestricted QFORM remains **OPEN** because the remaining task is a matrix/analytic estimate uniform over those extreme product laws, not because of tails or support localization.
