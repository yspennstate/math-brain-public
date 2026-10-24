# Literature search log

Search date: 2026-10-11. Results and API failures will be recorded below.

- 2026-10-11 source_pdf: https://arxiv.org/pdf/1806.03755
  source_pdf: OK 229412 bytes

- 2026-10-11 source_abs: https://arxiv.org/abs/1806.03755
  source_abs: OK 40451 bytes

- 2026-10-11 arxiv: http://export.arxiv.org/api/query?search_query=all%3A%22generalized%20reflected%20Brownian%22&max_results=30
  arxiv: OK 3391 bytes

- 2026-10-11 openalex: https://api.openalex.org/works?search=Exponential%20ergodicity%20and%20convergence%20for%20generalized%20reflected%20Brownian%20motion&per-page=20
  openalex: FAILED HTTP Error 429: Too Many Requests

- 2026-10-11 crossref: https://api.crossref.org/works?query=generalized%20reflected%20Brownian%20motion&rows=20
  crossref: FAILED HTTP Error 429: Too Many Requests

- 2026-10-11 semantic: https://api.semanticscholar.org/graph/v1/paper/ARXIV:1806.03755?fields=title,authors,year,externalIds,citations.title,citations.year,citations.externalIds
  semantic: FAILED HTTP Error 429: 

- 2026-10-11 github: https://api.github.com/search/repositories?q=%22generalized%20reflected%20Brownian%22
  github: OK 55 bytes

- 2026-10-11 arxiv_https: https://export.arxiv.org/api/query?search_query=all%3A%22generalized%20reflected%20Brownian%22&max_results=50
  OK 3391 bytes

- 2026-10-11 arxiv_rate: https://export.arxiv.org/api/query?search_query=all%3A%22Brownian%22%20AND%20all%3A%22Tang%22%20AND%20all%3A%22ergodicity%22&max_results=30
  OK 8507 bytes

- 2026-10-11 openalex_retry: https://api.openalex.org/works?filter=title.search:generalized%20reflected%20Brownian&per_page=50
  HTTP Error 429: Too Many Requests

- 2026-10-11 crossref_retry: https://api.crossref.org/works?query.title=Exponential%20ergodicity%20and%20convergence%20for%20generalized%20reflected%20Brownian%20motion&rows=10
  OK 70097 bytes

- 2026-10-11 semantic_retry: https://api.semanticscholar.org/graph/v1/paper/search?query=generalized%20reflected%20Brownian&limit=30&fields=title,year,authors,externalIds
  HTTP Error 429: 

- 2026-10-11 github_retry: https://api.github.com/search/repositories?q=Brownian%20ergodicity
  OK 6634 bytes

- 2026-10-11 openalex_doi: https://api.openalex.org/works/https://doi.org/10.1007/s11134-019-09610-5
  HTTP Error 429: Too Many Requests

- 2026-10-11 openalex_doi_filter: https://api.openalex.org/works?filter=doi:https%3A//doi.org/10.1007/s11134-019-09610-5
  HTTP Error 429: Too Many Requests

- 2026-10-11 semantic_doi_citations: https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/s11134-019-09610-5/citations?fields=title,year,authors,externalIds&limit=100
  OK 1177 bytes

- 2026-10-11 arxiv_soft: https://export.arxiv.org/api/query?search_query=all%3A%22soft%20reflection%22%20OR%20all%3A%22OConnell-Yor%22%20OR%20%28all%3A%22O%27Connell-Yor%22%20AND%20all%3A%22convergence%22%29&max_results=60
  OK 28397 bytes

- 2026-10-11 arxiv_dimension: https://export.arxiv.org/api/query?search_query=ti%3A%22reflected%20Brownian%22%20AND%20%28all%3A%22dimension%22%20OR%20all%3A%22relaxation%22%29&max_results=40
  OK 28499 bytes

## Exact source and search assessment

- Tang, Wenpin (2019). Exponential ergodicity and convergence for generalized reflected Brownian motion. Queueing Systems 92, 83–101. DOI: 10.1007/s11134-019-09610-5. arXiv:1806.03755v2. Theorem 1.3 gives a Lyapunov drift constant of order 1/d; Corollary 1.4 gives a positive unspecified exponential rate; Conjecture 1.5 requests a rate at least C/d.
- Semantic Scholar DOI citations endpoint succeeded: 3 citing records, none concerning GRBM relaxation. Tang, Zhang and Zhou, Exploratory HJB Equations and Their Convergence (2022), DOI 10.1137/21M1448185, arXiv:2109.10269; Tang and Zhou, Simulated annealing from continuum to discretization: a convergence analysis via the Eyring–Kramers law, arXiv:2102.02339 (2021); Tang and Zhou, Tail probability estimates of continuous-time simulated annealing processes (2022; record has no DOI/arXiv).
- OpenAlex searches and exact DOI lookup returned HTTP 429. Its citing-works search remains to be attempted; missing results are not negative evidence.
- ArXiv exact phrase query returned the source and an unrelated older Robin-boundary paper. Broader queries returned hard reflection and KPZ/polymer scaling papers; none of the inspected abstracts states a solution.
- Crossref title search succeeded on retry and confirms the source DOI and journal publication. GitHub exact phrase query returned zero repositories; Brownian ergodicity query returned a numerical RBM repository, not a proof.

