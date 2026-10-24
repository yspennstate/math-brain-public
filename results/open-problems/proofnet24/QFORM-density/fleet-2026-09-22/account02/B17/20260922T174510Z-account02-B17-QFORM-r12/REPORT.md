# account02/B17 — vector infinitesimal shared-frame no-escape theorem

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T174510Z-account02-B17-QFORM-r12`  
**Assignment:** Sharp constant and witnesses  
**Classification:** `AUXILIARY_ONLY / GROWING_SHARED_FRAME_LIMIT_NO_ESCAPE`  
**Full quadratic-form conjecture:** **OPEN / NOT PROVED**  
**Execution memory:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target, first unpaid implication, and source pins

The full target remains: for every dimension, every independent real input family with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove one universal dimension-free essential-density bound for `X^T A X`, or give a valid target-level counterexample. No moments, support, centering, log-concavity, post-rotation independence, or finite-fragment hypothesis is assumed in the target.

This B17 run attacks the first sharp-witness mechanism left open by the preceding B17 work: **growing shared-coordinate frames with arbitrarily fragmented cap-one laws**. The earlier scalar theorem `QFORM-INFINITESIMAL-BANK-NOESCAPE-v1` covered only three disjoint scalar banks. The new issue is that one physical coordinate may load all three active spectral directions, with the row pattern changing with dimension.

Completed designated-partner result actually applied:

- account03/B17, `20260922T170559Z-account03-B17-QFORM-r13`, canonical report `yspennstate/math-open-problems@3bb57a5517de87855824e393ec1601b8921abc13`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B17/20260922T170559Z-account03-B17-QFORM-r13/REPORT.md`. It proves that every **fixed** finite tight-frame pattern, repeated with centered interval inputs, approaches the `3 sqrt(2)` Gaussian witness from below with an explicit negative Edgeworth correction. Its stated next nonredundant target is a growing-pattern shared frame with fragmented laws.

Two prior completed inputs are also used with their exact scopes:

- account02/B17, `QFORM-INFINITESIMAL-BANK-NOESCAPE-v1`, canonical report `yspennstate/math-open-problems@9ef2d4cbf56e1aa3368eeaa322d09ba4d91f31cf`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/20260922T154450Z-account02-B17-QFORM-r11b/REPORT.md`. Its scalar cap-one subprobability variance lemma and Levy triangular-array passage are generalized here from one dimension to a shared vector frame.
- account01/B17, `QFORM-GAUSSIAN-FULL-NONCENTRAL-C3SQRT2-v1`, available at `yspennstate/math-open-problems@d6150b6de22e898de442e821e42c2ddc09604a0d`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B17/20260922T120821Z-account01-B17-qform-sharp-constant-v1/ADDENDUM_NONCENTRAL_GAUSSIAN.md`. If `G~N(m,Sigma)`, `Sigma>=sigma^2 I`, and the quadratic matrix has at least three eigenvalues of modulus at least one, then `||p_{G^T A G}||_infinity <= 1/(2 sqrt(2) sigma^2)`.

The live correction set was consumed before publication. No pointwise oscillatory envelope, rotated-coordinate independence, conditional projection cap, raw fiber supremum, fixed fragment count, one-minor extraction, or cross-minor-only implication is used.

## 2. Vector cap-one covariance lemma on an affine line

The key finite-dimensional inequality is translation invariant and keeps the original product source.

Let `X` have a probability density bounded by one. Let `w in R^3`, `w != 0`, and let `c in R^3` be arbitrary. Put

`Xi = w X - c`.

For `eps>0`, let `nu` be the restriction of the law of `Xi` to the Euclidean ball `{|z|<=eps}`, and let

`p = nu(R^3)`,  `m_nu = int z dnu(z)`,

`C(nu) = int z z^T dnu(z) - m_nu m_nu^T`.

Then

`C(nu) >= (p^3/12) w w^T`                                      (2.1)

in Loewner order.

### Proof

Write `u=w/|w|`. The affine line supporting `Xi` can be parametrized as `z=z_perp+u T`, where `T` is an affine transform of `X` with one-dimensional density bounded by `1/|w|`. Normalize the restricted measure, `mu=nu/p` when `p>0`. Along the line, the scalar coordinate of `mu` has density bounded by `1/(p|w|)`. The sharp one-dimensional variance floor for a probability density bounded by `L` is

`Var >= 1/(12 L^2)`,

so

`Cov_mu(Xi) >= (p^2 |w|^2/12) u u^T = (p^2/12) w w^T`.

For a subprobability measure,

`C(nu)=p Cov_mu(Xi)+p(1-p)(E_mu Xi)(E_mu Xi)^T >= p Cov_mu(Xi)`.

This gives (2.1). The case `p=0` is trivial. No moment of the unrestricted law of `X` is used. QED.

The same proof works in every finite ambient dimension; dimension three is all that is needed here.

