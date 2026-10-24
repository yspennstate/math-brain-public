# account02/B07 — determinant-weight aggregation for finite row-direction alphabets

**Run:** `account02-B07-20260922T113436Z-qform`  
**Classification:** `ESSENTIAL_STEP_APPLIED / QUANTITATIVE SUPPORTING THEOREM / FULL_TARGET_OPEN`.

## 1. Statement

The Walsh model in the canonical report is not isolated. The same mechanism closes every semidefinite quadratic form whose Gram rows occupy only finitely many directions, with an explicit constant depending on the number of directions but **not** on dimension, multiplicities, input laws, or eigenvector delocalization inside the direction classes.

### Theorem 1.1 — `QFORM-FINITE-DIRECTION-PSD-v1`

Let `A` be a real positive-semidefinite `n x n` matrix with at least three eigenvalues at least `1`. Write a Gram factorization

\[
A=WW^T,
\]

where the row vectors of `W` are `w_1,...,w_n` in `R^r`. Assume that the nonzero rows lie in the union of at most `m` one-dimensional subspaces. Let `X_1,...,X_n` be independent real random variables with probability densities bounded by `1`.

Then `Q=X^TAX` has a bounded density and

\[
\boxed{
\|p_Q\|_\infty
\le 2\pi\sqrt{\frac{\binom m2}{3}}.
}
\tag{1.1}
\]

The same conclusion holds for negative-semidefinite `A` after reflection of `Q`.

For `m=4`, (1.1) is exactly `2sqrt(2) pi`, matching the Walsh-family bound from the canonical report.

## 2. Product-preserving aggregation

Partition the nonzero rows according to their one-dimensional row direction. For group `G_g`, choose a unit vector `u_g` and write

\[
w_i=c_i u_g,\qquad i\in G_g.
\]

Define

\[
\alpha_g=\left(\sum_{i\in G_g}c_i^2\right)^{1/2},
\qquad
Y_g={1\over\alpha_g}\sum_{i\in G_g}c_iX_i,
\qquad
U_g=\alpha_g u_g.
\tag{2.1}
\]

(Zero groups are discarded.) Because the coordinate groups are disjoint, the variables `Y_1,...,Y_m` are independent.

For each `g`, the coefficient vector `(c_i/alpha_g)_{i in G_g}` has Euclidean norm `1`. By the `k=1` marginal theorem of Livshyts--Paouris--Pivovarov for product densities bounded by `1`,

\[
\boxed{\|p_{Y_g}\|_\infty\le\sqrt2.}
\tag{2.2}
\]

Moreover

\[
W^TX=\sum_{i=1}^nw_iX_i
=\sum_{g=1}^mU_gY_g,
\]

and hence

\[
Q=\left\|\sum_{g=1}^mU_gY_g\right\|^2.
\tag{2.3}
\]

Thus the potentially enormous original dimension has been compressed to `m` **independent** scalar aggregates without any loss or approximation.

## 3. Determinant-weight identity on aggregate directions

The aggregate frame operator is

\[
\sum_{g=1}^m U_gU_g^T
=\sum_{i=1}^nw_iw_i^T
=W^TW.
\tag{3.1}
\]

The nonzero eigenvalues of `W^TW` are exactly the nonzero eigenvalues of `A=WW^T`.

For each pair `g<h`, define its Gram determinant

\[
d_{gh}
=\det\begin{pmatrix}
\|U_g\|^2&\langle U_g,U_h\rangle\\
\langle U_g,U_h\rangle&\|U_h\|^2
\end{pmatrix}
=\|U_g\wedge U_h\|^2
\ge0.
\tag{3.2}
\]

Cauchy--Binet/exterior algebra gives

\[
\sum_{g<h}d_{gh}
=e_2(W^TW)
=\sum_{a<b}\lambda_a(A)\lambda_b(A).
\tag{3.3}
\]

Since at least three eigenvalues are at least `1`, at least the three pair products among those eigenvalues contribute `1`, so

\[
\sum_{g<h}d_{gh}\ge3.
\tag{3.4}
\]

There are at most `binom(m,2)` terms. Therefore some pair satisfies

\[
\boxed{d_{gh}\ge {3\over\binom m2}.}
\tag{3.5}
\]

This is the exact determinant-weight selection statement that fails at the original-coordinate scale but succeeds after exact direction aggregation.

## 4. Conditioning on the selected aggregate pair

Fix a pair `(g,h)` satisfying (3.5) and condition on all other aggregate variables. Equation (2.3) becomes, as a function of `(Y_g,Y_h)`,

\[
\begin{pmatrix}Y_g&Y_h\end{pmatrix}
B_{gh}
\begin{pmatrix}Y_g\\Y_h\end{pmatrix}
+\ell^T\begin{pmatrix}Y_g\\Y_h\end{pmatrix}+c,
\]

where `B_{gh}` is exactly the Gram matrix in (3.2). It is positive definite and has determinant `d_{gh}`.

The two remaining variables stay independent under this conditioning and each has density cap `sqrt(2)` by (2.2). The definite-block lemma from the canonical report therefore gives the uniform conditional estimate

\[
\|p_{Q\mid(Y_k)_{k\ne g,h}}\|_\infty
\le{\pi(\sqrt2)^2\over\sqrt{d_{gh}}}
={2\pi\over\sqrt{d_{gh}}}.
\]

Using (3.5),

\[
\|p_{Q\mid(Y_k)_{k\ne g,h}}\|_\infty
\le2\pi\sqrt{\frac{\binom m2}{3}}.
\]

A mixture of densities with the same `L^infinity` cap has that cap, proving (1.1). QED.

## 5. Interpretation for coordinate-minor selection

The theorem gives a precise positive counterpart to the fixed-principal-block no-go.

- Original coordinate minors can all be microscopic; the Walsh family has pair determinants `8/n^2`.
- If many rows share exact directions, their squared coefficients can be aggregated. The one-dimensional marginal theorem converts each full group into one independent scalar with a universal density cap.
- The total determinant mass then lives on only `binom(m,2)` aggregate pairs, forcing one quantitatively definite block by averaging.

The bound scales linearly in `m` up to constants. Thus the unsolved generic problem is exactly the **infinite direction-alphabet** regime.

An approximate clustering argument is not immediate: the hypotheses impose no moments or support bounds, so replacing a row vector by a nearby direction produces an error coefficient multiplying an arbitrarily large `X_i`. A successful extension needs an exact information-preserving decomposition or a probabilistic mechanism that pays for those residuals without assuming moments.

## 6. Source scope

External source used: Livshyts, Paouris, Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, only its one-dimensional (`k=1`) marginal bound `sqrt(2)`.

Peer mechanism applied: account01/B12, `yspennstate/math-open-problems@e423d315ae772630a32bc826c5abb58a5ad09c95`, for the principle that conditioning outside a selected original/product-preserving block turns cross couplings into linear terms; the present proof performs that conditioning after exact disjoint-group aggregation.

## 7. Remaining implication

`QFORM-DIRECTION-ALPHABET-REMOVAL-v1`: replace the finite exact row-direction assumption by a dimension-free exact decomposition or inequality that preserves product information for arbitrary row frames, while retaining enough determinant mass to invoke a definite or indefinite local density mechanism.

Status: `ESSENTIAL_STEP_APPLIED`. This theorem is a quantitatively stated supporting result, not a proof of the full indefinite arbitrary-eigenvector conjecture.
