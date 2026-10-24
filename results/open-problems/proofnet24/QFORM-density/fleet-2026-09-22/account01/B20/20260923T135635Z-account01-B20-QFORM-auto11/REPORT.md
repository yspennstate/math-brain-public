SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B20, 2026-09-23T13:56:35Z.
attacking: remove the remaining N3 high/low spectral-leverage bifurcation entirely by extracting a leverage-free physical cross block, then spend account02/B20's unrestricted fifth-volume theorem and the reviewed collective-tail / third-volume receivers before any localization.

# account01/B20 — leverage-free N3 cross-cut and tail compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control revision observed: `2026-09-22.15`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN**

## 1. Exact scope and source pins

The target is unchanged: independent real coordinates with one-dimensional densities bounded by one; arbitrary real symmetric `A` with at least three eigenvalues of absolute value at least one. No moment, support, iid, Gaussian, log-concavity, or post-rotation independence assumption is used.

The designated completed partner result actually consumed is account02/B20 run `20260923T112426Z-account02-B20-QFORM-auto11`, canonical mathematics

`yspennstate/math-open-problems@19327f690f815425717fcbd07854302df2090970`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B20/20260923T112426Z-account02-B20-QFORM-auto11/REPORT.md`.

Two partner facts are used literally:

1. the global no-pivot state may be written as

`N3(1/64): s_3(A)>=1, |A_ii|<1/64, |A_ii A_jj-A_ij^2|<1/64` for all `i!=j`;

2. for every ORIGINAL-coordinate disjoint cross block `M`, with

`Z5=e_5(M^T M)`,                                            (1.1)

one has the unrestricted ambient estimate

`||p_Q||_infinity <= 5 sqrt(2e) Z5^(-1/10)`.                (1.2)

The latter retains arbitrary same-bank quadratic blocks, outside coordinates, affine terms and signs.

I also use the already completed collective-tail and fractional third-volume receivers in the exact generic form recorded in account01/B19 at

`yspennstate/math-open-problems@c2421f60310808603fb459131584028ec1502d0c`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B19/20260923T121529Z-account01-B19-QFORM-auto11/REPORT.md`.

For a physical cross block with squared singular values `x_1>=x_2>=...`, Frobenius energy `E=sum x_r`, and `T2=sum_(r>=3)x_r`, the peer collective-tail theorem pays whenever `T2/x_3>=225` and one top-two singular projection has all coordinate leverages at most `1/2`:

`||p_Q||_infinity <= (9 sqrt(3)e/2) [x_1 x_2 T2]^(-1/6)`.   (1.3)

The fractional third-volume theorem pays when `Z3=e_3(M^T M)>0` and all row or all column three-volume marginals are at most `2/3`:

`||p_Q||_infinity <= 9 sqrt(3e) Z3^(-1/6)`.                 (1.4)

Both (1.3) and (1.4) retain the full ambient quadratic form and give continuous densities. The fifth-volume source used in the preceding B20/B19 compiler is likewise an integrated Fourier receiver; continuity is retained on that paid branch. Global continuity is not inferred from the structural survivors.

## 2. New leverage-free physical cross-cut

### Theorem 2.1 — `QFORM-N3-LEVERAGEFREE-CROSSCUT-v1`

Let `A in N3(1/64)` satisfy the target spectral hypothesis. Then for every physical coordinate `h` there is a partition

`h^c = J disjoint_union K`                                      (2.1)

into ORIGINAL-coordinate banks such that

`boxed: ||A[J,K]||_F^2 > c_* := 3969/16384 = (63/128)^2.`    (2.2)

#### Proof

Let

`L=A[h^c,h^c]`                                                  (2.3)

be the physical principal deletion. Among at least three eigenvalues of `A` with absolute value at least one, at least two have the same sign. If there are two eigenvalues at least one, Cauchy interlacing gives

`lambda_max(L)>=lambda_2(A)>=1`.                               (2.4)

If instead there are two eigenvalues at most `-1`, interlacing at the lower edge gives