## Read-only brain / earlier work

2026-10-11: brain.py recall generalized reflected Brownian motion; brain.py recall reflected Brownian motion mistakes; math_recall.py generalized reflected Brownian exponential ergodicity Tang; math_recall.py Poincare log gamma Morse potential spectral gap. Returned generic spectral/Poincare cards, no solution.
Searched E0110 in the probability intake ledgers and codex_pool_2026_10_10. Read origin/master:prob1000_lean_20260908/ultracode_20260909/E0110/memo.md and U_E0110.lean through git show. September attempt proves transport identities / frozen-rate model only; it expressly leaves nonlinear coupling and joint total variation open. Its stationary expectation argument assumes integrability that must be justified separately. Its marginal histogram comparisons are not joint-TV checks.

- 2026-10-11 openalex_citing: https://api.openalex.org/works?filter=cites:https%3A%2F%2Fdoi.org%2F10.1007%2Fs11134-019-09610-5&per-page=100
  HTTP Error 429: Too Many Requests

- 2026-10-11 openalex_doi_variant: https://api.openalex.org/works/doi:10.1007/s11134-019-09610-5
  OK 15516 bytes

- 2026-10-11 arxiv_loggamma: https://export.arxiv.org/api/query?search_query=%28all%3A%22log-gamma%22%20OR%20all%3A%22Morse%22%29%20AND%20%28all%3A%22Poincare%22%20OR%20all%3A%22spectral%20gap%22%29&max_results=20
  OK 34504 bytes

- 2026-10-11 OpenAlex citing works: https://api.openalex.org/works?filter=cites:W2935248447&per_page=100
  HTTP Error 429: Too Many Requests

- 2026-10-11 OpenAlex citing works retry: https://api.openalex.org/works?filter=cites:W2935248447&per-page=50&select=id,doi,title,publication_year
  HTTP Error 429: Too Many Requests

- 2026-10-11 burgers_pdf: https://arxiv.org/pdf/1908.06591
  OK 307211 bytes

- 2026-10-11 crossref_rbm2020: https://api.crossref.org/works/10.1287/moor.2019.1006
  OK 4644 bytes

- 2026-10-11 crossref_rbm2018: https://api.crossref.org/works/10.1007/s11134-018-9574-1
  OK 12051 bytes


## Relevant subsequent and surrounding references

- Sayan Banerjee and Amarjit Budhiraja, Parameter and dimension dependence of convergence rates to stationarity for Reflecting Brownian Motions, arXiv:1902.04501v2 (2019; subsequent publication in Annals of Applied Probability, 2020). The inspected abstract gives L1-Wasserstein rates for hard-reflected orthant RBM, including O((log d)^2) relaxation for the Blanchet–Chen class and O(d^6(log d)^2) for the Atlas model. These are not the soft GRBM or the requested TV bound.
- Sayan Banerjee and Brendan Brown, Dimension-free local convergence and perturbations for reflected Brownian motions, arXiv:2009.12937v3. The inspected abstract gives dimension-independent stretched-exponential local convergence and polynomial perturbation results for hard RBM. Local convergence does not settle joint-TV Conjecture 1.5.
- Jose Blanchet and Xinyun Chen, Rates of Convergence to Stationarity for Reflected Brownian Motion, Mathematics of Operations Research 45 (2020), 660–681, DOI 10.1287/moor.2019.1006; preprint arXiv:1601.04111. Hard-reflection coupling results, referenced by the source, not a solution for soft GRBM.
- Peter W. Glynn and Rob J. Wang, On the rate of convergence to equilibrium for reflected Brownian motion, Queueing Systems 89 (2018), 165–197, DOI 10.1007/s11134-018-9574-1. Earlier hard-reflection work; its existence does not supply a subsequent solution of the source conjecture.
- Milton Jara and Gregorio R. Moreno Flores, Stationary Directed Polymers and Energy Solutions of the Burgers Equation, arXiv:1908.06591v1 (16 August 2019). PDF fetched and inspected: intermediate-disorder convergence of stationary O'Connell–Yor increments to stochastic Burgers energy solutions. Its abstract explicitly says it avoids spectral-gap estimates. This is a scaling limit, not the requested finite-dimensional relaxation theorem.

The broader arXiv queries also returned polymer free-energy fluctuation/scaling papers, including arXiv:2307.01172, 2511.11207, 2505.05685, 2401.10130, 2008.07241, 1809.09869, 1204.1024 and 1312.2600. Their inspected abstracts concern integrability, large deviations, Airy/KPZ scaling, or boundary perturbations, and make no claim to solve the general GRBM relaxation conjecture. Query result XML files preserve exact metadata.

## Final bounded-search assessment (2026-10-11)

No inspected paper settles Conjecture 1.5. This is not a definitive assertion that the literature has no solution.
OpenAlex exact source metadata finally succeeded using /works/doi:10.1007/s11134-019-09610-5, identifying W2935248447 and reporting cited_by_count=1. Both subsequent searches filter=cites:W2935248447 returned HTTP 429, so the OpenAlex citation graph could not be inspected. Semantic Scholar's DOI citation endpoint succeeded and returned three unrelated citing works. All failures, retries and exact query URLs are recorded above. No built-in web search or image tool was used.
