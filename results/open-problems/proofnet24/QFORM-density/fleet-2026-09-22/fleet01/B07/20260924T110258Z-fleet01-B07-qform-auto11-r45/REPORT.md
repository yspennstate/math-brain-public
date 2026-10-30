SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B07, 2026-09-24T11:02:58Z.
attacking: the r44 heavy rank-three physical-range survivor — use weighted Cauchy-Binet to route it into a partner-paid diffuse restriction or a bounded heavy set carrying exact mixed principal-minor packets.

# fleet01/B07 r45 — heavy rank-three range to diffuse payment or bounded exterior packets

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: coordinate minor selection  
Status: **NEW EXACT HEAVY-SET EXTERIOR DECOMPOSITION / DESIGNATED-PARTNER BRANCH PAID / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**

The unrestricted conjecture remains OPEN. No Gaussian, log-concavity, moment, compact-support, connected-support, iid, diagonal-basis, or independence-after-rotation assumption is used. No law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea bound, fiber-supremum argument, or deletion of a nonzero quadratic tail is used.

## 1. Source-pinned incoming state


The immediate B07 predecessor is

`yspennstate/math-open-problems@e192b40cf28c79aeb0dd3c7abcbf96f69a8f764f`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B07/20260924T100351Z-fleet01-B07-qform-auto11-r44/REPORT.md`.

On the exact-singular physical-pair branch, r44 supplies the unchanged ORIGINAL-coordinate residual principal block

`C=R+T`,                                                        (1.1)

where `R=R_C` is symmetric with `rank R<=3` and

`||T||_op = ||F_H^(4)||_op/gamma`, `gamma>=7/96`.             (1.2)

The r44 diffuse-small-tail rank-three state was paid using the designated partner fleet02/B07 r51. The remaining heavy-range state is the object of this run.

The completed designated partner result is

`yspennstate/math-open-problems@0489be649867dd226d4b6cea9ded74c973f19d46`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260924T093902Z-fleet02-B07-qform-r51/REPORT.md`.

Its theorem `QFORM-BALANCED-RANKR-CUT-v1` says that if a symmetric rank-r ORIGINAL-coordinate matrix `R0=V M V^T`, `V^T V=I_r`, has maximum physical range leverage `delta`, `rho=sqrt(r delta)<1`, then there is a literal physical partition with

`s_k(R0[I,J]) >= ((1-rho)/2) s_k(R0)`.                         (1.3)

The source-refresh portion of r51 applies the completed marginal-free physical-E3 receiver from fleet02/B03: if an actual original-coordinate crossing `B` has `e3(BB^T)>0`, then the full ambient quadratic form has a continuous density and

`||p_Q||_infinity <= C3 e3(BB^T)^(-1/6)`,
`C3=3*2^(4/3)*e^(1/3)=10.5501688311648...`.                   (1.4)

All same-bank curvature, outside couplings, affine terms and additional spectrum remain arbitrary in (1.4).

## 2. Rank-three setup and heavy physical coordinates

Assume now `rank R=3` and write

`R=U Lambda U^T`, `U^T U=I_3`,                                (2.1)

with `Lambda` nonsingular diagonal. Put

`sigma=s_3(R)=s_3(Lambda)>0`, `eta=||T||_op`.                 (2.2)

For each ORIGINAL residual coordinate let

`ell_i=||U(i,:)||_2^2`.                                      (2.3)

Then

`sum_i ell_i=3`.                                              (2.4)

Define the heavy set at the fixed threshold `1/24` by

`K={i: ell_i>1/24}`, `L=K^c`.                                (2.5)

Thus

`|K|<72`, and throughout we use the safe integer bound `|K|<=72`. (2.6)

Let

`G=U_K^T U_K`,                                                (2.7)

with eigenvalues

`1>=a_1>=a_2>=a_3>=0`.                                       (2.8)

Since `U_L^T U_L=I-G`, the same eigenbasis diagonalizes both heavy and light Gram matrices.

## 3. Exact weighted Cauchy-Binet identity

### Theorem 3.1 — `QFORM-R3-HEAVYSET-EXTERIOR-PACKET-FUNNEL-v1`

For `k=0,1,2,3`, define

`c_k := sum_{I subset O, |I|=3, |I cap K|=k} det(U_I)^2`.     (3.1)

Then

`boxed: det((I-G)+tG)=sum_(k=0)^3 c_k t^k`                    (3.2)

for every `t>=0`, and therefore

`c_0=prod_j (1-a_j)`,                                        (3.3)

