# fleet02/B15 — ruled rough-input audit, affine extension, and tent reduction

Run: `20260923T000548Z-fleet02-B15-QFORM`
Programme: `QFORM-DENSITY-3EIG-20260922`
Role: absolute continuity and regularity; complementary constructions/source-valid counterexamples
Status: `SUPPORTING_THEOREM_PROVED / PARTNER_BRIDGE_INDEPENDENTLY_CHECKED`
Full universal QFORM theorem: **OPEN**.
Execution context: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

The target remains the universal estimate

\[
  \Pr\{X^TAX\in I\}\le C|I|
\]

for every finite dimension, every product law with one-dimensional densities bounded by one, and every real symmetric \(A\) with at least three eigenvalues of modulus at least one.  Continuity is a separate regularity conclusion and is not used below to infer the height bound.

The newest Claude-attributed source used here is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`,

whose Theorem C gives a dimension-free ruled estimate on the one-sheet side of an exact rank-three form of signature `(+,+,-)`.  I independently check the rough-input bridge completed by the designated partner fleet03/B15, and then apply the ruled estimate to the owner-relevant positive tent functional.  The result isolates the exact remaining obstruction to the two-sheet side.

## 2. Exact ruled theorem and independent audit of the rough-input bridge

Let \(X=(X_1,\ldots,X_n)\) have independent densities \(0\le f_i\le1\).  Let \(r_1,r_2,r_3\in\mathbb R^n\) be orthonormal and set

\[
Y_k=\langle r_k,X\rangle,
\qquad
Q=\lambda_1Y_1^2+\lambda_2Y_2^2-\mu Y_3^2,
\qquad \lambda_1,\lambda_2,\mu\ge1.
\]

The partner fleet03/B15 report at

`yspennstate/math-open-problems@b4c8edd512776799decc9a16a40a3b37afba45b6`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B15/20260922T233101Z-fleet03-B15-qform-r21/REPORT.md`

proves, for every interval \(I\subset[0,\infty)\),

\[
\Pr(Q\in I)\le C_+(\lambda_1,\lambda_2,\mu)|I|,
\]

where

\[
C_+=(\lambda_1\lambda_2\mu)^{-1/2}
\int_0^{2\pi}
\frac{d\theta}{\sqrt{\sin^2\theta/\lambda_1+\cos^2\theta/\lambda_2+1/\mu}}
\le \pi\sqrt2.
\tag{2.1}
\]

I checked the bridge independently, including the factors that are easy to lose.

### 2.1 Cap-preserving smoothing and total variation

For independent standard Gaussians \(G_i\), define \(X_i^{(\varepsilon)}=X_i+\varepsilon G_i\).  Then

\[
f_i^{(\varepsilon)}=f_i*\gamma_\varepsilon,
\qquad 0\le f_i^{(\varepsilon)}\le1,
\qquad \|f_i^{(\varepsilon)}-f_i\|_1\to0.
\]

For finite \(n\), the tensor-product telescoping inequality gives

\[
\left\|\bigotimes_i f_i^{(\varepsilon)}-\bigotimes_i f_i\right\|_1
\le \sum_i\|f_i^{(\varepsilon)}-f_i\|_1\to0.
\tag{2.2}
\]

Pushforward under a measurable map contracts total variation, so the quadratic output laws converge in total variation.  Thus a uniform interval inequality for the padded laws passes to the original rough law without any continuity assumption on the inputs.

### 2.2 Ruled coordinates and exact Jacobian

Put

\[
D=\operatorname{diag}(\sqrt{\lambda_1},\sqrt{\lambda_2},\sqrt\mu),
\quad Z=DY,
\quad q(z)=z_1^2+z_2^2-z_3^2.
\]

For \(s>0\), define

\[
e_\theta=(\cos\theta,\sin\theta,0),
\quad e_\theta^\perp=(-\sin\theta,\cos\theta,0),
\quad d_\theta=e_\theta^\perp+e_3,
\]

and

\[
F(s,\theta,t)=\sqrt{s}\,e_\theta+t d_\theta.
\]

Then \(q(F)=s\).  Direct differentiation gives

\[
\partial_sF=(2\sqrt{s})^{-1}e_\theta,
\quad
\partial_\theta F=\sqrt{s}\,e_\theta^\perp-t e_\theta,
\quad
\partial_tF=e_\theta^\perp+e_3,
\]

hence

\[
\left|\det(\partial_sF,\partial_\theta F,\partial_tF)\right|=\frac12.
\tag{2.3}
\]

For the padded law, \(Y_\varepsilon\) has a smooth density \(\rho_\varepsilon\), because \(R^TG\) is a nondegenerate standard Gaussian in \(\mathbb R^3\).  Therefore for \(I\subset(0,\infty)\), ordinary change of variables gives

