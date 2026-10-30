# fleet01/B12 — semidefinite-cloud and one-adverse-direction stability through physical Schur chains

**Programme:** QFORM-DENSITY-3EIG-20260922, owner revision 2026-09-22.6 at publication (run began under 2026-09-22.5)  
**Run:** B12-20260922T161722Z-r13  
**Assignment:** Additional eigenvalue control  
**Classification:** PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN  

## 1. Target and first unpaid implication

The full target remains OPEN: for every dimension, independent real coordinates with probability densities bounded by one, and every real symmetric matrix having at least three eigenvalues of absolute value at least one, prove one dimension-independent bound on the essential supremum of the density of `X^T A X`, or construct a valid counterexample. Continuity is tracked separately.

This run attacks a specific additional-eigenvalue question left after the previous Schur-chain theorem: **which arbitrarily large added spectral directions can be transported through a source-valid physical elimination chain without paying their operator norm or falsely treating a rotated remainder as independent noise?**

The new answer is sign-sensitive and exact. An arbitrary semidefinite cloud of favorable sign is monotone through every sign-matched physical Schur pivot. After that cloud, one completely arbitrary adverse spectral direction remains rank one through every nonzero physical pivot. An arbitrary small full-rank mixed-sign tail can be propagated at an explicit recursive Schur price. The resulting terminal physical triple is still covered by the existing two-same-sign-three-block theorem.

The low high-spectral-leverage branch is already closed by the source-pinned ridge-window theorem: if the spectral projection onto `|lambda(A)|>=1/64` has maximum coordinate diagonal at most `1/32`, then the density is continuous and bounded by `288 sqrt(3e)/13 < 64`. Therefore the present theorem is aimed at a complementary structured part of the high-leverage branch, not at re-proving the diffuse theorem.

No spectral rotation is used to preserve independence. The live corrections excluding law-uniform pointwise Fresnel decay, post-rotation independence, fiberwise trace bounds, and the false local-block/cross-rank-three dichotomy are respected. A final correction refresh also consumed `QFORM-ONE-HEAVY-ROW-SAME-SQUARE-ABSORPTION-FALSE-v1`; the proof below does not use the refuted heavy-row same-square absorption mechanism.

## 2. Source-pinned inputs actually used

### 2.1 Assigned partner fleet02/B12

The latest completed partner result used here is

`yspennstate/math-open-problems@c1c87a33cb9223e78b3b50398328ff73d7dc85d1`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/20260922T155613Z-fleet02-B12-qform-add-eigen-r11/REPORT.md`.

Two exact statements from that report are used.

1. If a physical scalar pivot of a base matrix is nonzero, an arbitrary symmetric rank-`r` full-matrix perturbation changes the corresponding Schur residual by rank at most `r`, provided the final pivot is also nonzero.
2. If a base matrix is perturbed by a symmetric tail of operator norm `delta<|a|` and then by an arbitrary rank-`r` matrix, the final Schur residual decomposes as base residual plus a tail of norm at most

   `delta (1+kappa)^2/(1-delta/|a|)`

   plus a rank-`r` term, where `kappa` is the Euclidean norm of the base off-diagonal pivot row divided by `|a|`.

These facts are applied recursively below, not merely cited.

### 2.2 Terminal physical-triple theorem

From

`yspennstate/math-open-problems@b3c543b40dfaef13468466fa82625303a7719af8`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/20260922T141530Z-two-samesign-threeblock/REPORT.md`,

let

`C_* = 24.183038289961516...`.

If a physical principal `3x3` block has at least two eigenvalues at least `L>0` (or at most `-L`), while the third eigenvalue is arbitrary, then after conditioning on every outside original coordinate the resulting quadratic form has an essentially bounded density with

`||p||_infinity <= C_*/L`.                                      (2.1)

The estimate is uniform in the affine tilt produced by outside conditioning. Continuity was not claimed in that source and is not imported here.

### 2.3 Previous fleet01/B12 Schur-density lift

From this worker's preceding report

`yspennstate/math-open-problems@cf8f19fd2ecfcd33387bf8b730c61b511e3d7217`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B12/B12-20260922T151637Z-r12/REPORT.md`,

if a terminal residual has density cap `M_m` and the preceding original-coordinate Schur pivots are nonzero numbers `a_1,...,a_m`, then

`M_0 <= max{ M_m, max_j 4/|a_j| }`.                            (2.2)

This follows from the source-valid dependent-square estimate

`M_(j-1) <= 2 sqrt(M_j/|a_j|)`

and never rotates the random vector.

### 2.4 One-scale ridge branch

The completed source-pinned theorem

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`

