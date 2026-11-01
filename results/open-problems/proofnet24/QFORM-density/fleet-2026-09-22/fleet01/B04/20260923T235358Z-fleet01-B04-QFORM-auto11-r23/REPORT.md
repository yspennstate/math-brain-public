SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-23T23:53:58Z.
attacking: aggregate overlap-two third-compound mass before selecting any local Schur coefficient; convert the entire off-diagonal Schur Frobenius packet into first-compound product-Fourier energy by a physical random cut.

# fleet01/B04 r23 — fixed indefinite pair: aggregate overlap-two energy -> rank-free product-Fourier receiver

Programme: `QFORM-DENSITY-3EIG-20260922`
Assignment: Product Fourier rearrangement
Status: `NEW SUPPORTING THEOREM / FIXED-PAIR OVERLAP2 AGGREGATION CLOSED / PARTNER APPLIED / FULL TARGET OPEN`
Continuity in the new branch: **essential boundedness proved; continuity not claimed**.
Independent review: **pending**.
Execution label: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture is **not proved** here. The new result closes one specific structural debt left by the preceding first-compound/pair-log receiver: for a fixed invertible indefinite physical pair, it converts the *entire* overlap-two minor mass incident to that pair into a density estimate, without selecting or inverting any individual residual coefficient. All random variables remain original physical product coordinates. No post-rotation independence, moments, compact support, connected support, Gaussianity, log-concavity, arbitrary-joint coarea, conditional-density cap, or law-uniform pointwise quadratic-phase decay is used.

## 1. Source boundary and pinned inputs


The main analytic input is this worker's completed result

`QFORM-INDEFINITE-PAIR-FIRSTCOMPOUND-RANKFREE-v1`

at

`yspennstate/math-open-problems@5d4cd3fcb9976deebd0cb409ebcca9cfb29cb9ba`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B04/20260923T212739Z-fleet01-B04-QFORM-auto11-r20/REPORT.md`.

It states: if `H` is an invertible indefinite physical pair with
`D=|det B_H|`, `kappa=sigma_min(B_H)`, and a physical bipartition of the exact pair-Schur residual has crossing block `N` with
`Z_1=||N||_F^2>0`, then

`||p_Q||_infinity <= C_* (D kappa)^(-1/4) Z_1^(-1/8)`,              (1.1)

where

`C_*=2^(23/8) exp(1/8) sqrt(Gamma(1/4))
    =15.82845716570843... .`                                      (1.2)

The proof of (1.1) first uses product-Fourier rearrangement to obtain a square-root small-ball estimate for the *full* residual, including arbitrary same-bank curvature, then feeds that estimate into the exact indefinite-pair logarithmic envelope. It proves an essentially bounded density but does not prove continuity.

The designated partner result used below is fleet02/B04's completed

`QFORM-C1-RANK2-ZCURVATURE-BIPARTITE-RECEIVER-v1`

introduced at

`yspennstate/math-open-problems@6efdb84dba8c88442c7d85a5af8bea67ed747eec`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/20260923T224543Z-fleet02-B04-QFORM-auto11/REPORT.md`.

For the zero-anchor C1 factorization with `rank(E_ZZ)=2`, it gives

`||p_Q||_infinity <=2 sqrt(pi) (||b||_2 lambda)^(-1/2)`,           (1.3)

where `lambda=||E_ZZ||_op`. This groups a physical bipartite curvature bank before paying a coefficient.

The live correction `QFORM-INDEFINITE-INNOVATION-ARBITRARY-REMAINDER-FALSE-v1` was re-read and is respected: the theorem below never replaces genuine residual curvature by slope innovation. The complete Schur remainder is kept and its physical cross energy is used directly.

## 2. The exact overlap-two Schur identity with the diagonal removed

Fix a physical pair

`H={h_1,h_2}`

and put

`B=A[H,H]`.

Assume `B` is invertible and indefinite. Let

