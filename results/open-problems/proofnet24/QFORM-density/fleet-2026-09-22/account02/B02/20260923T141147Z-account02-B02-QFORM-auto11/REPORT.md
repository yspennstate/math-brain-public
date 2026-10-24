SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B02, 2026-09-23T14:11:47Z.
attacking: QFORM-SECONDANCHOR-LOWSTABLERANK-RECEIVER-v1 by combining physical-anchor Plancherel endpoints with D'/D5 sharp-Hausdorff--Young exterior-volume estimates and account03/B02 r30's heavy-anchor theorem.

# account02/B02 — anchor-volume geometric-mean L1 receivers

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Assignment:** Integrated Fourier estimate  
**Status:** ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN  
**Target-wide unweighted Fourier L1:** OPEN_NOT_REFUTED  
**Continuity:** proved on the new Fourier-L1 branches below; full-target continuity remains open.

The full target is unchanged: arbitrary independent real coordinates with probability densities at most one and arbitrary real symmetric A having at least three eigenvalues of modulus at least one. No moments, support bounds, log-concavity, iid assumption, diagonal-basis independence, or post-rotation independence is used.

## 1. Sources actually used

Required Claude package: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, files `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, `COUNTEREXAMPLE_SEARCH.md`.

Reviewed sharp-Hausdorff--Young continuation: `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba:proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`. Its degree-k argument gives, at q=2,

`|phi_Q(t)| <= min(1, e^(k/4) 2^(-k/8) pi^(k/4) E_k(M)^(-1/8) |t|^(-k/4))`       (1.1)

for every original-coordinate physical cross block M; arbitrary same-bank phases and outside couplings are retained. In particular k=5 is the reviewed D5 branch

`||p_Q||inf <= (5e/sqrt(2)) E5(M)^(-1/10)`.                                      (1.2)

Designated partner actually applied: `account03/B02` r30, canonical mathematics `yspennstate/math-open-problems@cb55a355bc5c623eb5a98c1db8a0ebaa58ff1027`. For a physical cross block B with `Z=E3(B)>0`, at q=4/3 the partner proves: either D' pays

`||p_Q||inf <= (9sqrt(3)e/2) Z^(-1/6)`,                                         (1.3)

with `phi_Q in L1`, or a physical row/column anchor pair has joint incident third-volume `J_ij>Z/3`.

The immediately preceding account02/B02 result `QFORM-HEAVYSTAR-STRIP-TO-DOUBLEANCHOR-v1`, canonical mathematics `yspennstate/math-open-problems@9a5b5b7ee3ec28d8f2fb9eaced2254ac050b5104`, sends the two-sided transport-failure branch to a fixed second physical anchor packet `G>Z/24`. If the second 2x2 anchor P is invertible, with `D=|det P|` and algebraic cross-Schur residual S,

`G=D^2 ||S||_F^2 > Z/24`.                                                         (1.4)

If P has rank one, choosing a genuinely nonzero scalar physical entry p and its scalar cross-Schur residual S1 gives

`H:=p^2 E2(S1) >= G > Z/24`.                                                       (1.5)

## 2. Physical-anchor Plancherel endpoints

If H,K are disjoint pairs of ORIGINAL coordinates and `P=A[H,K]` is invertible, `D=|det P|`, then for every `t!=0`,

`boxed: |phi_Q(t)| <= pi D^(-1/2) |t|^(-1).`                                      (2.1)

Condition on every original coordinate except the two row-anchor variables `x in R^2` and two column-anchor variables `y in R^2`. The conditional phase is `F(x)+2 x^T P y+G(y)` for arbitrary real F,G. Put `alpha(x)=f_H(x)e^(itF(x))` and `beta(y)=f_K(y)e^(itG(y))`. Since each original density has mass one and cap one, `||alpha||_2,||beta||_2<=1`. With `hat beta(xi)=int beta(y)e^(i xi.y)dy`, Cauchy--Schwarz, the change `xi=2tP^Tx`, and Plancherel give

`|int alpha(x) hat beta(2tP^Tx)dx| <= pi D^(-1/2)|t|^(-1)`.

The estimate is uniform in conditioning and survives averaging. Exactly the same proof for a nonzero scalar physical cross pivot p gives

`boxed: |phi_Q(t)| <= sqrt(pi) |p|^(-1/2)|t|^(-1/2).`                              (2.2)

These are bilinear product-source estimates, not the false law-uniform scalar quadratic stationary-phase bound.

## 3. Stable-rank cap packing for exterior volume

For nonnegative `x_j` with `T=sum x_j` and `rho=T/max_j x_j`, normalize `y_j=x_j/T`. Then `sum y_j=1`, `0<=y_j<=1/rho`. For fixed `y_i+y_j`, elementary symmetric `e_m(y)` is a concave quadratic in `y_i`:

`e_m(y)=y_i y_j e_(m-2)(rest)+(y_i+y_j)e_(m-1)(rest)+e_m(rest)`.

Thus a minimum on the capped simplex is attained after repeated pairwise pushes at a vertex: all but at most one coordinate are either zero or the cap `1/rho`.

For `m=3`, if `rho>2`,

`E3(S) >= c3(rho) ||S||_F^6`,                                                        (3.1)

where `c3(rho)=(rho-2)/rho^3` for `2<rho<=3`, and `c3(rho)=1/27` for `rho>=3`. In particular `rho>=5/2` implies `c3>=4/125`.

For `m=5`, if `rho>4`,

`E5(S) >= c5(rho) ||S||_F^10`,                                                       (3.2)

where `c5(rho)=(rho-4)/rho^5` for `4<rho<=5`, and `c5(rho)=1/3125` for `rho>=5`.

## 4. Main theorem — QFORM-ANCHOR-D5-GEOMEAN-L1-v1

Assume the invertible second-anchor branch (1.4). Let `rho=sr(S)>2`. Every 5x5 minor of B using the fixed 2x2 anchor and three residual rows/columns is `det(P)` times the corresponding 3x3 minor of S. Hence

`E5(B) >= D^2 E3(S) >= c3(rho) G^3/D^4`.                                           (4.1)

Insert (4.1) into the sharp-HY D5 pointwise estimate (1.1) at k=5:

`|phi_Q(t)| <= e^(5/4)2^(-5/8)pi^(5/4)c3(rho)^(-1/8)
               D^(1/2)G^(-3/8)|t|^(-5/4)`.                                         (4.2)

Combine (4.2) with (2.1). The elementary inequality `min(u,v)<=sqrt(uv)` cancels D exactly:

`boxed:
 |phi_Q(t)| <= min{1,
  e^(5/8)2^(-5/16)pi^(9/8)c3(rho)^(-1/16)
  G^(-3/16)|t|^(-9/8)}.