states: if `P` is the spectral projection of the full matrix `A` onto all eigenspaces with `|lambda|>=1/64`, the target spectral hypothesis holds, and

`max_i P_ii <= 1/32`,                                            (2.3)

then `X^T A X` has a continuous `C_0` density and

`||p||_infinity <= 288 sqrt(3e)/13 < 64`.                       (2.4)

All smaller eigenvalues can be nonzero, mixed-sign, arbitrarily numerous and arbitrarily oriented. This is used only to identify the already-closed low-window-leverage branch.

## 3. New exact algebra: semidefinite additions are monotone through sign-matched scalar Schur pivots

For a symmetric block matrix

`M = [[a,b^T],[b,C]]`, `a!=0`,

write

`Sc(M)=C-bb^T/a`.

The following fact is the central new algebraic observation.

### Lemma 3.1 — QFORM-SCHUR-SEMIDEFINITE-MONOTONICITY-v1

Assume `a>0`, and let `P>=0` be an arbitrary symmetric positive-semidefinite matrix of the same size. Then the first pivot of `M+P` is positive and

`Sc(M+P) >= Sc(M)`                                               (3.1)

in Loewner order.

There is no rank or operator-norm restriction on `P`, and `M` itself need not be positive semidefinite.

By reflection, if `a<0` and `P<=0`, then the final pivot remains negative and

`Sc(M+P) <= Sc(M)`.                                              (3.2)

#### Proof

Use the physical triangular shear

`L = [[1,0],[-b/a,I]]`.

Then

`L M L^T = diag(a,H)`, `H=Sc(M)`.

Congruence preserves positive semidefiniteness, so write

`L P L^T = [[p,c^T],[c,D]] >=0`.

The transformed first coordinate is the original first coordinate because the first row of `L` is `(1,0,...,0)`. Hence the final pivot is `a+p>0`. Schur complementation is invariant under this shear, so

`Sc(M+P)-H = D - cc^T/(a+p)`.                                  (3.3)

If `p=0`, positivity of the `2x2` block forces `c=0`, so the right side is `D>=0`.

If `p>0`, positivity gives the ordinary Schur inequality

`D - cc^T/p >=0`.

Therefore

`D - cc^T/(a+p)`
` = [D-cc^T/p] + [1/p-1/(a+p)] cc^T >=0`.

This proves (3.1). Apply the same statement to `-M` and `-P` to obtain (3.2). QED.

### Corollary 3.2 — QFORM-SCHUR-CHAIN-SEMIDEFINITE-MONOTONICITY-v1

Fix an original-coordinate elimination order. Suppose a base matrix `A0` has strictly positive scalar Schur pivots `a_1^(0),...,a_m^(0)` in that order. If `P>=0` is arbitrary, then the same elimination order is valid for `A0+P`, every pivot satisfies

`a_j(A0+P) >= a_j^(0) >0`,                                     (3.4)

and at every stage the residual difference relative to the base chain is positive semidefinite.

The reflected statement holds for strictly negative base pivots under an arbitrary negative-semidefinite addition.

#### Proof

Apply Lemma 3.1 inductively. After one elimination the perturbed residual equals the base residual plus a PSD matrix, so the next pivot is the base pivot plus a nonnegative diagonal entry. Repeat. QED.

This is stronger than ordinary eigenvalue monotonicity for the present purpose: it operates in the original independent coordinates and controls the *actual physical pivots and Schur residuals* used by conditional density arguments.

## 4. Direct physical-triple consequence: unlimited favorable eigenvalues plus one arbitrary adverse eigenvalue

The same sign idea gives a particularly clean terminal theorem that does not need a Schur chain.

### Theorem 4.1 — QFORM-ONE-ADVERSE-INERTIA-TRIPLE-v1

Let `T` be three original coordinates. Suppose

`A0[T,T] >= L I_3`, `L>0`.                                     (4.1)

Let `F` be an arbitrary symmetric full matrix satisfying

`nu_-(F) <= 1`,                                                 (4.2)

