# Literature searches, 2026-10-12

- arxiv: `http://export.arxiv.org/api/query?search_query=all%3A%22Erlang%20Weighted%20Tree%22%20OR%20all%3A%22La-Kabkab%22&max_results=30` ? OK; raw response: arxiv.response.txt
- arxiv_https: `https://export.arxiv.org/api/query?search_query=all%3A%22bilateral%22%20AND%20all%3A%22random%20graph%22&max_results=30` ? OK; raw response: arxiv_https.response.txt
- openalex: `https://api.openalex.org/works?search=Erlang%20Weighted%20Tree&per-page=30` ? ERROR HTTP Error 429: Too Many Requests; raw response: openalex.response.txt
- openalex_bilateral: `https://api.openalex.org/works?search=bilateral%20random%20graph&per-page=30` ? ERROR HTTP Error 429: Too Many Requests; raw response: openalex_bilateral.response.txt
- crossref: `https://api.crossref.org/works?query=Erlang%20Weighted%20Tree&rows=15` ? OK; raw response: crossref.response.txt
- semantic: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:2002.03993?fields=title,year,citationCount,citations.title,citations.year,citations.externalIds` ? ERROR HTTP Error 429: ; raw response: semantic.response.txt
- github: `https://api.github.com/search/repositories?q=%22Erlang%20Weighted%20Tree%22` ? OK; raw response: github.response.txt
- 2026-10-12 openalex_retry: `https://api.openalex.org/works?search=2002.03993&per_page=10` ? HTTP Error 429: Too Many Requests
- 2026-10-12 arxiv_nearest: `https://export.arxiv.org/api/query?search_query=all%3A%22mutual%22%20AND%20all%3A%22nearest%20neighbor%22%20AND%20all%3A%22giant%22&max_results=40` ? OK
- 2026-10-12 semantic_retry: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:2002.03993/citations?fields=title,year,externalIds&limit=100` ? OK
- 2026-10-12 crossref_bilateral: `https://api.crossref.org/works?query.title=Connectivity%20of%20a%20Family%20of%20Bilateral%20Agreement%20Random%20Graphs&rows=5` ? OK
- 2026-10-12 connectivity_pdf: `https://arxiv.org/pdf/2209.05677v3` ? OK

## Verified primary sources

Mehrdad Moharrami, Vijay Subramanian, Mingyan Liu and Rajesh Sundaresan, *The Erlang Weighted Tree, A New Branching Process*, arXiv:2002.03993v5, 27 May 2023, 90 PDF pages. Downloaded source_v5.pdf; extracted source_v5.txt. Section 4 question 3, PDF p.16 explicitly asks for the reverse inequality. The introduction assumes P on positive integers, finite mean, P(1)<1; Section 2 permits deterministic degree arrays whose empirical laws converge weakly and di<=n-2. Theorem 2.1 (p.9) is annealed local convergence EU(Nn) => Er(P). IID budgets are described on p.3, truncated at n-1; thresholds at n-1 can be interpreted as infinity. Exponential moment assumptions concern later spectral results, not the wording of question 3.

Hossein Dabirian and Vijay Subramanian, *Connectivity of a Family of Bilateral Preference Random Graphs*, arXiv:2209.05677v3, 8 July 2025; journal DOI 10.1017/jpr.2025.10051 (Semantic Scholar identifies a 2025 journal record, DBLP labels it 2026). Its Theorem 1.1, PDF p.1, addresses budgets k(n) near log n. It does not state or prove the fixed-law giant-density equality. Saved connectivity_pdf.pdf and connectivity.txt.

Semantic Scholar citations endpoint succeeded on retry: exactly two records, the arXiv and journal versions of Dabirian--Subramanian. Initial paper-detail endpoint was rate limited. OpenAlex searches have been rate limited, so the search is incomplete there. Crossref broad search returned unrelated Erlang distribution/tree automata records; title search for the connectivity paper checked separately. GitHub exact-title search returned zero repositories. ArXiv exact EWT/La-Kabkab query returned the source only; bilateral/random-graph query found the connectivity paper; mutual/nearest-neighbor/giant query returned no entries. No matching solution in print was found; this is a bounded search, not a certification that no solution exists.
- 2026-10-12 openalex_doi: `https://api.openalex.org/works/https://doi.org/10.1017/jpr.2025.10051` ? HTTP Error 429: Too Many Requests
- 2026-10-12 openalex_title_retry: `https://api.openalex.org/works?filter=title.search:erlang%20weighted%20tree&per-page=5` ? HTTP Error 429: Too Many Requests
- 2026-10-12 arxiv_local: `https://export.arxiv.org/api/query?search_query=ti%3A%22giant%22%20AND%20ti%3A%22local%22&max_results=20` ? OK
- 2026-10-12 github_bilateral: `https://api.github.com/search/repositories?q=%22bilateral%22%20%22random%20graphs%22` ? OK
- 2026-10-12 almostlocal_pdf: `https://arxiv.org/pdf/2103.11733v3` ? OK
- 2026-10-12 arxiv_preferences: `https://export.arxiv.org/api/query?search_query=all%3A%22bilateral%20preference%22%20OR%20all%3A%22La%20Kabkab%22%20OR%20all%3A%22mutual%20k-nearest%22&max_results=50` ? OK
- 2026-10-12 crossref_source: `https://api.crossref.org/works?query.title=The%20Erlang%20Weighted%20Tree%20A%20New%20Branching%20Process&rows=5` ? OK
- 2026-10-12 crossref_source_doi: `https://api.crossref.org/works/10.1002/rsa.21180` ? OK
- 2026-10-12 openalex_source_doi: `https://api.openalex.org/works/https://doi.org/10.1002/rsa.21180` ? HTTP Error 429: Too Many Requests
- 2026-10-12 wiley_source: `https://onlinelibrary.wiley.com/doi/10.1002/rsa.21180` ? HTTP Error 403: Forbidden
- 2026-10-12 semantic_source_doi: `https://api.semanticscholar.org/graph/v1/paper/DOI:10.1002/rsa.21180/citations?fields=title,year,externalIds&limit=100` ? OK

