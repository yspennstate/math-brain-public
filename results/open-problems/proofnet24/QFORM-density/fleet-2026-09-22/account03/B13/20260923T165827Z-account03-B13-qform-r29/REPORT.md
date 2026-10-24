SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B13, 2026-09-23T16:58:27Z.
attacking: close the physical third-volume bi-hub branch by a 1-hub/2-cross -> 2-hub/1-cross -> 3-hub volume cascade, then reduce every physical cross block to rank at most two at scale O(1/rho).

# account03/B13 r29 — the third-volume bi-hub branch is paid by a three-stage original-coordinate volume cascade

Status: **PROVED SUPPORTING TARGET-LEVEL IMPLICATION, CONDITIONAL ONLY ON THE SOURCE-PINNED COMPLETED FOURIER RECEIVERS / FULL QFORM OPEN / FULL CONTINUITY OPEN / WITHOUT_VERIFIED_BRAIN**.

Programme: `QFORM-DENSITY-3EIG-20260922`. Role: extremal product laws. All random-variable groupings below are in ORIGINAL coordinates. Deterministic orthogonal projections are used only on coefficient rows.

## 1. Source-pinned inputs actually used

### 1.1 Account02/B13 rank-four/star alternative

Source:

`yspennstate/math-open-problems@f6ad7b994c1ba509af30fceaf45e8b464db86af8`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260923T155736Z-account02-B13-rank4star-r30/REPORT.md`.

For every disjoint ORIGINAL-coordinate physical cross block `B=A[L,R]` in a slab witness of ratio

`rho = P{Q in J}/|J|`,

put

`Z=e_3(B^T B)=sum_{|S|=|T|=3} det(B[S,T])^2`

and let `alpha_i,beta_j` be the row/column marginals of the normalized squared-third-minor law. With

`C3=9 sqrt(3e)=25.70102107534928...`,

that report proves the alternative

`(I) s_3(B)<=C3/rho`,

or

`(II) there exist physical i in L, j in R with alpha_i>2/3 and beta_j>2/3`.

In branch (II), inclusion-exclusion gives

`Z_ij/Z=P(i in S and j in T)>1/3`,

where `Z_ij` is the sum of squared `3x3` minors containing row `i` and column `j`.

### 1.2 Account01/B13 anchored-volume identity

Source:

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B13/20260923T163131Z-account01-B13-qform-auto11/REPORT.md`

(on fresh master during this run).

It records the same quantitative consequence in branch (II): if branch (I) fails, then

`Z_ij > C3^6/(3 rho^6)`

and therefore

`Z_ij^(1/6) > kappa/rho`,

where

`kappa = C3/3^(1/6) = 3^(7/3) sqrt(e)
       = 21.4008078980155...`.                                      (1.1)

I rederive the only part used here directly from `Z_ij>Z/3` and `Z>=s_3(B)^6`; no scalar Schur inversion is needed.

### 1.3 Grouped projected-crossing receiver

Source:

`yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

The complete written supporting theorem there (independent review still pending) says the following. Let `H` be a bank of `k` original hub coordinates, let `J` be a disjoint original-coordinate bank, and let `M_J` be the `k x |J|` hub-to-`J` coefficient block with singular-value product `S>0`. Project the remaining light-to-`J` crossing rows off `row(M_J)` and call the resulting matrix `C`. For an integer `ell>=1`, put `Z_ell=e_ell(CC^T)` and let the natural squared-`ell`-minor row marginals be at most `1/2`. If `d=k+ell>2`, then the full ambient quadratic form, with arbitrary same-side curvature and arbitrary internal hub functions retained, has

`||p_Q||_inf <= [d/(d-2)] 2^((k+3ell)/(2d)) exp(ell/(2d))
                 M_H^(1/d) S^(-1/d) Z_ell^(-1/(2d))`,              (1.2)

where the exponential factor is omitted for `ell=1`. If the hub bank consists of original coordinates, `M_H<=1`.

The same source also proves the exact rank-`r` crossing estimate. For three original hubs and a full-rank `3 x m` cross matrix of singular-value product `S_3`,

`||p_Q||_inf <= 3 (M_Y/S_3)^(1/3)`,

and the standard three-dimensional projection cap gives `M_Y<=2^(3/2)`, hence

`||p_Q||_inf <= 3 sqrt(2) S_3^(-1/3)`.                            (1.3)

### 1.4 Designated partner account04/B13 product purification

Source:

`yspennstate/math-open-problems@82f9b7e9372c2434f27fd1f5a65e7148663516a7`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260923T121154Z-account04-B13-nonattained-bathtub-r1/REPORT.md`.

