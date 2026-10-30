SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B13, 2026-09-23T11:02:12Z.
attacking: the designated partner's two-hub leaf-curvature gap by reversing which original-coordinate bank is null, while aggregating the whole curved leaf bank before reciprocal payment.

# fleet01/B13 auto21 — dual rectangular null-bank aggregation with arbitrary opposite-side curvature

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** Extremal product laws  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** **ESSENTIAL_STEP_APPLIED / PROVED SUPPORTING TARGET-LEVEL BRANCH / FULL QFORM OPEN / FULL CONTINUITY OPEN**

The full conjecture is not proved or disproved here. The new result pays a complementary endpoint of the current two-hub/trihub obstruction: the newest designated-partner theorem requires the large leaf bank to be exactly null but allows arbitrary hub curvature; the theorem below requires the finite hub bank to be exactly null but allows **completely arbitrary curvature on the large leaf bank**. Both retain all original-coordinate independence and arbitrary fragmented/unbounded input laws.

## 1. Fresh scope and immutable premises


The designated partner actually applied is the newest `fleet02/B13` theorem:

- `yspennstate/math-open-problems@597eebafb5c9c540ef679226b655f23ea436d4e4`
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260923T102244Z-fleet02-B13-extreme-7c91d2ab/REPORT.md`.

It proves `QFORM-RECTANGULAR-NULLBANK-AGGREGATE-v1`. For `r>=2`, an `r x m` full-row-rank original-coordinate cross block `B`, and

`Q=F(U,Z)+2 U^T B V+c(Z)^T V`,

with the **V-bank exactly null**, one has

`||p_Q||inf <= K_r det(BB^T)^(-1/(2r))`,
`K_r=[r/(sqrt(2)(r-1))] omega_r^(1/r)`.                            (1.1)

For `r=2`, `K_2=sqrt(2pi)`. Its proof also records the two analytic ingredients used below:

`||p_{a dot U}||inf <= sqrt(2)/||a||_2`                            (1.2)

for an original independent cap-one bank, and the reciprocal-distance lemma

`sup_z E ||Y-z||^(-1) <= [r/(r-1)] omega_r^(1/r) M^(1/r)`          (1.3)

whenever an `R^r` probability density is bounded by `M`.

A second completed source is fleet02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`:

- `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

If `R` is `m x r` with orthonormal columns and `V` has independent cap-one scalar coordinates, then the actual projection `R^T V` has a joint density satisfying

`||p_{R^T V}||inf <= exp(r/2)`.                                    (1.4)

This is a density estimate for an analyzed projection. It does **not** assert that projected coordinates are independent.

Finally, the exact arbitrary-law/product-set compiler used below is the previous B13 result:

- `yspennstate/math-open-problems@4be4c9842b3828e8a862e58d7e6eec894a85317c`
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B13/20260923T102930Z-fleet01-B13-qform-auto20/REPORT.md`.

Every cap-one scalar probability density is an exact barycenter of indicators of arbitrary measurable sets of Lebesgue measure one; tensoring gives an exact mixture identity for every nonnegative measurable product kernel. No attained optimizer, single interval, centered uniform, bounded diameter, or bounded fragment count is used.

The live corrections remain binding: no law-uniform pointwise quadratic oscillatory decay, no independence after rotation, no arbitrary-joint quadratic coarea theorem, no worst-fiber supremum, no positive moment of a worst conditional projection cap, no bounded-diameter localization, no fixed fragment count, and no perturbative deletion of a small matrix on arbitrary unbounded product supports.

## 2. Dual rectangular theorem: null finite bank, arbitrary curved large bank

### Theorem 2.1 — `QFORM-DUAL-RECTANGULAR-NULLBANK-AGGREGATE-v1`

Let `r>=2` and `m>=r`. Let

`U=(U_1,...,U_r) in R^r`, `V=(V_1,...,V_m) in R^m`

be disjoint original-coordinate banks whose scalar coordinates, together with arbitrary remaining coordinates `Z`, are mutually independent and have probability densities bounded by one. Let `B` be an `r x m` real matrix of full row rank. Suppose

