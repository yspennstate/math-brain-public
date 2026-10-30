SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B13, 2026-09-23T10:22:44Z.
attacking: scalar-pivot trihub closure and a product-preserving escape from the no-pivot low-cross-rank obstruction.

# fleet02/B13 — rectangular null-bank aggregation before reciprocal payment

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: `Extremal product laws`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING/TARGET-LEVEL NULL-BANK THEOREM / FULL QFORM OPEN / FULL CONTINUITY OPEN**

## 1. Exact target and first unpaid implication

The target remains: for every finite `n`, every independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove

`P(X^T A X in J) <= C |J|`

for one universal finite `C`, every interval `J`, or give a valid counterexample. No moment, support, connectedness, log-concavity, identical-law, diagonal-basis, or post-rotation-independence assumption is allowed. Continuity is separate.

The previous fleet02/B13 run left the high-density/no-pivot survivor simultaneously low in every disjoint exterior order `r>=5` and concentrated, when order-two scalar-Schur currency is not analytically paid, on a finite physical twohub/trihub packet. Its first unpaid implication was `QFORM-TWOHUB-LOW-HIGHER-EXTERIOR-CLOSURE-v1`.

A newer designated-partner result, fleet03/B13 r23, paid the **square** exact-null-bank endpoint using one invertible `r x r` cross block. This run attacks the remaining fragmentation issue on the null side: a two-hub packet can couple to a large leaf bank through many small minors even when no single selected square minor is quantitatively good.

The new theorem below pays the whole rectangular leaf bank by its aggregate Gram determinant before any reciprocal is taken. In the two-hub case this determinant is exactly the sum of squares of **all** `2x2` hub-to-leaf minors.

## 2. Source-valid premises actually used

### 2.1 Designated partner fleet03/B13

Source:

`yspennstate/math-open-problems@57d2f3bcf9a2dec39c1761aafff0f3f7f1732c59`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B13/20260923T093454Z-fleet03-B13-qform-r23/REPORT.md`.

It proves the square exact-null-bank theorem: for `r>=2`, independent original-coordinate cap-one `U,V in R^r`, invertible `B`, remaining independent coordinates `Z`, and

`Q=F(U,Z)+2 U^T B V+c(Z)^T V`,

one has a continuous density with

`||p_Q||_inf <= [r^(3/2)/(2(r-1))] omega_r^(1/r) |det B|^(-1/r)`.

Its key reciprocal-distance lemma is: if an `R^r` probability density is bounded by `M`, then for `r>=2`

`sup_z E |W-z|^(-1) <= [r/(r-1)] omega_r^(1/r) M^(1/r)`.         (2.1)

This run keeps that mechanism but replaces the square `V` bank by an arbitrary-width original-coordinate bank and uses a source-valid dimension-free linear-form density bound on that bank.

### 2.2 Required pinned Claude/Fourier package

Source:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

The package repeatedly uses the sharp Rogozin/Ball bounded-density convolution/section principle. The weighted one-dimensional consequence used below is

`||p_{sum_j a_j V_j}||_inf <= sqrt(2) / ||a||_2`                 (2.2)

for independent scalar `V_j` with density at most one. Indeed, after scaling, `a_j V_j` has density cap `|a_j|^-1`; Rogozin reduces the concentration bound to interval uniforms with the same caps, and Ball's cube-slicing theorem gives the displayed `sqrt(2)/||a||_2` bound. Zero coefficients are omitted.

The same pinned package proves the no-marginal fifth-volume bound: for any disjoint original-coordinate cross block `M=A[I,J]`,

`||p_Q||_inf <= 5 sqrt(2e) e_5(M^T M)^(-1/10)`.                 (2.3)

All same-bank curvature, outside couplings, and affine terms are retained.

### 2.3 No-attainment product purification

Source:

`yspennstate/math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B13/20260922T231352Z-fleet04-B13-rough-geometric-transfer-r5/REPORT.md`.

For every bounded measurable product kernel, its supremum over cap-one product densities equals the supremum over product indicators of bounded finite unions of intervals of measure one. The proof uses `L^1` approximation and finite convex mixtures through a finite hypersimplex; no attained threshold optimizer, single interval, bounded diameter, or uniform fragment count is asserted.

The preceding fleet02/B13 r24 finite-family purification at

`yspennstate/math-open-problems@cc40e95933db0262eddb6e679211145a84dca081`

allows a finite battery of bounded slab/test kernels to be transferred simultaneously to one common bounded-finite-union product-indicator law. This run only needs the one-slab version for the theorem itself, but the finite-family version remains available for gluing it to structural alternatives.

## 3. Rectangular affine-bilinear null-bank theorem

### Theorem 3.1 — `QFORM-RECTANGULAR-NULLBANK-AGGREGATE-v1`

Let `r>=2` and `m>=r`. Let

`U=(U_1,...,U_r) in R^r`,  `V=(V_1,...,V_m) in R^m`

be disjoint original-coordinate banks, all scalar coordinates independent and having probability densities bounded by one. Let `Z` denote any remaining independent coordinates. Let `B` be a real `r x m` matrix of full row rank. Consider

`Q = F(U,Z) + 2 U^T B V + c(Z)^T V`,                              (3.1)

where `F` and `c` are arbitrary measurable functions for which the displayed random variable is defined. Then `Q` has a continuous probability density and

`boxed:
 ||p_Q||_inf <= K_r det(B B^T)^(-1/(2r)),
 K_r = [r/(sqrt(2)(r-1))] omega_r^(1/r).
