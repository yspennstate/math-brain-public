# QFORM fleet01/B14 — aggregate bilinear localization through a null direction

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B14, 2026-09-23T06:14:54Z.

attacking: translation-uniform localization for aggregate disjoint-bank reductions, with unnormalized fragment mass retained through reciprocal quadratic smoothing.

Programme: `QFORM-DENSITY-3EIG-20260922`.  
Run: `20260923T061454Z-fleet01-B14-QFORM-auto11`.  
Status: **NEW SUPPORTING TARGET-LEVEL THEOREM / FULL QFORM OPEN**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source boundary and exact problem

The target remains: independent real coordinates with densities at most one, arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, and a universal essential density bound for `X^T A X`, or a valid counterexample. No support radius, moments, centering, connected support, log-concavity, identical laws, or independence after rotation is assumed.


Relevant corrections consumed before publication include: no law-uniform pointwise quadratic Fourier decay; no post-rotation independence; no arbitrary-joint rank-three coarea bound; no positive moment of worst conditional projection caps; no bounded-diameter or fixed-fragment-count localization; no universally good single physical minor/cross cut; and no normalization of thin conjugate fibers before a singular reciprocal payment.

Two completed inputs are used at equations:

1. `fleet02/B14` r26, canonical report `yspennstate/math-open-problems@5704e7da5b6134fc8e3bdde6caedc7358a666f65`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B14/20260923T050751Z-fleet02-B14-QFORM-r26/REPORT.md`, plus correction addendum `@19de5b5fc1dcc88d0bad7ce28f7857ae40a8e545`. In particular, for an original-coordinate product bank and a nonzero coefficient vector `a`,

   `||p_(a^T X)||_infinity <= sqrt(2)/||a||_2`.

   Its disjoint-multibank theorem, with the canonical cap choice `eta_j=sqrt(2)/||a_j||_2`, gives `C4/min(nu,r_*)`, where `C4=1000(8+log 4)` and `r_j=gamma_j||a_j||_2/sqrt(2)`.

2. The completed physical-pair logarithmic theorem, canonical source `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`, path `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`. For an invertible indefinite physical `2x2` pair `C`, with `D=|det C|` and `kappa=sigma_min(C)`, after completing the pair its Schur critical remainder `R` obeys, for every `s>0`,

   `p_Q(t) <= 2sqrt(2)/s + D^(-1/2) E log_+(2s^2/(kappa |t-R|)).`        (1.1)

The new step below is to pay the logarithm against a *bilinear aggregate remainder* without conditioning on or normalizing its product-bank linear statistic.

## 2. Exact scalar localization lemma for a bilinear remainder

### Lemma 2.1 — translation-uniform bilinear small ball

Let `U` be independent of a random vector `Y`, with `||p_U||_infinity<=1`. Let `Z=Z(Y)` be a scalar random variable with density cap

`||p_Z||_infinity <= M`.

Let `G(Y)` be arbitrary measurable, let `beta !=0`, and define

`R = 2 beta U Z + G(Y)`.

Translations are included: replacing `Z` by `Z-c` or adding any affine term in `U` simply changes the center of `Z` and does not change `M`.

For every `t` and `rho>0`, put

`q = 2 M rho/|beta|`.

Then

`P(|R-t|<rho) <= S(q)`,                                       (2.1)

where

`S(q)=q(1+log(1/q))` for `0<q<=1`, and `S(q)=1` for `q>=1`.

#### Proof

Condition on `Y`. If `Z(Y)=z !=0`, the event is an interval in `U` of length

`rho/(|beta z|)`,

because the slope of `2 beta U z` is `2 beta z` and the target interval has width `2rho`. Hence

`P(|R-t|<rho | Y) <= min(1, rho/(|beta||Z|)).`                 (2.2)

Set `a=rho/|beta|`. Among all scalar probability densities bounded by `M`, the expectation of the symmetric decreasing function `min(1,a/|z|)` is maximized by the saturated density `M 1_{[-1/(2M),1/(2M)]}` (the one-dimensional bathtub principle). If `a<=1/(2M)`, direct integration gives

`2M[a+a log((1/(2M))/a)] = q(1+log(1/q)).`

If `a>=1/(2M)`, the trivial probability bound one is exact for the bathtub envelope. This proves (2.1). No support location, diameter, fragment count, moment, or tail enters. QED.

### Lemma 2.2 — exact logarithmic payment

For every `A>0`, define

`q_0 = 2 M A/|beta|`.

Then Lemma 2.1 and layer cake give

`E log_+(A/|t-R|) <= Lambda(q_0)`,                             (2.3)

where

`Lambda(q)=q(2-log q)` for `0<q<=1`, and `Lambda(q)=2+log q` for `q>=1`.

Indeed,

`E log_+(A/|t-R|) = integral_0^infty P(|t-R|<A e^{-u}) du`.

If `q_0<=1`, substitute (2.1) and integrate `q_0 e^{-u}(1-log q_0+u)`. If `q_0>=1`, the part `0<=u<=log q_0` contributes `log q_0`, and the remaining integral equals

`integral_0^infty e^{-v}(1+v) dv=2`.

This is the localization point: the aggregate scalar is never conditioned on, so its density cap is paid before any thin-fiber normalization. Arbitrarily remote fragments therefore cannot create an extra conditional-cap factor.

## 3. Compiler with the physical-pair logarithmic theorem

Insert Lemma 2.2 into (1.1). With

`q = 4 M s^2/(kappa |beta|)`

and

`a_0 = 4sqrt(2) sqrt(D M/(kappa |beta|))`,                    (3.1)

we obtain

`||p_Q||_infinity <= D^(-1/2) inf_(q>0) [a_0 q^(-1/2)+Lambda(q)].`  (3.2)

A convenient explicit optimization is:

- if `a_0<=2`, choose `q=1` and obtain

  `||p_Q||_infinity <= D^(-1/2)(a_0+2) <=4 D^(-1/2)`;          (3.3)

- if `a_0>=2`, the minimum of the `q>=1` branch occurs at `sqrt(q)=a_0/2`, giving

  `||p_Q||_infinity <= D^(-1/2)[4+2 log(a_0/2)].`              (3.4)

The theorem is uniform under arbitrary affine shifts generated by conditioning on any disjoint outside original coordinates.

## 4. Rank-two-null aggregate theorem

### Theorem 4.1 — dimension-free aggregate null-direction branch

Let the original independent cap-one coordinates contain three singleton variables `U=(U_1,U_2,U_3)` and an arbitrary product bank `Y=(Y_1,...,Y_d)`, independent of `U`. Let

`Q = U^T B U + 2(k^T U) r^T Y + Y^T H Y + a^T U+b^T Y+c`,     (4.1)

where:

- `B=B^T` has rank two and indefinite nonzero eigenvalues `lambda_+,lambda_-` with `|lambda_+|,|lambda_-|>=1`;
- `k` is a unit null vector, `Bk=0`;
- `H=H^T` is completely arbitrary;
- `||r||_2>=1`;
- all affine coefficients are arbitrary.

Then

`boxed: ||p_Q||_infinity <= sqrt(3)[4+(7/2)log 2] < 11.131.`   (4.2)

The same bound holds with arbitrary additional independent original coordinates and arbitrary couplings to the displayed variables, after conditioning on those outside coordinates.

#### Proof

Choose an original coordinate `i` with `|k_i|>=1/sqrt(3)`, and let `P={1,2,3}\{i}`. Write `C=B_PP`. Since `B` has rank two and null unit vector `k`,

`adj(B)=lambda_+ lambda_- k k^T`.

Therefore

`det C=lambda_+ lambda_- k_i^2`,                              (4.3)

so `C` is an invertible indefinite physical pair. Put

`D=|det C|`, `kappa=sigma_min(C)`, `L=||B||_op`.

Because the smaller nonzero spectral magnitude is at least one,

`D >= L/3`,                                                   (4.4)

and since `||C||_op<=L`,

`kappa >= D/L >=1/3`.                                        (4.5)

Complete the physical pair `U_P` while retaining the original scalar `U_i` and the entire product bank `Y`. The Schur complement can be computed exactly. If `d=B_(P,i)`, the null-vector equation gives

`C k_P+d k_i=0`, hence `C^(-1)d=-k_P/k_i`.                   (4.6)

The scalar-square Schur coefficient is zero because `rank B=2`. The scalar-to-bank coefficient becomes

`k_i-d^T C^(-1)k_P = k_i+||k_P||^2/k_i =1/k_i`.              (4.7)

Consequently the exact critical remainder has the form

`R=2 beta U_i (r^T Y+zeta)+G(Y)`,                             (4.8)

where

`beta=1/k_i`,

`zeta` is an arbitrary constant generated by affine terms, and `G` is an arbitrary quadratic-plus-affine function of `Y`. The arbitrary matrix `H` is absorbed into `G`; no restriction on its rank, sign, or size has been used.

By the partner product-projection cap,

`M := ||p_(r^T Y+zeta)||_infinity <= sqrt(2)/||r||_2 <=sqrt(2).` (4.9)

Moreover `|beta|>=1`, and for the `2x2` pair

`D/kappa=||C||_op<=L`.                                        (4.10)

Thus (3.1) gives

`a_0 <= 2^(11/4) sqrt(L)`.                                   (4.11)

If `a_0<=2`, (3.3) and (4.4) give at most `4sqrt(3)`, which is smaller than (4.2). If `a_0>=2`, use (3.4), (4.4), and (4.11):

`||p_Q||_infinity`
` <= sqrt(3/L) [4+2 log(2^(7/4) sqrt(L))]`
` = sqrt(3) L^(-1/2) [4+(7/2)log2+log L].`                   (4.12)

For `L>=1`, the function `L^(-1/2)[4+(7/2)log2+log L]` is strictly decreasing, because its derivative has sign

`1-(1/2)[4+(7/2)log2+log L] <0`.

Therefore (4.12) is at most its value at `L=1`, proving (4.2).

Finally, arbitrary outside original coordinates may be conditioned on first. They produce only affine terms in the active variables, already allowed in (4.1), so averaging preserves the same constant. QED.

### Why this is genuinely target-valid

The two nonzero eigenvectors of `B` in `k^perp` remain exact invariant directions of the full matrix in (4.1), giving two eigenvalues of modulus at least one. On `span{k} direct_sum R^d`, the remaining symmetric block is

`[[0,r^T],[r,H]].`

Its operator norm is at least `||r||_2>=1`, since its action on `(1,0)` has norm `||r||_2`. Hence it has an eigenvalue of modulus at least one. Thus every matrix covered by Theorem 4.1 lies inside the exact three-large-eigenvalue target.

## 5. Actual application of fleet02/B14 r26 and removal of its selection loss

Take the normalized family

`Q_d = U_1^2-U_2^2 + 2U_3 r^T Y + Y^T H Y + affine`,          (5.1)

where `||r||_2=1`, the `Y_j` are independent cap-one variables, and `H` is **arbitrary**. For a concrete diffuse choice let

`r=(1,...,1)/sqrt(d)`.

Treating the `Y_j` as singleton disjoint banks, fleet02/B14 r26 with its corrected canonical cap `eta_j=sqrt(2)` gives

`r_* = 1/sqrt(2d)`

and therefore the actual partner inequality

`||p_(Q_d)||_infinity <= C4 sqrt(2d),`

`C4=1000(8+log4).`                                            (5.2)

This is a valid inequality but loses `sqrt(d)` because it selects one bank before aggregate payment.

The new theorem instead keeps the entire statistic `r^T Y` aggregated through the logarithmic singularity. Here `D=kappa=|beta|=1` and `M<=sqrt(2)`, so

`a_0=2^(11/4)`

and (3.4) yields the much sharper dimension-free estimate

`boxed: ||p_(Q_d)||_infinity <= 4+(7/2)log2 = 6.4260151319... .` (5.3)

This holds for every `d`, every symmetric `H`, every affine perturbation, every cap-one product input law, arbitrary distant fragments and unbounded supports, with no moments. In particular it strictly extends the earlier rank-one-curvature example: no diffuse/hub orthogonality, leverage condition, or cross-volume certificate inside `H` is required.

The comparison (5.2) versus (5.3) is an equation-level application of the completed designated-partner result and identifies the exact repair: **aggregate the entire product-linear statistic before paying the logarithmic reciprocal singularity.**

## 6. Scope and first unpaid implication

This is not a proof of unrestricted QFORM. The bare hypothesis `s_3(A)>=1` does not yet force a principal representation of the form (4.1) with two uniformly large rank-two core eigenvalues and aggregate null-direction coupling norm at least one. Previous corrections rule out obtaining that by simply choosing one uniformly good physical minor or one weak bank.

The next structural target is therefore: after product-preserving coordinate grouping, prove an exhaustive alternative that either exposes a rank-two-null aggregate core covered by Theorem 4.1, or exits through one of the already completed ridge/cross-volume/mixed-hub mechanisms, without normalizing overlapping or thin conditional fibers first.

No claim of continuity is made here; the conclusion is essential boundedness in the stated target-valid branch. The dependency on the physical-pair theorem is source-pinned and remains at its stated review status. Full QFORM remains OPEN.

## 7. Integrity note

Changed-file scope for this run is confined to this immutable mathematical report and the assigned fleet01/B14 brain handoff/memory/own run records. The text was manually reviewed for credentials, personal material, public-release instructions, and unrelated research; none is present. No public visibility, permission, scheduler, notification, email, task, cross-account authentication, paid call, or remote workflow change is authorized or made.
