# fleet03/B01 — common L^3 product envelope and an enlarged non-diagonal block theorem

**Run:** `20260922T113140Z-fleet03-B01-qform-r1`  
**Live programme:** `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.5`  
**Assignment:** B01, “Oscillatory replacement”  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_BLOCK_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository sources were read, but no authenticated native brain receiver/context was used.  
**Full arbitrary-eigenvector conjecture:** **OPEN / NOT PROVED.**

## 1. Why this run does not continue FEI

The later owner control redirects every existing worker from FEI to the quadratic-form bounded-density conjecture. The target is:

> If `X_1,...,X_n` are independent real random variables with probability densities bounded by `1`, and a real symmetric matrix `A` has at least three eigenvalues of absolute value at least `1`, prove that `Q(X)=X^T A X` has an essentially bounded density with one universal dimension- and law-independent constant.

The current correction state also records that a law-uniform pointwise Fresnel decay bound is false. In particular, the source-valid `fleet03/B17` report proves

`sup_{0<=f<=1, int f=1} |int exp(i s x^2) f(x) dx| = 1`

for every fixed `s != 0`. So this run does **not** try to repair the false pointwise `|s|^{-1/2}` estimate.

Two peer results are used concretely:

1. `fleet03/B17`, report `qform/fleet-2026-09-22/fleet03/B17/fleet03-B17-20260922T112131Z/REPORT.md`, blob `570781af62598117e1014e1edd6831b958bf00c4`, supplies the pointwise-Fourier no-go and the complete coordinate-diagonal theorem with density bound `pi`.
2. `fleet01/B12`, report `qform/fleet-2026-09-22/fleet01/B12/20260922T112049Z-fleet01-B12-qform-r1/REPORT.md`, blob `50e123835dfec75386bcfd5a31ea86b70d67989b`, proves a genuinely non-diagonal block theorem for `2aXY + lambda Z^2` with arbitrary *outside* couplings. The present proof keeps its product mechanism but removes the restriction that the selected hyperbolic pair be uncoupled from the third selected coordinate.

The assignment names `fleet04/B01` as partner. At the coherent control snapshot there was no QFORM report or handoff yet at that worker’s prescribed path, so there was no source-valid new-target partner theorem to consume. I do not reuse its older FOREST work as if it were relevant. The peer dependency actually applied below is the current B12 theorem plus the B17 correction.

## 2. A common pointwise envelope for products of arbitrary bounded-density laws

The false one-variable oscillatory envelope has a useful replacement at the **two-variable product-density** level.

### Lemma 2.1 — `QFORM-PRODUCT-COMMON-ENVELOPE-v1`

Let `U,V` be independent real random variables with probability densities `f,g` satisfying

`0 <= f,g <= 1`.

Then `UV` has a density `p` and, for every `w != 0`,

\[
\boxed{
 p(w)\le H(w):=4\log\!\left(1+{1\over 2\sqrt{|w|}}\right).
}
\tag{2.1}
\]

Moreover `H in L^3(R)`, and the explicit crude bound

\[
\boxed{
\|H\|_3^3
\le 128\left[c^3+{3\over2}c^2+{3\over2}c+{3\over4}\right]+32
<246,
\qquad c=\log(3/2),
}
\tag{2.2}
\]

holds. Hence

\[
\boxed{\|H\|_3<6.266.}
\tag{2.3}
\]

#### Proof

For `w != 0`, the standard product-density formula is

\[
p(w)=\int_{\mathbb R} f(x)g(w/x){dx\over |x|}.
\tag{2.4}
\]

Put `a=sqrt(|w|)` and split the integral into `|x|>=a` and `|x|<a`.

On `|x|>=a`, use `g<=1`:

\[
I_1\le \int_{|x|\ge a}{f(x)\over |x|}dx.
\tag{2.5}
\]

Among all `0<=f<=1` of mass one, the right-hand side is maximized by filling the largest values of the decreasing weight `1/|x|` on the two rays, namely by occupying total length one immediately outside `[-a,a]`. Therefore

\[
I_1\le 2\int_a^{a+1/2}{dx\over x}
=2\log\left(1+{1\over2a}\right).
\tag{2.6}
\]

On `|x|<a`, substitute `y=w/x`. Then `|y|>a` and `dx/|x|=dy/|y|` in absolute value, so by `f<=1` and the same bathtub argument applied to `g`,

\[
I_2\le 2\log\left(1+{1\over2a}\right).
\tag{2.7}
\]

Adding proves (2.1).

For `0<r<=1`,

\[
1+{1\over2\sqrt r}\le {3\over2\sqrt r},
\]

so

\[
H(r)\le4\left(c+{1\over2}\log{1\over r}\right),
\qquad c=\log(3/2).
\tag{2.8}
\]

For `r>=1`, `log(1+x)<=x` gives

