SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B13, 2026-09-23T01:35:55Z.
attacking: change mechanism from entropy duality to exterior-algebra hub contraction, then combine the resulting one-row aggregate currency with the completed one-row/E2 smoothing theorem.

# account03/B13 r21 — three-volume contraction gives a universal L3 cross-block theorem

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Extremal product laws  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **PROVED TARGET-RELEVANT SUPPORTING THEOREM / FULL QFORM OPEN / FULL CONTINUITY OPEN**

## 1. Scope and source pins

The exact owner target remains: every finite dimension, independent original-coordinate laws with densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one. No moment, compact-support, connected-support, Gaussian, log-concavity, diagonal-basis, or post-rotation-independence hypothesis is used below.

Fresh control was resolved from `yspennstate/math-research-brain`; the run began from commit `15a04a432b03444e18a3836528f5da5ee23d6f99`, OWNER CONTROL revision `2026-09-22.15`, QFORM-only. The live state still marks full QFORM and full continuity OPEN. The argument does not use the refuted law-uniform pointwise quadratic-phase decay, arbitrary-joint rank-three coarea, positive conditional-projection-density moment, bounded-diameter localization, fixed fragment count, naive fiber-sup integration, or a universally good single physical minor.

Three completed inputs are used at their exact scopes.

1. **Previous B13 entropic three-volume / six-hub dichotomy:** `yspennstate/math-open-problems@5d38cf0af8ff126d75857cd2011f928d6704b690`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260923T003350Z-account03-B13-qform-r20/REPORT.md`. For any original-coordinate cross block `M`, with `Z=e_3(M^T M)>0` and any `L>0`, either a row-capped determinant law pays an `L^infinity` density bound `6 sqrt(e) exp(L/6) Z^(-1/6)`, or at most six original physical rows `H` can be deleted so that the surviving three-volume is `<exp(-L)Z`.

2. **One-row / aggregate-E2 smoothing:** account03/B06, read at `yspennstate/math-open-problems@a9eaf559d5a8301180175f27b21d8625039d379e`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260922T201841Z-account03-B06-qform-r18/REPORT.md`. If an original-coordinate cross block has a selected row of Euclidean norm `r>0`, and `E=e_2(N^T N)>0` for the bank `N` obtained after deleting that row, then, with arbitrary same-side quadratic phases, affine terms and outside conditioning,

`|phi_Q(t)| <= min{1,
 (pi sqrt(e)/(r|t|))^(1/4)
 [1+16 E t^4/(pi^4 e^4)]^(-1/8)}.`                              (1.1)

3. **Designated partner account04/B13 no-attainment purification:** `yspennstate/math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260922T231352Z-account04-B13-rough-geometric-transfer-r5/REPORT.md`. Every cap-one mass-one marginal is an `L1` limit of finite convex combinations of indicators of bounded finite unions of intervals of measure one; products expand into finite mixtures and product `L1` error is controlled by the sum of marginal errors. No optimizer, interval extremality, bounded diameter or uniform fragment count is asserted.

## 2. New exact exterior-algebra identity

Let `M` be a finite real matrix with row set `I` and column set `J`. Put

`Z=e_3(M^T M)=sum_{|S|=|T|=3} det(M_{S,T})^2`.

For a physical row `h in I`, let `a=m_h`, let `N=M_{I\{h},J}`, and, if `a!=0`, let

`P_a=I-a^T a/||a||_2^2`

be the orthogonal projection in the column space onto `a^perp`. Define the three-volume incident to row `h` by

`Z_h=sum_{S contains h, |S|=3, |T|=3} det(M_{S,T})^2`.

### Lemma 2.1 — `QFORM-HUB-WEDGE-CONTRACTION-v1`

For every nonzero row `a`,

`boxed: Z_h=||a||_2^2 e_2((N P_a)^T(N P_a)) <= ||a||_2^2 e_2(N^T N).`   (2.1)

If `a=0`, both sides relevant to `Z_h` are zero.

### Proof

Fix two rows `u,v` of `N`. Cauchy--Binet gives

`sum_{|T|=3} det([a;u;v]_T)^2 = det Gram(a,u,v)`.

