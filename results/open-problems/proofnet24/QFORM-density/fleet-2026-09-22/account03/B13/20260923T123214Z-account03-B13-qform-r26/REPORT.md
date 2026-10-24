SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B13, 2026-09-23T12:32:14Z.
attacking: extremal-product skeleton-or-spread closure by compiling the aggregate two-hub singleton third-volume into one genuine disjoint original-coordinate cross block before any reciprocal-minor payment.

# account03/B13 r26 — aggregate bordered volume -> disjoint cross-volume or bounded physical hubs

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: extremal product laws / STRUCTURE  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full continuity: **OPEN**.

Fresh owner control during this run remained revision `2026-09-22.15`, QFORM only. The current correction inbox was reread before this report. No pointwise scalar quadratic-phase decay, post-rotation independence, arbitrary-joint coarea, bounded support/diameter, fixed fragment count, or uniformly good physical minor is used.

## 1. Completed inputs actually used

### 1.1 Designated partner account04/B13: no-attainment purification

Canonical mathematics:

`yspennstate/math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260922T231352Z-account04-B13-rough-geometric-transfer-r5/REPORT.md`.

For every bounded measurable product kernel `K`,

`sup_{0<=f_i<=1, int f_i=1} int K prod_i f_i`

is exactly the supremum over products of indicators `1_{E_i}` with `|E_i|=1`, with every `E_i` allowed to be a bounded finite union of intervals. This is equality of suprema, not an optimizer assertion. There is no single-interval, centered-uniform, bounded-diameter, or bounded-fragment reduction.

This partner theorem is applied to the new slab inequality in Section 7.

### 1.2 Newest required volume theorem

Canonical package:

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

Its fractional three-volume theorem says that for an ORIGINAL-coordinate cross block `M`, total squared three-volume `Z=e_3(M^T M)>0`, and `1<=q<3/2`, if every natural row marginal is at most `q/2`, then

`||p_Q||_inf <= [3e/((3-2q)sqrt(q))] Z^(-1/6)`,                  (1.1)

with a continuous density. Arbitrary self blocks, outside couplings and affine terms are retained.

The proof is a positive determinant expansion plus weighted AM-GM, sharp Hausdorff--Young and Brascamp--Lieb. Section 4 below applies that proof to a selected subfamily of physical minors rather than silently treating a selected sum as the full `e_3`.

### 1.3 account03/B09 aggregate rank-two stability

Canonical source:

`yspennstate/math-open-problems@dc7d419453536317f88f75407b6060c50a37b1be`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260923T114612Z-account03-B09-QFORM-r31/REPORT.md`.

Let `B in R^{T x 2}` be a full-rank two-hub/leaf cross bank, `G=B^T B`, `Delta=sqrt(det G)`, and `h=max_j b_j^T G^(-1)b_j<1`. For a symmetric leaf block `D`, its singleton augmentation volumes `Gamma_j` obey

`Gamma_j^2 = det(B_{-j}^T B_{-j}) dist(D_{-j,j}, col B_{-j})^2`. (1.2)

With `Gamma=(sum_j Gamma_j^2)^(1/2)`, the Frobenius distance to `B Sym_2 B^T + diagonal` is comparable to `Gamma/Delta`:

`Gamma/Delta <= E(B,D) <= sqrt(2) Gamma/[Delta sqrt(1-h)]`.       (1.3)

The early checkpoint of this run independently rediscovered (1.2); after reading the full B09 proof, I treat (1.2)-(1.3) as predecessor mathematics rather than claiming them again. The new step here is to compile the **aggregate** `sum Gamma_j^2` into a genuine disjoint physical cross-volume family on which the newest Fourier theorem can act.

### 1.4 Existing mixed-minor theorem and B13 entropy compiler

The arbitrary-selected-minor Fourier source is

`yspennstate/math-open-problems@66b5ff888a219c7c8e754dd25062fac6aecb2f22`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260923T001242Z-b01-qform-auto11/REPORT.md`.

It permits any probability law on nonzero physical square minors, not only the natural law on all minors. For fixed order three and row marginals at most `1/2`, it gives

`||p_Q||_inf <= 6 sqrt(e) K^(-1/6)`,                              (1.4)

where `K=exp(H+E log det^2)` is the entropy-determinant currency.

The previous account03/B13 entropy-or-six-hub proof is

