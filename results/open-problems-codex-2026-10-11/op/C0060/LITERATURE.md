# Literature search log

Date: 2026-10-11. Source and API responses are saved locally. Brain recall is a lead, not evidence.

- 2026-10-11 | openalex_book | `https://api.openalex.org/works?search=An%20introduction%20to%20random%20interlacements&per-page=5` | openalex_book: ERROR HTTP Error 429: Too Many Requests

- 2026-10-11 | openalex | `https://api.openalex.org/works?search=random%20interlacements%20Sierpinski%20gasket&per-page=30` | openalex: ERROR HTTP Error 429: Too Many Requests

- 2026-10-11 | arxiv | `https://export.arxiv.org/api/query?search_query=all%3Ainterlacements%20AND%20all%3ASierpinski&max_results=30` | arxiv: OK 2668 bytes

- 2026-10-11 | github | `https://api.github.com/search/repositories?q=interlacements%20Sierpinski` | github: OK 55 bytes

- 2026-10-11 | semantic | `https://api.semanticscholar.org/graph/v1/paper/search?query=random%20interlacements%20Sierpinski%20gasket&limit=30&fields=title,authors,year,url,externalIds,abstract` | semantic: ERROR HTTP Error 429: 

- 2026-10-11 | crossref | `https://api.crossref.org/works?query=random%20interlacements%20Sierpinski%20gasket&rows=20` | crossref: OK 182348 bytes

- 2026-10-11 | source | `https://www.mi.uni-koeln.de/~drewitz/SpringerRI.pdf` | source: OK 1007278 bytes

- 2026-10-11 | arxiv_gasket | `https://export.arxiv.org/api/query?search_query=all%3A%22vacant%20set%22%20AND%20all%3Agasket&max_results=100&sortBy=submittedDate&sortOrder=descending` | arxiv_gasket: OK 743

- 2026-10-11 | semantic_retry | `https://api.semanticscholar.org/graph/v1/paper/search?query=vacant%20interlacements&limit=30&fields=title,authors,year,url,externalIds` | semantic_retry: OK 13794

- 2026-10-11 | openalex_retry | `https://api.openalex.org/works?search=interlacements&per_page=50` | openalex_retry: ERROR HTTP Error 429: Too Many Requests

- 2026-10-11 | arxiv_prevost | `https://export.arxiv.org/api/query?search_query=au%3APrevost%20AND%20all%3Apercolation&max_results=100&sortBy=submittedDate&sortOrder=descending` | arxiv_prevost: OK 26862

- 2026-10-11 | arxiv_positive | `https://export.arxiv.org/api/query?search_query=all%3Ainterlacements%20AND%20all%3Apositivity&max_results=100&sortBy=submittedDate&sortOrder=descending` | arxiv_positive: OK 203833

- 2026-10-11 | arxiv_general | `https://export.arxiv.org/api/query?search_query=all%3Ainterlacements%20AND%20%28all%3Agraphs%20OR%20all%3Afractal%29&max_results=100&sortBy=submittedDate&sortOrder=descending` | arxiv_general: OK 184872

- 2026-10-11 | crossref_book | `https://api.crossref.org/works?query.bibliographic=An%20introduction%20to%20random%20interlacements%20Drewitz%20Rath%20Sapozhnikov&rows=30` | crossref_book: OK 443185

- 2026-10-11 | crossref_general | `https://api.crossref.org/works?query.bibliographic=vacant%20set%20random%20interlacements%20transient%20graphs&rows=30` | crossref_general: OK 354321

- 2026-10-11 | openalex_citing | `https://api.openalex.org/works?filter=cites:doi:10.1007/978-3-319-05852-8&per-page=100` | openalex_citing ERROR HTTP Error 429: Too Many Requests

- 2026-10-11 | semantic_book | `https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/978-3-319-05852-8?fields=title,year,citations.title,citations.year,citations.externalIds` | semantic_book OK 23660

