# fleet01/B19 r11 — multiplicity-eight incident-volume reduction

Run: `20260924T144921Z-fleet01-B19-fixed-mult-audit-r11`  
Baseline manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Status: **new proved reduction; not a multiplicity-eight theorem.**

This note attacks the first unresolved endpoint after the independently reconstructed multiplicity-nine replacement. It is designed for the current no-pivot multiplicity-eight survivor in which a literal physical two-coordinate anchor `H` has robust crossing into its complement. It keeps all original-coordinate product structure, all signs, all complement curvature and all affine terms.

## 1. Deterministic incident-volume identity forced by `s_8`

Let `A=A^T`, let `H` be two original coordinates, put `L=H^c`, and write

`A = [[B,C],[C^T,D]]`,

where `B` is `2 x 2`, `C=A[H,L]` is `2 x |L|`, and `D=A[L,L]` is symmetric. Assume

`Delta := det(C C^T) > 0`

and `s_8(A)>=1`.

### Lemma 1: the complement retains four unit singular directions

Define

`K = [[B,C],[C^T,0]]`.

The first block row of `K` has rank at most two, and after removing it the remaining matrix is supported only in the two columns indexed by `H`, so

`rank K <=4`.

Since

`A = diag(0_H,D)+K`,

the audited nonsymmetric rank-perturbation inequality with `j=4`, `q=4` gives

`1 <= s_8(A) <= s_4(D)`.

Thus

`boxed: s_4(D)>=1.`                                                   (1)

This conclusion does not use invertibility, sign or size of the anchor self-block `B`.

### Lemma 2: a total incident three-volume is at least the anchor two-volume

Let

`P=C^T(CC^T)^(-1)C`,

the orthogonal projection in `R^L` onto the two-dimensional row space of `C`. Since `rank(DP)<=2`, Eckart--Young gives

`||D(I-P)||_op = ||D-DP||_op >= s_3(D) >= s_4(D) >=1`.

Hence also

`||D(I-P)||_F^2 >=1`.                                                (2)

For `i in L`, let `d_i` denote row `i` of `D`. The Gram determinant of the three rows obtained by adjoining `d_i` to the two rows of `C` is

`det([[C],[d_i]] [[C],[d_i]]^T)
 = Delta * ||d_i(I-P)||_2^2`.

By Cauchy--Binet, the same quantity is

`sum_(T subset L, |T|=3) det A[H union {i},T]^2`,

where row/column ordering signs disappear after squaring. Summing over `i` therefore gives the exact identity

`W_tot(H)
 := sum_(i in L) sum_(T subset L, |T|=3)
       det A[H union {i},T]^2
 = Delta ||D(I-P)||_F^2.`                                           (3)

By (2),

`boxed: W_tot(H) >= Delta.`                                         (4)

This is a target-scale statement forced solely by `s_8(A)>=1` and a rank-two physical anchor crossing.

## 2. Separate the product-usable volume from the shared-coordinate collision

Split (3) into

`W_dis(H)
 = sum_(i in L) sum_(T subset L, |T|=3, i notin T)
       det A[H union {i},T]^2`,

and

`W_col(H)
 = sum_(i in L) sum_(T subset L, |T|=3, i in T)
       det A[H union {i},T]^2`.

Then exactly

`boxed: W_dis(H)+W_col(H)=W_tot(H)>=Delta.`                         (5)

The distinction matters probabilistically. Terms in `W_dis` can be placed on genuinely disjoint original-coordinate banks and hence can be fed directly into a product-Fourier receiver. The collision terms share the physical coordinate `i` between a row and a column and cannot be silently treated as an independent crossing.

## 3. A complete receiver for the disjoint incident volume

### Theorem

Under the setup above, if `W_dis(H)>0`, then for arbitrary independent original-coordinate densities bounded by one and arbitrary affine terms,

`boxed:
 ||p_(X^TAX+b^TX+c)||_infinity
 <= C_inc W_dis(H)^(-1/6),
 C_inc = 3 * 2^(5/6) * e^(2/3)
       = 10.4114025627... .`                                      (6)

This branch has an integrable characteristic function and therefore a continuous `C_0` density.

### Proof: random physical cut

Take a fair independent partition `L=I sqcup J`. Define

`W(I,J)
 = sum_(i in I) sum_(T subset J, |T|=3)
       det A[H union {i},T]^2`.

Every term in `W_dis(H)` appears exactly when its one row coordinate is put in `I` and its three distinct column coordinates are put in `J`, an event of probability `2^-4=1/16`. Hence

