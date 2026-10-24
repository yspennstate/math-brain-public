SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-23T21:44:00.800572Z.
attacking: upgrade the r41 large-hub failure to a quantitative two-original-row rank-two crossing, remove the projected-volume marginal obstruction by an actual grouped-two-hub versus exact-three-hub split, and isolate only a small Frobenius tube around a rank-two common plane.

# account03/B12 r42 — hub-pair extraction and marginal-free rank-two-plane compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: additional eigenvalue control  
Run: `20260923T214400Z-qform-eigenvalue-r42`  
Status: **PROVED SUPPORTING COMPILER / FULL QFORM OPEN**  
Continuity: the positive-transverse-residual exits below have continuous `C_0` densities; no continuity or bounded-density conclusion is asserted in the surviving rank-two-tube branch.

## 1. Scope and exact source inputs

The target is unchanged: `X_1,...,X_n` are independent ORIGINAL coordinates with scalar probability densities bounded by one; `A=A^T` is arbitrary and has at least three eigenvalues of absolute value at least one; the goal is a dimension-free universal bound on the density of `Q=X^TAX`. No moments, compact support, connected support, iid, Gaussianity, log-concavity, post-rotation independence, pointwise quadratic-phase decay, arbitrary-joint coarea, or independent-convolution treatment of an added quadratic term is used.

The immediate own predecessor is account03/B12 r41,

`yspennstate/math-open-problems@ad8a6c26a38ec733582879b8c5372306268ca95d`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260923T204505Z-qform-eigenvalue-r41/REPORT.md`.

It proves the three-square-mode pivot-row dichotomy used in Sections 2-3 below.

The analytic receiver is the checked grouped projected-crossing theorem,

`yspennstate/math-open-problems@d2f970d33fa7084f8de55412189402ac609e4da6`,

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

The designated partner actually applied in Section 7 is account04/B12 r7,

`yspennstate/math-open-problems@3df1475f988c811570dc5c249a7756d24adb51bf`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260923T191531Z-account04-B12-hybrid-square-defect-r7/REPORT.md`.

That partner theorem allows arbitrarily large signed commuting replacements, an arbitrary noncommuting packet charged only through its destructive-square tail, an arbitrary finite-rank packet, and a dense operator-norm tail, while retaining an actual ORIGINAL-coordinate square-Gram gate.

## 2. Incoming three-mode chamber

Let `H` be an ORIGINAL-coordinate set, `|H|=m>=3`, put `J=H^c`, and write

`C=A[H,H]`, `B=A[H,J]`.

Assume the FINAL matrix has the physical square-energy gate

`lambda_3((A^2)[H,H]) >= g^2`.                                    (2.1)

Because

`(A^2)[H,H]=C^2+BB^T`,                                            (2.2)

all extra spectrum, of every sign and size, is already included in the deterministic gate.

Work in the nearly-rank-one self chamber

`s_1(C)>=c`, `s_2(C)<=b`, `0<b<c/m`.                              (2.3)

Choose the literal pivot coordinate `i` exactly as in r41 from a top eigenvector of `C`. Put `K=H\{i}` and define

`alpha=c/m-b`,
`L=(c/sqrt(m)+b)/alpha`,
`d=sqrt(g^2-b^2)`.                                                 (2.4)

Write

`w=B[i,J]`, `h=||w||_2`.                                          (2.5)

The r41 proof gives

`|C_ii|>=alpha`, `s_2(B)>=d`,                                     (2.6)

and, after the scalar Schur peel,

`s_2(B#)>=Delta(h):=sqrt((d^2-h^2)_+) - Lh`.                      (2.7)

If `Delta(h)>0`, r41 already closes the branch by the scalar half-Riesz plus a literal rank-two crossing. Therefore only

`Delta(h)<=0`                                                     (2.8)

is considered below. Then r41 gives the physical hub-row lower bound

`h>=h_*:=d/sqrt(1+L^2)`.                                         (2.9)

The previous run left a two-volume/marginal obstruction behind this hub. The point of this run is that the same square-energy reserve forces a second ORIGINAL row transverse to the hub, and then the weighted-subset marginal failure itself produces a third hub.

## 3. A second original row is forced

Let `P_w` denote orthogonal projection in the `J` coefficient space onto `span{w}` and put

`R=B[K,J](I-P_w)`.                                                 (3.1)

### Lemma 3.1 — rank-two row export

One has

`boxed: ||R||_op >= s_2(B) >= d.`                                 (3.2)

Consequently there exists a literal coordinate `j in K` such that, with `b_j=B[j,J]`,

`boxed:
S_ij:=sqrt(det([w;b_j][w;b_j]^T))
     = h ||b_j(I-P_w)||_2
     >= h d/sqrt(m-1)
     >= S_*:=h_* d/sqrt(m-1).`                                   (3.3)

#### Proof

The matrix `B P_w` has rank at most one. Therefore Eckart-Young gives

`s_2(B) <= ||B-BP_w||_op = ||B(I-P_w)||_op = ||R||_op`,           (3.4)