Its Theorem 3.1 proves, without an attainment assumption, equality of the supremum of every nonnegative product functional over arbitrary cap-one mass-one marginals and over unit product indicators. In particular, a strict slab ratio for arbitrary cap-one laws can be purified with arbitrarily small ratio loss while preserving the same coefficient matrix. I apply this in Section 7 to the actual cross-block inequality proved below; no interval, centered-uniform, bounded-diameter, or fixed-fragment extremality is used.

## 2. Main claim

### Theorem 2.1 — `QFORM-BIHUB-VOLUME-CASCADE-CLOSURE-v1`

Assume the source-pinned grouped projected-crossing receiver of Section 1.3. Let `Q=X^TAX` with independent original coordinates of densities at most one. Let `J` be an interval of positive length and

`rho=P{Q in J}/|J|`.

For every disjoint original-coordinate cross block `B=A[L,R]`,

`boxed: s_3(B) <= (9 sqrt(3e))/rho.`                               (2.1)

Equivalently, the physical third-volume bi-hub alternative in account02/B13 r30 is analytically paid; it cannot survive as an additional branch.

This is not the full QFORM theorem: matrices such as the known singleton-plus-two-bank family can have all physical cross blocks of rank at most two while still having three large eigenvalues. The next structural step must classify/pay that global rank-two-cross regime.

## 3. Start from the alleged bi-hub branch

Suppose for contradiction that

`s_3(B)>C3/rho`.                                                   (3.1)

Account02/B13 r30 gives physical `i in L`, `j in R` with

`Z_ij/Z>1/3`.                                                      (3.2)

Since

`Z=e_3(B^T B)>=s_1(B)^2 s_2(B)^2 s_3(B)^2>=s_3(B)^6`,             (3.3)

we obtain

`Z_ij > C3^6/(3 rho^6)`,

hence (1.1):

`Z_ij^(1/6)>kappa/rho`, `kappa=3^(7/3)sqrt(e)`.                   (3.4)

Write the selected row of `B` as

`m=B[i,R] in R^|R|`,

and write all other rows as `n_a`, `a in L\{i}`. Since `Z_ij>0`, `m!=0`.

Let

`c_a=P_(m^perp)n_a`,

and let `C` be the matrix with rows `c_a`.

## 4. Exact row-anchor wedge identity

### Lemma 4.1 — `QFORM-ROW-ANCHORED-E3-PROJECTION-IDENTITY-v1`

With the notation above,

`boxed:
 ||m||_2^2 e_2(CC^T)
 = sum_{a<b} ||m wedge n_a wedge n_b||_2^2
 = sum_{a<b}\ sum_{|T|=3} det B[{i,a,b},T]^2.
}`                                                                      (4.1)

Consequently

`boxed: ||m||_2^2 e_2(CC^T) >= Z_ij.`                              (4.2)

#### Proof

For each pair `a,b`, orthogonal projection of `n_a,n_b` off `m` gives

`||m wedge n_a wedge n_b||^2
 = ||m||^2 ||c_a wedge c_b||^2`.

Summing over pairs gives the first equality because

`e_2(CC^T)=sum_{a<b}||c_a wedge c_b||^2`.

Cauchy-Binet expands each three-row squared volume as the sum of the squared `3x3` minors over all three-column sets `T`. The quantity `Z_ij` is only the sub-sum for triples containing column `j`, proving (4.2). QED.