`                                                                                     (4.3)

Since `9/8>1`, Fourier inversion yields

`boxed:
 ||p_Q||inf <=9 e^(5/9)2^(-5/18)c3(rho)^(-1/18) G^(-1/6).
`                                                                                     (4.4)

If `rho>=5/2`,

`boxed: ||p_Q||inf <15.665527 G^(-1/6) <26.606039 Z^(-1/6).`                         (4.5)

The characteristic function is genuinely in L1, so the density has a continuous representative vanishing at infinity. The uncontrolled positive power of the anchor determinant in the preceding D5 density estimate has disappeared.

## 5. Singular second anchor — D5 criticality and a D6 exit

Assume (1.5). The scalar endpoint (2.2) has decay exponent 1/2. A scalar-pivot plus residual fourth exterior volume feeds D5, whose decay exponent is 5/4. The determinant powers cancel only at geometric weight 1/3 on (2.2), and then the time exponent is exactly `(1/3)(1/2)+(2/3)(5/4)=1`. Thus direct D5-plus-scalar-anchor interpolation is critical/nonintegrable; this is an obstruction to that receiver, not to QFORM or target-wide Fourier L1.

The same proved general degree-k sharp-HY calculation, now k=6, gives a genuine exit if `rho1=sr(S1)>4`. Every 6x6 minor using the scalar pivot and five residual rows/columns gives

`E6(B)>=p^2 E5(S1)`.                                                                (5.1)

By (3.2) and `E2(S1)<=||S1||_F^4/2`,

`E6(B)>=c5(rho1)2^(5/2)H^(5/2)|p|^(-3)`.                                           (5.2)

The k=6,q=2 pointwise sharp-HY estimate and (5.2) give

`|phi_Q(t)| <= e^(3/2)2^(-17/16)pi^(3/2)c5(rho1)^(-1/8)
               H^(-5/16)|p|^(3/8)|t|^(-3/2)`.                                      (5.3)

Take geometric weight `3/7` on (2.2) and `4/7` on (5.3); p cancels and the time exponent is `15/14>1`:

`|phi_Q(t)| <= min{1,
 pi^(15/14)e^(6/7)2^(-17/28)c5(rho1)^(-1/14)
 H^(-5/28)|t|^(-15/14)}`.                                                           (5.4)

Hence

`boxed:
 ||p_Q||inf <=15 e^(4/5)2^(-17/30)c5(rho1)^(-1/15) H^(-1/6).
