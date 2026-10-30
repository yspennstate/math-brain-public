# fleet03/B03 — direct half-Riesz time integral sharpens the rank-two Schur branch

**Run:** `20260922T142410Z-fleet03-B03-QFORM-r13`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Decoupled time integral  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact scope and correction-aware starting point

The full target remains open: for every dimension, independent real coordinates with one-dimensional probability densities at most one, and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove one dimension-free essential-density bound for `Q=X^TAX`, or give a valid target counterexample. Continuity is a separate stronger requirement.

This run stays in original coordinates. It does **not** assume independence after an eigenvector rotation, does not use the refuted law-uniform pointwise one-dimensional Fresnel decay, and does not condition on a sum/difference variable and assign it a false density cap. The independent-copy/Cauchy step is kept in the original product blocks; equivalently, when `|eta(t)|^2` is formed, no claim is made that sums and differences of a coordinate pair are independent.

The exact designated partner `fleet04/B03` still had no completed current-QFORM handoff at the final pre-publication scan, so no partner premise is invented. Two completed compatible results are actually used:

1. fleet03/B09, `QFORM-SCHUR-RANK2-RECTANGULAR-v1`, canonical report `yspennstate/math-open-problems@ad5aac11726332af91f2f2680a10f755e22d08db:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260922T134741Z-fleet03-B09-QFORM-r12/REPORT.md`, which supplies the exact rank-two residual endpoint
   `|eta(t)| <= min(1,2 pi Delta^{-1/2}/|t|)` after a physical pivot;
2. fleet04/B20, `QFORM-CONDITIONED-WHITENED-DIFFUSE-v1`, canonical report `yspennstate/math-open-problems@94bf446b8547b1124a37033e940ef594c460b64f:proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B20/20260922T141640Z-fleet04-B20-QFORM-r2/REPORT.md`, which supplies the complementary diffuse-after-conditioning branch `||p_Q||_infinity < 27/delta` under its exact residual leverage certificate.

The new point here is that the B09 rank-two endpoint should be fed **directly** into a half-order Riesz time integral. Passing first through an `L^3` residual density and then doing spatial interpolation loses a fixed constant. The direct transducer is also closer to the assigned decoupled-time mechanism and yields linear small-ball scaling immediately.

## 2. Main lemma: an endpoint-to-linear-small-ball transducer

### Lemma `QFORM-HALF-RIESZ-ENDPOINT-v1`

Let `Z` be a real random variable with probability density bounded by one and independent of a random element `W`. Suppose

`Q = d (Z+h(W))^2 + R(W)`,

where `d != 0` and `h,R` are arbitrary measurable functions. No independence between `h(W)` and `R(W)` is assumed. Let

`eta(t)=E exp(i t R(W))`.

Assume that for some `K>0`,

`|eta(t)| <= min(1,K/|t|)` for all `t != 0`.                       (2.1)

Then `Q` is absolutely continuous and

`boxed( ||p_Q||_infinity <= 4 sqrt(2/pi) |d|^{-1/2} K^{1/2}. )`     (2.2)

Consequently, for every interval `J`,

`P{Q in J} <= 4 sqrt(2/pi) |d|^{-1/2} K^{1/2} |J|`.                (2.3)

This is linear, rather than square-root, small-ball scaling.

### Proof

Condition on `W=w`. Translation of `Z` preserves the density cap. The map

`z -> d(z+h(w))^2+R(w)`

has at most two inverse branches, and the sum of the two Jacobian contributions is bounded by

`p_{Q|W=w}(s) <= |d|^{-1/2} |s-R(w)|^{-1/2}`                       (2.4)

for almost every `s`; the sign of `d` only chooses the relevant half-line. Averaging gives

`p_Q(s) <= |d|^{-1/2} E |s-R|^{-1/2}`.                             (2.5)

The one-dimensional Riesz kernel has, under the convention

`hat f(t)=int_R exp(-itx)f(x) dx`,

`widehat{|x|^{-1/2}}(t)=sqrt(2 pi)|t|^{-1/2}`.                     (2.6)