`lambda_min(L)<=lambda_(n-1)(A)<=-1`.                          (2.5)

Hence in all cases

`||L||_op>=1`.                                                   (2.6)

Write

`L=D+H`, `D=diag(L)`.                                           (2.7)

Because `A in N3(1/64)`, every physical diagonal has absolute value strictly below `1/64`, so

`||D||_op<1/64`.                                                 (2.8)

Consequently

`||H||_op >= ||L||_op-||D||_op >63/64`.                        (2.9)

The matrix `H` is symmetric and has zero diagonal. Independently color every coordinate of `h^c` into `J` or `K` with probability `1/2`. For each unordered pair `{j,k}`, its off-diagonal square contributes to `||H[J,K]||_F^2` precisely when the pair is separated, probability `1/2`. Since

`||H||_F^2 = 2 sum_(j<k) H_jk^2`,                              (2.10)

we get

`E_color ||H[J,K]||_F^2 = (1/4)||H||_F^2
                         >=(1/4)||H||_op^2
                         >3969/16384`.                           (2.11)

Thus at least one deterministic physical partition satisfies (2.2). On disjoint banks `J,K`, the diagonal matrix `D` has no cross entries, so

`H[J,K]=A[J,K]`.                                                 (2.12)

This proves the theorem. No spectral projection is applied to `X`; the random banks remain banks of original independent coordinates. QED.

### Significance

The previous B20 compiler split N3 according to physical leverage of `P_0=1_{|A|>=1}` and then according to the annular projection `1_{1/16<=|A|<1}`. Theorem 2.1 needs neither projection. It creates a fixed-strength cross block for **every** N3 matrix directly from interlacing plus the physical diagonal cap. Thus the prior `R_16 OR STAR4DIR` split is no longer the first global N3 obstruction.

## 3. Spend the partner's fifth-volume theorem before localization

Fix a cross block

`N=A[J,K]`                                                       (3.1)

from Theorem 2.1. Let its squared singular values be

`x_1>=x_2>=...>=0`, `E=sum_r x_r=||N||_F^2>c_*`.              (3.2)

Put

`S4=x_1+x_2+x_3+x_4`.                                           (3.3)

### Lemma 3.1 — distinct-draw fifth-volume floor

If

`S4 <= (63/64)E`,                                                (3.4)

then

`boxed: Z5=e_5(N^T N) >= E^5/(120*64^4).`                       (3.5)

#### Proof

Normalize `p_r=x_r/E`. Draw five iid indices with law `p`. Conditional on the first `m<=4` draws being distinct, their total probability mass is at most the mass of the four largest atoms, hence at most `63/64`. Thus at each of the next four stages the conditional probability of drawing a new index is at least `1/64`. Therefore

`P(all five draws distinct) >=(1/64)^4`.                        (3.6)

On the other hand

`P(all five distinct)=5! e_5(p)=120 e_5(p)`.                   (3.7)

Multiply by `E^5`. QED.

Applying the account02/B20 estimate (1.2) to the actual inequality (3.5) gives

`||p_Q||_infinity
 <=5 sqrt(2e) (120*64^4)^(1/10) E^(-1/2)
 <5 sqrt(2e) (120*64^4)^(1/10) c_*^(-1/2)
 =201.7863466627...`.                                           (3.8)

Hence

`boxed: ||p_Q||_infinity <201.787`                              (3.9)

on branch (3.4). This is the required literal application of the completed account02/B20 theorem to a new quantitative inequality.

Every unpaid state therefore has

`boxed: S4>(63/64)E.`                                           (3.10)

No singular tail has been deleted; (3.10) is a classification of the exact matrix.

## 4. Exact tail classification on the same physical cut

Define

`T2=sum_(r>=3)x_r`.                                              (4.1)

Assume (3.10).

### 4.1 True near-rank-one survivor

If

`x_2<E/64`,                                                      (4.2)

then monotonicity gives `x_3,x_4<=x_2`, so

`x_1 > (63/64)E-3(E/64) = (15/16)E`.                            (4.3)