Put

`Z2=e_2(CC^T)>0`.

Let

`gamma_a = [sum_{b!=a} ||c_a wedge c_b||^2]/Z2`                  (4.3)

be the natural squared-two-volume row marginals. They satisfy `sum_a gamma_a=2`.

## 5. Stage one: one original hub plus two diffuse crossing directions

Assume first

`gamma_a<=1/2` for every residual row `a`.                         (5.1)

Use original coordinate `X_i` as the single hub and take the column bank `R` as the selected `J` bank in the grouped-crossing theorem. The hub-to-`J` row is exactly `m`; every other original coordinate is left in the light bank. The projected light-to-`J` crossing matrix contains `C` as a row submatrix, so its `e_2` currency is at least `Z2`. Applying (1.2) with `(k,ell,d)=(1,2,3)` and `M_H<=1` yields

`rho <= 3*2^(7/6)*e^(1/3) (||m||^2 Z2)^(-1/6)`.                   (5.2)

By (4.2) and (3.4),

`rho < [3*2^(7/6)*e^(1/3)/kappa] rho`.                            (5.3)

The numerical factor is

`3*2^(7/6)*e^(1/3)/kappa
 =0.439195189856381... <1`.                                       (5.4)

This is impossible. Therefore some residual physical row `h` obeys

`gamma_h>1/2`.                                                     (5.5)

## 6. Stage two: two original hubs plus one diffuse crossing direction

Let `n_h` be that row and put

`c_h=P_(m^perp)n_h`.

Since `gamma_h>0`, the two hub rows `m,n_h` are linearly independent. Let

`M2=[m;n_h]`,

and denote its singular-value product by

`S2=sqrt(det(M2 M2^T))=||m|| ||c_h||`.                            (6.1)

For every remaining residual row `a`, set

`d_a=P_(span{m,n_h}^perp)n_a`,

and put

`Z1=sum_a ||d_a||^2`.                                             (6.2)

The same wedge calculation gives the exact identity

`S2^2 Z1
 = ||m||^2 sum_{a!=h} ||c_h wedge c_a||^2
 = ||m||^2 gamma_h Z2`.                                          (6.3)

Using (5.5) and (4.2),

`boxed: S2^2 Z1 > Z_ij/2.`                                       (6.4)

Define the one-volume row marginals

`delta_a=||d_a||^2/Z1`, `sum_a delta_a=1`.                        (6.5)

If every `delta_a<=1/2`, use the two original coordinates `i,h` as the hub bank. Their joint density is at most one, and their hub-to-`R` block is `M2`. Applying (1.2) with `(k,ell,d)=(2,1,3)` gives (the `ell=1` exponential factor is absent)

`rho <= 3*2^(5/6) (S2^2 Z1)^(-1/6)`
`    < 3*2^(5/6)*2^(1/6) Z_ij^(-1/6)`
`    = 6 Z_ij^(-1/6)`
`    < (6/kappa) rho`.                                            (6.6)

But

`6/kappa=0.280363247434055...<1`,                                 (6.7)

again impossible. Hence some third physical row `h2` obeys

`delta_h2>1/2`.                                                    (6.8)

## 7. Stage three: three original hubs force an exact rank-three crossing payment

Let

`M3=[m;n_h;n_h2]`.

Its singular-value product `S3` is the Euclidean three-volume of its rows. Gram-Schmidt along the previous projections gives

`S3^2=S2^2 ||d_h2||^2
     =S2^2 delta_h2 Z1
     > (1/2) S2^2 Z1
     > Z_ij/4`.                                                    (7.1)

Now take the three ORIGINAL coordinates `i,h,h2` as one side and **all remaining original coordinates** as the other side. Let `B_full` be their complete `3 x (n-3)` cross block. Its restriction to columns `R` is `M3`, so

`B_full B_full^T >= M3 M3^T`

in Loewner order and therefore its singular-value product satisfies

`S_full>=S3`.                                                      (7.2)