`                                                                    (3.2)

For `r=2`,

`K_2=sqrt(2 pi)=2.506628274631...`;                              (3.3)

for `r=3`, `K_3=1.709775662855...`.

The constant is independent of the width `m` of the null bank.

### Proof

Fix `Z=z` and `U=u`. The entire random dependence on `V` is the linear form

`a(u,z) dot V`,  `a(u,z)=2 B^T u+c(z)`.                           (3.4)

By (2.2), whenever `a(u,z)!=0`,

`||p_{Q|U=u,Z=z}||_inf <= sqrt(2)/||2B^T u+c(z)||_2`.             (3.5)

Decompose `c(z)` orthogonally as

`c(z)=c_parallel(z)+c_perp(z)`,

where `c_parallel(z)` lies in `range(B^T)` and `c_perp(z)` is orthogonal to `range(B^T)`. Since `B` has full row rank, `B^T:R^r->R^m` is injective, so there is a unique `u_0(z)` with

`c_parallel(z)=-2B^T u_0(z)`.                                    (3.6)

Orthogonality gives the exact Pythagorean identity

`||2B^T u+c(z)||_2^2
 =4||B^T(u-u_0(z))||_2^2+||c_perp(z)||_2^2`,                     (3.7)

hence

`||p_{Q|U=u,Z=z}||_inf
 <= (1/sqrt(2)) ||B^T(u-u_0(z))||_2^(-1)`.                       (3.8)

Put

`L=(BB^T)^(1/2)`.                                                (3.9)

Because

`||B^T x||_2^2=x^TBB^Tx=||Lx||_2^2`,                             (3.10)

we may rewrite the right side of (3.8) as `(1/sqrt(2))|L(u-u_0)|^-1`.

The joint density of `U` is the product of its scalar densities, hence has mass one and is bounded by one. Under the invertible affine map

`w=L(u-u_0(z))`,                                                  (3.11)

the density of `w` has mass one and is bounded by

`M=|det L|^-1=det(BB^T)^(-1/2)`.                                 (3.12)

Apply the reciprocal-distance lemma (2.1): uniformly in `z`,

`E_U ||B^T(U-u_0(z))||_2^(-1)
 <= [r/(r-1)] omega_r^(1/r) det(BB^T)^(-1/(2r)).`                 (3.13)

Average (3.8) first in `U`, then in `Z`, to obtain (3.2). Equivalently, for every interval `J`,

`P(Q in J)
 <= K_r det(BB^T)^(-1/(2r)) |J|`.                               (3.14)

This proves absolute continuity and the essential density bound.

For continuity, fix `z`. The set of `u` for which the vector `a(u,z)` has at most one nonzero coordinate is a finite union of proper affine subspaces of `R^r`: otherwise the `r`-dimensional range of `B^T` would lie in a coordinate axis, contradicting `r>=2` and full row rank. Thus for almost every `u`, at least two coefficients in the linear form (3.4) are nonzero. The sum of the corresponding two scaled `L^1` densities is a convolution of two `L^1` functions and therefore has a continuous density; convolution with the remaining independent factors preserves continuity. The pointwise conditional densities are dominated by the integrable majorant (3.8), whose `U` integral is uniformly bounded in `z` by (3.13). Dominated convergence in `(U,Z)` therefore yields a continuous averaged density `p_Q(t)`. QED.

## 4. Original-matrix form and the aggregate two-minor currency

### Corollary 4.1 — `QFORM-ORIGINAL-RECTANGULAR-NULLBANK-v1`

Let `A` be any real symmetric matrix. Let `P,T` be disjoint sets of original coordinates with

`|P|=r>=2`, `|T|=m>=r`, `A[T,T]=0`,                              (4.1)

and suppose the rectangular physical cross block

`B=A[P,T]`                                                        (4.2)

has full row rank. Then for arbitrary independent cap-one original-coordinate inputs,

`boxed:
 ||p_{X^TAX}||_inf
 <= K_r det(A[P,T] A[P,T]^T)^(-1/(2r)),