The standard Gaussian-regularization argument used in fleet01/B02's completed half-order Fourier proof applies because the forthcoming weighted Fourier integral is absolutely finite. It yields

`sup_s E |s-R|^{-1/2}`
` <= (2 pi)^(-1/2) int_R |t|^{-1/2}|eta(t)| dt`.                  (2.7)

Using (2.1) and splitting at `|t|=K`,

`int_R |t|^{-1/2}|eta(t)| dt`
` <= 2[ int_0^K t^{-1/2}dt + K int_K^infinity t^{-3/2}dt ]`
` = 8 sqrt(K)`.                                                     (2.8)

Thus

`sup_s E |s-R|^{-1/2} <= 4 sqrt(2/pi) K^{1/2}`.                    (2.9)

Insert (2.9) into (2.5). This proves (2.2). The conditional square laws are absolutely continuous, so their mixture is absolutely continuous; integrating the density bound over an interval gives (2.3). QED.

### Dependence point

The shift `h(W)` may be maximally correlated with `R(W)`. It disappears from the envelope (2.4) before averaging. Thus the lemma does **not** use the false hypothesis that the square shift and residual are independent. This is exactly the correlation obstacle left open by several earlier Fourier attempts.

## 3. Application: improved rectangular rank-two Schur theorem

Choose one original coordinate `k` with

`d=A_kk != 0`.

Choose disjoint original-coordinate sets `I,J`, also disjoint from `{k}`. Put

`a=A[I,k]`, `b=A[J,k]`, `B=A[I,J]`,

and let

`C = B-a b^T/d`.                                                     (3.1)

Assume `C` has rank exactly two, with nonzero singular values `s_1,s_2`, and put

`Delta=s_1s_2`.

Condition on all coordinates outside `I union J union {k}`. Completing the physical `k`-square gives exactly

`Q = d[ X_k + (a^T X_I+b^T X_J+c)/d ]^2 + R(X_I,X_J)`,             (3.2)

where the cross block of `R` between the untouched, independent original-coordinate banks `I,J` is `C`. All self terms and conditioned linear terms are arbitrary.

The completed B09 rank-two cross-block calculation gives, uniformly in every outside conditioned value,

`|eta(t)| <= min(1, 2 pi Delta^{-1/2}/|t|)`.                        (3.3)

Apply Lemma 2 with

`K=2 pi Delta^{-1/2}`.

The constants collapse exactly:

`4 sqrt(2/pi) sqrt(2 pi Delta^{-1/2}) = 8 Delta^{-1/4}`.

Hence:

### Theorem `QFORM-SCHUR-RANK2-DIRECT-RIESZ-v1`

Under the hypotheses above,

`boxed( ||p_Q||_infinity <= 8 |d|^{-1/2} Delta^{-1/4}. )`           (3.4)

Equivalently,

`P{Q in J} <= 8 |d|^{-1/2} Delta^{-1/4}|J|`                         (3.5)

for every interval `J`.

This has exactly the same structural hypotheses as B09's `QFORM-SCHUR-RANK2-RECTANGULAR-v1`, but improves its constant from

`16/3^(1/4) = 12.1573709704...`

to

`8`.

The gain is analytic, not numerical: the earlier proof used `eta in L^(3/2) -> p_R in L^3 ->` spatial interpolation, while (2.7)--(2.8) integrates the exact half-order kernel against the endpoint Fourier envelope directly.

No continuity claim is made. The proof yields an essentially bounded Radon--Nikodym density and a linear interval bound. The full characteristic function need not be in `L^1` by this argument.

## 4. Original-coordinate independent-copy derivation and two sharper physical-side constants

For completeness, the endpoint (3.3) itself is a dependence-safe squared/Plancherel estimate. In the square physical case `|I|=|J|=2`, write the conditional residual as

`R(x,y)=q_I(x)+q_J(y)+2x^T C y`                                     (4.1)

with arbitrary real quadratic-affine `q_I,q_J`. Let `rho_I,rho_J` be the product densities of the two untouched original-coordinate pairs and set

