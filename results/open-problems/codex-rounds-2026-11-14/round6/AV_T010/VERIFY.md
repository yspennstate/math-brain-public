# T010 verification, round 6 — November 15, 2026

The literature verdict remains PARTIAL-CLAIMED. This session's REPORT.md uses the later continuation task's PARTIAL verdict for a local conditional lemma. The three exact theorem blocks below were retained from round 5 and checked against the actual theorem-bearing TeX sections opened in this session; their entry-file links are inherited navigation, not a claim that the entry files were reopened.

## Our statement

For the Anderson model on ℓ²(Z²) with iid non-degenerate potential (not almost surely constant) of any strength λ>0, the spectrum is pure point with exponentially decaying eigenfunctions.

Almost surely is understood. The coupling is fixed before the probability-one assertion.

## Candidate 1: planar pure-point spectrum

OpenAI, *Pure-Point Spectrum for the Two-Dimensional Anderson Model at Every Positive Disorder*, September 23, 2026. The earlier record links its [entry TeX](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/paper.tex), [introduction](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/introduction.tex), and [README](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/README.md). The author and date are those on the manuscript.

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

OpenAI, *Absolutely Continuous Spectrum for Weak-Disorder Anderson Models in Dimensions at Least Three*, September 23, 2026. The earlier record links its [entry TeX](https://raw.githubusercontent.com/openai/math/main/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/build/paper.tex) and [introduction](https://raw.githubusercontent.com/openai/math/main/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/build/01-introduction.tex). Its model has negative nearest-neighbor hopping on Z^d plus λ times iid uniform [-1,1] potentials. Main theorem body:

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

OpenAI, *Fixed-energy universality for weak Anderson disorder on random regular graphs*, October 5, 2026. The earlier record links its [entry TeX](https://raw.githubusercontent.com/openai/math/main/preprints/Fixed-energy-universality-for-weak-Anderson-disorder-on-random-regular-graphs-October-5-2026/build/paper.tex) and [introduction](https://raw.githubusercontent.com/openai/math/main/preprints/Fixed-energy-universality-for-weak-Anderson-disorder-on-random-regular-graphs-October-5-2026/build/sections/01-introduction.tex). Here H is adjacency plus iid uniform diagonal disorder on a uniformly random simple labelled d-regular graph with n vertices, independent of the disorder. The symbols ν and ρ denote the density-of-states measure and density of the corresponding infinite-tree model; Ξ_n^GOE is the normalized GOE bulk point process specified in the paper. Main theorem body:

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

## Follow-ups and opened sources

The initial search lasted at most five minutes. Web queries were the exact planar title with 2026; openai/math Anderson error localization; Anderson localization two dimensions all disorder 2026 proof; the exact title with correction/refutation/November 2026; and two-dimensional Anderson proof November 2026. No later full settlement, specific refutation, or named referee assessment was identified. This is a bounded negative search. No SOLVED_ELSEWHERE.md is justified by it.

Opened in this session:

- The three theorem-bearing introductions linked above, including planar lines 1–31 and 85–86, higher-dimensional lines 10–53, and random-graph lines 76–127. The planar theorem still has the same uniform-law, pure-point scope and expressly omits exponential decay. These exact theorem bodies were manually compared with the source views; no changed statement was found.
- All three README files: [planar](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/README.md), [higher-dimensional](https://raw.githubusercontent.com/openai/math/main/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/README.md), and [random graphs](https://raw.githubusercontent.com/openai/math/main/preprints/Fixed-energy-universality-for-weak-Anderson-disorder-on-random-regular-graphs-October-5-2026/README.md). They give the author OpenAI and dates September 23, September 23, and October 5, 2026. No new planar repair or withdrawal notice appears in its README.
- [Repository history](https://raw.githubusercontent.com/openai/math/main/history.md): still ends October 29, with no listed Anderson withdrawal or repair. This is not a guarantee that no error exists.
- [Lean scope document](https://raw.githubusercontent.com/openai/math/main/lean/docs/261.md) and the actual [mapped solution](https://raw.githubusercontent.com/openai/math/main/lean/OAI/MathematicalPhysics/PlanarAnderson/Spectrum.lean), especially lines 623–630. The exported anderson_spectrum_ae statement constructs a self-adjoint Anderson operator and identifies its spectral interval. The subsequent pure-point helper assumes a complete orthonormal eigenbasis; it does not construct one for this random operator. No Lean build was run.
- Xujie Lai and Fan Yang, [Localization Lengths for Two-Dimensional Random Band Matrices: Exponential Lower Bounds, arXiv:2609.24426](https://arxiv.org/abs/2609.24426). The abstract page remains v4 dated November 8, 2026 and concerns Gaussian random band matrices. It provides no proof of the full iid-potential lattice statement. Its full text was read by earlier workers; only its arXiv abstract/version record was reopened here.
- [transmission.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/transmission.tex), especially lines 195–532, and [resonant.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/resonant.tex), including its geometry, sampler, profile statement and residual calculation. These are the sources for the new local lemma.
- The repository [Apache 2.0 license](https://raw.githubusercontent.com/openai/math/main/LICENSE), under which the mathematical theorem excerpts are reproduced with attribution.

All repository links are mutable main-branch sources; no immutable snapshot was acquired. The earlier workers' additional references and GitHub issue views were not reopened and supply no new evidence here. Secondary search hits were not treated as endorsements. Shell downloads of six sections failed at DNS resolution; all successful source inspections used the web tool.

## Recommended replacement for “where it stands”

The full arbitrary-law statement remains unverified by this release. OpenAI's unrefereed Pure-Point Spectrum for the Two-Dimensional Anderson Model at Every Positive Disorder (September 23, 2026) claims pure-point spectrum at every fixed positive disorder for iid uniform potentials, but expressly does not assert exponential eigenfunction decay. The linked Lean result proves the spectral interval only, and this bounded follow-up search found no later settlement of the full row.

## Spot check

The preceding round's scalar integration, mark-independent envelope and conditional parent cap survive independent re-derivation; the transmission lower bound remains an explicit assumption. In particular, the envelope costs exp(O(L²)), the fresh-mark event has probability at most 9 theta, and the inverse parent incidence costs exp(2 b_parent^6). LOG.md records the derivation and conditions.

The single extension checks trans:jitter-success on each regular zero-jitter boundary/common-shift datum, assuming the stated branch profile estimates. PROOF.md gives all steps: normalize the source without bounding the exterior norm; find a source component near the boundary; control the terminal field by separating the direct profile from its reflected term; construct a logarithmic path of polynomially large inverse entries; and expose fresh shell jitters successively.

More precisely, for s transfers and one terminal update, the conditional probability is at least 4^(-(s+1)) of a normalized numerator at least a (w/9) (w delta/9)^s sqrt(rho). Here a and delta have polynomial lower bounds, w=L^(-D3), and s=O(log L). This gives the manuscript's exp(-C(log L)²) numerator threshold and exp(-C(1+log L)) success probability, uniformly after conditioning on nonpath jitters. The proof covers complex coefficients, zero source weight, an empty transfer path, destructive later updates, and all simultaneous jitter perturbations.

No failure was found in this conditional local step. The weighted good-boundary estimate, regular-common-shift probability, inverse-producing profile lemma, restoration of absorption and root, and the rest of the manuscript remain outside this verification. The next worker should audit imp:weighted, particularly the uniform fraction of boundary transmission weight carried by a polynomially bounded projected inverse, then recheck the regular-r integration before using the local numerator result in trans:lower.
