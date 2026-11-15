# T010 verification, continued November 15, 2026

The earlier scope verdict survives independent rechecking: PARTIAL-CLAIMED. This records what is claimed, without certifying the preprint’s proof. The new local check is in [PROOF.md](PROOF.md) and summarized under “Spot check” below. REPORT.md uses the continuation task’s later-required verdict vocabulary.

## Our statement

For the Anderson model on ℓ²(Z²) with iid non-degenerate potential (not almost surely constant) of any strength λ>0, the spectrum is pure point with exponentially decaying eigenfunctions.

Almost surely is understood. The coupling is fixed before the probability-one assertion.

## Candidate 1: planar pure-point spectrum

OpenAI, *Pure-Point Spectrum for the Two-Dimensional Anderson Model at Every Positive Disorder*, September 23, 2026. Opened its [entry TeX](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/paper.tex), [introduction](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/introduction.tex), and [README](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/README.md). The author and date are those on the manuscript.

The actual model is nearest-neighbor adjacency plus the diagonal field v on ℓ²(Z²), with independent v_x uniform on [-h,h]. Its main theorem body, copied as TeX:

```tex
For each fixed $h>0$, almost surely $H_v$ has pure-point spectral type,
admits a complete orthonormal eigenbasis, and has spectrum
\[
 \sigma(H_v)=[-4-h,4+h].
\]
Its eigenvalues are dense in this interval. The probability-one event
in this statement is allowed to depend on $h$.
```

| Our words | Comparison |
| --- | --- |
| Anderson model on ℓ²(Z²) | Same infinite square lattice and nearest-neighbor hopping. A hopping sign change is unitarily equivalent on this bipartite lattice; a Laplacian normalization may shift the energy. |
| iid | Matches. |
| non-degenerate, not almost surely constant | Uniform laws are one subfamily. Bernoulli, general densities, singular laws, and unbounded laws are not covered. |
| any strength λ>0 | Matches every fixed positive strength within the uniform family; h=λ for base uniform law on [-1,1]. |
| spectrum is pure point | Matches pure-point spectral type throughout the spectrum for that family. It is not merely finite-volume or edge localization. |
| exponentially decaying eigenfunctions | Not asserted: the introduction’s scope paragraph expressly excludes this conclusion. |

A change of interval midpoint only adds a scalar operator and cannot change an arbitrary iid law into a uniform law. The spectral interval and dense eigenvalues are extra conclusions, but neither supplies the omitted decay property. Verdict for this candidate: PARTIAL-CLAIMED.

## Candidate 2: absolutely continuous spectrum in higher dimensions