`K=[n]\H`,
`L=A[H,K]`,
`S=A[K,K]-L^T B^(-1)L`                                           (2.1)

be the exact Schur complement. Set

`D=|det B|`,
`kappa=sigma_min(B)>0`.                                           (2.2)

Define the **exact overlap-two energy incident to H**

`W_H^(2)
 = sum_(i,j in K, i!=j)
   det A[H union {i}, H union {j}]^2`.                            (2.3)

The row and column roles in (2.3) are labelled; because the determinant is squared, any harmless ordering sign disappears.

For each `i!=j`, the block determinant identity gives

`det A[H union {i}, H union {j}]
 = +/- det(B) [A_ij-A_iH B^(-1) A_Hj]
 = +/- det(B) S_ij`.                                              (2.4)

Therefore

`boxed:
 W_H^(2)=D^2 sum_(i!=j) S_ij^2.`                                  (2.5)

The exclusion `i=j` is essential: the diagonal Schur energy belongs to overlap three, not overlap two. Formula (2.5) is the exact quantity needed below.

## 3. Random physical cut of the whole overlap-two packet

Independently assign every coordinate of `K` to two labelled banks `U,V` with probability `1/2`, and put

`N=S[U,V]`.                                                       (3.1)

This is a partition of **original coordinates**; no random variable is rotated.

For every ordered pair `i!=j`,

`P(i in U, j in V)=1/4`.

Hence

`E ||N||_F^2
 = (1/4) sum_(i!=j) S_ij^2
 = W_H^(2)/(4D^2).`                                               (3.2)

Consequently some deterministic physical partition `K=U sqcup V` obeys

`boxed:
 Z_1:=||S[U,V]||_F^2
 >=W_H^(2)/(4D^2).`                                               (3.3)

This is the missing aggregate-before-inversion step for a fixed pair. No individual `S_ij` is selected.

## 4. Main theorem: determinant cancellation

### Theorem `QFORM-FIXED-INDEFINITE-PAIR-OVERLAP2-RANDOMCUT-v1`

Let `X_1,...,X_n` be independent real random variables with densities at most one. Let `A=A^T`. Suppose some physical pair `H` has an invertible indefinite block `B=A[H,H]`, and let `kappa=sigma_min(B)`. If `W_H^(2)>0`, then `Q=X^TAX` has a density satisfying

`boxed:
 ||p_Q||_infinity
 <= C_ov2 [kappa^2 W_H^(2)]^(-1/8),`                              (4.1)

where

`C_ov2
 =2^(25/8) exp(1/8) sqrt(Gamma(1/4))
 =18.82331388097627... .`                                        (4.2)

No rank assumption is imposed on the Schur complement.

#### Proof

Complete the physical pair exactly:

`Q
 =(X_H+B^(-1)L X_K)^T B (X_H+B^(-1)L X_K)
  + X_K^T S X_K`.                                                 (4.3)

Choose the physical partition `K=U sqcup V` supplied by (3.3). In the residual,

`X_K^T S X_K
 = X_U^T S_UU X_U
   +2 X_U^T S_UV X_V
   +X_V^T S_VV X_V`.                                              (4.4)

Thus the exact residual crossing block is `N=S[U,V]`, while both same-bank quadratic blocks are retained. The hypotheses of (1.1) therefore hold with the same physical pair `B` and with `Z_1` from (3.3). Hence

`||p_Q||_infinity
 <= C_* (D kappa)^(-1/4)
        [W_H^(2)/(4D^2)]^(-1/8)`                                 (4.5)

`= C_* 2^(1/4) kappa^(-1/4) [W_H^(2)]^(-1/8)`.                   (4.6)

The determinant cancels **exactly**:

`D^(-1/4) (D^2)^(1/8)=1`.                                        (4.7)

Since
`kappa^(-1/4)[W_H^(2)]^(-1/8)
 =[kappa^2 W_H^(2)]^(-1/8)`,
(4.1) follows, with `C_ov2=2^(1/4)C_*`. QED.