- 2026-10-11 | arxiv_exact | `https://export.arxiv.org/api/query?search_query=all%3A%22random%20interlacements%22%20AND%20%28all%3Agraphs%20OR%20all%3Agasket%20OR%20all%3Apositivity%29&max_results=100&sortBy=submittedDate&sortOrder=descending` | arxiv_exact OK 71690

- 2026-10-11 | zeroone2026 | `https://arxiv.org/pdf/2603.10896` | zeroone2026 OK 463624

- 2026-10-11 | signclusters | `https://arxiv.org/pdf/1708.03285` | signclusters OK 478709

- 2026-10-11 | sznitman2012 | `https://arxiv.org/pdf/1010.1490` | sznitman2012 OK 461105

- 2026-10-11 | fpp2023 | `https://arxiv.org/pdf/2309.03880` | fpp2023 OK 1499575

- 2026-10-11 | geometry | `https://arxiv.org/pdf/1811.05970` | geometry OK 1530546

## Verified resolution (2026-10-11)

Alexander Drewitz, Alexis Prévost and Pierre-François Rodriguez, **Geometry of Gaussian free field sign clusters and random interlacements**, *Probability Theory and Related Fields* **192**, 625–720 (2025), issues 1–2. First published online 15 June 2024. DOI: https://doi.org/10.1007/s00440-024-01285-1. Preprint: https://arxiv.org/abs/1811.05970 (first submitted November 2018; fetched version v3, 19 May 2024).

Primary evidence: Theorem 1.2 (preprint p. 6), equation (1.4), and Corollary 3.9 (preprint p. 27). The exact graph is explicitly included. The theorem supplies a positive level below which the vacant set has an infinite connected component almost surely. The authors explicitly state this resolves Sznitman's Remark 5.6(2), the same open problem cited on p. 81 of the source book.

Source: Alexander Drewitz, Balázs Ráth and Artem Sapozhnikov, *An Introduction to Random Interlacements*, preliminary version, 30 December 2013, Chapter 10, §10.3, p. 81; downloaded from https://www.mi.uni-koeln.de/~drewitz/SpringerRI.pdf. Published book DOI: 10.1007/978-3-319-05852-8 (2014).

Earlier formulation: Alain-Sol Sznitman, *Decoupling inequalities and interlacement percolation on G × Z*, *Inventiones mathematicae* **187**(3), 645–706 (2012), DOI 10.1007/s00222-011-0340-9; arXiv:1010.1490; Remark 5.6(2). Theorem 5.1's restriction ν ≥ 1 excluded this gasket example.

Relevant later corroboration: Alexis Prévost, *First passage percolation, local uniqueness for interlacements and capacity of random walk*, arXiv:2309.03880, fetched v3. Its discussion following (2.21) cites the general positivity result under (WSI). This is corroboration; the actual resolution is the Drewitz–Prévost–Rodriguez theorem.

Search assessment: arXiv's unquoted token “interlacements” also retrieved unrelated interlacing papers; the follow-up used the quoted phrase “random interlacements”. The gasket-only query returned Windisch (2010), not the resolving paper. The resolving paper was found via the broader graph query and Crossref bibliographic query. OpenAlex returned HTTP 429 for both works searches and the attempted citing-works request; that citing filter was not validated and yielded no evidence. Semantic Scholar's first query returned HTTP 429; a broader retry and book citation lookup succeeded. GitHub repository search returned zero repositories. No negative search result is used to establish openness.

Read-only prior-work checks: brain.py recall “Sierpinski gasket random interlacements”; brain.py recall “random interlacements mistakes”; math_recall.py --id claim_a835d45e1798b39d585bc9cc2c8c531b6036d8edce009ddc059cb9f939556aef; math_recall.py “Drewitz Prevost Rodriguez transient graphs vacant percolation”. Intake ledgers and codex_pool searched for C0060; Windows wildcard path initially failed and was replaced by enumerating matching directories. Published answer read with git show origin/master:probability_campaigns/codex_pool_2026-10-10/team_O/w343/C0060_proof.md. That earlier answer only refutes a finite-fiber blocking heuristic; it is not a resolution of the threshold question.
