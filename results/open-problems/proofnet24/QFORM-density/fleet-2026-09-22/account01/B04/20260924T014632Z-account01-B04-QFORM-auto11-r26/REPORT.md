SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-24T01:46:32Z.
attacking: replace range-leverage collision by canonical third-compound energy collision, so large physical leverage carried only by spectrally tiny directions no longer blocks the disjoint-E3 product-Fourier route.

# account01/B04 r26 — energy-weighted third-compound collision

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Status: **NEW SUPPORTING THEOREM / STRICT REFINEMENT OF r25 DISJOINT-E3 ROUTE / DESIGNATED PARTNER APPLIED / FULL TARGET OPEN**  
Continuity: the new paid branch has a continuous `C_0` density; the unrestricted continuity statement remains open.  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture is not proved here. Every random variable remains an original physical product coordinate. No moment/support/log-concavity/Gaussian assumption, no post-rotation independence, no arbitrary-joint coarea estimate, no fiber-supremum shortcut, and no law-uniform pointwise quadratic-phase decay is used.

## 1. Fresh sources and the first missing implication


The analytic receiver used below is the completed marginal-free cross-third-volume theorem

`QFORM-CROSS-E3-OPTIMAL-THRESHOLD-v1`

from

`yspennstate/math-open-problems@563bc41e4f9247f9daf3343a57757f45e3f6e703`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/20260923T215155Z-account03-B04-QFORM-auto11-r42/REPORT.md`.

For every literal original-coordinate cross block `M`, with arbitrary same-bank quadratic terms and induced affine terms,

`||p_Q||_infinity <= C_* E_3(M)^(-1/6)`,                           (1.1)

where

`C_*=8.45302122552817687470491804598...`,                         (1.2)

and the characteristic function is in `L^1`, hence `p_Q in C_0(R)`.

The designated account02/B04 result actually applied in Section 7 is

`QFORM-FRACTIONAL-SUPPORT-DEFECT-COMPLETE-EXIT-v1`,

source

`yspennstate/math-open-problems@00e728cf7f226ccce4b41ad751d494c5c94f67ec`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/20260923T111930Z-account02-B04-qform/REPORT.md`.

For a physical cross block with exactly three active row coordinates and `E_3(M)=Z>0`, its exact-rank-three branch gives

`||p_Q||_infinity <=6 Z^(-1/6)`                                   (1.3)

with a continuous `C_0` density. The newer account02/B04 r16 report was also read; its C1 zero-anchor paving theorem is scope-specific and is not silently applied to the generic matrix below.

The preceding account01/B04 r25 theorem used the range-leverage collision

`tau=sum_i ell_i^2`,                                               (1.4)

and proved

`Delta_3^disj(S)>=(1-tau)e_3(S^2)`.                               (1.5)

This is useless when `tau>=1`, even if the high-leverage physical directions belong only to tiny singular values. The first essential implication attempted here is to replace `tau` by a third-compound **energy-weighted** collision that ignores such spectrally irrelevant range directions.

## 2. Canonical third-compound energy marginals

Let

`S=S^T=U Lambda U^T`, `U^T U=I_r`, `r>=3`,                        (2.1)

and put

`C_3(S)=wedge^3 S = W D W^T`,
`W=wedge^3 U`, `D=wedge^3 Lambda`.                                (2.2)

Write

`E=||C_3(S)||_F^2=e_3(S^2)>0`.                                   (2.3)

For each physical coordinate `i`, let `P_i` be the coordinate projection in `wedge^3 R^n` onto basis wedges containing `i`. Define

`ell_i=(P_range(S))_ii=||U^T e_i||^2`,                            (2.4)

and define the **canonical third-compound energy marginal**

`mu_i=E^(-1)||C_3(S) P_i||_F^2
    =E^(-1) tr(P_i C_3(S)^2).`                                   (2.5)

Equivalently, if one puts the canonical squared-minor probability law

`q(R,T)=det(S[R,T])^2/E`, `|R|=|T|=3`,                            (2.6)

then, because `S` is symmetric,

`mu_i=P_q(i in R)=P_q(i in T)`.                                  (2.7)

Thus `mu_i` measures where the **third-compound energy** actually lives, whereas `ell_i` measures the entire nonzero range, including arbitrarily weak singular directions.

Two elementary identities are immediate:

`sum_i mu_i=3`,                                                    (2.8)

and

`0<=mu_i<=ell_i<=1`.                                               (2.9)

For (2.8), use `sum_i P_i=3I` on third exterior power. For (2.9), note that the contraction argument from r25 gives

