SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B04, 2026-09-24T04:38:00Z.
attacking: the multicarrier face-collapse gap by an exact three-carrier entropy dual; then pay surviving pair-anchored fourth volume with the newest account03/B04 receiver on the same physical matrix.

# account02/B04 r19 — three-carrier cube dual and pair-E4 escape

Programme: `QFORM-DENSITY-3EIG-20260922`.
Role: Product Fourier rearrangement / complementary constructions.
Status: **NEW SUPPORTING THEOREM / GLOBAL PHYSICAL-WEIGHT OPTIMIZATION / PINNED D APPLIED / PARTNER r48 APPLIED / FULL QFORM OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner target is not proved here. The new step makes the previous “multicarrier face collapse” obstruction quantitative: three simultaneous heavy physical carriers admit an exact finite-dimensional entropy dual, and failure of the balanced third-volume currency forces every complementary pair of carrier faces to collapse. On a target-valid three-heavy-row family the entire D/D' weighted-volume problem can be solved globally, and the newest pair-anchored E4 receiver is then strictly stronger than ambient balancing on the identical physical matrix.

The early note `EARLY.md` had one arithmetic root error; immutable `CORRECTION.md` fixes it. The theorem and all calculations below use the corrected root.

## 1. Sources actually consumed

Fresh owner control came from `yspennstate/math-research-brain/main`, OWNER CONTROL revision `2026-09-22.15`, with the exclusive QFORM continuation and the later Fisher continuation. Full QFORM remains open and the live corrections against pointwise quadratic-phase decay, post-rotation independence and arbitrary-joint coarea remain binding.

The required pinned source was read at exactly

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`: `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. The completed result used below is Theorem D: for a literal physical crossing and any supported squared-minor weight whose constrained-side row marginals are at most `1/2`,

`||p_Q||_infinity <= 6 sqrt(e) G^(-1/6)`,

where

`G=exp(E_w log det(M_ST)^2 + H(w))`.

The D' proof in the same source gives the relaxed row-marginal window `h<3/4`; repeating the identical weighted AM-GM step with an arbitrary supported weight gives

`||p_Q||_infinity
 <= 6 sqrt(e) (2h)^(-1/2) (3-4h)^(-1) G^(-1/6)`.          (1.1)

The newest compatible designated partner is account03/B04 r48,

