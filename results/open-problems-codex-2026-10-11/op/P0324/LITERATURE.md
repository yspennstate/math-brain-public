# Literature check ? P0324, 2026-10-12

Outcome: no paper proving the requested all-positive-temperature real analyticity was found in the accessible searches. This is NOT an exhaustive certification that no such paper exists. OpenAlex repeatedly returned HTTP 429; its citing-work search could not be completed. No SOLVED_IN_LITERATURE verdict is justified.

## Exact source and hypotheses
Jeanne Boursier, *Decay of correlations and thermodynamic limit for the circular Riesz gas*, arXiv:2209.00396v4, 19 July 2023, 64 PDF pages. https://arxiv.org/pdf/2209.00396. Retrieved as source.pdf, extracted as source.txt.
The model in equations (1.1), (1.3), (1.4) has 0<s<1, beta>0, unit circle, cyclically ordered configurations D_N, H_N=N^{-s} sum_{i!=j} g_s(x_i-x_j), and density proportional to exp(-beta H_N) times ordered Lebesgue measure. Section 1.3, PDF page 5, equation (1.10) discusses free energy and states:

> In dimension one, one expects that no phase transition occurs for the circular
> Riesz gas and that the free energy is smooth and even analytic. To prove that f is twice diﬀerentiable,
> a standard approach is to prove that the rescaled variance of the energy under (1.4) converges locally
> uniformly in β as N tends to inﬁnity. This should be an easy consequence of Theorems 1 and 3.
> 

This is an expectation, not an analyticity theorem. Theorems 1 and 3 prove gap-correlation decay and convergence of periodic laws. Their statements do not give all-order energy cumulants or complex-temperature control. See ATTEMPT.md for the entropy normalization issue in the literal displayed (1.10).

## Relevant retrieved leads and exact references
- Yan Ru Pei, *Uniform displacement bounds and Gibbs limits for periodic one-dimensional Riesz gases*, arXiv:2609.28503v1, 15 September 2026. Theorems 1.1?1.3, PDF pages 2?3, concern local potential -|x|^a, 0<a<1 (negative Riesz exponent), not +|x|^{-s}, 0<s<1. No analyticity claim in this PDF. Different model; cannot solve P0324.
- Martin Huesmann and Bastian M?ller, *Gap metrics for stationary point processes and quantitative convexity of the free energy*, arXiv:2509.08659v1, 10 September 2025. Theorem 1.1, PDF page 2, proves convexity along interpolation of point-process laws. Section 6 applies this to logarithmic and long-range Riesz interactions. It does not assert analyticity as a function of beta. Convexity in the measure variable is a lead, not a solution.
- Pierre Le Doussal and Gr?gory Schehr, *Cumulants and large deviations for the linear statistics of the one-dimensional trapped Riesz gas*, arXiv:2408.04437v1, 8 August 2024; DOI 10.1007/s10955-025-03429-6 reported by Semantic Scholar. External confinement and linear-statistic cumulants differ from total-energy cumulants of the circular thermodynamic gas. No theorem matching P0324 was found.
- L?o Touzo, Pierre Le Doussal and Gr?gory Schehr, *Spatio-temporal fluctuations in the passive and active Riesz gas on the circle*, arXiv:2411.01355v1, 2 November 2024. Weak-noise linearization and Hessian calculations; no all-temperature free-energy analyticity theorem. IMPORTANT metadata correction: Semantic Scholar supplied this arXiv ID for the trapped-cumulants title. Reading the PDF showed that identification was wrong. Correct trapped-cumulants ID was recovered from the arXiv search above.
- Rodrigue Lelotte, *Phase transitions in one-dimensional Riesz gases with long-range interaction*, arXiv:2309.08951 (retrieved current PDF has shortened title *Phase transitions in one-dimensional Riesz gases*). The numerical investigation is for -1<s<0; Remark 1 on PDF page 4 discusses possible BKT behavior for positive s as an open direction. This is not a proved counterexample for 0<s<1, and uniqueness of the periodic law alone would not rule out every kind of transition.
- Thomas Lebl? and Sylvia Serfaty, *Large deviation principle for empirical fields of Log and Riesz gases*, Inventiones Mathematicae 210 (2017), 645?757, arXiv:1502.02970. Source reference [LS17] for existence of a suitably normalized free-energy limit. Existence is not analyticity.
- Andr?s Pr?kopa, *On logarithmic concave measures and functions*, Acta Scientiarum Mathematicarum (Szeged) 34 (1973), 335?343. The classical marginal log-concavity theorem is used explicitly, with all application hypotheses checked, in ATTEMPT.md. It supplies the variance bound only.

