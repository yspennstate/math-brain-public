SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B13, 2026-09-23T17:10:27Z.
attacking: global rank-two-cross structure after the partner's volume cascade; replace reciprocal tiny-minor selection by a bounded-coefficient physical skeleton and isolate the surviving max-norm twist.

# account02/B13 — four-anchor max-volume skeleton and an anchored three-volume cascade

Status: **PROVED SUPPORTING TARGET-LEVEL IMPLICATIONS / FULL QFORM OPEN / FULL CONTINUITY OPEN / WITHOUT_VERIFIED_BRAIN**.

Programme: `QFORM-DENSITY-3EIG-20260922`.

All coordinate sets below are ORIGINAL physical coordinates. Deterministic linear algebra on coefficient matrices is allowed; no transformed random coordinates are declared independent. No support, moment, centering, log-concavity or connectedness assumption is used.

## 0. First unpaid implication

The first remaining B13 implication after this report is

`QFORM-FOUR-HUB-MAXNORM-TWIST-GLUE-v1`:

> Pay, with one universal slab constant, the self-consistent configuration in which at most four physical coordinates are retained as hubs and the remaining principal block is diagonal plus rank at most four plus a zero-diagonal twist `E`, where `||E||_max` obeys the slab-dependent bounds (7.3) below, every disjoint physical cross block has `s_3=O(rho^{-1})`, and every fifth exterior cross volume is `O(rho^{-10})`. The argument must retain `E` as a genuine quadratic term on arbitrary fragmented/unbounded product laws; it may not delete it using coefficient smallness. Otherwise construct a genuine cap-one product counterexample, which by purification may be taken to be a product of unit-measure sets without assuming interval or diameter control.

The new point is that the prior vague “global rank-two-cross structure” has been converted into an explicit physical `2 x 2` max-volume core with bounded interpolation coefficients and a quantitative max-norm twist. The twist is `O(rho^{-3/2})` whenever the largest physical off-diagonal entry stays at a fixed positive scale.

## 1. Source-pinned premises actually used

### 1.1 Designated partner account03/B13 r29

Current completed partner source:

`yspennstate/math-open-problems@a23ddf469392d77526db53d0811248a52a84d088`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260923T165827Z-account03-B13-qform-r29/REPORT.md`

with the later proof clarification

`yspennstate/math-open-problems@c9a6c9160e063f07856a62fc89a2ba62b857d3cf`

`.../POSTREFRESH_ADDENDUM.md`.

Its theorem `QFORM-BIHUB-VOLUME-CASCADE-CLOSURE-v1`, after the clarification that Stages 1 and 2 condition every original coordinate outside the displayed physical banks, states:

for every slab witness

`rho = P{X^T A X in J}/|J|`

and every disjoint physical cross block `B=A[L,R]`,

`boxed: s_3(B) <= C_3/rho,   C_3=9 sqrt(3e)=25.701021075349... .`       (1.1)

The partner proves this by closing its former third-volume bi-hub alternative with the grouped projected-crossing receiver. I use (1.1) at an actual `3 x 3` physical block below.

### 1.2 Reviewed grouped projected-crossing receiver

I read the current independently checked statement at

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

The instance needed here is `(k,ell,d)=(2,1,3)`. Two ORIGINAL hubs `H`, a three-coordinate physical column bank `J`, hub-to-`J` matrix `M_J` of row rank two with singular-value product `S`, and projected residual rows `c_i` with

`Z_1=sum_i ||c_i||^2`

satisfy, when each one-volume row marginal `||c_i||^2/Z_1 <=1/2`,

`||p_Q||_inf <= 3*2^(5/6) (S^2 Z_1)^(-1/6)`.                     (1.2)

All same-side light curvature, all diagonal terms, all affine terms and arbitrary internal hub functions remain. The same source's exact-rank crossing theorem says that for two groups of exactly three original coordinates with invertible `3 x 3` physical cross matrix `M`,

`||p_Q||_inf <= 3 |det M|^(-1/3)`.                                (1.3)

No post-rotation independence is used in either statement.

### 1.3 Required pinned Claude/Fourier source

I read at the required immutable source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

all of

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`,
`FOURIER_ROUTE_REPORT.md`, and
`COUNTEREXAMPLE_SEARCH.md`.

I use two completed results from it.

First, the unconditional fifth-volume theorem `D_5`: for every disjoint physical cross block `M`, with

