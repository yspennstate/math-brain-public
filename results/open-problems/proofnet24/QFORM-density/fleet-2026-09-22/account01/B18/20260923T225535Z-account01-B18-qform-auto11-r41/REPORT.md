SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B18, 2026-09-23T22:55:35Z.
attacking: the newest account02/B18 near-parallel coupled stress family; condition only the K-bank sum B so X0+eta V is automatically cap-one by convolution, then feed the surviving J-bank pair into the completed scalar/dependent-pair receiver.

# account01/B18 r41 — convolution-before-conditioning closes the near-parallel partner family

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Role:** Literature-to-proof transfer  
**Status:** PROVED SUPPORTING TARGET-VALID FAMILY CLOSURE / FULL QFORM OPEN  
**Execution:** WITHOUT_VERIFIED_BRAIN

## 1. Fresh target and corrections

The owner target remains: for independent real coordinates with one-dimensional densities bounded by one and a symmetric matrix with at least three eigenvalues of modulus at least one, prove one universal finite density bound for the quadratic form; continuity is tracked separately.

This report does **not** claim the full theorem. It preserves the live corrections: no post-rotation independence; no arbitrary-joint three-dimensional coarea; no replacement of genuine independence by a conditional density cap; no deletion of a small nonzero coefficient; no law-uniform pointwise Fresnel decay; no worst-fiber substitution; and no fixed-good-minor inference.

The newest designated partner handoff is account02/B18 `account02-B18-20260923T220809Z-a35ad7e4`, canonical mathematics `yspennstate/math-open-problems@c666bf6ec06dea6643ea0a0b8cd054edf5d893a6`. It isolates the target-valid family

\[
Q_{m,\eta}=2X_0G+2\eta GV+(b_0C+\rho B)^2,
\qquad b_0=\frac{\sqrt{63}}8,\quad \rho=\frac18,
\]

with disjoint original-coordinate source blocks: `X0`, a J-bank producing `(G,C)`, and a K-bank producing `(B,V)`. Its nonzero physical spectrum is exactly

\[
\{-\sqrt{1+\eta^2},\ 1,\ \sqrt{1+\eta^2}\}.
\]

The partner proves that conditioning away the complementary J source can create a nonlinear private-bank density spike of order `|eta|^{-1/2}` and therefore rules out a supremum-over-conditioned-private-bank interpolation. That obstruction is accepted here; the proof below conditions in the opposite direction.

## 2. Primary theorem transferred literally

Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), Theorem 1.1, arXiv:1507.07949, proves: if

\[
f(x)=\prod_{j=1}^N f_j(x_j),\qquad \|f_j\|_\infty\le1,
\]

then every `k`-dimensional orthogonal marginal has density at most `2^{k/2}`. No moment, iid, support, log-concavity, centering, symmetry, or smoothness hypothesis is imposed.

In the partner family the J-bank coefficient vectors of `G` and `C` are orthonormal. Therefore

\[
\boxed{\ \|p_{(G,C)}\|_\infty\le2.\ }
\tag{2.1}
\]

This is used only as a joint-density cap. No independence of `G` and `C` is asserted.

## 3. Completed partner-compatible analytic receiver

The completed account02/B18 theorem `QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-v1`, source

