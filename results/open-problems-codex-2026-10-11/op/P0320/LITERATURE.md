# P0320 literature search, 2026-10-11

## Assessment

No complete solution of the higher-dimensional exponent band was found. This is a bounded search, not a proof of open status. OpenAlex repeatedly returned HTTP 429, so its source identification and citing-work searches could not be completed. Semantic Scholar source metadata and its citation list succeeded; its keyword and later author-paper requests were rate-limited. arXiv, Crossref, and GitHub returned usable results.

The source's 2023 statement is now partly superseded in dimension one for **periodic** ensembles: the September 2026 Pei preprint, combined with the Dereudre–Digneaux transport theorem, implies number rigidity for -1<s<0. The already-known Sine_beta rigidity handles s=0. Neither this implication nor the searched later papers settles every admissible Riesz ensemble or the d>=2 band.

## Relevant exact references and checked content

1. Eric Thoma, **Nonrigidity properties of the Coulomb gas**, *Annals of Probability* **54**(3) (2026), 1197–1211, DOI **10.1214/25-AOP1787**; arXiv:**2303.11486v1**, 20 March 2023. PDF fetched in full, text in `source_pdf_text.txt`; publication metadata fetched from Crossref. Introduction p. 2 explicitly leaves s in (d-2,d-1] open and proposes integrability of the Hessian as a heuristic. Proposition 1, p. 3, gives Coulomb non-rigidity under finite-volume convergence, beta bounds, upper Laplacian bound on W, and the non-vacuum annulus condition. Lemma 1 uses superharmonicity; Theorem 3 uses conditioned local-density estimates. These are the two parts a Riesz extension must address.
2. David Dereudre and Thibaut Vasseur, **Number-rigidity and β-circular Riesz gas**, *Annals of Probability* **51**(3) (2023), 1025–1065, DOI **10.1214/22-AOP1606**; arXiv:**2104.09408v1**, 19 April 2021. PDF fetched. For d-1<s<d and beta>0, proves existence of a non-number-rigid circular thermodynamic limit; stronger conditional support properties are in Theorem 1.11. Does not cover the target positive-exponent band.
3. Yan Ru Pei, **Uniform displacement bounds and Gibbs limits for periodic one-dimensional Riesz gases**, arXiv:**2609.28503v1**, 15 September 2026 (manuscript dated 14 September). PDF fetched and Theorems 1.1–1.3 inspected. For g=-|x|^a, 0<a<1, beta>0, every stationary periodic limit has a stationary ordered unit-lattice matching with square-integrable displacement (Theorem 1.2), and canonical Gibbs equations (Theorem 1.3). Theorem 1.2 plus reference 4 implies number rigidity in the d=1 negative-exponent target band. The paper explicitly does not identify periodic limits with stationarized container ensembles. This is a preprint result; no journal publication was verified.
4. David Dereudre and Rafaël Digneaux, **Rigidity of one-dimensional point processes via optimal transport**, arXiv:**2510.17257v2**, 21 September 2026 (v1 submitted 20 October 2025). PDF fetched. Theorem 2.1: a stationary one-dimensional point process with finite first transport distance to the shifted unit lattice is number rigid and has a cyclic factor. Its own Riesz application, Theorem 2.7, is for -2<s<=-1, outside the target interval; applying its general transport theorem to Pei's matching covers the periodic -1<s<0 interval. The introduction's open crystallization discussion concerns its container ensembles and does not erase this ensemble distinction.
5. Luke Peilen and Sylvia Serfaty, **Local Laws and Fluctuations for Super-Coulombic Riesz Gases**, arXiv:**2511.18623v2**, 31 December 2025 (v1 submitted 23 November 2025). PDF fetched. Treats d-2<s<d, proves bulk local laws and mesoscopic CLTs under assumptions A1–A6 on the confining potential and equilibrium measure. These fluctuation results are not a number-rigidity or non-rigidity theorem. The bulk nature of the stated local laws leaves the global pair-moment hypothesis of ATTEMPT.md unverified.
6. Raphaël Lachièze-Rey, **Rigidity of random stationary measures and applications to point processes**, arXiv:**2409.18519v3**, 27 February 2025. PDF fetched. Spectral criteria concern linear prediction/linear rigidity; non-rigidity in that sense must not be confused with failure of number measurability with respect to the whole exterior sigma-field. Its Riesz discussion deduces spectral non-integrability constraints from previously known non-rigidity, not a solution of the target band.
7. Thomas Leblé, **DLR equations, number-rigidity and translation-invariance for infinite-volume limit points of the 2DOCP**, arXiv:**2410.04958v1**, 7 October 2024. PDF fetched. Proves rigidity for two-dimensional Coulomb/log jellium at every positive temperature in its specified thermodynamic-limit regime. This is the s=0 boundary below the d=2 target interval (0,1], not a solution of it.

