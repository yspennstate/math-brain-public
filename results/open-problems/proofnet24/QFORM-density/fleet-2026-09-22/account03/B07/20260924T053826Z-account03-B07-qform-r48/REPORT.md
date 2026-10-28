SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B07, 2026-09-24T05:38:26Z.
attacking: the retained-tail physical rank-two carrier — globalize it to one full original-coordinate separator, then select pair-block minors by determinant weight before any inversion.

# account03/B07 r48 — global separator and pair-block E2 deletion selection

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: coordinate minor selection / GEOMETRY  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
Status: **NEW LIVE-BRANCH GLOBALIZATION + NEW PAIR-BLOCK DETERMINANT-WEIGHT SELECTION / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**.

No Gaussianity, moments, log-concavity, compact or connected support, iid assumption, diagonal-basis assumption, post-rotation independence, law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea, fiber supremum, or deletion of a nonzero coefficient tail is used. Singular-vector calculations below are deterministic coefficient algebra only.

## 1. Fresh controls and exact incoming branch


The exact incoming theorem is account03/B07 r44:

`yspennstate/math-open-problems@b12b80a3b5a2185d67074eed7c739bec6abc06b2`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260924T050943Z-account03-B07-qform-r44/REPORT.md`.

It comes from the pair-disjoint matching branch of r47. If `H_M` is the union of the matched physical pairs, `U=I union J` is the fixed opposite physical bank, and

`C0=A[U,H_M]`,

then the deterministic pair-kernel compression has squared Frobenius energy greater than

`T0=8192/31=264.258064516129...`.

R44 proves the exhaustive physical-crossing alternative:

1. a literal physical E3 crossing already pays the full ambient law continuously; or
2. the entire literal crossing satisfies

`dist_F(C0,rank<=2)<d_*`,

where

`d_*=0.10429071727552326290...`,

and moreover either

`dist_F(C0,rank<=1)<sqrt(2)d_*`

or

`s1(C0)s2(C0)>p_*:=1.19876993884320...`.

The nonzero coefficient tail is retained in this statement.

The completed physical-E3 receiver used below is the current source line quoted and applied in account03/B20 r46 (`yspennstate/math-open-problems@9ae7023224386e95ab2bd7f088347db8750c7b06`): for any literal original-coordinate cross block `M`,

`||p_Q||_infinity <= C_E3 E3(M)^(-1/6)`,

`C_E3=8.4530212255281768747049...`,

with a continuous C0 density on the paid branch; arbitrary same-side quadratic blocks, affine terms, outside couplings, signs and extra spectrum are retained.

The designated account04/B07 dependency read in full is

`yspennstate/math-open-problems@dab16464e87c939cc0cf3fd01d070045290192fa`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B07/20260923T161510Z-account04-B07-coordinate-core-r2/REPORT.md`.

For an actual physical principal block of size `m=r+3` with

`A[I,I]=D+R+E`, `|D_ii|>=d`, `rank R<=r`, `|E|_max<=epsilon`,

it proves

`s3(A[I,I])>=d-(r+3)epsilon`,

and the corresponding full-ambient essential-density bound. Continuity is not claimed by that gate.

## 2. First missing implication: local matched carrier -> one global separator

The r44 carrier only crossed from `U` into the matched endpoint bank `H_M`; arbitrary outside coordinates could still carry additional crossing curvature. The first task is to include every such coupling without deleting it.

Assume the r44 branch is **not** the near-rank-one alternative, so

`dist_F(C0,rank<=1)>=sqrt(2)d_*`.                                  (2.1)

Let the singular values of `C0` be `s1>=s2>=...`, and set

`t2=sum_{j>=3}s_j^2=dist_F(C0,rank<=2)^2<d_*^2`.                  (2.2)

From (2.1)-(2.2),

`s2^2+t2>=2d_*^2`,

so

`boxed: s2(C0)>d_*=0.104290717...>1/64.`                         (2.3)

Also

`s1(C0)^2+s2(C0)^2=||C0||_F^2-t2>T0-d_*^2`.

Since `s1>=s2`,

`boxed: s1(C0)^2>c2:=(T0-d_*^2)/2`
`     =132.1235939812095945658... .`                             (2.4)

In particular

`s1(C0)s2(C0)>sqrt(c2)d_*=1.19876993884320...`,                  (2.5)

recovering the r44 nondegeneracy constant directly.

Now form the **global literal physical separator**

`M=A[H_M^c,H_M]`.                                                 (2.6)

The old crossing `C0` is a row submatrix of `M`. Thus

`M^T M=C0^T C0+D^T D`

for the omitted outside-row block `D`, and PSD eigenvalue monotonicity gives

`s_j(M)>=s_j(C0)` for every j.                                   (2.7)

