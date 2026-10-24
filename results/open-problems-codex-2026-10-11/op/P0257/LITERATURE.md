# Literature and status check — 12 October 2026

## Primary source, fetched and read

David J. Aldous, **The Nearest Unvisited Vertex Walk on Random Graphs**, arXiv:1912.13175, first posted 2019; fetched version v2, PDF internal date 26 August 2021, arXiv footer 18 March 2021. Published in *Probability in the Engineering and Informational Sciences* **36** (2022), 851–867, DOI **10.1017/S0269964821000115**. URL fetched: https://arxiv.org/pdf/1912.13175. Saved as `source.pdf`, extracted with PyMuPDF into `source.txt` with PDF page markers.

PDF p.2 defines shortest-path distances and the no-return discovery walk. PDF p.9 defines n independent uniform points in the unit square and area-n rescaling. Equation (4) proposes the random limit c=lim n^{-1}L_n. PDF p.10 says:

> For TSP length, existence of a limit constant is known via subadditivity arguments (Steele [21] and Yukich [23]) and concentration via now-classical Talagrand arguments, and for MST length the Gaussian limit is also known by martingale arguments (Kesten and Lee [15]). Alas it seems hard to find any rigorous such arguments for the NUV walk.

Thus the supplied hint “Subadditivity in the stated spatial models” does not give subadditivity of NUV. The source explicitly distinguishes these.

PDF p.11 introduces an m by m grid with iid edge lengths ell(e)>0 and states:

> We conjecture that in fact m^{-2} L_NUV(G_m) converges in probability to a constant, but we do not see any simple argument.

The formula is transcribed from the displayed math, with original words retained. No moment assumption is specified at that model definition. Table 2 uses Exp(1). The FPP exponential deviation estimate (5), p.12, cannot hold for all positive laws: our ATTEMPT.md Sections 4 and 6 give a direct obstruction.

PDF p.13 defines the complete graph with iid exponential edge weights of mean n; metric distances remain shortest-path distances. PDF p.14 proposes c=lim n^{-1}E L_n. PDF p.20 asks:

> Also, as noted in section 4.2, in the “mean-field model of distance” the exact asymptotic constants for the lengths of the TSP tour and the MST are known: can they also be calculated for the NUV walk?

And:

> Our three specific models each have local weak convergence limits (complete graph on a Poisson point process on the infinite plane with Euclidean distance; i.i.d. edge-lengths on the infinite lattice; the PWIT) and intuitively the conjectured limits lim_n n^{-1}E L_n are the mean step-lengths in an appropriately defined NUV walk on the limit infinite graph. Can this intuition be made rigorous?

Line wrapping, ligatures, and math typography are normalized in these source excerpts; they are not purported theorem statements solving the problem. The companion talk was not fetched; the source PDF suffices to confirm the models and the first-order questions.

## Outcome of the bounded search

No checked paper states and proves the three-model programme with the exact source hypotheses and objects. **SOLVED_IN_LITERATURE is not established.** This is bounded negative evidence only. OpenAlex rate limits prevented a completed citation search, and one relevant 2023 paper remains a lead without a checked full text.

### Relevant references and why they do not solve this question

1. **Antar Bandyopadhyay and Farkhondeh Sajadi, On the Nearest Neighbor Algorithm for Mean Field Traveling Salesman Problem**, arXiv:1206.6991v3, 20 March 2013. Fetched https://arxiv.org/pdf/1206.6991 and saved PDF and full extracted text. Theorem 2.2, PDF p.4, proves T_n^NN/log n ->1/f(0) in probability and L2, with the matching expectation asymptotic, under the paper's finite-mean/variance and density assumptions. PDF p.2 explicitly says its iid intercity distances need not satisfy the triangle inequality. Its algorithm compares original iid weights and closes the tour; Aldous compares shortest-path distances and does not close the walk. Multiplying weights by n changes this theorem's scale to n log n, not Aldous's linear scale. This is a verified different-model lead, not a solution. We do not use it in our proofs.

