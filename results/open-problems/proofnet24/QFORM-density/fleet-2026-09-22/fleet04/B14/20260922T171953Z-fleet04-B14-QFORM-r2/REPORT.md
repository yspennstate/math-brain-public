# fleet04/B14 — cap-preserving compact completion and exact localization

**Programme:** \`QFORM-DENSITY-3EIG-20260922\`  
**Control revision:** \`2026-09-22.8\` (programme revision \`2026-09-22.5\`)  
**Startup control:** \`yspennstate/math-research-brain@4af7ebffc7f51910f4025d443dd4417addd04e1c\`  
**Run:** \`20260922T171953Z-fleet04-B14-QFORM-r2\`  
**Assignment:** translations and localization  
**Classification:** \`ESSENTIAL_STEP_APPLIED / SUPPORTING_LOCALIZATION_THEOREM / FULL_QFORM_OPEN\`  
**Execution:** \`WITHOUT_VERIFIED_BRAIN\`

## 1. Target and result

The full target remains open: for independent real coordinates with densities bounded by one and a symmetric matrix having at least three eigenvalues of absolute value at least one, prove a universal density bound for the quadratic form, or give a counterexample.

This report proves the exact constant-preserving localization statement needed to remove unbounded support as a separate obstruction.

### Theorem (cap-preserving compact completion)

Let \(\mu_i=f_i(x)\,dx\), \(1\le i\le n\), where \(0\le f_i\le1\) and \(\int f_i=1\). For every \(\varepsilon>0\), there are compactly supported probability densities \(g_i\) with \(0\le g_i\le1\) such that
\[
 d_{\rm TV}(f_i\,dx,g_i\,dx)<\varepsilon/n.
\]
Consequently, for every Borel map \(T:\mathbb R^n\to\mathbb R\),
\[
 d_{\rm TV}\!\left(T_\#\bigotimes_i f_i\,dx,\,
 T_\#\bigotimes_i g_i\,dx\right)<\varepsilon.
\]

In particular, the optimal interval-concentration constant for \(T(x)=x^TAx\) over all cap-one product densities is exactly the optimal constant over compactly supported cap-one product densities:
\[
 C_{\rm all}=C_{\rm compact}.
\]
No enlargement of the constant occurs.

Combined with the previously proved coordinatewise bathtub and finite-fragment approximation theorem, this gives
\[
 C_{\rm all}=C_{\rm compact}=C_{\rm finite\ interval\ unions},
\]
where the last class consists of products of indicators \(1_{E_i}\) with each \(E_i\) a bounded finite union of intervals of total length one. There is no uniform bound on support diameter, fragment count, fragment separation, or translations.

## 2. Proof

Fix one admissible density \(f\). Put
\[
 m_R=\int_{-R}^{R}f(x)\,dx,\qquad \delta_R=1-m_R.
\]
Choose any bounded measurable set \(F_R\subset\mathbb R\setminus[-R,R]\) of Lebesgue measure \(\delta_R\), for example an interval to the right of \(R+1\), and define
\[
 g_R(x)=f(x)1_{[-R,R]}(x)+1_{F_R}(x).
\]
The two summands have disjoint supports, hence \(0\le g_R\le1\), and
\[
 \int g_R=m_R+\delta_R=1.
\]
The support of \(g_R\) is bounded. Moreover
\[
 \|g_R-f\|_1
 =\int_{\mathbb R\setminus[-R,R]}|1_{F_R}-f|
 \le |F_R|+\int_{\mathbb R\setminus[-R,R]}f
 =2\delta_R.
\]
Therefore
\[
 d_{\rm TV}(g_R\,dx,f\,dx)\le\delta_R\longrightarrow0.
\]

Apply this construction independently to every coordinate. The standard product coupling inequality gives
\[
 d_{\rm TV}\!\left(\bigotimes_i\mu_i,\bigotimes_i\nu_i\right)
 \le\sum_i d_{\rm TV}(\mu_i,\nu_i).
\]
Total variation contracts under measurable pushforward, so the claimed estimate holds for every Borel \(T\), in particular every quadratic form.

Now suppose every compactly supported admissible product law satisfies
\[
 \Pr\{X^TAX\in I\}\le C|I|
\]
for every interval \(I\). Passing to the total-variation limit gives the same inequality for the original arbitrary product law. Conversely, the compact class is a subclass of the full class, so the optimal constants are equal.

The interval estimate implies absolute continuity and an essentially bounded density: the distribution function is \(C\)-Lipschitz, hence differentiable almost everywhere with derivative bounded by \(C\).

## 3. Translations, distant fragments, and what is not reduced

The filler interval \(F_R\) may be placed arbitrarily far away. The proof therefore uses no moment, barycenter, support radius, or tail-rate bound. Arbitrary translations of the original densities are harmless because the construction and total-variation estimate are translation covariant.

This does **not** prove a uniform bounded-diameter reduction. Such a statement is false under the live corrections: separated shell fibers can require arbitrarily large gaps even for a positive form. The theorem only says that each individual instance may be approximated by some bounded support, while the final proof constant must be uniform over all resulting diameters, translations, gaps, and fragment counts.

## 4. Partner theorem applied to an actual shell inequality

The completed partner result actually used is fleet01/B14:

- \`yspennstate/math-open-problems@2ad67886f215eff6f3daed247871a882a6f0314b\`;
- \`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B14/20260922T160955Z-fleet01-B14-qform-r13/REPORT.md\`.

For independent cap-one \(X_1,X_2,X_3\), arbitrary real edge offsets \(d_{12},d_{23},d_{31}\), and three square-root singularities, it proves
\[
 \mathbb E\prod_{\rm cyc}|X_i-X_j-d_{ij}|^{-1/2}\le125.
\]
No compatibility among the offsets is required.

Apply it to the concrete deterministic-outside shell interface
\[
 \Pr\{Q_A(X_S,z)\in I\mid z\}
 \le K|I|\,\mathbb E_S
 \prod_{\rm cyc}|X_i-X_j-d_{ij}(z)|^{-1/2}.
\]
For every compactly supported cap-one active triple, the partner theorem gives the actual inequality
\[
 \Pr\{Q_A(X_S,z)\in I\mid z\}\le125K|I|.
\]
Integrating the outside variables preserves it, and the compact-completion theorem then yields
\[
 \Pr\{X^TAX\in I\}\le125K|I|
\]
for the original arbitrary, possibly unbounded and multiply translated product densities, with no further localization loss.

If the three offsets are cycle-consistent, the sharper partner constant \(61+12\pi\) may replace \(125\), and the same cap-preserving transfer remains exact.

Thus localization consumes no additional power of \(|I|\) and introduces no tail or moment term. The first unpaid implication is exactly the matrix-geometric one: derive the displayed deterministic-outside shell/coarea inequality, with a universal \(K\), for every remaining three-large-eigenvalue matrix branch.

## 5. Continuity is separate

The argument proves preservation of the interval bound and hence an essentially bounded density. It does not transfer continuity from compact approximants.

Indeed, continuous probability densities \(p_m=1_{[0,1]}*\rho_m\) can satisfy \(\|p_m\|_\infty\le1\) and converge in \(L^1\) to \(1_{[0,1]}\), whose density has no continuous representative. Therefore total-variation localization alone cannot establish the owner's stronger continuity request.

Continuity would transfer under a common equicontinuity modulus (or another locally uniform scale-coherence estimate), but such a modulus is not proved here.

## 6. Corrections respected

This proof uses no pointwise van-der-Corput decay, post-rotation independence, bounded projection density as a substitute for a cone trace, bounded-diameter reduction, uniform fragment-count reduction, moment hypothesis, compact-support hypothesis in the final statement, or Monte Carlo extremality claim.

The full conjecture remains **OPEN**.