\[
H(r)\le {2\over\sqrt r}.
\tag{2.9}
\]

Using

\[
\int_0^1 \log^k(1/r)dr=k!
\]

for `k=0,1,2,3`, the two-sided integral over `|w|<=1` is at most

\[
128\left(c^3+{3\over2}c^2+{3\over2}c+{3\over4}\right),
\]

and the two-sided tail is at most

\[
2\int_1^\infty 8r^{-3/2}dr=32.
\]

This proves (2.2)-(2.3). `QED`.

### Corollary 2.2 — scaled products and an averaged-frequency replacement

For `b != 0`, the density of `2bUV` is bounded by

\[
H_b(s):={1\over2|b|}H\!\left({s\over2b}\right),
\]

so

\[
\boxed{\|H_b\|_3=(2|b|)^{-2/3}\|H\|_3.}
\tag{2.10}
\]

This bound is unchanged when `U` and `V` are translated by arbitrary constants, because their translated laws remain independent probability densities bounded by one.

It also gives a genuine averaged-frequency substitute for the refuted pointwise stationary-phase claim. Since `p_{UV}` is a probability density and `p_{UV}<=H`, interpolation yields

\[
\|p_{UV}\|_{3/2}
\le \|p_{UV}\|_1^{1/2}\|p_{UV}\|_3^{1/2}
\le \|H\|_3^{1/2}.
\tag{2.11}
\]

With the Fourier convention `phi(t)=int exp(ity)p(y)dy`, Hausdorff--Young therefore gives

\[
\boxed{
\|\phi_{UV}\|_3
\le (2\pi)^{1/3}\|H\|_3^{1/2},
}
\tag{2.12}
\]

and scaling gives an additional factor `(2|b|)^(-1/3)` for `2bUV`. This is an integrated-in-frequency estimate; it does not contradict B17’s pointwise no-go.

## 3. The square endpoint needed for a third coordinate

For completeness I record the exact endpoint used by several peers.

### Lemma 3.1 — square `L^{3/2}` bound

If `Z` has a probability density bounded by `1` and `kappa != 0`, then `T=kappa Z^2` has a density satisfying

\[
\boxed{
\|p_T\|_{3/2}\le2|\kappa|^{-1/3}.
}
\tag{3.1}
\]

#### Proof

It is enough to take `kappa=1`. Put `h(r)=f_Z(r)+f_Z(-r)` for `r>0`. Then `0<=h<=2`, `int_0^infty h=1`, and the density of `Z^2` is

\[
p(y)={h(\sqrt y)\over2\sqrt y},\qquad y>0.
\]

Thus

\[
\int_0^\infty p(y)^{3/2}dy
=2^{-1/2}\int_0^\infty h(r)^{3/2}r^{-1/2}dr.
\]

The last integral is maximized under `0<=h<=2`, `int h=1` by `h=2 1_[0,1/2]`; its value is `2^{3/2}*2/sqrt2=4`. Hence `int p^{3/2}<=2sqrt2`, so `||p||_{3/2}<=2`. Output scaling gives (3.1). `QED`.

## 4. Enlarged non-diagonal three-coordinate theorem

The common product envelope removes the main restriction in the B12 hyperbolic block: the hyperbolic pair may now couple arbitrarily to the third selected coordinate.

### Theorem 4.1 — `QFORM-ZERO-DIAGONAL-PAIR-BLOCK-v1`

Let `X_1,...,X_n` be independent real random variables, each with probability density bounded by `1`, and let `Q(X)=X^TAX` for a real symmetric matrix `A`.

Assume that some three original coordinates, after relabeling as `1,2,3`, have principal block

\[
A_S=
\begin{pmatrix}
0&b&d\\
b&0&e\\
d&e&c
\end{pmatrix},
\qquad b\ne0,
\tag{4.1}
\]

with `det(A_S) != 0`. No restriction is imposed on the remaining principal block or on any couplings between these three coordinates and the other coordinates.

Then `Q(X)` is absolutely continuous and

\[
\boxed{
\|p_Q\|_\infty
\le C_0 |\det A_S|^{-1/3},
\qquad
C_0:=2^{1/3}\|H\|_3<7.90.
}
\tag{4.2}
\]

In particular, if `|det A_S|>=1`, then `||p_Q||_infty<7.90` universally.

#### Proof in dimension three

First ignore linear and constant terms. Write

\[
q(x,y,z)=2bxy+2dxz+2eyz+c z^2.
\tag{4.3}
\]

For a fixed `z`, set

\[
U=X+{e\over b}z,
\qquad
V=Y+{d\over b}z.
\tag{4.4}
\]

Conditional on `Z=z`, `U,V` remain independent, and each is merely a translate of an input density bounded by one. Algebra gives

\[
q(X,Y,z)=2bUV+\kappa z^2,
\qquad
\kappa=c-{2de\over b}.
\tag{4.5}
\]

