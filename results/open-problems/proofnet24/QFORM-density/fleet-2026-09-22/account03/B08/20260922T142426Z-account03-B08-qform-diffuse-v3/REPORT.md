# account03/B08 — optimized full-range diffuse branch

**Run:** `20260922T142426Z-account03-B08-qform-diffuse-v3`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** `Diffuse eigenvector case`  
**Classification:** `TARGET_SUPPORTING_THEOREM`; the full conjecture remains **OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 0. Exact target and correction discipline

The target is unchanged: for every dimension `n`, every independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues satisfying `|lambda_j(A)|>=1`, prove that `Q=X^TAX` has a universally bounded density, or give a valid counterexample. No moment, support, log-concavity, identical-law, sign, or eigenbasis-independence assumptions are added below.

This report uses the live correction state. In particular it does **not** use law-uniform pointwise van-der-Corput decay, does not rotate the product law and then assert independence, and does not use an unrestricted fiber supremum.

The completed source theorem applied here is the regularized original-coordinate cross-block estimate from

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`

at

`proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`.

Its relevant consequence is: if an original-coordinate cross block `B=A[I,J]` has at least `r>2q` singular values at least `sigma`, for some `1<=q<2`, and the maximum coordinate leverage of `range(B)` on one side is at most `q/2`, then

`||p_Q||_infinity <= e r / [sqrt(2q) sigma (r-2q)]`,

and the density is continuous and vanishes at infinity. Arbitrary within-side quadratic terms, outside couplings, signs, and additional tiny singular values are retained. I read the underlying proof, including its graph Brascamp--Lieb and regularized determinant steps, before using it.

The designated partner `account04/B08` still has no completed current-QFORM handoff in the fresh shared-handoff directory; I therefore do not attribute a theorem to that worker. Consistent with the instruction to work asynchronously rather than wait, the completed cross-block theorem above is applied directly to an actual inequality.

## 1. New theorem: optimized diffuse full-range threshold

### Theorem — `QFORM-FULLRANGE-DIFFUSE-OPTIMIZED-v1`

Let

`A = U Lambda U^T`,

where the columns of `U` form an orthonormal basis of the **entire range** of `A`, and `Lambda` is invertible on that range. Assume at least three singular values of `Lambda` are at least one, equivalently at least three eigenvalues of `A` satisfy `|lambda|>=1`.

Write `u_i^T` for the rows of `U` and assume

`max_i ||u_i||_2^2 <= epsilon`.

Define

`delta(epsilon) = 1/2 - epsilon - sqrt(2 epsilon)`.

If

`epsilon < epsilon_* := (39 - 6 sqrt(30))/98 = 0.0626188423...`,

then for every `q` satisfying

`max(1, 2 epsilon/delta(epsilon)) <= q < 3/2`,

and for every admissible independent product input law,

`Q=X^TAX`

has a bounded **continuous** density satisfying

`||p_Q||_infinity
 <= 3e / [sqrt(2q) delta(epsilon) (3-2q)].`

All additional nonzero eigenvalues of `A` may be arbitrarily small or large and of either sign. No assumption is made on moments, supports, or the laws beyond independence and the cap `f_i<=1`.

### Proof

Because the rows of `U` form a tight frame,

`sum_i u_i u_i^T = I`.

Apply the two-part Marcus--Spielman--Srivastava frame partition used in the completed source proof. There is a partition of the **original physical coordinates** into `I union J` such that

`M_I := U_I^T U_I <= beta I`,
`M_J := U_J^T U_J <= beta I`,

where

`beta = (1/sqrt(2) + sqrt(epsilon))^2
      = 1/2 + epsilon + sqrt(2 epsilon)`.

Since `M_I+M_J=I`, both also satisfy

`M_I, M_J >= delta I`,

with

`delta = 1-beta = 1/2 - epsilon - sqrt(2 epsilon)`.

The assumed range of `epsilon` makes `delta>0`, so both restricted frames have full column rank.

Consider the **actual full-matrix** original-coordinate cross block

`B=A[I,J]=U_I Lambda U_J^T`.

Using polar decompositions

`U_I=Q_I M_I^(1/2)`, `U_J=Q_J M_J^(1/2)`

with `Q_I,Q_J` isometries, the nonzero singular values of `B` are exactly those of

`M_I^(1/2) Lambda M_J^(1/2)`.

For every singular-value index `k`,

`s_k(B) >= s_min(M_I^(1/2)) s_k(Lambda) s_min(M_J^(1/2))
        >= delta s_k(Lambda)`.

Hence `B` has at least three singular values at least

`sigma=delta`.

Because `Lambda`, `M_I`, and `M_J` are invertible on the range dimension,

`range(B)=range(U_I)`.

The coordinate leverage of this range at an index `i in I` equals

`u_i^T M_I^(-1) u_i`

and therefore is at most

`epsilon/delta`.

Thus the completed regularized cross-block theorem applies whenever

`epsilon/delta <= q/2`.

Taking only the three guaranteed cross singular values gives `r=3`. Its integrability condition is

`3>2q`,

that is `q<3/2`. Therefore any

`max(1,2epsilon/delta) <= q <3/2`

is valid and gives

`||p_Q||_infinity
 <= 3e/[sqrt(2q) delta (3-2q)].`

The source theorem also gives continuity and vanishing at infinity because the resulting characteristic-function majorant is in `L^1`.

It remains only to characterize when such a `q` exists. This requires

`epsilon/delta < 3/4`.

Substituting `delta=1/2-epsilon-sqrt(2epsilon)` gives

`4epsilon < 3delta`

iff

`7epsilon + 3sqrt(2epsilon) < 3/2`.

Set `x=sqrt(2epsilon)`. Then this is

`7x^2+6x-3<0`.

The positive root is

`x_*=(sqrt(30)-3)/7`,

so

`epsilon < x_*^2/2
         = (39-6sqrt(30))/98 = epsilon_*.`

This proves the theorem. QED.

## 2. Explicit clean corollary at leverage 1/16

The preceding threshold is close to `0.06262`. A simple exact corollary is obtained from

`epsilon = 1/16 < epsilon_*`.

Then

`delta = 7/16 - sqrt(2)/4 = (7-4sqrt(2))/16`,

and

`epsilon/delta = 1/(7-4sqrt(2)) = (7+4sqrt(2))/17`.

Choose

`q=149/100`.

The leverage requirement is rigorous because

`(7+4sqrt(2))/17 < 149/200`.

Indeed this is equivalent to

`800sqrt(2)<1133`,

and squaring positive sides gives

`1,280,000 < 1,283,689`.

Hence every target matrix whose **entire range projection** has diagonal at most `1/16` satisfies

`||p_Q||_infinity
 <= 150e / [sqrt(149/50) delta]
 = 2400e(7+4sqrt(2)) / [17 sqrt(149/50)]
 < 2814.`

The density is continuous and vanishes at infinity. The exact arithmetic behind this corollary is also recorded in `verify_threshold.py` in the same immutable run directory.

This materially enlarges the previously supplied full-spectrum diffuse-range branch from leverage `1/32` to `1/16`, nearly a factor of two in allowed maximum coordinate leverage, while preserving arbitrary extra eigenvalues of either sign and arbitrary magnitude.

## 3. Why this is target-relevant but not the full theorem

This is not an easy diagonal or sign-restricted subclass: the matrix may be indefinite, rotated, high rank, and have arbitrary extra eigenvalues. The only extra hypothesis is geometric delocalization of the **entire range projection**.

The remaining obstruction is structural. A full-rank matrix has range projection equal to the identity, hence leverage one on every coordinate and lies entirely outside this branch. More generally, even if the three large eigenvectors themselves are diffuse, additional spectral directions can make the full range highly localized. The completed cross-block estimate requires leverage control of the actual full cross-block range, so one cannot silently replace full-range leverage by selected-large-eigenspace leverage.

Thus the first unpaid implication is:

> Convert delocalization of the three-large-eigenvalue spectral subspace, possibly in the presence of a highly localized arbitrary spectral remainder, into either (i) a full original-coordinate cross block with three large singular values and controlled actual range leverage, or (ii) a complementary localized-coordinate smoothing estimate.

That implication is not proved here.

## 4. Relation to the previous B08 run

The previous B08 run proved:

1. a block-remainder theorem when the spectral remainder has no cross interaction across a suitable physical partition; and
2. a `3e` bound for every rank-three definite form, including heavy leverage.

The present result attacks a different bottleneck: it keeps **all** spectral directions and optimizes the quantitative frame-partition / fractional-exponent interface. Therefore this is not a repetition of the previous block-diagonal remainder mechanism.

## 5. Status

**Proved here:**

- `QFORM-FULLRANGE-DIFFUSE-OPTIMIZED-v1` with exact threshold
  `epsilon_*=(39-6sqrt(30))/98`;
- explicit continuous-density corollary for maximum full-range coordinate leverage `<=1/16`, with universal constant `<2814`;
- arbitrary additional eigenvalues, signs, dimension, and admissible independent coordinate laws are retained.

**Not proved here:**

- the unrestricted three-large-eigenvalue conjecture;
- a reduction from selected-large-eigenspace delocalization to full-range delocalization;
- the heavy/full-rank localized complement.

The full QFORM conjecture therefore remains **OPEN**.
