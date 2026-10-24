SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B18, 2026-09-22T18:15:04Z.
attacking: the rank-one endpoint of the product-preserving one-sided Schur-cross branch, using sharp product marginal density bounds and fractional square smoothing rather than conditioning away the product source.

# account02/B18 — one-sided cross half-Riesz hierarchy and the rank-one Schur endpoint

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T181504Z-account02-B18-QFORM-r12`  
**Assignment:** Literature-to-proof transfer  
**Fresh control at mathematical start:** brain main `0ae6e7fcbee02908fb8b1595108284e928d19835`, owner control revision `2026-09-22.11`; refreshed during proof to `d4c3b6e2da0616173d467b0f100cfdc4c60c5e46`.  
**Status:** `PROVED_SUPPORTING_THEOREMS / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (authenticated repository retrieval occurred; no native learned-memory receiver use).

## 1. First unpaid implication attacked

The full target remains OPEN: for arbitrary dimension, independent real coordinates with one-dimensional probability densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite bound for the density of `X^T A X`, or give a target-valid counterexample.

The live correction `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE` shows that one may be left, after a physical scalar pivot, with only a **rank-one** one-sided cross star. The completed designated partner account03/B18 theorem `QFORM-ONE-SIDED-CROSS-AGGREGATE-v1` pays the corresponding product branch when the cross matrix has rank at least two, but its density proof has no rank-one endpoint. The newest completed partner run also proves that conditioning on the full orthogonal spectral complement can make every positive conditional projection-density moment diverge; aggregation must occur before that conditioning.

This run closes the missing **rank-one one-sided-cross endpoint after a nonzero scalar pivot**, without moments, support assumptions, or independence after rotation. Together with the partner theorem, every nonzero cross rank is now paid whenever one side of the post-Schur physical block has exactly zero self-quadratic block. The spectral hypothesis is not proved to force that geometry, so this is not a full solution.

## 2. Source-matched literature transfer

### 2.1 Livshyts--Paouris--Pivovarov

Primary source: G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1.

If `X` has independent coordinates with probability densities bounded by one and `E` is a `j`-dimensional subspace, then the orthogonal marginal onto `E` has density bounded by `2^(j/2)`. In particular, every unit linear form has density at most `sqrt(2)`.

This is an exact source match: no moments, bounded support, log-concavity, identical laws, centering, or post-rotation independence is assumed. I use the theorem only for genuine orthogonal marginals of the original product source, before any conditioning that could destroy product structure.

### 2.2 Hu--Paouris is not an `L^infinity` rank-one closure

Primary source: X. Hu, G. Paouris, *Small Ball Probabilities for Simple Random Tensors*, arXiv:2403.20192. For an order-`ell` simple tensor of independent vectors with independent bounded-density coordinates, their small-ball theorem has the scale

`epsilon/(ell-1)! * (C log(e/epsilon))^ell`,

and the paper states that this order is sharp when the projection dimension is small. At the scalar bilinear endpoint `ell=2`, this retains logarithmic loss and therefore does **not** imply a bounded density for a single bilinear product. This exactly matches the familiar logarithmic product singularity. I therefore do not transfer that theorem as a false rank-one density estimate; instead the argument below asks only for a half-Riesz potential, which is the amount of smoothing supplied by one additional genuine square pivot.

## 3. Two elementary fractional rearrangement lemmas

### Lemma 3.1 — scalar capped half-Riesz potential

If a real random variable `Z` has a probability density bounded by `K`, then

`sup_t E |Z-t|^(-1/2) <= 2 sqrt(2K)`.                       (3.1)

**Proof.** The kernel is symmetric decreasing around `t`. By the bathtub principle, the cap-`K`, mass-one density maximizing the integral is `K` on the centered interval of length `1/K`. Thus

`K int_{-1/(2K)}^{1/(2K)} |x|^(-1/2) dx = 2 sqrt(2K)`.
QED.

### Lemma 3.2 — inverse-half radius under a joint density cap

Let `Z` be `R^j`-valued with density bounded by `M`, `j>=1`, and let `v_j` be the volume of the Euclidean unit ball in `R^j`. Then

`E ||Z||^(-1/2)
 <= [2j/(2j-1)] (M v_j)^(1/(2j)).`                         (3.2)

**Proof.** Layer cake and the ball-volume bound give

`E ||Z||^(-1/2)
 = int_0^infinity P(||Z||<s^(-2)) ds
 <= int_0^infinity min(1,M v_j s^(-2j)) ds`.

Split at `s_0=(M v_j)^(1/(2j))`. The integral is

`s_0 + M v_j s_0^(-(2j-1))/(2j-1)
 = [2j/(2j-1)] s_0`.
QED.

## 4. Main theorem — one-sided cross half-Riesz aggregation, including rank one

Let `U in R^m` and `V in R^k` be mutually independent coordinate families; all individual coordinates have probability densities bounded by one. Let `B` be an `m x k` real matrix of rank `r>=1`, with singular values

`sigma_1>=...>=sigma_r>0`,

let `G:R^m->R` be arbitrary measurable and finite almost surely, and let `beta in R^k`. Put