Therefore the whole global cut satisfies

`s1(M)^2>c2`, `s2(M)>d_*`, `s1(M)s2(M)>p_*`.                     (2.8)

No outside coupling has been discarded.

## 3. The global separator either pays E3 or is rank-two thin

Account03/B20 r46 proves for every real matrix `M` the deterministic inequality

`E3(M) >= (1/3) s1(M)^2 dist_F(M,rank<=2)^4`.                    (3.1)

Take

`epsilon=2^-16`.

If

`dist_F(M,rank<=2)>=epsilon`,                                    (3.2)

then (2.4) and (3.1) give

`E3(M)>delta_global:=c2 epsilon^4/3`
` =2.38747812718366933884e-18`.                                  (3.3)

The completed physical-E3 receiver therefore pays the **full ambient law with a continuous C0 density**:

`||p_Q||_infinity`
` <=C_E3 delta_global^(-1/6)`
` =7311.76221377679...<7312.`                                    (3.4)

Hence every still-unpaid non-near-rank-one matching state has one global original-coordinate cut satisfying simultaneously

`boxed: dist_F(M,rank<=2)<2^-16,`                                (3.5)

`boxed: s2(M)>0.104290717,`                                      (3.6)

`boxed: s1(M)s2(M)>1.1987699388.`                               (3.7)

This is `QFORM-MATCHED-R2-TO-GLOBAL-SEPARATOR-v1`.

The result is stronger than a local rank-two carrier: every coupling from a matched physical endpoint to every coordinate outside `H_M` is now part of the same rank-two tube. It does **not** delete the Frobenius tail in (3.5) as a random perturbation.

A source audit found the related account02/B20 global-heavy-arm funnel. That source already establishes the general strategy that a physical arm can be globalized to a rank-two cut. The present contribution is not a claim of novelty for that generic idea; it is the explicit application to the r44 matched-kernel carrier, with the stronger live constants (3.5)-(3.7) and the pair-preserving determinant selection below.

## 4. New pair-block E2 deletion theorem

The matching structure gives a partition of the column set `H_M` into disjoint **physical pairs**. A one-column inclusion marginal is not enough here because deleting only one endpoint destroys the pair geometry used by the exact rank-one-pair receiver. The correct currency is an inclusion marginal of an entire matched pair.

Let `N` be any real matrix whose columns are partitioned into disjoint blocks `K` of size two. For each unordered physical column pair `J={a,b}`, define its complete second-minor weight

`w_J=sum_{|I|=2} det N[I,J]^2 >=0`.                              (4.1)

By Cauchy-Binet,

`Z:=e2(NN^T)=sum_{|J|=2} w_J`.                                  (4.2)

For a matched physical pair `K`, define the determinant-weighted block inclusion marginal

`beta_K=(1/Z) sum_{J: J cap K != empty} w_J`.                    (4.3)

Each two-column set `J` intersects either one matched pair (when both columns belong to the same pair) or two matched pairs. Therefore

`sum_K beta_K`
` =(1/Z) sum_J (# matched blocks hit by J) w_J`
` <=2`.                                                          (4.4)

Consequently

`boxed: #{K: beta_K>2/3}<=2.`                                   (4.5)

Let `N_{-K}` denote the matrix obtained by deleting both physical columns belonging to `K`. Exactly the weights in (4.3) disappear, hence

`e2(N_{-K}N_{-K}^T)=Z(1-beta_K)`.                               (4.6)

Thus every pair except at most two satisfies

`boxed: e2(N_{-K}N_{-K}^T)>=Z/3.`                              (4.7)

This is `QFORM-PAIR-BLOCK-E2-DELETION-v1`. It spends the whole second-compound determinant bank before selecting a physical pair, and it never takes a reciprocal of one coordinate minor.

The theorem is dimension-free and exact. It is distinct from the prior single-row/single-column E2 inclusion identities: the blocks here are the actual pair-disjoint matching objects and both physical endpoints are deleted together.

## 5. Apply the pair-block theorem to the live global separator

Apply Section 4 to the global separator `M` from (2.6), with its physical matched-pair column partition. From (3.7),

`Z=e2(MM^T)>=s1(M)^2s2(M)^2>p_*^2`
` =1.43704936627412946815... .`                                 (5.1)

Hence all but at most two matched physical pairs satisfy the concrete deletion-stability inequality

`boxed: e2(M_{-K}M_{-K}^T)`
` >p_*^2/3`
` =0.479016455424709822718... .`                                (5.2)

This is a much stronger conclusion than saying that some pair has a nonzero minor. Nearly the entire matched family may be deleted one pair at a time while retaining a macroscopic complete E2 determinant packet across the global cut.

