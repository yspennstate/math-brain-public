# fleet03/B05 — mixed-pair sectional coarea and the pair-Pluecker aggregation tax

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `20260922T144946Z-qform-B05-a03-r12`  
**Assignment:** Quadratic coarea bound  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING THEOREM PROVED / PRECISE MISSING FACTOR IDENTIFIED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval/write is not native learned-memory receiver use.

## 1. Scope and corrections

The owner target remains the full statement for every dimension, every independent real coordinate family with densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one. This report proves supporting coarea mathematics for the exact-rank-three heavy-isotropic branch and does **not** claim the full theorem or continuity.

The proof stays in original independent coordinates. It does not use law-uniform pointwise Fresnel decay, post-rotation independence, a spectral-fiber supremum, a single cross minor as a full certificate, or a conditional density cap as a substitute for genuine independence. In particular it respects the live `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` falsifier.

The preceding B05 run proved `QFORM-HIDDEN-BANK-HYPERBOLIC-SQUARE-v1` when a genuinely independent transverse square bank survives. Its first unpaid branch was the mixed case in which essentially every transverse coordinate also carries leakage or hyperbolic mass. The present run changes mechanism from a pure-subbank split to a **two-coordinate sectionalization**: on any two residual coordinates with nonzero `y-z` determinant, all leakage on those two coordinates is an exact linear combination of the two projected coordinates and can therefore be absorbed algebraically before coarea.

The assigned partner is `fleet04/B05`. Fresh searches of its current-QFORM proof and shared-handoff roots found no completed current-programme artifact, so no theorem is attributed to that slot. A completed compatible fleet04 theorem that is actually applied below is `fleet04/B18`, `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, source `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`. The aggregate/localization interface used for comparison is fleet03/B07, `QFORM-PLUCKER-COLLAR-TRICHOTOMY-v1`, source `yspennstate/math-open-problems@c3b0a3023962496543da62be43f07bff5ca0865b`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/fleet03-B07-20260922T124045Z-qform-minors-v11/REPORT.md`.

## 2. A pair-sectional coarea theorem

### Theorem 2.1 — `QFORM-PAIR-SECTIONAL-COAREA-v1`

Let `U` be independent of the pair `(V,Z)`. Assume `U` has a probability density bounded by `M_U`, while `(V,Z)` has a joint probability density `g` bounded by `M_2`. No independence between `V` and `Z` is assumed. Let `a,b != 0`, and let `H, theta` be arbitrary measurable real functions. Define

`W = 2 a U V + H(V) + b ( Z + theta(V) )^2`.                            (2.1)

Then `W` is absolutely continuous and

`boxed{ ||p_W||_infinity
 <= 3*2^(2/3) M_U^(2/3) M_2^(2/3)
      |a|^(-2/3)|b|^(-1/3). }`                                        (2.2)

Equivalently every interval `I` satisfies the linear small-ball estimate

`P(W in I) <= 3*2^(2/3) M_U^(2/3) M_2^(2/3)
              |a|^(-2/3)|b|^(-1/3) |I|`.                              (2.3)

#### Proof

Fix `v`. Push the `z`-subdensity `g(v,z) dz` through

`z -> b(z+theta(v))^2`.

By the one-dimensional change-of-variables formula, its pushforward has an a.e. density bounded by

`M_2 |b|^(-1/2) [sigma w]_+^(-1/2)`, `sigma=sign(b)`.                   (2.4)

For a probability density `f<=M_U`, a real `q`, and `d!=0`, the exact one-sided bathtub estimate is

`int f(u) [q-du]_+^(-1/2) du <= 2 sqrt(M_U/|d|)`.                       (2.5)

Indeed, after the affine change `x=q-du`, the maximizing cap-`M_U` density places its unit mass on the interval adjacent to `x=0`, of length `|d|/M_U`; integrating `x^(-1/2)` gives (2.5).

Apply (2.5) with `d=2av`. For `v!=0`, the contribution at fixed `v` to the density of `W` is therefore bounded by

`M_2 sqrt(2M_U) |ab|^(-1/2) |v|^(-1/2)`.                              (2.6)

Split at `R>0`. On `|v|<=R`, integration of (2.6) in Lebesgue `v` gives

`p_near(t) <= 4 sqrt(2) M_2 sqrt(M_U) |ab|^(-1/2) sqrt(R)`.             (2.7)

On `|v|>R`, instead condition on `(V,Z)`. For fixed `v,z`, (2.1) is affine in `U` with slope `2av`, so its conditional density is at most

`M_U/(2|av|) <= M_U/(2|a|R)`.

Since `(V,Z)` has total mass one,

`p_far(t) <= M_U/(2|a|R)`.                                              (2.8)

Thus

`p_W(t) <= A R^(1/2) + D R^(-1)`,                                      (2.9)

with

`A=4 sqrt(2) M_2 sqrt(M_U)/sqrt(|ab|)`,
`D=M_U/(2|a|)`.

The minimum occurs at `R=(2D/A)^(2/3)` and equals

