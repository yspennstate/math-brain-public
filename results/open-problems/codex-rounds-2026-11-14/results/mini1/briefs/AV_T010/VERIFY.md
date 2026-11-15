# T010: localization of the two-dimensional Anderson model at every disorder

Checked November 14, 2026. Verdict: **PARTIAL-CLAIMED**. The relevant preprint claims pure-point spectral type for the uniform single-site law at every fixed positive disorder. It does not claim our full statement, which also requires arbitrary iid non-degenerate laws and exponentially decaying eigenfunctions. This is a comparison of claims, not a judgment that the proof is correct.

## Our statement

“For the Anderson model on ℓ²(Z²) with iid non-degenerate potential (not almost surely constant) of any strength λ > 0, the spectrum is pure point with exponentially decaying eigenfunctions.”

The almost-sure qualification is understood. As usual, the coupling is fixed before the probability-one assertion; our wording does not explicitly require a common event for all couplings.

## 1. Pure-point candidate

**OpenAI, *Pure-Point Spectrum for the Two-Dimensional Anderson Model at Every Positive Disorder*, September 23, 2026.** Opened the actual [entry TeX](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/paper.tex), [introduction](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/introduction.tex), and [README](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/README.md). Author and date are given in the TeX and README.

Its model is

\[
(H_vu)(x)=\sum_{|y-x|_1=1}u(y)+v_xu(x),\qquad u\in\ell^2(\mathbb Z^2),
\]

where the independent variables \(v_x\) are each uniform on \([-h,h]\), equivalently \(v_x=h\omega_x\) with \(\omega_x\) uniform on \([-1,1]\).

Theorem 1.1, copied exactly as TeX from the introduction, including its displayed formula:

```tex
For each fixed $h>0$, almost surely $H_v$ has pure-point spectral type,
admits a complete orthonormal eigenbasis, and has spectrum
\[
 \sigma(H_v)=[-4-h,4+h].
\]
Its eigenvalues are dense in this interval. The probability-one event
in this statement is allowed to depend on $h$.
```

The introductory scope paragraph expressly excludes exponential eigenfunction decay and dynamical localization. Thus the absence of decay from the theorem is deliberate, rather than merely a shortened abstract.

| Words in our statement | What this theorem claims | Coverage |
| --- | --- | --- |
| Anderson model on ℓ²(Z²) | Infinite square lattice, nearest-neighbor hopping and diagonal potential | Same model and dimension under the usual nearest-neighbor convention. A hopping sign change is unitarily equivalent on the bipartite lattice; a Laplacian convention can add a constant energy shift. |
| iid | Independent identically uniform site variables | Matches independence and identical distribution. |
| non-degenerate, not almost surely constant | Uniform on an interval of positive width | A special case. It does not cover Bernoulli, other discrete laws, nonuniform densities, singular continuous laws, or general unbounded laws. |
| any strength λ > 0 | Every fixed h > 0 | Matches arbitrary positive strength within that uniform-law family, including arbitrarily weak disorder. Set h = λ for base law uniform on [-1,1]. |
| the spectrum is pure point | Pure-point spectral type and a complete eigenbasis throughout the spectrum | Matches this quantity for the stated law; it is an infinite-volume claim, not only a finite-size limit. Dense eigenvalues do not mean every spectral point is an eigenvalue. |
| with exponentially decaying eigenfunctions | No such conclusion in Theorem 1.1; introduction expressly disclaims asserting it | Not covered by the stated main result. |

Any non-degenerate uniform interval reduces to a centered interval by subtracting its midpoint. This change does not turn a general iid distribution into a uniform one. The paper also states a fixed-real-energy exponential fractional-moment estimate in Section 10, but that is a separate intermediate claim, not an asserted exponential-eigenfunction conclusion. A later comment about possible implications is recorded below.

Candidate verdict: **PARTIAL-CLAIMED**.

## 2. Absolutely-continuous candidate