because the pivot row of `B(I-P_w)` is zero. Hence `||R||_F>=d`, so one of its `m-1` physical rows has norm at least `d/sqrt(m-1)`. For that row, the two-row Gram determinant is exactly the squared area of `w,b_j`, namely `h^2||b_j(I-P_w)||^2`. This proves (3.3). QED.

This is stronger than the r41 conclusion. Failure of scalar Schur retention cannot leave only one uncontrolled hub row: it forces a quantitatively rank-two **literal two-coordinate crossing** from `{i,j}` into the untouched ORIGINAL-coordinate bank `J`.

## 4. Project away the forced physical hub pair

Let

`M=[w;b_j]`                                                       (4.1)

be the `2 x |J|` crossing from the two hub coordinates `{i,j}` to `J`. By (3.3), `M` has rank two and singular-value product

`S_M=s_1(M)s_2(M)=S_ij>=S_*`.                                    (4.2)

Let `P_M` be orthogonal projection in the `J` coefficient space onto the row space of `M`. For the remaining physical rows

`I=H\{i,j}`,

define the projected crossing

`C_perp=B[I,J](I-P_M)`,                                           (4.3)

and its first-volume scale

`F=||C_perp||_F`.                                                  (4.4)

The key point is that the current grouped crossing theorem with two hubs needs only **one** additional projected crossing direction (`k=2`, `ell=1`). Its only row-spread gate is the first-volume marginal condition. If that gate fails, the heavy row itself is a third literal hub and exact rank-three crossing closes the same configuration.

## 5. Marginal-free two-hub-plus-one compiler

### Theorem 5.1 — `QFORM-TWO-HUB-MARGINAL-FREE-TRANSVERSE-v1`

Under (4.1)-(4.4), if `F>0`, then the full ambient quadratic form has a continuous `C_0` density satisfying

`boxed:
||p_Q||_infinity
 <= 3*2^(5/6) (S_M F)^(-1/3)
 <= 3*2^(5/6) (S_* F)^(-1/3).`                                  (5.1)

No marginal assumption remains in the theorem statement.

#### Proof

For `ell=1`, the volume row marginals of `C_perp` are simply

`a_k=||c_k||_2^2/F^2`, `sum_k a_k=1`,                            (5.2)

where `c_k` are its physical rows.

**Case A: every `a_k<=1/2`.**

Use the grouped projected-crossing theorem with the two ORIGINAL hub coordinates `{i,j}`, so the hub projection is the identity and its joint density cap is `M_H<=1`. Split the light coordinates as `I` and `J`. The hub crossing into `J` is exactly `M` with singular product `S_M`; the projected light crossing is exactly (4.3), with `Z_1=F^2`. At `(k,ell,d)=(2,1,3)`, the theorem gives

`||p_Q||_infinity
 <= 3*2^(5/6) (S_M F)^(-1/3)`.                                  (5.3)

The characteristic function is integrable, so the density is continuous and vanishes at infinity.

**Case B: some `a_k>1/2`.**

Choose that literal coordinate `k in I`. Then

`||c_k||_2>F/sqrt(2)`.                                            (5.4)

The three rows `w,b_j,b_k` restricted to the physical column bank `J` have three-dimensional volume

`V_3
 =sqrt(det([w;b_j;b_k][w;b_j;b_k]^T))
 =S_M * dist(b_k,span(w,b_j))
 =S_M ||c_k||_2
 > S_M F/sqrt(2).`                                                (5.5)

The full crossing from the three ORIGINAL hub coordinates `{i,j,k}` to their complete complement only adds columns, so its Gram matrix is larger in Loewner order and its singular-value product is at least `V_3`.

Apply the exact-rank-three crossing theorem to these three original hub coordinates. Their joint density is bounded by one, while the orthogonal three-dimensional projection on the other side has density bounded by `2^(3/2)`. Therefore

`||p_Q||_infinity
 <= 3*sqrt(2) V_3^(-1/3)
 < 3*2^(2/3)(S_M F)^(-1/3)
 < 3*2^(5/6)(S_M F)^(-1/3).`                                    (5.6)

Again the characteristic function is integrable and the density is `C_0`. This proves (5.1). QED.

The important point is conceptual: **concentration is no longer an obstruction**. If the projected first-volume is diffuse, use the grouped theorem. If one physical row carries more than half of it, promote that row to a third hub and use exact rank-three crossing.

## 6. Rank-two-plane tube is the only survivor at a chosen scale

### Corollary 6.1 — `QFORM-THREE-MODE-HUB-PAIR-OR-R2-TUBE-v1`

Keep the assumptions of Sections 2-4 and suppose the r41 scalar-retention branch fails. For every threshold `tau>0`, one of the following holds:

1. **continuous density exit:** `F>=tau` and

   `boxed:
   ||p_Q||_infinity
   <= 3*2^(5/6)(S_* tau)^(-1/3);`                                (6.1)

2. **quantitative rank-two common-plane tube:**

   `boxed:
   dist_F(B,{rank <=2 matrices})
   <= ||B(I-P_M)||_F
   =F<tau,`                                                       (6.2)

   while the same rank-two plane is witnessed by two literal ORIGINAL rows with

   `s_1(M)s_2(M)>=S_*`.                                           (6.3)

