SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B14, 2026-09-22T21:01:20Z.
attacking: singular-active kernel leakage — average subcritical outside-generated affine coefficients before worst-case localization or reciprocal payment.

# account02/B14 — subcritical kernel-leakage averaging and a singular-active Fourier-sup obstruction

**Run:** `20260922T210120Z-account02-B14-QFORM-r21`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Translations and localization / complementary constructions and source-valid counterexamples  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `SUPPORTING_TARGET_LEVEL_THEOREMS + REFUTED_INTERMEDIATE_MECHANISM`; full QFORM remains OPEN.

## 1. First unpaid implication and mechanism change

The previous B14 run proved an exact disjoint-bank compression theorem: whole original-coordinate banks may be projected to three independent scalar bank variables before reciprocal determinant payment. Its remaining structural debt was to find such banks, a physical cross block, or a ridge mechanism from the bare three-large-eigenvalue hypothesis.

The newest assigned-partner result, account03/B14 r18, supplies a complementary exact localization interface for an original-coordinate active block

\[
A=\begin{pmatrix}B&C\\ C^T&D\end{pmatrix}.
\]

It proves the expectation-before-supremum inequality

\[
\int_{\mathbb R}|\phi_Q(t)|\,dt
\le \mathbb E_V J_B(2CV;\mu_U),
\qquad
J_B(b;\mu):=\int_{\mathbb R}
\left|\mathbb E_\mu e^{it(U^TBU+b^TU)}\right|dt,
\tag{1.1}
\]

and then a sufficient worst-case bound using
`sup_{b in Range(C)} J_B(b;mu)`.  For invertible `B` every affine term in `Range(B)` can be translated away exactly; for singular `B`, only the kernel component `P_{ker B}b` is genuine leakage.

This run changes the mechanism at that precise point.  In singular blocks it can be fatal to replace the actual random leakage by a supremum.  Instead, keep the expectation in (1.1), prove a dimension-free **negative-moment bound for the actual outside-generated leakage**, and average any subcritical singularity before taking a reciprocal power.  This gives a new localization compiler and an explicit target-valid counterexample to the stronger singular-block Fourier-sup criterion.

## 2. Source-pinned inputs actually used

### 2.1 Assigned partner: active-block Fourier localization

Account03/B14 run `20260922T203640Z-account03-B14-QFORM-r18`, theorem `QFORM-ACTIVE-BLOCK-FOURIER-LOCALIZATION-v1`, canonical proof

