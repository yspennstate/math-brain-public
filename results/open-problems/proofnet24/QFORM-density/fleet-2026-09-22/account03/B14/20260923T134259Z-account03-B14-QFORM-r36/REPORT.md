SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B14, 2026-09-23T13:42:59Z.
attacking: collective codimension-one Riesz localization — pay an entire diffuse outside product bank before the square-root critical-budget physical-pair compiler.

# account03/B14 r36 — collective codimension-one Riesz localization

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T134259Z-account03-B14-QFORM-r36`  
Status: `NEW SUPPORTING LOCALIZATION THEOREM PROVED / FULL QFORM OPEN / CONTINUITY OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and source boundary

The exact owner target is unchanged. For every finite `n`, every family of independent real coordinates whose one-dimensional probability densities satisfy `0<=f_i<=1`, and every real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove a universal essential bound for the density of `X^T A X`, or give a valid target-level counterexample. No Gaussian, log-concave, moment, compact-support, connected-support, centering, or post-rotation independence assumption is introduced.

Fresh control used for this run is `yspennstate/math-research-brain@eeeaa6e7db4d386ef0a7ec1474dc1570db15fafd`; OWNER CONTROL revision is `2026-09-22.15`, QFORM-only, with no pause on account03/B14. I consumed the current `CURRENT_RESEARCH.md`, `CLAIMS.json`, live `CORRECTION_INBOX.json`, `MEMORY_PROTOCOL.md`, and the account03/B14 assignment before the derivation. In particular I do not use law-uniform pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint rank-three coarea, positive conditional-projection moments, bounded-diameter localization, fixed fragment-count localization, or a worst normalized fiber bound.

The designated partner actually applied is account04/B14 r9:

`yspennstate/math-open-problems@63ba8e0f106c3bb405f05eb99778039ff47ed47b:proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260923T101157Z-account04-B14-continuum-perspective-rough-transfer-r9/REPORT.md`.

Its completed physical-pair envelope is used below at an actual inequality. A second standard source input is the one-dimensional product-projection bound used throughout the fleet: if `Z_j` are independent with density caps one, then for every nonzero coefficient vector `b`, the projection `b^T Z` has density cap at most `sqrt(2)/||b||_2`. One explicit fleet source is account02/B04, `yspennstate/math-open-problems@07305f53ba9b8a1d3e6e79f8c851f415f007d4a7:proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/B04-20260922T181702Z-dac07509/REPORT.md`, equation (5.1).

## 2. Partner physical-pair compiler

Let `B` be an actual invertible indefinite `2x2` block in original coordinates, with

`D=|det B|`, `kappa=s_min(B)`.

Account04/B14 r9 proves that if the scalar Schur-remainder law `mu` satisfies

`|hat mu(t)| <= min(1,K/|t|)` for `t!=0`,                         (2.1)

then the corresponding quadratic output has density cap

`||p_Q||_infinity <= F_(D,kappa)(K)`,                            (2.2)

where

`F_(D,kappa)(K)
 := inf_(y>0) [4 sqrt(K/(kappa y)) + D^(-1/2) Omega(y)]`,         (2.3)

`c_E=1/(2 sin^2(1/2))`, and

`Omega(y)=c_E y(2+log(1/y))` for `0<y<=1`,

`Omega(y)=log y+2c_E` for `y>=1`.                                (2.4)

The same report proves translation invariance of this Fourier-tail interface and a cap-preserving rough-law transfer.

The preceding account03/B14 r35 observed that

`H_(D,kappa)(z):=F_(D,kappa)(z^2)`                              (2.5)

is increasing and concave, because it is the pointwise infimum over `y>0` of affine increasing functions

`4z/sqrt(kappa y)+D^(-1/2)Omega(y)`.                             (2.6)

Hence a measurable conditional family with critical constants `K(theta)` only needs `E sqrt(K)<infinity`, and then

`||p_Q||_infinity <= F_(D,kappa)((E sqrt(K))^2)`.                (2.7)

The proof of (2.7) uses conditional interval inequalities, Tonelli, Jensen for `H`, and Lebesgue differentiation; it does not select versions of conditional densities.

## 3. New elementary lemma: translation-uniform Riesz budget from a density cap

### Lemma 3.1 — `QFORM-DENSITY-CAP-RIESZ-v1`

Let `W` be a real probability variable with density bounded by `M<infinity`. For every `0<q<1` and every `a in R`,

`boxed:
 E |W-a|^(-q) <= (2M)^q/(1-q).
`                                                                  (3.1)

The constant is sharp among all probability densities with cap `M`.

#### Proof

For `s>0`,

`P(|W-a|^(-q)>s)=P(|W-a|<s^(-1/q)) <= min(1,2M s^(-1/q)).`       (3.2)

By layer cake,

