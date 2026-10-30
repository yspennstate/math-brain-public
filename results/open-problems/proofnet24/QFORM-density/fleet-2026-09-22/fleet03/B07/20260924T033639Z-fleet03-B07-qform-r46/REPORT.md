SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B07, 2026-09-24T03:36:39Z.
attacking: the r40 overlap-two rank-one shared-pair star-star packet — derive a product-preserving physical-pair receiver from the kernel star, then turn failure into a new aggregate determinant-weighted residual currency.

# fleet03/B07 r46 — rank-one physical-pair kernel-star receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: coordinate minor selection / GEOMETRY  
Run: `20260924T033639Z-fleet03-B07-qform-r46`  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
Status: **NEW FULL-AMBIENT RANK-ONE-PAIR RECEIVER + NEW OVERLAP-TWO RESIDUAL CURRENCY / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**.

No Gaussian, log-concavity, moment, compact-support, connected-support, iid, diagonal-basis, post-rotation independence, uniform pointwise quadratic-phase decay, arbitrary-joint coarea, or deletion of a small nonzero coefficient is used. The only rotation below is a deterministic two-dimensional change of variables inside an integral; the input density remains the literal product `f_i(x_i)f_j(x_j)`, and no rotated variables are declared independent.

## 1. Fresh source state and exact incoming debt


The main incoming structural source is my r40 positive overlap compiler:

`yspennstate/math-open-problems@c21a61aa6390c0be6ed68027341207e44c1bbb07`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260923T224121Z-fleet03-B07-qform-r40/REPORT.md`.

In its overlap-two branch, for a physical shared pair `K={h1,h2}` with actual principal pair

`B=A[K,K]`,

and disjoint physical banks `I,J`, the rank-one part is exact. If `rank B=1`, let `lambda != 0` be its nonzero eigenvalue and let `v` be a unit vector spanning `ker B`. Define

`L_K^2 = sum_{r in I} (v^T A[K,r])^2`,
`R_K^2 = sum_{c in J} (v^T A[K,c])^2`.

Then the whole singular-pair bordered-minor packet is

`sum_{r,c} det A[K union {r}, K union {c}]^2
 = lambda^2 L_K^2 R_K^2`.                                      (1.1)

The r40 compiler forces, in the rank-one-pair alternative,

`sum_K lambda_K^2 L_K^2 R_K^2 > 1/512`.                         (1.2)

Previously (1.2) was only structural. This run analytically pays every term whose physical kernel star has a definite scale and quantifies what remains if no term pays.

The linear-form density input below is the source-valid Rudelson--Vershynin transfer already proved and applied in fleet03/B18:

`yspennstate/math-open-problems@9c6683c03c8b0dbd635314109854871448343055`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B18/20260923T235531Z-fleet03-B18-QFORM-auto14/REPORT.md`.

For independent cap-one original coordinates and a nonzero coefficient vector `w`, the scalar `w^T Y` has density bounded by `sqrt(2)/||w||_2`.

## 2. A one-dimensional quadratic pullback lemma

### Lemma 2.1 — `QFORM-QUADRATIC-PULLBACK-L1-v1`

Let `f` be any probability density on `R` with `0<=f<=1`, and let

`F(y)=a y^2+b y+c`, `a!=0`.

Then

`boxed: integral_R f(F(y)) dy <= 2/sqrt(|a|).`                    (2.1)

### Proof

Complete the square, `F(y)=a(y-y0)^2+c0`. If `a>0`, setting `r=a(y-y0)^2` on the two branches gives

`integral f(F(y))dy
 = a^(-1/2) integral_0^infinity f(c0+r) r^(-1/2) dr`.

The one-sided function `r -> f(c0+r)` has cap one and total mass at most one. Since `r^(-1/2)` is decreasing, the bathtub bound gives

`integral_0^infinity f(c0+r) r^(-1/2)dr <= integral_0^1 r^(-1/2)dr=2`.

The case `a<0` is identical with `f(c0-r)`. QED.

This lemma is translation-uniform and makes no regularity assumption on `f`.

## 3. Conditional density for one actual rank-one physical pair

Let `K={i,j}` be two literal original coordinates and suppose

`B=A[K,K]=lambda u u^T`,                                         (3.1)

where `u` is a unit vector, `lambda!=0`, and `v` is a unit vector orthogonal to `u`, so `v` spans `ker B`.

Condition on every original coordinate outside `K`. All outside quadratic terms become a scalar shift, and the conditional polynomial in the actual pair `x=(x_i,x_j)` is

