SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B08, 2026-09-22T20:40:04Z.
attacking: grouped payment of the two-sided near-coloop/bicoloop branch without selecting a reciprocal minor.

# fleet01/B08 — rank-two physical cross blocks give a dimension-free half-Riesz smoother

**Run:** `20260922T204004Z-fleet01-B08-qform-r17`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control observed:** revision `2026-09-22.15`  
**Assignment:** diffuse eigenvector case  
**Status:** `ESSENTIAL_STEP_APPLIED / INDEPENDENT SUPPORTING DERIVATION / EXACT-RANK2 BICOLOOP SUBBRANCH PAID / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Full target and first unpaid implication

The full target remains open: for arbitrary dimension, arbitrary independent real inputs with densities at most one, and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal bound for the density of `X^T A X`, with continuity tracked separately.

This run changes mechanism from leverage-threshold optimization to grouped physical-coordinate smoothing. It consumes the current corrections: no law-uniform pointwise Fresnel decay, no independence after rotation, no unrestricted fiber supremum, no arbitrary-joint rank-three coarea bound, no positive conditional projection-density moment, no selected reciprocal minor, and no near-zero-pivot one-arm half-Riesz shortcut.

The designated partner result actually consumed is fleet02/B08 `QFORM-REGULARIZED-BICOLOOP-SCHUR-STAR-v1`, canonical source

`yspennstate/math-open-problems@7f37e244e4ec78acf9f499ebdf06ad3cb79a4ede`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/B08-20260922T201017Z-r15/REPORT.md`.

In its unpaid two-sided near-coloop branch, at `g=gamma/16`, for the actual physical cross block `H` one forms

`Z=H(g^2 I+H^T H)^(-1/2)`

and obtains a heavy physical row/column whose complete incident normalized minor bank obeys

`sum_{k!=j,s!=r} det Z[{j,k},{r,s}]^2 > c_*`,

where

`c_*=2349/5000`.                                           (1.1)

That source also gives the exact `d`-arm star obstruction showing why selecting one minor loses dimension. The first unpaid implication is therefore to consume a genuinely grouped rank-two bank before reciprocal inversion.

A second dependency is fleet02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical source

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

For every orthonormal `n x k` frame `R`, the projection `R^T X` of an independent cap-one product law has density bounded by `exp(k/2)`. In particular every two-dimensional orthogonal projection has density cap `e`. This is a weighted affine-fiber integral and does not invoke the refuted fiber-supremum step.

## 2. Grouped rank-two cross half-Riesz payment

### Proposition `QFORM-RANK2-PHYSICAL-CROSS-HALF-RIESZ-v1`

Let `I,J` be disjoint sets of original coordinates and let the corresponding inputs be independent with one-dimensional probability densities bounded by one. Let

`R(x,y)=q_I(x)+q_J(y)+2 x^T B y`,                         (2.1)

where `q_I,q_J` are arbitrary real measurable functions for which the displayed expectation is defined; in the QFORM application they are arbitrary quadratic-plus-linear self terms induced after conditioning outside coordinates. Assume the **physical cross block** `B` has exact rank two, with nonzero singular values

`s_1 >= s_2 > 0`.                                         (2.2)

Then for every `u in R`,

`E |R-u|^(-1/2) <= 4 sqrt(2e) (s_1 s_2)^(-1/4)`.           (2.3)

The bound is dimension-free, does not assume moments, compact support, log-concavity or post-rotation independence, and allows arbitrary self quadratic forms on the two physical sides.

### Proof

Take a singular-value decomposition

`B=U Sigma V^T`,  `Sigma=diag(s_1,s_2)`,                   (2.4)

with `U,V` having orthonormal columns. For each Fourier frequency `t`, push the two physical product measures to the two-dimensional variables

`xi=U^T x`, `eta=V^T y`,                                  (2.5)

while retaining the self phases. Define the complex amplitudes by affine-fiber integration

`F_t(xi)= integral_{U^T x=xi} exp(i t q_I(x)) prod_{i in I} f_i(x_i) dH`,

`G_t(eta)= integral_{V^T y=eta} exp(i t q_J(y)) prod_{j in J} f_j(y_j) dH`,       (2.6)

with the coarea normalizations induced by the orthonormal maps. The ordinary projected densities `p_U,p_V` satisfy, pointwise,

`|F_t|<=p_U`, `|G_t|<=p_V`.                                (2.7)

By `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1` at `k=2`,

`||p_U||_infinity<=e`, `||p_V||_infinity<=e`.              (2.8)

Also `||F_t||_1,||G_t||_1<=1`. Therefore

`||F_t||_2<=sqrt(e)`, `||G_t||_2<=sqrt(e)`.                (2.9)

The characteristic function is now exactly

`phi_R(t)= integral_R2 integral_R2 F_t(xi) G_t(eta)
           exp(2 i t xi^T Sigma eta) dxi deta`.             (2.10)

