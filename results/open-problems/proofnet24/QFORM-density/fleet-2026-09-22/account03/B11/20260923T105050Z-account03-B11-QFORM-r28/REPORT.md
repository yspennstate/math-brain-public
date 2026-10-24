SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-23T10:50:50Z.
attacking: the large-disjoint-Plucker-mass indefinite branch; convert diffuse disjoint two-volume into two independent original-coordinate banks before any reciprocal minor is paid.

# account03/B11 r28 — disjoint Plucker mass forces a balanced two-bank spectral split

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** indefinite signatures / quantitative inequalities and rigorous computations  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_STRUCTURAL_THEOREM / PARTNER_RESULT_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and correction boundary

The full target remains open: for every `n`, every family of independent real original-coordinate inputs with probability densities bounded by one, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal `L^infinity` bound for the density of `X^T A X`, or give a genuine counterexample. Continuity is a separate desired conclusion.

Fresh owner control remained revision `2026-09-22.15`, QFORM-only. The live correction inbox was re-read immediately before publication. Nothing below assumes post-rotation independence, a law-uniform pointwise Fresnel/van-der-Corput estimate, an arbitrary-joint indefinite coarea bound, a conditional-density cap manufactured by conditioning, or the existence of one uniformly good physical minor.

The immediate structural predecessor is account03/B11 r24, `QFORM-EXACT-RANK3-LOCAL-OR-DISJOINT-WEDGE-v1`, canonical source `yspennstate/math-open-problems@9d7b5bb7d58f4f7a92ab12e3332bfbac36fa01f0`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260923T080909Z-account03-B11-QFORM-r24/REPORT.md`. For an exact-rank-three frame it proves that either the output is already bounded through a localized original-coordinate triple, or the ordered probability `Delta` that two Plucker-volume-sampled physical row pairs are disjoint satisfies `Delta>=1/64`.

A new analytic receiver relevant to the endpoint below is account03/B01 `QFORM-RANK2-CROSS-BOUNDED-REMAINDER-L2-v1`, source `yspennstate/math-open-problems@7d42d8f8f6b64490b4462fe304676462a4e7d3a8`. It pays a source-disjoint rank-two physical cross bicore once an independent bounded-density remainder is available. The present result supplies bank-level spectral currency before inversion; it does not silently assert that the needed bicore/remainder decomposition follows automatically.

The designated partner result actually applied below is account04/B11's completed sign-frustrated-triangle theorem, canonical source recorded in the fleet as `yspennstate/math-open-problems@572f6cd066c9cdef7b5a509917b4dcd79cea2fda`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260923T021512Z-account04-B11-sign-frustrated-triangle-r4/REPORT.md`.

## 2. Setup: Plucker edge law

Let `R` be an `n x 3` real matrix with orthonormal columns and rows `r_i in R^3`. Thus

`sum_i r_i r_i^T = I_3`.                                           (2.1)

For every physical edge `e={i,j}`, set

`w_e = ||r_i wedge r_j||^2`.                                       (2.2)

Cauchy--Binet on the second exterior power gives

`sum_e w_e = e_2(R^T R)=e_2(I_3)=3`.                              (2.3)

Hence `p_e=w_e/3` is a probability law on physical edges. Define the **ordered disjoint-edge mass**

`Delta = sum_{e cap f = empty} p_e p_f`.                            (2.4)

The sum in (2.4) is ordered, exactly as in r24.

## 3. Main theorem: random-cut two-bank balance

### Theorem — `QFORM-DISJOINT-PLUCKER-TO-TWO-BANK-BALANCE-v1`

For every frame `R` above there is a partition of the ORIGINAL coordinate set

`{1,...,n}=S disjoint_union T`                                     (3.1)

such that, writing

`G_S = R_S^T R_S = sum_{i in S} r_i r_i^T`,
`G_T = R_T^T R_T = I_3-G_S`,                                      (3.2)

one has

`e_2(G_S)e_2(G_T) >= 9 Delta/16`.                                 (3.3)

If the eigenvalues of `G_S` are

`1>=g_1>=g_2>=g_3>=0`,                                             (3.4)

then necessarily

`g_2(1-g_2) >= Delta/16`,                                          (3.5)

and in particular

`g_2 >= Delta/16`, `1-g_2 >= Delta/16`.                            (3.6)

Equivalently,

`sigma_2(R_S)^2 >= Delta/16`,
`sigma_2(R_T)^2 >= Delta/16`.                                      (3.7)

Thus in the r24 unpaid branch `Delta>=1/64` there is a disjoint original-coordinate bipartition with

`boxed: sigma_2(R_S), sigma_2(R_T) >= 1/32.`                       (3.8)

This is dimension-free and does not select a physical coordinate or minor.

### Proof

Color each physical coordinate independently `S` or `T` with probability `1/2`. Define

