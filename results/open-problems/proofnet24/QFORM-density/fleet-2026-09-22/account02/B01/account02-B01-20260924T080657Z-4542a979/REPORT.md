SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B01, 2026-09-24T08:06:57Z.
attacking: almost-single-leaf stability in the finite-leak rank-one two-hub arrowhead; spend the two Schur singular directions before the weak tail.

# account02/B01 — uniform stability through the single-leaf limit

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `account02-B01-20260924T080657Z-4542a979`  
Role: Oscillatory replacement / complementary constructions and source-valid counterexamples  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **ALMOST-SINGLELEAF INSTABILITY REMOVED IN THE RANK-ONE TWO-HUB ARROWHEAD / FULL QFORM OPEN**

## 1. Scope and correction boundary

All random scalar variables below are ORIGINAL independent coordinates with probability densities bounded by one. No moment, Gaussian, iid, compact-support, connected-support, log-concavity, smoothness, or post-rotation independence hypothesis is used. Affine terms are arbitrary. Essential boundedness is the target; continuity is not claimed here.

The phase-aligned-density obstruction is preserved. At any prescribed nonzero frequency `tau`, a cap-one probability density can be supported on a finite union of intervals where `tau x^2` is arbitrarily close to `2 pi Z`, so `Re E exp(i tau X^2)` can be arbitrarily close to one. Therefore no law-uniform pointwise scalar quadratic-phase decay is used below.

The live correction ledger was refreshed before publication. In particular, this report does not use arbitrary-joint coarea, conditional projection-density caps, a uniformly good physical minor, near-zero-half-Riesz continuity, or the recently refuted mixed-norm integral `int |t|^(-1/2)||G_t||_2 dt`.

## 2. Source-pinned inputs actually used

### 2.1 Required 20260922T211500Z Fourier package

Required source:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

The following proved statements are spent at explicit equations.

1. **Square peel.** If an ORIGINAL coordinate with coefficient `a!=0` is completed exactly,

`Q=a(X+h)^2+R`,

then

`||p_Q||_infinity <= |a|^(-1/2) H_(1/2)(R)`,                  (2.1)

where `H_alpha(Z)=sup_s E|Z-s|^(-alpha)`.

2. **Quarter-potential of a square.** For any literal nonzero diagonal coefficient `a`, irrespective of the remaining quadratic/affine terms,

`H_(1/4) <= 4 |a|^(-1/4)`.                                    (2.2)

3. **Logarithmic two-square interface.** After a literal scalar completion,

`H_(1/2)(a(V+h)^2+T)`
` <= |a|^(-1/2)[8+2 sup_s E log_+(|a|/(4|s-T|))]`.             (2.3)

Since `log_+ z <= 4 z^(1/4)`, if `H_(1/4)(T)<=H` then

`H_(1/2)(a(V+h)^2+T)`
` <= 8|a|^(-1/2)+8*4^(-1/4)H|a|^(-1/4)`.                     (2.4)

4. Scalar Schur persistence: completing one nonzero physical pivot of a matrix with three singular/eigenvalue magnitudes at least one leaves a Schur coefficient with at least two such magnitudes.

The same pinned package's D/D'/D5 volume currencies are tested on a concrete target family in Section 7.

### 2.2 Earlier B01 receivers

The immediately preceding grouped-arrowhead theorem is at

`yspennstate/math-open-problems@fb7b0f71ead32ea608ff9ec45370edc246f7239e`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260924T063552Z-account02-B01-qform-auto11-r46/REPORT.md`.

For a quadratic rank-one two-hub arrowhead with hub-leaf cross block `w c^T`, put

`W=||w||_2`, `C=||c||_2`, `s=WC`.

If `max_i c_i^2/C^2<=1/2`, it proves

`H_(1/2) <= 2^(13/4) s^(-1/2)`.                                (2.5)

If a unique heavy leaf `h` satisfies `c_h^2>C^2/2`, let

`T=(C^2-c_h^2)^(1/2)`, `q_h=W|c_h|`, `q=WT`.

When `q>0`, it proves

`H_(1/2) <= 2^(23/8) (q_h q)^(-1/4)`.                          (2.6)

The loss in (2.6) diverges as `q->0`; removing that loss is the present task.

The previous B01 3-variable theorem is at

`yspennstate/math-open-problems@522585af1e80eff6ad75808d7e3be55a3a2bc8ac`.

It proves that every symmetric `3x3` coefficient with `s_2>=1` has

`H_(1/2)<169`                                                    (2.7)

for arbitrary independent cap-one laws and arbitrary affine terms. By homogeneity,

`s_2(C)>=tau>0  =>  H_(1/2)(C)<169 tau^(-1/2)`.                (2.8)

Finally, the orientation-free exact-rank-two affine theorem at

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

gives

`H_(1/2) <=128 |det Lambda|^(-1/4)`                            (2.9)

for any exact rank-two coefficient and arbitrary affine term.

### 2.3 Freshest designated partner account03/B01

Fresh source resolution found account03/B01 r47 at

`yspennstate/math-open-problems@fb16bfb901a09a67fd139e99f5b79e9381307a0d`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/20260924T073034Z-account03-B01-qform-auto11-r47/REPORT.md`.