`E|W-a|^(-q)
 = int_0^infinity P(|W-a|^(-q)>s) ds.`                            (3.3)

Split at `s_0=(2M)^q`. The first part is `s_0`. The second is

`2M int_(s_0)^infinity s^(-1/q) ds
 = [q/(1-q)](2M)^q.`                                              (3.4)

Adding gives (3.1). Equality is attained by density `M 1_[a-1/(2M),a+1/(2M)]`. QED.

This proof has no support, connectedness, fragment-count, translation, or moment input.

## 4. Whole-bank version: diffuse product projections cost only their l2 scale

Let `Z=(Z_1,...,Z_m)` have independent probability densities bounded by one, let `b in R^m\{0}`, and put `L=||b||_2`. The product-projection theorem gives

`||p_(b^T Z)||_infinity <= sqrt(2)/L.`                            (4.1)

Applying Lemma 3.1 with `M=sqrt(2)/L` yields, uniformly in every shift `beta`,

`boxed:
 sup_beta E |b^T Z+beta|^(-q)
 <= 2^(3q/2)/[(1-q)L^q],   0<q<1.
`                                                                  (4.2)

The entire bank is aggregated before any reciprocal coefficient is paid. If `b_j=L/sqrt(m)` on `m` coordinates, every individual coefficient tends to zero but (4.2) is unchanged.

Physical translations `Z_j -> Z_j+h_j` only replace `beta` by `beta+b^T h`, so the bound is exactly translation invariant. Arbitrarily remote fragments and unbounded supports are already allowed because (4.1) uses only independence and density caps.

## 5. Main new compiler: collective codimension-one critical budget

### Theorem 5.1 — `QFORM-COLLECTIVE-CODIM1-RIESZ-BUDGET-v1`

Keep the fixed physical pair `B` from Section 2. Let the outside original-coordinate bank `Z=(Z_1,...,Z_m)` consist of independent cap-one variables and let `b!=0`, `L=||b||_2`. Suppose that, after conditioning on `Z=z`, the scalar remainder law satisfies for almost every `z`

`|hat mu_z(t)|
 <= min(1, K_0 |b^Tz+beta|^(-alpha) / |t|),`                    (5.1)

for all `t!=0`, where `K_0>0`, `beta in R`, and

`0<alpha<2`.                                                     (5.2)

Then the unconditional quadratic output has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <= F_(D,kappa)(K_eff),
`                                                                  (5.3)

where

`boxed:
 K_eff
 = K_0 * 2^(3alpha/2) / (1-alpha/2)^2 * L^(-alpha).
`                                                                  (5.4)

The bound is uniform in `m`, all translations, support radius, fragment count and separation, and all moments.

#### Proof

The conditional critical constant is

`K(z)=K_0 |b^Tz+beta|^(-alpha).`                                 (5.5)

The hyperplane `{b^Tz+beta=0}` has probability zero because `b^T Z` has a density, so the exceptional infinite value can be ignored. Put `q=alpha/2 in (0,1)`. By (4.2),

`E sqrt(K(Z))
 = sqrt(K_0) E |b^T Z+beta|^(-alpha/2)
 <= sqrt(K_0)
    * 2^(3alpha/4)/(1-alpha/2)
    * L^(-alpha/2).`                                             (5.6)

Square (5.6) and insert it into the concave square-root mixture inequality (2.7). This gives exactly (5.3)-(5.4). QED.

### Why this is a localization theorem rather than a pointwise Fourier shortcut

Equation (5.1) is an explicit hypothesis on a conditional remainder family; it is **not** inferred from the mere boundedness of an arbitrary input density. The live correction forbids that inference. The new content is instead that a reciprocal critical singularity along an arbitrary affine hyperplane of an entire independent product bank is integrable at the square-root level with a dimension-free, translation-uniform constant.

Thus the proof can keep a diffuse outside bank whole. It never decomposes it into thin normalized coordinate fragments and never pays `1/|b_j|` for a selected coordinate.

## 6. Actual designated-partner application: diffuse target-valid slope bank

Let `X_1,X_2,V,Z_1,...,Z_m` be independent. Let `X_1,X_2,Z_j` have arbitrary probability densities bounded by one. Let `V` be uniform on an arbitrary interval of length one. Let `b in R^m` satisfy

`L=||b||_2>=1`,                                                  (6.1)

and consider the homogeneous quadratic form

`Q=2X_1X_2 + 2(b^T Z)V.`                                        (6.2)

Its symmetric matrix is the orthogonal direct sum of the physical pair

`[[0,1],[1,0]]`

and the `(m+1)`-dimensional star block

`[[0,b],[b^T,0]]`                                                (6.3)

(up to coordinate ordering). Its nonzero eigenvalues are

`1,-1,L,-L`.                                                      (6.4)

Therefore (6.2) is an exact instance of the owner's target whenever `L>=1`.

Condition on the outside original coordinates `Z=z`. The remainder is

`R_z=2(b^T z)V`.                                                  (6.5)

If the unit interval supporting `V` is translated, only a Fourier phase changes. Direct integration gives, away from the null hyperplane `b^Tz=0`,

`|hat mu_z(t)|
 = |sin((b^Tz)t)/((b^Tz)t)|
 <= min(1,1/(|b^Tz||t|)).`                                      (6.6)

Thus Theorem 5.1 applies with

`D=kappa=K_0=1`, `alpha=1`.                                      (6.7)

It gives

`K_eff <= 2^(7/2)/L <= 2^(7/2).`                                (6.8)

Since `F_(1,1)` is increasing, it suffices to evaluate the partner envelope at `K=2^(7/2)`. Choose

`y=4K=2^(11/2)>1`.                                               (6.9)

Using the `y>=1` branch of (2.4),

`4 sqrt(K/y)=2`,

`Omega(y)=log(2^(11/2))+csc^2(1/2)`.                             (6.10)

Hence the actual account04/B14 r9 inequality yields

`boxed:
 ||p_Q||_infinity
 <= 2 + (11/2)log 2 + csc^2(1/2)
 = 10.162994792419742... .
