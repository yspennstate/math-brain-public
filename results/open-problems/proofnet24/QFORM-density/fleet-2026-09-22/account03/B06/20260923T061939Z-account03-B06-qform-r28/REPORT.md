SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B06, 2026-09-23T06:19:39Z.
attacking: the two-row/two-column determinant hub left by the aggregate E2 branch; compress its curvature to one anchored Schur-or-double-star currency before any reciprocal local-minor payment.

# account03/B06 r28 — two-hub anchored Schur currency

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15`  
**Assignment:** Curved fiber integration  
**Classification:** `NEW SUPPORTING STRUCTURAL THEOREM + LIVE BRANCH APPLICATION / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and first missing implication

The target remains the full owner statement: for every dimension, independent ORIGINAL real coordinates with one-dimensional probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal essential-density bound for `Q=X^TAX`, or give a valid counterexample. No Gaussian, log-concave, moment, compact-support, connected-support, iid, or diagonal-basis hypothesis is added. Orthogonal changes of deterministic matrices are never used to manufacture independence of spectral coordinates. Continuity remains a separate desired conclusion.

The preceding B06 run reduced the low-third-volume / near-rank-two chamber as follows. For an ORIGINAL-coordinate cross block `B`,

`Z2=e2(B^T B)=sum_(|S|=|T|=2) det B[S,T]^2`,

and the determinant-squared row-pair law has disjointness probability `delta_R`. The completed account01/B04 theorem gives, with a genuine untouched original-coordinate square coefficient `a!=0`,

`||p_Q||_infinity <= 4 sqrt(2e) |a|^(-1/2) Z2^(-1/8) delta_R^(-1/16)`.

In the live B06 transverse scale, `Z2>16G^4/25`; therefore `delta_R>=1/256` pays the branch by `<13.947/sqrt(|a|G)`. If `delta_R<1/256`, an actual two-row hub captures more than `255/256` of the determinant-weighted row-pair mass. Applying the same theorem to `B^T` yields the identical alternative on the column side. Thus the first genuinely new state is: **both a two-row and a two-column hub exist, but no individual physical minor need be large**.

This run proves the exact deterministic compiler for that state. It aggregates the full hub-intersection mass first and turns it into one of four anchored cofactor matrices. The resulting currency has an exact Schur/double-star identity and remains dimension-free even in the canonical family where every individual physical minor tends to zero.

Consumed live corrections include: law-uniform pointwise quadratic-phase decay is false; arbitrary-joint rank-three coarea is false; positive conditional projection-density moments are false; post-rotation independence is false; unrestricted fiber suprema lose dimension; aggregate determinant mass does not force one uniformly good physical minor; and a small nonzero tail may not be discarded.

## 2. Source-valid inputs

### 2.1 Disjoint E2 entropy-halving theorem

Account01/B04 proved `QFORM-DISJOINT-E2-ENTROPY-HALVING-v1` at

`yspennstate/math-open-problems@e0f6866f77e8c38b5c482acaf55094f60d3f28ac`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B04/20260923T055035Z-account01-B04-QFORM-auto13/REPORT.md`.

Besides the paid inequality above, it proves the exact residual-volume identity

`delta_R = E_(S~mu_R)[ e2(B[S^c,J]^T B[S^c,J])/Z2 ]`.

Hence `delta_R<epsilon` yields a physical row pair `H_R` for which more than `1-epsilon` of the determinant-squared row-pair law intersects `H_R`. Transposition gives the column version.

### 2.2 Dependence-safe square theorem from account04

The completed account04/B18 result

`QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`,

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`,

states that if `R` has density at most `M` and, conditionally on `R=r`, `V_r` has density at most one, then

`T=R+aV_R^2`, `a!=0`,

has density at most

`||p_T||_infinity <= 2 sqrt(M/|a|)`.

No independence between `R` and the translated square variable is required.

The exact designated partner `account04/B06` still has no completed current-QFORM canonical artifact in the fresh repository search; I do not invent one. Section 6 applies the compatible completed account04/B18 theorem to an actual target-valid diffuse-hub family.

## 3. General two-hub anchor lemma

Let `B` be any real `m x n` matrix with `Z2>0`. Put the canonical joint determinant law

`nu(S,T)=det B[S,T]^2/Z2`,

where `S` ranges over physical row pairs and `T` over physical column pairs. Let `mu_R,mu_C` be its row and column marginals.

Let `H_R` and `H_C` be physical row and column hub sets, not necessarily of size two, and suppose

`mu_R{S:S cap H_R != empty} >= 1-epsilon_R`,
`mu_C{T:T cap H_C != empty} >= 1-epsilon_C`,

with `epsilon_R+epsilon_C<1`.

For an anchor `(i,a)` define the complete anchored two-volume

`Z_(i,a)=sum_(j!=i, b!=a) det B[{i,j},{a,b}]^2`.                  (3.1)