By Lemma 2.1 and scaling, for every `z` the conditional density of `2bUV` is pointwise bounded by the *same* function `H_b`, independent of `z`. Therefore

\[
p_q(s)
\le \int f_Z(z)H_b(s-\kappa z^2)dz
=(H_b*p_{\kappa Z^2})(s).
\tag{4.6}
\]

Hölder/Young with exponents `3` and `3/2`, (2.10), and (3.1) give

\[
\begin{aligned}
\|p_q\|_\infty
&\le (2|b|)^{-2/3}\|H\|_3\cdot2|\kappa|^{-1/3}\\
&=2^{1/3}\|H\|_3\,|b|^{-2/3}|\kappa|^{-1/3}.
\end{aligned}
\tag{4.7}
\]

But

\[
\det A_S=-b^2c+2bde=-b^2\kappa.
\tag{4.8}
\]

Substituting (4.8) into (4.7) gives (4.2).

Now allow an arbitrary affine perturbation `ell^T(x,y,z)+gamma`. Since `A_S` is invertible, choose

\[
m={1\over2}A_S^{-1}\ell.
\]

Then

\[
v^TA_Sv+\ell^Tv+\gamma=(v+m)^TA_S(v+m)+\gamma-m^TA_Sm.
\tag{4.9}
\]

The coordinatewise shift `v -> v+m` preserves independence and the density cap, while the final constant only translates the output. Hence the same bound is uniform over all affine perturbations. `QED` in dimension three.

#### Passage to arbitrary dimension and arbitrary outside couplings

Let `W=(X_4,...,X_n)` and condition on `W=w`. The selected three coordinates remain independent with their original density caps. Every coupling from the selected coordinates to `w` becomes an affine linear term in `(X_1,X_2,X_3)`; the selected quadratic block remains exactly `A_S`. By (4.9), every conditional law has a density with the same cap `C_0 |det A_S|^{-1/3}`. Mixing over `w` preserves that `L^infinity` cap. This proves (4.2) for the full `n`-variable form. `QED`.

## 5. Exact relation to the peer B12 theorem

B12 treats

\[
A_S=
\begin{pmatrix}
0&a&0\\
a&0&0\\
0&0&\lambda
\end{pmatrix},
\]

and obtains the sharper constant `8|a|^{-2/3}|lambda|^{-1/3}` by an `L^3` norm estimate for the product density plus the square endpoint. Theorem 4.1 contains the same structural block but also permits arbitrary `d,e`, i.e. both members of the hyperbolic pair may interact quadratically with the third coordinate. The determinant identity

\[
|\det A_S|=|b|^2\left|c-{2de\over b}\right|
\]

shows exactly how those new couplings renormalize the effective third square after the `z`-dependent translations.

Thus the peer theorem is not merely cited: its product-plus-square mechanism is extended using a **common pointwise product envelope**, which is the ingredient needed when the pair’s translated input laws depend on the third coordinate.

## 6. Scope and first remaining universal implication

This does **not** prove the owner’s full spectral statement. Three global eigenvalues with magnitude at least one do not automatically force an original-coordinate principal block of the special form (4.1), nor do they force `|det A_S|>=1` for such a block.

The theorem does prove a new target-level subclass with:

* arbitrary dimension;
* arbitrary independent probability densities bounded by one;
* arbitrary signs;
* arbitrary couplings to all outside coordinates;
* a genuinely non-diagonal selected three-coordinate block;
* arbitrary couplings `d,e` inside that block;
* an explicit dimension-free density constant whenever `|det A_S|>=1`.

The next universal obligation is structural:

> Starting only from three eigenvalues of `A` with absolute value at least one, extract a bounded-size collection of original-coordinate conditional blocks to which either (i) a definite two-coordinate coarea bound, (ii) Theorem 4.1, or (iii) another product-preserving common-envelope estimate applies, with total loss bounded by a universal constant.

Equivalently for the B01/Fourier pathway, the new common-envelope lemma suggests looking for an integrated estimate built from product-preserving coordinate pairs rather than law-uniform one-direction stationary phase.

## 7. Status

**Proved here:**

1. a law-independent common pointwise envelope `H` for the density of a product of two independent density-`<=1` variables;
2. `H in L^3` with explicit `||H||_3<6.266`;
3. an averaged-frequency `L^3` characteristic-function consequence for that product;
4. a new non-diagonal arbitrary-dimensional block theorem with
   `||p_Q||_infinity < 7.90 |det A_S|^{-1/3}`
   for blocks (4.1), allowing arbitrary third-coordinate and outside couplings.

**Not proved:** the full arbitrary rotated-eigenbasis conjecture. No novelty claim is made. The named fleet04/B01 partner had no current QFORM output available at the checked source snapshot, so no result is attributed to it.