`c_1=sum_i a_i prod_(j!=i)(1-a_j)`,                          (3.4)

`c_2=sum_i (1-a_i) prod_(j!=i)a_j`,                          (3.5)

`c_3=prod_j a_j`.                                            (3.6)

In particular `c_0+c_1+c_2+c_3=1`.

#### Proof

Multiply each row of `U` indexed by `K` by `sqrt(t)` and leave every row in `L` unchanged. Call the resulting matrix `U(t)`. Its Gram matrix is

`U(t)^T U(t)=U_L^T U_L+t U_K^T U_K=(I-G)+tG`.                (3.7)

Cauchy-Binet gives

`det(U(t)^T U(t))
 =sum_(|I|=3) det(U(t)_I)^2
 =sum_(|I|=3) t^(|I cap K|) det(U_I)^2`,                     (3.8)

which is (3.2). Since `I-G` and `G` commute, diagonalizing `G` gives

`det((I-G)+tG)=prod_(j=1)^3 (1-a_j+t a_j)`,                  (3.9)

and coefficient comparison proves (3.3)-(3.6). QED.

This identity tracks the entire physical third-exterior-volume law by the number of heavy coordinates in a triple; no individual tiny minor is selected.

## 4. If the heavy Gram is not dominant, designated partner r51 pays the ACTUAL matrix

Suppose first

`a_1<=1/2`.                                                   (4.1)

Then on the light physical coordinates

`G_L:=U_L^T U_L=I-G >=(1/2) I_3`.                            (4.2)

Set

`V=U_L G_L^(-1/2)`,                                          (4.3)

so `V^T V=I_3`, and rewrite the literal light principal restriction as

`R[L,L]=V (G_L^(1/2) Lambda G_L^(1/2)) V^T`.                 (4.4)

Hence

`s_3(R[L,L]) >= (1/2) sigma`.                                (4.5)

For every `i in L`, the physical range leverage of the restriction is

`delta_i = u_i^T G_L^(-1) u_i <=2 ell_i <=1/12`.             (4.6)

Thus the designated partner theorem (1.3), applied with rank `r=3`, gives a literal original-coordinate partition

`L=I disjoint_union J`                                       (4.7)

such that

`s_3(R[I,J]) >= (1/4) s_3(R[L,L]) >= sigma/8`.               (4.8)

This is an equation-level use of fleet02/B07 r51 on the present coefficient state.

Now return to the ACTUAL residual block `C=R+T`. Since every rectangular compression of `T` has operator norm at most `eta`, Weyl gives

`boxed: s_3(C[I,J]) >= sigma/8-eta.`                         (4.9)

Consequently, if

`eta<=sigma/16`,                                              (4.10)

then

`s_3(C[I,J])>=sigma/16`.                                     (4.11)

The completed marginal-free physical-E3 receiver (1.4) therefore gives the full ambient law a continuous density satisfying

`boxed:
 ||p_Q||_infinity
 <=16 C3/sigma
 =168.8027012986368.../sigma.
`                                                                 (4.12)

No coefficient tail has been discarded: (4.12) is applied to the actual crossing of `C`.

Thus, under the small-tail gate (4.10), an unpaid heavy-range state must satisfy

`a_1>1/2`.                                                     (4.13)

If (4.10) fails, the r44 anchored-fourth-compound currency is already relatively large through `eta=||F_H^(4)||_op/gamma`; this is kept as a separate branch rather than perturbatively deleted.

## 5. If `a_1>1/2`, a bounded heavy set carries one of three exact determinant packets

Assume now

`a_1>1/2`.                                                     (5.1)

Because `|K|<=72`, the exact coefficients from Section 3 force one of the following three ORIGINAL-coordinate structures.

### Case A — a heavy physical triple

If

`a_3>=1/4`,                                                    (5.2)

then also `a_2>=1/4`, and

`c_3=a_1 a_2 a_3 >1/32`.                                     (5.3)

Since there are at most

`binom(72,3)=59640`                                           (5.4)

physical triples inside `K`, some literal `H subset K`, `|H|=3`, satisfies

`boxed: det(U_H)^2 >1/1908480.`                              (5.5)

For the rank-three approximant itself,

`det R[H,H] = det(Lambda) det(U_H)^2`,                        (5.6)

hence

`boxed: |det R[H,H]| > |det Lambda|/1908480.`                 (5.7)

### Case B — one heavy physical pair carries a complete pair-to-leaf packet

Suppose