`F_t(x)=rho_I(x)e^{itq_I(x)}`,
`G_t(y)=rho_J(y)e^{itq_J(y)}`.

Both satisfy `||F_t||_2,||G_t||_2 <=1` because each product density is a probability density bounded by one. Then

`eta(t)=int F_t(x) hat G_t(-2t C^T x) dx`.

Squaring and applying Cauchy--Schwarz before any sum/difference change gives

`|eta(t)|^2`
` <= ||F_t||_2^2 int |hat G_t(-2tC^Tx)|^2 dx`
` = pi^2 |t|^{-2}|det C|^{-1} ||F_t||_2^2||G_t||_2^2`,             (4.2)

where the last equality is the two-dimensional Plancherel identity and the change of variables `xi=2tC^Tx`. Thus

`|eta(t)| <= min(1, pi |det C|^{-1/2}/|t|)`.                        (4.3)

Equation (4.2) is precisely the safe `|eta|^2` decoupling: it can be written with an independent copy, but no claim of independence is made after replacing any pair by its sum and difference. All independence used is the original independence of the disjoint physical banks `I` and `J`.

Applying Lemma 2 with `K=pi|det C|^{-1/2}` gives the sharper square-bank theorem

`boxed( ||p_Q||_infinity <= 4 sqrt(2) |d|^{-1/2}|det C|^{-1/4}. )` (4.4)

There is an exact homogeneous determinant certificate. Since

`dC=dB-a b^T`,

put

`Theta = |det(dB-a b^T)| = |d|^2 |det C|`.                          (4.5)

Then (4.4) is simply

`boxed( ||p_Q||_infinity <= 4 sqrt(2) Theta^{-1/4}. )`              (4.6)

This form makes the cancellation of the separate pivot scale explicit. If

`M = [[d,b^T],[a,B]]`,

then `det M=d det C`, hence `Theta=|d det M|`.

If only one side, say `I`, consists of exactly two physical coordinates while the other side is an arbitrary original-coordinate bank, the same Plancherel proof pays only one two-dimensional projection loss. The endpoint becomes

`|eta(t)| <= min(1, sqrt(2) pi Delta^{-1/2}/|t|)`,                  (4.7)

so Lemma 2 yields

`boxed( ||p_Q||_infinity <= 2^(11/4)|d|^{-1/2}Delta^{-1/4} )`       (4.8)

with `2^(11/4)=6.7271713220...`.

The three constants form the exact hierarchy

- arbitrary rectangular rank-two banks: `8`;
- one physical two-coordinate side: `2^(11/4) = 6.72717...`;
- two physical two-coordinate sides: `4sqrt(2) = 5.65685...`.

## 5. Strict improvement of the exact-rank-three Pluecker-Schur branch

The same B09 report proves, in exact rank three, the following. Write

`A=U Lambda U^T`, `U^TU=I_3`,

fix a physical pivot row `u` with leverage `ell=||u||^2` and `d=u^TLambda u !=0`, and let `R_2(V)` be the disjoint residual two-dimensional Pluecker mass defined there. B09 proves that some original-coordinate residual cut has Schur cross singular product

`Delta >= [|det Lambda| ell/(4|d|)] sqrt(R_2(V)).`                  (5.1)

Substitute (5.1) directly into the new bound (3.4):

`||p_Q||_infinity`
` <= 8sqrt(2) [|d| ell |det Lambda|]^(-1/4) R_2(V)^(-1/8).`        (5.2)

This improves B09 equation (3.13), whose prefactor was

`16sqrt(2)/3^(1/4)=17.1931189092...`,

to

`8sqrt(2)=11.3137084990...`                                         (5.3)

with no change in structural hypotheses.

If `max_j q_j <= eta <1/2` for the residual two-frame, B09's exact inequality `R_2(V)>=1-2eta` gives

`boxed(
 ||p_Q||_infinity
 <= 8sqrt(2) [|d| ell |det Lambda|]^(-1/4)(1-2eta)^(-1/8).
)`                                                                   (5.4)

Under the target exact-rank-three normalization `|det Lambda|>=1`, that factor may be dropped from the denominator.