`3*2^(-2/3) A^(2/3)D^(1/3)
 =3*2^(2/3) M_U^(2/3)M_2^(2/3)|a|^(-2/3)|b|^(-1/3)`.                  (2.10)

The near and far pieces are mixtures of absolutely continuous conditional laws with the displayed integrable majorants, so this also supplies an unconditional density. This proves (2.2); integrating over an interval proves (2.3). QED.

### What is new relative to the preceding B05 theorem

The previous hidden-bank theorem required the square supplier `Z` itself to be independent of the hyperbolic variable `V`. Theorem 2.1 allows arbitrary dependence between `V` and `Z`. The price is the joint-density cap `M_2`. This is exactly the interface available from any invertible two-coordinate section of an original product law.

## 3. Apply the theorem to a genuinely mixed heavy-isotropic pair

Use the exact-rank-three heavy-isotropic normal form from the preceding B05/B10 work. Let

`A=U Lambda U^T`, `U^T U=I_3`, `|det Lambda|>=1`,

and suppose a physical row is

`u_i=sqrt(c)e`, `c>1/2`, `e^T Lambda e=0`.

In an orthonormal spectral basis `(e,f,g)`, write

`Lambda=[[0,B,0],[B,r,s],[0,s,tau]]`,                                  (3.1)

so

`B^2 |tau|=|det Lambda|>=1`.                                            (3.2)

For residual rows write

`u_j=s_j e+y_j f+z_j g`,

and define

`T=sum s_j X_j`, `Y=sum y_j X_j`, `Z=sum z_j X_j`.

Parseval gives

`sum s_j^2=1-c`, `sum y_j^2=sum z_j^2=1`,
`sum s_j y_j=sum s_j z_j=sum y_j z_j=0`.                               (3.3)

After completing the spectral `Z` square,

`Q=2B(sqrt(c)X_i+T)Y + A_0 Y^2 + tau(Z+kappa Y)^2`                      (3.4)

for fixed real `A_0,kappa`.

Choose any two residual original coordinates `j,k` such that

`Delta_jk = y_j z_k - y_k z_j !=0`.                                    (3.5)

Condition on every residual coordinate except `X_j,X_k`, but do **not** condition on `X_i`. Write the conditioned contributions of all other residual coordinates as constants `t_0,y_0,z_0`, and put

`Y_K=y_jX_j+y_kX_k`, `Z_K=z_jX_j+z_kX_k`.

Since the two coefficient vectors `(y_j,y_k)` and `(z_j,z_k)` form a basis of `R^2`, there exist exact scalars `alpha,beta` with

`s_jX_j+s_kX_k = alpha Y_K + beta Z_K`.                                (3.6)

Set

`V=Y_K+y_0`, `U_0=sqrt(c)X_i`.

The map `(X_j,X_k)->(Y_K,Z_K)` has Jacobian determinant `Delta_jk`; because the original pair density is at most one,

`||p_(Y_K,Z_K)||_infinity <= |Delta_jk|^(-1)`.                         (3.7)

Translation in `Y_K` preserves that cap. Also `U_0` is genuinely independent of this pair and

`||p_(U_0)||_infinity <= c^(-1/2)`.                                    (3.8)

Substitute (3.6) into (3.4). The only extra term coupling `Z_K` to `V` is `2B beta V Z_K`; it can be absorbed into the existing `tau` square:

`tau(Z_K+z_0+kappa V)^2 +2B beta V Z_K`

`=tau(Z_K+theta(V))^2 + H_1(V)`                                       (3.9)

with

`theta(V)=z_0+kappa V+(B beta/tau)V`

and an explicit scalar function `H_1`. Every remaining conditioned term, including the `alpha` leakage contribution, depends only on `V`. Hence the conditional form is exactly

`Q=2B U_0 V + H(V) + tau(Z_K+theta(V))^2`.                             (3.10)

Theorem 2.1 applies with

`M_U=c^(-1/2)`, `M_2=|Delta_jk|^(-1)`, `a=B`, `b=tau`.

Using (3.2), uniformly in all conditioned outside values,

`boxed{ ||p_Q||_infinity
 <=3*2^(2/3)c^(-1/3)|Delta_jk|^(-2/3)|det Lambda|^(-1/3). }`           (3.11)

Since `c>1/2` and `|det Lambda|>=1`,

`boxed{ ||p_Q||_infinity < 6 |Delta_jk|^(-2/3). }`                     (3.12)

Mixing over the conditioned coordinates preserves the same bound.

This is `QFORM-MIXED-PAIR-COAREA-v1`. It closes every mixed-transverse exact-rank-three heavy-isotropic instance for which one physical residual pair has a quantitatively nontrivial `y-z` determinant. No pure transverse coordinate is required; both selected coordinates may simultaneously carry `s`, `y`, and `z` mass.

## 4. Exact pair-Pluecker mass and the remaining dimension tax

The two residual coefficient rows `y=(y_j)` and `z=(z_j)` are orthonormal by (3.3). Cauchy-Binet therefore gives the exact identity

`sum_{j<k} Delta_jk^2 = det([[<y,y>,<y,z>],[<z,y>,<z,z>]]) =1`.         (4.1)