`yspennstate/math-open-problems@48d2f4234b05dfa527f1119c2c3dfc4a4b941f5d`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260923T003350Z-account03-B13-qform-r20/REPORT.md`.

Its finite-alphabet LP/entropy dual argument will be applied to the selected family below.

## 2. Aggregate bordered third-volume

Fix two original hub coordinates

`U={u1,u2}`

and a disjoint leaf set `T`. Put

`B=A[T,U] in R^{T x 2}`

and let `D=A[T,T]` denote the leaf block. For each `j in T`, define

`B_j=B[T\{j},:]`,

`c_j=A[T\{j},{j}]`,

and

`Z_j := det([B_j,c_j]^T [B_j,c_j])`.                            (2.1)

Cauchy--Binet gives the exact physical expansion

`Z_j = sum_{S subset T\{j}, |S|=3} det A[S, U union {j}]^2`.     (2.2)

By the B09 singleton identity, `Z_j=Gamma_j^2`. Define the aggregate currency

`Z_* := sum_{j in T} Z_j = Gamma^2`.                              (2.3)

Thus `Z_*` is precisely the aggregate squared singleton third-volume which controls distance from the exact slope-span-plus-diagonal skeleton in (1.3). It is not the maximum of individual augmentations.

## 3. New random-cut compiler

### Theorem 3.1 — `QFORM-AGGREGATE-BORDERED-RANDOM-CUT-v1`

There is a partition of the original leaf labels

`T=R disjoint_union C`

such that the genuine original-coordinate cross block

`M=A[R, U union C]`                                                (3.1)

contains a selected order-three minor family with total squared determinant currency

`W(R,C)
 := sum_{j in C} sum_{S subset R, |S|=3}
      det A[S,U union {j}]^2`                                      (3.2)

satisfying

`boxed: W(R,C) >= (27/256) Z_*.`                                  (3.3)

No spectral rotation is made and the row and column coordinate sets in (3.1) are disjoint.

### Proof

Independently put every leaf label into `R` with probability `theta` and into `C` otherwise. Fix one term in (2.2), indexed by a distinguished `j` and a three-set `S` disjoint from `j`. It appears in (3.2) exactly when all three elements of `S` lie in `R` and `j` lies in `C`, an event of probability

`theta^3(1-theta)`.

Linearity of expectation therefore gives

`E W(R,C)=theta^3(1-theta) Z_*`.                                  (3.4)

The coefficient is maximized at `theta=3/4`, where it equals `27/256`. Hence some deterministic cut realizes at least its expectation. QED.

This is an aggregate-before-inversion statement: no individual `Gamma_j` or individual physical `3x3` minor is selected or inverted.

## 4. New selected-family fractional-volume lemma

The newest theorem (1.1) is stated for the natural law over all `3x3` minors. The following is the exact subfamily version needed here.

### Lemma 4.1 — `QFORM-SELECTED-3VOLUME-FRACTIONAL-v1`

Let `M=A[I,J]` be an original-coordinate cross block with `I cap J=empty`. Let `F` be any nonempty finite family of nonzero physical `3x3` minors `(S,T)` of `M`. Put

`W_F=sum_{(S,T) in F} det(M_ST)^2`,

`w_ST=det(M_ST)^2/W_F`,

and let

`alpha_i=P_w(i in S)`, `beta_j=P_w(j in T)`.

If `1<=q<3/2` and every row marginal satisfies `alpha_i<=q/2`, then the full ambient quadratic form has a continuous density and

`boxed:
 ||p_Q||_inf
 <= [3e/((3-2q)sqrt(q))] W_F^(-1/6).
`                                                                     (4.1)

All same-side quadratic terms, outside couplings and affine terms remain arbitrary.

### Proof

Use the same original-coordinate decoupling as the newest volume theorem. The Gaussian Brascamp--Lieb denominator contains the positive expansion

`det(D_J+M^T D_I M)
 = sum_T sum_{|S|=|T|} det(M_ST)^2 prod_{i in S}d_i prod_{j notin T}e_j.` (4.2)

Drop every positive term except those in `F`. Weighted AM--GM with the selected weights `w_ST` gives

`det(D_J+M^T D_I M)
 >= W_F prod_i d_i^{alpha_i} prod_j e_j^{1-beta_j}`.             (4.3)

The rest of the newest proof depends only on the identities

`sum_i alpha_i=sum_j beta_j=3`

and the row gate `alpha_i<=q/2`: the same sharp Hausdorff--Young estimates cancel the row factors, the column factors are bounded by `e^{3/2}`, Jensen contributes the same `q`, and exact integration of the resulting `|t|^{-3/(2q)}` envelope gives (4.1). Columns with `beta_j=1` are handled by the same endpoint convention as the source determinant expansion. QED.

This is a genuine application of the newest required theorem at an equation, not a relabeling of a total `e_3`.

## 5. Direct paid-or-one-heavy-leaf alternative

Take the cut from Theorem 3.1 and the selected family

`F={(S,U union {j}): j in C, S subset R, |S|=3, det !=0}`.      (5.1)

Its currency is `W>=27 Z_*/256`. Let `alpha_i` be its natural selected row marginals.

### Theorem 5.1 — `QFORM-BORDERED-VOLUME-OR-ONE-LEAF-v1`

If `Z_*>0`, at least one of the following holds.

**Paid selected-volume branch:** every `alpha_i<=2/3`, and then Lemma 4.1 with `q=4/3` gives

`boxed:
 ||p_Q||_inf
 <= C_sel Z_*^(-1/6)
 = C_sel Gamma^(-1/3),
