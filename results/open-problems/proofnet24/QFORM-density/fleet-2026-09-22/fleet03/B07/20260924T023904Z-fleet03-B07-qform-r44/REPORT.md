SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B07, 2026-09-24T02:39:04Z.
attacking: the r43 rank-12 cross-skeleton — add the missing H-vs-(I union J) determinant center and force either another physical E3 payment or a tunably small rank-6 three-bank carrier.

# fleet03/B07 r44 — four-crossing E3 router and tunably small rank-6 physical carrier

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: coordinate minor selection / GEOMETRY  
Run: `20260924T023904Z-fleet03-B07-qform-r44`  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
Status: **NEW FOUR-CROSSING DETERMINANT ROUTER + RANK-6 HIGH-SLAB-RATIO COMPILER / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**.

No Gaussian, moment, support, iid, log-concavity, diagonal-basis, post-rotation-independence, conditional-density-cap, or uniform pointwise oscillatory-decay assumption is used. All random banks below consist of literal original coordinates. Every nonzero coefficient tail is retained; no small Frobenius residual is declared probabilistically harmless.

## 1. Fresh source state and incoming branch


Immediate predecessor:

`yspennstate/math-open-problems@b028ca514bbb6d42baf6b544d787b55fcac0c24b`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260924T013915Z-fleet03-B07-qform-r43/REPORT.md`.

The inherited physical banks `H,I,J` are pairwise disjoint. Put

`K=A[I,J]`, `U=A[I,H]`, `V=A[H,J]`,

and

`Z=e2(KK^T) >= zeta:=2^(-12)`.

The r43 chamber also had `e3(KK^T)<eta:=2^(-30)`, but the theorem below is parameterized by a fresh threshold and does not freeze the r43 error scale.

Two pinned supporting results are used exactly in scope.

1. **Rank-two tail from the second/third compounds**, fleet02/B07:

`yspennstate/math-open-problems@81d6956476fa400f61d266effb4123a42fe3185c`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260924T003945Z-fleet02-B07-qform-auto11/REPORT.md`.

If `tau_2(K)=dist_F(K,rank<=2)^2`, then

`tau_2(K) Z <= 3 e3(KK^T)`.                                      (1.1)

2. **Marginal-free physical third-volume receiver**, fleet02/B03:

