SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B13, 2026-09-23T15:57:36Z.
attacking: rank-four misalignment versus physical principal-volume star, using canonical fiber-score cores and source-pinned D5 control without deleting residual quadratic curvature.

# fleet02/B13 r30 — rank-four misalignment collapses to rank two or a physical third-volume bi-hub

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: extremal product laws / complementary constructions  
Designated partner: fleet03/B13  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**  
Full continuity: **OPEN**.

## 1. First unpaid implication

The first unpaid implication after this run is

`QFORM-RANK2-MISALIGNMENT-CORE-GLUE-v1`:

> On the canonical positive-slab-mass core, pay the remaining rank-at-most-two low-spectral cross interaction without rotating the independent variables and without globally deleting either the low-spectral leaf curvature or the explicit `rho^{-1}` operator tail. If this cannot be done, turn the large-core-radius / low-curvature alternatives below into a genuine bounded-finite-union product-indicator counterexample.

This is strictly smaller than the preceding fleet03/B13 obstruction `QFORM-RANK4-MISALIGNMENT-OR-STAR-CLOSURE-v1`: the rank-four cross misalignment is reduced below to rank at most two, except on an already identifiable physical third-volume bi-hub branch.

## 2. Source-pinned inputs actually used

### 2.1 Exact extremal-product purification, with no attained optimizer

Fleet04/B13, canonical commit

`yspennstate/math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B13/20260922T231352Z-fleet04-B13-rough-geometric-transfer-r5/REPORT.md`,

proves that every cap-one mass-one density is an `L^1` limit of finite convex mixtures of indicators of bounded finite unions of intervals of measure one. Consequently, for every bounded product kernel `K`,

`sup_(0<=f_i<=1, int f_i=1) int K prod_i f_i`

is the same supremum as over bounded finite-union unit-product indicators. This is an equality of suprema, not an attained bathtub theorem. There is no universal support diameter, interval shape, or fragment-count bound.

For a slab kernel this also gives the quantitative transfer used below: if an arbitrary cap-one product law has slab ratio `rho_0`, then for every `eta>0` there is a bounded finite-union unit-product witness with slab ratio at least `rho_0-eta`. Thus every strict high-ratio implication proved for those finite-union witnesses transfers back with arbitrarily small loss.

### 2.2 Designated partner fleet03/B13 canonical-core compiler

The latest completed compatible designated-partner result is fleet03/B13 r27,

`yspennstate/math-open-problems@980dd55d0202bf513f4dd0d6f72e78c8e74883d7`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B13/20260923T140232Z-fleet03-B13-qform-r27/REPORT.md`.

For a bounded finite-union near-extremal witness, its genuine coordinate fiber scores define canonical cores carrying at least half of the actual slab mass. Split selected physical coordinates into banks `U,V`, write the leaf block as `R`, the physical cross block as `B`, let `P_tau` be the deterministic spectral projection of the coefficient matrix `R` onto `|lambda|>=tau`, and let `R_U,R_V` be Euclidean radii of the canonical core after arbitrary centers. Put

`Delta_tau = tau R_V^2 + 2 ||B(I-P_tau)||op R_U R_V`.

When `d_tau=rank(P_tau)>=3`, `max_j(P_tau)jj<=1/2`, and the retained geometric mean `Lambda_tau=|pdet(R_tau)|^(1/d_tau)>=1`, the partner theorem gives

`rho <= 24(1+2 Delta_tau/ell)`,

where `ell` is the slab length. Hence

`rho>48  ==>  Delta_tau>ell/2`.                                      (2.1)

No random variables are rotated in this statement. The spectral projection is used only on the deterministic coefficient matrix.

### 2.3 Required pinned Claude/Fourier package

At the exact requested source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`,

`FOURIER_ROUTE_REPORT.md` proves two inequalities used here.

**D5.** For every ORIGINAL-coordinate disjoint physical cross block `M`, with

`Z_5=e_5(M^T M)`,

`||p_Q||inf <= C5 Z_5^(-1/10),      C5=5 sqrt(2e)`.                  (2.2)