**OpenAI, *Absolutely Continuous Spectrum for Weak-Disorder Anderson Models in Dimensions at Least Three*, September 23, 2026.** Opened its [entry TeX](https://raw.githubusercontent.com/openai/math/main/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/build/paper.tex), [introduction](https://raw.githubusercontent.com/openai/math/main/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/build/01-introduction.tex), and [README](https://raw.githubusercontent.com/openai/math/main/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/README.md).

Here \(V_x\) are iid uniform on \([-1,1]\), and

\[
(H_{\lambda,\omega}\psi)(x)
=-\sum_{j=1}^d\bigl(\psi(x+\mathbf e_j)+\psi(x-\mathbf e_j)\bigr)
+\lambda V_x(\omega)\psi(x).
\]

Theorem 1.1, copied exactly as TeX:

```tex
There is a fixed sufficiently small number $e_2\in(0,1/100)$ such that,
for every fixed integer $d\ge3$, there is a number $\lambda_d>0$
with the following property. Set
\begin{equation}\label{eq:energy-windows}
 I_d=
 \begin{cases}
   (-6+e_2/2,-6+e_2),&d=3,\\
   -2d+(1/200,1/100),&d\ge4.
 \end{cases}
\end{equation}
Then
for every fixed $0<\lambda<\lambda_d$, almost surely
\[
 I_d\subset\sigma(H_{\lambda,\omega}),\qquad
 \chi_{I_d}(H_{\lambda,\omega})\ell^2(\ZZ^d)
       \subset\mathcal H_{\mathrm{ac}}(H_{\lambda,\omega}).
\]
In particular, the spectral restriction to $I_d$ is purely absolutely
continuous and $\chi_{I_d}(H_{\lambda,\omega})\ne0$.
For $d\ge4$, one may take $\lambda_d=\sqrt3\,2^{-n_*(d)}$, where the finite-matrix
specification of $n_*(d)$ is given in Definition~\ref{def:threshold}.
For $d=3$, the proof supplies an existential positive threshold.
```

Comparison: nearest-neighbor lattice Anderson operator and iid diagonal disorder are shared, but the theorem excludes dimension two, assumes a uniform law, restricts the coupling to a sufficiently small interval, and treats only \(I_d\), rather than the full spectrum. Its quantity is purely absolutely continuous spectral type with nonzero weight, rather than pure-point type or exponential eigenfunction decay. For fixed dimension and coupling it asserts an actual infinite-volume statement; it supplies no effective numerical disorder threshold. It gives neither a special case of our planar conclusion nor a contradiction to it, because the dimension differs.

Candidate verdict: **NOT-THIS**.

## 3. Random-regular-graph candidate

**OpenAI, *Fixed-energy universality for weak Anderson disorder on random regular graphs*, October 5, 2026.** Opened its [entry TeX](https://raw.githubusercontent.com/openai/math/main/preprints/Fixed-energy-universality-for-weak-Anderson-disorder-on-random-regular-graphs-October-5-2026/build/paper.tex), [introduction](https://raw.githubusercontent.com/openai/math/main/preprints/Fixed-energy-universality-for-weak-Anderson-disorder-on-random-regular-graphs-October-5-2026/build/sections/01-introduction.tex), and [README](https://raw.githubusercontent.com/openai/math/main/preprints/Fixed-energy-universality-for-weak-Anderson-disorder-on-random-regular-graphs-October-5-2026/README.md).

Its model is \(H_{n,d,w}=A_{n,d}+w\operatorname{diag}(\omega_1,\ldots,\omega_n)\), where \(A_{n,d}\) is the ordinary adjacency matrix of a uniformly random simple labelled d-regular graph and the \(\omega_i\) are iid uniform on \([-1,1]\), independent of the graph. The measure \(\nu_{d,w}\) is the expected root spectral measure of the corresponding infinite d-regular tree. If \(\mu_i\) are eigenvalues of normalized GOE (off-diagonal variance \(1/n\), diagonal variance \(2/n\)), the reference point process is \(\Xi_n^{\mathrm{GOE}}=\sum_i\delta_{(n/\pi)\mu_i}\).

Theorem 1.1 [Fixed-energy universality], copied exactly as TeX:

```tex
For every $d\ge3$ and every $0<\kappa<2\sqrt{d-1}$, there is
$w_0=w_0(d,\kappa)>0$ with the following property.  For each fixed
$0<w<w_0$, the restriction of $\nu_{d,w}$ to an open neighborhood of
\[
 I_{d,\kappa}=[-2\sqrt{d-1}+\kappa,\,2\sqrt{d-1}-\kappa]
\]
has a continuous density $\rho_{d,w}$, strictly positive on
$I_{d,\kappa}$.  For every fixed $E\in I_{d,\kappa}$, set
\[
 \Xi_{n,E}=\sum_{i=1}^n
       \delta_{n\rho_{d,w}(E)(\lambda_i-E)}.
\]
Then, for every nonnegative $f\in C_c(\RR)$,
\begin{equation}\label{eq:main-laplace}
 \left|
 \EE\exp\left(-\int f\,d\Xi_{n,E}\right)
 -\EE\exp\left(-\int f\,d\Xi_n^{\GOE}\right)
 \right|\longrightarrow0
\end{equation}
as $n\to\infty$ through all sizes $n>d$ with $nd$ even.
```

Comparison: this is a sequence of finite random graphs, not the fixed infinite lattice Z². Here d is the graph degree, not Euclidean dimension; degree four does not specialize the graph law to the square lattice. The disorder is uniform and sufficiently weak, fixed before the graph grows. The quantity is the limiting microscopic eigenvalue point-process law near fixed bulk energy after unfolding, not pure-point spectral type or eigenfunction decay on an infinite lattice. Finite matrices having eigenbases says nothing by itself about our infinite-volume problem.

Candidate verdict: **NOT-THIS**.

## Follow-ups and formalization

The searches and the following openings were made November 14, 2026. No arXiv version of the three candidate manuscripts, specific refutation, error report, or named referee certification was found in these searches. That is a bounded search result, not a claim of exhaustive absence.

- Opened the repository [history](https://raw.githubusercontent.com/openai/math/main/history.md), with entries through October 29, and all three READMEs linked above. None records an Anderson-specific correction or withdrawal in the versions retrieved. The [issues page](https://github.com/openai/math/issues) displays zero open issues and no matching results; it supplies no mathematical assessment.
- Opened the repository [Lean README](https://raw.githubusercontent.com/openai/math/main/lean/README.md), [formalization index](https://raw.githubusercontent.com/openai/math/main/lean/formalization.yaml), [scope document 261](https://raw.githubusercontent.com/openai/math/main/lean/docs/261.md), and [PlanarAndersonSpectrum comparator challenge](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/PlanarAndersonSpectrum.lean). The scope covers existence of the bounded self-adjoint uniform-law planar operator and the almost-sure spectral interval [-4-h,4+h]. It explicitly excludes pure-point spectral type. The challenge statement has exactly that limited conclusion; its `sorry` is in the challenge template, not evidence by itself of a missing solution. The index has no Anderson entry or match for the random-graph title. Attempted `lean/docs/219.md`, which returned 404; no formalization of the random-graph theorem was located.
- Followed the [comparator configuration](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/PlanarAndersonSpectrum.json) to the actual [solution source](https://raw.githubusercontent.com/openai/math/main/lean/OAI/MathematicalPhysics/PlanarAnderson/Spectrum.lean). Its exported `anderson_spectrum_ae` (lines 623–628) has only the spectral-set conclusion. The source defines a stronger `MainStatement` involving pure-point type, but does not prove that statement. The helpers at the end assume a complete eigenbasis. This independently agrees with the stated formalization scope; no local kernel check was performed.
- Opened **Yao Xu**, [*anderson-ac-lean4*](https://github.com/cadamcat/anderson-ac-lean4). Its README claims a Lean proof of the second candidate’s AC result and gives a Mathlib-only challenge and reported axiom checks. This is an external formalization claim about dimensions at least three; no local build or kernel replay was performed, and it does not formalize planar pure-point type. Also opened Xu’s *Extended states in the Anderson model*, version 1.0.2 (November 2026), a PDF reached from [MathDB’s problem page](https://mathdb.com/p/389103/extended-states-in-the-anderson-model-in-dimension-3) via a search-result link. It explains the AC proof and formalization and distinguishes the unrefereed manuscript from reported kernel checks. Its broad statement that planar all-disorder localization remains open is not an analysis or refutation of the separate planar preprint.
- Opened **Xujie Lai and Fan Yang**, [*Localization Lengths for Two-Dimensional Random Band Matrices: Exponential Lower Bounds*, arXiv:2609.24426](https://arxiv.org/abs/2609.24426), and its [v4 full text](https://arxiv.org/html/2609.24426v4), revised November 8, 2026. In the introduction they describe both OpenAI results as claims. They also say the planar paper’s Theorem 10.1 implies eigenvector localization, while observing that no quantitative weak-disorder upper bound on localization length is given. This is a pertinent later mathematical comment, not a referee report or a verification of the full proof. The planar manuscript itself still expressly limits its asserted conclusion; the broader iid-law requirement remains uncovered regardless of this comment.

Queries included each exact distinctive title with arXiv, review, error, gap, refutation, or Lean; exact-title searches restricted to arxiv.org; `site:github.com/openai/math/issues Anderson`; and Anderson/OpenAI with error or refutation. Secondary catalogs and explanatory pages appeared in search results but were not used to certify a theorem. All citations to papers above refer to sources actually opened; historical references in the supplied old note have not been independently rechecked here.

## Recommended new “where it stands” text

The full statement for arbitrary iid non-degenerate potentials, including exponential eigenfunction decay at every positive disorder, remains unverified by this release. OpenAI’s unrefereed *Pure-Point Spectrum for the Two-Dimensional Anderson Model at Every Positive Disorder* (September 23, 2026) claims pure-point spectrum throughout the spectrum for iid uniform potentials at each fixed positive disorder, but expressly does not assert exponential eigenfunction decay. The accompanying Lean formalization covers the spectral interval only, so our row should record a partial claim rather than a settled problem.

## Spot check

Selected the analytic-trace lemma `van:analytic-bounds` in Section 9 of the planar paper, the key analytic step in the dimension-specific proposition `van:zero`. Sources opened: [vanishing.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/vanishing.tex), especially lines 472–610 and 700–758, and its weak-integral input in [matrix.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/matrix.tex), lines 283–440. This is a local check conditional on the earlier good-event estimates, not an audit of the whole argument.

The lemma asserts a positive lower bound on \(|\mathfrak h(0)|\) and a dimension-independent bound on \(\int|H(z)|^p\,d\gamma(z)\) for \(0<p<1/2\), on the constructed good event. In this section d denotes limiting affine energy, not the lattice dimension. The scattering matrix is partitioned as \(S=\left(\begin{smallmatrix}A&T\\T^\top&B\end{smallmatrix}\right)\); \(K=\|T\|_{\mathrm{HS}}^2\leq\kappa\). Closing probes gives \(S_z=A+Tz(1-zB)^{-1}T^\top\).

1. **Determinant and inverse estimates.** Unitarity gives \(AA^*=1-TT^*\). If the eigenvalues of \(TT^*\) are \(\delta_j\), then \(\delta_j\geq0\) and \(\sum_j\delta_j=K<1\). Consequently \(A\) is invertible, \(|\det A|^2=\prod_j(1-\delta_j)\geq1-K\), and \(\|A^{-1}\|\leq(1-K)^{-1/2}\). Independently multiplying the identity for \(AA^*\) by \(A^{-1}\) gives \(A^{-1}-A^*=A^{-1}TT^*\), hence the claimed trace-norm error \(K/\sqrt{1-K}\). These estimates do not introduce a factor equal to the number of ports.

2. **Sign of the central trace.** For one real diagonal component F, replacing the internal inverse block by the adjoint gives

   \[
   \sum_{i\in I}F_i^2-\sum_{i,j\in I}F_iF_j|A_{ij}|^2
   =\frac12\sum_{i,j\in I}|A_{ij}|^2(F_i-F_j)^2
   +\sum_{i\in I}F_i^2\left(1-\sum_{j\in I}|A_{ij}|^2\right).
   \]

   Re-expansion verifies the equality, using symmetry of A for the two square terms. The last term is nonnegative because A is a contraction. Summing components, the good-event jump bound supplies the positive contribution \(c_1d/2\). Boundedness of F on I controls the inverse-replacement error by \(CK\). The cross block costs \(C\delta_A(\delta_A+K)\), where \(\delta_A=\|A_{IJ}\|_{\mathrm{HS}}+\sum_\nu\|A_{IJ}F_\nu|_J\|_{\mathrm{HS}}\). Thus the lower-bound argument works if the earlier good-event estimate indeed makes this cross block sufficiently small in the stated order of constants.

3. **Analyticity and boundary values.** The adjugate formula for \(\mathfrak h\) removes the nonanalytic adjoint. The transfer matrix is rational and analytic in the disk since B is contractive. Its unitary boundary values away from finitely many points preclude a genuine rational boundary pole. On the circle, \(\operatorname{adj}(S_z)=\det(S_z)S_z^*\), giving \(|\mathfrak h|=|H|\). This justifies using the analytic function rather than treating the original adjoint expression as analytic.

4. **Moment bound and its exponent.** For a tail bound \(\gamma\{X>t\}\leq\min(1,a/t)\), direct integration gives \(\int X^q\,d\gamma\leq a^q/(1-q)\) for \(0<q<1\). The linear terms are trace resolvents with bounded trace-norm coefficients; the quadratic term is bounded by a product of two Hilbert–Schmidt resolvents. Cauchy–Schwarz requires moment \(2p<1\) for each factor, exactly explaining the lemma’s restriction \(p<1/2\). In the supporting weak-resolvent estimate, the positive matrix-valued measure has total mass the identity; partitionwise Cauchy–Schwarz bounds the variation of \(UMV\) by \(\|U\|_{\mathrm{HS}}\|V\|_{\mathrm{HS}}\). This is the relevant place to check that a hidden port-count factor has not entered; the displayed estimate has none.

The subsequent submean comparison is also consistent at this local level: for \(0<p'<p\), it gives a lower expected boundary moment at least \(c_2^{p'}/2\) on an event of probability at least one half, against the proposed upper bound below \(c_2^{p'}/4\). The exponent in the Hölder upper bound is \(1-p'/p>0\), and the stated order first fixes the Cauchy tail cutoff, then the amplitude cutoff, then the spatial scales.

No algebraic or exponent error was found in this lemma under its stated inputs. This leaves the construction and probability of the good event, screening, thinning, and invariance of hierarchy statuses under potential changes unchecked; those are essential to `van:zero` and hence to the main claim. The spot check supplies no correctness verdict on the preprint and does not change `PARTIAL-CLAIMED`.