`                                                                     (5.2)

where

`C_sel
 = (9 sqrt(3)e/2)(256/27)^(1/6)
 = 30.823384457000472...`.                                           (5.3)

The density is continuous in this branch.

**One-heavy-physical-leaf branch:** some original leaf `i in R` carries more than the fixed fraction

`boxed:
 H_i
 := sum_j sum_{S: i in S, |S|=3}
       det A[S,U union {j}]^2
 > (9/128) Z_*
 =0.0703125 Z_*.
`                                                                     (5.4)

Here the global sum is over all admissible `j in T\S`, so it dominates the selected incident mass.

### Proof

If every selected row marginal is at most `2/3`, (5.2) follows from Lemma 4.1 and `W>=27Z_*/256`.

Otherwise some `alpha_i>2/3`. The selected terms incident to `i` have total weight `alpha_i W`, hence exceed

`(2/3)(27/256)Z_*=(9/128)Z_*`.

Those selected terms are a subset of the global terms defining `H_i`. QED.

This turns the aggregate B09 defect into either a real Fourier exit or a **single original coordinate** carrying a dimension-free share of the aggregate augmentation currency.

## 6. Entropy-strengthened paid-or-six-leaf alternative

There is a complementary Pareto point with a better analytic constant and a stronger total captured fraction at the cost of up to six leaves.

### Theorem 6.1 — `QFORM-BORDERED-VOLUME-OR-SIX-LEAF-HUB-v1`

For the same cut and selected family, at least one of the following holds.

**Entropy-paid branch:** there is a probability law `mu` on the selected nonzero minors with every row load at most `1/2` and

`D(mu||w)<=log 64`.

Then

`boxed:
 ||p_Q||_inf
 <= C_ent Gamma^(-1/3),
`                                                                     (6.1)

where

`C_ent
 =12 sqrt(e)(256/27)^(1/6)
 =28.783339961443850...`.                                            (6.2)

The density is continuous.

**Six-leaf concentration branch:** there is a set `H subset R` with `|H|<=6` such that the global bordered currency carried by row triples meeting `H` satisfies

`boxed:
 H_H
 := sum_{j,S: S cap H != empty}
      det A[S,U union {j}]^2
 > (1701/16384) Z_*
 =0.10382080078125 Z_*.
`                                                                     (6.3)

If no row-capped law exists at all, `|H|<=5` and the selected family is hit exactly; then `H_H>=27Z_*/256`.

### Proof

Run the finite-alphabet proof from B13 r20 on the selected natural law `w`. Nothing in that proof requires the family to contain *all* minors: it uses only the finite support, its row-triple incidence and relative entropy. If a row-capped `mu` exists with divergence at most `log64`, then its entropy-determinant currency is

`K(mu)=W exp(-D(mu||w)) >= W/64`.                                  (6.4)

Apply the arbitrary-selected-minor theorem (1.4):

`||p_Q||_inf
 <=6sqrt(e)(W/64)^(-1/6)
 =12sqrt(e) W^(-1/6)
 <=C_ent Z_*^(-1/6)`.

If this entropy branch fails, the same finite dual gives at most six row labels `H` for which the selected minor mass avoiding `H` is `<1/64`. Thus selected terms meeting `H` carry more than `(63/64)W`. Since `W>=27Z_*/256`,

`(63/64)W
 >=(63/64)(27/256)Z_*
 =(1701/16384)Z_*`.

The global incident currency `H_H` dominates those selected terms. The infeasible row-cap case is the fractional-matching/vertex-cover endpoint from r20 and uses at most five rows. QED.

## 7. Required application of account04/B13 to arbitrary cap-one laws

This run uses the designated partner theorem on the actual new inequality, not as a bibliography-only citation.

Fix `A`, the cut from Theorem 3.1, and suppose either paid branch above holds. For every tuple of unit-measure bounded finite-union sets `E_i`, the selected-family Fourier argument gives, for every interval `J`,

`|{x in prod_i E_i : x^T A x in J}|
 <= C Gamma^(-1/3) |J|`,                                           (7.1)

with `C=C_sel` in Theorem 5.1 or `C=C_ent` in Theorem 6.1.

Apply account04/B13 Corollary 2.2 to the bounded kernel

`K(x)=1_{x^T A x in J}`.

Its exact supremum identity transfers (7.1), with **zero constant loss**, to every independent cap-one mass-one marginal law:

`boxed:
 P(X^T A X in J)
 <= C Gamma^(-1/3)|J|.