Semantic Scholar returned three papers citing Thoma: Leblé's reference 7; Eric Thoma's *A maximum principle for the Coulomb gas: microscopic density bounds, confinement estimates, and high temperature limits*, arXiv:2501.02733 (2025); and *Emergence of a Poisson process in weakly interacting particle systems*, arXiv:2405.02625 (2024). Only the first was directly fetched here; the citation list is not necessarily complete. The other two citation entries are not evidence of a solution.

GitHub `Riesz rigidity` returned zero repositories; `Riesz gas` returned `djalilchafai/RieszBox.jl` and `rodriguel/PTRiesz.jl`, both simulation projects. No proof or resolution was found through those repository results.

## Read-only internal searches

2026-10-11: `math_recall.py "Thoma Riesz number rigidity"` returned the source card, the open-problem card, and the earlier symmetric-Hessian attempt. The earlier attempt was also read using `math_recall.py --id claim_c546e11abf981724f6b7e1f81256ea839110d4d904cff1380f684bbdb289957f`; its integrability computation was independently rederived. `brain.py recall "Riesz number rigidity mistakes"` and `brain.py recall "Coulomb gas number rigidity"` returned mostly unrelated memories, with no verified solution.

2026-10-11: `rg -n P0320` in the read-only research ledgers found the intake entry and a ranking entry marked unsolved. A PowerShell wildcard path passed literally to rg failed; it was replaced by enumerating matching directories before rg. The supplied prior-attempt card records only the Hessian-tail calculation and explicitly leaves entropy, conditional control, and singularities unresolved. The repository command `git ... ls-tree -r --name-only origin/master | rg 'P0320|p0320'` returned no matching paths; the checkout was not modified. This is a path search, not a search of every repository file's contents.

## Raw remote-query log

The following entries record every fetch/query URL and its outcome. Successful raw responses are retained locally. The OpenAlex `cites:doi:...` filter was an unsuccessful attempted citation query; a valid source OpenAlex ID could not be obtained because source lookups were rate-limited, so it is not presented as a completed citing-work search.

- 2026-10-11 | openalex_search | https://api.openalex.org/works?search=Riesz%20number%20rigidity&per-page=50 | HTTP Error 429: Too Many Requests

- 2026-10-11 | openalex_source | https://api.openalex.org/works?search=Non-rigidity%20Properties%20of%20the%20Coulomb%20Gas&per-page=5 | HTTP Error 429: Too Many Requests

- 2026-10-11 | arxiv_https | https://export.arxiv.org/api/query?search_query=all:Riesz+AND+all:rigidity&start=0&max_results=40 | OK 43224 bytes

- 2026-10-11 | arxiv_http | http://export.arxiv.org/api/query?search_query=all:Riesz+AND+all:rigidity&start=0&max_results=40 | OK 43224 bytes

- 2026-10-11 | semantic_source | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2303.11486?fields=title,authors,year,externalIds,citations.title,citations.year,citations.externalIds | OK 1026 bytes

