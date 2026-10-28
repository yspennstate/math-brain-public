SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B20, 2026-09-24T02:20:38Z.
attacking: the fresh account02/B20 r44 fixed-positive-E2 full-cut survivor; force either physical E3 smoothing, a genuine original-coordinate star, or a simultaneous crossed rank-two collar while retaining every nonzero tail.

# account01/B20 — fixed-positive E2 collapses to a physical star or crossed rank-two collar

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T022038Z-account01-B20-QFORM-auto11e`  
Role: Proof closure and keeper / SYNTHESIS  
Status: **ESSENTIAL_STEP_APPLIED / E2 HEAVY-STAR OR CROSSED-R2 COLLAR / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`. Full-target continuity remains separate and OPEN.

## 1. Scope and fresh source boundary

The exact target remains: for arbitrary independent ORIGINAL real random variables with probability densities `0<=f_i<=1`, and arbitrary real symmetric `A` satisfying `s_3(A)>=1`, prove a dimension- and law-independent essential bound on the density of `Q=X^TAX`, or exhibit a valid target counterexample.

No Gaussianity, moments, iid assumption, compact/connected support, log-concavity, finite-rank assumption on `A`, or independence after a spectral/SVD rotation is introduced. Every bank and cut below is a literal set of original independent source coordinates. Small coefficient tails are retained in the actual quadratic form; they are used only in deterministic coefficient inequalities.

Fresh owner control remained revision `2026-09-22.15`, QFORM-only. The live correction boundary remains in force: no law-uniform pointwise quadratic oscillatory decay; no worst-fibre projection cap; no arbitrary-joint rank-three coarea bound; no post-rotation independence; no one-good-minor inference from aggregate volume; and no deletion of a small nonzero coefficient tail on unbounded inputs.

The newest completed designated account02/B20 result actually consumed is