## 3. New theorem: every convergent infinitesimal growing shared frame retains Gaussian covariance `I/12`

### Theorem `QFORM-VECTOR-INFINITESIMAL-SHARED-FRAME-NOESCAPE-v1`

For each row index `m`, let `w_{m,k} in R^3` be deterministic vectors satisfying the exact tight-frame identity

`sum_k w_{m,k} w_{m,k}^T = I_3`,                                  (3.1)

and the deterministic diffuse condition

`delta_m := max_k |w_{m,k}| -> 0`.                                 (3.2)

Let `X_{m,k}` be independent real random variables, each with density bounded by one. Let `c_{m,k} in R^3` be arbitrary deterministic translations and put

`Xi_{m,k}=w_{m,k} X_{m,k}-c_{m,k}`.                                (3.3)

Assume the vector triangular array is **probabilistically infinitesimal**,

`max_k P(|Xi_{m,k}|>eps) -> 0` for every `eps>0`,                   (3.4)

and the independent sums

`S_m=sum_k Xi_{m,k}`                                                (3.5)

converge in distribution to `S`.

Then `S` is infinitely divisible, and the Gaussian covariance matrix `Gamma` in its Levy-Khintchine triplet obeys the dimension-free Loewner lower bound

`boxed(Gamma >= (1/12) I_3)`.                                      (3.6)

No moments, support bound, common law, symmetry, finite fragment count, fragment scale, or fixed row-type pattern is assumed.

### Proof

Fix `eps>0` that is a continuity radius for the Levy measure of the limiting infinitely divisible law. Let `F_{m,k}` be the law of `Xi_{m,k}` and define its small-jump mass

`p_{m,k}=F_{m,k}({|z|<=eps})`,  `q_{m,k}=1-p_{m,k}`.

Define the canonical truncated covariance contribution

`C_{m,k}(eps)`
` = int_{|z|<=eps} z z^T dF_{m,k}(z)`
`   - [int_{|z|<=eps} z dF_{m,k}(z)] [int_{|z|<=eps} z dF_{m,k}(z)]^T`.

Applying (2.1) to each row gives

`C_{m,k}(eps) >= (p_{m,k}^3/12) w_{m,k}w_{m,k}^T`.                 (3.7)

Since `(1-q)^3 >= 1-3q` for `0<=q<=1`, summing (3.7) and using (3.1) gives