`||P_i W||_op^2<=ell_i`,                                          (2.10)

hence `H_i=W^T P_i W<=ell_i I`; then

`mu_i=tr(D^2 H_i)/tr(D^2)<=ell_i`.                                (2.11)

Define the new collision currency

`boxed: chi_3(S)=sum_i ell_i mu_i.`                               (2.12)

By (2.9),

`chi_3(S)<=sum_i ell_i^2=tau`,                                    (2.13)

so every old r25 certificate is retained, while a strict improvement is possible.

There is also a basis-free physical formula. Under the canonical law (2.6), `mu_i` is exactly the row/column inclusion marginal, so `chi_3` can be computed directly from physical squared-minor energy and the range projector without choosing eigenvectors inside repeated eigenspaces.

## 3. New theorem: energy-weighted disjoint third-compound mass

### Theorem `QFORM-ENERGY-WEIGHTED-THIRDCOMPOUND-COLLISION-v1`

With the notation above,

`boxed:
 Delta_3^disj(S)
 >=(1-chi_3(S)) e_3(S^2),`                                       (3.1)

where

`Delta_3^disj(S)
 =sum_(|R|=|T|=3, R intersect T=empty) det(S[R,T])^2`.            (3.2)

Hence the conclusion is useful whenever `chi_3(S)<1`, even if the old range collision `tau` is larger than one.

### Proof

Let `O` be the overlap energy, the sum of `det(S[R,T])^2` over `R intersect T!=empty`. Union-bound the overlap event by a shared physical coordinate:

`O<=sum_i ||P_i C_3(S) P_i||_F^2`.                               (3.3)

For one coordinate, using `C_3(S)=W D W^T`,

`P_i C_3(S)P_i=(P_i W)(D W^T P_i)`.                              (3.4)

Therefore

`||P_i C_3(S)P_i||_F^2
 <=||P_i W||_op^2 ||D W^T P_i||_F^2`.                            (3.5)

The first factor is at most `ell_i` by (2.10). The second factor is exactly

`||D W^T P_i||_F^2
 =tr(P_i W D^2 W^T P_i)
 =tr(P_i C_3(S)^2)
 =mu_i E`.                                                        (3.6)

Thus

`||P_i C_3(S)P_i||_F^2<=ell_i mu_i E`.                           (3.7)

Summing (3.7) in (3.3) gives

`O<=chi_3(S)E`.                                                    (3.8)

Since `Delta_3^disj=E-O`, (3.1) follows. QED.

This proof is a product-coordinate exterior-power estimate. It contains no oscillatory pointwise bound and no rotation of the random variables.

### Spectral formula for `mu_i`

For a spectral triple `K subset {1,...,r}`, put

`d_K^2=product_(k in K) lambda_k^2`,
`ell_i(K)=sum_(k in K) u_ik^2`.                                  (3.9)

Then

`boxed:
 mu_i = [sum_(|K|=3) d_K^2 ell_i(K)]/E.`                         (3.10)

Indeed `||P_i W e_K||^2=ell_i(K)` for the unit decomposable wedge associated with the three-dimensional spectral subspace `K`.

If all nonzero singular values of `S` have the same magnitude and `rank(S)=r`, then the spectral triples are equally weighted and

`mu_i=(3/r)ell_i`,
`chi_3=(3/r)sum_i ell_i^2`.                                       (3.11)

Thus even in the equal-singular-value case the new collision can improve the previous range collision by the factor `3/r`.

## 4. Random cut and density consequence

Color the physical coordinates independently into labelled banks `I,J` with probability `1/2`. Every ordered **disjoint** pair of triples lands with `R subset I`, `T subset J` with probability `2^-6=1/64`. Hence

`E_cut E_3(S[I,J])=Delta_3^disj(S)/64`.                           (4.1)

By Theorem 3.1, some literal original-coordinate cut satisfies

`boxed:
 E_3(S[I,J])
 >=(1-chi_3(S))e_3(S^2)/64.`                                    (4.2)

Apply the completed marginal-free cross-E3 receiver (1.1).

### Theorem `QFORM-ENERGY-COLLISION-CROSS-E3-v1`

Suppose a full ambient quadratic form contains a physical coordinate bank `K` whose coefficient block `C` has the same off-diagonal entries as a symmetric carrier `S` on `K` (in particular `S=C` or `S=off(C)`). If `e_3(S^2)>0` and `chi_3(S)<1`, then