`yspennstate/math-open-problems@ba2e2fbc9d22196f83c4ae35080e7f3d23a55fa1`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260923T013147Z-bf13c29b/REPORT.md`,

states the following. Let `S` be a scalar with density cap `K`, genuinely independent of a possibly dependent pair `(Y,Z)` whose joint density has cap `M`. Then

\[
R=2\beta SY+\alpha Y^2+2\delta YZ+\gamma Z^2,
\qquad \beta\gamma\ne0,
\]

has an essentially bounded density and

\[
\boxed{
\|p_R\|_\infty
\le3(2MK)^{2/3}|\beta^2\gamma|^{-1/3}.
}
\tag{3.1}
\]

The pair coordinates need not be independent.

## 4. New lemma — conditional convolution restores a cap-one scalar

### Lemma 4.1 (`QFORM-CONDITION-OTHER-BANK-CONVOLUTION-v1`)

Let `X0` have density `f0` with `||f0||_infty<=1`. Let `(B,V)` be any real random pair independent of `X0`; no density hypothesis on `(B,V)` is needed. For any real `eta`, choose a regular conditional law `mu_b` of `V` given `B=b` and define

\[
T_b=X_0+\eta V\quad\text{under the conditional law }B=b.
\]

Then for almost every `b`, `T_b` has a density bounded by one.

**Proof.** Conditional on `B=b`, `X0` remains independent of `V` because `X0` is independent of the whole pair `(B,V)`. Hence

\[
p_{T_b}(t)=\int f_0(t-\eta v)\,\mu_b(dv).
\]

Since `mu_b` is a probability measure,

\[
0\le p_{T_b}(t)\le\|f_0\|_\infty\le1.
\]

No conditional density of `V` is required. QED.

This elementary `L^\infty` contraction is exactly the averaging that is lost if one conditions on the J-bank first.

## 5. New target-family theorem

### Theorem 5.1 (`QFORM-NEARPARALLEL-HUB-CONVOLUTION-CLOSURE-v1`)

Let the source sets of `X0`, the J-bank, and the K-bank be pairwise disjoint original-coordinate sets. Assume:

1. `X0` has density cap at most one;
2. `(G,C)` is a two-dimensional orthogonal projection of the cap-one product law on the J-bank;
3. `(B,V)` is any K-bank statistic independent of the first two source blocks;
4. `b\ne0` and

\[
Q=2GX_0+2\eta GV+(bC+\rho B)^2.
\]

Then, for every real `eta,rho`,

\[
\boxed{
\|p_Q\|_\infty
\le 3\,4^{2/3}|b|^{-2/3}.
}
\tag{5.1}
\]

**Proof.** Condition only on `B=b_*`. Set

\[
T=X_0+\eta V.
\]

By Lemma 4.1, under the conditional law `B=b_*`, `T` has density cap `K<=1`.

Because the J-bank is independent of the joint source `(X0,B,V)`, conditioning on the K-measurable variable `B` preserves genuine independence between `(G,C)` and `T`: for bounded test functions `a,c`,

\[
\mathbb E[a(T)c(G,C)\mid B]
=
\mathbb E[a(T)\mid B]\,\mathbb E[c(G,C)].
\]

By the primary LPP theorem, `(G,C)` has joint density cap at most two. Translate only the second coordinate of that pair,

\[
D=C+\frac{\rho b_*}{b}.
\]

The pair `(G,D)` still has joint density cap `M<=2` and remains independent of `T`. Moreover, exactly,

\[
Q\mid\{B=b_*\}=2TG+b^2D^2.
\]

Apply (3.1) with

\[
S=T,\quad Y=G,\quad Z=D,\quad
K\le1,\quad M\le2,\quad
\beta=1,\quad \alpha=\delta=0,\quad \gamma=b^2.
\]

This gives, uniformly for almost every `b_*`,

\[
\|p_{Q\mid B=b_*}\|_\infty
\le 3(4)^{2/3}|b^2|^{-1/3}
=3\,4^{2/3}|b|^{-2/3}.
\]

Finally, for every Borel set `E`, disintegration yields

\[
\Pr(Q\in E)
=\mathbb E[\Pr(Q\in E\mid B)]
\le 3\,4^{2/3}|b|^{-2/3}|E|.
\]

Therefore the unconditional law is absolutely continuous with the same essential density bound. QED.

### Why this does not violate the live conditional-cap correction

No conditional density cap is used as a substitute for independence. The scalar/pair independence comes from disjoint ORIGINAL source blocks. The only conditional estimate is the convolution identity for `X0+eta V`, which uses the genuine independence of `X0` from the entire K-bank. The J projection is never rotated into independent coordinates; LPP supplies only its two-dimensional joint-density cap.

## 6. Application to the newest account02/B18 stress family

For the partner family

\[
b=b_0=\frac{\sqrt{63}}8,
\qquad b_0^2=\frac{63}{64}.
\]

Theorem 5.1 gives for **every** even `m`, every real `eta`, and every admissible cap-one product input law,

\[
\boxed{
\|p_{Q_{m,\eta}}\|_\infty
\le
3\,4^{2/3}\left(\frac{64}{63}\right)^{1/3}
=7.599314012743973\ldots<7.600.
}
\tag{6.1}
\]

This is uniform through the singular-looking near-parallel limit `eta -> 0`. It strictly improves the previously recorded natural-decomposition estimates `10.7188818574 |eta|^{-1/3}` for `eta!=0` and `76.1092553602` at `eta=0` on this family.

The partner's private conditional spike therefore reflects a **bad conditioning order**, not an output-density obstruction for this stress family. The product-preserving repair is: condition the K-bank sum `B` first, retain `X0` as a convolution smoother for `eta V`, and only then use the J-bank two-dimensional projection.

The matrix is target-valid because its three nonzero eigenvalues are

\[
-\sqrt{1+\eta^2},\quad1,\quad\sqrt{1+\eta^2},
\]

all of modulus at least one.

## 7. Continuity and full-target status

The completed scalar/dependent-pair receiver used in (3.1) establishes essential boundedness. This report does **not** promote the new branch to a continuous representative; continuity remains separate.

The unrestricted owner conjecture remains OPEN. The new theorem depends on a concrete source decomposition with a singleton independent smoothing coordinate `X0`, a J-bank yielding an orthogonal two-dimensional projection, and a K-bank whose `B` can be conditioned while retaining the smoother. The bare hypothesis of three large eigenvalues does not yet force such a decomposition. The next structural question is whether a general heavy/near-parallel state can be compiled into this `condition-other-bank + convolution-smoother + dependent-pair` packet, or routed into an already-paid ridge/physical-pivot/grouped-cross branch without discarding extra spectrum.

## 8. Source-validity / novelty boundary

Primary source applied: Livshyts--Paouris--Pivovarov, Theorem 1.1, arXiv:1507.07949 / Israel J. Math. 216 (2016). Internal analytic receiver applied: account02/B18 `QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-v1` at commit `ba2e2fbc9d22196f83c4ae35080e7f3d23a55fa1`. Designated partner family/obstruction applied: account02/B18 at commit `c666bf6ec06dea6643ea0a0b8cd054edf5d893a6`.

No exact published theorem closing the unrestricted owner target is asserted here, and no novelty claim is inferred from the targeted literature check.
