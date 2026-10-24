# Addendum — every fractional-mixed P2 survivor has a fixed pair- or third-order two-anchor packet

This strengthens `ADDENDUM_FRACTIONAL_MIXED.md`. Full QFORM remains **OPEN**.

Retain its notation. The completed account02/B20 P2 packet gives

`Z>1/768`, `E2(D)>1/48`.                                             (1)

The fractional mixed theorem used

`lambda=1/32`, `rho=493/500`,

and if the row-oriented fractional gate fails at a residual physical row `j`, then

`a_j+31 q_j > C0`, `C0:=8000/493`.                                  (2)

If the transposed gate also fails, choose a failing physical column `p`; with its anchored-third marginal `b_p` and natural pair-volume column marginal `r_p`,

`b_p+31 r_p > C0`.                                                   (3)

Put

`s:=q_j+r_p`.                                                        (4)

Two **different but source-compatible probability laws on physical minors** now give complementary lower bounds.

## 1. Pair-volume joint-anchor mass

Under the natural residual pair-volume law `v2`, the events

`R={row j is selected}`, `C={column p is selected}`

have probabilities `q_j,r_p`. Hence

`P_v2(R intersect C) >= q_j+r_p-1=s-1`.                             (5)

Multiplying by the total pair-volume currency `E2(D)` gives the actual fixed-row/fixed-column physical `2x2` bank

`M2(j,p):=
 sum_{k != j, q != p} det D[{j,k},{p,q}]^2`

and

`M2(j,p) >= (s-1)_+ E2(D) > (s-1)_+/48`.                            (6)

No individual `2x2` minor has been selected.

## 2. Anchored-third-volume joint-anchor mass

Adding (2)-(3) gives

`a_j+b_p > 2C0-31s`.                                                 (7)

Under the anchored-third law `w3`, union bound gives

`P_w3(R intersect C) >= a_j+b_p-1
 > 2C0-31s-1`.                                                       (8)

Thus the fixed original outer anchors `i,a` together with the new residual anchors `j,p` carry

`M3(i,j;a,p):=
 sum_{k != j, q != p} det B[{i,j,k},{a,p,q}]^2`

with

`M3(i,j;a,p)
 > (2C0-31s-1)_+ Z
 > (2C0-31s-1)_+/768`.                                               (9)

Again this is aggregate source-coordinate determinant mass, not a large-minor assertion.

## 3. Balance the two bounds

Choose the crossover `s_*` by equality of the two normalized lower bounds:

`(s_*-1)/48=(2C0-31s_*-1)/768`.                                    (10)

Since `C0=8000/493`, exact arithmetic gives

`s_*=(15+2C0)/47=23395/23171
    =1.00966725648...`,                                              (11)

and the common mass floor is

`(s_*-1)/48
 =(2C0-31s_*-1)/768
 =14/69513
 =0.000201401176758... .`                                           (12)

Therefore:

- if `s>=s_*`, (6) and `E2>1/48` imply

  `boxed: M2(j,p)>14/69513`;                                        (13)

- if `s<=s_*`, (9) and `Z>1/768` imply

  `boxed: M3(i,j;a,p)>14/69513`.                                    (14)

This proves the exhaustive theorem

## `QFORM-P2-BALANCED-TWOANCHOR-CASCADE-v1`

For every account02/B20 P2 state with `Z>1/768` and `E2(D)>1/48`, one of the following holds:

1. the fractional mixed-order Brascamp--Lieb gate of the preceding addendum holds in the row or column orientation, in which case the full ambient quadratic form has a bounded continuous density with `||p_Q||_infinity<5902`; or
2. there are fixed physical residual row and column anchors `(j,p)` with

   `sum det D[{j,k},{p,q}]^2 >14/69513`;                              (15)

   or
3. there are the original fixed anchors `(i,a)` and fixed residual anchors `(j,p)` with

   `sum det B[{i,j,k},{a,p,q}]^2 >14/69513`.                          (16)

The sums in (15)-(16) run over all admissible remaining physical row/column choices.

This is stronger than the earlier `>1/2`-hub versus nested-third formulation: it eliminates the arbitrarily small `q_j+r_p-1` issue by balancing the pair-volume and anchored-third laws. Every still-unpaid P2 state now carries a **dimension-free two-anchor determinant bank at one of two consecutive exterior orders**, with the same explicit mass floor `14/69513`.

## 4. Exact deshear forms of the two survivors

The two aggregate packets admit useful exact physical identities. Around `(j,p)`, write

`D=[[d,r^T],[c,C]]`.

Then every anchored `2x2` determinant is `d C_{kq}-c_k r_q`, so

`boxed: M2(j,p)=||dC-c r^T||_F^2`.                                  (17)

Around the two row anchors `(i,j)` and two column anchors `(a,p)`, write the corresponding physical block as

`[[P,U],[V,C]]`,

where `P` is the physical `2x2` anchor block, `U` has two rows and the remaining columns, and `V` has the remaining rows and two columns. For each remaining `(k,q)`, Laplace/Schur expansion gives

`det B[{i,j,k},{a,p,q}]
 = det(P) C_{kq} - V_{k,:} adj(P) U_{:,q}`.

Consequently

`boxed: M3(i,j;a,p)
 =||det(P) C - V adj(P) U||_F^2`.                                   (18)

Thus the remaining P2 debt is no longer an unstructured spike/dust tail: it is an explicit physical Frobenius reserve of a first- or second-level deshear residual. These identities are algebraic only; neither residual matrix is silently assigned independent random coordinates.

## 5. First remaining implication

The earliest P2 closure debt can now be stated without volume marginals:

`QFORM-P2-TWOANCHOR-DESHEAR-PAYMENT-v1` — prove a source-product density/half-Riesz payment whenever either physical reserve (17) or (18) exceeds `14/69513`, under the strict N3 hypotheses and with arbitrary same-bank blocks and outside couplings retained.

The account02/B20 zero-edge doubly-transverse and double-star branches remain separate debts. The full conjecture is not claimed solved.