There is no volume-marginal hypothesis.

**D'.** If the natural squared-`3x3`-minor row marginals of a physical cross block `M` are all at most `h<3/4`, then

`||p_Q||inf <= 6 sqrt(e)(2h)^(-1/2)(3-4h)^(-1)e_3(M^T M)^(-1/6)`. (2.3)

At `h=2/3`, the constant is

`C3=9 sqrt(3e)=25.70102107534928...`.                               (2.4)

Both estimates retain arbitrary same-side quadratic blocks, outside couplings, and affine terms. `COUNTEREXAMPLE_SEARCH.md` was also read; its numerical search found no counterexample, but none of those numerics are used as proof here.

## 3. D5 forces every physical cross block to be rank four plus a small operator tail

Let a product-law slab witness have interval length `ell>0` and ratio

`rho=P(Q in J)/ell`.                                                (3.1)

Let `B` be any disjoint ORIGINAL-coordinate physical cross block of its coefficient matrix. If `rank(B)<5`, then `s_5(B)=0`. Otherwise, (2.2) and `rho<=||p_Q||inf` give

`rho <= C5 e_5(B^T B)^(-1/10)`.                                    (3.2)

Since

`e_5(B^T B)>=s_1(B)^2 ... s_5(B)^2 >= s_5(B)^10`,                 (3.3)

we obtain in all cases

`boxed: s_5(B)<=C5/rho.`                                           (3.4)

Let `H` be the best rank-at-most-four SVD truncation of `B`, and set

`E=B-H`.                                                           (3.5)

By Eckart--Young,

`boxed: rank(H)<=4,   ||E||op=s_5(B)<=C5/rho.`                     (3.6)

This is a decomposition of the deterministic physical coefficient matrix. It is not a statement that the random quadratic form generated by `E` may be discarded on unbounded inputs.

## 4. Main theorem: rank-four misalignment collapses to rank two or a physical 3-volume bi-hub

Let `P` be **any** orthogonal projection acting on the column-coordinate Euclidean space of `B`; the intended application is `P=P_tau` from the partner theorem. Define

`H_P=HP,       H_Q=H(I-P)`.                                       (4.1)

Because `P(I-P)=0`,

`HH^T = HPH^T + H(I-P)H^T
      = H_P H_P^T + H_Q H_Q^T`.                                  (4.2)

Therefore

`H H^T >= H_Q H_Q^T`                                              (4.3)

in the positive-semidefinite order, and eigenvalue monotonicity gives

`s_3(H_Q)<=s_3(H)`.                                                (4.4)

Weyl's perturbation inequality and (3.6) then give

`s_3(H_Q)<=s_3(B)+C5/rho`.                                        (4.5)

Now consider the natural squared-third-minor probability law of `B` when `rank(B)>=3`:

`w_(S,T)=det(B[S,T])^2/e_3(B^T B)`.                               (4.6)

Write its row marginals as `alpha_i` and column marginals as `beta_j`.

### Theorem 4.1 — `QFORM-RANK4-MISALIGNMENT-TO-RANK2-OR-BIHUB-v1`

For every physical cross block `B`, every orthogonal right projection `P`, and every slab witness of ratio `rho`, at least one of the following holds:

1. **small third singular value:**
   `s_3(B)<=C3/rho`;

2. **physical third-volume bi-hub:** there are an original physical row `i` and original physical column `j` such that
   `alpha_i>2/3`, `beta_j>2/3`, and therefore
   `P_w(i in S and j in T)>1/3`;

and in alternative 1 there exists a matrix `L` of rank at most two such that

`boxed: B(I-P)=L+F,   ||F||op <= C*/rho`,                          (4.7)

where

`C*=C3+2C5
   =9 sqrt(3e)+10 sqrt(2e)
   =49.017460891320525...`.                                       (4.8)

#### Proof

If `rank(B)<3`, alternative 1 holds and the rank-two conclusion is immediate (take `L=B(I-P)`, `F=0`). Assume `rank(B)>=3`.