- 2026-10-11 | source_pdf | https://arxiv.org/pdf/2303.11486 | OK 459617 bytes

- 2026-10-11 | github | https://api.github.com/search/repositories?q=Riesz+rigidity&per_page=30 | OK 55 bytes

- 2026-10-11 | semantic_search | https://api.semanticscholar.org/graph/v1/paper/search?query=Riesz%20number%20rigidity&limit=30&fields=title,authors,year,externalIds | HTTP Error 429: 

- 2026-10-11 | source_html | https://arxiv.org/html/2303.11486 | OK 446773 bytes

- 2026-10-11 | crossref | https://api.crossref.org/works?query=Riesz%20number%20rigidity&rows=30 | OK 104749 bytes

- 2026-10-11 | openalex_doi | https://api.openalex.org/works/https://doi.org/10.1214/25-AOP1787 | HTTP Error 429: Too Many Requests

- 2026-10-11 | openalex_retry | https://api.openalex.org/works?search=Nonrigidity%20properties%20Coulomb&per_page=10 | HTTP Error 429: Too Many Requests

- 2026-10-11 | optimal_transport_pdf | https://arxiv.org/pdf/2510.17257 | OK 347202 bytes

- 2026-10-11 | arxiv_nonrigidity | https://export.arxiv.org/api/query?search_query=all:nonrigidity+OR+all:non-rigidity&sortBy=submittedDate&sortOrder=descending&max_results=40 | OK 92237 bytes

- 2026-10-11 | arxiv_riesz_recent | https://export.arxiv.org/api/query?search_query=all:Riesz+AND+all:gas&sortBy=submittedDate&sortOrder=descending&max_results=60 | OK 72718 bytes

- 2026-10-11 | github_gas | https://api.github.com/search/repositories?q=Riesz+gas&per_page=30 | OK 10648 bytes

- 2026-10-11 | stationary_pdf | https://arxiv.org/pdf/2409.18519 | OK 514587 bytes

- 2026-10-11 | circular_pdf | https://arxiv.org/pdf/2104.09408 | OK 421935 bytes

- 2026-10-11 | crossref_source | https://api.crossref.org/works/10.1214/25-AOP1787 | OK 6249 bytes

- 2026-10-11 | leblé_pdf | https://arxiv.org/pdf/2410.04958 | OK 616558 bytes

- 2026-10-11 | openalex_search_retry | https://api.openalex.org/works?search=Riesz%20gas%20rigidity&per-page=30&mailto=research%40example.org | HTTP Error 429: Too Many Requests

- 2026-10-11 | openalex_citing | https://api.openalex.org/works?filter=cites:doi:10.1214/25-aop1787&per-page=50 | HTTP Error 429: Too Many Requests

- 2026-10-11 | arxiv_target | https://export.arxiv.org/api/query?search_query=all:%22Riesz%22+AND+(all:%22non-rigidity%22+OR+all:%22number-rigidity%22)&max_results=40 | OK 6011 bytes

- 2026-10-11 | displacement_pdf | https://arxiv.org/pdf/2609.28503 | OK 372629 bytes

- 2026-10-11 | supercoulomb_pdf | https://arxiv.org/pdf/2511.18623 | OK 1549261 bytes

- 2026-10-11 | openalex_source_filter | https://api.openalex.org/works?filter=doi:https%3A%2F%2Fdoi.org%2F10.1214%2F25-aop1787 | HTTP Error 429: Too Many Requests

- 2026-10-11 | semantic_transport | https://api.semanticscholar.org/graph/v1/paper/ARXIV:2510.17257?fields=title,authors,year,citations.title,citations.externalIds | HTTP Error 429: 

- 2026-10-11 | crossref_transport | https://api.crossref.org/works?query.title=Rigidity%20of%20one-dimensional%20point%20processes%20via%20optimal%20transport&rows=3 | OK 19019 bytes
