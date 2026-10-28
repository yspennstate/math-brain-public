SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-24T00:15:09Z.
attacking: the freshly localized overlap-two branch from account03/B20; use the fixed-pair aggregate Fourier receiver before any local-minor inversion, and identify the exact residual small-pair currencies when that receiver cannot fire.

# account01/B04 r24 — local overlap-two off-diagonal exit and small-pair numerator dichotomy

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Status: **NEW TARGET-LEVEL PARTIAL PAYMENT + NEW STRUCTURAL DICHOTOMY / FULL TARGET OPEN**  
Continuity: the density-payment branch below proves essential boundedness only; the square-root small-ball branch does not by itself prove existence of a bounded density.  
Independent review: pending.  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

The full conjecture is not proved here. Every random variable remains an original physical product coordinate. No moment, compact-support, log-concavity, connected-support, Gaussian, post-rotation-independence, arbitrary-joint coarea, conditional-density-cap, or law-uniform pointwise quadratic-phase estimate is used.

## 1. Fresh source boundary


Two completed inputs are used exactly at their proved scope.

### Input A: localized third-compound overlap funnel

account03/B20 r42, source

`yspennstate/math-open-problems@7e9f6e73f1f1f5304cc30a6204caf7ee0629904a`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260923T234606Z-account03-B20-QFORM-r42/REPORT.md`

proves that under the bare target hypothesis `s_3(A)>=1`, every unpaid state after its first three completed branches satisfies

`max_i |A_ii| < 1/64`                                              (1.1)

and either a fixed physical pair `S` has

`J_2(S) >= 1/144`,                                                  (1.2)

or the separate localized overlap-one alternative occurs. Here

`J_2(S)
 = sum_(|I|=|J|=3, I intersect J=S) det A[I,J]^2`.                (1.3)

This run attacks (1.1)--(1.2).

### Input B: fixed indefinite pair, aggregate overlap-two receiver

This worker's preceding r23 theorem, source

`yspennstate/math-open-problems@da10ec9c10ed601095b763a3df3128ab7e400ac5`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B04/20260923T235358Z-account01-B04-QFORM-auto11-r23/REPORT.md`

proves: for a physical pair `S`, if `B=A[S,S]` is invertible indefinite, `kappa=sigma_min(B)`, and `J_2(S)>0`, then

`||p_Q||_infinity
 <= C_ov2 [kappa^2 J_2(S)]^(-1/8)`,                               (1.4)

where

`C_ov2
 =2^(25/8) exp(1/8) sqrt(Gamma(1/4))
 =18.82331388097627... .`                                         (1.5)

The proof random-cuts the entire exact pair-Schur overlap-two packet into first-compound product-Fourier energy. It does not select an individual residual coefficient. Essential boundedness is proved; continuity was not claimed.

## 2. First new theorem: the localized overlap-two branch is paid when the shared off-diagonal is not tiny

### Theorem `QFORM-LOCAL-OVERLAP2-OFFDIAGONAL-EXIT-v1`

Let `delta>0`. Suppose a symmetric physical matrix `A` has a pair

`S={r,s}`

such that

`|A_rr|<=delta`, `|A_ss|<=delta`,                                  (2.1)

`J_2(S)>=j>0`,                                                      (2.2)

and

`|A_rs|>=2 delta`.                                                  (2.3)

Then the quadratic form has a density satisfying

`boxed:
 ||p_Q||_infinity
 <= C_ov2 (delta^2 j)^(-1/8).`                                     (2.4)

No condition is imposed on any other entry of `A`, on its rank, on signs outside `S`, or on additional spectrum.

#### Proof

Write

`B=A[S,S]=[[a,c],[c,b]]`,
`m=(a+b)/2`,
`r0=sqrt(((a-b)/2)^2+c^2)`.                                       (2.5)

The two eigenvalues of `B` are `m+r0` and `m-r0`. By (2.1),

`|m|<=delta`,                                                      (2.6)

while (2.3) gives

`r0>=|c|>=2delta`.                                                 (2.7)

Thus the eigenvalues have opposite signs and