Its proved Riesz-to-Fejer compiler states, at the critical half-power,

`sup_y D_T law(Z)(y) <= [sqrt(T)/(pi sqrt(2))] H_(1/2)(Z)`.     (2.10)

Section 8 applies (2.10) to the new theorem at an actual signed-frequency inequality.

## 3. Setup

Let `H=(H_1,H_2)` be two original hub coordinates and `Y=(Y_1,...,Y_m)` a source-disjoint original product bank. Consider a quadratic-plus-affine residual whose coefficient matrix is

`S = [[B, w c^T], [c w^T, D]]`,                                (3.1)

where `B=B^T` is `2x2`, `D=diag(d_1,...,d_m)`, `w in R^2`, and `c in R^m`. Assume

`boxed: s_2(S)>=1.`                                             (3.2)

This is exactly the spectral resource produced after one outer scalar completion of a full target form by the pinned Schur-persistence lemma.

Fix

`delta=1/4`, `rho=1-delta=3/4`.                                (3.3)

The key move is spectral allocation **before** paying a weak cross coefficient. Whenever a cross packet of operator norm `<delta` is deleted, Weyl's singular-value inequality gives

`s_2(S_0)>rho`.                                                  (3.4)

The deleted variables are then conditioned, so their actual cross terms become affine terms. They are never treated as a small random quadratic perturbation.

## 4. Small total hub-leaf cross packet

Put `s=||w|| ||c||`. First suppose

`s<delta`.                                                       (4.1)

Delete the entire hub-leaf cross packet. Then

`S_0=B direct_sum D`, `||S-S_0||=s<delta`,

and therefore

`s_2(S_0)>rho`.                                                  (4.2)

There are three exhaustive allocations of these two large singular directions.

### 4.1 Two hub directions

If `s_2(B)>=rho`, condition on all leaves. The induced leaf couplings become arbitrary affine terms in the two independent hubs. Since `|det B|>=rho^2`, (2.9) gives

`H_(1/2) <=128 rho^(-1/2)
          =147.8016689126...`.                                  (4.3)

### 4.2 Two diagonal leaf directions

If two distinct leaves satisfy `|d_j|,|d_k|>=rho`, condition on every other coordinate and apply (2.9) to `diag(d_j,d_k)`:

`H_(1/2) <=128 rho^(-1/2)<148`.                                 (4.4)

### 4.3 One hub direction and one leaf direction

The only remaining allocation has `s_1(B)>=rho` and some `|d_j|>=rho`. Keep the literal three-coordinate block on `(H_1,H_2,Y_j)` and condition all other leaves. Its coefficient is

`C_j = [[B,u],[u^T,d_j]]`, `u=c_j w`.                           (4.5)

The block `B direct_sum [d_j]` has `s_2>=rho`, while the off-diagonal perturbation in (4.5) has norm `||u||<=s<delta`. Hence

`s_2(C_j)>rho-delta=1/2`.                                       (4.6)

By the scaled 3D theorem (2.8),

`H_(1/2)<169 (1/2)^(-1/2)
         =169 sqrt(2)
         =239.0020920411... <240`.                              (4.7)

Thus every small-total-cross state is paid uniformly.

## 5. Non-small cross packet: spread leaves

Assume now `s>=delta`. If

`max_i c_i^2/C^2<=1/2`,                                         (5.1)

then the grouped averaged-frequency theorem (2.5) gives

`H_(1/2)
 <=2^(13/4) delta^(-1/2)
 =19.0273138401...`.                                            (5.2)

No individual weak edge is inverted.

## 6. Non-small cross packet: one heavy leaf