`a_3<1/4`, `a_2>=1/4`.                                       (5.8)

The term of (3.5) with the light factor `1-a_3` gives

`c_2 >=(1-a_3)a_1a_2 > (3/4)(1/2)(1/4)=3/32`.               (5.9)

Group the exact `c_2` mass by its two heavy coordinates. There are at most

`binom(72,2)=2556`                                            (5.10)

heavy pairs, so some literal `H subset K`, `|H|=2`, satisfies

`boxed:
 sum_(r in L) det(U_(H union {r}))^2 >1/27264.
`                                                                  (5.11)

Since every rank-three principal determinant has the same `det Lambda` sign factor,

`det R[I,I]=det(Lambda) det(U_I)^2`,                            (5.12)

we equivalently obtain the complete determinant-weight statement

`boxed:
 sum_(r in L) |det R[H union {r},H union {r}]|
 > |det Lambda|/27264.
`                                                                  (5.13)

This is deliberately an aggregate pair-to-leaf packet; no tiny leaf coordinate is inverted.

### Case C — one heavy physical coordinate carries a complete singleton-to-two-leaf packet

Finally suppose

`a_2<1/4`.                                                       (5.14)

Then `a_3<1/4`, and the term of (3.4) corresponding to `a_1` gives

`c_1 >=a_1(1-a_2)(1-a_3)
 >(1/2)(3/4)^2=9/32`.                                        (5.15)

There are at most 72 heavy singletons, so some literal `h in K` satisfies

`boxed:
 sum_(r<s, r,s in L) det(U_{h,r,s})^2 >1/256.
`                                                                  (5.16)

Equivalently,

`boxed:
 sum_(r<s, r,s in L) |det R[{h,r,s},{h,r,s}]|
 > |det Lambda|/256.
`                                                                  (5.17)

Again the entire determinant weight is preserved before any later conditioning or minor selection.

Cases A-C are exhaustive once (5.1) holds.

## 6. What this does and does not prove

Combining Sections 4-5 gives the exact new funnel:

**Under the r44 rank-three physical approximant state and the gate `eta<=sigma/16`, either**

1. `a_1<=1/2` and the designated fleet02/B07 r51 theorem produces an ACTUAL physical crossing of `C` with `s_3>=sigma/16`; the full ambient law has a continuous density bounded by (4.12); **or**
2. `a_1>1/2` and a bounded heavy set `K`, `|K|<=72`, carries one of the exact rank-three-approximant determinant currencies (5.7), (5.13), (5.17).

If `eta>sigma/16`, the nonzero operator tail is retained as the separate anchored-C4-large branch.

The new packet statements are for the finite-rank approximant `R`, not automatically for `C=R+T`. A high-rank operator tail can change the sum of many physical determinant weights in a dimension-dependent way even when its operator norm is small. I therefore do **not** transfer (5.13) or (5.17) to the actual matrix by a naive termwise perturbation argument. Doing so would repeat exactly the kind of dimension-loss this programme is avoiding.

The remaining analytic obligation is now sharper:

`QFORM-R3-BOUNDED-HEAVY-PACKET-TAIL-ROBUST-RECEIVER-v1`:

jointly spend the exact-singular physical pair from r43/r44, one of the bounded-heavy-set packets above, and the genuine nonzero tail `T`, or route a relatively large anchored-C4 packet. The bounded heavy set has size at most 72, but the leaf packet can remain diffuse and must be aggregated before reciprocal minor payment.

This is a supporting coordinate-selection theorem, not a proof of the full conjecture. Full QFORM remains OPEN. Continuity is proved only on the paid partner branch (4.12); no full-target continuity claim is made.

## 7. Source/status summary

- Owner control: `yspennstate/math-research-brain`, revision `2026-09-22.15`, QFORM-only.
- Predecessor: `yspennstate/math-open-problems@e192b40cf28c79aeb0dd3c7abcbf96f69a8f764f`, r44 report path above.
- Designated partner actually applied: `yspennstate/math-open-problems@0489be649867dd226d4b6cea9ded74c973f19d46`, fleet02/B07 r51 report path above.
- Actual marginal-free E3 receiver used through the partner source refresh: `yspennstate/math-open-problems@df738b7f0821d9af56dfd992cab10ecc6704e3fb`, fleet02/B03 `20260923T184716Z-fleet02-B03-QFORM-auto11/REPORT.md`.
- Brain status: `WITHOUT_VERIFIED_BRAIN`; repository retrieval/write/readback is not native learned-memory ingestion.