`yspennstate/math-open-problems@085560dcfb3b90238f3e84dd2de7d0e09bfa7525`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/20260924T041814Z-account03-B04-QFORM-auto11-r48/REPORT.md`.

Its theorem `QFORM-PAIR-ANCHORED-E4-PROMOTION-v1` says that for a literal physical row pair `{a,b}` in a cross block, with

`H_ab = sum_{|R|=4,{a,b} subset R} det Gram(M_R)`,

one has

`||p_Q||_infinity <= 2^(17/8) H_ab^(-1/8)`.                   (1.2)

This branch has an integrable characteristic function and hence a continuous `C_0` density. It preserves literal original-coordinate hubs and promotes heavy residual rows instead of assuming independence after any coefficient rotation.

For comparison I use the completed direct ridge theorem at `math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`, `interactive/20260922T151048Z-ridge-window/REPORT.md`.

## 2. New theorem — `QFORM-THREE-CARRIER-CUBE-DUAL-v1`

Let `M=A[I,J]` be a literal original-coordinate cross block. For a physical row triple `S` define its total squared-minor mass

`z_S = sum_{|T|=3} det(M[S,T])^2`.

Fix three distinguished physical rows

`H={a,b,c}`.

For every face `R subset H`, aggregate all physical third-volume mass with precisely that carrier intersection:

`W_R = sum_{S: S cap H = R} z_S`.                              (2.1)

Assume the face constraints below are feasible. Among all supported physical `3 x 3` minor laws for which each of the three carrier row marginals is exactly `1/2`, let `G_H` be the supremum of the determinant-entropy currency.

### Theorem

Define

`P(x_a,x_b,x_c)=sum_{R subset H} W_R prod_{i in R} x_i`.

Then

`boxed:
 G_H = inf_{x_a,x_b,x_c>0}
       P(x_a,x_b,x_c)/sqrt(x_a x_b x_c).`                      (2.2)

Moreover, pairing each face with its complement in the three-cube gives the universal lower bound

`boxed:
 G_H >= 2 sum_{R mod (R ~ H\R)} sqrt(W_R W_{H\R}).`            (2.3)

Thus if `G_H<g`, every complementary face product satisfies

`W_R W_{H\R} < (g/2)^2`.                                      (2.4)

### Proof

Index a physical minor by `(S,T)` and put `d_ST=det(M[S,T])^2`. For any supported law `w_ST`,

`log G(w)=sum_{S,T} w_ST log(d_ST/w_ST)`.                       (2.5)

Let `q_R` be the total probability of carrier face `R`. Apply log-sum separately inside each face:

`sum_{(S,T) in R} w_ST log(d_ST/w_ST)
 <= q_R log(W_R/q_R)`,                                         (2.6)

with equality exactly when the conditional law inside that face is proportional to `d_ST`. Consequently the full physical minor problem reduces *exactly*, not approximately, to

`max_q sum_R q_R log(W_R/q_R)`                                 (2.7)

subject to `sum_R q_R=1` and

`sum_{R contains i} q_R=1/2`, `i=a,b,c`.                       (2.8)

Lagrange multipliers give

`q_R = W_R x^R/P(x)`,                                          (2.9)

where `x^R=prod_{i in R}x_i`, and the three multipliers are chosen so that (2.8) holds. Substituting (2.9) into (2.7) gives

`log G_H = log P(x) - (1/2)sum_i log x_i`,                     (2.10)

which is the dual formula (2.2); boundary cases follow by the usual limiting argument.

For each complementary pair `(R,H\R)`, AM-GM gives

`W_R x^R + W_{H\R} x^(H\R)
 >= 2 sqrt(W_R W_{H\R}) sqrt(x_a x_b x_c)`.                   (2.11)

Summing the four disjoint complementary pairs and dividing by `sqrt(x_a x_b x_c)` proves (2.3) for every positive `x`, hence after the infimum. Equation (2.4) follows immediately. QED.

### Meaning for the live obstruction

The previous unpaid branch said that several physical E3 carriers can simultaneously be too heavy for the naive canonical minor law. Equation (2.3) identifies a precise currency that survives simultaneous balancing: if *any* opposite pair of carrier faces both carries substantial aggregate determinant mass, the balanced law cannot be poor. Therefore a genuinely bad three-carrier state must collapse all four opposite-face products at once. This is substantially sharper than saying merely that three canonical marginals are large.

No pointwise characteristic-function decay, coordinate rotation of the random inputs, or reciprocal of a selected local minor appears in this theorem.

## 3. A dense target-valid three-carrier family

Let `H_8` be the Sylvester Hadamard matrix and

`U = H_8[:,0:4]/sqrt(8)`,

so `U^T U=I_4`. Let

`V=(1/15) *
 [[14,-2,-3,-4],
  [-2,11,-6,-8],
  [-3,-6,6,-12],
  [-4,-8,-12,-1]]`.                                           (3.1)

Direct integer multiplication gives `V^T V=I_4`. For `L>0`, stack three literal heavy physical rows above the Walsh frame,

`R_L = [ L e_1 ; L e_2 ; L e_3 ; U ]`,                        (3.2)

and set

`M_L=R_L V^T`.                                                  (3.3)

The multiplication by `V` is purely a deterministic coefficient-space choice; no random coordinate is rotated. Every entry in the first three rows of `V` is nonzero, and every entry of `U V^T` is nonzero, so all `11*4=44` physical coefficients of `M_L` are nonzero.

Also

`M_L^T M_L` is orthogonally similar to

`diag(L^2+1,L^2+1,L^2+1,1)`.                                  (3.4)

Hence the pure-cross symmetric matrix

`A_L=[[0_11,M_L],[M_L^T,0_4]]`                                 (3.5)

has nonzero spectrum

`{ +/-sqrt(L^2+1) (three pairs), +/-1 }`.                       (3.6)

Thus it is genuinely non-diagonal in the physical independent coordinates, indefinite, and has eight eigenvalues of modulus at least one for every `L>0`.

## 4. Exact face masses and the globally optimal pinned-D weight

Take the three heavy rows as the carrier set `H`. Fix a carrier face `R` of size `r`. Schur/Gram elimination of the orthogonal heavy rows contributes `L^(2r)`. The remaining `k=3-r` light rows are measured after projection onto the `d=4-r` coefficient directions orthogonal to those carriers. Because `U` is Parseval, that projected light frame is again Parseval on a `d`-dimensional space, so its total `k`th squared volume is

`e_k(I_d)=binom(d,k)`.

Therefore every *specific* carrier face has mass

`W_R = L^(2r) binom(4-r,3-r)`,                                 (4.1)

namely

`W_empty=4`,
`W_single=3 L^2` for each of three singletons,
`W_double=2 L^4` for each of three doubletons,
`W_abc=L^6`.                                                    (4.2)

The unconstrained canonical E3 law has each heavy-row marginal

`q_can = L^2(L^2+3)/[(L^2+1)(L^2+4)]`.                         (4.3)

It exceeds `1/2` precisely when

`L^2 > y_0 := (sqrt(17)-1)/2`.                                 (4.4)

In this regime the global Theorem-D optimization has all three heavy constraints active. Indeed the determinant-entropy functional is strictly concave, the problem is invariant under carrier permutations, and if the common optimal marginal were below `1/2`, a small mixture toward the unique unconstrained canonical law would remain feasible while increasing the objective.

By symmetry put `x_a=x_b=x_c=x` and `y=L^2 x`. The dual polynomial is

`P(y)=4+9y+6y^2+y^3`.                                          (4.5)

The marginal equation is

`y P'(y)/P(y)=3/2`,                                             (4.6)