The homogeneity is correct: `kappa^2 W_H^(2)` has degree eight in `A`, so the right side of (4.1) scales as `|c|^(-1)` under `A -> cA`.

This theorem is materially stronger than choosing one overlap-two minor. The individual determinants can all tend to zero while their squared aggregate and the density certificate remain at fixed scale.

## 5. Relation to the global overlap-two sector

Define

`Delta_3^(2)(A)
 = sum_(|R|=|T|=3, |R intersect T|=2) det A[R,T]^2`.              (5.1)

Every pair `(R,T)` in (5.1) has a unique shared physical pair
`H=R intersect T`, so exactly

`boxed:
 Delta_3^(2)(A)=sum_(|H|=2) W_H^(2).`                             (5.2)

Thus the overlap-two problem is reduced to a sharply stated pair-selection problem:

> Find an invertible indefinite physical pair `H` for which
> `kappa_H^2 W_H^(2)` is universally large, or route the complementary mass—pairs that are definite, singular, or badly conditioned—into the already completed definite-pair, singular-pair, diagonal/principal, grouped-hub, ridge, projected-crossing, or square-factor receivers.

The residual-rank issue and the "many tiny S_ij" issue are no longer obstructions for a fixed indefinite pair.

This is not yet a global theorem because (5.2) alone does not force an indefinite, well-conditioned physical pair. The full target remains open.

## 6. Fully dense genuinely rotated indefinite stress family

The new theorem has a clean dimension-free test on a family where every individual overlap-two minor vanishes like `1/m`.

Fix `m>=3`. Let

`B=[[1,3],[3,1]]`,                                                (6.1)

so

`spec(B)={4,-2}`,
`D=8`,
`kappa=2`.                                                        (6.2)

Let `1_m` be the all-ones vector and define the Householder reflection

`H_m=I_m-(2/m)1_m 1_m^T`,
`S_m=2H_m=2I_m-(4/m)J_m`.                                        (6.3)

Thus `S_m` has spectrum `{-2,+2^(m-1)}` and every off-diagonal entry is `-4/m`.

Set

`L_m=(1/(100m)) [[1,...,1],
                  [2,...,2]]`,                                   (6.4)

and define

`A_m=
 [[B,   L_m],
  [L_m^T, S_m+L_m^T B^(-1)L_m]].`                                (6.5)

Because

`B^(-1)=[[-1/8,3/8],[3/8,-1/8]]`

and for every pair of outside coordinates

`(L_m^T B^(-1)L_m)_ij=7/(80000 m^2)`,                             (6.6)

every entry of `A_m` is nonzero for `m>=3`. In particular its outside off-diagonal entries are

`-4/m + 7/(80000m^2) !=0`,                                       (6.7)

and the outside diagonal entries are

`2-4/m+7/(80000m^2)>0`.                                          (6.8)

The matrix is fully dense and its eigendirections are not the original coordinate axes.

The exact pair-Schur complement is `S_m`. The block-diagonal comparison matrix

`A_m^0=B direct_sum S_m`

has all eigenvalues of modulus at least two. Moreover

`||A_m-A_m^0||_op
 <= ||L_m||_op + ||L_m^T B^(-1)L_m||_op`
` = sqrt(5)/(100 sqrt(m)) + 7/(80000m)`.                          (6.9)

For `m>=3` this is at most `0.012939112`. Weyl's inequality therefore gives

`min_j |lambda_j(A_m)|
 >=2-[sqrt(5)/(100sqrt(m))+7/(80000m)]
 >1.987`.                                                         (6.10)

In particular every `A_m` satisfies the owner's spectral hypothesis with substantial room to spare and is indefinite.

For the distinguished first two physical coordinates `H`, every ordered `i!=j` outside `H` has

`|det A_m[H union {i}, H union {j}]|
 =D |(S_m)_ij|
 =8*(4/m)
 =32/m`.                                                          (6.11)