Thus at least one pair has

`|Delta_jk| >= binom(m,2)^(-1/2)`                                     (4.2)

when `m` residual coordinates are present. Feeding only this pigeonhole estimate into (3.12) yields

`||p_Q||_infinity < 6 binom(m,2)^(1/3)`.                              (4.3)

This is better than a linear fiber-sup loss, but it is still dimension-dependent. Equation (4.1) identifies the exact missing factor: **the coarea argument must aggregate the full pair-Pluecker mass before paying the reciprocal determinant.** Selecting one pair first is intrinsically too expensive.

### Source-valid stress frame showing this local tax is real

For `m>=3`, let

`theta_j=2 pi j/m`,
`y_j=sqrt(2/m) cos(theta_j)`,
`z_j=sqrt(2/m) sin(theta_j)`.

Then `y,z` are exactly orthonormal and

`Delta_jk=(2/m) sin(theta_k-theta_j)`,                                 (4.4)

so

`max_{j<k}|Delta_jk| <=2/m`,                                           (4.5)

while (4.1) still equals one. Choose any unit vector `w` perpendicular to both `y,z`, set `s=sqrt(1-c) w`, and add the heavy row `sqrt(c)e`. This gives a valid rank-three Parseval physical frame satisfying all identities (3.3). Therefore a proof that first chooses a single pair and then invokes (3.11) can genuinely pay order `m^(2/3)` on a perfectly valid target frame. This is a counterexample to that **mechanism**, not to QFORM.

The aggregate fleet03/B07 collar theorem explains why this stress frame does not threaten the target: aggregate determinant mass, rather than the largest one pair minor, can remain dimension-free and close diffuse states.

## 5. Actual application of completed fleet04 mathematics

For comparison, suppose a selected physical triple `{i,j,k}` in the same heavy-isotropic frame has a residual scalar pivot of the minority inertia sign with magnitude at least `1/2`. The principal triple determinant is

`|det A_{i,j,k}| = c |det Lambda| Delta_jk^2`.                          (5.1)

This follows from `A_I=U_I Lambda U_I^T` and

`det(U_I)^2 = c Delta_jk^2`.

Applying the completed fleet04/B18 theorem `QFORM-SCHUR-PIVOT-SMOOTHING-v1` to that actual triple gives

`||p_Q||_infinity
 <=2 sqrt(pi) ( |A_jj| c |det Lambda| Delta_jk^2 )^(-1/4)`.            (5.2)

Under `|A_jj|>=1/2`, `c>1/2`, `|det Lambda|>=1`, this becomes

`||p_Q||_infinity <=2 sqrt(2 pi) |Delta_jk|^(-1/2).`                   (5.3)

This is a genuine application of a completed fleet04 result to the current inequality. It pays the minority-sign branch more efficiently in `Delta`. The new pair-sectional theorem (3.11) is useful precisely on the complementary majority/near-light-cone pair where that signed-pivot gate is unavailable.

The assigned `fleet04/B05` slot still had no completed current-QFORM artifact at the source refresh used for this report; that absence is reported rather than replaced by a false attribution.

## 6. First unpaid implication after this run

The previous `rho_pure ->0` obstruction has been narrowed. Pure transverse mass is no longer necessary: every nondegenerate physical pair gives a rigorous mixed-bank coarea estimate. The remaining first coarea implication is now

**`QFORM-PAIR-PLUCKER-AGGREGATION-v1` — OPEN.** Starting from the exact identity

`sum_{j<k} Delta_jk^2=1`,

aggregate the pair-section bounds before inversion/conditioning so that the final estimate pays the total pair-Pluecker mass rather than `max |Delta_jk|^(-2/3)`. Equivalently, prove a multi-pair coarea inequality which preserves shared-coordinate dependence and gains from the whole Parseval frame, or produce a source-valid counterexample to such an aggregation inequality.

For the complete owner target there remains a separate additional-spectrum interaction debt: arbitrary small/nonselected eigen-directions create nonseparable quadratic terms and cannot simply be conditioned or convolved away.

## 7. Status

**Proved in this report:**

1. `QFORM-PAIR-SECTIONAL-COAREA-v1`, equation (2.2), allowing arbitrary dependence in the quadratic pair `(V,Z)`.
2. `QFORM-MIXED-PAIR-COAREA-v1`, equation (3.11), for every nonzero physical residual `y-z` pair minor in the exact-rank-three heavy-isotropic state.
3. the exact aggregate identity (4.1) and a valid Parseval stress frame showing why single-pair selection alone loses up to order `m^(2/3)`.
4. the fleet04/B18 minority-pivot inequality (5.2)-(5.3) applied to the same physical triple geometry.

**Not proved:**

- pair-Pluecker aggregation with a dimension-free constant;
- arbitrary localized majority/near-light-cone rank-three closure;
- arbitrary additional nonseparable spectral directions;
- the full QFORM conjecture;
- continuity of the density. The new theorem establishes absolute continuity and an essential `L^infinity` bound only.

No numerical histogram, moment assumption, support regularity, diagonalization-independence assumption, or refuted pointwise oscillatory claim is used.