`                                                                    (4.3)

and the density is continuous.

#### Proof

Condition on every original coordinate outside `P union T`. The same-side curvature on `P`, all outside curvature/couplings, and every affine leakage are absorbed into `F(U,Z)` and `c(Z)`. The hypothesis `A[T,T]=0` is exactly the null-bank condition, while the cross term is `2U^T A[P,T]V`. Apply Theorem 3.1. No random-coordinate rotation occurs. QED.

### Corollary 4.2 — exact two-hub aggregation

For `|P|=2`, Cauchy-Binet gives

`det(BB^T)
 = sum_{S subset T, |S|=2} det B[:,S]^2
 = e_2(B^T B).`                                                  (4.4)

Therefore an exact-null leaf bank attached to two physical hub coordinates satisfies

`boxed:
 ||p_Q||_inf
 <= sqrt(2pi) e_2(B^T B)^(-1/4).
`                                                                    (4.5)

This is the key new point: **all** hub-to-leaf `2x2` minors are summed before the reciprocal fourth root. The theorem does not select one good minor and incurs no factor depending on the number of leaves.

For a slab witness of ratio

`R_0=P(Q in J)/|J|`,                                              (4.6)

(4.5) forces

`boxed:
 e_2(B^T B) <= (sqrt(2pi)/R_0)^4
             = 4 pi^2 R_0^(-4).