where `nu_-` denotes the number of negative eigenvalues counted with multiplicity. Let `S` be an arbitrary symmetric full matrix with

`||S||_op <= delta < L`.                                       (4.3)

Put

`A=A0+F+S`.

Then for every independent product input with coordinate densities bounded by one,

`||p_(X^TAX)||_infinity <= C_*/(L-delta)`.                     (4.4)

All coefficients and eigenvalues outside the physical triple, including all outside cross couplings, are unrestricted. The matrix `F` may have arbitrarily many arbitrarily large positive eigenvalues and one arbitrarily large negative eigenvalue. The small tail `S` may have arbitrary rank and mixed signs.

By reflection, if `A0[T,T]<=-L I_3` and `nu_+(F)<=1`, the same conclusion holds.

#### Proof

By Cauchy interlacing, a principal submatrix cannot have more negative eigenvalues than the full matrix, so

`nu_-(F[T,T])<=1`.

Thus the second-largest eigenvalue of the `3x3` matrix `F[T,T]` is nonnegative:

`lambda_2(F[T,T])>=0`.

Weyl and (4.1)-(4.3) give

`lambda_3(A0[T,T]+S[T,T]) >= L-delta`.

The lower Weyl inequality for three-dimensional Hermitian matrices then yields

`lambda_2(A[T,T])`
` >= lambda_3(A0[T,T]+S[T,T]) + lambda_2(F[T,T])`
` >= L-delta`.                                                 (4.5)

Hence the final physical triple has at least two eigenvalues at least `L-delta`, while its third eigenvalue is arbitrary. Apply (2.1) uniformly after conditioning on every outside original coordinate. Averaging the conditional densities preserves the same cap. QED.

This theorem is useful precisely because it prices the *adverse inertia*, not the rank or norm of the favorable spectral cloud.

## 5. Main new chain theorem: one adverse spectral direction survives an arbitrary favorable cloud

The direct triple theorem does not control a matrix whose good physical triple appears only after eliminating coupled coordinates. The partner's rank-preservation theorem and Lemma 3.1 combine to handle that situation.

Let `A0` be a symmetric base matrix, and fix distinct original-coordinate indices `i_1,...,i_m`. Eliminate them in that order. Assume every base pivot is positive, and let the terminal base residual be `H0`. Suppose there is a physical terminal triple `T` such that

`H0[T,T] >= L I_3`.                                            (5.1)

Now let `F` be arbitrary with `nu_-(F)<=1`. By spectral decomposition there is a source-exact decomposition

`F=P+R`, `P>=0`, `rank(R)<=1`, `R<=0`.                          (5.2)

Define `B=A0+P` and `A=B+R`.

### Theorem 5.1 — QFORM-SCHUR-CHAIN-ONE-ADVERSE-v1

Under the preceding hypotheses, suppose every scalar pivot of the *final* matrix `A` in the chosen physical elimination order is nonzero. Let those actual pivots be `a_1(A),...,a_m(A)`. Then

`||p_(X^TAX)||_infinity`
` <= max{ C_*/L, max_(1<=j<=m) 4/|a_j(A)| }`.                 (5.3)

In particular, if

`eta := min_j |a_j(A)| >0`,                                    (5.4)

then

`||p_(X^TAX)||_infinity <= max{C_*/L,4/eta}`.                  (5.5)

If moreover

`eta >= 4L/C_* = 0.165405188216... L`,                         (5.6)

then the arbitrary favorable cloud and the one adverse direction cost **nothing in the final terminal constant**:

`||p_(X^TAX)||_infinity <= C_*/L`.                             (5.7)

All outside completion beyond the selected chain and terminal triple is arbitrary. Reflection gives the corresponding negative-pivot theorem for `nu_+(F)<=1`.

#### Proof

First compare `B=A0+P` with `A0`. Corollary 3.2 shows that the same physical elimination order is valid for `B`, every pivot of `B` is at least the corresponding positive base pivot, and the terminal residual `H_B` satisfies

`H_B-H0>=0`.

Therefore

`H_B[T,T]>=L I_3`.                                             (5.8)

Now compare `A=B+R` with `B`. The perturbation `R` has rank at most one. At the first pivot, the assigned fleet02/B12 theorem gives

`rank(Sc(A)-Sc(B))<=1`