Indeed the two hub rows lie exactly in `row(M)`, and the remaining rows contribute precisely `C_perp` after projection, so

`||B-BP_M||_F=F`.                                                 (6.4)

Thus the r41 survivor has been reduced from “large hub plus low/concentrated two-volume” to a substantially sharper object: **a quantitatively nondegenerate rank-two physical plane plus a genuinely small Frobenius off-plane tail**. All concentration cases at positive transverse scale are already paid.

This is a deterministic stability statement about the final coefficient matrix. It does not delete the tail from the random quadratic form; when `F<tau` it merely records the exact coefficient geometry that still needs a dependence-safe near-common-plane receiver.

## 7. Designated account04/B12 partner applied to an actual inequality

Use account04/B12 r7, Theorem `QFORM-HYBRID-TWO-SQUARE-PROFILES-v1`. In its explicit hostile-packet family, for any eleven-coordinate carrier `H` it gives

`sqrt(lambda_6((A^2)[H,H]))>=7/4`,                                (7.1)

and hence in particular

`sqrt(lambda_3((A^2)[H,H]))>=7/4`.                                (7.2)

The same family allows fourteen arbitrary-sign/arbitrary-magnitude commuting eigenvalue replacements except for two charged severe losses, an arbitrary full-rank noncommuting packet with rank-two destructive-square defect, an arbitrary-magnitude rank-one packet, and a dense symmetric tail of operator norm at most `1/4`. None of these terms is separated probabilistically.

In the final nearly-rank-one self chamber take

`m=11`, `g=7/4`, `c=1`, `b=1/20`.                                (7.3)

Then

`alpha=0.04090909090909091`,
`L=8.59249953412311`,
`d=1.7492855684535902`,
`h_*=0.20221799441931182`.                                       (7.4)

The new pair extraction gives

`boxed:
S_M>=S_*=h_* d/sqrt(10)
     =0.11186146737680702.`                                      (7.5)

Choose `tau=0.1`. If the scalar Schur-retention exit has already failed and the projected residual behind the forced pair has `F>=0.1`, Theorem 5.1 gives the actual target-law inequality

`boxed:
||p_Q||_infinity
 <=3*2^(5/6)(0.11186146737680702*0.1)^(-1/3)
 =23.9011839181... .`                                            (7.6)

This branch has a continuous `C_0` density.

Otherwise

`boxed:
dist_F(B,{rank<=2 matrices})<0.1`                                (7.7)

for a rank-two plane explicitly generated by two ORIGINAL rows whose crossing singular-product is at least `0.1118614673...`.

For comparison, if the selected pivot row has `h<=0.1`, r41 gives `Delta>=0.8871749662...` and the earlier scalar-retention bound `||p_Q||_(infinity,ess)<56.829`. Hence on the partner hostile-spectrum family the only branch not now closed at explicit scale is a genuinely near-rank-two physical common plane; projected-volume concentration itself is no longer a separate survivor.

## 8. Relation to the current common-plane work

Fresh common-plane synthesis elsewhere in the fleet has independently isolated rank-two common-plane cycles as a live structural endpoint. The present theorem reaches that endpoint directly from the three-square-mode rank-one-self chamber and does so with an explicit Frobenius distance and a lower bound on the physical two-row singular product. It therefore supplies a quantitative input to those common-plane receivers rather than claiming that a small coefficient tail is a small random quadratic error.

In particular, no statement here says that `F<tau` may be discarded. The full conjecture still requires a receiver uniform as `tau->0`, or a structural argument showing that this rank-two tube necessarily falls into a paid common-plane/hub mechanism.

## 9. Finite consistency check

A fixed-seed numerical checker tested 10,000 random rectangular cross blocks of varying sizes. It verified with zero violations:

- `s_2(B)<=||B[K,J](I-P_w)||_op`;
- the extracted two-row area is at least `||w|| s_2(B)/sqrt(m-1)`;
- whenever an `ell=1` row marginal exceeds `1/2`, the corresponding literal three-row crossing volume is at least `S_M F/sqrt(2)`.

Minimum observed numerical margins were approximately

`2.78e-8`, `7.78e-2`, and `3.00e-5`, respectively.

These computations are sanity checks only. The proof is the deterministic rank-one approximation, Cauchy/row averaging, exact volume identity, and the source-pinned analytic crossing theorems above.

## 10. Status and next implication

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.**

The exact B12 survivor is now:

> a final three-square-mode carrier whose nearly-rank-one self block and failed scalar Schur retention force a quantitatively nondegenerate two-row physical crossing, while the entire remaining carrier-to-outside crossing lies in an arbitrarily thin Frobenius tube around that rank-two common plane.

The next useful implication is a dependence-safe **near-common-plane stability theorem** whose constant does not deteriorate as the off-plane Frobenius tail tends to zero. Current exact-common-plane compilers should be tested at the coefficient level first; no independent-noise interpretation of the small tail is allowed.

Continuity is established on the `F>0` exits of Theorem 5.1. It is not claimed for the unresolved `F<tau` tube or for unrestricted QFORM.