Suppose first that all row marginals satisfy `alpha_i<=2/3`. D' with `h=2/3` gives

`rho <= C3 e_3(B^T B)^(-1/6)`.                                    (4.9)

Since `e_3(B^T B)>=s_1^2s_2^2s_3^2>=s_3^6`,

`rho<=C3/s_3(B)`, hence `s_3(B)<=C3/rho`.                         (4.10)

Exactly the same argument applied to the physical transposed block `B^T` shows that if all column marginals satisfy `beta_j<=2/3`, then (4.10) again holds.

Consequently, if (4.10) fails, D' must fail in both orientations: some `alpha_i>2/3` and some `beta_j>2/3`. These marginals refer to the same law (4.6). Inclusion--exclusion therefore gives

`P_w(i in S and j in T)
 >=alpha_i+beta_j-1
 >1/3`,                                                            (4.11)

which is alternative 2.

It remains to prove (4.7) under alternative 1. By (4.5) and (4.10),

`s_3(H_Q)<= (C3+C5)/rho`.                                         (4.12)

Let `L` be the best rank-at-most-two approximation to `H_Q`. Eckart--Young gives

`||H_Q-L||op=s_3(H_Q)`.                                           (4.13)

Since

`B(I-P)=H_Q+E(I-P)`,                                               (4.14)

set

`F=(H_Q-L)+E(I-P)`.                                                (4.15)

Then `rank(L)<=2`, and using `||I-P||op=1`, (3.6), and (4.12),

`||F||op
 <=s_3(H_Q)+||E||op
 <=(C3+2C5)/rho
 =C*/rho`.                                                         (4.16)

This proves the theorem. QED.

### Scope check

The D'/D5 theorems are applied only to the genuine original-coordinate physical block `B`, where product independence is valid. The projection `P` appears only after those probabilistic estimates, inside deterministic singular-value algebra. No distribution of `P V` is ever asserted independent or cap one.

## 5. Apply Theorem 4.1 to the designated partner's canonical-core obstruction

Take the partner setup of Section 2.2, so `P=P_tau` and

`Delta_tau=tau R_V^2+2||B(I-P_tau)||op R_U R_V`.                   (5.1)

Suppose the physical third-volume bi-hub branch of Theorem 4.1 does **not** occur. Then there is `L`, `rank(L)<=2`, with

`B(I-P_tau)=L+F`, `||F||op<=C*/rho`.                              (5.2)

Hence

`Delta_tau
 <=tau R_V^2+2||L||op R_U R_V+2(C*/rho)R_U R_V`.                (5.3)

Assume the partner's diffuse retained-range hypotheses

`d_tau>=3`, `max_j(P_tau)jj<=1/2`, `Lambda_tau>=1`,                (5.4)

and `rho>48`, so (2.1) gives `Delta_tau>ell/2`.

We get the following exhaustive canonical-core obstruction.

### Corollary 5.1 — `QFORM-CANONICAL-CORE-RANK2-MISALIGNMENT-REDUCTION-v1`

Under (5.4), `rho>48`, and absent the physical third-volume bi-hub, at least one of

`(A)  R_U R_V > rho ell/(8C*)`,                                   (5.5)

`(B)  tau R_V^2 > ell/8`,                                         (5.6)

or

`(C)  there is rank(L)<=2 with ||L||op R_U R_V > ell/16`          (5.7)

holds.

#### Proof

If (A) fails, the last term in (5.3) is at most

`2(C*/rho)R_U R_V <= ell/4`.                                      (5.8)

Because `Delta_tau>ell/2`, the first two terms on the right side of (5.3) then sum to more than `ell/4`. Thus at least one exceeds `ell/8`. These are exactly (B) and, after dividing the second inequality by two, (C). QED.