Assume there is a unique heavy leaf `h` with

`c_h^2>C^2/2`.                                                   (6.1)

Let `q_h=W|c_h|`, `q=W(C^2-c_h^2)^(1/2)`. Then `q_h>q`.

### 6.1 Tail cross norm not small

If `q>=delta`, (2.6) and `q_h q>delta^2` give

`H_(1/2)
 <2^(23/8) delta^(-1/2)
 =14.6720646913...`.                                            (6.2)

### 6.2 Tail cross norm small

Suppose instead

`q<delta`.                                                       (6.3)

Retain the heavy leaf in the literal 3-variable core `C_h` on `(H_1,H_2,Y_h)` and delete only the hub-to-tail cross packet. Thus

`S_0=C_h direct_sum D_tail`, `||S-S_0||=q<delta`,

so again

`s_2(S_0)>rho`.                                                  (6.4)

There are again three allocations.

If `s_2(C_h)>=rho`, condition the tail and use (2.8):

`H_(1/2)<169 rho^(-1/2)
         =195.1443909861...`.                                   (6.5)

If two tail diagonals have modulus at least `rho`, condition everything else and use (2.9), obtaining the bound (4.4).

It remains to treat the mixed allocation

`s_1(C_h)>=rho`, `|d_j|>=rho`                                   (6.6)

for one tail leaf `Y_j`. Keep `(H_1,H_2,Y_h,Y_j)` and condition all other coordinates. The cross vector from `Y_j` into the core is

`u=(c_j w,0)`, `||u||<=q<delta`.                                (6.7)

Complete the literal coordinate `Y_j` exactly:

`d_j(Y_j+d_j^(-1)u^T Z)^2 + Z^T C' Z + affine`,

`C'=C_h-d_j^(-1)u u^T`.                                        (6.8)

The Schur correction has norm at most

`||u||^2/|d_j| < delta^2/rho =1/12`.                           (6.9)

Hence

`||C'||_op >=rho-1/12=2/3`.                                    (6.10)

For a symmetric `3x3` matrix, `||C'||_op<=3 max_{kl}|C'_{kl}|`; therefore some literal physical coefficient has magnitude at least `2/9`. If it is diagonal, use the pinned square quarter-potential (2.2); if it is off-diagonal, use the earlier B01 physical-edge quarter-potential, whose constant is smaller than the square bound at this scale. Uniformly,

`H_(1/4)(Z^T C'Z+affine)
 <=4(9/2)^(1/4).`                                               (6.11)

Insert (6.11) into the pinned logarithmic interface (2.4) at `|d_j|>=rho`:

`H_(1/2)
 <=8 rho^(-1/2)
   +8*4^(-1/4)*4(9/2)^(1/4) rho^(-1/4)
 =44.6514257375...`.                                            (6.12)

This closes the heavy-leaf limit without a reciprocal power of `q`.

## 7. Main theorem and a strict vanishing-tail stress family

### Theorem — `QFORM-RANK1-TWOHUB-ARROWHEAD-UNIFORM-v1`

For every quadratic-plus-affine residual with coefficient (3.1) and `s_2(S)>=1`,

`boxed: H_(1/2)(R)<240.`                                       (7.1)

The cases in Sections 4-6 are exhaustive, and the largest displayed constant is `169 sqrt(2)<240`.

Consequently, if a full target form has one exact ORIGINAL-coordinate completion

`Q=a_0(X_0+h)^2+R`, `a_0!=0`,                                  (7.2)

whose Schur coefficient has the rank-one two-hub arrowhead form (3.1), then scalar Schur persistence gives (3.2), and the **required pinned square peel** (2.1) yields the actual target-level estimate

`boxed: ||p_Q||_infinity <240 |a_0|^(-1/2).`                   (7.3)

In the previously isolated chamber `|a_0|>=1/64`, this is

`boxed: ||p_Q||_infinity <1920.`                                (7.4)

No tail-leakage parameter appears.

### Vanishing-tail target family

For `0<epsilon<=1/4`, on original coordinates `(X_0,H_1,H_2,Y_1,Y_2)` take the direct sum of the outer coefficient `[1]` and

`S_epsilon =
 [[1, 1,  1,  epsilon],
  [1, 1, -1, -epsilon],
  [1,-1,  1,  0],
  [epsilon,-epsilon,0,0]].`                                    (7.5)

This is (3.1) with