because the base pivot is nonzero and the actual final pivot is nonzero. The residual difference after this elimination is therefore still rank at most one. Apply the same partner theorem recursively at each subsequent pivot. By induction, at the terminal stage

`H_A = H_B + E`, `rank(E)<=1`.                                 (5.9)

Restricting to the physical terminal triple cannot increase rank. Since `H_B[T,T]>=L I_3`, rank-one eigenvalue interlacing implies that `H_A[T,T]` has at least two eigenvalues at least `L`; the third is arbitrary. The terminal quadratic form therefore has density cap `C_*/L` by (2.1).

Finally apply the previous fleet01/B12 Schur-density lift (2.2) along the actual pivots of `A`. This gives (5.3), and (5.5)-(5.7) are immediate. QED.

### Favorable-sign subcase

If `F=P>=0` has **no adverse direction**, the nonzero-final-pivot assumption is unnecessary: Corollary 3.2 says every pivot stays at least its strictly positive base value. The terminal residual remains `>=L I_3`; indeed any physical pair in the terminal triple is positive definite with determinant at least `L^2`, so the elementary two-same-sign-square bound gives terminal density at most `pi/L`. Hence

`||p||_infinity <= max{ pi/L, max_j 4/a_j^(0) }`.              (5.10)

Thus an arbitrary-rank, arbitrary-magnitude PSD cloud is genuinely free except for the pre-existing base-chain pivot floor.

## 6. Mixed-sign small-tail extension via the partner's exact Schur price

The preceding theorem permits one adverse spectral direction of unbounded magnitude but no additional full-rank mixed-sign error. We now incorporate the partner's exact tail recursion.

Keep the base chain `A0` and favorable cloud `P>=0`, and set `B=A0+P`. Along the fixed physical elimination order write the stage-`j` base residual as

`B^(j-1) = [[b_j,c_j^T],[c_j,D_j]]`, `b_j>0`,                  (6.1)

and define

`kappa_j = ||c_j||_2/b_j`.                                     (6.2)

Add one arbitrary adverse rank-one matrix `R` and an arbitrary symmetric tail `S` with `||S||_op<=delta_0`. Define recursively

`delta_j = delta_(j-1) (1+kappa_j)^2`
`          / (1-delta_(j-1)/b_j)`,                             (6.3)

whenever

`delta_(j-1) < b_j`.                                           (6.4)

### Theorem 6.1 — QFORM-SCHUR-CHAIN-SPIKE-CLOUD-TAIL-v1

Let

`A=A0+P+R+S`,                                                   (6.5)

where `P>=0`, `rank(R)<=1`, and `S` is arbitrary symmetric with `||S||<=delta_0`. Assume (6.4) for every stage, every actual final scalar pivot of `A` in the chosen order is nonzero, and

`delta_m < L`.                                                  (6.6)

Then

`||p_(X^TAX)||_infinity`
` <= max{ C_*/(L-delta_m), max_j 4/|a_j(A)| }`.                (6.7)

Thus arbitrarily many favorable large eigenvalues, one arbitrary adverse large eigenvalue, and arbitrarily many additional mixed-sign eigenvalues contained in a small operator-norm tail can coexist without any post-rotation independence assumption.

The reflected negative-chain statement also holds.

#### Proof

At stage zero compare `A` with `B`. It is `B+S+R`, with tail norm `delta_0` and rank-one spike. The assigned partner theorem gives, after one physical Schur elimination, a decomposition

`A^(1)=B^(1)+S_1+R_1`,

with `||S_1||<=delta_1` and `rank(R_1)<=1`, exactly because (6.3) is the partner's explicit tail price and the actual final pivot is nonzero.

The same hypotheses now hold at stage one relative to `B^(1)`: the tail is bounded by `delta_1`, the spike remains rank one, and (6.4) makes the base pivot stable. Iterate. At the terminal stage,

`H_A=H_B+T_m+E_m`,
`||T_m||<=delta_m`, `rank(E_m)<=1`.                             (6.8)

By Corollary 3.2, `H_B[T,T]>=L I_3`. Therefore `H_B[T,T]+T_m[T,T]` is at least `(L-delta_m)I_3`. A rank-one perturbation can move at most one of its three eigenvalues below that level. Hence `H_A[T,T]` has at least two eigenvalues at least `L-delta_m`, and (2.1) gives the terminal cap `C_*/(L-delta_m)`. Apply (2.2) along the actual pivots to obtain (6.7). QED.

