# fleet03/B16 — projection/product interaction via near spectral volume + far product transversality

**Run:** `20260922T115325Z-fleet03-B16-qform-r2`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** projection-product interaction  
**Classification:** `PROVED_SUPPORTING / QUALITATIVE_GLOBAL_CLOSURE / UNIVERSAL_CONSTANT_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository sources were read, but no distinct native learned-memory receiver/context was verified.

## 0. Fresh-control redirect

The incoming invocation still asked for the older FEI signed-cancellation path. Fresh owner control instead says all eighty workers stop FEI and work only on the quadratic-form bounded-density conjecture. I therefore did no FEI mathematics.

The live target is: for independent real `X_i` with probability densities `0<=f_i<=1` and real symmetric `A` with at least three eigenvalues of absolute value at least `1`, prove a universal finite bound on the density of `Q=X^T A X`.

Corrections consumed before the proof:

* law-uniform pointwise Fresnel decay is false;
* taking a fiberwise supremum loses dimension;
* rotating to the eigenbasis preserves a joint density cap but destroys independence;
* `QFORM-CROSSMINOR-ALONE-FALSE`: a nonsingular cross block alone does not imply bounded density without the needed pivot-side structure.

The designated `fleet04/B16` partner had no completed QFORM handoff in the fresh repository snapshot, so no result was fabricated or attributed to it. I instead applied two completed compatible cross-account results:

1. **fleet01/B05** (`qform/fleet-2026-09-22/fleet01/B05/20260922T1136Z-qform-principal2d-B05-r1/REPORT.md`): a definite original-coordinate `2x2` principal block gives the exact shell bound `pi/sqrt(|det B|)`, and its Walsh example proves that no fixed coordinate pair can be uniformly nondegenerate under the target spectral hypothesis.
2. **fleet02/B07** (`proofnet24/quadratic-form-bounded-density/fleet02/B07/fleet02-B07-20260922T113436Z-qform/PEER_APPLIED.md`): the rank-three Walsh projection has eigenvalues `(1,1,1,0,...)` while every fixed-size principal block has operator norm `O(k/n)`, so any theorem below that depends on one fixed principal block is necessarily only a supporting theorem, not the universal closure.

The proof below combines B05's exact same-sign elliptical shell calculation with a different far-field mechanism that keeps the original coordinate product structure. It yields a new conclusion: **for every fixed symmetric matrix of rank at least three, the quadratic form already has some finite bounded density for every allowed product law.** What remains open is only a dimension/matrix-independent constant under the three-large-eigenvalue normalization.

---

## 1. A local theorem for an arbitrary invertible principal block

Let `k>=3`. Let `B` be a real symmetric invertible `k x k` matrix, with eigenvalues `mu_1,...,mu_k`. Define

`σ(B)=min_j |mu_j| > 0`,

and, because among `k>=3` nonzero real eigenvalues two have the same sign,

`P(B)=max{|mu_i mu_j| : i<j and mu_i mu_j>0} > 0`.

Let `v_m` denote the Euclidean volume of the unit ball in `R^m` (`v_1=2`).

### Theorem 1 — `QFORM-INVERTIBLE-PRINCIPAL-BLOCK-v1`

Let `X=(X_1,...,X_k)` have independent coordinates, each with probability density bounded by `1`. For arbitrary `b in R^k` and `c in R`, put

`q(X)=X^T B X + b^T X + c`.

For every interval `I` of length `eta` and every `R>0`,

\[
\boxed{
\Pr(q(X)\in I)
\le \eta\left[
{\pi v_{k-2}R^{k-2}\over \sqrt{P(B)}}
+{k^{3/2}\over \sigma(B)R}
\right].
}
\tag{1.1}
\]

Consequently `q(X)` is absolutely continuous and has an essentially bounded density. Optimizing `R` gives the explicit finite constant

\[
\boxed{
\|p_q\|_\infty
\le C_k(B):=(k-1)
\left({\pi v_{k-2}\over\sqrt{P(B)}}\right)^{1/(k-1)}
\left({k^{3/2}\over (k-2)\sigma(B)}\right)^{(k-2)/(k-1)}.
}
\tag{1.2}
\]

No moment, centering, support, smoothness, unimodality, or sign-definiteness assumption is used.

### Proof

Complete the square. Put

`z=x+(1/2)B^{-1}b`.

Then

`x^T Bx+b^Tx = z^T Bz - (1/4)b^T B^{-1}b`.

Coordinatewise translation preserves both independence and the bound `f_i<=1`, so it suffices to prove the estimate for `q(z)=z^T Bz` up to a harmless output translation.

Split the event into

`N_R={q(z) in I, |z|<=R}` and `F_R={q(z) in I, |z|>R}`.

#### Near region: rotate only after using the joint density cap

The translated product density is pointwise at most `1`. Orthogonally diagonalize `B`. Lebesgue measure and Euclidean radius are invariant under this rotation; we do **not** claim the rotated coordinates are independent.

Choose a same-sign eigenvalue pair `(mu_a,mu_b)` attaining `P(B)`. Fix the other `k-2` spectral coordinates. The set of the two selected coordinates for which `z^T Bz` lies in an interval of length `eta` is an elliptic annulus (after changing the overall sign if the pair is negative definite). Exactly as in the B05 two-dimensional shell calculation, its planar area is at most

`pi eta / sqrt(P(B))`.

The remaining `k-2` coordinates range inside the projection of the radius-`R` ball, whose volume is `v_{k-2}R^{k-2}`. Hence

\[
\Pr(N_R)
\le {\pi v_{k-2}R^{k-2}\over\sqrt{P(B)}}\,\eta.
\tag{1.3}
\]

This step uses only the rotated joint-density cap, not false rotated independence.

#### Far region: return to original independent coordinates

In the translated original coordinate system,

`grad q(z)=2Bz`,

so on `|z|>R`,

`|grad q(z)| >= 2 σ(B) R`.

Therefore at every far point at least one original coordinate `j` obeys

\[
|partial_j q(z)| >= {2σ(B)R\over\sqrt{k}}=:d.
\tag{1.4}
\]

Partition `F_R` measurably into `k` pieces according to a coordinate attaining the maximum absolute partial derivative (break ties deterministically). Fix `j` and condition on all coordinates other than `z_j`. Along that one-dimensional fiber, `q` is a polynomial of degree at most two. On the set `|partial_j q|>=d`, there are at most two monotone branches. The inverse-image length of an interval of length `eta` on each branch is at most `eta/d`; therefore the total admissible `z_j`-length is at most

`2 eta/d = sqrt(k) eta/(σ(B)R)`.

Because the `j`th density is at most `1`, the conditional probability of the `j`th partition piece is no larger than that quantity. The other `k-1` product densities integrate to one. Summing over `j` gives

\[
\Pr(F_R)
\le {k^{3/2}\over σ(B)R}\,\eta.
\tag{1.5}
\]

Adding (1.3) and (1.5) proves (1.1).

For `m=k-2`, minimize `aR^m+b/R`, where

`a=pi v_m/sqrt(P(B))`, `b=k^(3/2)/σ(B)`.

The optimizer satisfies `R^(m+1)=b/(ma)`, yielding (1.2). Since every interval obeys `Pr(q in I)<=C_k(B)|I|`, the output measure is dominated by `C_k(B)` times Lebesgue measure, hence has a Radon--Nikodym density bounded by `C_k(B)`. QED.

---

## 2. Explicit three-coordinate constant

For `k=3`, `v_1=2`, and (1.1) becomes

\[
\Pr(q(X)\in I)
\le \eta\left[
{2\pi R\over\sqrt{P(B)}}+{3\sqrt3\over σ(B)R}
\right].
\tag{2.1}
\]

Thus

\[
\boxed{
\|p_q\|_\infty
\le 2\sqrt{ {6\pi\sqrt3\over σ(B)\sqrt{P(B)}} }.
}
\tag{2.2}
\]

In particular, if **all three** eigenvalues of this original-coordinate `3x3` principal block satisfy `|mu_j|>=delta`, then `σ(B)>=delta` and `P(B)>=delta^2`, so

\[
\boxed{
\|p_q\|_\infty
\le {2\sqrt{6\pi\sqrt3}\over delta}
< {11.428\over delta}.
}
\tag{2.3}
\]

For `delta=1` this gives the concrete bound `11.427753682367488...`. This is not as sharp as the special elliptic `pi` or hyperbolic-plus-square `8` normal forms, but it covers **every** invertible `3x3` principal block, with arbitrary diagonal/cross-term pattern and arbitrary linear perturbation.

---

## 3. Ambient conditioning corollary

### Corollary 2 — arbitrary outside couplings are harmless once one block is invertible

Let `A` be an `n x n` real symmetric matrix. If some original-coordinate principal submatrix `B=A[J,J]`, `|J|=k>=3`, is invertible, then for every independent input vector with coordinate densities bounded by one,

\[
\|p_{X^TAX}\|_\infty \le C_k(B).
\tag{3.1}
\]

### Proof

Condition on all coordinates outside `J`. For every outside value `w`, the conditional polynomial in the selected independent coordinates has the form

`x_J^T B x_J + b(w)^T x_J + c(w)`.

Theorem 1 is uniform in the linear and constant terms, so every conditional law obeys the same interval bound `C_k(B)|I|`. Averaging over `w` preserves it. QED.

This is the exact projection/product interaction exploited here: spectral rotation is used only on a bounded near region where the full joint density cap is enough; the unbounded far region is paid using one original independent coordinate at a time, where product structure is still intact.

---

## 4. Every fixed rank-at-least-three matrix has a bounded output density

The preceding corollary becomes global after a purely algebraic fact.

### Lemma 3 — principal-rank lemma for real symmetric matrices

If a real symmetric matrix `A` has rank `r`, then it has a nonsingular principal submatrix of order `r`.

### Proof

Induct on `r`. If some diagonal entry is nonzero, pivot on that `1x1` principal block. If every diagonal entry is zero but `A` is nonzero, choose a nonzero off-diagonal entry `a_ij`; the principal block

`[[0,a_ij],[a_ij,0]]`

is invertible and serves as a `2x2` pivot. In either case, after a simultaneous permutation write

`A=[[P,C],[C^T,D]]`

with `P` the invertible principal pivot. Symmetric block elimination is a congruence taking `A` to

`diag(P, D-C^T P^{-1}C)`.

Hence the Schur complement is symmetric and has rank `r-rank(P)`. By induction it has a nonsingular principal submatrix of that order. Joining those indices to the pivot indices gives, by the Schur determinant formula, a nonsingular principal submatrix of `A` of order `r`. QED.

### Theorem 4 — `QFORM-FIXED-MATRIX-QUALITATIVE-LINF-v1`

For **every fixed real symmetric matrix `A` of rank at least three**, and every independent real input vector whose coordinate densities are bounded by one, the law of

`Q=X^TAX`

has an essentially bounded density.

The bound is finite and explicit after choosing the nonsingular principal block supplied by Lemma 3, but it may depend on `A` and its rank.

### Proof

Let `r=rank(A)>=3`. By Lemma 3 choose a nonsingular principal block `B` of order `r`. Apply Corollary 2 with `k=r`. QED.

This is stronger than the target in one qualitative direction: the assumption `|lambda_j|>=1` is unnecessary for mere boundedness at a fixed matrix; rank at least three suffices. It does **not** prove the owner's conjecture, because the owner requires one finite constant uniform over all dimensions and all matrices with three spectral singular values at least one.

The result also explains the sharp qualitative threshold: rank-one squares can have a `y^{-1/2}` singularity; rank-two opposite-sign forms can have a logarithmic singularity; every fixed rank-three-or-higher symmetric form is now covered by Theorem 4.

---

## 5. Why this does not accidentally solve the universal problem

The fleet02/B07 Walsh stress family is mandatory here. For `n=2^m`, let

`A_n=r_1r_1^T+r_2r_2^T+r_3r_3^T`

with three flat orthonormal Walsh vectors. Then `A_n` has spectrum `(1,1,1,0,...)`, exactly satisfying the target threshold, yet every fixed `k` principal block obeys

`||A_n[J,J]||_op <= 3k/n`.

In particular any invertible `3x3` principal block, when present, has all eigenvalues at most `9/n` in magnitude, so the bound (2.2) necessarily deteriorates with `n`; some triples can also be singular. Therefore neither Theorem 1 nor Theorem 4 supplies a dimension-independent target constant by selecting one fixed block.

This applies the B07 peer result directly: the remaining implication is **high-cardinality aggregation**, not another search for a uniformly curved fixed coordinate triple.

The latest correction `QFORM-CROSSMINOR-ALONE-FALSE` is also respected: no inference is made from a cross minor by itself. The far estimate uses the full invertible principal Hessian, and the near estimate uses an actual same-sign spectral pair of that Hessian.

---

## 6. What changed and what remains

### PROVED in this run

1. `QFORM-INVERTIBLE-PRINCIPAL-BLOCK-v1`, the exact near/far small-ball inequality (1.1).
2. The explicit arbitrary `3x3` principal-block constant (2.2), with `11.428/delta` when its three eigenvalues are all at least `delta` in modulus.
3. `QFORM-FIXED-MATRIX-QUALITATIVE-LINF-v1`: every fixed symmetric quadratic form of rank at least three maps every allowed product law to an essentially bounded one-dimensional density.
4. The proof retains original-coordinate product structure exactly where it is needed; it never assumes independence after rotation and never takes the refuted global fiber supremum.

### OPEN

The **universal constant** required by the owner remains open. The exact missing implication can now be phrased more sharply:

> Upgrade the A-dependent principal-block bound to a dimension-free aggregate estimate under only `s_3(A)>=1`, without selecting one fixed block. Any candidate must survive the rank-three flat Walsh projection family and must aggregate many weak original-coordinate derivatives/curvatures while preserving their common-source product structure.

A natural next mechanism is to combine the near/far decomposition here with the rank-two bilinear smoothing/Pluecker mass theorem proved by fleet03/B09: use many weak coordinates collectively in the far region rather than paying `k^{3/2}/(sigma R)` from a maximum-coordinate partition. The new theorem identifies that `k^{3/2}/sigma` term, not the two-dimensional shell term, as the precise place where delocalized aggregation is still unpaid.

## Status

Full universal quadratic-form conjecture: **OPEN / NOT PROVED**.  
Qualitative boundedness for every fixed rank-`>=3` symmetric matrix: **PROVED**.  
Universal matrix/dimension-independent constant under three `|lambda|>=1`: **OPEN**.
