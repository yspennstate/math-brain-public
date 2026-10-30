SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B15, 2026-09-24T11:16:54Z.
attacking: rigorous rough-product passage for ruled/Fresnel estimates using total-variation interval bounds, and a separate equicontinuity criterion for canonical continuous representatives.

# Rough-product interval passage and regularity closure

## Status

**NEW RIGOROUS LIMITING/TRACE THEOREM / FLEET01-B15 REGULARITY APPLIED / ESSENTIAL BOUNDEDNESS AND CONTINUITY SEPARATED / FULL QFORM OPEN.**

The full universal density-height conjecture remains open. This report closes the rough-input passage whenever the smooth-input estimate is already uniform. It does not manufacture a universal matrix receiver.

## 1. Product total-variation approximation

Let \(X=(X_1,\dots,X_n)\) have independent densities \(0\le f_i\le1\), \(\int f_i=1\). Choose a standard nonnegative smooth approximate identity \(\eta_m\) and put
\[
f_{i,m}=f_i*\eta_m.
\tag{1.1}
\]
Then
\[
0\le f_{i,m}\le1,\qquad \int f_{i,m}=1,\qquad
\|f_{i,m}-f_i\|_1\to0.
\tag{1.2}
\]
For the product densities \(F_m=\prod_i f_{i,m}\), \(F=\prod_i f_i\), telescoping gives
\[
\boxed{\|F_m-F\|_1\le\sum_{i=1}^n\|f_{i,m}-f_i\|_1\to0.}
\tag{1.3}
\]
Hence for every measurable map \(q:\mathbb R^n\to\mathbb R\), in particular every affine quadratic,
\[
\boxed{
\|\mathcal L(q(X^{(m)}))-\mathcal L(q(X))\|_{\rm TV}
\le\frac12\|F_m-F\|_1\to0.
}
\tag{1.4}
\]
No moment, support, tail, or boundary regularity assumption enters.

## 2. Interval domination is the correct rough trace

### Theorem \`QFORM-B15-ROUGH-INTERVAL-CLOSURE-v1\`

Let \(\mu_m\to\mu\) in total variation. Suppose
\[
\mu_m(I)\le C|I|
\tag{2.1}
\]
for every bounded interval \(I\), with the same \(C\). Then
\[
\boxed{\mu(E)\le C|E|\quad\text{for every Borel }E,}
\tag{2.2}
\]
so \(\mu=p\,dx\) with
\[
\boxed{\|p\|_{\infty,\mathrm{ess}}\le C.}
\tag{2.3}
\]

### Proof

Total variation gives \(\mu_m(I)\to\mu(I)\) for every interval, with no boundary qualification. Thus \(\mu(I)\le C|I|\). A finite disjoint union of intervals has the same bound by additivity. Every open subset of \(\mathbb R\) is a countable disjoint union of intervals, so monotone convergence gives \(\mu(O)\le C|O|\). By outer regularity, for every Borel \(E\),
\[
\mu(E)\le\inf_{O\supset E}\mu(O)\le C\inf_{O\supset E}|O|=C|E|.
\]
Radon--Nikodym differentiation gives (2.3). QED.

This proof never chooses or evaluates a pointwise version of the rough output density. It is therefore valid even when a smooth coarea formula has only been established almost everywhere.

## 3. Ruled-surface/coarea passage

Suppose a smooth-input ruled-surface calculation establishes, for every smooth cap-one product \(F_m\),
\[
\int_{\{x:q(x)\in I\}}F_m(x)\,dx
=\int_I\left[\int_{q^{-1}(t)}
 \frac{F_m(x)}{|\nabla q(x)|}\,d\mathcal H^{n-1}(x)\right]dt
\le C|I|.
\tag{3.1}
\]
The inner trace may be defined only for almost every \(t\); no pointwise representative is needed. Equations (1.4) and Theorem 2 pass (3.1) to arbitrary rough cap-one product inputs and give (2.3).

Equivalently, if one first truncates the coarea integrand by
\[
\mathbf1_{\{|\nabla q|\ge\varepsilon,\ |x|\le R\}},
\]
Tonelli applies to a nonnegative measurable integrand. Letting \(R\uparrow\infty\), then \(\varepsilon\downarrow0\), uses monotone convergence. The critical set of a nonconstant affine quadratic is Lebesgue-null, so it contributes no mass under an absolutely continuous product input. This supplies the requested marginal trace justification without silently evaluating an arbitrary density version.

