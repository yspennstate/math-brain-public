SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B14, 2026-09-23T12:35:14Z.
attacking: square-root critical-budget localization — average the optimized physical-pair Fourier/log cost across arbitrary outside fibers without requiring a finite mean critical constant.

# fleet03/B14 r35 — square-root critical-budget localization

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T123514Z-fleet03-B14-QFORM-r35`  
Status: `NEW SUPPORTING LOCALIZATION THEOREM PROVED / FULL QFORM OPEN / CONTINUITY OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and source boundary

The exact target remains unchanged: for every finite `n`, every family of independent real coordinates with one-dimensional probability densities bounded by one, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal essential bound on the density of `X^T A X`, or give a valid counterexample. No moment, compact-support, connected-support, centering, Gaussian, log-concave, or post-rotation independence hypothesis is added.


The designated partner actually applied is fleet04/B14 r9:

`yspennstate/math-open-problems@63ba8e0f106c3bb405f05eb99778039ff47ed47b:proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B14/20260923T101157Z-fleet04-B14-continuum-perspective-rough-transfer-r9/REPORT.md`.

Its completed physical-pair compiler is the sole external analytic premise below.

## 2. Partner physical-pair envelope

Let `B` be an actual invertible indefinite physical `2x2` block in original coordinates and write

`D=|det B|`, `kappa=s_min(B)`.

Fleet04/B14 r9 proves that when the scalar Schur remainder law `mu` satisfies

`|hat mu(t)| <= min(1,K/|t|)` for `t!=0`,

the corresponding full conditional quadratic output has density cap

`||p_Q||_infinity <= F_(D,kappa)(K)`,                            (2.1)

where

`F_(D,kappa)(K)
 := inf_(y>0) [ 4 sqrt(K/(kappa y)) + D^(-1/2) Omega(y) ]`,       (2.2)

and

`c_E=1/(2 sin^2(1/2))`,

`Omega(y)=c_E y(2+log(1/y))` for `0<y<=1`,

`Omega(y)=log y+2c_E` for `y>=1`.                                (2.3)

The partner proves `Omega` increasing and concave, and its estimate is invariant under arbitrary deterministic translations of the remainder. The parameter `K` is a critical Fourier-tail constant; bounded input density alone does **not** imply such a constant for an arbitrary quadratic phase.

## 3. New theorem: square-root critical-budget mixture

The r9 continuum theorem averages `K` first, giving a sufficient criterion involving `E K`. That can fail at a codimension-one critical fiber even though the optimized physical-pair density cost remains integrable. The correct quantity after optimization is `E sqrt(K)`.

### Theorem 3.1 — `QFORM-SQRT-CRITICAL-BUDGET-MIXTURE-v1`

Let `(Theta,pi)` be a probability space parametrizing conditioning on outside **original** coordinates. Assume the same physical pair `B` remains active on every fiber, and for almost every `theta` the conditional scalar remainder law satisfies

`|hat mu_theta(t)| <= min(1,K(theta)/|t|)`,                      (3.1)

with measurable `K:Theta->[0,infinity]`. Assume only

`b := int sqrt(K(theta)) d pi(theta) < infinity`.                (3.2)

Then the unconditional output law has an essentially bounded density and

`boxed:
 ||p_Q||_infinity <= F_(D,kappa)(b^2).
`                                                                  (3.3)

This remains true when every conditional remainder is translated by an arbitrary measurable amount. No bound on `E K` is required.

#### Proof

Define

`H_(D,kappa)(z)=F_(D,kappa)(z^2)`, `z>=0`.                       (3.4)

By (2.2),

`H_(D,kappa)(z)
 = inf_(y>0) [ 4 z/(sqrt(kappa y)) + D^(-1/2) Omega(y) ].`       (3.5)

For each fixed `y`, the expression in brackets is affine and increasing in `z`. The pointwise infimum of affine functions is concave, and the infimum of increasing functions is increasing. Hence `H_(D,kappa)` is concave and nondecreasing on `[0,infinity)`.

Apply the partner theorem (2.1) separately on almost every fiber. To avoid any measurable-density-version issue, use its equivalent interval inequality: for every bounded interval `I`,

`P{Q in I | theta} <= H_(D,kappa)(sqrt(K(theta))) |I|`.          (3.6)

Tonelli gives