`                                                                    (4.7)

Thus a high-density witness cannot hide substantial exact-null two-hub curvature by fragmenting it among many small physical minors.

## 5. Extremal-product/geometric transfer, with no global optimizer

For unit-measure product-indicator inputs, (3.14) is the geometric sublevel-set inequality

`|{x in product_i E_i : Q(x) in J}|
 <= K_r det(BB^T)^(-1/(2r)) |J|`,                                (5.1)

for arbitrary measurable unit sets, hence in particular for bounded finite unions of intervals.

Apply the fleet04/B13 no-attainment purification to the bounded kernel `1_{Q in J}`. Approximate each cap-one marginal in `L^1` by finite convex mixtures of bounded finite-union unit indicators, expand the finite product mixtures, and use the telescoping product `L^1` bound. Every mixture component obeys (5.1), so after averaging and passing to the limit the same constant holds for the original arbitrary product law.

No threshold optimizer is assumed to exist. No centered interval, single interval, bounded support diameter, or uniform fragment count enters. Arbitrarily separated fragments and unbounded original supports remain admissible.

The direct proof in Section 3 already gives the arbitrary-law bound independently; this purification argument establishes the exact geometric-to-product interface required by this slot.

## 6. Application to the current twohub/no-pivot survivor

The preceding fleet02/B13 r24 result showed that a hypothetical high-density/no-pivot witness must have very small higher disjoint exterior volume, while the designated-partner scalar-Schur compiler concentrates any unpaid order-two currency on a finite physical twohub/trihub packet.

The new theorem removes one concrete escape in that packet. Suppose, after conditioning the finite physical hub variables and every unused original coordinate, a surviving leaf bank `T` has **exact** same-bank nullity `A[T,T]=0`. If two unconditioned physical hub-side coordinates `P={h_1,h_2}` retain aggregate cross two-volume

`E_2=e_2(A[P,T]^T A[P,T])>0`,                                   (6.1)

then the branch is paid by

`||p_Q||_inf <= sqrt(2pi) E_2^(-1/4)`.                           (6.2)

Consequently a slab witness of ratio `R_0` in this exact-null twohub chamber must have

`E_2 <= 4pi^2 R_0^(-4)`.                                        (6.3)

The same conclusion survives arbitrary within-`P` curvature, arbitrary outside curvature/couplings, arbitrary conditioned translations, and arbitrary fragmentation of every input law.

This genuinely extends the partner's square-null-bank theorem: even if every particular `2x2` hub-to-leaf minor is tiny, their full squared sum is paid before inversion.

## 7. Required Claude D5 result applied to the same obstruction

The pinned D5 theorem (2.3) supplies an independent global obstruction. If a slab witness has ratio `R_0`, then for **every** disjoint original-coordinate cross block `M=A[I,J]`,

`boxed:
 e_5(M^T M)
 <= (5 sqrt(2e)/R_0)^10.
`                                                                    (7.1)

Thus any hypothetical diverging counterexample sequence in the exact-null/twohub region must simultaneously satisfy two different matrix constraints:

- every physical cut has vanishing fifth cross-volume at the quantitative rate (7.1);
- every exact-null leaf bank attached to a two-hub packet has vanishing aggregate second cross-volume at the quantitative rate (6.3).

This is a real use of the required Claude result: it isolates the surviving geometry between order two and order five. Large rank-five transverse currency is already paid; large exact-null two-hub order-two currency is now also paid **without** one-minor selection.

No counterexample was found by the pinned source search, but its numerics are not used as proof.

## 8. What is still unpaid

The full QFORM conjecture remains OPEN / NOT PROVED / NOT DISPROVED. The theorem above is exact in the null-bank hypothesis and does **not** permit replacing a small nonzero `A[T,T]` by zero: arbitrarily translated and fragmented cap-one supports make raw coefficient perturbation unsafe.

The first unpaid implication is now sharpened to

`QFORM-TWOHUB-LEAFCURVATURE-GLUE-v1`:

> In the current high-density/no-pivot twohub/trihub survivor, after excluding every substantial high-order disjoint exterior volume and paying every exact-null two-hub leaf bank by the aggregate theorem above, use genuinely nonzero same-bank leaf curvature itself to force an already-paid scalar-square, physical-pair, E2/E3 entropy, grouped-bank, bordered-volume, or Fresnel certificate — without deleting that curvature perturbatively and without losing original-coordinate product provenance — or construct a genuine bounded-finite-union product-indicator counterexample.

Equivalently, the remaining obstruction is no longer “many tiny null-bank minors.” It is a true interaction between nonzero leaf-leaf curvature and the finite hub packet.

Full continuity remains separately OPEN, although continuity is proved in the rectangular exact-null-bank branch.

## 9. Review status

The new theorem and its corollaries are analytic derivations in this run and have **not** received an independent end-to-end review. No Monte Carlo or benchmark evidence is used. No task, notification, email, permission, workflow, public-release, or account-binding state is changed by this mathematical report.
