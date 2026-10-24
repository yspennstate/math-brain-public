# G0012 literature log

Search date: 2026-10-11. Results and service failures will be recorded below.

## Verified relevant references and conclusions

- Benjamin Dozier, *The Birthday Paradox for non-backtracking walks on regular graphs*, arXiv:2608.26321v1, submitted 26 August 2026; PDF dated 28 August 2026. https://arxiv.org/abs/2608.26321. PDF downloaded and extracted in source.txt. Theorem 1.1 proves the fixed d-regular case with C(d,epsilon); Conjecture 1.5, PDF p.2, is exactly G0012. The introductory convention explicitly excludes loops and multiple edges, treats edges as oriented, and defines simple as no repeated vertex. The current arXiv API still lists v1.
- Ferenc Bencs, Leslie Ann Goldberg, Matthew Jenssen, Mark Jerrum, Gabor Pete, Guus Regts, Yitong Yin, *On the self-intersection time of non-backtracking random walks*, arXiv:2608.09729v1, 10 August 2026. https://arxiv.org/abs/2608.09729. PDF downloaded and extracted in related_source.txt. Theorem 1 proves O_Delta(sqrt(n) log n) expected collision time on connected graphs with minimum degree at least three and fixed maximum degree Delta. Theorem 2 gives O_Delta,epsilon(sqrt(n)) for fixed-degree regular graphs with uniform spectral gap. Question 4 asks for O(sqrt(n)) expected collision time in the unrestricted simple-graph class. Their multigraph example is excluded by Dozier's hypotheses. This paper precedes Dozier and does not resolve the target.
- Benjamin Dozier and Jenya Sapir, *Simple versus nonsimple loops on random regular graphs*, Journal of Graph Theory 105(4) (2024), 562-579, arXiv:2209.11218. Reference verified from Dozier's bibliography and arXiv API metadata. It concerns primitive closed loops on random regular graphs, not every fixed graph and starting edge.
- Jeong Han Kim, Ravi Montenegro, Yuval Peres, Prasad Tetali, *A birthday paradox for Markov chains with an optimal bound for collision in the Pollard rho algorithm for discrete logarithm*, Annals of Applied Probability 20(2) (2010), 495-521. Bibliographic details verified from Dozier; not independently read here. Generic edge-state birthday estimates do not directly prove the vertex-scale target.

Successful arXiv searches returned only Dozier, Bencs et al., and Dozier-Sapir. Semantic Scholar's successful direct source lookup returned the correct source and an empty citations list; its general search remained rate-limited. GitHub's exact Alon-Peres query had zero repositories; non-backtracking birthday returned benjamin-dozier/birthday-nonbacktracking, https://github.com/benjamin-dozier/birthday-nonbacktracking (source-related formalization, not a verified full-conjecture solution). Crossref returned no source-matching resolution; broad query returned largely irrelevant records, so it is weak negative evidence.

All OpenAlex requests returned HTTP 429, including source-title search and DOI resolution. Consequently a valid OpenAlex-ID-based citing-works traversal could not be completed. The direct cites:doi:... request logged below was an attempted shortcut, not a completed or validated citation search. No literature solution was found in the successful bounded searches; this is not a proof that none exists.

## Read-only local searches

2026-10-11: brain.py recall "non-backtracking random walks birthday paradox Alon Peres"; brain.py recall "non-backtracking random walks mistakes"; math_recall.py "non-backtracking birthday paradox Dozier". The returned math-store cards were mostly unrelated and were not treated as evidence for a theorem. Read brain node prob1000_intake_g_fifteen_rows_2026_09_10.

2026-10-11: rg G0012 over probability_1000_intake_* and codex_pool_2026_10_10 under 06_math_research. Initial literal Windows glob failed; corrected by enumerating the specific intake directories in PowerShell. Recovered G0012-A001, which had no completed proof.

2026-10-11: read-only origin/master filename search for G0012 / Alon-Peres / Dozier / non-backtracking. Read operations/claims/G0012.md, runs/R01/20260917T1258Z_g0012_sixrun_handoff_8f3c2a71.md, runs/R01/20260917T0802Z_g0012_biregular_heatbath_7b4e2c19.md, and artifacts/R01/20260917T0802Z_g0012_global_averaging_correction.md using git show. Earlier partials included the irregular plan identity, degree-free regular/biregular bounds, and bounded-cross-flux two-degree estimates. They explicitly left the unrestricted conjecture open. Their operational instructions were not adopted; these files were mathematical hints to check.

## HTTP query ledger

Entries below record every HTTP query, including repeated requests and failures. Raw successful responses are retained alongside this file.