`Q = G(V,Z) + (2 B V+c(Z))^T U`,                                  (2.1)

where `G` and `c` are arbitrary measurable functions for which the displayed random variable is defined. Then `Q` has a continuous density and

`boxed:
 ||p_Q||inf <= K_r^dual det(BB^T)^(-1/(2r)),
 K_r^dual = [r/(r-1)] sqrt(e/2) omega_r^(1/r)
          = sqrt(e) K_r.
`                                                                    (2.2)

In particular,

`K_2^dual=sqrt(2 pi e)=4.1327313541...`.                           (2.3)

The point is that **`G(V,Z)` is completely arbitrary**. It may contain every quadratic coefficient inside the `V` bank, all `V-Z` couplings, arbitrary outside curvature, and arbitrary conditioned translations. Thus no nullity or smallness is required on the large `V` bank.

### Proof

Fix `V=v` and `Z=z`. As a function of the still-random original coordinates `U`, the variable is the scalar linear form

`a(v,z)^T U + G(v,z)`,
`a(v,z)=2Bv+c(z)`.                                                  (2.4)

By the sharp one-dimensional Rogozin/Ball consequence (1.2), for `a(v,z)!=0`,

`||p_{Q|V=v,Z=z}||inf <= sqrt(2)/||2Bv+c(z)||_2`.                  (2.5)

The difficulty is therefore to average one reciprocal Euclidean distance in the coefficient vector **without** conditioning a spectral projection and without deleting the curved term `G`.

Set

`L=(BB^T)^(1/2)`,
`R=B^T L^(-1)`.                                                    (2.6)

Since `B` has full row rank,

`R^T R = L^(-1) B B^T L^(-1)=I_r`,                               (2.7)

and

`B = L R^T`.                                                       (2.8)

By (1.4), the actual random projection

`W=R^T V in R^r`                                                   (2.9)

has a probability density with

`||p_W||inf <= e^(r/2)`.                                           (2.10)

No independence among the coordinates of `W` is claimed or needed. Under the invertible affine map

`Y=2 L W+c(z)=2BV+c(z)`,                                           (2.11)

the density of `Y`, for every fixed `z`, has mass one and satisfies

`||p_{Y|Z=z}||inf
 <= e^(r/2) / [2^r det L]
 = e^(r/2) / [2^r sqrt(det(BB^T))]
 =: M.`                                                            (2.12)

Apply the reciprocal-distance lemma (1.3) at the origin:

`E_V ||2BV+c(z)||_2^(-1)
 <= [r/(r-1)] omega_r^(1/r) M^(1/r)`
` = [r/(2(r-1))] sqrt(e) omega_r^(1/r)
     det(BB^T)^(-1/(2r)).`                                        (2.13)

Average (2.5) in `V` and then `Z`. Equations (2.5) and (2.13) give

`P(Q in J)
 <= [r/(r-1)] sqrt(e/2) omega_r^(1/r)
    det(BB^T)^(-1/(2r)) |J|`                                      (2.14)

for every interval `J`, proving absolute continuity and (2.2).

For continuity, for fixed `z` the coefficient vector `Y=2BV+c(z)` has an absolutely continuous `R^r` law by (2.12). The set of coefficient vectors with at most one nonzero coordinate is a finite union of proper linear coordinate subspaces and therefore has Lebesgue measure zero because `r>=2`. Hence for almost every `v`, at least two coefficients in `a(v,z)` are nonzero. The corresponding conditional law in (2.4) is a convolution of at least two scaled `L^1` densities, hence has a continuous density in the output variable; convolution with any remaining `U` factors preserves continuity. The conditional densities are dominated by the integrable majorant on the right of (2.5), whose `V` integral is uniformly bounded in `z` by (2.13). Dominated convergence in `(V,Z)` gives a continuous averaged density. `QED`.

### Why this does not violate the projection corrections

The proof never conditions on `W=R^T V`, never assigns its coordinates independence, and never uses a density cap for `W` as if it controlled an arbitrary dependent indefinite quadratic pushforward. The projected density cap is used only to integrate the positive kernel `||2LW+c||^-1`; the actual quadratic leaf curvature stays inside `G(V,Z)` and disappears only as an **additive scalar shift after conditioning on the genuine original coordinates `(V,Z)`**. This is exactly the dependence-safe place where projection density information is sufficient.