### Theorem 3.1 — `QFORM-TWO-HUB-ANCHOR-CURRENCY-v1`

There is an anchor `(i,a) in H_R x H_C` such that

`boxed:
 Z_(i,a) >= [(1-epsilon_R-epsilon_C)/(|H_R||H_C|)] Z2.
`                                                                       (3.2)

#### Proof

Under `nu`, let

`A={S cap H_R != empty}`, `C={T cap H_C != empty}`.

The two marginal hypotheses and the union bound give

`nu(A cap C)>=1-epsilon_R-epsilon_C`.                                (3.3)

Now sum the anchored masses over all hub anchors. A fixed minor `(S,T)` is counted exactly

`|S cap H_R| |T cap H_C|`

times. On `A cap C` this multiplicity is at least one. Hence

`sum_(i in H_R,a in H_C) Z_(i,a)
 >= Z2 nu(A cap C)
 >=(1-epsilon_R-epsilon_C)Z2`.                                      (3.4)

There are `|H_R||H_C|` anchors. Pigeonhole gives (3.2). QED.

The order is crucial: the determinant squares are summed over the entire physical cross bank **before** any anchor is selected. No lower bound on one local `2 x 2` determinant is inferred.

## 4. Exact anchored Schur / double-star identity

Fix any anchor `(i,a)`. Delete row `i` and column `a`, and write the block decomposition

`B = [[b, r^T],
      [c, D]]`,                                                     (4.1)

where

`b=B_(i,a)`,
`r=B_(i,J\{a})`,
`c=B_(I\{i},a)`,
`D=B_(I\{i},J\{a})`.

### Theorem 4.1 — `QFORM-ANCHOR-SCHUR-COFACTOR-IDENTITY-v1`

The anchored currency has the exact identity

`boxed:
 Z_(i,a)=|| bD-c r^T ||_F^2.
`                                                                       (4.2)

Consequently:

* if `b!=0`,

  `boxed: Z_(i,a)=b^2 ||D-c r^T/b||_F^2`,                            (4.3)

  so the currency is exactly the scalar anchor squared times the **entire Schur cross-bank Frobenius energy**;

* if `b=0`,

  `boxed: Z_(i,a)=||c||_2^2 ||r||_2^2`,                              (4.4)

  so a vanishing anchor does not destroy the payment: all curvature becomes an exact two-sided double-star product;

* in every case,

  `sqrt(Z_(i,a)) <= |b| ||D||_F + ||c||_2 ||r||_2`,                 (4.5)

  hence at least one of

  `|b| ||D||_F >= (1/2)sqrt(Z_(i,a))`,

  `||c||_2 ||r||_2 >= (1/2)sqrt(Z_(i,a))`                           (4.6)

  holds.

#### Proof

For every deleted row `j` and deleted column `beta`,

`det B[{i,j},{a,beta}]=b D_(j,beta)-c_j r_beta`.                    (4.7)

Squaring and summing (4.7) over all `j,beta` gives (4.2). Equations (4.3) and (4.4) are immediate. The Frobenius triangle inequality gives

`||bD-cr^T||_F <= |b| ||D||_F+||c r^T||_F
                 = |b| ||D||_F+||c||_2||r||_2`,

and (4.6) follows. QED.

This is the useful finite-hub normal form. The `b!=0` branch points to a grouped Schur receiver; the `b=0` branch points to a grouped double-star/hyperbolic receiver. Neither branch pays a reciprocal individual minor.

## 5. Concrete live B06 constants

Return to the r27 transverse chamber. There

`Z2>16G^4/25`.                                                       (5.1)

If either row or column determinant-pair disjointness is at least `1/256`, the completed entropy-halving/square route already pays the corresponding branch. Therefore consider only

`delta_R<1/256`, `delta_C<1/256`.                                   (5.2)

The residual-volume identity produces a two-row hub `H_R` and, after transposition, a two-column hub `H_C`, each capturing more than `255/256` of its marginal pair mass. Apply Theorem 3.1 with

`|H_R|=|H_C|=2`, `epsilon_R=epsilon_C=1/256`.

Then some anchor `(i,a)` satisfies

`Z_(i,a)
 > (1-2/256) Z2/4
 = (127/512) Z2
 > (127/800) G^4`.                                                  (5.3)

Thus

`boxed:
 ||bD-cr^T||_F > sqrt(127/800) G^2
              =0.3984344362... G^2.
`                                                                       (5.4)

By (4.6), at least one of the two grouped currencies obeys

`boxed:
 |b| ||D||_F >0.1992172181... G^2
   or
 ||c||_2 ||r||_2 >0.1992172181... G^2.
`                                                                       (5.5)

This is the new quantitative squeeze. The old state was merely “two row hubs and two column hubs”; the survivor is now forced into one of four **anchored Schur-or-double-star packets** carrying a fixed fraction of the full two-volume scale.