`W_S = sum_{e subset S} w_e`,
`W_T = sum_{f subset T} w_f`.                                      (3.9)

By the exterior Cauchy--Binet identity on a restricted row set,

`W_S=e_2(G_S)`, `W_T=e_2(G_T)`.                                   (3.10)

Now expand the expectation of the product. If two edges intersect, the event `e subset S` and `f subset T` is impossible. If `e,f` are disjoint, all four involved vertices receive prescribed colors, so

`P(e subset S, f subset T)=1/16`.                                 (3.11)

Therefore

`E[W_S W_T]
 = (1/16) sum_{e cap f=empty} w_e w_f
 = (1/16)*9 Delta
 = 9 Delta/16`.                                                     (3.12)

Hence some deterministic cut satisfies (3.3).

For that cut, because `0<=G_S<=I`, its eigenvalues satisfy (3.4), and

`e_2(G_S)=g_1g_2+g_1g_3+g_2g_3 <=3g_2`.                           (3.13)

The eigenvalues of `G_T=I-G_S` are `1-g_3 >= 1-g_2 >= 1-g_1`, so similarly

`e_2(G_T)<=3(1-g_2)`.                                              (3.14)

Combining (3.3), (3.13), and (3.14),

`9 Delta/16 <= e_2(G_S)e_2(G_T)
              <=9 g_2(1-g_2)`,                                   (3.15)

which is (3.5). Since `g_2(1-g_2)<=g_2` and also `<=1-g_2`, (3.6) follows. The nonzero squared singular values of `R_S` are the eigenvalues of `G_S`; those of `R_T` are the eigenvalues of `G_T`. Their second squared singular values are therefore `g_2` and `1-g_2`, giving (3.7). At `Delta=1/64`, (3.7) gives squared lower bound `1/1024` and singular-value lower bound `1/32`. QED.

## 4. Product-provenance meaning of the theorem

Let `q_1,q_2,q_3` diagonalize `G_S`, with `q_2` the middle eigenvector. The scalar spectral contribution in direction `q_2` splits as

`q_2^T R^T X
 = q_2^T R_S^T X_S + q_2^T R_T^T X_T`.                           (4.1)

The two terms in (4.1) are **genuinely independent**, because they come from disjoint original-coordinate banks. Their coefficient-vector norms are respectively

`sqrt(g_2)`, `sqrt(1-g_2)`,                                       (4.2)

and both are at least `sqrt(Delta)/4`. In the r24 large-Delta branch both are at least `1/32`.

More strongly, the top two eigen-directions of `G_S` can be normalized to an orthonormal two-dimensional coefficient system inside source bank `S`; the corresponding normalized two-dimensional projection of `X_S` has a source-valid product-marginal density cap at most `2`. The same is true for the top two directions of `G_T`. Thus large disjoint Plucker mass has now been converted into **two independent source banks, each carrying two spectral directions with quantitative norm**, rather than into one microscopic physical edge.

This is exactly the aggregate-before-inversion currency that the live local-minor corrections require.

## 5. Why this does not yet imply a rank-two physical cross bicore

One must not replace (3.7) by the stronger assertion that the physical cross block `A_{S,T}` automatically has two large singular values. That implication is false even at fixed positive `Delta`.

Take four physical rows

`r_1=(1,0,0)`,
`r_2=(0,1/sqrt(2),0)`,
`r_3=(0,1/sqrt(2),0)`,
`r_4=(0,0,1)`,                                                  (5.1)

and

`M=diag(1,1,-1)`, `A=R M R^T`.                                   (5.2)

Then `R^T R=I_3` and `A` has nonzero spectrum `{1,1,-1}`. The six Plucker weights are

`w_12=w_13=w_24=w_34=1/2`, `w_14=1`, `w_23=0`,                   (5.3)

so their sum is three and

`Delta=1/9`.                                                       (5.4)

For the cut `S={1,2}`, `T={3,4}`,

`G_S=diag(1,1/2,0)`, `G_T=diag(0,1/2,1)`,                        (5.5)

so both banks carry two spectral directions. Nevertheless

`A_{S,T}=[[0,0],[1/2,0]]`                                        (5.6)

has rank only one.

This is not a QFORM counterexample. In fact the whole quadratic form is

`Q = X_1^2 + ((X_2+X_3)/sqrt(2))^2 - X_4^2`.                     (5.7)

The three displayed grouped scalars come from disjoint original-coordinate banks. The grouped middle scalar has density cap at most `sqrt(2)`, while `X_1` and `X_4` have caps at most one. The two positive square terms therefore have convolution density at most

`boxed: pi sqrt(2) = 4.4428829381...`,                            (5.8)

and convolution with the independent negative square cannot increase the essential supremum. Thus when the rank-two cross currency collapses in this example, the third direction reappears as same-sign grouped self-curvature and still removes the rank-two logarithm.