## Required service searches (actual requests, including failures)
Every request below was made from Python urllib in this folder, without built-in web search. Raw responses are saved under the listed file names. HTTP 429 means unavailable, not no results. Dates use the supplied local research date.

- 2026-10-12 ? `source.pdf`: https://arxiv.org/pdf/2209.00396
  Result: source.pdf: OK 914778 bytes
- 2026-10-12 ? `arxiv.xml`: http://export.arxiv.org/api/query?search_query=all%3A%22Riesz%22%20AND%20%28all%3A%22analyticity%22%20OR%20all%3A%22Boursier%22%29&max_results=40
  Result: arxiv.xml: OK 70939 bytes
- 2026-10-12 ? `openalex.json`: https://api.openalex.org/works?search=Decay%20of%20correlations%20and%20thermodynamic%20limit%20for%20circular%20Riesz%20gas&per-page=10
  Result: openalex.json: ERROR HTTP Error 429: Too Many Requests
- 2026-10-12 ? `openalex_analytic.json`: https://api.openalex.org/works?search=Riesz%20gas%20free%20energy%20analyticity&per-page=25
  Result: openalex_analytic.json: ERROR HTTP Error 429: Too Many Requests
- 2026-10-12 ? `crossref.json`: https://api.crossref.org/works?query=Riesz%20gas%20free%20energy%20analyticity&rows=25
  Result: crossref.json: ERROR HTTP Error 429: Too Many Requests
- 2026-10-12 ? `semantic.json`: https://api.semanticscholar.org/graph/v1/paper/ARXIV:2209.00396?fields=title,authors,year,externalIds,citations.title,citations.year,citations.externalIds
  Result: semantic.json: OK 2675 bytes
- 2026-10-12 ? `github.json`: https://api.github.com/search/repositories?q=Riesz%20gas
  Result: github.json: OK 10648 bytes
- 2026-10-12 ? `lead_2609.28503.pdf`: https://arxiv.org/pdf/2609.28503
  Result: OK 372629
- 2026-10-12 ? `lead_2509.08659.pdf`: https://arxiv.org/pdf/2509.08659
  Result: OK 721824
- 2026-10-12 ? `lead_2411.01355.pdf`: https://arxiv.org/pdf/2411.01355
  Result: OK 2268996
- 2026-10-12 ? `lead_2309.08951.pdf`: https://arxiv.org/pdf/2309.08951
  Result: OK 1336444
- 2026-10-12 ? `openalex_retry.json`: https://api.openalex.org/works?filter=locations.source.id:s4306400194&search=Riesz&per_page=10
  Result: HTTP Error 429: Too Many Requests
- 2026-10-12 ? `openalex_source_retry.json`: https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2209.00396
  Result: HTTP Error 429: Too Many Requests
- 2026-10-12 ? `crossref_retry.json`: https://api.crossref.org/works?query.title=Decay%20of%20correlations%20and%20thermodynamic%20limit%20for%20circular%20Riesz%20gas&rows=5
  Result: OK 35060
- 2026-10-12 ? `arxiv_recent.xml`: https://export.arxiv.org/api/query?search_query=all%3A%22Riesz%20gas%22&sortBy=submittedDate&sortOrder=descending&max_results=60
  Result: OK 52196
- 2026-10-12 ? `openalex_final.json`: https://api.openalex.org/works?search=circular%20Riesz%20gas&per-page=5
  Result: HTTP Error 429: Too Many Requests