No conclusion is drawn from (5.5) by deleting the complementary spectrum or by choosing its largest entry. The next analytic receiver must consume `b(D-cr^T/b)` or the whole double star `cr^T` at the product-law level.

## 6. Diffuse double-star stress family and actual account04 inequality

The `b=0` alternative in (4.4) is not an artificial endpoint. It occurs in a target-valid family for which every local physical minor tends to zero.

Let the left bank have coordinates `{0,1,...,N}` and the right bank `{0,1,...,M}`. Let

`u=(0,N^(-1/2),...,N^(-1/2))`,
`v=(0,M^(-1/2),...,M^(-1/2))`,

and let `e0` be the first coordinate vector on either side. Define

`B_(N,M)= e0 v^T + u e0^T`.                                        (6.1)

Because `e0 perp u` and `e0 perp v`, the two nonzero singular values of `B_(N,M)` are exactly `1,1`. Every nonzero physical `2 x 2` minor uses row `0` and column `0`, and

`det B[{0,j},{0,k}] = -1/sqrt(NM)`.                                (6.2)

Hence

`Z2=1`, `delta_R=delta_C=0`, `Z_(0,0)=1`,                           (6.3)

while the largest local minor tends to zero as `N,M->infinity`. At the anchor `(0,0)`,

`b=0`, `D=0`, `||c||=||r||=1`,                                    (6.4)

so (4.4) records the whole curvature exactly.

The symmetric pure-bipartite matrix

`A0=[[0,B_(N,M)],[B_(N,M)^T,0]]`

has nonzero spectrum `{1,1,-1,-1}` and is therefore inside the owner's spectral target. The completed weighted two-bank theorem gives the base quadratic form

`R=2 X^T B_(N,M) Y`

a density bound

`M=e sqrt(2pi)=6.8137220896...`.                                   (6.5)

Now add one untouched original coordinate `Z`, independent of both banks, and set

`Q=Z^2+R`.                                                          (6.6)

This matrix still satisfies the target, now with an additional `+1` eigenvalue. Apply the completed account04/B18 theorem to the **actual** decomposition (6.6), with `a=1` and no independence assumption needed after disintegration:

`||p_Q||_infinity <=2 sqrt(M)
 =2 sqrt(e sqrt(2pi))
 =5.2206214533... .`                                                (6.7)

Thus the canonical zero-anchor / infinitely diffuse local-minor family is uniformly paid once its whole double-star bank is retained. This is a concrete check that the currency in (4.4), rather than a largest-minor selector, is the correct geometric object.

The exact assigned partner `account04/B06` has no completed current-QFORM result visible at publication; (6.7) is therefore the required actual use of the compatible completed account04/B18 result, not a fabricated partner claim.

## 7. What is new and what remains unpaid

The new theorem closes a structural gap but not yet the analytic hub packet in complete generality:

1. if determinant-pair disjointness is not tiny on either side, the existing aggregate E2 smoother pays before any single minor is selected;
2. if both disjointness probabilities are tiny, Theorem 3.1 forces one of four row-hub/column-hub anchors to carry at least `127/800` of the live `G^4` scale;
3. Theorem 4.1 identifies that anchor exactly as either a full Schur cross-bank currency `b(D-cr^T/b)` or a zero-anchor double-star currency `cr^T`;
4. the exact diffuse double-star stress family is uniformly paid and shows why selecting one local minor would be wrong.

The first unpaid implication is therefore

`QFORM-ANCHORED-SCHUR-OR-DOUBLESTAR-PRODUCT-RECEIVER-v1`:

> Starting from (5.4), and retaining arbitrary same-bank quadratic curvature plus every complementary spectral component, prove a product-preserving weighted receiver which pays either the whole Schur bank `b(D-cr^T/b)` or the whole double-star bank `cr^T` without dividing by a single small physical coefficient. A valid receiver may be a two-dimensional Fresnel/Brascamp--Lieb integral, an aggregate half-Riesz inequality, or an exhaustive route into already-paid pair/ridge/grouped-bank nodes.

The very fresh account02/B19 near-null interpolation theorem is complementary rather than duplicative: it reduces the punctured scalar-curvature loss inside a different rank-two transverse receiver, but still reports the full target open. The anchored identity here supplies a deterministic grouped currency that can feed such near-null or grouped-hub receivers.

## 8. Scope and regularity

`QFORM-TWO-HUB-ANCHOR-CURRENCY-v1` and `QFORM-ANCHOR-SCHUR-COFACTOR-IDENTITY-v1` are deterministic supporting theorems. Equation (6.7) is an actual target-valid bounded-density application. No universal continuity conclusion is proved by the new structural theorem; the full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**, and the universal continuous-density statement remains open separately.

A finite checker accompanying this report verifies (4.2) on random matrices, the exact constants in (5.3)-(5.5), and the diffuse double-star singular values/minor sum. It is a sanity check only; the algebra above is the proof.