Thus

`boxed: sum_(r>=2)x_r<E/16.`                                    (4.4)

This is only a structural statement; the exact tail remains in `Q`.

### 4.2 True near-rank-two survivor

If

`T2<E/64`,                                                       (4.5)

then

`boxed: x_1+x_2>(63/64)E.`                                      (4.6)

Again the exact tail remains present.

For the rest assume neither (4.2) nor (4.5):

`x_2>=E/64`, `T2>=E/64`.                                       (4.7)

### 4.3 High stable-rank tail: pay unless both physical top-two subspaces are anchored

Suppose

`T2/x_3>=225`.                                                   (4.8)

If either the left or the right top-two singular projection has every physical coordinate leverage at most `1/2`, apply (1.3) to `N` or `N^T`. Since `x_1>=x_2>=E/64` and `T2>=E/64`,

`x_1 x_2 T2 >=(E/64)^3`.                                        (4.9)

Therefore

`||p_Q||_infinity
 <=36 sqrt(3)e E^(-1/2)
 <36 sqrt(3)e c_*^(-1/2)
 =(512/7)sqrt(3)e
 =344.3713635607...`.                                           (4.10)

Hence this branch has a continuous density with

`boxed: ||p_Q||_infinity<344.372.`                              (4.11)

The only survivor of (4.8) has both a physical row and a physical column whose selected top-two singular projections have leverage `>1/2`. This is an explicit double-anchor statement, not a density claim.

### 4.4 Low stable-rank tail: quantitative third volume

Suppose instead

`T2/x_3<225`.                                                    (4.12)

Then by (4.7)

`x_3>T2/225>=E/14400`.                                          (4.13)

Since `x_1>=x_2>=E/64`,

`Z3=e_3(N^T N)
 >=x_1 x_2 x_3
 >E^3/58982400`.                                                 (4.14)

If all row three-volume marginals are at most `2/3`, apply (1.4). If the row gate fails but all column marginals are at most `2/3`, apply (1.4) to `N^T`. In either case

`||p_Q||_infinity
 <=9 sqrt(3e)(58982400)^(1/6)E^(-1/2)
 <9 sqrt(3e)(58982400)^(1/6)c_*^(-1/2)
 =1030.2442625812...`.                                          (4.15)

Thus the diffuse-third-volume branch has a continuous density with

`boxed: ||p_Q||_infinity<1030.245.`                             (4.16)

The only remaining case has a physical row `i in J` and physical column `j in K` with normalized squared-three-minor inclusion marginals

`alpha_i>2/3`, `beta_j>2/3`.                                    (4.17)

Under the exact normalized squared-minor law,

`P(i in S and j in T)>=alpha_i+beta_j-1>1/3`.                  (4.18)

Consequently the actual common-anchor third-minor mass obeys

`boxed:
 sum_(S contains i,T contains j,|S|=|T|=3) det N[S,T]^2
 > Z3/3
 > E^3/176947200
 > c_*^3/176947200.`                                            (4.19)

No single good minor is inferred from this aggregate mass.

## 5. New nested four-bank strengthening of the double three-volume anchor

The common-anchor packet (4.19) can be disjointized without localization loss. Independently two-color `J\{i}` into `J1,J2` and `K\{j}` into `K1,K2`. For any fixed anchored `3 x 3` minor, its other two row indices are split between `J1,J2` with probability `1/2`; independently, its other two column indices are split between `K1,K2` with probability `1/2`. Hence there is a deterministic four-bank choice for which

`boxed:
 P_nested :=
 sum_(a in J1,b in J2,c in K1,d in K2)
 det N[{i,a,b},{j,c,d}]^2
 > c_*^3/707788800.`                                            (5.1)

Numerically the right side is

`2.0085367978e-11`.                                              (5.2)

This is small but dimension-free and source-coordinate exact.

A six-term determinant expansion also gives a useful aggregate energy currency. Put