`E W(I,J)=W_dis(H)/16`,

so there is a literal physical cut with

`W(I,J)>=W_dis(H)/16`.                                             (7)

Fix such a cut. Let

`C_J=A[H,J]`,

and for `i in I` let `a_i=D[i,J]`. Whenever `W(I,J)>0`, `C_J` has row rank two. Put

`S^2=det(C_J C_J^T)`

and let `P_J` be projection onto its row space. Cauchy--Binet plus the three-row Gram determinant gives the exact currency identity

`W(I,J)
 = S^2 sum_(i in I) ||a_i(I-P_J)||_2^2.`                           (8)

Write

`Z_1=sum_(i in I)||a_i(I-P_J)||_2^2`.

Thus `W(I,J)=S^2 Z_1`.

### Diffuse residual rows

If every positive residual row marginal satisfies

`||a_i(I-P_J)||_2^2/Z_1 <=1/2`,

apply the rough-law-safe grouped physical-product compiler at `(k,ell,d)=(2,1,3)`, with the two literal anchor coordinates as the promoted hub. Their joint product density is bounded by one. The compiler gives

`||p_Q||_infinity
 <= 3 * 2^(1/6) * e^(2/3)
    S^(-1/3) Z_1^(-1/6)
 = 3 * 2^(1/6) * e^(2/3) W(I,J)^(-1/6).`                          (9)

All self-curvature on `H`, all curvature inside `I` and `J`, every other crossing and every affine term stay in the phase; only original coordinates are conditioned/duplicated.

### One heavy residual row

Otherwise some physical `i in I` satisfies

`r_i^2:=||a_i(I-P_J)||_2^2>Z_1/2`.

Promote this actual coordinate `i` into the hub. The three hub-to-`J` rows have Gram determinant

`det([[C_J],[a_i]] [[C_J],[a_i]]^T)
 =S^2 r_i^2
 > W(I,J)/2.`

The exact three-hub Plancherel terminal (`k=3, ell=0`) therefore gives

`||p_Q||_infinity
 <=3 sqrt(e) (S^2 r_i^2)^(-1/6)
 <3 sqrt(e) 2^(1/6) W(I,J)^(-1/6).`                               (10)

The coefficient in (10) is smaller than the coefficient in (9). Thus in all cases

`||p_Q||_infinity
 <=3 * 2^(1/6) * e^(2/3) W(I,J)^(-1/6).`

Insert (7), noting `16^(1/6)=2^(2/3)`, to obtain (6).

No leverage assumption remains: the only potential heavy residual row is promoted as a literal original coordinate.

## 4. Consequence for the current multiplicity-eight two-anchor survivor

A concurrent B08 reduction records, in the only unpaid no-pivot `s_8` chamber it analyzes, a literal two-coordinate anchor with

`Delta=det(A[H,H^c] A[H,H^c]^T)
 >= Delta_0 := 0.3649442658... .`

This B19 note does not independently revalidate the derivation of that numerical anchor constant; it uses the peer certificate only at the following exact implication.

By (5), every such state satisfies

`W_dis(H)+W_col(H)>=Delta_0.`                                      (11)

Therefore:

- if `W_dis(H)>=Delta_0/2`, theorem (6) pays the full arbitrary-law density by

  `||p_Q||_infinity
   <= C_inc (Delta_0/2)^(-1/6)
   <13.825`,

  with a continuous `C_0` density;

- otherwise

  `boxed: W_col(H)>Delta_0/2 = 0.1824721329... .`                 (12)

Thus the near-singular two-anchor obstruction cannot remain an undifferentiated determinant singularity. After the robust crossing certificate, **either a product-usable disjoint incident three-volume closes the full law, or a universal amount of volume is forced into the explicit shared-coordinate collision tensor (12).**

## 5. First remaining multiplicity-eight obligation

The first missing inequality is now the collision receiver:

`QFORM-S8-SHARED-COORDINATE-INCIDENT3-COLLISION-PAYMENT-v1`.

One must spend

`W_col(H)
 = sum_i sum_(T contains i, |T|=3)
     det A[H union {i},T]^2`

at a universal scale, without treating the shared coordinate `i` as independent of itself and without dividing by the near-singular determinant of `A[H,H]`. A valid solution could route this collision mass to a scalar/definite physical pivot, a three-coordinate promoted hub with a genuinely disjoint residual source, or another product-preserving receiver. Equation (12) shows that no small-parameter limit remains in the amount of collision currency.

Multiplicity eight is therefore still **GAP / NOT PROVED**. The unrestricted three-eigenvalue conjecture remains open.