`                                                                     (7.2)

No optimizer, interval support, bounded diameter, centered uniform law, or uniform fragment count is introduced. The Fourier proof itself already works for rough laws; the partner transfer is an independent valid extremal-product realization of the same target-level slab inequality and is the required B13 application.

## 8. How this advances the skeleton-or-spread obstruction

The B09 theorem says `Gamma` is the correct aggregate distance currency from `B Sym_2 B^T+diagonal`. The r25 extremal-product compiler says a small Frobenius residual can be compared to its exact skeleton only on an actual compact witness and only after paying the witness's centered support spread; it cannot be deleted uniformly on arbitrary unbounded laws.

Theorems 5.1 and 6.1 add the missing analytic interface **before** that perturbative comparison:

* if the aggregate augmentation defect is not concentrated on a bounded set of physical leaves, a genuine disjoint original-coordinate cross-volume family pays it by the newest volume theorem;
* if it does not pay, one leaf carries `>9/128` of `Gamma^2`, or at most six leaves carry `>1701/16384` of `Gamma^2` under the entropy formulation;
* if `Gamma` itself is small, B09 plus the r25 slab-scale Frobenius transfer routes the witness toward the exact low-rank-plus-diagonal skeleton or forces large translation-invariant support-spread currency.

Thus a bad no-coloop two-hub witness can no longer hide a large aggregate singleton defect solely by distributing it among infinitely many tiny individual augmentations: random cutting converts a universal fraction of the aggregate into one legal disjoint cross-block before any local-minor reciprocal is paid.

For a slab ratio `rho`, the direct paid branch implies

`Gamma <= (C_sel/rho)^3`;                                           (8.1)

and the entropy-paid branch gives

`Gamma <= (C_ent/rho)^3`.                                           (8.2)

Therefore a diverging counterexample sequence in this chamber must drive the aggregate B09 defect to zero at least cubically in the slab ratio, **or** repeatedly exhibit the bounded physical-leaf concentration described above.

## 9. What is still missing

This does **not** prove full QFORM. The bare three-large-eigenvalue hypothesis has not been shown to furnish one two-hub bank with `Gamma`, `Delta` and leverage parameters bounded below/away from their bad endpoints. The concentration branch is structural; a fixed share of `Gamma^2` on one or six leaves is not by itself an analytic density bound. Small `Gamma` is not a uniformly small random quadratic perturbation on arbitrary supports.

The next B13 implication is therefore:

`QFORM-BORDERED-HUB-PLUS-EXACT-SKELETON-GLUE-v1`:

> In the strict no-pivot survivor, combine the one/six-leaf bordered-volume concentration above with the r25 slab-scale curvature graph and the existing mixed-hub/grouped-bank payments. If the aggregate defect is small, use B09's exact-skeleton approximation together with the actual compact-witness support currency; if it is concentrated, move the bounded physical leaves into the heavy side and prove that either the remaining cross bank is diffuse enough for a completed volume/Fresnel theorem or an already-paid finite physical core fires.

The argument must continue to retain arbitrary translations, separated fragments, signs and outside couplings.

Full essential-boundedness theorem: **OPEN**.  
Full continuous-density theorem: **OPEN**.  
Continuity is obtained only in the paid selected-volume/entropy branches above through the source `L^1` characteristic-function estimates.

## 10. Deterministic check

`check_r26.py` and `CHECK_OUTPUT.txt` in this directory verify on a fixed seeded symmetric matrix:

* Cauchy--Binet for every `Z_j`;
* exact enumeration of every leaf cut and
  `E W=(27/256)Z_*` at `theta=3/4`;
* the constants `C_sel=30.823384457000472...` and
  `C_ent=28.783339961443850...`;
* the exact fractions `9/128` and `1701/16384`.

The checker terminates with

`QFORM_B13_R26_BORDERED_RANDOM_CUT_CHECK_PASS`.

The finite computation corroborates the algebra; it is not a proof of the analytic inequalities.