The example is included to keep the structural conclusion exact: the new theorem proves two-bank spectral balance, not a rank-two cross-block theorem.

## 6. Designated account04/B11 partner result applied to an actual target inequality

The completed partner theorem says that if a physical triple has positive diagonal entries `a_i`, and normalized off-diagonals are within `eta<1/2` of a sign pattern whose triangle product is `-1`, then its smallest singular value is at least

`min_i a_i (1-2eta)`,                                            (6.1)

and the full ambient quadratic form has the target-level bound

`||p_Q||_infinity <= 6 sqrt(pi) / [min_i a_i (1-2eta)]`           (6.2)

on that branch (or the better partner Schur bound when available).

Apply this to the genuinely rotated indefinite physical triple

`H=(4/3)*[[1, 7/8, 7/8],
          [7/8, 1, -7/8],
          [7/8, -7/8, 1]].`                                      (6.3)

Its normalized off-diagonal magnitudes are exactly `7/8`, so `eta=1/8`, and the sign product is negative. Its eigenvalues are exactly

`{5/2,5/2,-1}`,                                                   (6.4)

so it already satisfies the owner's three-large-eigenvalue target. Here

`min_i a_i(1-2eta)=(4/3)*(3/4)=1`.                               (6.5)

Therefore the completed account04/B11 theorem gives the actual inequality

`boxed: ||p_(X^T H X)||_infinity <= 6 sqrt(pi)
       =10.6347231054...}`                                       (6.6)

for every three independent cap-one input laws. The same estimate survives arbitrary outside coordinates/couplings in the partner theorem's stated physical-triple scope. This removes the sign-frustrated complement before the balanced large-Delta bank problem is attacked.

## 7. Rank-two control and the third-direction mechanism

The mandatory control remains exact. If `X,Y` are independent `Uniform[-1/2,1/2]`, then for `0<|t|<1/2`,

`p_(2XY)(t)=log(1/(2|t|))`,                                      (7.1)

so an opposite-sign rank-two saddle is genuinely unbounded.

The new theorem identifies what a third indefinite direction looks like when no single physical minor carries it: substantial disjoint Plucker mass forces a *bank-level* middle spectral direction to have independent source mass on both sides of a cut, and in fact forces two spectral directions into each side. The rank-collapse control (5.7) shows the complementary possibility: if the cross interaction loses one rank, same-sign grouped self-curvature may carry the missing third direction. Thus the correct closure must route **either** collective cross curvature **or** grouped self-curvature, while preserving source banks; selecting one physical pair is not enough.

## 8. Connection to the newest analytic receiver and exact remaining implication

Account03/B01's completed `QFORM-RANK2-CROSS-BOUNDED-REMAINDER-L2-v1` says that if disjoint original-coordinate banks expose a rank-two cross matrix `K` with `Delta_K=s_1(K)s_2(K)` and a source-disjoint remainder of density cap `M`, then

`||p_Q||_infinity <= 2 sqrt(M) Delta_K^(-1/4)`,                   (8.1)

with a continuous `C_0` density. The new Theorem 3 supplies a dimension-free two-bank spectral certificate in every r24 large-disjoint-wedge branch, but Section 5 proves that it is invalid to infer the required rank-two cross `Delta_K` directly.

The first unpaid B11 implication is therefore sharpened to

`QFORM-TWO-BANK-BALANCE-CROSS-OR-SELF-RECEIVER-v1`:

> Given an exact-rank-three indefinite frame and a source bipartition with `sigma_2(R_S),sigma_2(R_T)>=1/32`, prove a dimension-free dichotomy: either a rank-two cross bicore can be routed to an independent already-paid bounded remainder, or the failure of cross second-volume forces quantitatively usable same-sign/null grouped self-curvature that is paid by the existing half-Riesz, grouped-square, cone-envelope, or ridge receivers.

Arbitrary additional spectrum remains a separate bridge because a tail may cancel an exact-rank-three component on physical blocks. The full conjecture is therefore still **OPEN / NOT PROVED / NOT DISPROVED**. The present theorem is structural; it does not by itself prove a new continuity statement for the full target.

## 9. Deterministic checks

The accompanying checker verifies:

- `Delta=1/64 -> Delta/16=1/1024 -> sigma_2>=1/32`;
- the explicit frame (5.1) has `R^T R=I_3`;
- its Plucker weights sum to three and give `Delta=1/9`;
- the cut cross block (5.6) has rank one;
- `A` has spectrum `{-1,0,1,1}`;
- the grouped-square control constant is `pi sqrt(2)`;
- the partner target triple (6.3) has spectrum `{-1,5/2,5/2}` and partner bound `6 sqrt(pi)`.

These checks support exact algebra only; no Monte Carlo evidence is used.
