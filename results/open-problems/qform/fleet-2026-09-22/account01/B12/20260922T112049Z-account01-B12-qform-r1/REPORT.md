# account01/B12 — a genuinely non-diagonal three-large-eigenvalue block via multiplicative Young

**Live owner control:** revision `2026-09-22.4`, quadratic-form bounded-density target  
**Run:** `20260922T112049Z-account01-B12-qform-r1`  
**Classification:** `ESSENTIAL_STEP_APPLIED / NONDIAGONAL_BLOCK_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository sources were consumed, but no separately authenticated native brain receiver/context was used.  
**Full arbitrary-eigenvector conjecture:** **OPEN / NOT PROVED.**

## 1. Live target and source correction

The later owner message supersedes the earlier FEI assignment. The active target is: for independent real `X_1,...,X_n` with densities bounded by `1`, prove a universal `L^infinity` bound for the density of `Q(X)=X^T A X` whenever `A` has at least three eigenvalues of absolute value at least `1`.

Two completed peer results are used to avoid duplicating already-closed work.

1. `account03/B17`, commit `c64fcff680b0a252a3c92002c60eedba02bbb9ec`, report `qform/fleet-2026-09-22/account03/B17/account03-B17-20260922T112131Z/REPORT.md`, proves the entire coordinate-diagonal branch with the sharper constant `pi`, using a same-sign pair, and proves that the owner-suggested law-uniform pointwise Fresnel decay is false.
2. `account01/B08`, commit `aa81e06a1ea739fc6ec7895469ce9f8551b7d840`, report `proofnet24/quadratic-form-bounded-density/account01/B08/20260922T110731Z-account01-B08/REPORT.md`, proves the endpoint square-density estimate `||p_{X^2}||_{3/2}<=2` and its scaled/linearly shifted version.

The present report pushes beyond the diagonal branch. It proves a uniform theorem for a genuinely non-diagonal hyperbolic `2x2` block coupled to a third square, while allowing arbitrary interactions with all remaining coordinates. The key new estimate is an `L^3` bound for the density of a product of two independent bounded-density variables.

## 2. Multiplicative Young lemma

### Lemma 2.1 — positive half-line product

Let `X,Y` be independent nonnegative random variables with subprobability densities `f,g` satisfying `0<=f,g<=1`. Let their masses be `m=integral f<=1` and `n=integral g<=1`. The (subprobability) density `h` of `XY` on `(0,infinity)` satisfies

\[
\boxed{\|h\|_3\le 2^{4/3}(mn)^{1/3}.}
\tag{2.1}
\]

#### Proof

For `z>0`,
\[
h(z)=\int_0^\infty f(x)g(z/x)\,{dx\over x}.
\tag{2.2}
\]
Put `z=e^u`, `x=e^v`, and define
\[
F(v)=e^{v/3}f(e^v),\qquad G(v)=e^{v/3}g(e^v).
\]
Then
\[
e^{u/3}h(e^u)=(F*G)(u),
\]
so
\[
\|h\|_3^3
=\int_{\mathbb R}|F*G(u)|^3du.
\tag{2.3}
\]
Young's convolution inequality with exponents `3/2,3/2,3` gives
\[
\|h\|_3\le\|F\|_{3/2}\|G\|_{3/2}.
\tag{2.4}
\]
Moreover
\[
\|F\|_{3/2}^{3/2}
=\int_0^\infty x^{-1/2}f(x)^{3/2}dx
\le\int_0^\infty x^{-1/2}f(x)dx.
\tag{2.5}
\]
Under `0<=f<=1` and mass `m`, the last integral is maximized by filling the decreasing weight from the origin, i.e. by `1_[0,m]`, and therefore is at most `2 sqrt(m)`. Thus
\[
\|F\|_{3/2}\le 2^{2/3}m^{1/3},
\]
and likewise for `G`. Substitution in (2.4) proves (2.1). `QED`.

### Corollary 2.2 — signed product

If `X,Y` are arbitrary independent real random variables with probability densities bounded by `1`, then the density `p_{XY}` obeys
\[
\boxed{\|p_{XY}\|_3\le 2^{8/3}.}
\tag{2.6}
\]

#### Proof

Split each density into its positive and negative half-line pieces after reflection to `(0,infinity)`. On the positive output half-line there are the `++` and `--` product components; on the negative half-line there are the `+-` and `-+` components. Lemma 2.1 bounds each component by at most `2^{4/3}` in `L^3`. Triangle inequality gives at most `2^{7/3}` on either output half-line. The two half-lines are disjoint, hence
\[
\|p_{XY}\|_3^3
\le 2(2^{7/3})^3=2^8,
\]
which is (2.6). `QED`.

This constant is deliberately not optimized; only dimension- and law-independence matter here.

## 3. Hyperbolic pair with arbitrary linear perturbations

### Lemma 3.1

Let `X,Y` be independent with densities bounded by `1`, let `a!=0`, and let `b,c` be arbitrary real numbers. Then
\[
U=2aXY+bX+cY
\]
has a density satisfying
\[
\boxed{\|p_U\|_3\le 4|a|^{-2/3}.}
\tag{3.1}
\]

#### Proof

Complete the bilinear translation:
\[
2aXY+bX+cY
=2a\left(X+{c\over2a}\right)\left(Y+{b\over2a}\right)-{bc\over2a}.
\tag{3.2}
\]
Translations preserve independence and the density cap. Corollary 2.2 and one-dimensional density scaling give
\[
\|p_U\|_3
\le |2a|^{-2/3}2^{8/3}
=4|a|^{-2/3}.
\]
`QED`.

The exact importance of (3.2) is that all cross terms from these two coordinates to variables on which we later condition become harmless linear coefficients `b,c`.

## 4. Third square factor

The source-valid B08 square endpoint gives the following directly. If `Z` has density bounded by `1`, `lambda!=0`, and `d` is arbitrary, then
\[
V=\lambda Z^2+dZ
\]
has a density with
\[
\boxed{\|p_V\|_{3/2}\le2|\lambda|^{-1/3}.}
\tag{4.1}
\]
Indeed one completes the square; translation preserves the input density cap, and output scaling gives the factor `|lambda|^{-1/3}`.

Combining (3.1) and (4.1) by Young with `1/3+2/3=1` yields
\[
\boxed{
\|p_{U+V}\|_\infty
\le8|a|^{-2/3}|\lambda|^{-1/3}.
}
\tag{4.2}
\]
Here `U,V` are independent because they use disjoint original coordinates.

## 5. Main theorem — a non-diagonal three-large-eigenvalue principal block

### Theorem 5.1 — `QFORM-HYPERBOLIC-PAIR-PLUS-SQUARE-v1`

Let `X_1,...,X_n` be independent real random variables, each with density bounded by `1`, and let
\[
Q(X)=X^TAX
\]
for a real symmetric matrix `A`. Suppose that, after permuting original coordinates, the principal block on coordinates `1,2,3` is
\[
A_{\{1,2,3\}}
=
\begin{pmatrix}
0&a&0\\
a&0&0\\
0&0&\lambda
\end{pmatrix},
\qquad |a|\ge1,\quad|\lambda|\ge1.
\tag{5.1}
\]
No restriction is imposed on the remaining principal block or on the couplings from coordinates `1,2,3` to coordinates `4,...,n`.

Then `Q(X)` is absolutely continuous and
\[
\boxed{
\|p_Q\|_\infty
\le8|a|^{-2/3}|\lambda|^{-1/3}
\le8.
}
\tag{5.2}
\]

#### Proof

Condition on `W=(X_4,...,X_n)`. For every fixed outside value `w`, all couplings between the selected coordinates and `w` become linear terms, so the conditional polynomial has the exact form
\[
Q_w(x_1,x_2,x_3)
=2a x_1x_2+b(w)x_1+c(w)x_2
+\lambda x_3^2+d(w)x_3+e(w).
\tag{5.3}
\]
The variables `X_1,X_2,X_3` remain mutually independent under this conditioning. By Sections 3-4, the first two terms grouped as `U_w` have `L^3` density at most `4|a|^{-2/3}`, while the third-coordinate term `V_w` has `L^{3/2}` density at most `2|lambda|^{-1/3}`. The constant `e(w)` only translates the output. Therefore Young gives, uniformly in `w`,
\[
\|p_{Q\mid W=w}\|_\infty
\le8|a|^{-2/3}|\lambda|^{-1/3}.
\tag{5.4}
\]
A mixture of probability densities sharing the same `L^infinity` cap has the same cap. Hence (5.2) holds for the unconditional law. `QED`.

### Spectral meaning

The displayed `3x3` block has eigenvalues `a,-a,lambda` up to the sign convention for `a`. Thus it is a genuinely indefinite, non-diagonal original-coordinate block carrying three eigenvalues of magnitude at least `1`. Arbitrary coupling to all remaining coordinates is allowed. This is not the diagonal theorem in disguise: the hyperbolic pair `2aX_1X_2` is exactly the maximally off-diagonal two-variable quadratic form.

By principal-submatrix interlacing, the full matrix necessarily has the corresponding large positive/negative spectral directions. Thus Theorem 5.1 is a source-valid target-level subclass rather than a statement about an unrelated easier normalization.

## 6. Combined branch picture after consuming account03/B17

The named account03/B17 theorem covers a different conditional normal form: if two original coordinates have no mutual cross coefficient and have same-sign diagonal coefficients of magnitude at least `1`, then conditioning the rest and completing squares gives the sharp `pi` bound. Theorem 5.1 covers the complementary canonical hyperbolic block in which the `2x2` piece is purely off-diagonal and the third coordinate supplies the square factor.

So two exact product-preserving normal forms are now closed:

* elliptic pair: `alpha X^2+beta Y^2`, `alpha beta>0`, giving `C<=pi`;
* hyperbolic pair plus square: `2aXY+lambda Z^2`, giving `C<=8`.

Both remain valid under arbitrary outside couplings because those become linear terms after conditioning.

## 7. What remains unpaid

The arbitrary rotated problem is still open. A generic `3x3` principal block need not contain either normal form without a linear change mixing independent coordinates, and such a change destroys independence. Also, as B08 showed, replacing the rotated product density by only a joint `L^infinity` bound cannot work in the indefinite case because mass can concentrate in a thin null-cone tube.

The next useful implication is therefore structural rather than another stationary-phase estimate:

> prove a dimension-free decomposition/conditioning principle that extracts, from three spectral singular values `>=1`, a product-preserving coordinate block whose conditional quadratic polynomial is controlled by a finite collection of elliptic-pair or hyperbolic-pair-plus-square estimates; or establish an equally strong nonlinear Brascamp-Lieb estimate directly for the generic three-coordinate block.

Theorem 5.1 shows that substantial off-diagonal coupling itself is not the obstruction. The remaining difficulty is simultaneous presence of diagonal and several cross coefficients in every useful coordinate block while retaining original-coordinate independence.

## 8. Status

`ESSENTIAL_STEP_APPLIED / NONDIAGONAL_BLOCK_THEOREM / FULL_TARGET_OPEN`.

No claim is made that the full conjecture is proved. No pointwise law-uniform Fourier decay is used. The result is analytic and arbitrary-dimensional under the explicit principal-block hypothesis.