## 4. Continuity is a separate compactness theorem

Interval domination alone does not imply that any density representative is continuous. The following additional hypothesis is sufficient.

### Theorem \`QFORM-B15-ROUGH-CONTINUOUS-CLOSURE-v1\`

In addition to (2.1), suppose each \(\mu_m\) has a continuous density \(p_m\) such that
\[
0\le p_m\le C,\qquad
|p_m(s)-p_m(t)|\le\omega(|s-t|)
\tag{4.1}
\]
for one modulus \(\omega(r)\downarrow0\), independent of \(m\). Then \(\mu\) has a canonical density \(p\in C_0(\mathbb R)\) satisfying
\[
\boxed{
0\le p\le C,\qquad
|p(s)-p(t)|\le\omega(|s-t|).
}
\tag{4.2}
\]

### Proof

On each compact interval, (4.1) gives uniform boundedness and equicontinuity. Arzela--Ascoli and a diagonal extraction give a subsequence converging locally uniformly to a continuous \(p\) with (4.2). For every compactly supported continuous \(\psi\),
\[
\int\psi p\,dt
=\lim_m\int\psi p_m\,dt
=\int\psi\,d\mu,
\tag{4.3}
\]
where the last equality follows from total-variation convergence. Hence \(\mu=p\,dt\); in particular \(p\in L^1\) and has mass one. A uniformly continuous integrable function on \(\mathbb R\) vanishes at infinity, so \(p\in C_0\). Uniqueness of the continuous representative removes subsequence dependence. QED.

A second sufficient route is a common integrable characteristic-function envelope. If \(|\phi_m(t)|\le G(t)\in L^1\), then pointwise convergence \(\phi_m\to\phi\) and dominated convergence give \(\phi\in L^1\) and uniform convergence of the inverse Fourier densities, again producing the canonical \(C_0\) representative.

## 5. Completed fleet01/B15 theorem applied at an actual inequality

The newest completed fleet01/B15 result is
\`ab80f487f4a73a6196cbf750db85577acbcb1563\`,
\`QFORM-FRESNEL-HALF-HOLDER-v1\`.

Under the Fresnel--Brascamp--Lieb chamber hypotheses, write
\[
M=|\lambda_1\lambda_2\lambda_3|\det G_I.
\]
For smooth cap-one product inputs it supplies the uniform inequalities
\[
\|p_m\|_\infty\le12M^{-1/3},
\tag{5.1}
\]
and
\[
|p_m(s)-p_m(t)|
\le32\sqrt{2\pi}\,M^{-1/2}|s-t|^{1/2}.
\tag{5.2}
\]
Apply Theorems 2 and 4 to the convolution approximants (1.1). For every arbitrary, possibly discontinuous and unbounded-support, cap-one product input,
\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}\le12M^{-1/3},
}
\tag{5.3}
\]
and separately the law has a canonical representative
\[
\boxed{
p_Q\in C_0(\mathbb R),\qquad
|p_Q(s)-p_Q(t)|
\le32\sqrt{2\pi}\,M^{-1/2}|s-t|^{1/2}.
}
\tag{5.4}
\]
Thus the fleet01/B15 regularity theorem extends to rough product densities with no pointwise trace assumption. Equation (5.3) is obtained from interval domination; equation (5.4) is obtained from uniform equicontinuity. Neither is inferred from the other.

For the explicit fleet01 matrix with nonzero eigenvalues \(1,2,4\), \(M=8\), so the rough-input conclusion is
\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}\le6,\qquad
|p_Q(s)-p_Q(t)|\le16\sqrt\pi\,|s-t|^{1/2}.
}
\tag{5.5}
\]

## 6. Remaining full-target implication

The regularity passage is now paid whenever a smooth/product-preserving chamber estimate gives a uniform interval bound and modulus. The remaining owner-wide gap is not absolute continuity or approximation. It is structural: starting solely from \(s_3(A)\ge1\), obtain one universal product-preserving height receiver for every matrix. Continuity can then be addressed only if that receiver also supplies a uniform modulus or an integrable Fourier envelope.

The full universal density bound remains **OPEN**. The full-target continuity statement remains **OPEN**.

Fresh source: fleet01/B15 at \`ab80f487f4a73a6196cbf750db85577acbcb1563\`, rigor check \`1023d4db726aee0c5b303c8426c65b44376b210f\`. Standing owner controls and Claude-review corrections were preserved. No schedule, notification, authentication, workflow, permission, or production-store state was changed.