`boxed:
 ||p_Q||_infinity
 <=2 C_* (1-chi_3(S))^(-1/6)e_3(S^2)^(-1/6),`                    (4.3)

and

`boxed: p_Q in C_0(R).}`                                         (4.4)

### Proof

Condition on all original coordinates outside `K`; the retained coordinates remain independent with scalar density caps at most one, and all outside couplings become affine terms. Choose the deterministic cut from (4.2). Because `C-S` is diagonal, the actual physical crossing equals `S[I,J]`. Apply (1.1) and (4.2), uniformly in the conditioned affine terms. The source theorem has an `L^1` characteristic-function majorant at this fixed crossing scale, so averaging the conditioned characteristic functions preserves `L^1` and yields (4.4). QED.

By (2.13), this theorem strictly contains r25's collision-leverage theorem whenever the latter applies.

## 5. Stable-rank corollary and the current small-pair branch

The stable-rank estimate from r25 remains valid:

if

`rho=||S||_F^2/||S||_op^2>=3`,                                   (5.1)

then

`e_3(S^2)>=||S||_F^6/27`.                                        (5.2)

Combining with (4.3),

`boxed:
 ||p_Q||_infinity
 <=[2 C_* 27^(1/6)/||S||_F](1-chi_3(S))^(-1/6).`                 (5.3)

In particular

`chi_3(S)<=1/2`

implies

`boxed:
 ||p_Q||_infinity
 <=2 C_* 54^(1/6)/||S||_F.`                                      (5.4)

Therefore, in the current localized overlap-two small-pair branch, where r24 forces

`||off(C)||_F>=512/15`,                                           (5.5)

the whole complement-curvature subbranch is paid by

`boxed:
 ||p_Q||_infinity
 <=0.9629318385596067...,
 p_Q in C_0(R),}`                                                  (5.6)

whenever

`stable-rank(off(C))>=3`

and

`chi_3(off(C))<=1/2`.                                             (5.7)

This strictly weakens the r25 hypothesis `sum_i ell_i^2<=1/2`: high physical leverage carried only by weak singular directions is now harmless.

The first remaining implication for this route is

`QFORM-SMALLPAIR-LOW-STABLERANK-OR-HIGH-ENERGY-COLLISION-ROUTING-v1`:

> in the small-pair overlap-two state, route either `stable-rank(off(C))<3` or `chi_3(off(C))>1/2` into the completed rank-two rough-curvature, grouped-hub, pair, ridge, projected-crossing, square-bank, or mixed-volume mechanisms without deleting nonzero random curvature or paying an arbitrarily small local coefficient.

This is strictly sharper than the preceding `tau>1/2` remainder.

## 6. Fully dense genuinely rotated indefinite stress matrix outside the old collision gate

Use 64 physical rows indexed by `x in F_2^6` plus one additional row `h`. Let

`chi_0(x)=1`,
`chi_1(x)=(-1)^(x_1)`,
`chi_2(x)=(-1)^(x_2)`,
`chi_3(x)=(-1)^(x_3)`.                                            (6.1)

Define the `65 x 4` orthonormal frame `U` by

`u_x=(chi_0(x)/8, chi_1(x)/8, chi_2(x)/8, chi_3(x)/32)`,          (6.2)

`u_h=(0,0,0,sqrt(15)/4)`.                                        (6.3)

Walsh orthogonality gives `U^T U=I_4`. Put

`Lambda=diag(2,3,-4,1/10)`,
`A_*=U Lambda U^T`.                                                (6.4)

Its nonzero spectrum is exactly

`{3,2,1/10,-4}`,                                                   (6.5)

so it is indefinite and has three eigenvalues of modulus at least one.

It is also physically **fully dense**. For two Walsh rows,

`(A_*)_(xy)
 =[2+3 chi_1(x)chi_1(y)-4 chi_2(x)chi_2(y)]/64
  +chi_3(x)chi_3(y)/10240`.                                      (6.6)

The first numerator is an odd nonzero integer, hence has magnitude at least one, while the final perturbation has magnitude `1/10240<1/64`; thus every Walsh-Walsh entry is nonzero. Further,

`(A_*)_(xh)=sqrt(15) chi_3(x)/1280 !=0`,
`(A_*)_(hh)=3/32`.                                                 (6.7)

So every physical matrix entry is nonzero.

The range leverage scores are

`ell_x=49/1024` for all 64 Walsh rows,
`ell_h=15/16`.                                                     (6.8)

Consequently the old r25 collision parameter is

`tau=64(49/1024)^2+(15/16)^2
    =16801/16384
    =1.02545166015625>1`.                                        (6.9)