`q(x)=lambda (u^T x)^2 + 2 c^T x + C`.                           (3.2)

Write

`y=u^T x`, `z=v^T x`, `s=u^T c`, `t=v^T c`.

The orthogonal change of variables has Jacobian one, but the joint density is still kept explicitly as the physical product

`f_i(u_i y+v_i z) f_j(u_j y+v_j z)`.                             (3.3)

For `t!=0`, a level `q(x)=q0` solves uniquely for

`z(y)=[q0-C-lambda y^2-2 s y]/(2t)`.                             (3.4)

Therefore the conditional density is

`p(q0 | outside)
 = (1/(2|t|)) integral_R
     f_i(u_i y+v_i z(y)) f_j(u_j y+v_j z(y)) dy`.                 (3.5)

Choose `ell in {i,j}` with `|v_ell|>=1/sqrt(2)`. Drop the other density factor using only its cap one. The remaining physical coordinate

`x_ell(y)=u_ell y+v_ell z(y)`                                    (3.6)

is a quadratic whose leading coefficient has magnitude

`|a_ell|=|v_ell lambda|/(2|t|)
 >= |lambda|/(2 sqrt(2)|t|)`.                                    (3.7)

Lemma 2.1 inserted into (3.5) gives

`boxed:
 ||p(. | outside)||_infinity
 <= 2^(3/4) / sqrt(|lambda t|).
}`                                                               (3.8)

No density cap for either rotated coordinate `y` or `z` was used.

## 4. Full ambient theorem: kernel-star smoothing

Define the complete physical kernel-star vector

`w := A[K,K^c]^T v`,
`S := ||w||_2`.                                                   (4.1)

For the target quadratic form, after conditioning on `Y=X_{K^c}` one has exactly

`t=v^T A[K,K^c]Y=w^T Y`.                                         (4.2)

Assume `S>0`. The Rudelson--Vershynin linear-form theorem gives the density cap

`||p_t||_infinity <= sqrt(2)/S`.                                  (4.3)

In particular `P(t=0)=0`, so (3.8) holds almost surely. For any scalar density `h<=H`, the same centered bathtub calculation gives

`integral |r|^(-1/2) h(r) dr <= 2 sqrt(2H)`.                      (4.4)

Using `H=sqrt(2)/S`,

`E |t|^(-1/2) <= 2^(7/4) S^(-1/2)`.                              (4.5)

Averaging the conditional densities (3.8) and using Fubini proves the main result.

### Theorem 4.1 — `QFORM-RANK1-PHYSICAL-PAIR-KERNEL-STAR-v1`

For independent original coordinates with densities at most one, let `A` be any real symmetric matrix. If some actual two-coordinate principal block `B=A[K,K]` has rank one with nonzero eigenvalue `lambda`, unit kernel vector `v`, and

`S=||A[K,K^c]^T v||_2>0`,