`B=[[1,1],[1,1]]`, `w=(1,-1)`, `c=(1,epsilon)`, `D=diag(1,0)`.

The leaf `Y_1` is heavy and the tail norm is

`q=sqrt(2) epsilon ->0`.                                        (7.6)

Thus the previous estimate (2.6) diverges like `epsilon^(-1/4)`.

Set `u=(H_1+H_2)/sqrt(2)` and `v=(H_1-H_2)/sqrt(2)` only for deterministic spectral calculation. The `u` direction has eigenvalue `2`. The remaining `(v,Y_1,Y_2)` coefficient has characteristic polynomial

`p_epsilon(lambda)
 =lambda^3-lambda^2-2(1+epsilon^2)lambda+2epsilon^2`.            (7.7)

Since `p_epsilon(2)=-2epsilon^2<=0` and `p_epsilon(lambda)->+infinity` as `lambda->+infinity`, it has a positive root at least `2`; since `p_epsilon(-1)=4epsilon^2>=0` and `p_epsilon(lambda)->-infinity` as `lambda->-infinity`, it has a negative root at most `-1`. Hence the residual already has three eigenvalues of modulus at least one, and adjoining `X_0^2` makes (7.5) a strict full-target family.

Even more sharply, condition on `Y_2`. The literal `(H_1,H_2,Y_1)` coefficient is

`C_sharp=[[1,1,1],[1,1,-1],[1,-1,1]]`,                         (7.8)

whose spectrum is `{-1,2,2}`. The `Y_2` coupling becomes only an affine term. Therefore (2.8) gives

`H_(1/2)(R_epsilon)<=169/sqrt(2)=119.5010460206...`,            (7.9)

and the **required source square peel at `a_0=1`** gives

`boxed: ||p_(Q_epsilon)||_infinity <=169/sqrt(2)<120}`          (7.10)

uniformly as `epsilon->0`.

This family also gives a concrete obstruction to the required source's D/D'/D5 cross-volume route: it has five coordinates, so every disjoint physical cut has one side of cardinality at most two. Consequently every physical cross block has rank at most two, and

`e_3(M^TM)=e_5(M^TM)=0`                                        (7.11)

for every cut. The volume currencies vanish identically while the half-Riesz/spectral-allocation route pays (7.10).

## 8. Freshest partner result applied at an actual averaged-frequency inequality

Apply account03/B01 r47's Riesz-to-Fejer compiler (2.10) to the new theorem (7.1). For every rank-one two-hub arrowhead residual satisfying `s_2(S)>=1`,

`boxed:
 sup_y D_T law(R)(y)
 < [240/(pi sqrt(2))] sqrt(T)
 =54.0189789695... sqrt(T).
}`                                                               (8.1)

For the strict vanishing-tail family, (7.9) sharpens this to

`boxed:
 sup_y D_T law(R_epsilon)(y)
 <= [169/(2pi)] sqrt(T)
 =26.8971853826... sqrt(T).
}`                                                               (8.2)

This is a genuine signed averaged-frequency consequence; it is not a pointwise characteristic-function estimate.

The preceding partner r46 physical-pair theorem also shows why pair inversion alone does not give uniformity on (7.5). For the weak physical pair `(H_1,Y_2)`,

`P_epsilon=[[1,epsilon],[epsilon,0]]`,
`D=epsilon^2`,
`kappa=(sqrt(1+4epsilon^2)-1)/2 ~ epsilon^2`.                   (8.3)

Its valid bound

`14.180833 D^(-3/10)(kappa s_3(A))^(-1/5)`                     (8.4)

grows like a constant times `epsilon^(-1)`, while (7.10) is uniform. The new allocation mechanism is therefore complementary to the partner's fixed-pair receiver.

## 9. What remains

The first unpaid implication in this B01 finite-leak chain is now the complementary non-isotropic normal form

`QFORM-DIAGRANK1-PLUS-ONEEDGE-STABILITY-v1`:

> for a Schur remainder of the form
> `S=D+alpha q q^T+eta(e_j e_k^T+e_k e_j^T)`
> with the inherited two-large-singular-direction resource, obtain a half-Riesz or direct density compiler uniform as `eta->0`, without reciprocating the weak edge and without treating it as a small random quadratic perturbation.

The rank-one two-hub arrowhead branch—including the exact and arbitrarily close single-leaf limit—is paid by (7.1). The full unrestricted QFORM conjecture remains OPEN.