`kappa=sigma_min(B)=r0-|m|
 >=|c|-delta
 >=delta`.                                                         (2.8)

Apply the fixed-pair receiver (1.4) and use (2.2), (2.8):

`||p_Q||_infinity
 <=C_ov2 [kappa^2 J_2(S)]^(-1/8)
 <=C_ov2 [delta^2 j]^(-1/8)`.                                     (2.9)

QED.

### Target-level numerical corollary

In the exact remaining branch from account03/B20 r42,

`delta=1/64`, `j=1/144`.                                           (2.10)

Therefore if its localized pair satisfies

`|A_rs|>=1/32`,                                                     (2.11)

then

`boxed:
 ||p_Q||_infinity
 <= C_ov2 * 589824^(1/8)
 =99.09149694560317... .}`                                         (2.12)

So the overlap-two debt in the current global compiler is reduced to a fixed pair whose **entire physical 2x2 block is small**:

`|A_rr|,|A_ss|<1/64`, `|A_rs|<1/32`, `J_2(S)>=1/144`.              (2.13)

This removes the non-small shared-off-diagonal sector uniformly, without a scalar-pivot loss.

## 3. Exact polynomial identity in the remaining small-pair sector

Now take an arbitrary physical pair `S` and put

`K=[n]\\S`,
`B=A[S,S]=[[a,c],[c,b]]`,
`U=A[S,K]`,
`C=A[K,K]`,
`G=adj(B)=[[b,-c],[-c,a]]`.                                        (3.1)

For `i,j in K`, let `u_i` be the `i`th column of `U`. The exact 3-by-3 determinant identity, valid **without assuming B invertible**, is

`det A[S union {i}, S union {j}]
 = det(B) C_ij - u_i^T G u_j`.                                    (3.2)

It is simply the polynomial block-determinant expansion of

`[[B,u_j],[u_i^T,C_ij]]`.                                          (3.3)

Because overlap exactly two means `i!=j`, define `off(M)` by zeroing a matrix diagonal. Then

`boxed:
 J_2(S)
 = || off( det(B) C - U^T G U ) ||_F^2.`                           (3.4)

Unlike a Schur-complement identity, (3.4) remains valid at the singular-pair endpoint `det B=0`.

## 4. Second new theorem: small-pair numerator dichotomy

### Theorem `QFORM-SMALL-PAIR-NUMERATOR-DICHOTOMY-v1`

Assume

`|a|,|b|<=delta`, `|c|<=2delta`,                                   (4.1)

and `J_2(S)>=j>0`. Then at least one of

`boxed:
 ||off(C)||_F >= sqrt(j)/(10 delta^2)`,                             (4.2)

or

`boxed:
 ||U||_F^2 >= sqrt(j)/(6 delta)`                                   (4.3)

holds.

#### Proof

From (4.1),

`|det B|=|ab-c^2|
 <=|ab|+c^2
 <=5delta^2`.                                                      (4.4)

Also, because `G` is symmetric,

`||G||_op
 <=max row-sum(G)
 <=3delta`.                                                        (4.5)

Taking square roots in (3.4), using the triangle inequality, and then

`||U^T G U||_F <= ||G||_op ||U||_F^2`,                             (4.6)

gives

`sqrt(j)
 <= sqrt(J_2(S))
 <=5delta^2 ||off(C)||_F +3delta ||U||_F^2`.                       (4.7)

If both (4.2) and (4.3) failed, the two terms on the right of (4.7) would each be `<sqrt(j)/2`, contradiction. QED.

### Exact target constants

For the unpaid target values (2.10), the theorem becomes

`boxed:
 ||off(C)||_F >= 512/15 =34.133333...`                             (4.8)

or

`boxed:
 ||U||_F^2 >= 8/9.`                                                (4.9)

Thus the small-pair overlap-two branch cannot hide in a completely weak neighborhood. It forces either a very large off-diagonal curvature packet on the complement or an order-one aggregate coupling from the shared pair to the complement.

## 5. Product-Fourier consequence: every remaining small-pair state already has a universal square-root small-ball certificate

The first-compound product-Fourier theorem from this worker's r20 gives, for any literal original-coordinate crossing block `N` with

