# fleet02/B07 — high-cardinality aggregation closes the delocalized Walsh stress family

**Run:** `fleet02-B07-20260922T113436Z-qform`  
**Classification:** `ESSENTIAL_STEP_APPLIED / DELOCALIZED_STRESS_FAMILY_CLOSED / FULL_TARGET_OPEN`.

## 1. Purpose

The companion `PEER_APPLIED.md` gives a rank-three Walsh projection family `A_n` with spectrum `(1,1,1,0,...)` for which every fixed-size original-coordinate principal block has norm `O(k/n)`. That family rules out a universal fixed-block extraction lemma.

This note shows that the same family is nevertheless harmless once one aggregates many weak coordinates *before* applying a local two-variable density estimate. Thus the no-go is genuinely about the extraction mechanism, not about the conjecture.

The proof combines:

1. the source-valid product-density marginal theorem of Livshyts--Paouris--Pivovarov (2015): for a product probability density `F=prod_i f_i` with each `||f_i||_infty<=1`, every one-dimensional orthogonal marginal has density at most `sqrt(2)`; this is the `k=1` case of their bound `2^(k/2)` for `k`-dimensional marginals (`arXiv:1507.07949`);
2. the conditioning idea used in fleet01/B12's exact non-diagonal block theorem, `math-open-problems@e423d315ae772630a32bc826c5abb58a5ad09c95`, report `qform/fleet-2026-09-22/fleet01/B12/20260922T112049Z-fleet01-B12-qform-r1/REPORT.md`;
3. a two-variable positive-definite block lemma proved below.

No rotation of the original independent variables is performed. Aggregation is only across disjoint coordinate groups, so the four aggregate variables remain independent.

## 2. Positive-definite two-coordinate block lemma

### Lemma 2.1 — `QFORM-PD-2BLOCK-v1`

Let `Z_1,Z_2` be independent real random variables with densities bounded respectively by `K_1,K_2`. Let

\[
B=\begin{pmatrix}a&b\\b&c\end{pmatrix}
\]

be positive definite. For arbitrary `ell in R^2` and constant `d`, the random variable

\[
T=Z^T BZ+\ell^TZ+d
\]

has a density satisfying

\[
\boxed{\|p_T\|_\infty\le {\pi K_1K_2\over\sqrt{\det B}}.}
\tag{2.1}
\]

The same bound holds for negative definite `B`, after reflecting the output.

### Proof

Complete the square:

\[
Z^TBZ+\ell^TZ+d=(Z-z_0)^TB(Z-z_0)+d_0,
\qquad z_0=-\tfrac12B^{-1}\ell.
\]

Translation of each independent input preserves its density cap. Put

\[
U=B^{1/2}(Z-z_0).
\]

The joint density `h` of `U` is bounded by

\[
\|h\|_\infty\le {K_1K_2\over\sqrt{\det B}}.
\]

For `S=|U|^2`, polar coordinates give for `s>0`

\[
p_S(s)=\frac12\int_{S^1}h(\sqrt{s}\,\omega)\,d\omega
\le \frac12(2\pi)\|h\|_\infty
\le {\pi K_1K_2\over\sqrt{\det B}}.
\]

The additive constant only translates the output. QED.

### Conditional form

If a full quadratic form contains a positive-definite principal `2x2` block `B` on two independent original coordinates and all other coordinates are conditioned, cross couplings to the conditioned variables become linear terms. Hence the same bound (2.1) holds conditionally, uniformly in the conditioned values, and therefore also unconditionally by mixing.

This generalizes the same-sign diagonal beta-integral mechanism: a nonzero cross term inside the definite `2x2` block is harmless once its determinant stays quantitatively positive.

## 3. The Walsh projection family

Let `n=2^m`, `m>=2`, index coordinates by `x in {0,1}^m`, and define

\[
r_1(x)=n^{-1/2},\quad
r_2(x)=n^{-1/2}(-1)^{x_1},\quad
r_3(x)=n^{-1/2}(-1)^{x_2}.
\]

Set

\[
A_n=r_1r_1^T+r_2r_2^T+r_3r_3^T.
\]

As recorded in `PEER_APPLIED.md`, `A_n` is an orthogonal projection of rank three, so its eigenvalues are exactly `(1,1,1,0,...)`.

Partition the original coordinates into the four sign classes

\[
G_{\varepsilon,\eta}
=\{x:(-1)^{x_1}=\varepsilon,\ (-1)^{x_2}=\eta\},
\qquad \varepsilon,\eta\in\{\pm1\},
\]

all of cardinality `n/4`, and define

\[
Z_{\varepsilon,\eta}
={1\over\sqrt n}\sum_{x\in G_{\varepsilon,\eta}}X_x.
\tag{3.1}
\]

Because the groups are disjoint and the original coordinates are independent, the four `Z` variables are independent.