`yspennstate/math-open-problems@ed8e20464e9cbfd43eefc9ada31eafb3abd8c472`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B14/20260922T203640Z-account03-B14-QFORM-r18/REPORT.md`,

read-back blob `6b029ff13406fc0299e21222934e56ef3850f85c`.

Besides the final sufficient supremum theorem, its equation (3.3) gives the stronger pre-supremum estimate (1.1).  It also proves the exact translation quotient: after taking a supremum over admissible active product laws, a vector `b` may be replaced by `P_{ker B}b`; range-compatible affine terms are pure translations.  It further localizes fixed affine Fourier budgets exactly to compact finite-fragment indicator product laws.  No moments, support radii or fragment-count bounds are used.

### 2.2 Product-safe projection density cap

Account02/B06 proved `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1` at

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

If `T` is a `d x n` matrix with orthonormal rows and `X` has independent cap-one coordinates, then `TX` has a density bounded by `e^{d/2}`.  At `d=1`, every unit linear form has density at most `sqrt(e)`.  The proof is an original-product Brascamp--Lieb argument and does not manufacture independence after rotation.

### 2.3 Corrections preserved

This report does not use law-uniform pointwise oscillatory decay, arbitrary-joint 3D coarea, a positive moment of conditional projection-density suprema, post-rotation independence, bounded support/diameter, a fixed fragment-count reduction, or one uniformly good physical minor.  In particular it respects the current `QFORM-JOINT-DENSITY-COAREA-23-FALSE-v1`, `QFORM-CONDITIONAL-PROJECTION-POSITIVE-MOMENT-FALSE-v1`, `QFORM-NO-UNIFORM-FRAGMENT-COUNT-BATHTUB-v1`, and aggregate-before-inversion corrections.

## 3. A translation-uniform negative-moment theorem for product linear images

The central elementary lemma is useful independently of Fourier localization.

### Theorem 3.1 — `QFORM-LINEAR-IMAGE-NEGATIVE-MOMENT-v1`

Let `X=(X_1,...,X_n)` have independent real probability densities bounded by one.  Let

\[
L:\mathbb R^n\to\mathbb R^d
\]

have rank `d`, write

\[
G=LL^T>0,
\]

and let `v_d` denote the volume of the Euclidean unit ball in `R^d`.  Then for every `a in R^d` and every

\[
0<\alpha<d,
\]

\[
\boxed{
\mathbb E|LX-a|^{-\alpha}
\le
\frac{d}{d-\alpha}
\,v_d^{\alpha/d}
\,e^{\alpha/2}
\,[\det G]^{-\alpha/(2d)}.
}
\tag{3.1}
\]

Equivalently, in the natural Mahalanobis metric of the linear image,

\[
\boxed{
\mathbb E
\left|G^{-1/2}(LX-a)\right|^{-\alpha}
\le
\frac{d}{d-\alpha}
\,v_d^{\alpha/d}
\,e^{\alpha/2}.
}
\tag{3.2}
\]

The bound is uniform in the translation `a`, support geometry, support diameter, fragment count, tails and moments.

### Proof

Normalize the linear map by

\[
T=G^{-1/2}L.
\]

Then `TT^T=I_d`.  By the product-safe projection theorem in Section 2.2, the random vector

\[
W=TX
\]

has a density `p_W` satisfying

\[
\|p_W\|_\infty\le e^{d/2}.
\tag{3.3}
\]

Because `LX=G^{1/2}W`, the density `p_Z` of `Z=LX` obeys

\[
\|p_Z\|_\infty
\le M:=e^{d/2}[\det G]^{-1/2}.
\tag{3.4}
\]

For any probability density `p<=M`, radial decreasing rearrangement maximizes

\[
\int |z-a|^{-\alpha}p(z)\,dz
\]

by filling a centered ball around `a` with density `M`.  Let its radius be `R`; probability one means

\[
Mv_dR^d=1.
\tag{3.5}
\]

Hence

\[
\begin{aligned}
\int |z-a|^{-\alpha}p(z)\,dz
&\le M d v_d\int_0^R r^{d-1-\alpha}\,dr\\
&=\frac{d}{d-\alpha}Mv_dR^{d-\alpha}\\
&=\frac{d}{d-\alpha}v_d^{\alpha/d}M^{\alpha/d}.
\end{aligned}
\tag{3.6}
\]

Inserting (3.4) proves (3.1).  Applying the same argument directly to `W-G^{-1/2}a` gives (3.2).  QED.

### Sharp threshold

The restriction `alpha<d` is genuine for a raw absolute negative moment.  If `L` selects `d` original coordinates and those coordinates are iid Uniform[-1/2,1/2], their joint density is positive near zero, so `E|LX|^{-alpha}` diverges for `alpha>=d` (logarithmically at equality).  Thus any localization route that produces a `d`-dimensional leakage singularity of critical order `d` must retain cancellation or a stronger joint mechanism.

## 4. Subcritical kernel-leakage averaging compiler

The preceding theorem plugs directly into the assigned partner's expectation-before-supremum inequality.

For a symmetric active block `B`, let

\[
K_0=\ker B,
\qquad
L=P_{K_0}C.
\]

Use an orthonormal coordinate system on `Range(L)` and write `d=rank L`, `G=LL^T` on that `d`-dimensional range.  Define the worst active-law Fourier budget at fixed leakage vector

\[
\mathcal J_B(k)
:=\sup_{\mu\in\mathcal D_m}J_B(k;\mu).
\tag{4.1}
\]

By the partner r18 theorem, the same quantity is obtained by taking the supremum only over compact finite-fragment indicator product laws.

### Theorem 4.1 — `QFORM-SUBCRITICAL-KERNEL-LEAKAGE-AVERAGING-v1`

Assume `d>=1` and that for some `L_0,H>=0` and `0<alpha<d`, every nonzero `k in Range(L)` satisfies the natural-metric envelope

\[
\mathcal J_B(k)
\le L_0+H\,|G^{-1/2}k|^{-\alpha}.
\tag{4.2}
\]

Then every full admissible product input satisfies

\[
\boxed{
\int_{\mathbb R}|\phi_{X^TAX}(t)|\,dt
\le L_0
+H\,2^{-\alpha}
\frac{d}{d-\alpha}
 v_d^{\alpha/d}e^{\alpha/2}.
}
\tag{4.3}
\]

Consequently the full quadratic form has a bounded continuous density with

\[
\boxed{
\|p_Q\|_\infty
\le\frac1{2\pi}
\left[
L_0
+H\,2^{-\alpha}
\frac{d}{d-\alpha}
 v_d^{\alpha/d}e^{\alpha/2}
\right].
}
\tag{4.4}
\]

No determinant or smallest-singular-value penalty appears because the local singularity is measured in the exact Mahalanobis metric generated by the leakage map.

### Proof

Condition on the outside original coordinates `V=v`.  The partner theorem gives

\[
\int|\phi_Q|
\le\mathbb E_VJ_B(2CV;\mu_U).
\tag{4.5}
\]

For each fixed `v`, decompose `2Cv` into its `Range(B)` and `ker B` parts.  Translating the active product law removes the `Range(B)` part exactly; translation preserves independence and the density caps.  Therefore

\[
J_B(2Cv;\mu_U)
\le \mathcal J_B(2Lv).
\tag{4.6}
\]

Apply (4.2), then (3.2) with the outside product vector `V` and translation zero:

\[
\begin{aligned}
\int|\phi_Q|
&\le L_0+H\,\mathbb E|G^{-1/2}(2LV)|^{-\alpha}\\
&\le L_0+H\,2^{-\alpha}
\frac{d}{d-\alpha}v_d^{\alpha/d}e^{\alpha/2}.
\end{aligned}
\]

This is (4.3); Fourier inversion gives (4.4).  QED.

### Euclidean-envelope variant

If the available active-block estimate has the weaker Euclidean form

\[
\mathcal J_B(k)\le L_0+H|k|^{-\alpha},
\tag{4.7}
\]

then Theorem 3.1 instead yields

\[
\int|\phi_Q|
\le L_0+H\,2^{-\alpha}
\frac{d}{d-\alpha}v_d^{\alpha/d}e^{\alpha/2}
[\det(LL^T)]^{-\alpha/(2d)}.
\tag{4.8}
\]

This makes the localization ordering explicit: average the actual `d`-dimensional leakage first, then pay its geometric mean scale; do not select one tiny coefficient or take `sup_k` before averaging.

## 5. Concrete density theorem: a zero-self cross block

The same negative-moment input gives a direct small-ball/density result with no integrated-Fourier hypothesis.

### Theorem 5.1 — `QFORM-ZERO-SELF-CROSS-AVERAGING-v1`

Choose an original-coordinate set `Z` and write the full matrix as

\[
A=\begin{pmatrix}0&C\\ C^T&D\end{pmatrix},
\tag{5.1}
\]

where `rank C=d>=2`.  Let

\[
\Delta_C:=\det_+(CC^T)
=\prod_{j=1}^d s_j(C)^2
\tag{5.2}
\]

be the product of the positive eigenvalues, equivalently the squared product of the nonzero singular values.  Allow arbitrary `D`, arbitrary deterministic affine perturbation `ell^T X+c`, and arbitrary independent cap-one coordinate laws.  Then the full quadratic form has an essentially bounded density satisfying

\[
\boxed{
\|p_Q\|_\infty
\le
\frac{e d}{2(d-1)}
 v_d^{1/d}
\Delta_C^{-1/(2d)}.
}
\tag{5.3}
\]

Equivalently, with cross geometric mean

\[
\gamma(C):=\Delta_C^{1/(2d)}
=\left(\prod_{j=1}^d s_j(C)\right)^{1/d},
\]

\[
\boxed{
\|p_Q\|_\infty\le c_d\,\gamma(C)^{-1},
\qquad
c_d=\frac{e d}{2(d-1)}v_d^{1/d}.
}
\tag{5.4}
\]

In particular

\[
c_2=e\sqrt\pi<4.819,
\qquad
c_3=\frac{3e}{4}(4\pi/3)^{1/3}<3.287,
\tag{5.5}
\]

and crudely `c_d<=2e` for every `d>=2`.

### Proof

Write the original variables as `(X_Z,V)`.  Conditioning on `V=v`,

\[
Q_v=(2Cv+\ell_Z)^TX_Z+q(v).
\tag{5.6}
\]

For every nonzero vector `a`, the scalar linear form `a^TX_Z` has density cap at most

\[
\sqrt e\,|a|^{-1}
\tag{5.7}
\]

by the `d=1` projection theorem from Section 2.2.  Since `rank C=d>=2`, the random vector `CV` has an absolutely continuous `d`-dimensional law, so the event `2CV+ell_Z=0` has probability zero in its range.  Thus the conditional density bound (5.7) may be averaged:

\[
\|p_Q\|_\infty
\le\frac{\sqrt e}{2}
\mathbb E|CV+\ell_Z/2|^{-1}.
\tag{5.8}
\]

Apply Theorem 3.1 with `alpha=1` and `G=CC^T` on `Range(C)`.  Because `alpha=1<d`,

\[
\mathbb E|CV+\ell_Z/2|^{-1}
\le
\frac{d}{d-1}v_d^{1/d}e^{1/2}
\Delta_C^{-1/(2d)}.
\tag{5.9}
\]

Multiplying by `sqrt(e)/2` gives (5.3).  QED.

### Scope

This theorem is fully translation-uniform and survives arbitrary distant fragments and unbounded supports.  The outside block `D` is completely arbitrary and may have any rank/signature; after conditioning it contributes only a scalar.  No moment or centering parameter appears.  The theorem is a genuine target-level branch, but the bare hypothesis `s_3(A)>=1` does **not** by itself guarantee a zero-self physical block whose cross geometric mean is bounded below.

## 6. Target-valid route counterexample: the singular active Fourier supremum is too strong

The partner r18 supremum criterion is an elegant sufficient condition.  For singular active blocks it is not a necessary interface, even on a very easy valid target family.

### Construction — `QFORM-SINGULAR-ACTIVE-FOURIER-SUP-TOO-STRONG-v1`

Take

\[
A=\begin{pmatrix}
0&I_2\\ I_2&0
\end{pmatrix}.
\tag{6.1}
\]

Its spectrum is exactly `{1,1,-1,-1}`, so it satisfies the full target's three-large-eigenvalue hypothesis.  Split the first two original coordinates as the active block.  Then

\[
B=0,
\qquad C=I_2,
\qquad K=P_{\ker B}\operatorname{Range}(C)=\mathbb R^2.
\tag{6.2}
\]

The partner's worst-case singular-block Fourier constant is infinite.  Indeed, let the two active variables be independent Uniform[-1/2,1/2] and choose `k=(1,0)`.  Then

\[
J_0(k)
=\int_{\mathbb R}
\left|\mathbb E e^{itU_1}\right|dt
=\int_{\mathbb R}\left|\frac{\sin(t/2)}{t/2}\right|dt
=\infty.
\tag{6.3}
\]

Therefore

\[
\boxed{\mathcal L(0,\mathbb R^2)=\infty.}
\tag{6.4}
\]

So no proof of full QFORM can require a finite `sup_{k in K}J_B(k)` for every singular active block.

Yet the same target matrix is uniformly easy when the actual outside randomness is retained.  Its quadratic form is

\[
Q=2(X_1X_3+X_2X_4).
\tag{6.5}
\]

Theorem 5.1 applies with `d=2`, `C=I_2`, `Delta_C=1`, and gives for **every** admissible product law

\[
\boxed{\|p_Q\|_\infty\le e\sqrt\pi<4.819.}
\tag{6.6}
\]

Thus this is a source-valid counterexample to an intermediate proof mechanism, not a counterexample to QFORM.  It identifies the correct localization order: in a singular active block, retain and average the random kernel leakage before imposing a worst-case affine Fourier budget.

## 7. Relation to arbitrary shifts, fragments, and unbounded supports

All three results above are deliberately insensitive to the usual localization pathologies.

1. **Arbitrary shifts.**  The negative-moment theorem is uniform in the center `a`; range-compatible active affine terms are exact translations by partner r18; kernel-affine terms are averaged through the actual outside law.
2. **Distant fragments.**  The product projection theorem is applied to the whole law before any reciprocal singularity.  No component is normalized separately, so the previous `N^2` fragment tax cannot arise.
3. **Unbounded supports and no moments.**  Only probability normalization and one-dimensional density caps are used.  The rearrangement estimate for negative moments does not involve tails or moments.
4. **Original-coordinate provenance.**  Every conditioning is on original coordinates.  Linear projections are used only through the product-safe Brascamp--Lieb density theorem; no independence is asserted after rotation.
5. **Criticality is visible.**  The sole new integrability requirement is `alpha<d`, exactly the Euclidean collision threshold of the leakage variable.  At the critical exponent an independent-uniform example already diverges.

## 8. Connection to the full target and first unpaid implication

The full quadratic-form conjecture remains OPEN.  The new work narrows a specific structural debt.

The previous B14 disjoint-bank theorem pays an exact three-bank self-interaction after aggregation.  The current Theorem 5.1 pays a rank-at-least-two **pure cross** block by averaging its actual outside-generated coefficient vector.  The partner r18 theorem pays arbitrary outside geometry at zero localization cost once an active integrated-Fourier budget is available, and identifies kernel leakage as the only non-translatable affine obstruction for singular active blocks.

The first unpaid implication is therefore:

> **`QFORM-LEAKAGE-OR-BANK-STRUCTURAL-BRIDGE-v1`.**  Starting from arbitrary symmetric `A` with at least three eigenvalues of magnitude at least one, produce a product-preserving branch which either
> (i) exposes an invertible/grouped active block with a universal homogeneous Fourier budget,
> (ii) exposes a rank-at-least-two zero-self or product-aligned kernel-leakage block whose cross geometric mean is bounded below and is paid by Theorem 5.1 / Theorem 4.1,
> (iii) exposes three disjoint coordinate banks paid by `QFORM-DISJOINT-BANK-COMPRESSION-v1`, or
> (iv) routes to one of the already-supported ridge/cross-block mechanisms.
>
> The structural argument must not replace actual singular-block leakage by `sup_k` before averaging, select one tiny physical minor, normalize support fragments before reciprocal payment, or condition inside a bank in a way that destroys product provenance.

A successful structural theorem of this kind would convert the translation/localization problem from an uncontrolled support issue into a finite list of already-paid geometric branches.  This report does not prove such a dichotomy and therefore does not claim full QFORM closure.

## 9. Source integrity and correction status


Repository retrieval was genuine, including the complete assigned-partner proof, but no authenticated native brain receiver-memory use occurred.  Execution therefore remains `WITHOUT_VERIFIED_BRAIN`.  No scheduler mutation, task creation, email/notification action, cross-account authentication, paid model/API/Codex call, public release, remote workflow, permission change, credential access, benchmark answer use, or unrelated private-data access occurred.