or

`y^3+2y^2-3y-4=0=(y+1)(y^2+y-4)`.                             (4.7)

Hence

`y_0=(sqrt(17)-1)/2=1.561552812808830...`.                     (4.8)

The exact global determinant-entropy currency at the pinned `1/2` cap is

`boxed:
 G_D(L)=C_3 L^3,
 C_3=P(y_0)/y_0^(3/2)
    =8(3+y_0)/y_0^(3/2)
    =18.7011226692076049... .`                                 (4.9)

The complementary-face theorem already gives

`G_D(L) >= (4+6sqrt(6))L^3
          =18.6969384566990686... L^3`,                        (4.10)

so the simple opposite-face lower bound misses the exact optimum by only `0.0224%` in this stress family.

The remaining physical row constraints are genuinely harmless. Conditional on a carrier face of size `r`, the canonical light `k=3-r` volume law has every Walsh row marginal

`(k/d)*(d/8)=k/8=(3-r)/8`.                                     (4.11)

The three carrier constraints force `E r=3/2`, so every one of the eight light physical rows has final marginal exactly

`3/16<1/2`.                                                     (4.12)

Thus (4.9) is not merely a carrier-face optimum: it is the **global optimum over all supported physical 3x3 minor weights satisfying every Theorem-D row cap**.

## 5. Required pinned e5 result applied at an actual inequality

Apply the completed pinned Theorem D to `A_L` with the globally optimal weight (4.9). For every independent input law with one-dimensional densities bounded by one,

`boxed:
 ||p_(X^T A_L X)||_infinity
 <= 6 sqrt(e) C_3^(-1/6) L^(-1/2).`                            (5.1)

At the concrete stress value `L=64`,

`E3(M_64)=68820176900`,
`q_can=4197376/4199425=0.999512076058...`,                      (5.2)

so the naive canonical Theorem-D law is drastically inadmissible, but the exact physical entropy rebalance gives

`boxed:
 ||p_(X^T A_64 X)||_infinity
 <=0.7589803948990746404... .`                                 (5.3)

This is the required equation-level application of the pinned `e5f71d...` result. It also exhibits a source-valid obstruction to treating a near-unit canonical carrier marginal as a hard branch: three such carriers can still be balanced at only geometric aggregate cost.

## 6. Global optimization over the full D/D' weighted-volume family

The relaxed D' window changes the optimum once `L` is large. Let every heavy carrier be capped by a common `h in [1/2,3/4)`. The same strict-concavity/symmetry argument makes all three caps active. Let `y=y(h)` be the unique positive solution of

`h = y P'(y)/(3P(y))`.                                         (6.1)

The exact determinant-entropy optimum over all supported physical minor weights is

`boxed:
 G_h(L)=P(y) (L^2/y)^(3h).`                                    (6.2)

Again every light-row marginal is

`3(1-h)/8 <=3/16`,                                              (6.3)

so no hidden physical row constraint appears.

Let `v(h)=log G_h(L)`. Envelope differentiation using (6.1) yields the exact identities