Perform Gram--Schmidt only as an algebraic identity, not as a change of random coordinates. Projecting `u,v` orthogonally off `a`,

`det Gram(a,u,v)=||a||_2^2 det Gram(P_a u,P_a v)`.

Summing over all unordered row pairs of `N` and applying Cauchy--Binet at exterior order two proves the equality in (2.1). For the inequality, `P_a` is an orthogonal contraction, hence

`|| wedge^2(N P_a)||_HS <= ||wedge^2 N||_HS`,

and the squared Hilbert--Schmidt norms are exactly the two `e_2` quantities. QED.

This identity is support-free and inverse-free. It converts three-volume attached to one physical row into exactly the one-row-times-aggregate-E2 currency consumed by (1.1), without choosing any one `2x2` or `3x3` minor.

## 3. Six-hub concentration automatically contains one strong E2 row

Suppose the six-hub branch of the previous B13 theorem holds for a cross block `M`: for a set `H`, `|H|<=6`,

`Z_res:=e_3(M_{I\H,J}^T M_{I\H,J}) < e^(-L) Z`.                     (3.1)

The Cauchy--Binet mass `Z-Z_res` is exactly the mass of `3x3` minors whose row triples meet `H`. Every such minor is counted in `Z_h` for at least one `h in H`. Therefore

`sum_{h in H} Z_h >= Z-Z_res > (1-e^(-L))Z`.                        (3.2)

Hence some `h in H` satisfies

`Z_h > ((1-e^(-L))/6) Z`.                                             (3.3)

By Lemma 2.1, writing `r=||m_h||_2` and `E=e_2(N^T N)`,

`boxed: kappa:=r^2 E >= ((1-e^(-L))/6) Z.`                           (3.4)

Notice what has happened: the low residual three-volume is **not deleted as a perturbation**. It is used only to prove that one hub row sees a fixed fraction of the complete three-volume through the aggregate second exterior energy of every other row.

## 4. A scale-balanced L3 bound depending only on `kappa=r^2 E`

Starting from (1.1), use `1+x>=x` to obtain, for all `t!=0`,

`|phi_Q(t)|
 <= min{1, C0 kappa^(-1/8)|t|^(-3/4)},`                              (4.1)

where

`C0=2^(-1/2) pi^(3/4) e^(5/8)=3.1173205167723097...`.

Indeed the factors `r^(-1/4)` and `E^(-1/8)` combine exactly as `(r^2E)^(-1/8)`. This is the scale-balanced point that was not used in the earlier split-at-`E^(-1/4)` estimate.

Put `D=C0 kappa^(-1/8)` and `t0=D^(4/3)`. Then

`int_R |phi_Q(t)|^(3/2) dt
 <=2 t0 + 2D^(3/2) int_{t0}^infinity t^(-9/8)dt
 =18 D^(4/3)`

and therefore

`boxed:
 int_R |phi_Q(t)|^(3/2)dt
 <=18*2^(-2/3) pi e^(5/6) kappa^(-1/6).`                             (4.2)

The same Fourier convention as the B06 source and inverse Hausdorff--Young give an `L3` density with

`boxed:
 ||p_Q||_3
 <= C_E2 kappa^(-1/9),
 C_E2=3^(4/3) 2^(-4/9) e^(5/9)
      =5.541728894337633... .`                                       (4.3)

No continuity is claimed from this `L3` argument.

## 5. Main theorem: any rank-three original-coordinate cross block gives L3

### Theorem 5.1 — `QFORM-CROSS-3VOLUME-L3-v1`

Consider any real quadratic polynomial in independent original coordinates of cap-one one-dimensional densities. Let `I,J` be disjoint original-coordinate sets, and let `M=A[I,J]` be its physical cross block. If

`Z=e_3(M^T M)>0`,

then the output law has a density in `L3(R)` and

`boxed: ||p_Q||_3 < 6.787 Z^(-1/9).`                                 (5.1)

All same-side quadratic blocks, all coordinates outside `I union J`, all outside couplings, all affine terms and all signs are arbitrary.

### Proof

Apply the previous B13 theorem with `L=log 32`.

**Paid entropic branch.** It gives

`||p_Q||_infinity <=6 sqrt(e) 32^(1/6) Z^(-1/6)`.

