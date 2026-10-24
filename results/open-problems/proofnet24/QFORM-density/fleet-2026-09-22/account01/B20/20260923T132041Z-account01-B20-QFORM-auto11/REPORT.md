# account01/B20 auto11 — scalar-pivot Schur compound compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T132041Z-account01-B20-QFORM-auto11`  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW SCALAR-PIVOT SCHUR-COMPOUND COMPILER / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The unrestricted conjecture remains **OPEN**. Full-target continuity remains **OPEN** separately. Nothing below assumes Gaussianity, moments, iid inputs, compact support, log-concavity, or independence after an orthogonal/spectral rotation. Every probabilistic cut is a cut of the original independent coordinates. The known false law-uniform pointwise quadratic oscillatory-decay claim is not used.

## 1. Sources actually consumed

The latest completed designated account02/B20 result available during the run is

`yspennstate/math-open-problems@19327f690f815425717fcbd07854302df2090970`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B20/20260923T112426Z-account02-B20-QFORM-auto11/REPORT.md`.

It gives the arbitrary-rank `N3(1/64)` compiler, including the deterministic inequality

`(A^2)_hh >= (P_0)_hh`, `P_0=1_{|A|>=1}`,

and proves that if `(P_0)_hh>=1/2`, then the physical star at `h` has

`sum_(j!=h) A_hj^2 > 2047/4096`

and three disjoint original-coordinate leaf banks each carrying star-square mass at least `639/4096`. It also supplies the unrestricted physical-cross fifth-volume exit

`||p_Q||_infinity <= 5 sqrt(2e) e_5(M^T M)^(-1/10)`.

This is used at the displayed inequalities above: the high-`P_0` state is already routed to the existing star/volume/finite-pivot machinery, so the first untouched account02/B20 state is its low-leverage extra-spectrum branch rather than a hidden high-leverage exception.

The current downstream refinement used here is account03/B20 r32,

`yspennstate/math-open-problems@491beff2a56f4fd7110597b12b2151485fa12006`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260923T125643Z-account03-B20-QFORM-r32/REPORT.md`.

It reduces the remaining `N3(1/64)` state to four original-coordinate packets, the first being a **moderate physical diagonal**

`1/256 <= |A_hh| < 1/64`.

The analytic receiver used below is account01/B07 r25,