then the **full ambient quadratic form**, retaining every outside quadratic coefficient, every coupling, and every additional eigenvalue, has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity <= 4 sqrt(2) / sqrt(|lambda| S).
}`                                                               (4.6)

The proof establishes existence and essential boundedness of a density by an integrably dominated mixture of the conditional densities. **Continuity is not claimed.**

The scaling is exact: under `A -> cA`, both `lambda` and `S` scale by `|c|`, and the right side scales by `|c|^(-1)` as a density bound must.

### Correction compatibility

This does not conflict with the live `QFORM-ONE-HEAVY-ROW-SAME-SQUARE-ABSORPTION-FALSE-v1` or `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1` corrections. Their rank-one two-coordinate counterexamples have **zero external kernel star** `S=0`, precisely where (4.6) makes no assertion. Likewise no affine slope in the same square variable is credited with extra smoothing; the smoothing variable is the genuine kernel-direction coupling to independent original coordinates outside the pair.

## 5. Actual payment of the r40 star-star packet

Return to the rank-one shared pairs in (1.2). For each such `K`, set

`S_K := ||A[K,K^c]^T v_K||_2`.

Because `I,J subset K^c` are disjoint,

`S_K >= max(L_K,R_K)`.                                           (5.1)

Theorem 4.1 pays the full ambient law whenever a single pair has a sufficiently large product `|lambda_K|S_K`.

Choose the fixed scale

`delta=2^(-10)`.                                                  (5.2)

If some rank-one pair satisfies

`|lambda_K| S_K >= delta`,                                       (5.3)

then

`boxed:
 ||p_Q||_infinity <= 4 sqrt(2) delta^(-1/2)
 =128 sqrt(2)
 =181.019335983756... .
}`                                                               (5.4)

Assume now that no pair pays, so `|lambda_K|S_K<delta` for every rank-one pair in the packet. Then each term factors as

`lambda_K^2 L_K^2 R_K^2
 = (|lambda_K|S_K)^2 (L_K R_K/S_K)^2
 < delta^2 (L_K R_K/S_K)^2`.                                    (5.5)

Combining (5.5) with the determinant-weighted aggregate lower bound (1.2) gives a new dimension-free residual currency:

`boxed:
 sum_K (L_K R_K/S_K)^2 > 1/(512 delta^2)=2048.
}`                                                               (5.6)

Thus the old rank-one shared-pair star-star packet is no longer merely
`sum lambda^2 L^2 R^2>1/512`. It now has the exhaustive analytic/structural fork:

1. one actual physical rank-one pair pays the complete ambient density by (5.4); or
2. the normalized balanced kernel-star energy in (5.6) is enormous.

Equation (5.6) keeps the pair-by-pair determinant weight through the analytic conditioning step; no tiny principal minor is inverted.

There is also a slab-ratio form useful for a putative counterexample sequence. If an interval `J0` has

`rho=P{Q in J0}/|J0|`,

then every surviving rank-one pair must satisfy

`boxed: |lambda_K|S_K <= 32/rho^2`.                              (5.7)

Consequently (1.2) forces

`boxed:
 sum_K (L_K R_K/S_K)^2 > rho^4/524288.
}`                                                               (5.8)

So any unbounded-ratio sequence in this overlap-two chamber must develop quartically growing balanced kernel-star energy even though every individual analytic pair scale `|lambda|S` tends to zero.

## 6. Required application of the designated fleet04/B07 result

The designated completed partner is

`yspennstate/math-open-problems@dab16464e87c939cc0cf3fd01d070045290192fa`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B07/20260923T161510Z-fleet04-B07-coordinate-core-r2/REPORT.md`.

Its `r=0` coordinate-core theorem says that an actual physical triple `T` with

`|A_hh|>=1/64` for `h in T`,
`|A_hk|<=1/768` for distinct `h,k in T`,                         (6.1)

satisfies

`s_3(A[T,T])>=1/64-3/768=3/256`,                                 (6.2)

and hence the complete ambient law obeys

`boxed:
 ||p_Q||_infinity <= 2 sqrt(18 pi)/(3/256)
 =1283.393676611072... .
}`                                                               (6.3)

Here is a direct application to the present rank-one pairs. Since

`B_K=lambda_K u_Ku_K^T`,

one of its two actual physical diagonals satisfies

`max_{h in K}|A_hh| >= |lambda_K|/2`.                             (6.4)

Therefore three **pair-disjoint** rank-one packet terms with

`|lambda_K|>=1/32`                                                (6.5)

supply three distinct physical coordinates with diagonal magnitudes at least `1/64`. If their three selected representatives obey the actual mutual edge bounds in (6.1), the partner theorem immediately pays (6.3). Equivalently, in any slab witness with `rho>1283.393676612`, every such three-pair selection must contain a representative mutual edge larger than `1/768`.

Combined with the new pair receiver, a rank-one term with `|lambda_K|>=1/32` that survives (5.3) also has

`S_K<delta/(1/32)=1/32`.                                         (6.6)

Thus the large-`|lambda|` part of the unpaid packet is forced simultaneously toward a tiny kernel star and, when three disjoint terms exist, toward a dense physical endpoint graph. This is an actual quantitative use of the designated partner result, not a generic citation.

Continuity is not claimed on the partner-core exit.

## 7. What remains

The full QFORM conjecture is still **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity is also OPEN.

This run closes every r40 rank-one shared-pair term with `|lambda|S>=2^(-10)` and replaces the remaining aggregate by the stronger normalized currency (5.6), or by the high-ratio version (5.8). The immediate next debt is:

`QFORM-BALANCED-KERNEL-STAR-ENERGY-RECEIVER-v1`:

consume the residual sum `sum (L_K R_K/S_K)^2` without a dimension-dependent max selection. Natural mechanisms are a random physical endpoint cut that converts this normalized energy into a genuine `E3` crossing, or a low-rank/diagonal compiler in which the fleet04/B07 coordinate-core gate can spend the forced dense endpoint graph. Any such step must retain arbitrary outside curvature and the full nonzero coefficient tail.

The r44 rank-six inter-bank carrier, the one-overlap skew-mismatch packet, the invertible-pair overlap-two packet, and the principal fourth-power packet remain distinct debts; none is silently declared paid here.
