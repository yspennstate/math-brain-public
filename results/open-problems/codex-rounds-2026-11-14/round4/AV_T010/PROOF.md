# Admissibility of the signed adjustment through the complementary pass

This note checks the measurability hypothesis used when applying hier:comparison to the signed datum in van:adjustment. It is a finite conditional-probability argument from the specified sampler and hierarchy. It does not establish transmission, energy comparison, screening, or localization.

The manuscript is OpenAI, *Pure-Point Spectrum for the Two-Dimensional Anderson Model at Every Positive Disorder*, September 23, 2026. Sources opened November 15, 2026:

- [resonant.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/resonant.tex): cell:sets, cell:calibrated-root, cell:epsilon, cell:hidden-root.
- [hierarchy.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/hierarchy.tex): eligibility, labels, acceptance, hidden roots, and admissible data.
- [vanishing.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/vanishing.tex): van:trace-data and van:adjustment.
- [matrix.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/matrix.tex): response definition and mat:energy-closure.

These are mutable main-branch sources. The argument concerns their specified finite sampling rules.

## 1. Statement

Fix the finite torus, energy, offset, and integers n<m. Complete the gap pass and call its response S'. Freeze the site datum

\[
 g(x)=f(x)+t\varphi(x),\qquad 0<t<1,
\]

where

\[
 \varphi(x)=-\sum_D 1_{\mathcal P_D}\operatorname{sgn}(H_D^0)
              \eta_D(x)(f(x)-f(c_D)),
\]

\[
 H_D^0=\sum_{\nu=1}^4\operatorname{tr}
       [F_{I_D,\nu}(F_{D,\nu}-S'F_{D,\nu}S'^*)],
 \qquad F_D=(f-f(c_D))/R.
\]

The cutoffs and f depend on geometry only, the events \(\mathcal P_D\) use selectors only, and the sign at zero is zero. No artificial probes occur in this adjustment step.

**Proposition.** Under the specified finite sampler, g is measurable in a field preserving the conditional hidden-root law at every complementary-pass closure. It uses no thinning marks of that pass and no root value still hidden at its start. Its site increments satisfy the deterministic admissibility bound.

## 2. Root kernels and retained information

Eligible tiles are pairwise disjoint. First fix selectors and all corner labels needed for eligible tiles and their ancestors. An exposed ancestor triple meeting an eligible tile coincides with one of that tile's own corner triples. Its central root belongs to none of these triples.

For an accepted tile U with root a, put \(J_U=V_U\setminus\{a\}\). The reference and strength are

\[
 A_U^{\rm int}=\operatorname{Adj}_{J_U}+\operatorname{diag}_{J_U}(v-E),
 \qquad c_U=E+p_U^\top(A_U^{\rm int})^{-1}p_U,
 \qquad \sigma_U=e^{-2\nu L_U}.
\]

Neither uses \(v_a\). The prescribed root kernel, as a Lebesgue density, is

\[
 k_U(y)=Z_{\sigma_U}^{-1}\chi(y-c_U)
       \frac{\sigma_U}{\pi((y-c_U)^2+\sigma_U^2)}.                 \tag{1}
\]

It integrates to one and its support lies inside the original potential interval. The nonroot sampler may have correlated coordinates and common shifts. Its joint density with the root nevertheless has the form
\(q_U(v_{U\setminus\{a\}})k_U(v_a)\), since the root is sampled last with (1). No other eligible root lies in \(J_U\).

Let \(\mathcal A\) be ALL active cell roots at the start of the complementary pass, including roots outside its region and permanent roots of levels at least m. Let \(\mathcal F_0\) retain the offset, selectors, needed box labels, branch acceptance indicators, independent geometry, and every true site value outside \(\mathcal A\). Retain no numerical acceptance uniform. Formally this definition is made on each of the finitely many strata with a fixed active-root set. True values restored in the gap pass are already recorded.

The conditional joint law is

\[
 \mathbb P\{(v_a)_{a\in\mathcal A}\in d\mathbf y\mid\mathcal F_0\}
       =\prod_{a\in\mathcal A} k_{U(a)}(y_a)\,dy_a.               \tag{2}
\]

Indeed, after selectors and labels have been fixed, eligible-tile laws factor on disjoint sites. Integrating a tile's acceptance uniform multiplies its true conditional law by \(p_l\mathcal L_U\) on acceptance and by \(1-p_l\mathcal L_U\) on rejection. These are local factors after allowance is determined from labels. Accepted status therefore gives precisely the branch law. Recording that tile's nonroot coordinates leaves (1). Rejected tiles and accepted roots already restored have their true values recorded. Normalization gives (2).

Ineligible indicators are identically zero. Shared ancestor labels can affect the recorded nonroot information but cannot couple the remaining roots: every exposed triple meeting an eligible tile is its own corner triple, never its root.

## 3. Independent Bayes derivation

Write \(\mu(dy)=dy/(2h)\) for the original root law and fix nonroot coordinates in an allowed eligible tile. Its likelihood factors as

\[
 \mathcal L_U(v)=\ell_U(v_{U\setminus\{a\}})(2h)k_U(v_a),
\]

where \(\ell_U\) is the nonroot marginal likelihood. For bounded Borel b,

\[
 \mathbb E[b(v_a)1_{\{A_U=1\}}\mid\text{nonroot data}]
       =p_l\ell_U\int b(y)k_U(y)\,dy.
\]