Remco van der Hofstad, *The giant in random graphs is almost local*, arXiv:2103.11733v3, 6 October 2025. Theorem 2.2 (PDF p.4), condition (2.9), is exactly the abstract pairwise coalescence condition used in ATTEMPT.md Section 3; the source does not verify it for the La--Kabkab model. This is a lead/reduction, not a solution of P0452. Saved almostlocal_pdf.pdf and almostlocal.txt. The preference/mutual-nearest-neighbor search returned geometric or machine-learning models, not the complete-graph IID-edge-weight bilateral model.

Crossref exact-title search identified the EWT journal version DOI 10.1002/rsa.21180. Journal-version metadata and citation searches are being checked separately. OpenAlex could not resolve a source work ID because every request was rate limited; therefore its works-citing-source traversal could not be completed. Semantic Scholar citation traversal was completed via the arXiv identifier.

EWT journal metadata verified through Crossref: *Random Structures & Algorithms* 64(3), 537-624, DOI 10.1002/rsa.21180; published online 23 October 2023. Wiley landing-page access returned HTTP 403, so the journal text itself was not inspected. Semantic Scholar citation traversal through the DOI returned the same two connectivity-paper records as the arXiv traversal. OpenAlex DOI resolution again returned HTTP 429.

Source download: 2026-10-12, https://arxiv.org/pdf/2002.03993v5 ? success. Connectivity download: https://arxiv.org/pdf/2209.05677v3 ? success. General criterion download: https://arxiv.org/pdf/2103.11733v3 ? success. None of the related/general theorems is classified as a solution in print to P0452.

Final literature classification: NOT SOLVED_IN_LITERATURE. Successful arXiv, Crossref, Semantic Scholar and GitHub searches found no theorem proving this exact fixed-distribution lower bound. OpenAlex requests were rate limited, so neither its search nor its citing-work traversal is negative evidence. Wiley journal full text was inaccessible (403). The exact source question was verified in the specified arXiv v5 PDF.

## Exact source question (Section 4, question 3, PDF p.16)

> 3. What is the connection between the probability of extinction and the proportion of vertices in
> the giant component in the finite graph model? For other random graph models (e.g. configuration
> model, Erd˝os-R´enyi model, etc.), the the proportion of vertices in the giant component converges to
> 1 −P({extinction}), where P({extinction}) is the probability the associated branching process goes
> extinct eventually. We have observed the same relation via numerical simulation in Figures 5 and 6
> between the finite graph model and the EWT. Notice that by Corollary 2.2, the the proportion
> of vertices in the giant component is bounded above by 1 −P({extinction}); however, the reverse
> inequality needs a separate proof.

2026-10-12 second attempt: read the source Appendix A.3, Theorems A.6-A.7, PDF pp.62-63. A.7 is stated for self-adjoint operators, so it was not applied to the nonsymmetric mu-density of the return process. SECOND_ATTEMPT.md Section 5 proves weighted symmetry and derives the required positive eigenfunction from the ordinary compact self-adjoint spectral theorem (A.6). Brain gap queries used: "pairwise coalescence giant component unused preference capacity collision tolerant exploration"; "Bertoin coagulation limited aggregations arms gelation"; "multitype branching process global survival partial extinction compact mean operator truncation". The last returned an escaping-type warning, not a theorem supplying the solution.

2026-10-12 second-attempt result: an original complete proof is recorded in SECOND_ATTEMPT.md. This changes the research verdict to SOLVED, not SOLVED_IN_LITERATURE. No new matching publication is claimed. The ordinary compact self-adjoint spectral theorem is used; the positive-eigenfunction and weighted-symmetry steps are proved explicitly. Temporal coagulation was considered as the alternative new approach but was not used as an unverified theorem.