`v'(h)=6 log L -3 log y(h)`,
`v''(h)=-3 y'(h)/y(h)<0`.                                      (6.4)

For the weighted D' certificate

`B(h)=6 sqrt(e)(2h)^(-1/2)(3-4h)^(-1)G_h(L)^(-1/6)`,           (6.5)

one therefore has

`d/dh log B
 = -1/(2h)+4/(3-4h)-log L +(1/2)log y(h)`,                    (6.6)

and

`d^2/dh^2 log B
 =1/(2h^2)+16/(3-4h)^2 - v''(h)/6 >0`.                         (6.7)

Thus the global optimum is unique. At `h=1/2`, (6.6) equals

`3-log L +(1/2)log y_0`.                                       (6.8)

Consequently the original pinned cap `h=1/2` is globally optimal exactly up to

`L <= e^3 sqrt(y_0)=25.09931009503355...`;                     (6.9)

for larger `L`, the globally best D' certificate uses a strictly relaxed cap.

At `L=64`, the unique solution is

`y_*=1.8687620999555731096...`,
`h_*=0.5404201483179087172...`,                                (6.10)

with

`G_*=12596563.589915364...`,                                   (6.11)

and therefore

`boxed:
 ||p_(X^T A_64 X)||_infinity
 <=0.7441026652427036403... .`                                 (6.12)

This is the **global optimum over every supported physical third-minor weight and every proved D/D' exponent** for this matrix.

There is also a useful asymptotic separation. As `L->infinity`, the optimizer satisfies

`h_*=3/4 - 1/log L + O((log L)^(-2))`,                          (6.13)

because `y(h)->y_75=(3+sqrt(57))/2`. Hence

`B_DD'(L)=Theta((log L)L^(-3/4))`.                              (6.14)

The critical `h<3/4` singularity leaves a logarithmic price even after globally optimizing all ambient third-volume weights.

## 7. Fresh partner r48 applied on the identical physical matrix

Now retain the first two heavy physical rows as the pair anchor. Their Gram determinant is

`D_2=L^4`.                                                      (7.1)

After projecting off their span, the residual coefficient-space Gram has nonzero eigenvalues

`L^2+1, 1`: the third heavy row contributes `L^2` in the third coefficient direction, while the projected Walsh light frame contributes the identity on the two remaining directions. Therefore

`E2(C)=L^2+1`,                                                  (7.2)

and the exact pair-anchored fourth-volume mass is

`boxed:
 H_12=L^4(L^2+1).`                                              (7.3)

Apply the newest designated-partner theorem (1.2):

`boxed:
 ||p_(X^T A_L X)||_infinity
 <=2^(17/8) [L^4(L^2+1)]^(-1/8).`                              (7.4)

At `L=64`,

`H_12=68736253952`,                                             (7.5)

so

`boxed:
 ||p_(X^T A_64 X)||_infinity
 <=0.1927704709163505763... .`                                 (7.6)

This is a positive application of fresh account03/B04 r48 at its actual aggregate hypothesis, not merely a citation. The partner branch gives a continuous `C_0` density for this displayed family.

Asymptotically, (7.4) is

`2^(17/8)L^(-3/4)(1+O(L^-2))`,                                 (7.7)

so physical pair promotion removes the logarithm in (6.14). This is the mechanism change requested by the live role: once ambient entropy balancing is pushed against its critical marginal boundary, retaining a literal physical pair as a Fourier hub is quantitatively superior.

## 8. Direct ridge comparison on the same crossing

Put `g=gamma^2` and `a=L^2+1`. On the 11-row side, the three heavy physical ridge leverages are

`k_c=L^2/(a+g)`,                                                (8.1)

while every Walsh light row has leverage

`k_l=(1/8)[3/(a+g)+1/(1+g)]`.                                  (8.2)

The ridge trace is

`theta=3a/(a+g)+1/(1+g)`.                                      (8.3)

For the relevant range `k_c>k_l`, choose the smallest admissible Fourier exponent

`q=2k_c`.                                                       (8.4)

Then the strict integrability gap simplifies exactly to

`theta-2q
 = (3-L^2)/(a+g)+1/(1+g)
 = [4-g(L^2-4)]/[(a+g)(1+g)]`.                                 (8.5)

Thus the direct left-ridge gate can hold only in the very narrow window

`g<4/(L^2-4)` for `L>2`.                                       (8.6)