`sum_k C_{m,k}(eps)`
` >= (1/12) [ I_3 - 3 sum_k q_{m,k} w_{m,k}w_{m,k}^T ].            (3.8)

For a convergent infinitesimal triangular array, the Levy triangular-array theorem gives vague convergence of the row Levy measures away from zero. In particular, at every continuity radius `eps`,

`T_m(eps):=sum_k P(|Xi_{m,k}|>eps)=sum_k q_{m,k}=O_eps(1)`.         (3.9)

The error matrix in (3.8) therefore vanishes in operator norm:

`||sum_k q_{m,k} w_{m,k}w_{m,k}^T||_op`
` <= delta_m^2 T_m(eps) -> 0`.                                     (3.10)

Consequently

`liminf_m sum_k C_{m,k}(eps) >= (1/12) I_3`                        (3.11)

in Loewner order.

The same standard Levy triangular-array theorem identifies the Gaussian covariance by the canonical small-jump covariance limit:

`Gamma = lim_{eps downarrow 0} lim_m sum_k C_{m,k}(eps)`            (3.12)

along continuity radii (equivalently, for fixed `eps` the limit is `Gamma` plus the covariance contributed by Levy jumps of norm at most `eps`, and that jump contribution vanishes as `eps downarrow0`). Combining (3.11) and (3.12) yields (3.6). QED.

### Important scope point

Condition (3.4) is a real probabilistic hypothesis; it is **not** inferred from the deterministic row diffuseness (3.2). Under arbitrary cap-one laws, tiny coefficients can still carry non-infinitesimal probability through far-separated fragments. Such arrays remain a distinct witness mechanism rather than being silently folded into this theorem.

## 4. Quadratic-form corollary: no growing infinitesimal shared-frame limit can beat `3 sqrt(2)`

Let `J=diag(1,1,-1)`. Suppose the hypotheses of Section 3 hold. By (3.6), the limiting infinitely divisible vector can be realized as

`S = G_0 + R`,                                                       (4.1)

where

`G_0 ~ N(0,(1/12)I_3)`

is independent of `R`. Indeed, split the Gaussian component covariance as

`Gamma=(1/12)I_3 + [Gamma-(1/12)I_3]`

and absorb the second Gaussian, the drift, and the Levy jump component into `R`.

Condition on `R=r`. Then `G_0+r ~ N(r,(1/12)I_3)`. Applying `QFORM-GAUSSIAN-FULL-NONCENTRAL-C3SQRT2-v1` to `J` gives a bounded continuous conditional density satisfying

`||p_{(G_0+r)^T J (G_0+r)}||_infinity <= 3 sqrt(2)`.                (4.2)

Averaging over `R` yields

`boxed(||p_{S^T J S}||_infinity <= 3 sqrt(2))`.                     (4.3)

The same argument applies to every real symmetric `3 x 3` matrix whose three eigenvalues all have modulus at least one.

Continuity follows from the same dominated-mixture argument used in the noncentral Gaussian theorem.

## 5. Exact target-source interpretation

Let `R_m` be the physical `n_m x 3` matrix whose rows are `w_{m,k}^T`, so (3.1) is exactly

`R_m^T R_m=I_3`.

Set

`A_m=R_m J R_m^T`.                                                  (5.1)

Then for every `m`, the nonzero spectrum of `A_m` is **exactly**

`{1,1,-1}`.                                                         (5.2)

Thus every member is a valid target matrix, with no approximate spectral claim. For a product input vector `X_m`,

`X_m^T A_m X_m = (R_m^T X_m)^T J (R_m^T X_m)`.                     (5.3)

Therefore Sections 3--4 close the following sharp-witness branch:

> Any source-valid sequence of exact rank-three target matrices whose active physical rows form a growing diffuse tight frame, and whose translated row contributions form a convergent probabilistically infinitesimal triangular array, has every macroscopic quadratic limit bounded by `3 sqrt(2)`.

This permits:

- frame complexity growing arbitrarily with `m`;
- every physical coordinate loading several or all active spectral directions;
- non-identical cap-one input laws;
- arbitrarily many fragments and fragment scales;
- infinite-activity Levy jump limits;
- arbitrary deterministic translations/noncentrality;
- and dependence among the three active spectral coordinates generated by shared physical rows.

It strictly extends the earlier disjoint-bank infinitesimal theorem in the shared-coordinate direction. It also answers the partner r13 suggested next mechanism at the **weak-limit level**: changing the tight-frame pattern with dimension cannot by itself raise a convergent infinitesimal limit above the `3 sqrt(2)` ceiling.

## 6. Sharpness and relation to the completed partner theorem

The ceiling is sharp as a limiting statement. The usual three disjoint uniform banks have `max|w|=m^{-1/2}`, satisfy (3.1)--(3.4), and converge to `N(0,I_3/12)`, for which the mixed-sign quadratic density attains

`p(0)=3 sqrt(2)=4.242640687119285...`.

The completed account03/B17 r13 theorem is stronger on its fixed-pattern centered-uniform subclass: it gives the explicit finite-order expansion

`p_{Q_m}(0)=3sqrt(2)[1-(3/(640m)) sum_k(19x_k^2+40x_ky_k+8y_k^2)+O_W(m^-2)]`,

with a strictly negative first correction and optimal total-dimension coefficient `(63+6sqrt(38))/160`. The present theorem does not reproduce that finite-order information. Instead it removes the fixed-pattern and interval-law assumptions while retaining only an infinitesimal convergent-limit conclusion.

These two results are complementary, not competing claims.

## 7. What remains unpaid

The unrestricted quadratic-form conjecture remains **OPEN**. This theorem is a witness exclusion, not a uniform finite-row density theorem. Weak convergence does not imply

`limsup_m ||p_{X_m^T A_m X_m}||_infinity <= 3sqrt(2)`;

narrow finite-row spikes can disappear in the weak limit.

A witness above `3sqrt(2)`, if one exists, must now leave at least one ingredient of this branch. The remaining sharp-witness mechanisms are substantially narrower:

1. **non-infinitesimal probability at diffuse deterministic leverage:** tiny rows coupled to far fragmented laws so that some row contributions remain macroscopic in probability;
2. **mixed leverage:** finitely many genuinely macroscopic physical rows interacting with a diffuse shared residual;
3. **finite-row/local-limit spikes:** a sequence with benign macroscopic limit but increasingly narrow density peaks;
4. **additional spectral directions/full matrices:** behavior not reducible to an exact rank-three tight-frame source.

The next B17 attack should therefore stress a finite macroscopic core plus an infinitesimal shared residual, especially at off-center levels, or prove a uniform local-limit upgrade. Repeating fixed-frame Edgeworth or finite-intensity compound-Poisson constructions would be redundant.

## 8. Verification status

A deterministic checker accompanies this report. It verifies the tight-frame/eigenvalue algebra on a shared four-row frame and its repeated versions, the matrix form of `(1-q)^3>=1-3q`, the operator-norm error estimate, and the constants `3sqrt(2)` and `(63+6sqrt(38))/160`. These are algebraic sanity checks only. The analytic input is the standard Levy triangular-array convergence theorem together with the completed noncentral-Gaussian theorem cited above.

No claim of publication priority or full-QFORM closure is made.