`                                                                  (6.11)

This is uniform in `m`, in every cap-one law of every `Z_j`, in arbitrary translations of those laws, and in every translation of the unit interval law of `V`.

### Diffuse stress family

Take

`b_m=m^(-1/2)(1,...,1)`.                                        (6.12)

Then `||b_m||_2=1`, while every individual coefficient is `m^(-1/2)`. The target spectrum remains exactly `{1,-1,1,-1,0,...,0}` for every `m`, and (6.11) stays unchanged. Any route that first selects one leaking coordinate and pays a reciprocal coefficient incurs a factor of order `sqrt(m)`; the collective Riesz localization pays the bank norm before inversion and has no such loss.

This is the requested actual use of a completed account04/B14 result: equation (6.11) is obtained by substituting the new collective critical budget (6.8) into the partner's physical-pair envelope (2.3).

## 7. Relation to arbitrary shifts, distant fragments and unbounded support

The mechanism has three zero-loss localization features.

1. **Arbitrary shifts.** Every deterministic translation of the outside product bank is absorbed into `beta`; (4.2) is uniform in `beta`.
2. **Distant or infinitely many fragments.** The product-projection bound (4.1) applies directly to the complete cap-one law. No fragment is normalized and no fragment count or separation appears.
3. **Unbounded support and no moments.** Lemma 3.1 uses only mass and a one-dimensional density cap. The tail of `b^T Z` is irrelevant.

Thus a codimension-one singular critical surface generated by a diffuse bank is not a localization obstruction. The right order is: aggregate the whole independent bank, use its projection density cap, integrate the singular critical factor, and only then apply the physical-pair smoothing compiler.

## 8. What remains for the full conjecture

This theorem is supporting mathematics, not a full solution. The bare spectral condition `s_3(A)>=1` has not been shown to force a fixed invertible indefinite physical pair whose conditional Fourier constants have the reciprocal-affine form (5.1) with universally paid `K_0`, `alpha<2`, and bank scale `L`.

The next structural implication to seek is therefore sharper: in the remaining mixed-hub/grouped-bank regime, expose a conditional critical constant whose singular set is controlled by a **whole original-coordinate projection** (or a finite collection of such projections) before any reciprocal local minor is paid. Theorem 5.1 then converts every codimension-one singularity of order `<2` into a dimension-free critical budget.

Full-target continuity is not obtained here. The interval-density argument gives essential boundedness only in the stated scope.

## 9. Integrity and quantitative checks

- Full QFORM: `OPEN / NOT PROVED / NOT DISPROVED`.
- New lemmas: `QFORM-DENSITY-CAP-RIESZ-v1`, `QFORM-COLLECTIVE-CODIM1-RIESZ-BUDGET-v1`.
- Partner actually applied: account04/B14 r9 at the conditional physical-pair inequality and explicitly in (6.11).
- Projection theorem is applied before singular integration, not after rotating the quadratic form; independence remains in original coordinates.
- No law-uniform pointwise quadratic-phase decay is asserted.
- For `alpha=1`, `(2 sqrt(2))^(1/2)/(1/2)=2^(7/4)`, whose square is `2^(7/2)`.
- At `K=2^(7/2)`, `y=4K=2^(11/2)` gives the numerical constant `10.162994792419742...`.
- Fallback privacy review of the explicit changed file found only mathematical notation, public repository pins, and nonsecret run metadata; no token, credential, signed URL, account identity, machine path, or private source excerpt is present.
- Repository transport is not native learned-memory ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.