\[
\Pr(Q_\varepsilon\in I)
=
\frac1{2\det D}
\int_I\int_0^{2\pi}\int_{\mathbb R}
\rho_\varepsilon(D^{-1}F(s,\theta,t))\,dt\,d\theta\,ds.
\tag{2.4}
\]

No coarea trace of a merely measurable representative is being evaluated.

### 2.3 Product-projection cap and line parameter

For fixed \(\theta\), put

\[
v_\theta=D^{-1}d_\theta=
\left(-\frac{\sin\theta}{\sqrt{\lambda_1}},
\frac{\cos\theta}{\sqrt{\lambda_2}},
\frac1{\sqrt\mu}\right).
\]

Let \(E_\theta\) be an orthonormal basis of \(v_\theta^\perp\).  Then

\[
U_\theta=E_\theta^TY_\varepsilon=(RE_\theta)^TX^{(\varepsilon)},
\]

and the two columns of \(RE_\theta\) are orthonormal in \(\mathbb R^n\).  The two-dimensional product-projection theorem used in the source therefore yields

\[
\|p_{U_\theta}\|_\infty\le2.
\tag{2.5}
\]

Because the padded density is smooth, this is a pointwise usable bound.  For
\(y_0=D^{-1}(\sqrt{s}\,e_\theta)\), the fibre through \(y_0\) parallel to \(v_\theta\) gives

\[
\int_{\mathbb R}\rho_\varepsilon(y_0+t v_\theta)\,dt
=
\frac1{|v_\theta|}\,p_{U_\theta}(E_\theta^Ty_0)
\le\frac2{|v_\theta|}.
\tag{2.6}
\]

The factor \(1/|v_\theta|\), rather than \(|v_\theta|\), is correct because \(t\) is not arclength.

Substituting (2.6) into (2.4) gives

\[
\Pr(Q_\varepsilon\in I)
\le
\frac{|I|}{\det D}
\int_0^{2\pi}\frac{d\theta}{|v_\theta|}
=C_+|I|.
\tag{2.7}
\]

Moreover

\[
\frac1{\det D\,|v_\theta|}
=
\frac1{\sqrt{\lambda_2\mu\sin^2\theta+
\lambda_1\mu\cos^2\theta+
\lambda_1\lambda_2}}
\le \frac1{\sqrt2},
\]

which proves the numerical constant \(C_+\le\pi\sqrt2\).  Total-variation passage via (2.2) yields (2.1) for arbitrary measurable cap-one marginals.  Finally \(\Pr(Q=0)=0\), because the source product law is absolutely continuous in \(\mathbb R^n\) and the zero set of the nonzero quadratic polynomial has Lebesgue measure zero, so intervals meeting the critical value are also covered.

**Audit verdict:** PASS.  I found no hidden continuity, support, moment, Gaussianity, or post-rotation independence assumption in the partner bridge.  Gaussian padding is used only as a cap-preserving approximation device to make the trace pointwise legitimate; the estimate is then returned to the original product law by total variation.

## 3. New affine-in-range extension

The ruled estimate is invariant under deterministic spectral translation, and this can be implemented without rotating the independent coordinates.

Let \(a=(a_1,a_2,a_3)\in\mathbb R^3\), \(c\in\mathbb R\), and define

\[
Q_{a,c}
=
\lambda_1(Y_1-a_1)^2+
\lambda_2(Y_2-a_2)^2-
\mu(Y_3-a_3)^2+c.
\tag{3.1}
\]

Set \(h=Ra\in\mathbb R^n\) and \(X'=X-h\).  This is a deterministic coordinatewise translation of the physical variables.  Hence the coordinates of \(X'\) remain independent and each translated density is still bounded by one.  Since \(R^TX'=Y-a\), the partner theorem applies verbatim to \(X'\).  Therefore for every interval \(I\subset[c,\infty)\),

\[
\boxed{
\Pr(Q_{a,c}\in I)\le C_+(\lambda_1,\lambda_2,\mu)|I|
\le\pi\sqrt2\,|I|.
}
\tag{3.2}
\]

Equivalently, every exact-rank-three affine quadratic polynomial

\[
X^TAX+b^TX+c_0
\]

with signature `(+,+,-)`, \(|\lambda_k(A)|\ge1\), and \(b\in\operatorname{range}(A)\), has its majority-sign one-sheet submeasure bounded by \(\pi\sqrt2\).  Indeed \(b\in\operatorname{range}(A)\) is exactly the condition allowing completion of the square inside the three-dimensional spectral range.  By negating the form, the same assertion holds for signature `(-,-,+)` on its majority-sign one-sheet side.