Taking b=1 and dividing gives (1) wherever the accepted conditional event has positive probability. Applying this calculation in each disjoint tile yields (2) separately from invoking the conditional-sampling proposition.

Accepted STATUS is permitted because it supplies the intended tilt. Retaining the numerical uniform instead would preserve the restriction \(t_U\le p_l\mathcal L_U(v)\) on y and generally truncate the kernel. The argument does not vary root values while holding numerical acceptance uniforms fixed.

## 4. Measurability of the full start response

Statuses and the prescribed gap pass determine the port set of S'. At each such root the real diagonal uses \(c_U\) and the absorber uses \(\sigma_U\), both known from \(\mathcal F_0\). Every other site uses its recorded true value. Thus the site matrix \(\mathscr L'\), port matrix Y', and

\[
 S'=I+2i(Y')^\top(\mathscr L')^{-1}Y'
\]

are \(\mathcal F_0\)-measurable where the inverse exists. A fixed definition on the measurable singular set preserves measurability. That set is null under the finite absolutely continuous law: a null vector of \(\mathscr L'\) vanishes at every absorber site and stays null after restoring the true diagonal values, whereas the true determinant is a nonzero polynomial in all diagonal variables.

The data F_D and their restrictions are geometric. Finite matrix products, adjoints and traces are measurable. Each trace is real, and sign with sign(0)=0 is Borel. Therefore \(H_D^0,\varphi,g\) are all \(\mathcal F_0\)-measurable.

One common field hides ALL start roots. This excludes a possible leak that a separate one-root argument could miss: a global sign formed from S' does not inspect another future hidden root.

## 5. Every later closure and interpolation

Adjoin all complementary-pass thinning marks to \(\mathcal F_0\), producing \(\mathcal F_0^*\). They are independent of the full branch construction and preserve (2). The datum g was fixed before these marks and does not use them.

At a fixed intermediate state let \(C\subset\mathcal A\) be the roots already closed. For each fixed interpolation parameter this set is determined by levels, geometry, statuses and independent marks, without inspecting the root values. Retain the restored true values:

\[
 \mathcal F_C=\mathcal F_0^*\vee\sigma(v_b:b\in C).
\]

Equation (2) gives, for every \(a\in\mathcal A\setminus C\),

\[
 \mathbb P(v_a\in dy\mid\mathcal F_C)=k_{U(a)}(y)\,dy.          \tag{3}
\]

The current matrix is measurable in this field: roots in C use recorded true values; other active roots retain their references. Branch choices are never recomputed. Both the current open response and the frozen g are measurable without v_a. Further conditioning on all other remaining roots gives the single-root conditioning of hier:hidden and still leaves (3) unchanged.

This applies after any number of closures, across levels, and to every retained subset at a fixed interpolation parameter. Different interpolation parameters need not form one monotone sample history; each parameter separately has the same conditional argument. Gap-pass restorations were in disjoint eligible tiles and were recorded before this pass.

Thus admissibility holds at every root comparison, rather than only at the initial state.

## 6. Deterministic increments

Put \(u_D(x)=\eta_D(x)(f(x)-f(c_D))\). On its support,
\(|f-f(c_D)|\le CR\), \(0\le\eta_D\le1\), and the cutoff has lattice Lipschitz constant at most C/R. For neighbors x,y,

\[
 |u_D(x)-u_D(y)|
 \le |f(x)-f(y)|+
       |\eta_D(x)-\eta_D(y)|\,|f(y)-f(c_D)|\le C.
\]

The same estimate applies to an edge exiting the support by using the zero cutoff outside. Distinct supports are separated at the stated scales. Multiplying each by a sign of modulus at most one therefore preserves a uniform edge bound. Summing along a shortest torus lattice path gives
\(|\varphi(x)-\varphi(y)|\le C d_{\rm graph}(x,y)\).

For the specified embedding, chord distance is bounded below by a fixed positive multiple of shortest Euclidean torus distance. Graph distance on the square lattice is at most \(\sqrt2\) times that distance. Consequently

\[
 |\varphi(x)-\varphi(y)|\le C'|f(x)-f(y)|,\qquad
 |g(x)-g(y)|\le(1+C')|f(x)-f(y)|.                              \tag{4}
\]

Squaring (4) supplies the required deterministic increment control, uniformly for 0<t<1 and for every choice of signs.

## 7. Attempts to break the result and limits

Both the product kernel and the separate Bayes calculation account for the information in acceptance statuses. The numerical acceptance uniforms remain unobserved. No conditioning on a potential-dependent good event is used.

The root enters neither its calibrated reference, its strength, nor any needed corner label. Other active references cannot use it because eligible tiles are disjoint. Thinning cannot create a previously rejected port. Permanent roots and roots outside the pass were included in the common hidden set. A zero trace has a measurable zero sign. Singular matrices require only a measurable null-set convention.

The adjustment step has no extra probes. For a general profile-dependent probe, omitting the real root diagonal would not alone hide its true value; the profile must also be constant on the hidden support. That separate plateau issue does not arise here. The signs must stay frozen: recalculating signs after closures changes the datum and cannot be substituted into the interpolation argument.

No failure was found in this admissibility step. This supplies one hypothesis of the energy comparison. The parent-alternative cap, adaptive envelope, transmission bounds, and screening remain unchecked. The result neither proves the manuscript nor extends its claim to general iid laws or exponential eigenfunction decay.