`yspennstate/math-open-problems@df738b7f0821d9af56dfd992cab10ecc6704e3fb`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260923T184716Z-fleet02-B03-QFORM-auto11/REPORT.md`.

For any literal original-coordinate crossing `M` with `e3(MM^T)>0`, the complete ambient form, with arbitrary same-side curvature, outside couplings, affine terms and additional spectrum retained, has a continuous `C_0` density satisfying

`||p_Q||_infinity <= C3 e3(MM^T)^(-1/6)`,                       (1.2)

where

`C3=3*2^(4/3)*e^(1/3)=10.550168831164775...`.

## 2. A missing elementary fact: E2-heavy directions are already top-two singular directions

Write the squared singular values of `K` as

`x1>=x2>=...>=0`, `S=sum_j xj`, `Z=e2(x)>0`.

The complete `E2` inclusion marginal from r43 is

`alpha_j=xj(S-xj)/Z`,                                              (2.1)

and

`sum_j alpha_j=2`.                                                (2.2)

For `i<j`,

`x_i(S-x_i)-x_j(S-x_j)
 =(x_i-x_j)(S-x_i-x_j) >=0`,                                     (2.3)

because `S-x_i-x_j` is the sum of the other nonnegative squared singular values. Hence

`alpha_1>=alpha_2>=alpha_3>=...`.                                (2.4)

Since the marginals sum to two,

`boxed: alpha_j<=2/3 for every j>=3.`                            (2.5)

Therefore the r43 spectral projection onto `alpha_j>2/3` is not merely rank at most two: it is a subprojection of the **top-two singular subspace** of `K` on each side.

This small ordering observation removes one entire extra deterministic direction from each of the `I` and `J` carrier spaces below.

## 3. Rank-two tail from a physical third crossing

### Lemma 3.1 — `QFORM-E3-R2-TAIL-v1`

For every real rectangular matrix `M`,

`boxed:
dist_F(M,rank<=2)^2 <= [6 e3(MM^T)]^(1/3).
}`                                                                  (3.1)

Equivalently,

`dist_F(M,rank<=2) <= [6 e3(MM^T)]^(1/6)`.                         (3.2)

### Proof

Let `y1>=y2>=...>=0` be the squared singular values, put `z=(y3,y4,...)`, and

`tau=sum_{j>=3} yj=dist_F(M,rank<=2)^2`.

Expanding `e3(y)` according to how many selected indices lie in `z`,

`e3(y)=y1*y2*tau+(y1+y2)e2(z)+e3(z)`.                            (3.3)

Since `y1,y2>=z_i`,

`y1*y2*tau >= sum_i z_i^3`.                                      (3.4)

Also `y1+y2>=z_i+z_j`, so

`(y1+y2)e2(z)
 >= sum_{i<j} z_i z_j(z_i+z_j)
 = sum_{i!=j} z_i^2 z_j`.                                        (3.5)

Finally

`tau^3=sum_i z_i^3+3 sum_{i!=j}z_i^2z_j+6e3(z)`.                  (3.6)

Comparing coefficients in (3.3)-(3.6) gives `e3(y)>=tau^3/6`, proving (3.1). QED.

No coordinate selection enters this lemma; it is an aggregate singular-volume statement.

## 4. Four literal physical crossings

Besides the three crossings already implicit in r43, introduce the missing physical cut centered on `H`:

`M0 = A[I,J] = K`,
`M1 = A[I,J union H] = [K U]`,
`M2 = A[I union H,J] = [K;V]`,
`M3 = A[H,I union J] = [U^T V]`.                                 (4.1)

Every row bank and column bank in (4.1) is disjoint in the original coordinates.

Fix **any** threshold `theta>0`.

If some `r in {0,1,2,3}` satisfies

`e3(M_r M_r^T) >= theta`,                                        (4.2)

then (1.2) immediately gives the full ambient form a continuous density with

`boxed:
||p_Q||_infinity <= C3 theta^(-1/6).
}`                                                                  (4.3)

Assume from now on that all four third volumes are `<theta`.

## 5. Simultaneous top-two synchronization on I and J

Let `P2` and `Q2` be top-two left/right singular projections for `K`, padded harmlessly if rank `K<2`.

The r43 Newton-transform inequality says that if `P_*` is the `alpha>2/3` left projection, then

`e3(M1 M1^T)-e3(KK^T)
 >= (Z/3)||(I-P_*)U||_F^2`.                                     (5.1)

By (2.5), `P_*<=P2`, so under the four-low-volume assumption,

`boxed:
||(I-P2)U||_F^2 < 3 theta/Z <= 3 theta/zeta.
}`                                                                  (5.2)

The right-side version gives

`boxed:
||V(I-Q2)||_F^2 < 3 theta/Z <= 3 theta/zeta.
}`                                                                  (5.3)

From (1.1),

`boxed:
||K-P2 K Q2||_F^2 < 3 theta/Z <=3 theta/zeta.
}`                                                                  (5.4)

Thus the same top-two SVD spaces of the common determinant bank `K` simultaneously carry `K`, the `I-H` interface from the `I` side, and the `H-J` interface from the `J` side.

## 6. The H-side crossing supplies the third common two-plane

Apply Lemma 3.1 to

`M3=[U^T V]: H -> I union J`.

Let `R2` be a top-two left singular projection of `M3` on the physical `H` coefficient space. Since `e3(M3M3^T)<theta`,

`boxed:
||(I-R2)M3||_F^2
 =||U(I-R2)||_F^2+||(I-R2)V||_F^2
 <=(6theta)^(1/3).
}`                                                                  (6.1)

Define the retained cross blocks

`U0=P2 U R2`,
`V0=R2 V Q2`,
`K0=P2 K Q2`.                                                       (6.2)

The orthogonality of the projections gives

`||U-U0||_F^2
 =||(I-P2)U||_F^2+||P2 U(I-R2)||_F^2`,                             (6.3)

and

`||V-V0||_F^2
 =||(I-R2)V||_F^2+||R2 V(I-Q2)||_F^2`.                             (6.4)

Using (5.2)-(5.4) and (6.1),

`boxed:
||U-U0||_F^2+||V-V0||_F^2+||K-K0||_F^2
 <= 9 theta/zeta +(6theta)^(1/3).
}`                                                                  (6.5)

## 7. Rank-six three-bank carrier

On the physical direct sum `H direct_sum I direct_sum J`, define the symmetric cross-only carrier

`R_cross = [[0,    U0^T, V0],
            [U0,   0,    K0],
            [V0^T, K0^T, 0 ]].`                                    (7.1)

Its range is contained in

`Ran(R2) direct_sum Ran(P2) direct_sum Ran(Q2)`,                    (7.2)

whose dimension is at most `2+2+2=6`. Therefore

`boxed: rank R_cross<=6.`                                          (7.3)

Let `E_cross` be the exact symmetric difference between the actual three inter-bank blocks and (7.1), with zero same-bank blocks. No coefficient is deleted. Since the symmetric Frobenius norm counts every rectangular interface twice, (6.5) gives

`boxed:
||E_cross||_F^2
 <=18 theta/zeta +2(6theta)^(1/3).
}`                                                                  (7.4)

This proves the new supporting theorem:

### Theorem 7.1 — `QFORM-FOUR-CROSSING-R6-CARRIER-v1`

In the r43 chamber `Z=e2(KK^T)>=2^(-12)`, for every `theta>0`, either one of the four literal original-coordinate crossings (4.1) has third volume at least `theta`, in which case the full ambient quadratic form has a continuous density bounded by `C3 theta^(-1/6)`, or the complete three-bank **inter-bank coefficient matrix** has an exact decomposition

`A_cross=R_cross+E_cross`,

with

`rank R_cross<=6`,

`||E_cross||_F^2 <=18 theta/zeta+2(6theta)^(1/3)`.                 (7.5)

All three same-bank blocks `A[H,H]`, `A[I,I]`, `A[J,J]`, every outside coupling, and every additional eigenvalue remain untouched. Equation (7.5) is structural currency, not a perturbative density theorem.

This improves r43 in two ways: the carrier rank drops from twelve to six, and the residual is no longer frozen at the `2^-30` threshold — it can be made quantitatively as small as demanded by a high small-ball ratio.

## 8. High-slab-ratio consequence: O(1/rho) distance to rank six

Let `J0` be an interval and

`rho = P{Q in J0}/|J0|`.                                            (8.1)

Choose

`theta=(2C3/rho)^6`.                                               (8.2)

If any crossing in (4.1) had third volume at least `theta`, (4.3) would give

`||p_Q||_infinity <=rho/2`,

contradicting (8.1). Hence every such high-ratio witness inside the r43 chamber must satisfy the rank-six alternative. Substituting (8.2) into (7.4),

`boxed:
||E_cross||_F
 <= (2C3/rho)
 sqrt(2*6^(1/3)+(18/zeta)(2C3/rho)^4).
}`                                                                  (8.3)

At the natural inherited scale `theta<=eta=2^-30`, equivalently

`rho>=rho0:=2C3 eta^(-1/6)=64 C3
 =675.2108051945455...`,                                           (8.4)

we have `2C3/rho<=1/32`, so

`boxed:
||E_cross||_F <=40.612278123/rho.
}`                                                                  (8.5)

Thus a putative unbounded-density sequence cannot remain merely a fixed-distance rank-twelve cross skeleton. In this determinant-heavy branch its complete inter-bank coefficient structure converges to **rank at most six at rate O(1/rho)**.

## 9. Actual application of the designated fleet04/B07 result

The designated completed partner is

`yspennstate/math-open-problems@dab16464e87c939cc0cf3fd01d070045290192fa`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B07/20260923T161510Z-fleet04-B07-coordinate-core-r2/REPORT.md`.