## 3. Original-matrix form: arbitrary leaf curvature is paid by an exact-null hub bank

### Corollary 3.1 — `QFORM-ORIGINAL-DUAL-RECTANGULAR-NULLBANK-v1`

Let `A` be any real symmetric matrix. Let `P,T` be disjoint original-coordinate sets with

`|P|=r>=2`, `|T|=m>=r`,
`A[P,P]=0`,                                                        (3.1)

and suppose

`B=A[P,T]`                                                         (3.2)

has full row rank. Then for arbitrary independent original-coordinate inputs with scalar density caps one,

`boxed:
 ||p_{X^T A X}||inf
 <= K_r^dual det(A[P,T]A[P,T]^T)^(-1/(2r)).
`                                                                    (3.3)

Moreover the density is continuous.

#### Proof

Let `U=X_P`, `V=X_T`, and condition on all original coordinates `Z` outside `P union T`. Because the principal `P` block is exactly zero, there is no `U^T H U` term. Every cross term from `P` to conditioned coordinates is linear in `U` and becomes `c(Z)^T U`. The cross term between `P` and `T` is exactly `2U^T B V`. Every coefficient internal to `T`, every `T-Z` coupling, and all curvature outside `P` go into `G(V,Z)`. Thus the conditioned expression has exactly the form (2.1), and Theorem 2.1 applies. `QED`.

The corollary is genuinely complementary to the newest designated-partner theorem: partner r25 assumes `A[T,T]=0` and allows arbitrary `A[P,P]`; Corollary 3.1 assumes `A[P,P]=0` and allows arbitrary `A[T,T]`.

## 4. Two-hub aggregate currency and the actual partner application

Take `r=2`, `P={h_1,h_2}`. Put

`B=A[P,T]`.

Cauchy--Binet gives the exact aggregate identity

`det(BB^T)
 = e_2(B^T B)
 = sum_{S subset T, |S|=2} det B[:,S]^2.`                        (4.1)

Hence the new dual theorem says that if the **two hubs themselves are an exact-null physical pair**,

`A[P,P]=0`,                                                       (4.2)

then **regardless of all same-bank leaf curvature `A[T,T]`**,

`boxed:
 ||p_Q||inf <= sqrt(2 pi e) e_2(B^T B)^(-1/4).
`                                                                    (4.3)

For an actual slab ratio

`rho=P(Q in J)/|J|`,                                               (4.4)

this forces

`boxed:
 e_2(B^T B)
 <= (sqrt(2 pi e)/rho)^4
 = 4 pi^2 e^2 rho^(-4).
`                                                                    (4.5)

Now apply the designated `fleet02/B13` theorem (1.1) to the **same actual two-hub cross bank** when the opposite side is null. If instead

`A[T,T]=0`,                                                        (4.6)

the partner theorem gives the stronger

`rho <= sqrt(2pi) e_2(B^T B)^(-1/4)`,                             (4.7)

hence

`e_2(B^T B) <=4pi^2 rho^(-4)`.                                    (4.8)

Combining (4.5) and (4.8) proves the two-sided null-bank certificate

### Corollary 4.1 — `QFORM-TWOHUB-EITHER-SIDE-NULL-v1`

For every disjoint two-hub set `P` and leaf bank `T`, if `B=A[P,T]` has row rank two and **either**

`A[P,P]=0`  or  `A[T,T]=0`,                                      (4.9)

then

`boxed:
 ||p_Q||inf <= sqrt(2 pi e) e_2(B^T B)^(-1/4).
`                                                                    (4.10)

Consequently every slab witness of ratio `rho` in this chamber satisfies

`boxed:
 e_2(B^T B) <=4pi^2 e^2 rho^(-4)
             =291.7082423756... rho^(-4).
`                                                                    (4.11)

This is an actual equation-level use of the designated partner result: (4.7)--(4.8) are its bound on the null-leaf side, while the new theorem supplies the previously unpaid curved-leaf/null-hub side.

