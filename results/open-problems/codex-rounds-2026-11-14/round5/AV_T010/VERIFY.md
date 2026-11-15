# T010 verification, round 5 — November 15, 2026

The literature verdict remains PARTIAL-CLAIMED. The later continuation task requires REPORT.md to use PARTIAL; it describes the local cap audit, not a solution of the Anderson problem. All three theorem-bearing introductions and their entry TeX files were reopened in this session. The exact theorem transcriptions below agree with those sources and the earlier record.

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

The opening update search was limited to five minutes. Searches for the exact planar title with arXiv/error/refutation, openai/math with Anderson/error/localization, and two-dimensional all-disorder localization with November 2026 found no later full settlement or specific error report. This is a bounded search, not evidence that none exists. No SOLVED_ELSEWHERE.md is warranted by the sources found.

Opened in this session, in addition to the six entry/introduction sources above:

- [Repository history](https://raw.githubusercontent.com/openai/math/main/history.md) and [planar README](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/README.md): retrieved history still ends October 29, with no Anderson-specific repair or withdrawal listed; the README has no such notice. Opened the [issues view](https://github.com/openai/math/issues); it supplies no expert proof assessment. No named referee report or new arXiv version of a candidate was identified.
- [Lean scope 261](https://raw.githubusercontent.com/openai/math/main/lean/docs/261.md), [comparator mapping](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/PlanarAndersonSpectrum.json), and the mapped [solution](https://raw.githubusercontent.com/openai/math/main/lean/OAI/MathematicalPhysics/PlanarAnderson/Spectrum.lean), especially lines 623–628. The exported theorem constructs the operator, proves self-adjointness, and gives its spectral interval. It does not prove pure-point type. The following helper about pure-point type assumes a complete eigenbasis. No Lean build or kernel replay was run.
- Xujie Lai and Fan Yang, [*Localization Lengths for Two-Dimensional Random Band Matrices: Exponential Lower Bounds*, arXiv:2609.24426](https://arxiv.org/abs/2609.24426), and [v4 full text](https://arxiv.org/html/2609.24426v4), November 8, 2026. This is the same follow-up already recorded by earlier workers: its introduction discusses the OpenAI claims and an eigenvector-localization implication of the planar Theorem 10.1. It does not certify that manuscript, extend its single-site law, or supply a later proof of our full row. The candidate's stated main theorem and explicit scope disclaimer remain the basis for the comparison above.
- For the cap audit: planar [hierarchy.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/hierarchy.tex), [resonant.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/resonant.tex), [transmission.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/transmission.tex), [impedance.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/impedance.tex), and [matrix.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/matrix.tex). The relevant passages are hier:cap, hier:sampling, trans:envelope, trans:lower, imp:comparison, and mat:profile-properties. The planar source is attributed to OpenAI; the repository [license](https://raw.githubusercontent.com/openai/math/main/LICENSE) is Apache 2.0.

Earlier source inspections remain in the original, round-3, and round-4 records. Their other papers and expositions were not reopened here and provide no new evidence in this session. All repository URLs refer to mutable main; no immutable snapshot was obtained. Search snippets and secondary catalogs were not treated as proof endorsements.

## Recommended replacement for “where it stands”

The full arbitrary-law statement remains unverified by this release. OpenAI's unrefereed *Pure-Point Spectrum for the Two-Dimensional Anderson Model at Every Positive Disorder* (September 23, 2026) claims pure-point spectrum at every fixed positive disorder for iid uniform potentials, but expressly does not assert exponential eigenfunction decay. The linked Lean result proves the spectral interval only, and this bounded follow-up search found no later settlement of the full row.

## Spot check

The preceding round's measurability claim was independently re-derived by writing the joint accepted-root density after integrating acceptance uniforms. It factors into the prescribed kernels over disjoint eligible tiles; revealing already closed roots leaves the remaining factors unchanged. A separate calculation with product test functions gives the same conditional law. No defect was found in that local claim.

The single extension is the parent-alternative cap hier:cap. The detailed conditional argument is in [PROOF.md](PROOF.md). Shared ancestor labels impose only the already fixed parent corner boxes. The exterior response stays fixed when the parent's selector is toggled; its accepted alternative is part of the same current ensemble during either pass. Side-law averages of the boundary weight can be compared pointwise through the absorbed resolvent, without requiring independence of the correlated branch-side draws.

The envelope was re-derived with one-coordinate integration under the true product law. For z(x)=x-alpha-i(beta+tau a(x)), the profile inequality (a')²<=A a gives integral Im(1/z)<=2pi+A tau |I|. It follows that the expected replacement trace is at most (pi/h+A tau)|V|. Summing the replacement bounds over all 2^|V| internal subsets gives a single envelope independent of selectors, acceptance choices, and survival marks, with logarithmic cost O(L²).

The exact event that at least one of nine child survival marks succeeds has probability 1-(1-theta)^9<=9theta. Applying that event to the mark-independent envelope, then comparing to the accepted-parent alternative, gives the cap conditional on the manuscript's branch transmission lower bound trans:lower. The argument permits log K_l<=2 b_{l+1}^6+C b_{l+1}²; the leading term is the inverse parent incidence probability. This is a local conditional check, not certification of the preprint's proof.

The audit covers theta=0 and 1, coincident corner labels, multiple survivors, empty subsets, continuously adaptive references, vanishing source weight, singular null sets, second-pass geometry, and profile-dependent probes. A null-set explanation was corrected during drafting: the polynomial determinant is that of the Hermitian real part after eliminating the fixed boundary block, not the full profile-dependent matrix. The remaining transmission lower bound and its weighted-boundary/jitter inputs were not proved.

Next check: trans:lower, beginning with the terminal-field/jitter-success step that supplies a nonzero numerator uniformly in the passive exterior. It is now the explicit analytic assumption in the parent-cap reduction; screening and the full localization argument also remain unchecked.