The recent account02/B07 reciprocal-fan regression was also checked. It shows that a Frobenius-small tail can carry most of E2, so (5.2) is **not** interpreted as saying that the E2 mass lies inside the rank-two SVD truncation. The full physical separator, including its nonzero tail, remains the object in (5.1)-(5.2).

## 6. Required account04/B07 theorem applied to the live pair selection

Each matched pair `K` in the r47/r44 source is an exact nonzero rank-one physical principal pair,

`A[K,K]=lambda_K u_K u_K^T`, `||u_K||=1`.                       (6.1)

If

`|lambda_K|>=1/32`,                                               (6.2)

then at least one physical endpoint `i(K)` satisfies

`|A_{i(K)i(K)}|=|lambda_K| |u_K(i(K))|^2>=1/64`.                 (6.3)

Call such a pair **high**, and call it **stable-high** if it also satisfies the determinant-weight deletion condition `beta_K<=2/3`. By (4.5), all but at most two high matched pairs are stable-high.

Take three stable-high pairs and their selected endpoints `i_1,i_2,i_3`. If the three literal mutual physical edges obey

`|A_{i_a i_b}|<=1/768` for `a!=b`,                              (6.4)

then the designated account04/B07 theorem applies with `r=0`,

`d=1/64`, `epsilon=1/768`,                                      (6.5)

and yields the actual principal-core inequality

`s3(A[{i_1,i_2,i_3},{i_1,i_2,i_3}])`
` >=1/64-3/768=3/256`.                                         (6.6)

Its full-ambient physical-fiber estimate gives

`boxed: ||p_Q||_infinity`
` <=2 sqrt(18 pi)/(3/256)`
` =1283.393676611072... .`                                      (6.7)

Continuity is not claimed by this partner gate.

Therefore, in an unpaid branch with at least five high matched pairs, at least three are stable-high, and the graph on all stable-high selected endpoints whose edges are

`|A_ij|>1/768`                                                   (6.8)

has independence number at most two. Equivalently, failure of the partner core forces a dense physical-edge obstruction **after** the pair-block determinant stability has already been secured.

The existing exact rank-one-pair receiver also implies, on an unpaid pair, `|lambda_K| S_K<2^-10`. Hence every high pair from (6.2) additionally has

`S_K<1/32`.                                                       (6.9)

So the residual high-pair obstruction is quantitative: a large physical diagonal endpoint, a small kernel-star, and a global E2 packet which survives deletion of the full pair.

## 7. What is closed and what remains

This run closes one precise synchronization debt from r44. In the non-near-rank-one matched branch, the local physical rank-two carrier can no longer hide uncontrolled outside coupling: either those outside directions create enough aggregate third curvature to give the full law a continuous density `<7312`, or the **entire global physical cut** is a `2^-16` rank-two tube with `s2>0.10429` and `s1s2>1.19877`.

Inside that global separator, pairwise coordinate selection is now determinant-weighted and pair-preserving: at most two matched physical pairs can destroy more than two thirds of the complete E2 packet when removed. Every other pair deletion leaves `E2>0.479016`.

The remaining branches are explicit:

1. the r44 near-rank-one physical carrier branch `dist_F(C0,rank<=1)<0.147489347`;
2. the global rank-two separator (3.5)-(3.7), whose small nonzero tail cannot be deleted and whose E2 may live in that tail;
3. within it, the stable-high endpoint graph with independence number at most two when the account04/B07 principal-core exit fails;
4. the distinct r47 high-degree hub branch.

The next B07 implication is `QFORM-GLOBAL-R2-PAIR-STABLE-THIRD-RESOURCE-v1`: jointly spend the global nondegenerate rank-two separator, its retained `2^-16` tail, and the pair-stable E2 bank to obtain the missing third smoothing resource or force a paid physical principal core / E3 crossing. The account02/B07 reciprocal-fan family is a mandatory regression: a proof may not treat the small Frobenius tail as negligible at compound level.

Full QFORM remains **OPEN / not proved / not disproved**. Full-target continuity remains **OPEN**. Continuity is proved here only on the physical-E3 payment (3.4); the designated account04/B07 principal-core payment establishes essential boundedness only.

## 8. Computation and source audit

`CHECKS.py` recomputes every displayed r44-to-global constant and runs 1000 deterministic-seed random-matrix regressions of the pair-block inclusion/deletion identities. The captured `CHECKS.txt` ends `STATUS=PASS`; its maximum relative deletion-identity error was `1.024e-15`. These checks are regression evidence only. The proofs are Sections 2-6.

A repository search found the related account02/B20 global rank-two separator and the account02/B07 reciprocal-fan stress calculation, and those are explicitly credited above. The search did not find a completed source matching the matched-pair block inclusion law (4.3)-(4.7) applied at the r44 constants. This is only a duplicate-work audit, not an external novelty claim.