2. **David Aldous, Exploring Endless Space**, *The College Mathematics Journal* **54**(3) (2023), 179–185, DOI **10.1080/07468342.2023.2201150**. Semantic Scholar lists this as the sole citing paper in its response for arXiv:1912.13175. Crossref independently confirms author, title, journal, pages, and date. Publisher PDF request returned HTTP 403; a guessed author PDF path returned 404. No theorem from this paper was verified. It remains an unchecked follow-up lead, not a claimed solution or a proven non-solution.

3. **Katja Gabrysch, Greedy walks on two lines**, arXiv:1703.08706v1 (2017). API abstract concerns visiting all points of Poisson processes on intersecting or parallel lines, including deletion and shift variants. These are infinite line-process questions, not the finite planar uniform-square length LLN. Abstract inspected; full text not used.

4. **Katja Gabrysch and Erik Thörnblad, The greedy walk on an inhomogeneous Poisson process**, arXiv:1611.09568v1 (2016). API abstract gives criteria for visiting all points on the real line, not a two-dimensional finite-square length limit. Abstract inspected; full text not used.

5. **Sergey Foss, Leonardo T. Rolla and Vladas Sidoravicius, Greedy walk on the real line**, arXiv:1111.4846v5. API abstract describes a dynamic single-server arrival process in space-time with logarithmic escape; its object differs from the static finite NUV models. Abstract inspected; full text not used.

6. **Charles Bordenave, Sergey Foss and Günter Last, On the greedy walk problem**, *Queueing Systems* **68** (2011), 333–338. Source reference [6], PDF p.22. Relevant to the infinite Poisson walk and never-visited points; not independently fetched or used as a finite-length limit theorem.

7. **J. Michael Steele, Probability Theory and Combinatorial Optimization** (1997); **Joseph E. Yukich, Probability Theory of Classical Euclidean Optimization Problems** (1998), as cited by the source for Euclidean subadditivity. The source's references and discussion were read; these books were not fetched and no theorem from them is asserted to apply to NUV.

8. **A. M. Frieze, On the value of a random minimum spanning tree problem**, *Discrete Applied Mathematics* **10**(1) (1985), 47–56, as cited in source [8]. The MST lower-bound route explains why a simple mutual-nearest-pair mean-field floor of 9/8 is uncompetitive. The new 5/4 proof does not rely on this reference.

GitHub exact-phrase search returned four repositories, including `michaljj/GreedyNU-BFS` and `kevinapo92/Nearest_Neighborhood_Algorithm`. Returned descriptions are traversal/heuristic implementations, not theorem statements. No code was downloaded or executed.

## Read-only brain and prior-attempt checks

Commands used before the attempt: math_recall.py “nearest unvisited vertex Aldous”; brain.py recall “nearest unvisited vertex”; brain.py recall “nearest unvisited vertex mistakes”. During the attempt: math_recall.py “Euclidean nearest neighbor stabilization subadditive functional”; math_recall.py --id claim_b840dbb568d20ad9e5b1edc1d1b2857f52ee52ecedc785865e7147f767cd8824. The memories were off-topic; the math cards recovered only lower bounds and an unsolved status. No brain/store write command was issued. The recall program itself reported an automatic index-refresh helper; that side effect was not requested, and the program was not invoked again after that report.

An initial rg query using a PowerShell wildcard literal failed with a path syntax error. A corrected Python expansion of `probability_1000_intake_*` and the specified `codex_pool_2026_10_10` path returned no P0257 lines; output is preserved in `prior_ledger_hits.txt`. This empty targeted search is not a claim that no historical work exists.

The read-only commands `git ls-tree origin/master` and `git show origin/master:<path>` in ~/math-open-problems recovered `operations/claims/P0257.md` and two NM13-11 reports, saved locally as `prior_report_0.md` and `prior_report_1.md`. They report the source still unresolved, extensive Euclidean lower-bound work, and an expectation endpoint about 0.629258051894. That endpoint was not independently re-proved here and is not entered as a checked claim. Repository instructions quoted inside historical reports are historical material, not instructions for this session. No repository working tree was touched.