`P{Q in I}
 <= |I| int H_(D,kappa)(sqrt(K(theta))) d pi(theta).`            (3.7)

Jensen for the concave function `H_(D,kappa)` yields

`int H_(D,kappa)(sqrt(K(theta))) d pi(theta)
 <= H_(D,kappa)( int sqrt(K(theta)) d pi(theta) )
 = F_(D,kappa)(b^2).`                                            (3.8)

Thus every interval has mass at most the right side of (3.3) times its length. Lebesgue differentiation gives an absolutely continuous output law with the density cap (3.3). A fiber translation multiplies `hat mu_theta` by a unimodular phase, so neither `K(theta)` nor the argument changes. QED.

### Strict gain over mean-K averaging

There are legal families with

`int K(theta) d pi(theta)=infinity`

but

`int sqrt(K(theta)) d pi(theta)<infinity`.

For those families the r9 mean-critical-budget compiler is silent while Theorem 3.1 is finite. This is not merely a reparameterization of Jensen on `Omega`; the optimization over the physical-pair scale is performed first, and the resulting envelope is concave in `sqrt K`.

## 4. Countable positive-piece / unnormalized perspective

The preceding statement has a localization form useful for remote fragments.

Suppose an outside law is decomposed into positive subprobability pieces of masses `m_j`, `sum_j m_j=1`. On the normalized `j`-th branch suppose the remainder Fourier bound has constant `K_j`. Then positivity and Theorem 3.1 applied to the discrete parameter give

`boxed:
 ||p_Q||_infinity
 <= F_(D,kappa)( [sum_j m_j sqrt(K_j)]^2 ).
`                                                                  (4.1)

Equivalently, if the **unnormalized** remainder submeasure `nu_j` obeys

`|hat nu_j(t)| <= min(m_j, k_j/|t|)`,                            (4.2)

then its normalized constant is `K_j=k_j/m_j` and the effective budget is

`boxed:
 B = sum_j sqrt(m_j k_j),
qquad ||p_Q||_infinity <= F_(D,kappa)(B^2).
`                                                                  (4.3)

If every piece satisfies the mass-homogeneous bound `k_j<=K_0 m_j`, then

`B <= sqrt(K_0) sum_j m_j = sqrt(K_0)`,                          (4.4)

so arbitrary finite or countable remote fragmentation creates **zero loss** in the final constant. No fragment location, diameter, separation, count or moment enters. The active physical pair must remain unnormalized; this theorem is an outside-fiber compiler, not permission to normalize arbitrary active-coordinate fragments.

## 5. Actual partner application: a target-valid singular-fiber family

The new square-root budget pays a genuine singular conditioning parameter that defeats mean-K averaging.

Let `X_1,X_2,Z,V` be independent. Let `X_1,X_2,Z` have completely arbitrary probability densities bounded by one, with no support or moment assumptions. Let `V` be uniform on an arbitrary interval of length one. Fix real `beta` and `gamma` with `|gamma|>=1`, and consider the affine quadratic family

`Q = 2 X_1 X_2 + 2 (gamma Z + beta) V`.                          (5.1)

The quadratic matrix on `(X_1,X_2,Z,V)` is

`A = [[0,1,0,0],
      [1,0,0,0],
      [0,0,0,gamma],
      [0,0,gamma,0]],`                                           (5.2)

whose spectrum is `{1,-1,|gamma|,-|gamma|}` up to ordering/sign convention. Hence (5.1) lies inside the owner's exact three-large-eigenvalue target whenever `|gamma|>=1`.

Use `(X_1,X_2)` as the physical pair. Then

`B=[[0,1],[1,0]]`, `D=1`, `kappa=1`.                             (5.3)

Condition on the outside original coordinate `Z=z`. The residual variable is

`R_z=2(gamma z+beta)V`.                                          (5.4)

Translation of the length-one interval supporting `V` changes only a Fourier phase. Direct integration gives

`|hat mu_z(t)|
 = | sin((gamma z+beta)t) / ((gamma z+beta)t) |
 <= min(1, 1/(|gamma z+beta| |t|))`.                             (5.5)

Thus

`K(z)=1/|gamma z+beta|`                                          (5.6)

away from the single zero of the denominator, which has probability zero because `Z` has a density.

For every cap-one probability density `f_Z`, symmetric decreasing rearrangement of `|u|^(-1/2)` gives, uniformly in `beta`,