The earlier partner gap `QFORM-TWOHUB-LEAFCURVATURE-GLUE-v1` is therefore strictly narrowed. **Arbitrary leaf curvature is no longer an obstruction when the two-hub principal block is null.** A high-density survivor with substantial aggregate two-hub cross area must now have nonzero same-side curvature on both sides of the cross bank.

For a two-coordinate hub block, `A[P,P]!=0` has the elementary exhaustive split:

1. at least one physical hub diagonal is nonzero, giving a genuine original-coordinate scalar-pivot interface; or
2. both hub diagonals vanish and the hub edge is nonzero, so `A[P,P]=[[0,c],[c,0]]` is an invertible indefinite physical pair.

Thus after Corollary 4.1 the remaining glue problem is no longer “arbitrary curved leaves” in isolation. It is specifically to propagate the aggregate `e_2(B^T B)` currency through a **nonzero scalar or physical-pair pivot** without using a false worst conditional-density cap or perturbatively deleting the opposite bank curvature.

## 5. Extremal-product/geometric transfer

For arbitrary measurable sets `E_i subset R` with `|E_i|=1`, their indicators are cap-one probability densities. Therefore Corollary 3.1 gives directly

`boxed:
 |{x in product_i E_i : x^T A x in J}|
 <= K_r^dual det(A[P,T]A[P,T]^T)^(-1/(2r)) |J|
`                                                                    (5.1)

under `A[P,P]=0` and the full-row-rank cross hypothesis. In the two-hub case this is

`|{x in product_i E_i : x^T A x in J}|
 <= sqrt(2pi e) e_2(B^T B)^(-1/4)|J|`.                            (5.2)

Conversely, the exact barycentric product purification from the previous B13 report says that any geometric inequality of this form, proved uniformly for arbitrary unit-measure product indicators, transfers with zero constant loss to every arbitrary cap-one product law. The transfer is an exact mixture identity for the nonnegative slab indicator kernel. No extremizer is assumed to exist, and no component is required to be an interval, centered, bounded in diameter, or bounded in fragment count.

## 6. What remains open

This report proves a supporting branch, not the full theorem. The sharpened first unpaid implication is

`QFORM-BOTH-SIDES-NONNULL-TWOHUB-CURVATURE-GLUE-v1`:

> In the high-density/no-pivot twohub/trihub survivor, after the higher exterior-volume exits and after the two-sided exact-null certificate above, assume substantial aggregate twohub cross currency `e_2(B^T B)` remains and both same-side blocks are genuinely nonzero. Use the resulting genuine scalar pivot or zero-diagonal indefinite pair on the hub side to transport that aggregate currency through the Schur remainder and force an already-paid scalar-square, physical-pair, `E_2/E_3`, grouped-bank, bordered-volume, or diffuse-window certificate, without deleting the curved leaf block perturbatively and without losing original-coordinate product provenance.

A useful exact identity for the scalar-pivot subcase is already visible. If the two rows of `B` are `b_1,b_2` and the first hub has scalar pivot `a!=0`, then after scalar Schur elimination the second hub-to-leaf row is

`w=b_2-(A_{12}/a)b_1`.

Since subtracting a multiple of `b_1` does not alter the transverse component,

`e_2(B^T B)
 = ||b_1||_2^2 ||P_{b_1^perp}b_2||_2^2
 = ||b_1||_2^2 ||P_{b_1^perp}w||_2^2
 <= ||b_1||_2^2 ||w||_2^2.`                                      (6.1)

So aggregate two-hub area cannot disappear completely under a scalar pivot: it reappears as a quantitative transverse one-row coupling unless the first coupling row is itself very large. Turning (6.1) into a product-preserving density payment in the presence of arbitrary leaf curvature is the next concrete step; the known “one heavy row absorbs arbitrary same-bank curvature” shortcut is false and is not used here.

**Independent end-to-end review:** not yet performed for this new theorem.  
**Full QFORM:** OPEN / NOT PROVED / NOT DISPROVED.  
**Full continuity conclusion:** OPEN, although continuity is proved in Theorem 2.1/Corollary 3.1.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository transport is not native learned-memory ingestion.
