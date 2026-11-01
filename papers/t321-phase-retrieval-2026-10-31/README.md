# Sampling Barriers for Real Gaussian Phase Retrieval

**Author:** Yitzchak Shmalo  
**Affiliation:** Einstein Institute of Mathematics, The Hebrew University of Jerusalem; Givat Ram, Jerusalem, Israel  
**Email:** yitzchak.shmalo@gmail.com  
**Manuscript date:** 31 October 2026  
**Research identifier:** T321

- [Read the complete paper](T321_Phase_Retrieval_Sampling.pdf)
- [Editable LaTeX source](T321_Phase_Retrieval_Sampling.tex)
- [Public repository](https://github.com/yspennstate/math-brain-public)
- [Designated archive](https://github.com/yspennstate/math-brain-public/tree/main/papers/t321-phase-retrieval-2026-10-31)

## Result and scope

The paper gives full proofs for the actual noiseless real Gaussian empirical phase-retrieval loss. For a deterministic unit signal, dimension `d >= 100`, and `m = 10^6 d` Gaussian measurements, a common data event has probability at least `1 - 10 exp(-d/2)`. On that event the paper establishes:

1. Explicit Gibbs concentration near the two minimizers at a stated inverse temperature of order `d/epsilon`.
2. An exponentially large raw-parameter-space Poincare constant and the corresponding logarithmic Sobolev lower bound.
3. Finite upper bounds for both functional-inequality constants through bounded convexification.
4. A necessary-temperature theorem for every Gibbs temperature attaining concentration probability at least `3/4`, in an explicitly very small tolerance range.
5. An exponential discrete MALA lower bound from a specified conditional-Gibbs `2`-warm initialization.
6. An arbitrary-accuracy total variation upper bound for ball-truncated MALA from every start in the ball, with controlled truncation error and zero invariant-distribution step-size bias.

All constants, restrictions, initialization choices, acceptance probabilities, and proofs are in the paper. The upper bound is deliberately loose and does not match the lower bound.

The bottleneck concerns the two signs in raw parameter space. It does **not** establish optimization hardness, hardness of sampling modulo sign, a lower bound for algorithms with global sign flips, a theorem for arbitrary initializations or all algorithms, a planted-network theorem, or an unadjusted Langevin guarantee. The lower-bound conditional-Gibbs start is not asserted to be efficiently generable.

## Novelty and review status

The sign-metastability mechanism is classical. The manuscript presents an explicit joint finite-sample concentration, functional-inequality, and discrete-sampling result for this model; it does not claim verified novelty, exclusive priority, or resolution of a previously open named published conjecture. Relevant comparisons include:

- [Raginsky, Rakhlin and Telgarsky](https://arxiv.org/html/1702.03849v3): nonconvex Langevin analysis and multiwell inverse-temperature bottlenecks.
- [Eldar and Mendelson](https://arxiv.org/abs/1211.0872): stable real phase retrieval with linearly many measurements.
- [Menz and Schlichting](https://arxiv.org/abs/1202.1510v4): functional inequalities and metastability.
- [Lytras, Makras and Sabanis, version 1, Section 8.2](https://arxiv.org/html/2608.06283v1): a distinct tamed unadjusted scheme for complex phase retrieval.

The literature comparison is limited and is not a systematic priority certification. The mathematical derivations, internal consistency reviews, writing, and publication preparation were AI-assisted as detailed in the declaration below. Neither those internal reviews nor the computational and layout checks constitute external peer review or formal verification.

## Acknowledgments and funding

The research presented in this paper was supported by the European Research Council (ERC) under the European Union's Horizon Europe research and innovation programme (grant agreement No. 101041711), by the Simons Foundation as part of the Collaboration on the Mathematical and Scientific Foundations of Deep Learning, by Heights Labs, by Convex Nexus Capital, by the Israel Science Foundation (grant number 2258/19), and by the Israel Science Foundation (ISF Grant 4101/25).

## Declaration of competing interest

The author holds equity in Heights Labs and in Convex Nexus Capital and has a management role at Convex Nexus Capital. These entities are included in the funding declaration above.

## Declaration of generative AI and AI-assisted technologies

OpenAI AI systems were used to develop the mathematical derivations, perform internal consistency and scope reviews, check relevant sources, and write and prepare this manuscript and its publication files. The author selected the problem and commissioned and directed the work; the author did not carry out the mathematics or the writing. Responsibility for submission or publication rests with the author. The AI-assisted internal reviews, compilation checks, and rendered-page inspections are not external peer review or formal verification.

## Data and code availability

This paper consists of self-contained theoretical proofs. It reports no empirical datasets or numerical experiments, and no separate empirical dataset is required. The editable LaTeX source and PDF are available through the manuscript links above. No separate verification-code package is claimed. Standard build instructions appear below.

## Provenance

The manuscript consolidates a finite-sample derivation and its internal mathematical scope review prepared in October 2026. It retains the stated data event, constants, necessary-temperature restriction, algorithm definitions, and truncation analysis. Its empirical deviation appendix expands the standard symmetrization argument. External mathematical inputs and comparisons are identified in the bibliography with primary-source links. No private operational records are part of this publication package.

## Build

A normal TeX Live or MiKTeX installation with `latexmk` and the packages named in the source is sufficient. From this directory, run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error T321_Phase_Retrieval_Sampling.tex
```

Alternatively, run `pdflatex` twice. No external data, shell escape, bibliography database, or network access is required. The source includes its bibliography. To render pages for layout inspection with Poppler:

```sh
mkdir -p rendered
pdftoppm -png -r 110 T321_Phase_Retrieval_Sampling.pdf rendered/page
```

The PDF is a complete mathematical manuscript, not a summary. The accompanying LaTeX is the editable source. Only the PDF, LaTeX source, and this README are intended as the manuscript publication package.