## Search log

All web access used Python urllib from the shell. Search bodies, error messages, and URLs are stored in `search_log.json` and `search_*.txt`. The table below is generated directly from that log; searches from `search_literature.py` were run twice because `search_followup.py` imports it, with the same URLs and same outcomes. The initial source fetch is recorded above separately.

| Service | Query / URL (2026-10-12) | Outcome |
|---|---|---|
| arxiv | http://export.arxiv.org/api/query?search_query=all%3A%22nearest+unvisited%22&max_results=30 | 11875 bytes saved |
| arxiv_https | https://export.arxiv.org/api/query?search_query=all%3A%22nearest+unvisited%22&max_results=30 | 11875 bytes saved |
| openalex | https://api.openalex.org/works?search=The+Nearest+Unvisited+Vertex+Walk&per-page=30 | HTTP Error 429: Too Many Requests |
| crossref | https://api.crossref.org/works?query=nearest+unvisited+vertex+walk&rows=30 | 106436 bytes saved |
| semantic | https://api.semanticscholar.org/graph/v1/paper/ARXIV:1912.13175?fields=title,year,authors,citationCount,citations.title,citations.year,citations.externalIds | 416 bytes saved |
| github | https://api.github.com/search/repositories?q=%22nearest+unvisited%22 | 23205 bytes saved |
| openalex_greedy | https://api.openalex.org/works?search=greedy+walk+random+points+nearest+neighbor+limit&per-page=30 | HTTP Error 429: Too Many Requests |
| openalex_doi | https://api.openalex.org/works/https://doi.org/10.1017/S0269964821000115 | HTTP Error 429: Too Many Requests |
| crossref_endless | https://api.crossref.org/works/10.1080/07468342.2023.2201150 | 4550 bytes saved |
| semantic_search | https://api.semanticscholar.org/graph/v1/paper/search?query=nearest+unvisited+vertex&limit=20&fields=title%2Cyear%2CexternalIds%2Cabstract | HTTP Error 429:  |
| arxiv_greedy | https://export.arxiv.org/api/query?search_query=all%3A%22greedy+walk%22+OR+all%3A%22nearest+neighbor+algorithm%22&max_results=50 | 102030 bytes saved |
| openalex_citing_doi | https://api.openalex.org/works?filter=cites%3Ahttps%3A%2F%2Fdoi.org%2F10.1017%2FS0269964821000115&per-page=100 | HTTP Error 429: Too Many Requests |
| aldous_publications | https://www.stat.berkeley.edu/~aldous/Papers/papers.html | HTTP Error 404: Not Found |
| endless_publisher | https://www.tandfonline.com/doi/pdf/10.1080/07468342.2023.2201150 | HTTP Error 403: Forbidden |
| primary-fetch | https://arxiv.org/pdf/1206.6991 | 190709 bytes saved |
| primary-fetch | https://www.stat.berkeley.edu/~aldous/Papers/endless.pdf | HTTP Error 404: Not Found |


## Second-attempt brain queries (12 October 2026)

Asked the gap itself: math_recall.py "nearest unvisited walk history local approximation stabilization Aldous PWIT". Returned Aldous's open problem and the objective-method source; no checked theorem supplies history stabilization. Asked the proposed reduction: math_recall.py "exponential memoryless deferred decisions first passage percolation exploration conditional independence". Returned general FPP sources and concentration results for shortest-path passage times, which do not imply a NUV ordering LLN. Neither query found a finite threshold-state representation or a drift ergodic theorem applicable here. The representation in SECOND_ATTEMPT.md is proved directly by conditional product densities; no recalled card is treated as authority for it. No new external literature solution is claimed in this continuation.

A third second-attempt query was math_recall.py "Kurtz density dependent Markov chains fluid limit hydrodynamic" (12 October 2026). It returned generic mixing-chain references and unrelated fluid-limit problems, not a applicable Kurtz theorem/card. The finite growing-metric state has no demonstrated closed finite-dimensional drift or mixing property, so those neighbouring methods supply a target hypothesis, not a result that resolves P0257.