This affine extension is useful because it is obtained by **physical deterministic translation**, which preserves the original-coordinate product structure; no independence after spectral rotation is asserted.

## 4. Direct application to the owner-relevant tent functional

For \(\varepsilon>0\) and \(y\in\mathbb R\), define the triangular kernel

\[
\tau_{\varepsilon,y}(s)=(\varepsilon-|s-y|)_+.
\]

Its Lebesgue integral is

\[
\int_{\mathbb R}\tau_{\varepsilon,y}(s)\,ds=\varepsilon^2.
\tag{4.1}
\]

Let \(\mu_+\) be the one-sheet submeasure of (3.1), supported on \([c,\infty)\).  From (3.2), \(d\mu_+/ds\) exists and is bounded by \(C_+\).  Therefore

\[
\boxed{
\mathbb E\big[(\varepsilon-|Q_{a,c}-y|)_+\,\mathbf1_{\{Q_{a,c}\ge c\}}\big]
\le C_+\varepsilon^2
\le\pi\sqrt2\,\varepsilon^2.
}
\tag{4.2}
\]

Thus the normalized tent height obeys

\[
\boxed{
\varepsilon^{-2}
\mathbb E\big[(\varepsilon-|Q_{a,c}-y|)_+\,\mathbf1_{\{Q_{a,c}\ge c\}}\big]
\le \pi\sqrt2.
}
\tag{4.3}
\]

This applies a completed newest-source result to the exact positive approximate-identity functional used in the current proof map.  Consequently

\[
\varepsilon^{-2}\mathbb E(\varepsilon-|Q_{a,c}-y|)_+
\le \pi\sqrt2
+
\varepsilon^{-2}\mathbb E\big[(\varepsilon-|Q_{a,c}-y|)_+\mathbf1_{\{Q_{a,c}<c\}}\big].
\tag{4.4}
\]

For exact rank-three indefinite forms, **the entire majority-sign one-sheet tent contribution is universally paid**.  The only remaining rank-three tent obstruction is the minority-sign two-sheet contribution.  This is a genuine reduction: it does not bound the latter term and therefore does not claim the full conjecture.

Exactly the same reasoning gives, for every Gaussian heat kernel \(\gamma_\eta\),

\[
\sup_y\int_{[c,\infty)}\gamma_\eta(s-y)\,d\mu_Q(s)\le C_+\le\pi\sqrt2,
\tag{4.5}
\]

but (4.2)-(4.4) are the more direct match to the current tent formulation.

## 5. Implication ledger

The logical distinctions required by this slot are:

1. **Absolute continuity.**  For any nonzero quadratic polynomial under an absolutely continuous source law, the critical set is a proper affine subspace; coarea away from that null set gives an absolutely continuous pushforward.  This does not imply an \(L^\infty\) bound.
2. **Essential boundedness.**  The ruled theorem proves a universal essential-density bound only for the stated one-sheet submeasure.  No continuity is needed for (3.2) or (4.2).
3. **Continuity.**  The smoothing used in the proof is an approximation argument and is not a proof that the original rough-output density is continuous.  Continuity remains a separate conclusion.  In particular, the universal tent bound cannot be inferred from continuity.

The familiar controls remain decisive: rank-one square output can be absolutely continuous with an unbounded density, and rank-two positive-definite product quadratics can have bounded but discontinuous output densities.  Therefore the three notions are not interchangeable outside the stronger rank-three product theorems.

## 6. What remains unpaid

This run does not solve QFORM.  It sharpens the rank-three indefinite reduction:

- majority-sign one-sheet side: universally bounded by \(\pi\sqrt2\), including rough cap-one laws and affine terms lying in the spectral range;
- minority-sign two-sheet side: still unpaid by the ruled/X-ray mechanism;
- definite exact-rank-three forms: not covered by the ruling;
- higher-rank matrices and dense additional couplings: require the global N3/hybrid structural step from the newest continuation.

The live correction `QFORM-TWOSHEET-XRAY-ONLY-FALSE` is respected: bounded two-dimensional projection densities alone do not control the two-sheet side.  Equation (4.4) therefore identifies a real obstruction rather than renaming the missing theorem.

## 7. Sources consumed

- Required newest Claude source: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, especially `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` in `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.
- Completed designated partner applied and independently checked: `yspennstate/math-open-problems@b4c8edd512776799decc9a16a40a3b37afba45b6`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B15/20260922T233101Z-fleet03-B15-qform-r21/REPORT.md`.
- Corrections consumed include the false arbitrary-joint coarea route, false positive conditional-density moment route, no-independence-after-rotation, and `QFORM-TWOSHEET-XRAY-ONLY-FALSE`.