This is the desired improvement over the partner's preceding rank-four obstruction. The residual high-rank part of the low-spectral cross interaction is quantitatively paid at scale `rho^{-1}`; the only unbounded cross interaction left is rank at most two. If the operator-tail payment is obstructed by support geometry, that obstruction is exposed as (A), rather than hidden by assuming bounded support. If the low-spectral leaf curvature itself matters on the core, it is exposed as (B), rather than perturbatively deleted.

## 6. Extremal-product transfer back to arbitrary cap-one laws

The canonical cores require a bounded finite-union witness only so that finite Euclidean core radii can be named. They do not require the original arbitrary-density law to have bounded support.

Given an arbitrary cap-one product law and a fixed slab `J` with ratio `rho_0`, choose `eta>0`. The no-attainment purification theorem supplies a bounded finite-union unit-product law with ratio

`rho>=rho_0-eta`.                                                  (6.1)

Run the canonical-core and Theorem 4.1 alternatives on that witness. Every inequality is source-valid for that genuine product indicator law. For a strict prospective counterexample sequence `rho_0 -> infinity`, choose `eta=o(rho_0)`; no constant loss appears. Fragment count and support diameter are allowed to depend arbitrarily on the approximant and may diverge. This is exactly why (5.5) is retained as an obstruction rather than ruled out by fiat.

No singular kernel is passed through bare total-variation convergence in this reduction. Only bounded slab indicators are transferred. Fractional/Riesz kernels, if used in the next glue step, must be introduced only after an appropriate integrability estimate has been established.

## 7. A real obstruction for any diverging counterexample sequence

Combine Corollary 5.1 with D5 itself. For any sequence of genuine target witnesses with `rho_m->infinity`, every physical cross block satisfies

`s_5(B_m)<=C5/rho_m ->0`.                                         (7.1)

At every spectral threshold for which the partner's retained-range hypotheses (5.4) hold, either a physical third-volume bi-hub occurs, or the low-spectral cross interaction on the canonical half-slab core has the explicit alternatives (5.5)--(5.7). Thus a counterexample cannot retain a genuinely rank-three-or-four misaligned cross piece of fixed operator scale while keeping canonical-core radii moderate. It is forced toward one of:

* physical third-volume concentration;
* exploding canonical-core radius product;
* slab-scale-significant low-spectral curvature;
* a rank-at-most-two low-spectral cross interaction.

The first and fourth are finite-hub/grouped-coordinate objects, while the middle two are explicit source-valid geometric obstructions. This is a strict reduction of the remaining search space; it is not yet the full theorem.

## 8. What remains

The next mathematical obligation is not another leverage cascade. It is the rank-two/core glue:

1. In branch (C), combine a rank-two physical-coefficient map `L` acting into the low-spectral deterministic subspace with the still-present true leaf block `R(I-P_tau)` and the canonical fiber-score core, using a completed physical-coordinate fractional-trace, grouped-bank, or pair mechanism. One must not declare the coordinates in the singular vectors of `L` independent.
2. In branch (B), use `tau R_V^2>ell/8` as actual slab-scale curvature rather than treating `R-R_tau` as a globally small random perturbation.
3. In branch (A), exploit the fact that the canonical core carries at least half of the slab mass and each coordinate belongs to a high fiber-score set; either derive a dimension-free swap/fragment penalty for enormous `R_U R_V`, or construct an explicit bounded-finite-union product-indicator counterexample.
4. In the bi-hub branch, route the `>1/3` third-minor currency through the existing physical hub/star and scalar/pair-pivot compilers.

Until one of these closes exhaustively, the full conjecture remains OPEN.

## 9. Integrity notes

Consumed live corrections include: no uniform pointwise quadratic-phase decay; no independence after rotation; no arbitrary-joint coarea bound; no worst-fiber conditional-cap moment; no universally good single physical minor or rank-three cross cut; no bounded-diameter or fixed-fragment-count extremal reduction; and no global deletion of a small coefficient tail on unbounded inputs.

The pinned counterexample search found no counterexample but is not proof. No moments, compact support of the original laws, log-concavity, Gaussianity, identical distribution, or post-rotation product structure is assumed. Essential boundedness is the target; continuity is kept separate.
