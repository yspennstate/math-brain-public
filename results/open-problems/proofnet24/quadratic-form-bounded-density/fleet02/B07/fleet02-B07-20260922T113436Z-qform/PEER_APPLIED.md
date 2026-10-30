# fleet02/B07 — peer-applied addendum: delocalized rank-three obstruction to fixed coordinate-block extraction

**Run:** `fleet02-B07-20260922T113436Z-qform`  
**Classification:** `CANDIDATE_REFUTED / STRUCTURAL_NO-GO / FULL_TARGET_OPEN`.

## 1. Peer results consumed

After the initial report was frozen, two complete other-account results became available and were read directly.

1. **fleet03/B17**, source commit `c64fcff680b0a252a3c92002c60eedba02bbb9ec`, `qform/fleet-2026-09-22/fleet03/B17/fleet03-B17-20260922T112131Z/REPORT.md`: proves the complete coordinate-diagonal branch with the sharper constant `pi`, and gives the stronger pointwise-Fresnel no-go `sup_f |E exp(isX^2)|=1` for every nonzero `s`.
2. **fleet01/B12**, source commit `e423d315ae772630a32bc826c5abb58a5ad09c95`, `qform/fleet-2026-09-22/fleet01/B12/20260922T112049Z-fleet01-B12-qform-r1/REPORT.md`: proves a genuinely non-diagonal conditional block theorem for a principal block `[[0,a,0],[a,0,0],[0,0,lambda]]`, `|a|,|lambda|>=1`, with density bound `8`, and proposes as one possible next route a dimension-free extraction of a product-preserving coordinate block from the three-large-eigenvalue hypothesis.

The present addendum applies B12's proposed structural route to an exact delocalized family and refutes it in any fixed block size.

## 2. Exact delocalized rank-three family

Let `n=2^m` with `m>=2`, index coordinates by `x in {0,1}^m`, and define three Walsh vectors

\[
r_1(x)=n^{-1/2},\qquad
r_2(x)=n^{-1/2}(-1)^{x_1},\qquad
r_3(x)=n^{-1/2}(-1)^{x_2}.
\]

They are pairwise orthonormal. Set

\[
A_n=r_1r_1^T+r_2r_2^T+r_3r_3^T.
\]

Then `A_n` is the orthogonal projection onto `span{r_1,r_2,r_3}`. Hence its spectrum is exactly

\[
(1,1,1,0,\ldots,0),
\]

so it satisfies the owner's target hypothesis with equality at the threshold.

For coordinates `x,y`,

\[
(A_n)_{xy}
=\frac{1+(-1)^{x_1+y_1}+(-1)^{x_2+y_2}}{n},
\]

and therefore

\[
|(A_n)_{xy}|\le \frac3n
\qquad\text{for every }x,y.
\tag{2.1}
\]

In fact the entries are only `3/n`, `1/n`, or `-1/n`.

## 3. No fixed-size principal block can carry a dimension-free large coefficient

Let `I` be any set of `k` original coordinates and let `A_n[I]` be the corresponding `k x k` principal block. By (2.1), every row of this block has absolute row sum at most `3k/n`, so

\[
\boxed{\|A_n[I]\|_{op}\le \frac{3k}{n}.}
\tag{3.1}
\]

Consequently every eigenvalue, diagonal coefficient, off-diagonal coefficient, and every canonical quadratic coefficient obtainable from this unchanged principal Hessian is `O(k/n)`.

For any fixed `k` and any positive dimension-free threshold `c`, choosing

\[
n>\frac{3k}{c}
\]

forces

\[
\|A_n[I]\|_{op}<c
\]

for **every** `k`-coordinate principal block simultaneously.

Conditioning on all coordinates outside `I` does not alter this Hessian: it only creates linear and constant terms in the selected variables. Therefore conditioning cannot amplify the principal quadratic coefficients.

## 4. Structural consequence

This exactly refutes the following universal proof strategy:

> From the assumption that `A` has three eigenvalues of magnitude at least `1`, extract a principal block on a fixed number `k=O(1)` of original independent coordinates whose quadratic coefficients or block singular values are bounded below by an absolute constant, then close the theorem using a finite list of fixed-dimensional product-preserving normal forms.

The family `A_n` has the required three unit eigenvalues but every fixed-size original-coordinate principal block tends uniformly to zero as `n->infinity`.

This does **not** refute B12's block theorem, B17's diagonal theorem, or the full quadratic-form conjecture. It shows that those local theorems cannot be promoted to the full target by a dimension-free fixed-coordinate extraction lemma. Any successful structural reduction must either:

- use a number of original coordinates growing with `n` (at least order `n` to recover an `O(1)` operator norm in this family), while preserving product structure; or
- use a genuinely high-cardinality inequality such as an oscillatory/nonlinear Brascamp--Lieb estimate, decoupling estimate, or small-ball inequality that aggregates many weak coefficients.

## 5. Sharpened first unpaid implication

The useful next target is therefore not `extract a fixed 3x3 block`, but:

> **QFORM-DELOCALIZED-AGGREGATION-v1.** Prove a dimension-free `L^1_t` or small-ball estimate for product densities when the three large spectral directions are completely delocalized across many original coordinates, with the Walsh projection family `A_n` above as a mandatory exact stress test.

Any proposed proof that depends only on one bounded-size principal block fails this stress test before analytic details begin.

## 6. Status

`CANDIDATE_REFUTED`: fixed-size, dimension-free principal-block extraction as a universal bridge from spectral rank-three information to B12/B17 local normal forms.

`FULL_TARGET_OPEN`: the Walsh projection family is not a counterexample to the density conjecture; it is a counterexample only to that structural reduction mechanism.