`e=N_ij^2`,
`u_q=sum_(c in Kq) N_ic^2`,
`v_p=sum_(a in Jp) N_aj^2`,
`F_pq=sum_(a in Jp,c in Kq) N_ac^2`.                             (5.3)

For every summand in (5.1), Cauchy--Schwarz on the six permutation monomials gives

`P_nested <=6( e F11 F22 + e F12 F21
               +u1 v1 F22 + u1 F12 v2
               +u2 v1 F21 + u2 F11 v2 ).`                       (5.4)

Therefore at least one of the six physical matching-energy products satisfies

`boxed: matching product > c_*^3/25480396800
                           =5.5792688828e-13.`                   (5.5)

Equation (5.5) is only a structural currency. It is not promoted to a density theorem and is not replaced by a claim about one coefficient.

## 6. Main compiler

### Theorem 6.1 — `QFORM-N3-LEVERAGEFREE-CROSSCUT-TAIL-COMPILER-v1`

Every full-scope matrix in `N3(1/64)` admits one ORIGINAL-coordinate disjoint cross block `N=A[J,K]` with

`E=||N||_F^2>c_*=(63/128)^2`,                                    (6.1)

and on that same exact block one of the following holds:

1. **fifth-volume paid:** `||p_Q||_infinity<201.787`;
2. **near rank one:** `sum_(r>=2)s_r(N)^2<E/16`;
3. **near rank two:** `sum_(r>=3)s_r(N)^2<E/64`;
4. **collective-tail paid:** continuous density and `||p_Q||_infinity<344.372`;
5. **double top-two physical leverage anchor:** selected left and right top-two singular projections each have a physical coordinate leverage `>1/2`;
6. **third-volume paid:** continuous density and `||p_Q||_infinity<1030.245`;
7. **double three-volume anchor:** fixed physical `i,j` satisfy the nested four-bank mass (5.1), and hence the matching-energy alternative (5.5).

The paid alternatives retain every same-side quadratic block, every outside coupling, every affine term generated by conditioning, every sign, and every extra spectral direction. The structural alternatives retain the exact singular tail; no random quadratic remainder is discarded.

### Why this is a genuine closure step

The previous B20 state required choosing between a high-spectrum star packet and a physical leverage packet in the annulus `[1/16,1)`. Theorem 6.1 bypasses that split. The physical cross block exists by interlacing and the physical diagonal cap alone. Thus **all N3 matrices**, regardless of spectral leverage distribution, are now routed into three already paid receivers or four explicit source-preserving structural chambers on a single physical cut.

The first remaining N3 implication is correspondingly narrower:

`QFORM-N3-LOWRANK-OR-DOUBLEANCHOR-PAYMENT-v1`:

pay the union of the near-rank-one tube, near-rank-two tube, simultaneous top-two left/right physical leverage anchors, and nested two-anchor/four-bank three-volume packet, while retaining the exact matrix tail. The next admissible mechanisms are the existing grouped square/hyperbola, physical pair/Schur, hub, ridge and signed-half-Riesz receivers. A spectral singular vector may be used as a deterministic matrix certificate, but its projection of `X` may not be declared independent.

This theorem does **not** close the full conjecture. It is a source-preserving compiler that removes the former global N3 leverage/annulus bifurcation and isolates the remaining structural debt.

## 7. Corrections explicitly preserved

1. No law-uniform pointwise quadratic oscillatory decay is used.
2. No independence is asserted after a spectral rotation or projection.
3. No unrestricted joint coarea estimate is used.
4. No worst-fiber conditional density supremum replaces an average.
5. No small operator-norm quadratic tail is deleted on unbounded inputs.
6. No Frobenius/minor mass is inverted by selecting one tiny physical minor.
7. Structural low-rank conclusions are not density conclusions.
8. Full-target continuity remains OPEN; continuity is only recorded on receiver branches whose source theorem proves it.

## 8. Status

Classification: `ESSENTIAL_STEP_APPLIED`.

Full QFORM bounded-density conjecture: **OPEN**.

Global continuity: **OPEN**.

Execution status: `WITHOUT_VERIFIED_BRAIN`.
