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

The opening update search was bounded to five minutes. It found no later result settling the full row, no newly identified arXiv version of these three manuscripts, and no specific refutation or named referee assessment. Search absence is not proof of absence. Queries and failed opens are recorded in LOG.md.

Opened in this session:

- [Repository history](https://raw.githubusercontent.com/openai/math/main/history.md), [planar README](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/README.md), and [issues](https://github.com/openai/math/issues): the retrieved history ends October 29 and lists no Anderson correction or withdrawal; the README contains no repair notice. The issues view supplies no mathematical assessment.
- [Lean scope 261](https://raw.githubusercontent.com/openai/math/main/lean/docs/261.md), [comparator configuration](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/PlanarAndersonSpectrum.json), and actual [solution](https://raw.githubusercontent.com/openai/math/main/lean/OAI/MathematicalPhysics/PlanarAnderson/Spectrum.lean): the exported theorem anderson_spectrum_ae, lines 623–628, constructs the self-adjoint operator and identifies its spectral interval. It has no pure-point conclusion. Later helpers assume an eigenbasis; they do not establish one. No Lean build or kernel replay was performed.
- Xujie Lai and Fan Yang, [*Localization Lengths for Two-Dimensional Random Band Matrices: Exponential Lower Bounds*, arXiv:2609.24426](https://arxiv.org/abs/2609.24426), and [v4 full text](https://arxiv.org/html/2609.24426v4), November 8, 2026. Their introduction calls the OpenAI result a claim and says its Theorem 10.1 also implies eigenvector localization. This is a relevant later comment, already known to the earlier workers; it is not proof certification or an extension to arbitrary iid laws. It should be read alongside the planar manuscript's explicit restriction of its asserted main conclusion.
- Linjun Li, Shihe Liu, Lingfu Zhang, [*Localization near the edge for the lattice Anderson-Bernoulli model on general dimension*, arXiv:2609.30209](https://arxiv.org/abs/2609.30209), v2 October 20, 2026. Opened the arXiv abstract page, which states bottom-edge localization for Bernoulli potentials in every d≥2. This does not settle the all-energy row; no broader theorem was inferred from it.

All three entry TeX files and theorem-bearing introductions linked above were reopened. For the new local check, also opened planar [resonant.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/resonant.tex), [hierarchy.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/hierarchy.tex), [vanishing.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/vanishing.tex), and [matrix.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/matrix.tex).

The earlier reports' further source inspections remain in their own records. Xu's exposition and external higher-dimensional Lean repository were not reopened in this session, so they supply no new evidence here. Repository URLs refer to mutable main, not a pinned snapshot. No SOLVED_ELSEWHERE.md was created because no full settlement was identified.

## Recommended replacement for “where it stands”

The full arbitrary-law statement remains unverified by this release. OpenAI's unrefereed *Pure-Point Spectrum for the Two-Dimensional Anderson Model at Every Positive Disorder* (September 23, 2026) claims pure-point spectrum at every fixed positive disorder for iid uniform potentials, but expressly does not assert exponential eigenfunction decay. Its linked Lean theorem proves the spectral interval only, and the bounded follow-up search found no later result settling the full row.

## Spot check

Round 3 checked the bounded-twist law change and retained-port stability. Independent re-derivation here confirms its quadratic density cost: the single-site chi-square divergence is exactly
\(s^2\int(\vartheta')^2/(1+s\vartheta')\,d\mu\), and the product cost is bounded when O(R²) coordinates each move by O(R⁻¹). Current acceptance rules confirm that retained tiles use ancestor labels only through validity; the geometric tail remains O(R⁻ᴷ) before the shift and O(R⁻ᴷ⁄²) after Cauchy–Schwarz.

The single extension is the suggested check of the signed datum in van:adjustment at EVERY complementary-pass root closure. The full local argument is in [PROOF.md](PROOF.md). After integrating acceptance uniforms, the hidden values at all start-of-pass roots have a product of cutoff-Cauchy kernels conditional on statuses, labels, and all other site values. The start response uses root-free calibrated references and deterministic strengths; hence the trace, its sign, and the frozen signed site datum are measurable without ANY of these draws. Independent thinning marks and revealing already closed roots preserve each remaining kernel.

A separate Bayes calculation checks the root factor directly, rather than treating recorded acceptance status as information-free. The audit also covers permanent roots, roots outside the pass, first-pass restorations, repeated closures, sign at zero, singular-matrix null sets, and the deterministic increment bound. No error was found in this local admissibility assertion; it does not establish the energy comparison or the preprint's proof.

Next check: the parent-alternative cap hier:cap, especially the conditional fields for shared corner labels, the envelope's independence from survival marks, and the comparison of true and branch boundary averages. These are still inputs, not consequences of the local result above.
