# account03/B14 — localization order and fragmentwise recentering tax

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T193756Z-account03-B14-QFORM-r17`  
**Assignment:** translations and localization  
**Startup control:** `yspennstate/math-research-brain@02127e5ec901c0b4f14f28fe2a6e09722af5e247`  
**Owner control at startup:** `2026-09-22.14`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** proved a target-relevant no-go for a tempting localization compiler and a corrected constant-preserving ordering principle; full QFORM remains OPEN. Continuity is not proved.

## 1. Why this run changes mechanism

The preceding B14 run proved a determinant-scale bound for one nonsingular physical principal triple,

\[
\|p_Q\|_\infty\le C_0 |\det B|^{-1/3},\qquad C_0=32\sqrt{10}.
\]

The remaining full-target problem is not local smoothing on one good triple, but how to aggregate many small physical pieces without paying the reciprocal determinant of one tiny piece. A natural but dangerous continuation is to localize each one-dimensional extreme set into its connected interval components, normalize every component, recenter each component separately, apply a translation-uniform local certificate, and finally average the componentwise \(L^\infty\) bounds.

This report proves that this compiler is intrinsically non-uniform even on the easiest diagonal target. The loss is algebraic and comes entirely from normalizing fragments before applying a positively homogeneous reciprocal-scale estimate.

## 2. General fragment-tax lemma

Let \(d\ge1\). Suppose a local density certificate for a \(d\)-coordinate block \(B\) has the following exact diagonal-scaling law: for \(D_\ell=\operatorname{diag}(\ell_1,\dots,\ell_d)\),

\[
K(D_\ell B D_\ell)=K(B)\prod_{i=1}^d \ell_i^{-\beta_i},
\qquad \beta_i\ge0.
\tag{2.1}
\]

For coordinate \(i\), let a unit-measure extreme input set be a disjoint union of intervals

\[
E_i=\bigsqcup_{k\in\mathcal K_i} I_{ik},
\qquad \ell_{ik}:=|I_{ik}|,
\qquad \sum_k \ell_{ik}=1.
\]

Condition on the component labels \((k_1,\dots,k_d)\). The label probability is

\[
w_{k_1,\dots,k_d}=\prod_i \ell_{ik_i}.
\]

After affine normalization of each selected interval to a unit interval, the active Hessian is congruent to

\[
D_\ell B D_\ell,
\qquad D_\ell=\operatorname{diag}(\ell_{1k_1},\dots,\ell_{dk_d}),
\]

while interval locations contribute only affine and scalar terms. Therefore any proof that discards those locations by applying the translation-uniform certificate separately to each normalized component and then uses the triangle inequality obtains at best

\[
\begin{aligned}
\|p_Q\|_\infty
&\le \sum_{k_1,\dots,k_d} w_{k_1,\dots,k_d}
      K(D_\ell B D_\ell)\\
&=K(B)\prod_{i=1}^d
   \left(\sum_{k\in\mathcal K_i}\ell_{ik}^{1-\beta_i}\right).
\tag{2.2}
\end{aligned}
\]

This is an exact computation of the compiler's cost, not merely an upper estimate on the number of fragments.

### Consequence

If some \(\beta_i>0\), no universal bound on the factor in (2.2) is possible over arbitrary fragmentations. Indeed, split coordinate \(i\) into \(N\) equal intervals of length \(1/N\). Then

\[
\sum_{k=1}^N \ell_{ik}^{1-\beta_i}
=N(1/N)^{1-\beta_i}=N^{\beta_i}.
\tag{2.3}
\]

Hence every positive inverse fragment-scale exponent creates a divergent fragmentation tax under componentwise normalization and \(L^\infty\)-triangle averaging.

The statement is about this proof compiler. It does not say the original output density is large, and it does not refute constant-preserving localization of whole unit-measure extreme sets.

## 3. Exact tax for the B14 principal-triple determinant theorem

For the completed B14 certificate

\[
K(B)=C_0|\det B|^{-1/3},\qquad C_0=32\sqrt{10},
\]

we have

\[
\det(D_\ell B D_\ell)
=(\ell_1\ell_2\ell_3)^2\det B.
\]

Therefore

\[
K(D_\ell B D_\ell)
=C_0|\det B|^{-1/3}
 (\ell_1\ell_2\ell_3)^{-2/3}.
\]

Thus \(\beta_1=\beta_2=\beta_3=2/3\), and (2.2) becomes

\[
\boxed{
\|p_Q\|_\infty\ \text{(fragmentwise compiler)}\
\le C_0|\det B|^{-1/3}
\prod_{i=1}^3\left(\sum_k \ell_{ik}^{1/3}\right).
}
\tag{3.1}
\]

If each coordinate is partitioned into \(N\) equal components, then

\[
\sum_{k=1}^N (1/N)^{1/3}=N^{2/3},
\]

so the product tax is exactly

\[
\boxed{N^2.}
\tag{3.2}
\]

Nothing about the quadratic law has changed; only the proof has artificially conditioned on a finer label.

## 4. Target-valid witness showing the loss is artificial

Take the exact target instance

\[
A=I_3,
\qquad X_1,X_2,X_3\stackrel{\rm ind}{\sim}\mathrm{Unif}[0,1].
\]

The output is

\[
Q=X_1^2+X_2^2+X_3^2.
\]

The completed separable theorem already gives the dimension-free bound

\[
\|p_Q\|_\infty\le \pi.
\]

Now partition each copy of \([0,1]\) into \(N\) consecutive intervals of equal length \(1/N\). This does not change the law at all. Nevertheless, if one conditions on the three interval labels, maps every selected component to a normalized unit interval, erases its location by translation invariance, invokes the determinant-homogeneous certificate on each conditional law, and then triangle-averages the conditional \(L^\infty\) bounds, (3.2) produces

\[
32\sqrt{10}\,N^2.
\]

The ratio between this proof bound and the true already-proved bound \(\pi\) diverges like \(N^2\). Hence the divergence is a pure proof artifact caused by the ordering

\[
\text{fragment}\to\text{normalize}\to\text{recenter}\to L^\infty\text{-bound}\to\text{average}.
\]

This witness stays inside the exact QFORM input class and uses no rotation, moment assumption, compactness hypothesis beyond the example itself, or numerical approximation.

## 5. Correct ordering: whole-set localization, then center once

The partner result account04/B14, `QFORM-CENTERED-AFFINE-LOCALIZATION-EQUIVALENCE-v1`, proves exactly

\[
C_{\rm hom}=C_{\rm ca}=C_{\rm ff},
\]

where `ff` consists of centered compact finite unions of intervals of total measure one and the affine term is range-compatible. Its canonical source is

`yspennstate/math-open-problems@1250c776b3840b8494ace461b27541f8e156e9bf:proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260922T182134Z-account04-B14-centered-affine-r3/REPORT.md`.

Apply that theorem to the actual inequality here. The whole extreme set \(E_i\), however disconnected, is kept as one probability density \(1_{E_i}\). It is translated once by its whole-set barycenter. The identity

\[
X^TAX=Y^TAY+2(Am)^TY+m^TAm
\]

shows that this global recentering creates only the range-compatible affine term covered by the partner theorem. There is no component normalization and therefore no \(\ell_{ik}^{-\beta_i}\) payment. Arbitrary component separation, count, and support diameter remain present inside the centered unit set and cost exactly zero at the localization stage.

Thus the partner theorem gives the positive replacement principle:

> **localize globally to whole unit-measure extreme sets, center each coordinate once at the whole-set level, and retain all internal fragments jointly through the smoothing estimate.**

The fragment-tax calculation proves why the order cannot in general be interchanged when the downstream certificate carries positive inverse scaling exponents.

## 6. `QFORM-FRAGMENTWISE-RECENTERING-TAX-v1`

The preceding argument proves the following target-relevant no-go.

### Theorem

Any QFORM proof scheme with all of the following features is not dimension/fragment-uniform:

1. a unit-measure extreme marginal is disintegrated into interval components;
2. each chosen component is normalized separately to unit mass/scale;
3. component locations are removed before aggregation using translation-uniformity;
4. the local conditional certificate has a positive inverse scaling exponent in at least one fragmented coordinate;
5. final assembly uses the triangle inequality for conditional \(L^\infty\) norms.

Its unavoidable tax is (2.2), and for the determinant-triple certificate the tax is exactly (3.1), equal to \(N^2\) under equal \(N\)-fragment partitions in all three coordinates.

This theorem does **not** refute QFORM, the partner's whole-set localization theorem, or finite-fragment extremality without a uniform fragment-count cap. It refutes only the componentwise normalize/recenter/take-sup/average compiler.

## 7. Implication for aggregate-before-inversion

The remaining full-target bridge must aggregate before paying reciprocal local scales. In localization language, at least one of the following has to happen:

- preserve all internal fragment locations until after the smoothing/payment is summed;
- use a mass-linear estimate at the whole-set level, rather than a normalized component estimate;
- exploit cancellation or displacement information between components before taking \(L^\infty\) suprema;
- or select/group physical coordinates before any fragment normalization, so the certificate sees original-coordinate geometry rather than tiny congruence-scaled Hessians.

This is directly relevant to the current grouped/ridge/aggregate-before-inversion programme: a proof that first localizes into tiny normalized boxes and then pays one reciprocal determinant per box cannot close the conjecture, even though whole-set localization itself is exactly constant-preserving.

## 8. Scope, corrections, and continuity

Used premises:

- account04/B14 `QFORM-CENTERED-AFFINE-LOCALIZATION-EQUIVALENCE-v1` at the source pinned above;
- account03/B14 `QFORM-PRINCIPAL-TRIPLE-DETERMINANT-LOCALIZATION-v1` at `yspennstate/math-open-problems@5e82f7573bc426a28a01fa25b0a2707ab0b573e2`;
- the completed separable density bound \(\pi\) for the witness.

Respected live corrections: no pointwise van-der-Corput bound, no independence after spectral rotation, no arbitrary-joint coarea bound, no positive conditional-projection-density moment, no bounded support diameter, and no universal fragment-count cap.

The theorem concerns essential-boundedness proof architecture. It neither proves nor disproves the requested continuous representative. Full QFORM remains OPEN.