No independence of the rotated coordinates is asserted: all product structure was used before and inside the affine-fiber amplitudes.

For `t!=0`, use Plancherel only on the two-dimensional eta-variable. With the convention `hat G(zeta)=integral exp(i zeta.eta)G(eta)deta`,

`||hat G||_2=(2 pi)||G||_2`,                               (2.11)

and the linear change `zeta=2t Sigma xi` gives

`||hat G_t(2t Sigma .)||_2
 = pi / (|t| sqrt(s_1 s_2)) ||G_t||_2`.                    (2.12)

Thus Cauchy-Schwarz and (2.9) yield the law-uniform but grouped estimate

`|phi_R(t)| <= min(1, A/|t|)`,

`A = pi e / sqrt(s_1 s_2)`.                               (2.13)

This is not the refuted one-dimensional pointwise van-der-Corput claim; the `1/|t|` comes from a genuine two-dimensional Fourier transform of the whole physical cross block.

We now pay exactly the fractional smoothing needed by a physical square pivot. For `eps>0`, set

`k_eps(x)=sqrt(2/pi) integral_0^infinity exp(-eps t) cos(tx) t^(-1/2) dt`.         (2.14)

This integral is absolutely convergent and equals a positive real multiple of `Re (eps-i x)^(-1/2)`, hence `k_eps(x)>=0`; moreover it converges pointwise to `|x|^(-1/2)` as `eps downarrow0` by

`integral_0^infinity cos(tx)t^(-1/2)dt=sqrt(pi/2)|x|^(-1/2)`.                    (2.15)

Tonelli at fixed `eps`, followed by the characteristic-function bound and Fatou, gives

`E|R-u|^(-1/2)
 <= sqrt(2/pi) integral_0^infinity |phi_R(t)| t^(-1/2)dt
 <= sqrt(2/pi) [integral_0^A t^(-1/2)dt
                 + A integral_A^infinity t^(-3/2)dt]
 = 4 sqrt(2/pi) sqrt(A)
 = 4 sqrt(2e) (s_1 s_2)^(-1/4)`.                          (2.16)

This proves (2.3).

## 3. Full-ambient scalar-pivot corollary

### Corollary `QFORM-PIVOT-PLUS-RANK2-CROSS-v1`

Let `X_0` be one original input coordinate, independent of all remaining coordinates `Y`, with density at most one. Write the full quadratic form as

`Q=a X_0^2+2 X_0 L(Y)+R_0(Y)`, `a!=0`.                     (3.1)

After physical square completion put

`S(Y)=R_0(Y)-L(Y)^2/a`,

so

`Q=a(X_0+L(Y)/a)^2+S(Y)`.                                 (3.2)

Suppose that, after conditioning any further original coordinates if necessary, some physical cut of the Schur residual `S` has exact rank-two cross block `B` with singular values `s_1,s_2`. Then `Q` has an essentially bounded density and

`||p_Q||_infinity <= 4 sqrt(2e) / [sqrt(|a|) (s_1 s_2)^(1/4)]`.                  (3.3)

Indeed, conditional on `Y`, the translated variable `X_0+L(Y)/a` still has density at most one. Therefore the conditional square density is bounded by

`|a|^(-1/2)|v|^(-1/2)`                                    (3.4)

on its supported half-line. Averaging and applying Proposition 2 to `S` gives (3.3). Arbitrary outside couplings merely become affine self terms after conditioning and are already permitted by (2.1).

This proves essential boundedness. Continuity is **not claimed** from this fractional-potential argument alone.

## 4. Direct application of the assigned partner's bicolloop bank

Apply fleet02/B08 r15 to its unpaid nonzero physical-pivot branch, with pivot coefficient denoted `a_0`, residual cross block `H`, and `g=gamma/16`. Assume now that this residual block has exact rank two. Let `s_1,s_2` be its two nonzero singular values and let

`z_i=s_i/sqrt(g^2+s_i^2)`, `i=1,2`,                         (4.1)

be the two nonzero singular values of `Z`.

For a rank-two matrix, Cauchy-Binet gives the exact total minor identity

`sum_{|K|=|S|=2} det Z[K,S]^2 = z_1^2 z_2^2`.              (4.2)

The partner's incident bank (1.1) is a sub-sum of (4.2), hence

`z_1^2 z_2^2 > c_* =2349/5000`.                            (4.3)

Because each `z_i^2<1`, (4.3) implies separately `z_i^2>c_*`. Solving (4.1),

`s_i^2/g^2 = z_i^2/(1-z_i^2) > c_*/(1-c_*) =2349/2651`.    (4.4)

Therefore

`s_1 s_2 > (2349/2651) g^2
          =(2349/2651) gamma^2/256`.                       (4.5)