`Z_1=||N||_F^2>0`,

`sup_t P(|Q-t|<rho)
 <=H_1 Z_1^(-1/4) sqrt(rho)`,                                      (5.1)

uniformly over arbitrary same-bank quadratic curvature and affine terms, with

`H_1=2^(3/4) exp(1/4) Gamma(1/4)
    =7.829376757708329... .`                                       (5.2)

This does **not** itself yield bounded density; it is recorded as the exact half-Riesz currency available for the next splice.

### 5.1 Coupling-heavy branch

If (4.9) holds, use the literal physical cut `S | K`. Its crossing matrix is exactly `U`, so

`Z_1>=8/9`.                                                        (5.3)

Hence the full quadratic form satisfies

`boxed:
 sup_t P(|Q-t|<rho)
 <=8.063346501398827... sqrt(rho).}`                               (5.4)

### 5.2 Complement-curvature branch

If (4.8) holds, independently color the coordinates of `K` into labelled banks `R,T` with probability one half. Every ordered off-diagonal pair survives in `C[R,T]` with probability `1/4`, so some physical cut satisfies

`||C[R,T]||_F^2
 >=(1/4)||off(C)||_F^2
 >=65536/225`.                                                     (5.5)

Conditioning only on the shared pair `X_S` leaves the `K` variables independent and turns all `S-K` terms into affine terms. Apply (5.1) on the `R|T` product cut and average the conditional small-ball estimate. This yields

`boxed:
 sup_t P(|Q-t|<rho)
 <=1.8951903621117363... sqrt(rho).}`                              (5.6)

Therefore the entire still-unpaid localized overlap-two branch (2.13) has a uniform square-root small-ball bound, with the worst explicit constant

`boxed: H_rem=8.063346501398827... .}`                             (5.7)

The genuinely missing step is now to combine this half-Riesz currency with the third curvature forced elsewhere by the global third-compound structure, without using the refuted arbitrary-remainder slope-innovation shortcut.

## 6. Fully dense genuinely rotated indefinite stress family for the new density branch

The off-diagonal exit is not merely a local toy. Fix `m>=3`, put

`epsilon=1/128`,
`B=[[epsilon,2],[2,-epsilon]]`,
`D=4+epsilon^2=65537/16384`,                                       (6.1)

and

`S_m=2I_m-(4/m)J_m`.                                               (6.2)

Then `spec(B)={+sqrt(D),-sqrt(D)}` and

`spec(S_m)={-2,+2^(m-1)}`.                                        (6.3)

Let

`L_m=(1/(100m)) [[1,...,1],[2,...,2]]`                             (6.4)

and define the exact dense Schur completion

`A_m=[[B,L_m],[L_m^T,S_m+L_m^T B^(-1)L_m]].`                       (6.5)

Every entry is nonzero. Indeed

`B^(-1)=D^(-1)[[epsilon,2],[2,-epsilon]]`,                         (6.6)

so every entry of the rank-one correction is

`q_m=(8-3epsilon)/(10000 D m^2)>0`.                               (6.7)

Hence the outside off-diagonals are `-4/m+q_m!=0`, the outside diagonals are `2-4/m+q_m>0`, and every `L_m` entry is positive.

The comparison matrix `B direct_sum S_m` has every eigenvalue of modulus at least two. Moreover

`||A_m-(B direct_sum S_m)||_op
 <=sqrt(5)/(100 sqrt(m)) +(8-3epsilon)/(10000 D m)`.               (6.8)

For `m>=3` the right side is `<0.013`, so Weyl gives every eigenvalue of `A_m` modulus `>1.987`. Thus this is a fully dense, genuinely rotated, indefinite target-valid family.

For the distinguished first two physical coordinates, the exact pair-Schur complement is `S_m`. Every individual overlap-two minor has magnitude

`|det B| * 4/m =4D/m ->0`,                                        (6.9)

but the entire packet is

`J_2(S)=16D^2 (m-1)/m`.                                           (6.10)

Since `kappa=sqrt(D)`, the new aggregate receiver gives

