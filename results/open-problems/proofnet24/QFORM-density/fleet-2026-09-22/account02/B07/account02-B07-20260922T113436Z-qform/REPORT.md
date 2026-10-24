# account02/B07 — coordinate-minor delocalization, determinant mass, and a solved high-cardinality Walsh model

**Run:** `account02-B07-20260922T113436Z-qform`  
**Current assignment:** `Coordinate minor selection` (owner control `2026-09-22.5`)  
**Classification:** `ESSENTIAL_STEP_APPLIED / CANDIDATE_REFUTED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Live target and assignment

The active target is the quadratic-form bounded-density conjecture: for independent real `X_i` with densities bounded by `1`, and real symmetric `A` with at least three eigenvalues of absolute value at least `1`, prove that `Q=X^TAX` has a density bounded by one universal constant.

The B07 assignment is to investigate dimension-free averaging/selection of coordinate minors, explicitly recognizing that one tiny principal minor is insufficient and that determinant weights must be tracked through conditioning.

This report does exactly that. It proves a spectral determinant-mass identity, gives an exact rank-three family showing that every fixed-size coordinate block can be tiny despite the three-large-eigenvalue hypothesis, and then closes that same delocalized stress family by a high-cardinality aggregation mechanism. Thus it rules out fixed-block selection while demonstrating a viable determinant-aware replacement in a nontrivial model.

## 1. Sources consumed and current corrections

Current canonical state records the full conjecture as open, the proposed law-uniform pointwise Fresnel decay as refuted, the full coordinate-diagonal branch as proved with bound `pi`, and naive two-dimensional fiber-supremum control as dimension-losing.

Two complete peer reports were consumed and applied:

1. **account03/B17**, `yspennstate/math-open-problems@c64fcff680b0a252a3c92002c60eedba02bbb9ec`, path `qform/fleet-2026-09-22/account03/B17/account03-B17-20260922T112131Z/REPORT.md`. It proves the diagonal branch with `C=pi` and the exact pointwise no-go `sup_f |E exp(isX^2)|=1` for each nonzero `s`.
2. **account01/B12**, `yspennstate/math-open-problems@e423d315ae772630a32bc826c5abb58a5ad09c95`, path `qform/fleet-2026-09-22/account01/B12/20260922T112049Z-account01-B12-qform-r1/REPORT.md`. It proves a genuinely non-diagonal hyperbolic-pair-plus-square block theorem with conditional density bound `8`, and motivates product-preserving coordinate-block reduction.

The assigned partner **account03/B07** had no completed handoff in the current shared qform handoff directory at the final partner check, so no nonexistent partner theorem is claimed. Work proceeded from the complete compatible peer snapshots above, as authorized by the owner order.

An external source is used only in Section 6: Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949. Its `k=1` theorem gives density at most `sqrt(2)` for every one-dimensional orthogonal marginal of a product probability density whose one-dimensional factors are bounded by `1`.

## 2. Exterior-power determinant mass forced by three large eigenvalues

Let the eigenvalues of real symmetric `A` be `lambda_1,...,lambda_n`. Cauchy--Binet applied to the compound matrices gives the exact identities

\[
\sum_{|I|=|J|=2}\det(A_{I,J})^2
=\|\wedge^2 A\|_{HS}^2
=\sum_{i<j}\lambda_i^2\lambda_j^2,
\tag{2.1}
\]

and

\[
\sum_{|I|=|J|=3}\det(A_{I,J})^2
=\|\wedge^3 A\|_{HS}^2
=\sum_{i<j<k}\lambda_i^2\lambda_j^2\lambda_k^2.
\tag{2.2}
\]

Hence if three eigenvalues have absolute value at least `1`, then

\[
\boxed{\sum_{|I|=|J|=2}\det(A_{I,J})^2\ge3,}
\qquad
\boxed{\sum_{|I|=|J|=3}\det(A_{I,J})^2\ge1.}
\tag{2.3}
\]

This is the dimension-free quantity that survives complete coordinate delocalization. It is *mass*, not a lower bound for one selected coordinate minor: the mass can be spread over polynomially many tiny minors.

For conditioning arguments, principal minors are especially useful because conditioning outside a principal coordinate set leaves its quadratic Hessian unchanged. The next family shows why no dimension-free lower bound for one such block can follow from (2.3).

## 3. Exact delocalized rank-three projection family

Let `n=2^m`, `m>=2`, index coordinates by `x in {0,1}^m`, and define normalized Walsh vectors

\[
r_1(x)=n^{-1/2},\qquad
r_2(x)=n^{-1/2}(-1)^{x_1},\qquad
r_3(x)=n^{-1/2}(-1)^{x_2}.
\]

They are orthonormal. Put

\[
A_n=r_1r_1^T+r_2r_2^T+r_3r_3^T.
\tag{3.1}
\]

Then `A_n` is the orthogonal projection onto their span, so

\[
\operatorname{spec}(A_n)=(1,1,1,0,\ldots,0).
\tag{3.2}
\]

For coordinates `x,y`,

\[
(A_n)_{xy}
={1+(-1)^{x_1+y_1}+(-1)^{x_2+y_2}\over n},
\]

so every entry has absolute value at most `3/n`. Therefore every `k x k` principal block obeys

\[
\boxed{\|A_n[I]\|_{op}\le {3k\over n}.}
\tag{3.3}
\]

For fixed `k`, every such block tends uniformly to zero as `n->infinity`. Conditioning all coordinates outside `I` changes only the linear and constant terms, not this Hessian.

### Consequence

The following universal bridge is false:

> three eigenvalues of magnitude at least `1` imply a principal block on `O(1)` original independent coordinates with a dimension-free lower bound on a quadratic coefficient, singular value, or operator norm.

This is a counterexample to the *selection mechanism*, not to the density conjecture.

## 4. Exact principal determinant distribution in the Walsh family

Partition coordinates into the four sign classes of `((-1)^{x_1},(-1)^{x_2})`, each of size `n/4`.

For two coordinates in the same class, their row vectors in the rank-three factor are identical and the `2x2` principal determinant is zero. For coordinates in two distinct classes, the diagonal entries are `3/n`, the off-diagonal entry has absolute value `1/n`, hence

\[
\det A_n[\{i,j\}]
={9-1\over n^2}
={8\over n^2}.
\tag{4.1}
\]

There are exactly

\[
\binom42(n/4)^2={3n^2\over8}
\]

such cross-class pairs. Thus the entire second elementary-symmetric determinant mass is

\[
{3n^2\over8}\,{8\over n^2}=3,
\tag{4.2}
\]

as predicted by the three unit eigenvalues, but it is spread over `Theta(n^2)` minors of size `Theta(n^{-2})`.

Likewise, a nonzero `3x3` principal determinant requires three distinct sign classes. For any three distinct classes the `3 x 3` Walsh row matrix has determinant magnitude `4/n^{3/2}`, so the Gram determinant is

\[
{16\over n^3}.
\tag{4.3}
\]

There are

\[
\binom43(n/4)^3={n^3\over16}
\]

such triples, and their determinants sum to `1`, exactly `e_3(1,1,1)=1`.

This is a model instance of the assignment's central issue: determinant weight is dimension-free only after summing over many tiny coordinate minors.

## 5. A definite two-coordinate conditioning lemma

### Lemma 5.1 — `QFORM-PD-2BLOCK-v1`

Let `Z_1,Z_2` be independent with density caps `K_1,K_2`. Let

\[
B=\begin{pmatrix}a&b\\b&c\end{pmatrix}
\]

be positive definite. For arbitrary linear term `ell` and constant `d`,

\[
T=Z^TBZ+\ell^TZ+d
\]

has density satisfying

\[
\boxed{\|p_T\|_\infty\le {\pi K_1K_2\over\sqrt{\det B}}.}
\tag{5.1}
\]

The same holds for negative definite `B`, after reflecting the output.

### Proof

Complete the square and translate the two independent variables. Put `U=B^{1/2}(Z-z_0)`. Its joint density is at most `K_1K_2/sqrt(det B)`. For `S=|U|^2`, polar coordinates give

\[
p_S(s)=\frac12\int_{S^1}h(\sqrt s\,\omega)d\omega
\le {\pi K_1K_2\over\sqrt{\det B}}.
\]

Translations of the output do not change the cap. QED.

If this block occurs as a principal block of a larger quadratic form, conditioning all other original coordinates only adds linear/constant terms, so (5.1) remains uniform in the conditioning variables and hence unconditionally valid.

## 6. High-cardinality aggregation closes the Walsh stress family

For each sign class `G_{eps,eta}`, define

\[
Z_{\varepsilon,\eta}
={1\over\sqrt n}\sum_{x\in G_{\varepsilon,\eta}}X_x.
\tag{6.1}
\]

The four aggregates are independent because their coordinate sets are disjoint.

Let

\[
Y_G={2\over\sqrt n}\sum_{x\in G}X_x.
\]

The coefficient vector of `Y_G` has Euclidean norm `1`. The `k=1` marginal theorem cited in Section 1 therefore gives

\[
\|p_{Y_G}\|_\infty\le\sqrt2.
\]

Since `Z_G=Y_G/2`,

\[
\boxed{\|p_{Z_G}\|_\infty\le2\sqrt2.}
\tag{6.2}
\]

Order the four classes as `(++),(+-),(-+),(--)`, set `z=(Z_1,...,Z_4)`, and let `s=(1,-1,-1,1)^T`. The three Walsh spectral coordinates are the first three Hadamard combinations, so exactly

\[
Q_n=X^TA_nX=z^TMz,
\qquad
M=4I-ss^T.
\tag{6.3}
\]

Every `2x2` principal block of `M` equals

\[
\begin{pmatrix}3&\pm1\\\pm1&3\end{pmatrix},
\qquad \det=8.
\tag{6.4}
\]

Condition on any two aggregate variables. The remaining two are independent, retain the density cap `K=2sqrt(2)`, and see a positive-definite quadratic block of determinant `8`. Lemma 5.1 yields

\[
\|p_{Q_n\mid \text{two aggregates}}\|_\infty
\le{\pi K^2\over\sqrt8}
=2\sqrt2\,\pi.
\]

Mixing preserves the cap. Therefore

\[
\boxed{\|p_{X^TA_nX}\|_\infty\le2\sqrt2\,\pi}
\tag{6.5}
\]

for every `n=2^m` and every collection of independent input densities bounded by `1`.

The family that destroys fixed-block selection is therefore itself uniformly safe once many tiny determinant contributions are aggregated in a product-preserving way.

## 7. What is paid and what remains unpaid

### Paid

1. **Fixed-size coordinate-minor selection is decisively ruled out.** Three unit eigenvalues may coexist with `||A[I]||op=O(|I|/n)` for every bounded-size principal block.
2. **The determinant mass is quantified exactly.** Exterior powers give dimension-free total mixed-minor mass; the Walsh family shows principal determinant mass spread over `Theta(n^2)` pairs and `Theta(n^3)` triples.
3. **One genuinely delocalized rank-three model is solved.** High-cardinality aggregation plus a sharp one-dimensional marginal theorem recovers a fixed definite block and gives the explicit universal bound `2sqrt(2) pi`.

### First unpaid implication — `QFORM-DETWEIGHT-AGGREGATION-v1`

For a general triple of large eigenvectors, prove a product-preserving partition/aggregation theorem (or an equivalent nonlinear Brascamp--Lieb/small-ball inequality) that converts the determinant mass in (2.3) into a bounded number of independent aggregate variables carrying a quantitatively definite conditional quadratic block.

The Walsh proof works because the row vectors take only four exact directions, so each group collapses to one scalar aggregate. Generic row directions vary continuously; approximate clustering alone is not automatically valid because inputs have no moment/support bound, so a small coefficient error can be multiplied by arbitrarily large coordinates. Any stability argument must therefore pay for this error without importing nonexistent moments.

This is the exact remaining connection to the full target.

## 8. Status and provenance

`CANDIDATE_REFUTED`: a universal fixed-size principal-coordinate-block extraction mechanism.

`ESSENTIAL_STEP_APPLIED`: exact determinant-mass identities, definite-block conditioning lemma, and complete high-cardinality closure of the rank-three Walsh stress family with `C=2sqrt(2)pi`.

The full arbitrary-eigenvector quadratic-form bounded-density conjecture remains **OPEN / NOT PROVED**. No numerical computation was used. The work is analytic and source-bound. The preliminary same-run files written before control revision `2026-09-22.5` were preserved rather than overwritten; this report is the canonical deliverable at the exact current assignment path.
