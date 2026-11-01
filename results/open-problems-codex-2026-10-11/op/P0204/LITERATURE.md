# P0204 literature audit — 2026-10-11

All network retrievals used Python urllib from the shell, not built-in web search. URLs below are the actual queries; corresponding raw responses are retained when retrieval succeeded. Source verification and broad searches preceded mathematical experiments. The decisive September result was discovered by the exact phrase query rather than the broader hypercube query.

## Exact relevant references and conclusions

1. **Decisive solution:** Yiming Chen, with an appendix by Yuval Peres (arXiv metadata lists Yiming Chen and Yuval Peres), *Mixing time under monotone censoring*, arXiv:2609.16515v2, first submitted 15 September 2026, revised 19 September 2026. https://arxiv.org/abs/2609.16515v2 . Theorem 1.2: for every nonempty increasing A, the censored lazy coordinate walk Q satisfies t_mix(Q,1/4)<=K mu_cube(A)^(-3) n log(en), and t_H^Q(1/4)<=6148 mu_cube(A)^(-3) n log(en). Corollary 1.3 gives O_c(n log n) for density >=c. Equation (1.1) fixes the kernel and uniform stationary law. This directly resolves Ding–Mossel's censored-walk conjecture; ATTEMPT.md section 4 rigorously transfers it to the user-specified degree-weighted induced walk. Public arXiv preprint, not a verified journal publication. Raw full HTML: arxiv_september_html.txt; metadata: entry in arxiv_exact.txt.

2. Jian Ding and Elchanan Mossel, *Mixing under monotone censoring*, Electronic Communications in Probability **19** (2014), 1–6, DOI https://doi.org/10.1214/ECP.v19-3157 ; arXiv:1311.5945v2. Corollary 1.2 gives a polynomial O(n^3) bound at constant density. Question 1.1 asks O_c(n log n), explicitly for the uniform-stationary censored walk. Verified from full HTML and Crossref metadata.

3. Yumou Fei and Renato Ferreira Pinto Jr., *On the Spectral Expansion of Monotone Subsets of the Hypercube*, APPROX/RANDOM 2025, LIPIcs **353**, Article 42, 24 pages; arXiv:2505.02685v2 (3 July 2026). Theorem 1.6 proves gap(Q)>=(1-sqrt(1-a))/n and Theorem 1.4 gives O(n^2) mixing at fixed density. Section 1.5 explicitly leaves the sharp mixing bound open. Conference reference is also listed in Oliveira Santos–Tripathi–Youssef's bibliography.

4. Fan Chang, Guowei Sun, and Lei Yu, *Functional inequalities and random walks on increasing subsets of the hypercube*, arXiv:2506.09852v4 (11 August 2026), first submitted 11 June 2025. Metadata says accepted for publication in SIAM Journal on Discrete Mathematics; no volume/pages/DOI verified. Theorem 2 reproves the Poincare bound with a factor-two loss; still O(n^2) censored mixing. Earlier versions had the title *Poincare inequality on the monotone sets revisited*.

5. Patrick Oliveira Santos, Raghavendra Tripathi, and Pierre Youssef, *Log-Sobolev under random monotone censoring*, arXiv:2606.09221v1 (8 June 2026). Theorem 1.1 proves a classical log-Sobolev constant of order n for uniformly random monotone sets, hence typical O(n log n) mixing. Theorem 3.1 treats Hamming caps; Proposition 5.1 gives worst-case order n^2 log-Sobolev constants even at density >=1/2. Remark 5.2 explicitly says these are not counterexamples to TV mixing. This is a partial precursor, not the decisive universal solution.

6. Yuval Peres and Perla Sousi, *Mixing times are hitting times of large sets*, Journal of Theoretical Probability **28** (2015), 488–519; arXiv:1108.0133v3 (27 April 2013). Theorem 1.1 compares the mixing time of the lazy version of any finite irreducible reversible chain with worst-case expected hitting times of stationary-large sets, for fixed alpha in (0,1/2). Full HTML theorem verified. This theorem closes the induced-walk transfer; also quoted as Theorem 2.3 in Chen–Peres.

7. Yuval Peres, *Markov chains and mixing times*, book-companion webpage, Related open problems, Question 1, https://www.yuval-peres-books.com/markov-chains-and-mixing-times/ , fetched 11 October 2026. Exact substance: V is coordinatewise increasing, has at least half the cube's vertices; asks best mixing bound for lazy simple random walk on V; cites Ding–Mossel O(n^3) and conjectures O(n log n). The live page has not incorporated the September resolution. The chain wording differs from the cited paper's explicit censored kernel, which is why a transfer is needed.

## Discovery limitations and read-only local searches

