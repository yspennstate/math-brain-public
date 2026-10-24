# P0211 paper and research record

Revised 12 October 2026. Author: Yitzchak Shmalo.

## Published paper

The current paper is **Sharp relaxation, cutoff, and graph diffusion for a linear-polymer chain**. It is 45 pages and contains 28 printed references.

- Public repository: https://github.com/yspennstate/linear-polymer-relaxation
- Publication commit: https://github.com/yspennstate/linear-polymer-relaxation/commit/da3fe283fb3b70aaa0b3ff62d845b70e04d12ebf
- PDF: https://github.com/yspennstate/linear-polymer-relaxation/blob/main/paper/main.pdf

This directory contains the complete published source, PDF, programs, and recorded results, together with private review records. The public repository contains the scientific package. Its PDF has a clickable repository link on the first page and in the paper. The author's affiliation, funding, competing-interest declaration, and AI acknowledgment are retained.

The revised PDF was emailed to the author's verified Gmail account on 12 October 2026. Gmail message `1a12dd85e3526776` was read back with the SENT label and a 657,778-byte PDF attachment. The PDF SHA-256 is `acc010e15b52c018abf53566ebd150c86fb5e044c754565d7a920754209f2f24`.

## Results established in the revision

The model has total mass n, rate 2/n for each unordered pair of polymer instances to merge, and fragmentation rate beta for each internal link.

1. The full polymer gap equals the count-chain gap. Granovsky and Erlihson announced this equality; the paper provides an independent proof through the harmonic sectors and does not claim the equality as a new discovery.
2. The uniform bound `(beta + sqrt(beta) + 1/n)/6 <= gamma_M <= 4(beta + sqrt(beta) + 1/n)` is strengthened to `sqrt(beta^2 + 4 beta) - 5/n <= gamma_M <= sqrt(beta^2 + 4 beta) + 4/n`. For `beta = b/n`, the relaxation time is asymptotic to `sqrt(n)/(2 sqrt(b))`.
3. At `beta = b/n^2`, a rigorously defined infinite birth-death operator gives the crossover function rho(b), with `|n gamma_M - rho(b)| <= b/n`. A second function sigma(b) describes the degree-one spatial reaction mode. Both have finite-dimensional approximation bounds and small- and large-b asymptotics.
4. For fixed b > 0 and `beta = b/n`, the count chain has total-variation cutoff at `sqrt(n) log(n)/(8 sqrt(b))`, with window at most order sqrt(n). The same statement holds for the polymer chain from one polymer and from all monomers. Separation from those states has twice this leading time.
5. From arbitrary polymer configurations, the total-variation upper bound is `C_b sqrt(n) ((log n)^2 + log(1/epsilon))`. The endpoint lower bound applies to worst-case mixing. The extra logarithm in the general upper bound is not removed.
6. With exclusion diffusion on a connected weighted graph, the exact gap is `min(gamma_M, eta_1 + D lambda_G)`. The paper gives sharp reaction estimates, cycle and torus consequences, a joint critical limit, and bounds for reversible inhomogeneous reaction conductances.
7. Conservative directed permutation motion has separate exact formulas for the asymptotic spectral rate and the best prefactor-one L2 rate. A stationary circulation on a four-state cycle in the original polymer graph strictly increases the least nonzero real part of the spectrum at every fixed n >= 4 and beta > 0, for every allowed nonzero circulation. No uniform-in-n acceleration factor is proved.
8. Shared growing multipliers `ij` and `i+j` on forward and reverse reactions preserve the original equilibrium and satisfy proved spectral bounds. Their sharp relaxation orders remain open. The distinct classical Ewens multiplicative-kernel model and its known spectrum are credited to the literature.

## What remains open

- The worst-case polymer total-variation cutoff, its profile, and a matching sharp mixing upper bound.
- A full gap theory for unrestricted nonconstant coagulation and fragmentation kernels; the shared product/additive bounds do not determine the small-beta order.
- General spatial coagulation-fragmentation equations, local mass-dependent spatial reactions, and continuum hydrodynamic limits. The graph model here retains global count-dependent reactions and an exchangeable stationary law.
- A uniform quantitative gain from the nonreversible polymer circulation.

The relaxation problem for the stated finite linear-polymer model has a complete proof. These results do not constitute a solution to every mixing or spatial problem in the broader coagulation-fragmentation family. The original gap equality and the classical special models are attributed. The full text of Granovsky-Zeifman (2000) was not available during the priority review; an absolute first-in-literature claim is not made.

## Verification and provenance

The code independently constructs finite polymer and cut-set generators and compares their spectra to the radial formulas. Exact arithmetic checks cover the algebraic identities, transition balance, monomer drift, and circulation fluxes. Numerical checks cover the sharp estimates, critical approximations, spatial formulas, directed motions, and growing kernels. Analytic critical-operator truncation bounds are distinguished from floating-point eigenvalue error.

The PDF compiled without LaTeX warnings or bad boxes. All 45 rendered pages were inspected. `final_validation.json`, the three current visual review files, and `extensions/` record the revision checks. `initial_15_page_handoff.md` and `initial_15_page_validation.json` describe the earlier paper. Older audit and short-range visual files retained by Git history or elsewhere in this archive concern that earlier version.

These are research checks by collaborating AI systems, not independent journal peer review or formal verification. The author directs the project and is responsible for the paper. The archive records the result and its provenance; protected problem registries and native acceptance gates retain their existing semantics.