Thus r25's bound `(1-tau)e_3` is negative and gives **no certificate at all** on this matrix.

The third-compound energy is

`E=e_3(A_*^2)
 =576+61/25
 =14461/25
 =578.44`.                                                        (6.10)

For the dominant spectral triple `{1,2,3}`,

`sum_i ell_i ell_i({1,2,3})=147/1024`.                            (6.11)

For each of the three spectral triples containing direction four,

`sum_i ell_i ell_i(K)=16017/16384`.                               (6.12)

Their total squared spectral weight is `61/25`. Therefore (3.10) gives the exact energy collision

`boxed:
 chi_3(A_*)
 =34845837/236929024
 =0.1470728930196412... .}`                                       (6.13)

Hence

`(1-chi_3)E
 =202083187/409600
 =493.36715576171875...`,                                         (6.14)

and some physical cut has

`E_3(A_*[I,J])
 >=202083187/26214400
 =7.708861808776856... .`                                        (6.15)

The new theorem therefore gives, for **every** admissible independent cap-one product input law,

`boxed:
 ||p_(X^T A_* X)||_infinity
 <= C_* (202083187/26214400)^(-1/6)
 =6.014233001847459...,
 p in C_0(R).}`                                                    (6.16)

This is a literal example where the old range-collision theorem is silent (`tau>1`) but the energy-weighted compound collision is strongly diffuse (`chi_3<0.15`).

## 7. Designated account02/B04 theorem applied to the same matrix

Take the three physical Walsh rows

`x^(1)=(0,0,0,0,0,0)`,
`x^(2)=(0,1,0,0,0,0)`,
`x^(3)=(1,0,0,0,0,0)`                                             (7.1)

as the left bank `I`, and let `J` be the remaining 62 Walsh rows plus `h`. The `3 x 4` spectral-frame restriction is

`U_I=
 [[1/8,  1/8,  1/8, 1/32],
  [1/8,  1/8, -1/8, 1/32],
  [1/8, -1/8,  1/8, 1/32]].`                                     (7.2)

For the actual physical crossing `M=A_*[I,J]`, orthonormality gives

`MM^T
 =U_I Lambda (I-U_I^T U_I) Lambda U_I^T`                         (7.3)

and exact arithmetic yields

`MM^T=(1/104857600)*
 [[ 44773821, -4993859,  17587581],
  [ -4993859, 45180861, -33408899],
  [ 17587581,-33408899,  46618941]],`                             (7.4)

with

`boxed:
 E_3(M)=det(MM^T)
 =522470223/17179869184
 =0.0304117695777677...>0.}`                                      (7.5)

Because the row bank has exactly three coordinates, every supported third minor contains all three rows; this is the coloop support-defect branch of account02/B04's completed theorem (1.3). Applying it at the actual inequality gives

`boxed:
 ||p_(X^T A_* X)||_infinity
 <=6(522470223/17179869184)^(-1/6)
 =10.739341066112344...,
 p in C_0(R).}`                                                    (7.6)

Thus, on the **same fully dense rotated indefinite target**, the new energy-collision aggregate certificate (6.16) improves this completed account02/B04 certificate by the factor

`10.739341066112344 / 6.014233001847459
 =1.785654307509107... .`                                        (7.7)

The comparison is not a claim that the partner theorem is globally optimized over all three-row selections. Its purpose is equation-level application of a completed designated-partner result and a concrete demonstration of aggregate-before-localization gain.

## 8. What was and was not proved

Proved in this run:

1. the invariant canonical third-compound marginal `mu_i` and `chi_3=sum ell_i mu_i`;
2. `Delta_3^disj(S)>=(1-chi_3)e_3(S^2)`;
3. the resulting marginal-free product-Fourier density bound (4.3), with `C_0` regularity;
4. a strict improvement of the current small-pair complement-curvature condition from range collision to energy collision;
5. a fully dense target-valid matrix with `tau>1` on which the new theorem gives `6.014234` while the old r25 collision theorem gives no certificate;
6. an actual same-matrix application of the completed account02/B04 support-defect theorem.

Not proved:

- the unrestricted three-large-eigenvalue conjecture;
- a universal reason that `chi_3<=1/2` in the remaining small-pair state;
- the low-stable-rank/high-energy-collision routing implication stated after (5.7).

The next B04 mechanism should attack the **energy-collision**, not range-collision, obstruction. In particular, a large physical leverage score is not itself a problem if its spectral directions contribute negligibly to third-compound energy.
