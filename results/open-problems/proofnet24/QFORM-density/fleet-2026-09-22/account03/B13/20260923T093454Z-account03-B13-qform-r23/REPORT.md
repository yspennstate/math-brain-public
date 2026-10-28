SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B13, 2026-09-23T09:34:54Z.
attacking: extremal-product concentration around the remaining trihub/global-third-curvature obstruction via a robust product-set slab inequality.

# account03/B13 20260923T093454Z — affine-bilinear null-bank theorem and continuous-density endpoint

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Extremal product laws  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW TARGET-RELEVANT THEOREM PROVED / FULL QFORM OPEN / FULL CONTINUITY OPEN**


Designated completed partner actually applied below: account04/B13 no-attainment product purification, `yspennstate/math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260922T231352Z-account04-B13-rough-geometric-transfer-r5/REPORT.md`.

## 1. The first missing endpoint attacked

The current B13 obstruction is concentrated physical hub geometry with a genuine third-curvature resource. A recurring exact endpoint is that, after conditioning the hub coordinates, one original-coordinate bank has **zero same-bank quadratic curvature**, while a nondegenerate physical cross block survives into that bank. This endpoint must be paid without rotating the random vector and without perturbing a nearly-zero block to zero.

This run proves the exact zero-bank case with a dimension-free linear slab bound, and in fact proves continuity of the output density in that branch. The near-zero case remains open because arbitrary fragmented/unbounded product supports forbid coefficient-deletion arguments.

## 2. Linear forms in an original product bank

Let `V=(V_1,...,V_r)` have independent one-dimensional probability densities bounded by one, and let `a in R^r`, `a!=0`. Conditioning on all `V_j` except a coordinate `j` for which `|a_j|=||a||_infty` gives

`||p_{a dot V}||_infty <= 1/||a||_infty <= sqrt(r)/||a||_2`.      (2.1)

For almost every `a` with at least two nonzero coordinates, the density can be chosen continuous: the sum of two nontrivial scaled `L^1` densities is a convolution of two `L^1` functions, hence is continuous and vanishes at infinity; convolution with the remaining independent factors preserves continuity. The same sup bound (2.1) holds for that continuous version.

## 3. Reciprocal-distance lemma with exact constant

Let `Z` be any `R^r` random vector having density `g` with `0<=g<=M`, `int g=1`, and let `r>=2`. Then for every center `z_0`,

`E |Z-z_0|^{-1} <= [r/(r-1)] omega_r^(1/r) M^(1/r)`,             (3.1)

where `omega_r=pi^(r/2)/Gamma(r/2+1)` is the volume of the Euclidean unit ball.

Proof. By layer cake,

`E |Z-z_0|^{-1} = int_0^infty P(|Z-z_0|<1/t) dt`.

The probability is at most `min(1, M omega_r t^{-r})`. Put `t_0=(M omega_r)^(1/r)`. Then

`int_0^t0 1 dt + int_t0^infty M omega_r t^{-r} dt`
` = t0 + t0/(r-1)`
` = [r/(r-1)] omega_r^(1/r) M^(1/r)`. QED.

The integral diverges at `r=1`, matching the logarithmic rank-one affine-bilinear obstruction.

## 4. Main theorem — `QFORM-AFFINE-BILINEAR-NULLBANK-LINF-CONT-v1`

Let `r>=2`. Let

`U=(U_1,...,U_r)`, `V=(V_1,...,V_r)`

be disjoint groups of independent original-coordinate random variables, each scalar marginal having density at most one. Let `Z` denote any remaining independent coordinates. Let `B` be a real invertible `r x r` matrix. Consider

`Q = F(U,Z) + 2 U^T B V + c(Z)^T V`,                              (4.1)

where `F` and `c` are arbitrary measurable functions for which the displayed random variable is defined. Then `Q` has a **continuous probability density** and

`boxed: ||p_Q||_infty <= C_r |det B|^(-1/r),`                    (4.2)

where

`C_r = [r^(3/2)/(2(r-1))] omega_r^(1/r)`.                        (4.3)

In particular

`C_2 = sqrt(2 pi) = 2.5066282746310007...`,
`C_3 = (3 sqrt(3)/4)(4 pi/3)^(1/3) = 2.094038974311569...`.      (4.4)

### Proof

Fix `Z=z` and `U=u`. The conditional random part depending on `V` is the linear form

`a(u,z) dot V`,  `a(u,z)=2 B^T u+c(z)`.

By (2.1), for almost every `u`,

`||p_{Q|U=u,Z=z}||_infty`
` <= sqrt(r)/||2B^T u+c(z)||_2`
` = [sqrt(r)/2] |B^T(u-u_0(z))|^{-1}`,                           (4.5)

where `u_0(z)` is uniquely determined by `2B^T u_0+c(z)=0`.

The joint density of `U` is the product of its scalar densities, hence is bounded by one and has mass one. Under the affine map