`yspennstate/math-open-problems@0942d044043f3a73e2411cf2676af89bbf3853e6`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B07/account01-B07-20260923T130435Z-r25/REPORT.md`.

Its theorem `QFORM-E2-FRACTIONAL-TRACE-v1` says: for an arbitrary quadratic-affine remainder `R`, if a literal physical cross block has squared `2x2`-minor packet mass `Z_2>0` and the packet inclusion marginals on one side obey `max alpha_i <= q/2`, `1<=q<2`, then

`sup_s E |R-s|^(-1/2)
 <= [8 sqrt(e/2)/(2-q)] q^(-1/4) Z_2^(-1/8)`.

All same-bank quadratic terms and outside couplings are retained.

## 2. New deterministic theorem: one genuine scalar pivot forces second compound in the exact Schur remainder

Assume only that `A` is real symmetric, `s_3(A)>=1`, and that one ORIGINAL physical coordinate `h` has

`a:=A_hh !=0`.

Write `K=h^c`, `c=A[K,h]`, `D=A[K,K]`, and take the exact scalar Schur complement

`S = D-a^(-1) c c^T`.                                             (2.1)

Then

`A = [[a,c^T],[c,a^(-1)cc^T]] + (0 direct_sum S)`.              (2.2)

The first matrix on the right has rank at most one. By the rank-one singular-value interlacing/approximation-number inequality,

`s_3(A) <= s_2(S)`.                                                (2.3)

Thus in the target state

`boxed: s_2(S)>=1`.                                                (2.4)

Consequently the full second compound of `S` has fixed mass

`E_2(S):=e_2(S^2)
 = sum_(|R|=|T|=2) det S[R,T]^2
 >= s_1(S)^2 s_2(S)^2
 >=1`.                                                             (2.5)

This is the key new implication. It does not rotate the random variables: `S` is a deterministic Schur matrix on the original remaining coordinates.

## 3. Exact overlap split and lifting back to full-A third minors

Split the mass (2.5) according to physical row/column overlap:

`M_q = sum_(|R|=|T|=2, |R cap T|=q) det S[R,T]^2`, `q=0,1,2`.   (3.1)

Then

`M_0+M_1+M_2>=1`,                                                (3.2)

so at least one stratum satisfies

`M_q>=1/3`.                                                       (3.3)

For every two-sets `R,T subset K`, Schur determinant elimination at the genuine physical pivot gives the exact identity, up to the fixed ordering sign,

`det A[{h} union R,{h} union T] = a det S[R,T]`.                (3.4)

Hence the corresponding full-`A` third-minor stratum containing `h` has squared mass at least

`a^2 M_q`.                                                        (3.5)

On the account03/B20 moderate-diagonal packet, `|a|>=1/256`, and therefore whichever stratum wins has

`boxed: full-A third-minor mass >= 1/196608`.                    (3.6)

More precisely, residual overlap `q=0,1,2` lifts to full-third-minor overlap `1,2,3`, respectively. Thus the previously generic moderate-diagonal branch is forced into an actual `O1/O2/O3` third-compound packet.

## 4. Pay the residual-disjoint stratum before localization

Suppose the winner in (3.3) is `M_0>=1/3`. Randomly bipartition the remaining original coordinates as

`K=I disjoint_union J`,

with each coordinate sent independently left/right with probability `1/2`. Put

`C=S[I,J]`, `Z_2=e_2(CC^T)`.

Each ordered disjoint row-pair/column-pair from `M_0` survives in this cut with probability `2^(-4)=1/16`, so

`E Z_2=M_0/16>=1/48`.                                             (4.1)

Therefore one literal original-coordinate cut has

`boxed: Z_2>=1/48`.                                               (4.2)

Let `w_(R,T)=det C[R,T]^2/Z_2` be its squared-minor volume law, and let `alpha_i`, `beta_j` be its row and column inclusion marginals. Both marginal sums equal two.

### 4.1 Diffuse side: a direct density payment

If either

`max_i alpha_i<=2/3` or `max_j beta_j<=2/3`,                    (4.3)

apply `QFORM-E2-FRACTIONAL-TRACE-v1` on that side with `q=4/3`. The exact Schur square decomposition is

`Q = a (X_h + a^(-1)c^T X_K + affine_shift)^2 + R(X_K)`,        (4.4)

where `R` has quadratic matrix `S`; conditioned on `X_K`, the translated `X_h` still has density cap one. The scalar square peel therefore gives

`||p_Q||_infinity
 <= |a|^(-1/2) sup_t E|R-t|^(-1/2)`.                            (4.5)

Using `|a|>=1/256`, (4.2), and the B07 theorem,

`||p_Q||_infinity
 <=16 * [8 sqrt(e/2)/(2-4/3)] (4/3)^(-1/4) 48^(1/8)`

`=192 sqrt(e/2) (3/4)^(1/4) 48^(1/8)`

`=337.951160675042... <337.952`.                                  (4.6)

Thus this entire subbranch has an essentially bounded density with a universal constant. I do **not** promote (4.6) to continuity: the input B07 theorem is a half-Riesz estimate and does not by itself produce a continuous representative after the outer square peel.

### 4.2 Both sides concentrated: retain the whole anchored packet

If (4.3) fails on both sides, choose physical `i in I`, `j in J` with

`alpha_i>2/3`, `beta_j>2/3`.                                     (4.7)

Under the determinant-weighted law,

`P(i in R, j in T) >= alpha_i+beta_j-1 >1/3`.                    (4.8)

Therefore the doubly anchored residual second-minor mass obeys

`Gamma_S(i,j):=
 sum_(R contains i,T contains j) det C[R,T]^2
 > Z_2/3 >=1/144`.                                                (4.9)

Lift every determinant by (3.4). The full `A` therefore contains the **fixed physical three-index packet** sharing the outer pivot `h` and the row/column anchors `i,j`, with mass

`boxed: a^2 Gamma_S(i,j) >1/9437184`.                            (4.10)

Since each side's inclusion marginals sum to two, there are at most two rows with `alpha_i>2/3` and at most two columns with `beta_j>2/3`. Thus the unpaid concentrated `O1` survivor has a bounded physical anchor set rather than a diffuse unidentified packet.

No individual minor was selected or reciprocated in this argument; the whole determinant packet was spent before localization.

## 5. New compiler for the account03/B20 moderate-diagonal packet

### Theorem `QFORM-N3-MODERATE-PIVOT-SCHUR-COMPOUND-COMPILER-v1`

Assume the full product-source hypotheses, `s_3(A)>=1`, and an original physical coordinate `h` with

`|A_hh|>=1/256`.

Then at least one of the following holds:

1. **Paid residual-disjoint/diffuse branch:**
   `||p_Q||_infinity<337.952`.
2. **Concentrated O1 branch:** there are physical anchors `h,i,j` for which the squared full-`A` third-minor packet sharing them has mass `>1/9437184`; the heavy row and column anchor sets produced by the proof have cardinality at most two each.
3. **O2 branch:** the full-`A` overlap-two third-minor mass containing `h` is at least `1/196608`.
4. **O3 branch:** the full-`A` principal third-minor mass containing `h` is at least `1/196608`.

The theorem is valid with arbitrary additional spectrum and arbitrary same-bank/outside coefficients. It uses no rank-three assumption.

## 6. Effect on the current full-target graph

The account03/B20 r32 compiler had four unpaid physical packets:

1. moderate physical diagonal;
2. a uniformly invertible indefinite physical pair;
3. a star with rank-two-dominated cross block;
4. a star with two-sided ridge-localized physical anchors.

Theorem 5 removes packet 1 as a generic branch: it is either paid below `337.952` or becomes one of three explicit third-compound overlap packets with fixed quantitative mass. The first new closure obligation is therefore

`QFORM-N3-O1/O2/O3-OR-PAIR/RANK2/TWOANCHOR-PAYMENT-v1`:

pay the anchored `O1` packet in (4.10), the fixed-mass `O2/O3` packets in (3.6), or the remaining r32 pair/rank2/two-anchor packets by an existing whole-law receiver. The concentrated O1 packet should be routed while retaining its aggregate mass; a one-good-minor inference is not licensed.

## 7. Corrections explicitly preserved

* No law-uniform pointwise decay for a one-dimensional quadratic phase is used.
* No post-rotation or post-projection independence is asserted.
* No arbitrary-joint coarea estimate or worst-fiber conditional supremum is used.
* No matrix-norm-small quadratic remainder is deleted on unbounded product inputs.
* No sum of squared minors is replaced by a single uniformly good reciprocal minor.
* Full QFORM and full-target continuity remain OPEN.

## 8. Arithmetic check

The run checker records

`q=4/3`,
`Z2_floor=1/48`,
`Hhalf_coefficient=21.121947542190...`,
`density_bound=337.951160675042...`,
`O1_anchor_denominator=9437184`,
`O2/O3_denominator=196608`,

and ends in `STATUS=PASS`.