OpenAI, *Absolutely Continuous Spectrum for Weak-Disorder Anderson Models in Dimensions at Least Three*, September 23, 2026. Opened its [entry TeX](https://raw.githubusercontent.com/openai/math/main/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/build/paper.tex) and [introduction](https://raw.githubusercontent.com/openai/math/main/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/build/01-introduction.tex). Its model has negative nearest-neighbor hopping on Z^d plus λ times iid uniform [-1,1] potentials. Main theorem body:

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

This is the same general operator class but a different dimension range, d>=3, a different spectral type, absolutely continuous, and a small-disorder interval conclusion. It claims no planar localization or arbitrary-law result. Verdict: NOT-THIS.

## Candidate 3: fixed-energy statistics on random regular graphs

OpenAI, *Fixed-energy universality for weak Anderson disorder on random regular graphs*, October 5, 2026. Opened its [entry TeX](https://raw.githubusercontent.com/openai/math/main/preprints/Fixed-energy-universality-for-weak-Anderson-disorder-on-random-regular-graphs-October-5-2026/build/paper.tex) and [introduction](https://raw.githubusercontent.com/openai/math/main/preprints/Fixed-energy-universality-for-weak-Anderson-disorder-on-random-regular-graphs-October-5-2026/build/sections/01-introduction.tex). Here H is adjacency plus iid uniform diagonal disorder on a uniformly random simple labelled d-regular graph with n vertices, independent of the disorder. The symbols ν and ρ denote the density-of-states measure and density of the corresponding infinite-tree model; Ξ_n^GOE is the normalized GOE bulk point process specified in the paper. Main theorem body:

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

The model is a finite random graph, the integer d is its degree, and the quantity is a microscopic eigenvalue-statistics limit. Disorder is sufficiently small and fixed while n grows. Finite matrices already have pure-point spectra; this theorem supplies no complete eigenbasis or exponential decay statement for an infinite operator on Z². Verdict: NOT-THIS.

## Follow-ups and source record

The bounded update search used the web search tool during the opening five minutes. Exact queries and findings are in LOG.md. No new solution, direct refutation, or named referee assessment was identified. This is a search result, not a proof that none exists. The earlier session’s wider search is recorded in its [VERIFY.md](~/codex_op_1114/briefs/AV_T010/VERIFY.md) and [LOG.md](~/codex_op_1114/briefs/AV_T010/LOG.md); those files were read before the new check.

Opened again in this session:

- [Repository history](https://raw.githubusercontent.com/openai/math/main/history.md): latest listed update remains October 29, 2026; no Anderson withdrawal or repair is listed. The planar README has no correction notice in the retrieved view.
- [Lean scope document 261](https://raw.githubusercontent.com/openai/math/main/lean/docs/261.md): explicitly identifies only the almost-sure spectral set as its target, excluding pure-point spectral type. This is not a Lean formalization of T010. No Lean build was run. The earlier worker inspected the mapped solution; that source inspection was not repeated here.
- Xujie Lai and Fan Yang, [*Localization Lengths for Two-Dimensional Random Band Matrices: Exponential Lower Bounds*, arXiv:2609.24426](https://arxiv.org/abs/2609.24426): the arXiv page still identifies v4, November 8, 2026, already known to the earlier worker. This concerns random band matrices, not a solution of T010. This session opened the abstract page, not its full text.
- Habib Ammari, Xin Fu, Wenjia Jing, Jiayu Qiu, Alexander Uhlmann, [*Anderson localisation in infinite and finite resonator crystals with long-range interactions*, arXiv:2611.03286](https://arxiv.org/abs/2611.03286), November 2, 2026: the abstract identifies random capacitance operators with long-range exponentially decaying interactions and edge localization. It does not settle the nearest-neighbor, all-energy statement here. This session opened the abstract page.

In addition to the three preprints’ entry and introduction sources linked above, the new spot check opened planar [hierarchy.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/hierarchy.tex), [vanishing.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/vanishing.tex), and [matrix.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/matrix.tex). No newly located arXiv version of a candidate or planar localization formalization was identified. All repository links refer to mutable main, not a pinned snapshot.

## Recommended replacement for “where it stands”

The broad statement remains unverified by this release. OpenAI’s unrefereed *Pure-Point Spectrum for the Two-Dimensional Anderson Model at Every Positive Disorder* (September 23, 2026) claims pure-point spectrum at every fixed positive disorder for iid uniform potentials, but expressly does not claim exponentially decaying eigenfunctions or cover general non-degenerate iid laws. The linked Lean formalization covers the spectral interval only, and the bounded follow-up search found no later result settling the full statement.

## Spot check

The earlier worker checked the analytic-trace lemma conditional on its good-event inputs. The single new check here is the bounded-twist probability estimate, `van:twist-probability`, needed to transfer the trace estimate through analytic closure despite recomputation of the hierarchy. Full details are in [PROOF.md](PROOF.md).

For T_s(x)=x+s theta(x), the exact single-site second moment is

\[
\int r_s^2\,d\mu
=1+s^2\int\frac{|\theta'|^2}{1+s\theta'}\,d\mu
\leq1+2s^2\int|\theta'|^2\,d\mu.
\]

Two substitutions independently give this identity. Product measure over O(R²) sites and |s|<=WC_0/R then give an L² density bound independent of R. Checking eligibility, allowance, likelihood, strengths, references, and restored gap roots shows that retained ports can change only through a large-ancestor validity failure. A union bound before and after the shift gives an exception at most u_R+D_W sqrt(u_R), with u_R=O(R^(-K_0)); the geometric-series power was derived two ways. This yields precisely the stated bounded-twist trace probability bound conditional on its input expectation a.

The checks include negative twists, changing box identities, rejected candidates becoming accepted, shared ancestors, null box boundaries, and the distinction between a bound for each twist and simultaneous invariance. No error was found in this local step under the stated definitions. The smallness of a, screening, and the construction of the good event remain unverified; consequently this supplies no correctness verdict for the paper or solution of T010.

The next check should test the measurability of the signed adaptive datum in `van:adjustment` under the hidden-root conditioning at every closure in the complementary thinning pass. That is the hypothesis needed to justify applying `hier:comparison` to make a small.