Because `p_Q` has mass one,

`||p_Q||_3 <= ||p_Q||_infinity^(2/3)
 <= C_paid Z^(-1/9)`,

where

`C_paid=(6 sqrt(e))^(2/3)32^(1/9)
       =6.772846206537608... .`                                      (5.2)

The source also gives a continuous density in this branch.

**Six-hub branch.** Equations (3.4) and (4.3), with

`(1-1/32)/6=31/192`,

give

`||p_Q||_3
 <= C_E2 (192/31)^(1/9) Z^(-1/9)
 =6.786385992671971... Z^(-1/9).`                                    (5.3)

Taking the larger of (5.2) and (5.3) proves (5.1). QED.

Equivalently, every original-coordinate cross block of rank at least three supplies an `L3` output-density theorem, with the natural homogeneous currency `||wedge^3 M||_HS^2=Z`. Under scaling `A -> sA`, the right side scales as `s^(-2/3)`, exactly the scaling of an `L3` density norm.

### Corollary 5.2 — fractional small-ball bound

For every interval `J0`,

`boxed:
 P(Q in J0) < 6.787 Z^(-1/9)|J0|^(2/3).`                              (5.4)

This is not yet the linear-in-`|J0|` estimate needed for full QFORM, but it is dimension-free and retains arbitrary fragmented supports.

## 6. Actual application of the designated account04/B13 purification

The partner result is useful here at the level of the **convex output `L3` functional**, not just one fixed slab.

First prove (5.1) for arbitrary unit-measure product indicators that are bounded finite unions of intervals. The proof above applies verbatim. Account04/B13 gives, for every admissible cap-one marginal tuple, product-law approximants that are finite convex mixtures of such product indicators and converge in `L1`; measurable pushforward contracts total variation.

Every finite mixture output has an `L3` density of norm at most the same constant in (5.1), by Minkowski convexity. Since `L3` is reflexive, a subsequence converges weakly in `L3` to some density `p` with the same norm bound. Total-variation convergence of the pushforward measures identifies that weak `L3` limit with the actual output law. Hence the partner's extreme-product reduction transfers the full `L3` estimate (5.1) to **all** cap-one product laws with zero constant loss.

This is an actual inequality-level application. It does not assert an extremizing interval, an attained bathtub set, bounded support diameter, or bounded fragment count.

## 7. Relation to the full conjecture and first unpaid implication

Theorem 5.1 is a genuine target-level regularity statement but is not a full solution. The bare assumption `s_3(A)>=1` does not force a disjoint physical cross block with `Z` bounded below by a universal constant, and even a uniform `L3` density bound does not by itself imply a uniform `Linfinity` bound.

The remaining B13 obligation is now narrower:

**`QFORM-CROSS-3VOLUME-L3-TO-LINF-GLUING-v1`.** Starting from the product-preserving `L3` theorem above, identify a dependence-safe extra one-dimensional curvature/product mechanism that upgrades the `|J|^(2/3)` bound to `O(|J|)` without assuming a support radius, moment, single interval, post-rotation independence, or a uniformly good individual minor. The previously completed square-kernel smoothing does this when a genuine original-coordinate scalar pivot has a quantitative lower scale; the live no-pivot branch requires an aggregate replacement.

A second structural debt remains: in bad no-pivot witnesses whose useful disjoint cross blocks all have very small `Z`, combine the max-volume/cross-rank skeleton and bounded-hub mechanisms before taking reciprocal scales.

Full QFORM therefore remains **OPEN / NOT PROVED**. Full continuity also remains **OPEN**. Continuity is available in the paid entropic branch, while the hub/E2 branch currently yields only an `L3` density.

## 8. Deterministic checks

The companion exact-rational checker verifies the hub-contraction identity on a fixed integer matrix, verifies `sum_h Z_h=3Z` when all rows are used as hubs, and checks the constants in Sections 4--5, including

`C0=3.1173205167723097...`,
`C_E2=5.541728894337633...`,
`C_paid=6.772846206537608...`,
`C_hub=6.786385992671971... <6.787`.

The checker is corroborating evidence only; the mathematical proof is the analytic argument above.