`Z_5=e_5(M^T M)`,

`boxed: ||p_Q||_inf <= C_5 Z_5^(-1/10),   C_5=5 sqrt(2e)=11.658219907986... .}`   (1.4)

There is no volume-marginal condition.

Second, the counterexample-search report's proved finite-dimensional Theorem A pays the `n=3` target directly: if all three eigenvalues have modulus at least one, then `||p_Q||_inf <=6 sqrt(pi)`. The numerical search itself reports no counterexample, but none of its numerical evidence is used as proof.

### 1.4 No-attainment product purification

I read account04/B13

`yspennstate/math-open-problems@82f9b7e9372c2434f27fd1f5a65e7148663516a7`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260923T121154Z-account04-B13-nonattained-bathtub-r1/REPORT.md`.

Its Theorem 3.1 proves for every nonnegative product kernel that the supremum over arbitrary cap-one, mass-one marginals equals the supremum over product indicators of arbitrary measurable unit-measure sets, without asserting an optimizer. Thus strict slab violations may be purified with arbitrarily small loss while keeping the coefficient matrix fixed. No centered interval, bounded diameter or finite universal fragment count enters.

### 1.5 Exact zero-minor structure

The current Claude continuation

`yspennstate/math-open-problems@c4c23b784395630c094ba299a50712209921d1ae`

`proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/structure/REPORT.md`

proves that if every disjoint/off-diagonal `2 x 2` minor of a symmetric matrix vanishes, then

`A = D + R,   D diagonal,   rank R <=2`.                            (1.5)

This is used only for the exact endpoint `Delta_2=0` below.

## 2. A new anchored three-volume bound around every physical two-core

Let `P,Q` be disjoint physical two-sets with

`K=A[P,Q]`, `det K !=0`,

and let `j` be any physical coordinate outside `P union Q`. Put

`J_3 = Q union {j}`

and define the anchored three-volume bank

`W_j(P,Q) = sum_{i notin P union Q union {j}} det A[P union {i}, Q union {j}]^2`.   (2.1)

### Theorem 2.1 — `QFORM-TWOCORE-ANCHORED3-CASCADE-v1`

For every slab witness of ratio `rho`,

`boxed: W_j(P,Q) <= 23328 rho^(-6).}`                               (2.2)

The same statement holds after swapping rows and columns.

### Proof

Use the two original coordinates `P` as the hub bank and the three original coordinates `J_3` as the selected column bank. Condition every original coordinate outside

`P union J_3 union I`,

where

`I=[n] \ (P union J_3)`.

The hub-to-column matrix

`M=A[P,J_3]`

has row rank two because it contains the invertible restriction `K`. Let

`S^2=det(MM^T)>0`.

For each `i in I`, project its physical crossing row off `row(M)`:

`c_i=P_(row(M)^perp) A[i,J_3]`.

Since `J_3` has dimension three and `row(M)` has dimension two, the `c_i` lie on one common one-dimensional transverse line. The Gram/Schur identity is exact:

`boxed: S^2 ||c_i||^2 = det A[P union {i},J_3]^2.}`                 (2.3)

Indeed, both sides are the squared three-volume of the three row vectors consisting of the two rows of `M` and `A[i,J_3]`.

Summing (2.3) gives

`S^2 Z_1=W_j`,   `Z_1=sum_i||c_i||^2`.                              (2.4)

If every one-volume row marginal

`alpha_i=||c_i||^2/Z_1`

is at most `1/2`, apply (1.2):

`rho <= 3*2^(5/6) W_j^(-1/6)`.

Therefore

`W_j <= (3*2^(5/6)/rho)^6 = 3^6 2^5 rho^(-6)=23328 rho^(-6)`.      (2.5)

If instead some physical `i` has `alpha_i>1/2`, put

`d_i=det A[P union {i},J_3]`.

Then by (2.3)--(2.4),

`d_i^2 > W_j/2`.                                                    (2.6)

Condition every other original coordinate and apply the exact three-by-three crossing estimate (1.3) to the three ORIGINAL rows `P union {i}` and three ORIGINAL columns `J_3`:

`rho <= 3 |d_i|^(-1/3)`.

Hence

`W_j < 2 d_i^2 <= 2*3^6 rho^(-6)=1458 rho^(-6)`,                  (2.7)

which is stronger than (2.2). These two cases exhaust the row-marginal gate. QED.

### Consequence 2.2

Every individual bordered determinant obeys

`boxed: |det A[P union {i},Q union {j}]| <= 108 sqrt(2) rho^(-3)}`  (2.8)

whenever the six involved row/column indices are disjoint in the displayed sense. Here

`sqrt(23328)=108 sqrt(2)=152.735064736294...`.

This conclusion is aggregate-before-inversion: (2.2) first pays the whole anchored bank; (2.8) is only a consequence.

## 3. Maximum physical two-core: bounded interpolation without a tiny-minor loss

Assume `n>=4`; `n=3` is already paid by the pinned finite-dimensional theorem in Section 1.3.

Define the largest disjoint physical two-minor

`Delta = max{|det A[P,Q]|: |P|=|Q|=2, P cap Q=empty}`.             (3.1)

If `Delta=0`, (1.5) gives the exact structure `A=D+R`, `rank R<=2`. So suppose `Delta>0`, choose maximizing disjoint `P,Q`, and put

`K=A[P,Q]`, `|det K|=Delta`,
`V=[n] \ (P union Q)`.

For `i in V`, define the left interpolation vector

`r_i = A[i,Q] K^(-1) in R^2`,

and for `j in V` define

`c_j = K^(-1) A[P,j] in R^2`.                                      (3.2)

### Lemma 3.1 — bounded physical interpolation

`boxed: ||r_i||_infinity <=1,   ||c_j||_infinity <=1.}`            (3.3)

#### Proof

By Cramer's rule, each coordinate of `r_i` is a disjoint physical `2 x 2` minor divided by `det K`: for example its first numerator is the determinant of the rows `{i,p_2}` against columns `Q`. Maximality of `Delta` bounds its modulus by `Delta`. The other coordinate and the two coordinates of `c_j` are identical. No lower bound on `Delta` is required. QED.

Thus the inverse `K^{-1}` may be numerically large, but it never appears as an uncontrolled interpolation coefficient: all physical interpolation factors have modulus at most one.

## 4. First max-volume residual estimate: direct use of the partner's global `s_3` theorem

For distinct `i,j in V`, form the physical `3 x 3` cross block

`M_ij=A[P union {i},Q union {j}]`.

The row and column triples are disjoint, so the partner theorem (1.1) gives

`s_3(M_ij)<=delta`,   `delta=C_3/rho`.                              (4.1)

Every one of the nine `2 x 2` minors of `M_ij` is itself a disjoint physical two-minor, hence has modulus at most `Delta`. Cauchy--Binet therefore gives

`e_2(M_ij M_ij^T)<=9 Delta^2`.                                     (4.2)

If its singular values are `t_1>=t_2>=t_3`,

`|det M_ij|^2=t_1^2t_2^2t_3^2
             <= t_3^2 e_2(M_ijM_ij^T)
             <=9 delta^2 Delta^2`.                                 (4.3)

The bordered determinant identity is

`det M_ij = det K [ A_ij - A[i,Q]K^(-1)A[P,j] ]`.                  (4.4)

Combining (4.3)--(4.4):

`boxed:
 |A_ij-A[i,Q]K^(-1)A[P,j]|
 <=3 delta
 =27 sqrt(3e)/rho
 =77.103063226048.../rho.
}`                                                                    (4.5)

This is a dimension-free max-norm skeleton estimate obtained from the partner's completed global cross-rank-two conclusion. It neither selects a reciprocal tiny minor nor discards any random quadratic term.

## 5. Second residual estimate: the new anchored three-volume cascade

For the same maximizing `P,Q`, (2.8) and (4.4) give the stronger scale-sensitive estimate

`boxed:
 |A_ij-A[i,Q]K^(-1)A[P,j]|
 <= (108 sqrt(2))/(Delta rho^3).
}`                                                                    (5.1)

Therefore the same physical rank-two skeleton satisfies

`boxed:
 |A_ij-A[i,Q]K^(-1)A[P,j]|
 <= min( 27 sqrt(3e)/rho,
          108 sqrt(2)/(Delta rho^3) ).
}`                                                                    (5.2)

When the maximal disjoint two-volume stays bounded below, the leaf error is `O(rho^{-3})`, not merely `O(rho^{-1})`.

## 6. A rank-one skeleton supplies the complementary small-`Delta` branch

Let

`a = max_{p!=q}|A_pq|`.                                             (6.1)

If `a=0`, `A` is diagonal and the already-proved diagonal theorem gives `||p_Q||_inf<=pi`. So assume `a>0`, choose `p!=q` with `|A_pq|=a`, and let

`V_1=[n]\{p,q}`.

For distinct `i,j in V_1`, the disjoint physical `2 x 2` minor on rows `{p,i}` and columns `{q,j}` gives

`|A_pq A_ij-A_pj A_iq|<=Delta`.

Hence the physical rank-one cross skeleton

`T^(1)_ij=A_iq A_pj/A_pq`

obeys

`boxed: |A_ij-T^(1)_ij|<=Delta/a.}`                                (6.2)

Again the interpolation coefficients are bounded:

`|A_iq/A_pq|<=1`, `|A_pj/A_pq|<=1`.                                (6.3)

Thus a small maximal two-volume is not inverted; it is routed to a lower-rank two-anchor skeleton.

## 7. Global hierarchical skeleton theorem

### Theorem 7.1 — `QFORM-FOUR-ANCHOR-HIERARCHICAL-SKELETON-v1`

Let `rho` be the slab ratio of a target witness and let `a` be (6.1).

If `a=0`, the form is diagonal and already paid.

If `a>0`, then there is a physical hub set `H` with `|H|<=4`, and on `V=H^c` a decomposition

`boxed: A[V,V]=D+S+E,}`                                             (7.1)

where

- `D` is diagonal;
- `S` is symmetric of rank at most four;
- `E` is symmetric with zero diagonal;
- `S` arises from a physical one- or two-core skeleton whose left/right interpolation coefficients all have modulus at most one; and
- the max-norm twist satisfies

`boxed:
 ||E||_max
 <= sqrt(108 sqrt(2)/(a rho^3))
 = 12.358602863443... a^(-1/2) rho^(-3/2).
}`                                                                    (7.2)

Moreover one may choose a (possibly different) four-hub rank-at-most-four skeleton with

`boxed:
 ||E||_max <= 27 sqrt(3e)/rho
             =77.103063226048.../rho.
}`                                                                    (7.3)

Consequently some at-most-four-hub decomposition obeys the better of the two displayed numerical upper bounds.

### Proof

If `Delta=0`, the exact structure theorem (1.5) is stronger, so take `E=0`.

For `Delta>0`, two candidates are available:

1. the two-anchor rank-one skeleton of Section 6, with residual

`epsilon_1<=Delta/a`;

2. the four-anchor rank-two nonsymmetric skeleton

`T=A[V,Q]K^(-1)A[P,V]`,

whose residual is at most

`epsilon_2<=108 sqrt(2)/(Delta rho^3)`

by (5.1).

Choose the smaller candidate. Since

`min(x,y)<=sqrt(xy)`,

`min(epsilon_1,epsilon_2)
 <=sqrt(108 sqrt(2)/(a rho^3))`.                                    (7.4)

The rank-one candidate has rank one before symmetrization; the rank-two candidate has rank two. Since `A[V,V]` is symmetric, replace the chosen `T` by

`S=(T+T^T)/2`.

The rank becomes at most two in the first branch and at most four in the second, while for every off-diagonal pair

`|A_ij-S_ij|
 <= (|A_ij-T_ij|+|A_ji-T_ji|)/2`

is bounded by the same residual. Put

`D=diag(A[V,V]-S)`

and `E=A[V,V]-D-S`. This proves (7.1)--(7.2). Equation (7.3) follows by using the max-two-volume skeleton and (4.5) instead. QED.

### Interpretation

For any hypothetical sequence with `rho->infinity` and with the largest off-diagonal physical coefficient bounded below by `a_0>0`, the remaining leaf twist after at most four physical hubs satisfies

`||E||_max=O(rho^(-3/2))`.

This is stronger than the previously available `O(rho^{-1})` max-norm reduction. It does **not** justify deleting `E`: a max-norm-small matrix may have dimension-growing operator norm, and arbitrary cap-one supports can be unbounded or fragmented.

## 8. Required pinned `D_5` result applied to the surviving obstruction

Apply (1.4) to every disjoint physical cut `I,J`. If

`Z_5=e_5(A[I,J]^T A[I,J])>0`,

then the slab ratio satisfies

`rho <= C_5 Z_5^(-1/10)`.

If `Z_5=0` the following is trivial. Hence every slab witness obeys

`boxed:
 e_5(A[I,J]^T A[I,J])
 <= (5 sqrt(2e)/rho)^10
}`                                                                    (8.1)

for every disjoint physical cut. In particular

`boxed: s_5(A[I,J])<=5 sqrt(2e)/rho.}`                              (8.2)

This is a real obstruction on the same four-hub skeleton chamber: a candidate cannot use a dimension-growing fifth exterior cross-volume to amplify the max-norm twist. The source theorem is unconditional in its volume marginals, so there is no hidden leverage gate here.

The pinned counterexample search reports no valid counterexample in its tested families; that numerical fact is not used in (8.1)--(8.2).

## 9. Product-law / nonattainment interface

Nothing in Sections 2--8 assumes an attained bathtub optimizer. The partner theorem (1.1) already applies to arbitrary cap-one product laws. Independently, account04/B13 Theorem 3.1 shows exactly why the extremal-law interface is safe:

for the bounded slab kernel

`K_J(x)=1_{x^T A x in J}`,

the supremum over arbitrary cap-one probability marginals equals the supremum over products of indicators of arbitrary unit-measure measurable sets. A strict violation can therefore be transferred with arbitrarily small loss and with the same coefficient matrix `A`.

The selector sets can be arbitrarily fragmented and unbounded. No argument above replaces them by one interval, imposes a common diameter, or assumes a global maximizer. The matrix skeleton is consequently source-valid for the exact arbitrary-law target.

A useful caution is that finite-union approximation does **not** make the twist `E` perturbative. Even a coefficient `eps` multiplying `XY` is not uniformly small on translated cap-one laws: if `X,Y` are uniform on `[eps^{-1},eps^{-1}+1]`, then after subtracting a constant, `eps XY` contains an order-one linear term. Such translations are harmless only to receivers already uniform in affine terms; they do not license deletion of the residual quadratic term. This is why `QFORM-FOUR-HUB-MAXNORM-TWIST-GLUE-v1` remains explicit.

## 10. Relation to the current Claude structure theorem

The current continuation's structure report proves the exact endpoint “all disjoint `2 x 2` minors vanish implies diagonal plus rank at most two,” and records a general max-volume skeleton idea. The present run contributes the slab-scale specialization needed after the designated partner's new global `s_3` theorem, plus the anchored three-volume cascade (2.2), which improves the residual from `O(rho^{-1})` to `O((Delta rho^3)^{-1})`, and then the hierarchical interpolation (7.2), which removes the reciprocal `Delta` by routing small `Delta` through a lower-rank physical skeleton.

The result is therefore not a claim that max-volume skeletonization itself is new. The new target-level content is the explicit combination

`partner global s_3` + `reviewed k=2,ell=1 projected crossing` + `physical max-volume hierarchy`,

with all constants and product-law provenance retained.

## 11. What is still not proved

The full conjecture is not proved. In particular:

1. `||E||_max=O(rho^{-1})` or even `O(rho^{-3/2})` cannot be promoted to a small random perturbation without moments/support control.
2. The rank-at-most-four leaf skeleton need not be aligned with independent coordinates after spectral diagonalization; no rotated independence is available.
3. The exact `Delta=0` class is diagonal plus rank at most two, but the general indefinite rough-law payment of every such higher-dimensional orientation is not asserted here beyond the separately source-proved subclasses.
4. The current Claude single-hub conditional-adaptation estimate `(SP)` remains OPEN and is not used as a theorem.
5. Continuity of the full output law remains separate.

The next useful analytic move should exploit the self-consistency of the twist scale together with the physical bounded-coefficient skeleton, rather than perturbatively deleting `E`. A counterexample attempt must respect simultaneously (1.1), (7.1)--(7.3), and the fifth-volume collapse (8.1).

## 12. Constants

`C_3=9 sqrt(3e)=25.701021075349...`

`3 C_3=27 sqrt(3e)=77.103063226048...`

`3*2^(5/6)=5.345392308842...`

`(3*2^(5/6))^6=23328`

`sqrt(23328)=108 sqrt(2)=152.735064736294...`

`sqrt(108 sqrt(2))=12.358602863443...`

`C_5=5 sqrt(2e)=11.658219907986...`.

All numerical values merely evaluate exact constants; no numerical experiment is used in a proof.