`T = G(U) + 2 U^T B V + beta^T V`.                          (4.1)

### Theorem 4.1 — `QFORM-ONE-SIDED-CROSS-HALF-RIESZ-v1`

For every `1<=j<=r`,

`sup_t E |T-t|^(-1/2)
 <= 2^(3/2) [2j/(2j-1)]
    [v_j / prod_(ell=1)^j sigma_ell(B)]^(1/(2j)).`          (4.2)

In particular the formerly unpaid rank-one endpoint is

`boxed: sup_t E |T-t|^(-1/2) <= 8 sigma_1(B)^(-1/2).`       (4.3)

No self-quadratic restriction is imposed on the `U` side because it is absorbed into the arbitrary function `G`. The `V` side has no self-quadratic term.

### Proof

Fix `U=u` and set

`c(u)=2B^T u+beta`.

Conditionally on `U=u`, `T` is a translation of the linear form `c(u)^T V`. For `c(u)!=0`, the one-dimensional LPP theorem gives density cap

`K(u)<=sqrt(2)/||c(u)||`.

Lemma 3.1 therefore yields

`sup_t E_V |T-t|^(-1/2 | U=u)
 <=2^(7/4)||c(u)||^(-1/2).`                                 (4.4)

The affine solution set `c(u)=0` has codimension at least one and hence zero probability because `U` has an absolutely continuous joint law.

Choose the top `j` left/right singular vectors `e_ell,v_ell` of `B`, and put

`W=(e_1^T U,...,e_j^T U)`.

By the `j`-dimensional LPP theorem, `W` has density at most `2^(j/2)` (if `j=m`, the full orthogonal image actually has density cap at most one, so the weaker displayed cap still holds). Define

`Z_ell=2 sigma_ell W_ell + <beta,v_ell>`.

Then `||c(U)||>=||Z||`, while the density of `Z` is bounded by

`M <= 2^(j/2) / [2^j prod_(ell<=j)sigma_ell]
   = 2^(-j/2)/prod_(ell<=j)sigma_ell.`                      (4.5)

Lemma 3.2 gives

`E ||c(U)||^(-1/2)
 <= [2j/(2j-1)] 2^(-1/4)
    [v_j/prod_(ell<=j)sigma_ell]^(1/(2j)).`                 (4.6)

Average (4.4) and multiply constants: `2^(7/4)2^(-1/4)=2^(3/2)`. This proves (4.2). For `j=1`, `v_1=2`, and (4.2) reduces exactly to (4.3). QED.

The theorem is a half-Riesz statement, not a claim that rank-one bilinear output itself has bounded density. That distinction is essential and source-valid.

## 5. Fractional square transducer

### Lemma 5.1 — `QFORM-HALF-RIESZ-SQUARE-TRANSDUCER-v1`

Let `(R,V)` be any pair of real random variables. Suppose

`M:=sup_t E|R-t|^(-1/2)<infinity`

and for almost every `r`, the conditional law of `V` given `R=r` has a density bounded by `K`. Then for every `a!=0`,

`S=R+aV^2`

has an essentially bounded density satisfying

`boxed: ||p_S||_infinity <= K M / sqrt(|a|).`                (5.1)

No independence between `R` and `V` is required.

**Proof.** For `a>0`, conditionally on `R=r`, the density of `aV^2` at `y>0` is

`[h_r(sqrt(y/a))+h_r(-sqrt(y/a))]/[2sqrt(a y)]
 <=K/sqrt(a y)`.

Thus the mixture has density

`p_S(t)
 <=K/sqrt(a) int_{r<t}|t-r|^(-1/2) dmu_R(r)
 <=K M/sqrt(a)`.

For `a<0`, reflect the one-sided kernel. This also constructs the asserted density. QED.

This is the precise fractional version of the completed dependence-safe square-smoothing mechanism: the base variable need not already have an `L^infinity` density.

## 6. Schur consequence and combination with the designated partner

Take an original physical pivot coordinate `Y` with `a=A_YY!=0`, and write its Schur complement

`S=A_{-Y,-Y}-A_{-Y,Y}A_{Y,-Y}/a`.                           (6.1)

Partition the residual physical coordinates into disjoint sets `I,J,O`. Assume

`S[J,J]=0`,

and put `B=S[I,J]`, with `rank(B)>=1`. All of `S[I,I]`, every coupling involving `O`, and the dimension/sign/additional spectrum are arbitrary.

Condition on `X_O=w`. The residual is exactly

`R_w=G_w(X_I)+2X_I^T B X_J+beta_w^T X_J+const_w`,           (6.2)

so Theorem 4.1 applies uniformly in `w`. Unconditioning preserves the same half-Riesz bound.

After completing the original pivot,

`Q=a(Y+a^(-1)A_{Y,-Y}X_{-Y})^2+R`.                         (6.3)

Conditioned on `R=r`, the shifted pivot is a mixture of translations of the original cap-one density of `Y`; hence its conditional density is still at most one. Lemma 5.1 applies.

### Corollary 6.1 — `QFORM-ONE-SIDED-SCHUR-ALL-RANK-v1`

If `rank(B)=1`, then

