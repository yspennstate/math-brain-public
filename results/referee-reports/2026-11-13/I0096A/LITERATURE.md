# Literature audit for I0096

Audit date: 2026-11-13. The requested target is the universal deterministic Conjecture 20, not the Gaussian Open Problem 21.

## Search scope and reproducibility

The raw OpenAlex and Semantic Scholar citation responses are in `data/`. They returned 75 and 90 records respectively. Records were screened for amplitude-map lower Lipschitz bounds, critical measurement counts, subframe singular values, and deterministic frame constructions. Neither public index is complete, and a search cannot certify absence from all literature.

Queries included the exact original title; Balan/Wang with conjecture, exponential, deterministic, lower Lipschitz, and critical; full spark and least singular value with 2025/2026; restricted invertibility and matrix selection; Vandermonde/harmonic/Fourier submatrices; and Plücker/Plucker relations with minors, frames, and singular values. Searches were run through the web search tool, with primary papers used to support mathematical conclusions. Non-paper open-problem trackers were discovery leads only.

## Verified core texts

- Bandeira et al., arXiv:2603.29571v1, Entry 10, Definition 10.1, Conjecture 20 and Open Problem 21: PDF p. 7. Conjecture 20 is the worst-case exponential bound; Open Problem 21 asks for Gaussian behavior.
- Balan–Wang, arXiv:1308.4718v1: Theorem 4.3, pp. 12–13, identifies the optimal amplitude-map lower Lipschitz constant through complementary subframe bounds. Section 5, equation (5.1), and Conjecture 5.1 are p. 16. The published ACHA 38 (2015), 469–488 version gives Theorem 4.3 on pp. 479–480, equation (5.1) on p. 483, and Conjecture 5.1 on p. 484. The arXiv conjecture has a sign typo corrected in the published version.
- the author, arXiv:2607.06249v1: Theorem 1.1, p. 2 (general real/complex Gaussian rate); Corollary 1.2, p. 4 (critical real rate 1/4). This is probabilistic and does not settle the universal conjecture.
- Häggblom, arXiv:2609.28198v1: Theorem 2, pp. 5–6, gives the full-spark critical reduction; Theorem 4, pp. 23–24, and Corollary 2, p. 24, give the finer high-probability scale, up to an arbitrary diverging subexponential factor.
- Yang–Wen–the author, arXiv:2608.07410v1: Theorem 1.1, pp. 2–3 (bounded-density subgaussian rate); Proposition 1.3 and Corollary 1.4, p. 4 (critical reduction and rate). The assumptions are on random ensembles, not on every matrix.
- Wen–Häggblom–Yang, arXiv:2611.06736v1 (2026-11-04): Theorems 1.1 and 1.3, pp. 3–4; Theorem 6.4 and Corollary 6.5, pp. 25–26. Extends random laws to surplus rows. It does not furnish a universal deterministic bound.

## Deterministic work that prevents claiming old bounds as new

- Liu–Wang, “On the decay of the smallest singular value of submatrices of rectangular matrices,” Asian-European J. Math. 9 (2016), 1650075, DOI 10.1142/S1793557116500753. Author-uploaded manuscript visible at ResearchGate; direct PDF retrieval failed (403). Lemma 2.2 on manuscript p. 3 gives 1/sqrt(n) for (n+1)-by-n; Lemma 2.4 on pp. 4–5 gives C/n^(3/2) for (n+2)-by-n. Its Section 3 develops kernel duality; Section 4 relates n+3 cases to planar point-to-line geometry. Journal pagination was not obtained and must not be invented.
- Liu, “On minimal smallest singular value of subframes for signal recovery,” Operators and Matrices 18 (2024), 273–293, DOI 10.7153/oam-2024-18-17. Theorem 2.3, pp. 277–280, characterizes the simplex equality case for n+1 rows. Theorem 2.7, pp. 284–286, solves the planar min-pair problem. Full text saved.
- Xu, arXiv:2508.10452v1, Theorem 1.1 p. 2 and Corollary 1.1 p. 3: deterministic lower bounds for the BEST selected submatrix, the opposite extremum from this problem.
- Kozyrev–Osinsky, arXiv:2610.08576: volume sampling/subset selection; assess whether any identity gives an upper bound for the WORST square subset rather than a good-subset guarantee.
- Xu–Xu–Zhang, arXiv:2510.04099v3, Theorems 1.1 and 1.2, pp. 2–3: optimal amplitude-map condition numbers in dimension 2. A planar result, not growing M at N=2M-1.
- Fourier/Vandermonde 2026 work, arXiv:2604.15135v3, addresses exponential conditioning of contiguous Fourier submatrices and related Vandermonde systems. Such structure-specific exponential examples cannot resolve the supremum over arbitrary frames.

## Lower Lipschitz background and adjacent citation branches

- Bandeira–Cahill–Mixon–Nelson, “Saving phase,” arXiv:1302.4618v3 / ACHA 37 (2014), 106–125: strong complement property and bounds for real amplitude measurements; predates the Balan–Wang paper but belongs in the comparison.
- Balan–Zou, LAA 496 (2016), 152–181: Theorem 2.1, p. 158, recalls the exact real lower Lipschitz formula; subsequent results concern complex maps, squared intensities, and Lipschitz extensions. No exponential dimension bound for every critical real frame.
- Freeman–Haider, arXiv:2502.09898: Theorem 3.10 and Corollary 3.11, pp. 19–20, refine strong-complement-property estimates. They do not supply the needed uniform exponential upper bound.
- Cahill–Casazza–Daubechies, arXiv:1601.06411: infinite-dimensional failure of uniform stability, not a universal exponential rate for all finite critical frames.
- “Stable phase retrieval and perturbations of frames,” arXiv:2212.13681: perturbation stability of a given frame; no dimension-uniform critical-threshold exponential theorem.
- Grohs–Koppensteiner–Rathmair, arXiv:1901.07911: survey of uniqueness and stability. Infinite-dimensional and structured-transform instability is distinct from the finite-dimensional worst-case conjecture.
- Rademacher–Shu, arXiv:2009.12685, Theorem 1.4, p. 4: Gaussian submatrix exponential instability, predating the exact Gaussian rate. Random, not universal deterministic.
- Balan–Dock, arXiv:2109.14522: generalized matrix frames, including lifted intensity-map constants; not the critical scalar-amplitude extremal problem.
- arXiv:2506.22053 and 2608.22418 study intensity-map / low-rank PSD sensing condition numbers with different metrics. These cannot be substituted for the amplitude map without tracking both the metric and constants.
- Phasebook, arXiv:2505.15351 / 2025 survey: checked as a recent source of open-problem context.

No printed proof or refutation of the universal conjecture has been located in this audit. This is a bounded search conclusion, not a claim of exhaustive coverage of all publications.