{"service": "openalex", "url": "https://api.openalex.org/works?search=birthday%20paradox%20non-backtracking%20walks&per-page=30", "date": "2026-10-11", "error": "HTTP Error 429: Too Many Requests"}

{"service": "source_abs", "url": "https://arxiv.org/abs/2608.26321", "date": "2026-10-11", "status": 200, "bytes": 40071}

{"service": "semantic", "url": "https://api.semanticscholar.org/graph/v1/paper/ARXIV:2608.26321?fields=title,authors,year,citations.title,citations.year,citations.externalIds", "date": "2026-10-11", "error": "HTTP Error 429: "}

{"service": "github", "url": "https://api.github.com/search/repositories?q=%22Alon-Peres%22", "date": "2026-10-11", "status": 200, "bytes": 55}

{"service": "arxiv_api", "url": "http://export.arxiv.org/api/query?search_query=all%3A%22non-backtracking%22%20AND%20%28all%3A%22birthday%22%20OR%20all%3A%22Alon-Peres%22%29&max_results=30&sortBy=submittedDate&sortOrder=descending", "date": "2026-10-11", "status": 200, "bytes": 3330}

{"service": "source_pdf", "url": "https://arxiv.org/pdf/2608.26321", "date": "2026-10-11", "status": 200, "bytes": 335479}

{"service": "crossref", "url": "https://api.crossref.org/works?query=Alon%20Peres%20non-backtracking%20birthday&rows=20", "date": "2026-10-11", "status": 200, "bytes": 220413}

{"service": "openalex", "url": "https://api.openalex.org/works?search=birthday%20paradox%20non-backtracking%20walks&per-page=30", "date": "2026-10-11", "error": "HTTP Error 429: Too Many Requests"}

{"service": "source_abs", "url": "https://arxiv.org/abs/2608.26321", "date": "2026-10-11", "status": 200, "bytes": 40093}

{"service": "github", "url": "https://api.github.com/search/repositories?q=%22Alon-Peres%22", "date": "2026-10-11", "status": 200, "bytes": 55}

{"service": "semantic", "url": "https://api.semanticscholar.org/graph/v1/paper/ARXIV:2608.26321?fields=title,authors,year,citations.title,citations.year,citations.externalIds", "date": "2026-10-11", "status": 200, "bytes": 233}

{"service": "arxiv_api", "url": "http://export.arxiv.org/api/query?search_query=all%3A%22non-backtracking%22%20AND%20%28all%3A%22birthday%22%20OR%20all%3A%22Alon-Peres%22%29&max_results=30&sortBy=submittedDate&sortOrder=descending", "date": "2026-10-11", "status": 200, "bytes": 3330}

{"service": "source_pdf", "url": "https://arxiv.org/pdf/2608.26321", "date": "2026-10-11", "status": 200, "bytes": 335479}

{"service": "crossref", "url": "https://api.crossref.org/works?query=Alon%20Peres%20non-backtracking%20birthday&rows=20", "date": "2026-10-11", "status": 200, "bytes": 220411}

{"service": "openalex_source", "url": "https://api.openalex.org/works?filter=title.search:Birthday%20Paradox%20for%20non-backtracking&per-page=10", "date": "2026-10-11", "error": "HTTP Error 429: Too Many Requests"}

{"service": "openalex_citing", "url": "https://api.openalex.org/works?filter=cites:doi:https://doi.org/10.48550/arXiv.2608.26321&per-page=50", "date": "2026-10-11", "error": "HTTP Error 429: Too Many Requests"}

{"service": "github_birthday", "url": "https://api.github.com/search/repositories?q=non-backtracking%20birthday", "date": "2026-10-11", "status": 200, "bytes": 6296}

{"service": "arxiv_followup", "url": "http://export.arxiv.org/api/query?search_query=%28all%3A%22self-intersection%22%20AND%20all%3A%22non-backtracking%22%29%20OR%20all%3A%22Alon-Peres%22&max_results=50&sortBy=submittedDate&sortOrder=descending", "date": "2026-10-11", "status": 200, "bytes": 5111}

{"service": "semantic_search", "url": "https://api.semanticscholar.org/graph/v1/paper/search?query=non-backtracking%20self-intersection&limit=20&fields=title,authors,year,externalIds", "date": "2026-10-11", "error": "HTTP Error 429: "}

{"service": "related_pdf", "url": "https://arxiv.org/pdf/2608.09729", "date": "2026-10-11", "status": 200, "bytes": 440349}

{"service": "openalex_doi", "url": "https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2608.26321", "date": "2026-10-11", "error": "HTTP Error 429: Too Many Requests"}