Thus **every local overlap-two minor tends to zero**. Nevertheless there are `m(m-1)` ordered terms, so

`boxed:
 W_H^(2)
 =m(m-1)(32/m)^2
 =1024 (m-1)/m.`                                                  (6.12)

The new theorem gives, for every independent cap-one product input law,

`boxed:
 ||p_(X^T A_m X)||_infinity
 <= C_ov2 [4*1024(m-1)/m]^(-1/8)
 = C_* 2^(-5/4) [m/(m-1)]^(1/8).}`                               (6.13)

The right side is uniformly bounded in `m` and tends to

`6.65504644481997...`.                                            (6.14)

For `m=4`, the matrix is especially transparent:

`S_4=2I_4-J_4`

with diagonal `+1` and every off-diagonal entry `-1`. Then

`W_H^(2)=768`

and

`boxed:
 ||p_(X^T A_4 X)||_infinity
 <=6.898718638656284... .}`                                      (6.15)

A direct exact check gives the twelve overlap-two determinants all equal to `+8` up to harmless ordering signs, so their squared sum is `12*64=768`.

This family shows the mechanism demanded by the assignment: decreasing-rearrangement/product-Fourier currency is aggregated in physical product space before any reciprocal local minor is paid.

The new branch proves **essential boundedness**. It does not, by itself, produce an `L^1` characteristic function, so continuity is not claimed.

## 7. Designated fleet02/B04 theorem applied to an actual inequality

To apply the current completed partner theorem at equation level, consider five original coordinates
`(X_h,X_1,X_2,X_p,X_q)` and the physical matrix

`A_ctrl=
 [[0,3,4,0,0],
  [3,0,0,0,0],
  [4,0,0,0,0],
  [0,0,0,0,3],
  [0,0,0,3,0]].`                                                 (7.1)

Its nonzero spectrum is exactly

`{+5,-5,+3,-3}`,                                                  (7.2)

so it itself satisfies the owner target.

Relative to the zero anchor `h`, the C1 factorization has

`b=(3,4)`, hence `||b||_2=5`,                                    (7.3)

and the residual zero-diagonal `Z-Z` curvature is

`E_ZZ=[[0,3],[3,0]]`, hence `lambda=3`.                           (7.4)

Applying fleet02/B04's theorem (1.3) gives the actual inequality

`boxed:
 ||p_(X^T A_ctrl X)||_infinity
 <=2 sqrt(pi)/sqrt(15)
 =0.915291232863769... .}`                                       (7.5)

This is a direct use of the designated partner result, not merely a citation to its existence.

## 8. Exact remaining implication

The new first unpaid implication for this branch is

`QFORM-OVERLAP2-PAIRSELECTION-OR-SIGNATURE-ROUTING-v1`:

Starting from target-scale global overlap-two mass
`Delta_3^(2)(A)`, prove that either

1. some physical pair `H` is invertible indefinite and has
   `kappa_H^2 W_H^(2) >= c` for a universal `c>0`, so Theorem 4.1 pays it; or
2. the overlap-two mass carried by definite, singular, or very poorly conditioned shared pairs forces one of the already-paid definite-pair, exact singular-pair, principal/diagonal, grouped-hub, ridge, projected-crossing, square-factor, or lower-compound receivers.

The key improvement is that one no longer needs to select a large individual overlap-two minor or a high-rank Schur remainder. The only fixed-pair losses left are pair signature and the physical conditioning parameter `kappa_H`.

## 9. Integrity notes

- Original-coordinate independence is preserved throughout.
- The random cut is a deterministic-existence argument over physical coordinates; it does not rotate the product law.
- The full Schur remainder is retained, including arbitrary same-bank curvature.
- No pointwise scalar quadratic-phase decay is used.
- No finite-support, moment, smoothness, Gaussian or log-concavity assumption is introduced.
- No Monte Carlo evidence is used.
- The full theorem is still OPEN.
- Two independent end-to-end reviews have not been obtained for this new theorem.