`int |gamma z+beta|^(-1/2) f_Z(z) dz
 = |gamma|^(-1/2)
   int |z+beta/gamma|^(-1/2) f_Z(z) dz
 <= |gamma|^(-1/2)
    int_(-1/2)^(1/2) |u|^(-1/2) du
 = 2 sqrt(2)/sqrt(|gamma|).`                                     (5.7)

Therefore Theorem 3.1 gives

`||p_Q||_infinity
 <= F_(1,1)(8/|gamma|)
 <= F_(1,1)(8).`                                                  (5.8)

At `K=8`, the optimizer lies in the `y>=1` branch. There

`4 sqrt(8/y)+Omega(y)
 = 8 sqrt(2)/sqrt(y) + log y + csc^2(1/2)`,                      (5.9)

whose derivative vanishes at `y=32`. Hence

`boxed:
 ||p_Q||_infinity
 <= 2 + log 32 + csc^2(1/2)
 = 9.81642120213977... .
`                                                                  (5.10)

This bound is uniform in `beta`, in all translations of the length-one interval supporting `V`, and in the arbitrary fragmented/unbounded cap-one law of `Z`.

### Why this application is genuinely beyond the partner's mean-K criterion

If, for example, `Z` is Uniform`[-1/2,1/2]` and `beta=0`, then

`E K(Z)=|gamma|^(-1) E|Z|^(-1)=infinity`,                        (5.11)

so the direct averaged-`K` continuum theorem in partner r9 gives no finite conclusion. But

`E sqrt(K(Z))=2 sqrt(2)/sqrt(|gamma|)<infinity`,                  (5.12)

and (5.10) follows. Thus the square-root compiler closes a real codimension-one singular-fiber localization loss.

The use of a uniform `V` in this stress family is explicit. I do **not** infer (5.5) from a mere density cap; the live correction forbids exactly that kind of law-uniform pointwise Fourier claim.

## 6. Relation to arbitrary shifts, fragments and unbounded supports

The theorem is translation-safe in three independent senses:

1. arbitrary measurable scalar translations of each conditional remainder preserve `K(theta)` because they only add Fourier phase;
2. physical translations of outside variables merely move the singular point in (5.7), and the rearrangement bound is uniform in that location;
3. countable positive outside fragments can be kept unnormalized and charged through the Hellinger-type budget `sum sqrt(m_j k_j)` rather than a worst normalized fiber constant.

Hence a codimension-one bad fiber with `K(theta)~dist(theta,theta_0)^(-1)` is harmless under any cap-one scalar outside law: its square root is locally integrable with the exact universal cap (5.7). No first or second moment, support radius, connectedness or finite fragment count is needed.

## 7. What remains

This is a supporting localization theorem, not the unrestricted solution. The bare hypothesis `s_3(A)>=1` has not been shown to produce an invertible indefinite physical pair whose residual critical constants possess a universally bounded square-root budget. The remaining structural problem is to extract such a budget, or one of the completed ridge/grouped-bank/volume exits, **before** paying reciprocal local minors or normalizing thin fragments.

Theorem 3.1 suggests a sharper target for that structural step than the previous `E K` condition: it is enough to establish a universal `E sqrt K` bound for the critical Fourier constants generated by the outside original-coordinate disintegration. Codimension-one reciprocal singularities are then integrable automatically.

Continuity is not obtained from the interval argument above for the full target; only an essentially bounded density is claimed in the stated scope.

## 8. Integrity

- Full QFORM: `OPEN / NOT PROVED / NOT DISPROVED`.
- New theorem: `QFORM-SQRT-CRITICAL-BUDGET-MIXTURE-v1`, equations (3.3), (4.1)-(4.3).
- Designated partner fleet04/B14 r9 is applied at the actual fiber inequality (3.6) and the target-valid family (5.8).
- The theorem strictly weakens the partner mixture hypothesis from finite `E K` to finite `E sqrt K` after physical-pair optimization.
- No pointwise law-uniform quadratic-phase decay, post-rotation independence, arbitrary-joint coarea lemma, conditional projection cap moment, bounded support, fixed fragment count, bounded diameter, or moment condition is used.
- Repository transport is not native learned-memory ingestion; status remains `WITHOUT_VERIFIED_BRAIN`.