with canonical mathematical report

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B20/20260924T020212Z-account02-B20-auto11/REPORT.md`.

The source snapshot used for this run is `yspennstate/math-open-problems@ed17668c322cb9ec5b8cc8f588d9dd0bad1b5bea` together with fresh brain main at the run's control read.

The physical third-volume receiver used below is the already-written supporting theorem

`QFORM-PHYSICAL-D3-NO-MARGINAL-GATE-v1`:

for every literal original-coordinate cross block `C=A[I,J]`, if

`Z_3(C):=e_3(CC^T)>0`,

then the full ambient quadratic form has a continuous `C_0` density and

`||p_Q||_infinity <= C_3 Z_3(C)^(-1/6)`,

where

`C_3=3*2^(4/3)*e^(1/3)=10.550168831164775... .`                    (1.1)

Its scope keeps arbitrary same-bank quadratic blocks, all outside couplings and all extra spectrum. The unrestricted QFORM theorem is not implied by that receiver alone and remains OPEN.

## 2. Exact account02/B20 inequality consumed

The fresh account02/B20 r44 compiler shows that every still-unpaid descendant of its finite-carrier/strong-packet branch contains a literal full physical cut

`M=A[P,Q]`, `Q=P^c`,                                                  (2.1)

with

`E:=||M||_F^2>c_0`,

`c_0:=((sqrt(766)-4sqrt(3))^2)/16384
     =0.026275654659752182...`,                                     (2.2)

and, after its D5 and grouped-rank-three exits,

`S_4(M):=sum_(r=1)^4 s_r(M)^2 > (63/64)E`,                         (2.3)

`s_3(M)<1/64<=s_2(M)`.                                               (2.4)

This is the partner's fixed-positive-E2 branch. I now apply (2.2)-(2.4) at an actual new inequality rather than merely cite the branch label.

Write

`s_1>=s_2>=...`, `x_r=s_r^2`, and `p:=s_1 s_2`.

From (2.3),

`s_1^2 >= S_4/4 > (63/256)E > (63/256)c_0`.                         (2.5)

Combining (2.5) with `s_2>=1/64` gives

`boxed:
 p>p_*:=sqrt((63/256)c_0)/64
      =0.0012564554392151157... .`                                  (2.6)

This is the equation-level consumption of the newest completed account02/B20 result used throughout the rest of the run.

## 3. First payment: third volume or an ultra-thin rank-two collar

Let

`T:=sum_(r>=3)s_r^2
  =dist_F(M,{rank<=2})^2`.                                           (3.1)

Cauchy--Binet in singular values gives the exact positive lower bound

`e_3(MM^T)
 >= x_1 x_2 sum_(r>=3)x_r
 = p^2 T`.                                                           (3.2)

Define

`theta_*:=3p_*/4096`,
`Z_*:=theta_*^2
    =8.468700907587555e-13`.                                         (3.3)

### Branch 3A: physical E3 payment

If

`e_3(MM^T)>=Z_*`,                                                    (3.4)

the literal physical block `M` enters (1.1), giving

`boxed:
 ||p_Q||_infinity
 <=C_3 Z_*^(-1/6)
 <1084.651.`                                                         (3.5)

This branch has a continuous `C_0` density.

### Branch 3B: retained tail becomes quantitatively tiny

Otherwise, (3.2), (2.6), and (3.3) give

`p sqrt(T) < sqrt(Z_*)=3p_*/4096`,

and therefore

`boxed:
 dist_F(M,{rank<=2})=sqrt(T)<3/4096
 =0.000732421875.`                                                   (3.6)

No tail is removed from `Q`; (3.6) is only deterministic coefficient geometry.

Let

`M_2=U diag(s_1,s_2)V^T`                                            (3.7)

be the best rank-two truncation. The matrices `U,V` are used only to describe the deterministic coefficient block `M`; the random variables are never rotated.

## 4. Top-two physical leverage dichotomy

For a physical row `i in P` let

`ell_i^L=||U(i,:)||_2^2`,

and for a physical column `j in Q` let

`ell_j^R=||V(j,:)||_2^2`.                                           (4.1)

### 4A. Heavy leverage produces a genuine original-coordinate star

Suppose

`max_i ell_i^L>1/32`                                                (4.2)

(the right-heavy case is identical after transposition). For the maximizing original coordinate `i`,

`||M_2[i,Q]||_2
 >=s_2 sqrt(ell_i^L)
 >1/(256sqrt(2)).`                                                   (4.3)

The corresponding row of the retained residual has norm at most the Frobenius tail (3.6). Hence the actual physical row of `M` satisfies

`||M[i,Q]||_2
 >1/(256sqrt(2))-3/4096
 >1/512`.                                                           (4.4)

The last comparison is exact: after multiplying by `4096`, it is `8sqrt(2)>11`, whose square is `128>121`.

Thus a heavy top-two leverage coordinate produces the literal source-coordinate packet

`boxed: ||A[i,Q]||_2>1/512`                                        (4.5)

or its transposed column analogue. Moreover there are at most `63` coordinates on either side with leverage `>1/32`, because the rank-two leverage sum is `2`.

This is a genuine physical one-anchor/star seed; it is not claimed by itself to pay the full law.

### 4B. Diffuse leverage gives four strong physical rank-two quadrants

Now assume

`max_i ell_i^L<=1/32`, `max_j ell_j^R<=1/32`.                       (4.6)

A Rademacher-sign paving yields original-coordinate partitions

`P=P_0 sqcup P_1`, `Q=Q_0 sqcup Q_1`                               (4.7)

such that for both `a,b in {0,1}`,

`U_(P_a)^T U_(P_a) >= g I_2`,
`V_(Q_b)^T V_(Q_b) >= g I_2`,

where

`g=3/8`.                                                            (4.8)

For completeness, if `u_i` is row `i` of `U`, then for random signs

`E ||sum_i eps_i u_i u_i^T||_F^2
 =sum_i ||u_i||^4
 <=(1/32)sum_i||u_i||^2
 =1/16`.

Hence some sign choice has operator norm at most `1/4`; the two color-Gram matrices `(I+-S)/2` are therefore both at least `3I/8`. The same proof applies to `V`.

For every physical quadrant

`C_ab:=M[P_a,Q_b]`,                                                 (4.9)

the rank-two core has

`s_2(M_2[P_a,Q_b])>=g s_2`,

`s_1(M_2[P_a,Q_b])s_2(M_2[P_a,Q_b])>=g^2 p`.                       (4.10)

The actual residual subblock has operator norm at most `sqrt(T)`. Thus (3.6) and `s_2>=1/64` give

`boxed:
 s_2(C_ab)>g/64-3/4096
          =21/4096
          =0.005126953125.`                                        (4.11)

For the product, Weyl's inequality and (3.6) give

`s_1(C_ab)s_2(C_ab)
 >=(g s_1-sqrt(T))(g s_2-sqrt(T))`
` =g^2p-g sqrt(T)(s_1+s_2)+T.`                                     (4.12)

Since `s_1>=s_2>=1/64`,

`s_1+s_2<=2s_1=2p/s_2<=128p`.                                      (4.13)

Also (3.2)-(3.3) in the unpaid branch imply

`p sqrt(T)<3p_*/4096`.                                             (4.14)

Therefore

`g sqrt(T)(s_1+s_2)
 <128g(3p_*/4096)
 =9p_*/256`,                                                        (4.15)

while

`g^2p>9p_*/64=36p_*/256`.                                          (4.16)

Dropping the positive `T` term in (4.12),

`boxed:
 s_1(C_ab)s_2(C_ab)
 >q_*:=27p_*/256
 =0.00013251678460471925...`                                       (4.17)

for **all four** literal original-coordinate quadrants.

## 5. Cross the paving: E3 payment or a second rank-two collar

The four strong quadrants can be spent again without treating their SVD coordinates as random variables. Define the crossed physical cut

`B:=A[P_0 union Q_0, P_1 union Q_1]`.                              (5.1)

It contains, as literal rectangular subblocks, `C_01` and `C_10^T`. Cauchy--Binet expresses `e_2(BB^T)` as the sum of squares of all physical `2x2` minors of `B`; hence it contains all the corresponding minors of either one of these quadrants. From (4.17),

`e_2(BB^T)
 >=e_2(C_01 C_01^T)
 >=[s_1(C_01)s_2(C_01)]^2
 >q_*^2.`                                                          (5.2)

Define

`Z_cross:=q_*^2/2^24
        =1.0466991783364748e-15`.                                  (5.3)

If

`e_3(BB^T)>=Z_cross`,                                               (5.4)

the physical receiver (1.1) pays the full ambient law with

`boxed:
 ||p_Q||_infinity
 <=C_3 Z_cross^(-1/6)
 <3310.974,`                                                        (5.5)

again with a continuous `C_0` density.

Otherwise use the elementary exterior-volume tail inequality. If `y_1>=y_2>=...` are the squared singular values of an arbitrary matrix `R` and `T_2=sum_(k>=3)y_k`, then

`boxed: T_2 e_2(y)<=3 e_3(y).}`                                    (5.6)

Indeed, for each pair `{i,j}`, `sum_(k notin {i,j})y_k>=T_2`; multiply by `y_i y_j` and sum over pairs. Every unordered triple is counted exactly three times.

Applying (5.6) to `B`, then (5.2)-(5.3), gives

`dist_F(B,{rank<=2})^2
 <3 Z_cross/q_*^2
 =3/2^24`.

Therefore

`boxed:
 dist_F(B,{rank<=2})
 <sqrt(3)/4096
 =0.0004228639666916204... .}`                                     (5.7)

Again this is a collar for the actual coefficient block, not permission to delete its tail from the random polynomial.

## 6. New theorem and proof-graph effect

### Theorem — `QFORM-R44-E2-HEAVYSTAR-OR-CROSSED-R2-COLLAR-v1`

Under the exact unpaid E2 branch produced by the completed account02/B20 r44 full-cut compiler, namely (2.1)-(2.4), at least one of the following holds:

1. **physical E3 payment on the original full cut:** `||p_Q||_infinity<1084.651`, with continuous `C_0` density;
2. **physical one-anchor/star seed:** some literal original-coordinate row or column of the cut has Euclidean norm `>1/512`;
3. **physical E3 payment on a crossed full cut:** `||p_Q||_infinity<3310.974`, with continuous `C_0` density;
4. **simultaneous crossed rank-two collar:** there are literal partitions `P=P_0 sqcup P_1`, `Q=Q_0 sqcup Q_1` such that
   - `dist_F(M,{rank<=2})<3/4096`;
   - every one of the four physical quadrants `C_ab=M[P_a,Q_b]` has `s_2(C_ab)>21/4096` and `s_1(C_ab)s_2(C_ab)>q_*=27p_*/256`;
   - the crossed full cut `B=A[P_0 union Q_0,P_1 union Q_1]` satisfies `dist_F(B,{rank<=2})<sqrt(3)/4096`.

This removes the former broad fixed-positive-E2 / multiplicative-rank-two chamber as an amorphous endpoint. The only unpaid descendants of that chamber are now a genuine original-coordinate star or a highly coherent **double rank-two physical collar** across two incompatible full cuts.

The account02/B20 finite curvature-flip packet is not claimed paid here, and its inherited one-anchor packets remain separate unless they match the physical-star seed above. Therefore the first remaining implication is sharpened to

`QFORM-R44-HEAVYSTAR-OR-CROSSED-R2-COLLAR/ONEANCHOR-OR-CURVATURE-FLIP-PAYMENT-v1`:

> pay the physical star / inherited one-anchor packets, the simultaneous crossed rank-two collar, or the finite curvature-flip packet while retaining arbitrary same-bank quadratic curvature, all nonzero coefficient tails, outside couplings, signs, affine terms, fragmented/unbounded source laws, and arbitrary extra spectrum.

The simultaneous collar is especially restrictive: two different literal full cuts are both within `7.33e-4` / `4.23e-4` Frobenius distance of rank two, while all four original quadrants between their constituent source banks carry a quantitatively nondegenerate second singular direction. Any further closure must exploit this compatibility in physical coordinates; a spectral rotation cannot be substituted for source independence.

## 7. Correction/scope audit

- Every cut and bank is a subset of the original independent coordinates.
- SVDs are deterministic coefficient decompositions only.
- No law-uniform pointwise quadratic Fourier decay is invoked.
- No arbitrary-joint coarea estimate is invoked.
- No worst-fibre density supremum is invoked.
- No small coefficient tail is removed from the random form.
- Aggregate `e_2`/`e_3` is never converted into a fictitious single universally good minor.
- Same-bank quadratic curvature and all exterior couplings stay in every density receiver.
- The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.
- Full-target continuity remains **OPEN**; continuity is asserted only on the two physical-E3-paid branches above.

## 8. Numerical checks

The constants used above are:

`c_0 =0.026275654659752182...`,
`p_* =0.0012564554392151157...`,
`Z_* =8.468700907587555e-13`,
`C_3 =10.550168831164775...`,
`C_3 Z_*^(-1/6)=1084.6508070708749...`,
`q_* =0.00013251678460471925...`,
`Z_cross=1.0466991783364748e-15`,
`C_3 Z_cross^(-1/6)=3310.9739388026574...`,
`1/(256sqrt(2))-3/4096=0.002029713989009951...>1/512`,
`21/4096=0.005126953125`,
`3/4096=0.000732421875`,
`sqrt(3)/4096=0.0004228639666916204...`.

The arithmetic is recorded separately in `CHECKS.md`. No numerical experiment is used as proof.