- OpenAlex broad search, title search, and DOI lookup returned HTTP 429. No OpenAlex work identifier could be recovered, so a valid ID-based citing-works query could not be completed. An attempted DOI-based cites filter also returned 429; OpenAlex normally requires its work ID for this filter, so that attempt supplies no citation evidence. This limitation does not affect the full-text verification of the decisive paper.
- Semantic Scholar broad paper search and the valid ARXIV:1311.5945 citations endpoint returned HTTP 429.
- GitHub repository searches for `monotone hypercube mixing` and `"monotone censoring"` succeeded, both with total_count=0. They are not evidence of absence of literature.
- Initial arXiv broad query returned 40 entries and was not exhaustive. A second hypercube/monotone query returned 70 entries. The exact `all:"monotone censoring"` query returned three entries, including the decisive September paper absent from the truncated broad searches. Each relevant paper was then fetched in full HTML.
- Read-only math-store recall: `monotone hypercube Ding Mossel mixing`; `log Sobolev monotone censoring Fei Pinto`. Read-only brain recall: `monotone hypercube mixing mistakes`; `Mixing on large monotone subsets of the hypercube`. These supplied earlier unsolved records and warnings about stationary-law conventions, not certified status.
- Read-only local rg search for P0204 in the math-research ledgers, then all probability_1000_intake_* directories and codex_pool_2026_10_10; earlier records were attempted-unsolved. Read-only `git ls-tree origin/master` name filtering for P0204/p0204/monotone-cube-or-mixing paths found no matching paths. No git working tree was modified.

## Actual network query log

- 2026-10-11 | source | https://www.yuval-peres-books.com/markov-chains-and-mixing-times/ | OK; raw response: source.txt

- 2026-10-11 | arxiv | https://export.arxiv.org/api/query?search_query=all%3Amonotone%20AND%20%28all%3Amixing%20OR%20all%3Awalk%29&max_results=40 | OK; raw response: arxiv.txt

- 2026-10-11 | openalex | https://api.openalex.org/works?search=monotone%20subsets%20hypercube%20mixing&per-page=20 | HTTP Error 429: Too Many Requests; raw response: openalex.txt

- 2026-10-11 | crossref | https://api.crossref.org/works?query=Ding%20Mossel%20monotone%20mixing%20hypercube&rows=15 | OK; raw response: crossref.txt

- 2026-10-11 | semantic | https://api.semanticscholar.org/graph/v1/paper/search?query=monotone%20hypercube%20mixing&limit=20&fields=title,authors,year,externalIds,url,abstract | HTTP Error 429: ; raw response: semantic.txt

- 2026-10-11 | github | https://api.github.com/search/repositories?q=monotone%20hypercube%20mixing | OK; raw response: github.txt

- 2026-10-11 | arxiv_target | https://export.arxiv.org/api/query?search_query=all%3Ahypercube%20AND%20%28all%3Amonotone%20OR%20all%3Acensoring%29&max_results=70&sortBy=submittedDate&sortOrder=descending | OK; raw response: arxiv_target.txt

- 2026-10-11 | arxiv_fei_html | https://arxiv.org/html/2505.02685v2 | OK; raw response: arxiv_fei_html.txt

- 2026-10-11 | arxiv_santos_html | https://arxiv.org/html/2606.09221v1 | OK; raw response: arxiv_santos_html.txt

- 2026-10-11 | arxiv_ding_html | https://arxiv.org/html/1311.5945v2 | OK; raw response: arxiv_ding_html.txt

- 2026-10-11 | openalex_doi | https://api.openalex.org/works/https://doi.org/10.1214/ECP.v19-3157 | HTTP Error 429: Too Many Requests; raw response: openalex_doi.txt

- 2026-10-11 | openalex_retry | https://api.openalex.org/works?search=Mixing%20under%20monotone%20censoring&per_page=10 | HTTP Error 429: Too Many Requests; raw response: openalex_retry.txt

- 2026-10-11 | semantic_citations | https://api.semanticscholar.org/graph/v1/paper/ARXIV:1311.5945/citations?fields=title,authors,year,externalIds&limit=100 | HTTP Error 429: ; raw response: semantic_citations.txt

- 2026-10-11 | crossref_new | https://api.crossref.org/works?query=spectral%20expansion%20monotone%20subsets%20hypercube&rows=12 | OK; raw response: crossref_new.txt

- 2026-10-11 | github_broad | https://api.github.com/search/repositories?q=%22monotone%20censoring%22 | OK; raw response: github_broad.txt

- 2026-10-11 | arxiv_csy_html | https://arxiv.org/html/2506.09852v4 | OK; raw response: arxiv_csy_html.txt

- 2026-10-11 | arxiv_csy_metadata | https://export.arxiv.org/api/query?id_list=2506.09852 | OK; raw response: arxiv_csy_metadata.txt

- 2026-10-11 | arxiv_exact | https://export.arxiv.org/api/query?search_query=all%3A%22monotone%20censoring%22&max_results=50 | OK; raw response: arxiv_exact.txt

- 2026-10-11 | crossref_ding | https://api.crossref.org/works/10.1214/ECP.v19-3157 | OK; raw response: crossref_ding.txt

- 2026-10-11 | openalex_citations | https://api.openalex.org/works?filter=cites:doi:10.1214/ECP.v19-3157&per-page=100 | HTTP Error 429: Too Many Requests; raw response: openalex_citations.txt

- 2026-10-11 | arXiv | https://export.arxiv.org/api/query?search_query=ti:%22Mixing%20times%20are%20hitting%20times%20of%20large%20sets%22&max_results=5 | OK; peres_sousi_metadata.txt

- 2026-10-11 | arXiv HTML | https://arxiv.org/html/1108.0133v3 | OK; peres_sousi_html.txt

- 2026-10-11 | arXiv HTML | https://arxiv.org/html/2609.16515v2 | OK; arxiv_september_html.txt