- 2026-10-12 ? `crossref_analytic.json`: https://api.crossref.org/works?query.bibliographic=Riesz%20gas%20free%20energy%20analyticity&rows=15
  Result: OK 84755
- 2026-10-12 ? `lead_2408.04437.pdf`: https://arxiv.org/pdf/2408.04437
  Result: OK 1566573
- 2026-10-12 ? `arxiv_analytic.xml`: https://export.arxiv.org/api/query?search_query=all%3A%22Riesz%22%20AND%20all%3A%22free%20energy%22&max_results=40
  Result: OK 28948
- 2026-10-12 ? `openalex_citing.json`: https://api.openalex.org/works?filter=cites:553252f8121d409b67c20553a02f3f4f39fa019a&per-page=50
  Result: HTTP Error 429: Too Many Requests

The final OpenAlex citing request used the Semantic Scholar paper identifier provisionally. This is NOT a valid OpenAlex work ID and would not be a valid citing search even without rate limiting. All OpenAlex title/DOI resolution requests also failed with 429; no resolved OpenAlex work ID was available. Therefore OpenAlex citing coverage remains explicitly incomplete. Semantic Scholar's successful source lookup supplied ten citing works, inspected for candidates above.

ArXiv searches: the first broad query returned many irrelevant Riesz-operator papers. The exact phrase "Riesz gas", sorted by most recent submission, and the conjunction "Riesz"/"free energy" supplied better model-specific coverage. No returned candidate claimed the requested theorem. Crossref broad search ranked largely irrelevant titles; the source-title search also found Boursier's earlier *Number-rigidity and beta-circular Riesz gas*, DOI 10.1214/22-aop1606, which is not the requested result. GitHub returned djalilchafai/RieszBox.jl and rodriguel/PTRiesz.jl, simulation repositories, not proofs of analyticity.

## Read-only research brain and earlier work
Ran math_recall.py on "Riesz gas free energy cumulant analyticity" and "Prekopa convex Hamiltonian temperature variance", and brain.py recall on "Riesz gas analyticity mistakes" and "one-dimensional Riesz free energy". The relevant previous-attempt card is claim_ea8e25cca971c64c25308f9a295caf1098dcf59bc250b52be36b1418748264f7: energy cumulants and a generic nonanalytic-limit example, with no solution. Its claims were treated as hints and proved independently here.
Read-only rg searched the expanded probability_1000_intake_* directories and codex_pool_2026_10_10 for P0324. The 7 September ranking records an unsolved cumulant obstruction. git ls-tree on origin/master in math-open-problems did not locate a dedicated P0324 path; no working-tree changes were made. No memory or repository was modified.

## Second-attempt neighboring theorem search, 2026-10-12

Read Fernandez and Procacci, *Cluster expansion for abstract polymer models. New bounds from an old approach*, arXiv:math-ph/0605041v2, 16 October 2006, PDF pages 3-4, equations (2.7) and (2.10)-(2.15). The Kotecky-Preiss criterion is used as a known theorem for a cell-constrained model; it is not a literature solution to P0324. Its product-reference and bounded-activity hypotheses are checked in SECOND_ATTEMPT.md.

- 2026-10-12 -- polymer_reference.pdf: https://arxiv.org/pdf/math-ph/0605041 -- OK 239573
- 2026-10-12 -- polymer_search.xml: https://export.arxiv.org/api/query?search_query=au:Fernandez%20AND%20au:Procacci%20AND%20all:polymer&max_results=5 -- OK 5783

Brain gap queries: complete analyticity/truncated correlations/tree cumulants/Helffer-Sjostrand; Kotecky-Preiss/polymer expansion/tree graphs; Ruelle/one-dimensional interaction/first moment/transfer operator; uniform energy cumulant factorial bounds/cluster expansion/Riesz. No direct applicable analyticity theorem returned. A recalled continuum-defect warning required checking both energy and measure costs; the second attempt proves an explicit pressure gap for the fixed-cell restriction rather than assuming it can be removed.