`w=B^T(u-u_0(z))`,

the density of `w` has mass one and is bounded by `M=|det B|^{-1}`. Applying (3.1) yields, uniformly in `z`,

`E_U |B^T(U-u_0(z))|^{-1}`
` <= [r/(r-1)] omega_r^(1/r) |det B|^(-1/r).`                   (4.6)

Averaging (4.5) in `U` and `Z` proves (4.2). Equivalently, for every interval `J`,

`P(Q in J) <= C_r |det B|^(-1/r) |J|`.                          (4.7)

This interval inequality implies absolute continuity and the same essential density bound.

For continuity, for fixed `z` and for almost every `u`, at least two coordinates of `a(u,z)` are nonzero: the exceptional set is a finite union of affine subspaces of positive codimension because `B` is invertible and `r>=2`. For such `u`, the conditional linear-form density is continuous by convolution of two nontrivial scaled `L^1` densities. Its pointwise absolute value is dominated by the integrable right side of (4.5). Dominated convergence in `u`, and then in `z` using the uniform bound supplied by (4.6), shows that the averaged density `p_Q(t)` is continuous in `t`. QED.

## 5. Original-matrix corollary — `QFORM-ORIGINAL-NULLBANK-DETERMINANT-v1`

Let `A` be any real symmetric matrix and let `P,T` be disjoint sets of original coordinates with

`|P|=|T|=r>=2`,  `A[T,T]=0`,  `det A[P,T] !=0`.                  (5.1)

For arbitrary independent cap-one original-coordinate inputs, condition on every coordinate outside `P union T`. The conditional quadratic polynomial has the form (4.1) with

`B=A[P,T]`;

all same-side curvature on `P`, all outside curvature/couplings, and all affine leakage are absorbed into `F` and `c`, while the hypothesis `A[T,T]=0` is exactly the null-bank condition. Therefore

`boxed: ||p_{X^T A X}||_infty <= C_r |det A[P,T]|^(-1/r),`      (5.2)

and the density is continuous.

For a physical `2x2` cross block this is

`||p_Q||_infty <= sqrt(2pi) |det A[P,T]|^(-1/2)`.                (5.3)

This is **not** a cross-minor-alone theorem: the exact nullity of the selected same-side principal block is essential. Thus it does not conflict with `QFORM-CROSSMINOR-ALONE-FALSE`.

## 6. Actual use of account04/B13 extremal-product purification

For unit-measure product-indicator laws, (4.5)-(4.7) are a geometric slab estimate:

`|{(u,v,z) in product E_i : Q(u,v,z) in J}|`
` <= C_r |det B|^(-1/r)|J|`.                                    (6.1)

Account04/B13's completed no-attainment purification writes every cap-one product law as an `L^1` limit of finite convex mixtures of bounded finite-union unit product indicators. Apply that theorem to the bounded kernel `1_{Q in J}` and expand the finite product mixtures. Inequality (6.1) transfers with **zero constant loss** to every admissible cap-one product law. No single interval, centered interval, bounded support diameter, or uniform fragment count is introduced.

The direct Fubini proof in Section 4 independently gives the same arbitrary-law inequality; the partner application establishes the exact extremal-product/geometric interface required by this slot.

## 7. Application to the live concentrated-hub obstruction

The recent B13/account02 structural reductions leave finite physical row/column hub packets and ask how to preserve a genuine third-curvature resource. The theorem above closes the **exact null-bank endpoint** of that obstruction:

- after conditioning any hub coordinates and all unused coordinates, if the surviving bank `T` has `A[T,T]=0` and contains a nonzero physical `2x2` cross minor against two coordinates on the opposite side, the branch is immediately paid by (5.3), with continuity;
- more generally an invertible `r x r` physical cross block against an exact null bank is paid by (5.2).

This is dependence-safe because every conditioning is on original coordinates and the remaining `U_i,V_j` stay independent. No random-coordinate rotation is performed.

The theorem does **not** pay a merely small `A[T,T]`: fragmented and arbitrarily translated supports prevent treating small coefficients as a uniformly small random perturbation. Consequently the first remaining implication for this mechanism is

`QFORM-TRIHUB-NEARNULL-BANK-GLUE-v1`:

> In the finite physical tri-hub survivor, either force an exact/null-bank determinant certificate as above, or use the nonzero same-bank curvature itself—without deleting it—to trigger an already-paid scalar-square, physical-pair, E2/E3 entropy, grouped-bank, or bordered-volume certificate.

## 8. Status

Full QFORM is still **OPEN / NOT PROVED / NOT DISPROVED**. The full continuous-density conclusion is also **OPEN**, although continuity is proved in the affine-bilinear exact-null-bank branch above.

No Monte Carlo evidence is used. No scheduled-task state, notification state, email delivery, public release, workflow, model/API purchase, or Codex action is changed by this run.