`boxed: ||p_Q||_infinity <= 8 / sqrt(|a| sigma_1(B)).`       (6.4)

For `rank(B)>=2`, the completed designated partner account03/B18 theorem is sharper: its `QFORM-ONE-SIDED-CROSS-AGGREGATE-v1`, combined with its completed dependence-safe square wrapper, gives

`||p_Q||_infinity
 <=2 |a|^(-1/2)
   min_(2<=j<=rank B)
   sqrt( [j/(j-1)] [v_j/prod_(ell<=j)sigma_ell(B)]^(1/j) ).` (6.5)

Therefore **every nonzero rank** of an exact one-sided-zero Schur cross bank is now paid: rank one by (6.4), rank at least two by the partner bound (6.5). This is an actual combination of compatible calculations, not a transfer beyond either theorem's hypotheses.

The newest account03/B18 correction is also obeyed substantively: no normalized conditional spectral density is introduced. The independent physical banks are aggregated first, and only the original scalar pivot is conditioned through a mixture-of-translations argument after the fractional payment has been made.

## 7. Exact target-valid stress family showing the rank-one aggregation gain

Let `m>=2` be even. On an `m`-coordinate bank `I`, let

`u=m^(-1/2)(1,...,1)`,
`w=m^(-1/2)(1,...,1,-1,...,-1)`,

with `m/2` plus signs and `m/2` minus signs, so `u perp w`. On a disjoint `m`-coordinate bank `J`, let `v=m^(-1/2)(1,...,1)`. Define the residual block

`S_II=w w^T`, `S_IJ=u v^T`, `S_JJ=0`,                     (7.1)

and add one independent physical pivot with coefficient `a=1` and no coupling to the residual:

`A_m = [1] direct_sum S`.                                   (7.2)

In the orthonormal basis `(u,w,v)`, the nonzero part of `S` is

`[[0,0,1],[0,1,0],[1,0,0]]`,                               (7.3)

whose eigenvalues are `{1,1,-1}`. Hence

`spec_nonzero(A_m)={1,1,1,-1}`,

so this is an exact target-valid family for every even `m`, with no distributional assumptions beyond the owner's cap-one product class.

Here `B=u v^T` has rank one and `sigma_1(B)=1`. Corollary 6.1 gives the dimension-free bound

`boxed: ||p_(X^T A_m X)||_infinity <=8.`                    (7.4)

The designated partner's rank-at-least-two theorem does not apply to this cross block. A proof that selects one physical row of the diffuse `I` bank sees cross norm only `1/sqrt(m)` and loses a factor growing like `m^(1/4)` after square smoothing. The aggregate singular value is exactly one, so (7.4) demonstrates the concrete gain from aggregating the whole original-coordinate bank before inversion.

## 8. Literature boundary and remaining full-target implication

Hu--Paouris correctly warns against demanding a bounded density from a single scalar bilinear/tensor projection: logarithmic losses are genuine at low projection dimension. The extra physical square pivot supplies exactly the missing half-order through Lemma 5.1. LPP supplies the source-valid marginal caps needed to make this quantitative while preserving the original product law.

What is **not** proved: the bare condition `s_3(A)>=1` does not yet imply the existence of a scalar pivot and an exact one-sided-zero Schur bank with `|a| sigma_1(B)` uniformly bounded below. It also does not permit dropping a nonzero self-quadratic block on the `J` side as a small perturbation, because inputs have no moments or support bounds.

After combining this run with the owner-supplied full-matrix indefinite-pair theorem and the ridge-window theorem, the first unpaid structural implication is now:

`QFORM-AGGREGATE-BEFORE-INVERSION-EXHAUSTION-v1` — from `s_3(A)>=1`, outside the already-paid ridge window and quantitatively invertible indefinite physical-pair branches, extract a product-preserving grouped-coordinate certificate that is either (i) a nonzero scalar pivot plus an exact one-sided-zero cross bank with quantitative aggregate singular value, or (ii) another already-paid grouped/ridge packet. No fixed-minor, post-rotation-independence, or conditional-moment shortcut is allowed.

The full universal QFORM conjecture remains **OPEN / NOT PROVED**. Continuity is not claimed from the new rank-one scalar-pivot wrapper.

## 9. Source pins

1. Livshyts--Paouris--Pivovarov, arXiv:1507.07949, Theorem 1.1.
2. Hu--Paouris, arXiv:2403.20192, simple-random-tensor small-ball theorem and sharp-low-dimensional statement.
3. Designated partner account03/B18 `QFORM-ONE-SIDED-CROSS-AGGREGATE-v1`: `yspennstate/math-open-problems@fb0c75e8f951da2564fe595f09f7e484c37dfd40`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B18/B18-20260922T155856Z-r13/REPORT.md`.
4. Latest completed partner correction/aggregate-before-conditioning rescue: `yspennstate/math-open-problems@58cde0caae66f5236332d48a1022fa7c5d12a1f7`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B18/20260922T175531Z-account03-B18-QFORM-r15/REPORT.md`.
5. Current owner proof-first request and full-matrix pair theorem source are pinned by brain control revision `2026-09-22.11`; no claim from those sources is extended beyond its stated scope here.