The explicit dependence on every `kappa_j` is retained. A small full-matrix tail is **not** claimed to remain small through a badly conditioned physical pivot.

## 7. Concrete spectral meaning

The new theorem is not merely a matrix-order curiosity. It permits spectral phenomena that are severe from the eigenvalue point of view.

- `P>=0` may have arbitrary rank and eigenvalues tending to `+infinity`; none of those large favorable eigenvalues is charged by norm.
- The single adverse direction `R` may have arbitrarily large negative eigenvalue and arbitrarily delocalized eigenvector; only its rank matters through the Schur chain.
- `S` may contain an arbitrary number of additional positive and negative eigenvalues, as long as its full operator norm satisfies the recursive tail conditions.
- The final spectrum can therefore contain arbitrarily many very large eigenvalues of one sign, an arbitrarily large eigenvalue of the opposite sign, and an arbitrary cloud of smaller mixed-sign eigenvalues.

This is exactly the type of additional-eigenvalue stability that cannot be justified by saying the added spectral terms are independent after rotation. They are generally dependent. The argument instead uses physical-coordinate Schur identities and inertia/rank bookkeeping.

## 8. Relation to the current ridge-window branch

The source state now gives a clean conditional end-to-end split:

1. If the spectral projection onto `|lambda|>=1/64` has coordinate leverage at most `1/32`, the ridge-window theorem gives a continuous density `<64`.
2. In the complementary high-leverage regime, any matrix admitting the sign-compatible Schur-chain plus one-adverse-direction decomposition of Theorem 5.1 or 6.1 is also bounded, with the explicit constants above.
3. The remaining full-target obstruction consists of high-window-leverage matrices that admit neither a controlled inertia-one physical chain nor one of the already-paid bank/cross aggregate certificates.

This is a narrower residual than before, but it is not empty and no exhaustive decomposition has been proved.

## 9. What changed and what remains open

### New proved implications

- **Semidefinite Schur monotonicity:** a sign-matched semidefinite cloud is free through every sign-matched scalar physical Schur pivot, even when the base matrix is indefinite elsewhere.
- **One-adverse-inertia physical triple:** a positive physical triple survives any perturbation with at most one negative eigenvalue, plus an arbitrary small full-rank mixed-sign tail, with explicit density cap `C_*/(L-delta)`.
- **One-adverse-inertia Schur chain:** after an arbitrary favorable semidefinite cloud, one arbitrary adverse spectral direction remains rank one through every nonzero physical pivot; the resulting full density cap is (5.5).
- **Spike/cloud/tail chain:** an additional arbitrary full-rank small tail propagates by the exact recursive price (6.3), yielding (6.7).

### Exact unpaid implication

The bare hypothesis “at least three eigenvalues satisfy `|lambda|>=1`” does not currently imply a sign-compatible physical Schur chain with a terminal definite triple, a quantitative lower floor on the actual pivots after an adverse direction, or the low-leverage spectral-window condition. The known diffuse singleton-plus-banks constructions warn against replacing this by a fixed local-minor or fixed cross-rank dichotomy.

The next useful bridge is therefore a product-preserving **high-window-leverage decomposition** that routes a matrix either to:

- a controlled sign-compatible Schur chain of the present type;
- the existing bank/hyperbolic aggregate mechanisms; or
- a ridge-certified cross block after an allowed physical partition.

No such exhaustive bridge is proved here. Full QFORM remains OPEN.

## 10. Continuity status

The ridge-window branch (2.2) proves a continuous `C_0` density. The new inertia-one physical-triple and Schur-chain theorems above prove **essential boundedness only**. The dependent-square Schur lift does not by itself provide an `L^1` characteristic-function bound for the final variable, so no continuity claim is made for those branches.

## 11. Deterministic checks

A small deterministic numerical check bundle for this run tests only the algebraic identities, not the universal probability theorem:

- 600 random positive-pivot examples verified `Sc(A+P)-Sc(A)>=0` up to numerical tolerance for random `P>=0`;
- 600 random chains verified that a full rank-one perturbation remains rank at most one in the terminal Schur residual whenever the tested pivots were nonzero;
- the constant `4/C_*` evaluates to `0.1654051882...`.

These checks are corroboration only. The proofs are the analytic arguments above.