Apply the exact rank-three crossing theorem (1.3):

`rho <= 3 sqrt(2) S_full^(-1/3)
     <= 3 sqrt(2) S3^(-1/3)`
`     < 3 sqrt(2) 4^(1/6) Z_ij^(-1/6)`
`     = 3*2^(5/6) Z_ij^(-1/6)`
`     < [3*2^(5/6)/kappa] rho`.                                   (7.3)

The factor is

`3*2^(5/6)/kappa=0.249775257752663...<1`.                         (7.4)

This third possibility is impossible as well.

Stages 1--3 exhaust the row-marginal alternatives. Thus the alleged branch `s_3(B)>C3/rho` cannot occur, proving Theorem 2.1. QED.

## 8. Actual application of the designated account04/B13 purification theorem

The proof above may be run first on bounded finite-union unit product indicators. Fix the matrix `A`, the same physical cross block `B`, and a slab `J`. Suppose an arbitrary cap-one product law had strict ratio `rho_0` with

`s_3(B)>C3/rho_0`.                                                 (8.1)

Choose `eta>0` so small that still

`s_3(B)>C3/(rho_0-eta)`.                                          (8.2)

Account04/B13 Theorem 3.1 purifies the bounded slab kernel to a unit product-indicator witness with ratio at least `rho_0-eta`, without changing `A` or `B`. The three-stage argument then contradicts (8.2). Letting the strict margin shrink proves (2.1) for every admissible product law.

This is a zero-loss application to an actual inequality. No optimizer, single interval, centered uniform law, common support diameter, or fixed fragment count is assumed.

## 9. Quantitative consequence for every hypothetical bad slab

Every disjoint physical cross block of a slab witness now satisfies

`boxed:
 s_3(A[L,R]) <= 25.70102107535/rho.
}`                                                                      (9.1)

Therefore a hypothetical sequence of target witnesses with `rho->infinity` must make **every disjoint original-coordinate cross block asymptotically rank at most two in operator norm**.

This strictly strengthens the previously completed universal `s_5=O(1/rho)` conclusion and removes the third-volume bi-hub as an unpaid analytic endpoint.

It does **not** solve the full conjecture: the exact family

`[1] direct_sum J_m/m direct_sum (-J_m/m)`

already shows that three large eigenvalues can coexist with cross rank at most two. Such grouped-bank matrices are paid by other mechanisms, but a universal structural compiler from (9.1) to the finite list of paid rank-two/grouped-bank geometries is still missing.

## 10. First remaining implication

`QFORM-GLOBAL-RANK2-CROSS-STRUCTURE-v1`:

> Given a symmetric `A` with at least three eigenvalues of modulus at least one and the slab-induced estimate `s_3(A[L,R])<=C3/rho` for every disjoint physical cut, prove a dimension-free product-preserving payment. A valid route may classify approximate rank-two off-diagonal geometry into (i) a paid physical principal block, (ii) a bounded number of original hubs plus rank-two grouped banks, or (iii) an aggregate bank certificate already covered by the existing Fourier/half-Riesz receivers. No reciprocal tiny-minor selection, moment assumption, or deletion of an entrywise/operator-small quadratic tail on unbounded inputs is allowed.

This is now the first B13 structural obligation. The preceding r28 transverse-spread obstruction remains compatible, but the new global `s_3` estimate is a sharper matrix-side input and changes the mechanism for the next run.

## 11. Continuity

The grouped-crossing and exact-rank-three receiver branches used above each yield continuous densities in their stated scopes. Theorem 2.1 itself is a structural consequence for arbitrary slab witnesses and does **not** prove continuity of the full QFORM law. Global continuity remains open separately from essential boundedness.

## 12. Deterministic constant check

Using

`C3=9 sqrt(3e)`, `kappa=C3/3^(1/6)`,

the three contradiction factors are

`0.439195189856381...`,
`0.280363247434055...`,
`0.249775257752663...`,

all strictly below one.

No Monte Carlo or numerical density estimate is used in the proof.