At `L=64`, take the explicit valid scale

`g=64^-8=3.552713678800501e-15`,                               (8.7)

and `q=2k_c`. The determinant-retaining completed ridge theorem gives

`boxed:
 ||p_(X^T A_64 X)||_infinity
 <=246.09836120764675... .`                                    (8.8)

As `g downarrow0`, this displayed ridge expression tends

`e(L^2+1)^(9/8)/(2L)=246.09836120675503...`;                    (8.9)

no claim of global ridge optimality over positive `g` is needed here.

The transposed four-row ridge orientation is worse in a structural sense: for every positive semidefinite four-by-four ridge operator, `max_i K_ii >= tr(K)/4`. The leverage gate forces `q>=2 max_i K_ii >=theta/2`, contradicting the strict requirement `theta>2q`. Hence **the transposed direct-ridge gate is impossible at every regularization scale** on this four-coordinate side.

For reference, the pinned D5 theorem has no finite certificate on this same natural crossing because `rank M_L=4`, hence `E5(M_L)=0`. This is only an obstruction to D5 on this crossing, not a statement about every possible physical cut of the full symmetric matrix.

## 9. Same-matrix comparison and structural lesson

At `L=64` the certified bounds obtained here are

`0.192770471   fresh pair-anchored E4 promotion (account03/B04 r48)`,
`0.744102666   globally optimized weighted D/D'`,
`0.758980395   globally optimized pinned Theorem D at h=1/2`,
`246.098362    displayed direct left-ridge certificate`,          (9.1)

while the transposed direct-ridge gate is impossible.

The important conclusion is not the numerical ordering itself. Three simultaneous near-unit canonical E3 carrier marginals do **not** define the hard branch. Exact product-space entropy balancing reduces the entire physical minor problem to a three-cube partition function, and the complementary-face inequality says that poor balanced currency requires four simultaneous opposite-face collapses. When a physical pair nevertheless carries fourth exterior volume, fresh partner r48 spends that aggregate directly and removes the critical D' logarithm.

This uses rearrangement/product-space determinant entropy and physical hub promotion throughout. It never uses false pointwise quadratic-phase decay or independence of post-rotation coordinates.

## 10. First unpaid implication

The first unpaid step is now

`QFORM-THREE-CARRIER-COMPLEMENT-COLLAPSE-PLUS-PAIR-E4-COLLAPSE-TO-C2-v1`.

Starting from the surviving high-leverage/small-`s3` zero-anchor `C1` residual, produce a literal original-coordinate crossing and a set of at most three heavy E3 carriers. Then:

1. if the three-cube complementary-face currency in (2.3) is target-scale and the remaining physical row marginals are admissible, pay it by pinned D / weighted D';
2. if any literal physical row pair has target-scale pair-anchored E4 mass `H_ab`, pay it by account03/B04 r48;
3. otherwise, use the simultaneous collapse of all complementary E3 face products *and* all pair-anchored E4 masses to force the target compound mass into an already-paid overlap-`C2/C3`, rank-two star, fixed-pair/hyperbolic, square-bank, grouped-hub, or ridge receiver.

The missing implication in item 3 is the real structural residue. It must aggregate before reciprocals, preserve original-coordinate product provenance, and may not delete a nonzero rough quadratic tail as a perturbation.

## 11. Deterministic audit

`CHECKS.py` verifies with no external packages:
- `V^T V=I` by exact integer arithmetic;
- all 44 physical cross coefficients are nonzero;
- the corrected half-cap stationary root and complementary-face lower constant;
- the exact `E3`, `E4`, `H12` and canonical heavy marginal at `L=64`;
- the unique D' optimum by bisection of (6.6);
- the partner r48 bound;
- ridge admissibility and the displayed ridge constant.

The committed output marker is

`QFORM_B04_R19_THREE_CARRIER_CUBE_CHECK_PASS`.

No Monte Carlo evidence, FEI, installation, benchmark or external paid computation was used.

## 12. Scope

This run proves a supporting entropy-dual theorem and a quantitative route separation on a target-valid family; it does **not** derive the needed carrier/pair structure from the bare three-large-eigenvalue hypothesis. Therefore the unrestricted QFORM conjecture remains **OPEN**. Continuity is asserted only for the displayed branches whose completed Fourier proofs give an integrable characteristic function; no unrestricted continuity claim is made.