`boxed:
 ||p_(X^T A_m X)||_infinity
 <=C_ov2 [16 D^3 (m-1)/m]^(-1/8).}`                               (6.11)

At `m=4` this is

`8.203958346289575...`,                                            (6.12)

and as `m->infinity` it tends to

`7.914184...`.                                                     (6.13)

Thus the certificate remains dimension-free while every individual overlap-two determinant vanishes like `1/m`.

## 7. Designated account02/B04 result applied to an actual inequality

The latest account02/B04 source read in this run is the r43 addendum at

`yspennstate/math-open-problems@75645ea7ff3609b55e7ed231900404ad2188693e`.

It records the completed banked-square theorem

`QFORM-BANKED-RANK2-PLUS-PROJECTION-SQUARE-v1`:

for two original-coordinate banks,

`Q=(U^T X)^T Lambda(U^T X)+b^T X+c
   +d(a^T Y+h(X))^2`,                                              (7.1)

with `b in Ran(U)`,

`||p_Q||_infinity
 <=16 sqrt(60) |d|^(-1/2)||a||^(-1)|det Lambda|^(-1/4).`           (7.2)

Apply it to its explicit `m=4` Walsh target

`Q=2(u_1^T X_H)^2-(u_2^T X_H)^2
   -2(w^T X_H/sqrt(2)+z^T X_L/sqrt(2))^2`.                         (7.3)

Here `Lambda=diag(2,-1)`, `d=-2`, `||a||=1/sqrt(2)`, `b=0`, so

`boxed:
 ||p_Q||_infinity
 <=16 sqrt(60) 2^(-1/4)
 =104.21688998922089... .}`                                       (7.4)

On this *same actual matrix*, choose the physical pair `S={2,3}` in the `H` bank (using one-based labels in the displayed Walsh ordering). Direct exact arithmetic gives

`A[S,S]=[[0,1],[1,0]]`,
`kappa=1`,
`J_2(S)=27/16`.                                                    (7.5)

Therefore the fixed-pair overlap-two theorem (1.4) gives the separate valid inequality

`boxed:
 ||p_Q||_infinity
 <= C_ov2 (27/16)^(-1/8)
 =17.63155480921866... .}`                                        (7.6)

This does not invalidate or dominate the partner theorem in general: for large diffuse Walsh banks the physical-pair conditioning can deteriorate, whereas (7.2) spends the whole independent-bank projection norm. It is an equation-level comparison on one target-valid matrix and satisfies the designated-partner requirement.

## 8. What is now genuinely left in the overlap-two branch

Combining account03/B20 r42 with Sections 2--5, every target state in its localized overlap-two output is now either

1. paid outright by (2.12), if the shared off-diagonal is at least `1/32`; or
2. has the tiny physical pair (2.13) and simultaneously carries one of the two explicit aggregate packets (4.8)/(4.9), hence the universal square-root small-ball estimate (5.7).

The first remaining implication is therefore

`QFORM-SMALLPAIR-HALFRIESZ-PLUS-THIRDCURVATURE-SPLICE-v1`:

> In the fixed localized overlap-two state (2.13), use the forced complement-curvature/coupling packet from (4.8)/(4.9) together with the remaining third-compound curvature to upgrade the universal `rho^(1/2)` small-ball estimate to a linear `O(rho)` estimate, while retaining arbitrary same-bank curvature and without invoking the refuted arbitrary-remainder slope-innovation mechanism.

The full QFORM theorem remains **OPEN**. Full-target continuity remains **OPEN**.

## 9. Exact numerical checks

The deterministic constants checked in this run are

`C_ov2 =18.82331388097627...`,
`C_ov2*(589824)^(1/8)=99.09149694560317...`,
`H_1=7.829376757708329...`,
`H_1*(9/8)^(1/4)=8.063346501398827...`,
`(512/15)^2/4=65536/225=291.2711111111111...`,
`H_1*(65536/225)^(-1/4)=1.8951903621117363...`,
`C_ov2*(27/16)^(-1/8)=17.63155480921866...`.

These numerical checks are only arithmetic verification; the proofs are Sections 2--5.