This is a genuine application of the new time-integral lemma to a completed team result, not merely a citation.

## 6. Application of a completed fleet04 result: an explicit two-certificate closure

The completed fleet04/B20 theorem states that if, after conditioning a heavy original-coordinate set `H`, the residual spectral Gram has floor `delta>0` and every whitened residual leverage is at most `1/32`, then

`||p_Q||_infinity < 27/delta`,                                      (6.1)

and the density in that branch is continuous.

Combining (6.1) with (3.4) gives a concrete target-level sufficient dichotomy: if a target matrix satisfies **either**

- the fleet04/B20 conditioned-whitened certificate with `delta>=1/2`, or
- a physical pivot plus rank-two Schur certificate with `|d|^2 Delta >=1/16`,

then it has an essentially bounded density with the universal bound

`||p_Q||_infinity < 54`.                                            (6.2)

Indeed the first branch gives `<54`, while the second gives

`8(|d|^2Delta)^(-1/4) <= 16`.

This does not claim that every target matrix satisfies that dichotomy. Its value is to formulate the remaining structural debt in dimensionless certificate form.

The known hard saddle family from fleet01/B19 correctly lies outside the rank-two-Schur alternative: its natural nonzero pivots leave only a rank-one star after Schur completion, while conditioning the unique heavy pivot can collapse a spectral direction. That family is instead controlled by product-preserving hyperbolic bank aggregation. Thus the new theorem respects, rather than contradicts, `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`.

## 7. What is now unpaid

The new analytic step closes the **time-integral** part of a rank-two-Schur-plus-square mechanism with a linear small-ball estimate and strictly better constants. It does not prove that the three-large-eigenvalue hypothesis always yields such a certificate.

The first target-relevant unpaid implication is therefore structural:

**`QFORM-THREE-WAY-AGGREGATE-CERTIFICATE-v1`.** Starting only from three eigenvalues of modulus at least one, prove a dimension-free exhaustive alternative among

1. conditioned-whitened diffuse residual geometry;
2. a nonzero physical pivot whose **aggregated** Schur cross operator has rank two and dimensionless certificate `|d|^2 Delta` bounded below;
3. a product-preserving hyperbolic/bank normal form of the type that controls the exact hard saddle families.

The live counterexamples show that one fixed coordinate minor or one local Schur extraction cannot serve as alternative 2. Aggregation must occur before reciprocal determinant payment.

The full arbitrary-matrix conjecture therefore remains **OPEN**. The new theorem proves essential boundedness only in its stated branches. Full continuity remains open outside branches already having an `L^1` characteristic function or another independent continuity argument.

## 8. Numerical/algebraic diagnostics

The exact constants are

- `16/3^(1/4) = 12.15737097042548` (previous B09 rectangular constant),
- `8` (new arbitrary-rectangular direct-Riesz constant),
- `2^(11/4) = 6.727171322029716` (one physical two-coordinate side),
- `4sqrt(2) = 5.656854249492381` (two physical two-coordinate sides).

A separate checker in this run verifies the square Schur determinant identities `det(dB-ab^T)=d^2 det C` and `det M=d det C` on exact rational test instances. These checks are diagnostics; the proof above is analytic.

## 9. Status

- `QFORM-HALF-RIESZ-ENDPOINT-v1`: **PROVED supporting lemma**.
- `QFORM-SCHUR-RANK2-DIRECT-RIESZ-v1`: **PROVED supporting theorem**, same structural scope as B09 but stronger constant.
- square determinant certificate (4.6): **PROVED**.
- exact-rank-three Pluecker-Schur improvement (5.2)--(5.4): **PROVED under the B09 branch hypotheses**.
- designated partner `fleet04/B03`: **no completed current-QFORM result observed; not fabricated**.
- completed fleet04/B20 result: **APPLIED to the explicit inequality (6.2)**.
- full owner target: **OPEN / NOT PROVED**.
- continuous density for the new Schur branch: **NOT PROVED**.
- native learned-memory receiver use: **NOT OBSERVED**; execution remains `WITHOUT_VERIFIED_BRAIN`.