`                                                                                     (5.5)

For `rho1>=5`,

`boxed: ||p_Q||inf <38.541906 H^(-1/6) <65.458853 Z^(-1/6).`                         (5.6)

Again `phi_Q in L1`, hence the density is continuous and C0 on this branch. This is a direct k=6 specialization of the same proved general degree-k sharp-HY argument; it is not represented as a separate independent review.

## 6. Combined live routing and remaining collar

Starting from a live physical block `B` with `Z=E3(B)>0`, the partner's q=4/3 theorem gives either the D' L1 bound (1.3) or a heavy incident anchor `J_ij>Z/3`. On the established two-sided transport-failure branch, account02/B02 r12 then gives a second physical anchor packet `>Z/24`.

This run pays:

1. invertible second anchor `G=D^2||S||_F^2>Z/24` whenever `sr(S)>=5/2`, by (4.5);
2. rank-one second anchor `H=p^2E2(S1)>Z/24` whenever `sr(S1)>=5`, by (5.6).

Together with the already-paid exact-rank-one invertible residual and exact-rank-two scalar-residual endpoints, the first unpaid implication becomes `QFORM-SECONDANCHOR-CRITICAL-STABLERANK-RECEIVER-v1`:

- invertible second anchor with `rank(S)>=2` and `sr(S)<5/2`, especially the near-rank-two/near-rank-one collar where `c3(rho)` degenerates as `rho downarrow2`;
- rank-one second anchor with `rank(S1)>=3` and `sr(S1)<5`;
- the separately tracked literal overlap case where the original fixed pivot shares a row or column with the partner heavy anchors.

A next receiver should spend the concentrated leading singular directions via a grouped hub/star or a TRUE symmetric Schur/pair mechanism while retaining every small transverse direction. Deleting those directions is not source-valid on arbitrary unbounded product inputs.

## 7. Correction boundary and checks

No refuted interface is used: no law-uniform pointwise quadratic-phase decay, no independence after spectral rotation or Schur shear, no arbitrary conditional-density cap, no arbitrary-joint coarea estimate, no fixed-good-minor inference, no pre-Schur-to-post-Schur transfer, and no small-matrix-tail deletion. The shears enter only through determinant identities; the actual Fourier estimates are performed on original-coordinate independent banks or after conditioning original coordinates.

No source-valid exact-target counterexample to `int_R |phi_Q(t)|dt<=C` was found. That target-wide stronger criterion remains OPEN / not refuted. The unrestricted bounded-density conjecture remains OPEN.

Constants: `15.665526723732583`, `26.606038105388244`, `38.541905462520745`, `65.4588526434027`. A deterministic capped-simplex stress check at rho in `{2.05,2.1,2.25,2.5,2.75,3,3.5,4,5,7}` found no violation of (3.1); this is diagnostic only, not the proof.