## 4. Uniform density cap for each aggregate

For one group `G`, let

\[
Y_G={2\over\sqrt n}\sum_{x\in G}X_x.
\]

The coefficient vector has Euclidean norm one because `|G|=n/4`. By the one-dimensional marginal theorem cited in Section 1,

\[
\|p_{Y_G}\|_\infty\le\sqrt2.
\]

Since `Z_G=Y_G/2`, one-dimensional density scaling gives

\[
\boxed{\|p_{Z_G}\|_\infty\le2\sqrt2.}
\tag{4.1}
\]

This is the high-cardinality step that a fixed principal-block argument cannot see: each individual coefficient is `n^{-1/2}`, yet the normalized sum has a dimension-free density cap.

## 5. Exact four-aggregate quadratic form

Order the groups as `(++),(+-),(-+),(--)` and write `z=(Z_{++},Z_{+-},Z_{-+},Z_{--})^T`. Then

\[
\langle X,r_1\rangle=z_1+z_2+z_3+z_4,
\]
\[
\langle X,r_2\rangle=z_1+z_2-z_3-z_4,
\]
\[
\langle X,r_3\rangle=z_1-z_2+z_3-z_4.
\]

Therefore

\[
Q_n(X)=X^TA_nX=z^TMz,
\]

where, using the fourth Hadamard row `s=(1,-1,-1,1)^T`,

\[
M=4I-ss^T.
\tag{5.1}
\]

Thus every `2x2` principal block of `M` has diagonal entries `3`, off-diagonal entry `+1` or `-1`, and determinant

\[
\boxed{\det B=3\cdot3-1=8.}
\tag{5.2}
\]

In particular every such block is positive definite.

## 6. Uniform density theorem for the delocalized family

### Theorem 6.1 — `QFORM-WALSH-RANK3-v1`

Let the independent inputs `X_x` have arbitrary probability densities bounded by `1`. For the rank-three projection `A_n` above,

\[
Q_n(X)=X^TA_nX
\]

has a density satisfying

\[
\boxed{\|p_{Q_n}\|_\infty\le2\sqrt2\,\pi.}
\tag{6.1}
\]

The constant is independent of `n` and of all input laws.

### Proof

Condition on any two of the four independent aggregate variables, say `Z_3,Z_4`. In the remaining pair `(Z_1,Z_2)`, the quadratic part is the principal block

\[
B=\begin{pmatrix}3&\pm1\\\pm1&3\end{pmatrix},
\qquad \det B=8,
\]

while the conditioned coordinates contribute only linear and constant terms. By (4.1), each remaining input density is bounded by `K=2sqrt(2)`. Lemma 2.1 therefore gives the uniform conditional bound

\[
\|p_{Q_n\mid Z_3,Z_4}\|_\infty
\le {\pi K^2\over\sqrt8}
={8\pi\over2\sqrt2}
=2\sqrt2\,\pi.
\]

Mixing over `(Z_3,Z_4)` preserves the same cap. QED.

## 7. What this changes

The Walsh family simultaneously demonstrates two facts:

- **fixed local extraction fails:** every fixed-size original-coordinate block of `A_n` tends to zero;
- **multiscale/high-cardinality aggregation succeeds:** grouping the weak coefficients into four independent normalized sums recovers a fixed positive-definite block and a universal density bound.

Therefore the natural global mechanism should search for a partition/aggregation principle adapted to the three large eigenvectors, rather than for a bounded-size principal block. A successful theorem would have to show that arbitrary three-dimensional spectral mass can be compressed into a bounded number of independent aggregate variables with controlled one-dimensional marginal densities and a quantitatively nondegenerate conditional quadratic block, or else replace that compression with an equivalent nonlinear Brascamp--Lieb estimate.

The full conjecture remains open because an arbitrary triple of orthonormal eigenvectors need not be exactly constant on four sign classes as in this Walsh model.

## 8. Source scope and status

External source used exactly at one point: Livshyts, Paouris, Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, whose stated theorem bounds every `k`-dimensional marginal density of a product density with one-dimensional factors bounded by `1` by `2^(k/2)`; only `k=1` is used here.

Other-account source applied: fleet01/B12 at immutable source commit `e423d315ae772630a32bc826c5abb58a5ad09c95`, specifically its conditioning principle for cross couplings and its product-preserving emphasis. fleet03/B17 at `c64fcff680b0a252a3c92002c60eedba02bbb9ec` remains the sharper source for the whole coordinate-diagonal branch (`C=pi`) and for the exact pointwise-Fresnel no-go.

Status: `ESSENTIAL_STEP_APPLIED`. The delocalized Walsh stress family is closed with constant `2sqrt(2) pi`; the arbitrary-eigenvector conjecture remains `OPEN_NOT_PROVED`.