Its `r=0` coordinate-core theorem applied to an actual physical triple `T` gives: if

`|A_hh|>=1/64` for `h in T`,

and every mutual off-diagonal obeys

`|A_hk|<=1/768`,                                                   (9.1)

then

`s3(A[T,T])>=1/64-3/768=3/256`,                                  (9.2)

and therefore

`boxed:
||p_Q||_infinity
 <= 2sqrt(18pi)/(3/256)
 =1283.393676611072... .
}`                                                                  (9.3)

This inequality is used at the high-ratio interface, not cited abstractly: if `rho>1283.393676612`, no such high-diagonal triple can survive. Its failure creates the independence-number-at-most-two high-diagonal graph already paid by r42's determinant-weighted physical-E3 cut. Hence a slab-ratio sequence beyond (9.3) that reaches the present r43/r44 branch is genuinely in the low-diagonal survivor; the partner theorem has removed the finite physical-core alternative before (8.5) is invoked.

Continuity is not claimed on the partner-core exit; the physical-E3 exits in Sections 4 and 9's r42 continuation do give continuity.

## 10. Regression checks

`CHECKS.py` uses only the Python standard library. It performs 5,000 exact-integer spectral regressions. It checks:

1. `6 e3 >= tau_2^3` from Lemma 3.1;
2. the exact `sum alpha=2` identity;
3. the ordering (2.4), the at-most-two heavy count, and that every `alpha>2/3` index lies among the first two;
4. `C3`, the inherited threshold `rho0`, the coefficient `40.612278123` in (8.5), and the partner constant (9.3).

The captured output ends `STATUS=PASS`. These are regression checks only; the proof is the algebra above.

## 11. Exact remaining implication

Full QFORM is not proved or disproved. Full-target continuity is not proved.

The next precise debt is

`QFORM-R6-CROSS-CARRIER-O(1/RHO)-PLUS-LOWCURVATURE-RECEIVER-v1`:

> In the low-diagonal determinant-heavy branch, consume the exact rank-at-most-six inter-bank carrier together with an `O(1/rho)` Frobenius inter-bank residual, while retaining arbitrary same-bank blocks, all outside couplings, and the original-coordinate product law; or force a new physical `E3` crossing / physical principal core.

The point of (8.5) is that a contradiction sequence now supplies a **vanishing deterministic coefficient error**, not merely a fixed small tail. It remains invalid to infer that `X^T E_cross X` is small without moment/support assumptions. A valid next receiver must exploit the vanishing coefficient geometry jointly with the cap-one product law.