Insert (4.5) into the scalar-pivot corollary:

`||p_Q||_infinity
 < 16 sqrt(2e) (2651/2349)^(1/4) / sqrt(|a_0| gamma)
 < 38.452 / sqrt(|a_0| gamma)`.                            (4.6)

Thus the exact-rank-two subbranch of the partner's bicolloop regime is paid without selecting one physical minor. The determinant bank is consumed through the product of the two singular directions before reciprocal inversion.

## 5. The partner's star obstruction is positively controlled

The partner gives an exact `d`-arm star cross block

`H_d=[[0,alpha^T],[beta,0]]`,                              (5.1)

with all arm entries `gamma/sqrt(d)`. Hence

`||alpha||=||beta||=gamma`,

and the only nonzero singular values of `H_d` are both exactly `gamma`. Every individual incident minor is only order `gamma^2/d`, so reciprocal single-minor selection loses dimension; nevertheless Proposition 2 sees the whole grouped bank and gives

`sup_u E|S-u|^(-1/2) <=4 sqrt(2e) gamma^(-1/2)`.            (5.2)

For the partner's target-valid construction with scalar pivot `a_0=1` and `gamma=1`, Corollary 3 gives the explicit dimension-free density estimate

`||p_Q||_infinity <=4 sqrt(2e)=9.326575926...`.             (5.3)

Thus the exact source-valid obstruction to one-minor selection is not an obstruction to grouped payment: its complete two-arm structure is quantitatively sufficient.

## 6. Fresh source overlap check and sharpened remaining gap

A required prepublication refresh found two newer relevant completed reports.

First, fleet03/B06 r17, canonical

`yspennstate/math-open-problems@1287456c9a709f8c3f117c23faa46e75f4560d01`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260922T194649Z-fleet03-B06-qform-r17/REPORT.md`,

independently proves a stronger density-level exact-rank-two cross-bank theorem using an `L^3` route and a dependent-square smoother. Consequently **no novelty or priority claim is made for exact-rank-two analytic closure in this report**. Proposition 2 is retained as an independent, short half-Riesz derivation with an explicit potential estimate that consumes the designated fleet02/B08 bank directly.

Second, fleet01/B06 r16, canonical

`yspennstate/math-open-problems@4ed07d5034b4499841f831975ceccfbf1ae45606`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B06/20260922T203709Z-qform-r16-b06/REPORT.md`,

sharpens the only current near-coloop survivor. It proves that the actual residual cross block admits a best rank-two core `H_2` with

`sigma_2(H_2)>0.19915795 gamma`,

`||H-H_2||_F <0.05682048 sigma_2(H_2)`.                    (6.1)

Thus the live unpaid implication is no longer a generic `rank>2` problem. It is the explicit **strong-rank-two plus <=5.683% relative tail** stability problem.

The combined current implication is

`QFORM-STRONG-RANK2-TAIL-STABILITY-v1`:

> For a disjoint-bank quadratic form with arbitrary within-bank quadratic/affine terms and cross block `H=H_2+E`, prove a dimension-free fractional-potential or square-smoothing estimate when `rank(H_2)=2`, `sigma_2(H_2)>=c gamma`, and `||E||_F<=0.057 sigma_2(H_2)`, without moments/support assumptions and without selecting a reciprocal physical minor; or convert `E` into an already-paid ridge/second-curvature branch.

The present Fourier proof explains exactly why this is nontrivial: when `E=0`, integrating the physical affine fibers leaves the two top projected amplitudes factorized, enabling two-dimensional Plancherel. A nonzero orthogonal cross tail couples the two fiber variables and destroys that factorization. Coefficient-smallness alone does not justify dropping the phase under arbitrary fragmented/remote supports. The required stability inequality must therefore retain the tail jointly rather than perturb it absolutely.

## 7. Conditional end-to-end position

Current nonzero-pivot architecture: broad ridge branches are paid; fleet03/B08 and fleet02/B08 reduce the two-sided near-coloop branch to grouped determinant currency; fleet03/B06 pays exact rank-two arbitrary-self-block cross banks; fleet01/B06 shows the sole remaining survivor lies in the quantitative tube (6.1). Proving `QFORM-STRONG-RANK2-TAIL-STABILITY-v1` would close this specific nonzero-pivot survivor. Separate zero/near-zero physical-pivot and global exhaustive-reduction debts remain.

Therefore full QFORM is **OPEN / not proved / not disproved**. This report proves essential boundedness only in the exact-rank-two pivot branch; continuity is not claimed there.

## 8. Exact constants

The companion `verify.py` checks only the displayed algebra and constants:

`c_*=2349/5000`,
`c_*/(1-c_*)=2349/2651`,
`4sqrt(2e)=9.326575926...`,
`16sqrt(2e)(2651/2349)^(1/4)=38.451554256...`.

A finite checker is not an independent proof review.