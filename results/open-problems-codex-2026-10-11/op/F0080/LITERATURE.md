# F0080 literature verification ? 2026-10-11

1. Russell Lyons, Yuval Peres, and Oded Schramm, **Minimal spanning forests**, *Annals of Probability* **34** (2006), no. 5, 1665?1692. DOI: 10.1214/009117906000000269. arXiv:math/0412263v5. Question 6.13 is on PDF p. 27. Local primary source: source_pdf.pdf; extracted text: source.txt.
2. Andreas Thom, **The expected degree of minimal spanning forests**, *Combinatorica* **36** (2016), no. 5, 591?600. DOI: 10.1007/s00493-014-3160-x. arXiv:1306.0303v1 (3 June 2013). Theorem 1 and Corollary 2, PDF pp. 2?3. The corollary explicitly identifies Question 6.13 as answered. The corollary uses generating MULTISETS. Crossref independently confirms author, journal, volume, issue, pages and DOI. Local source: thom_pdf.pdf and thom.txt.
3. Andreas Thom, **A remark about the spectral radius**, *International Mathematics Research Notices*, DOI: 10.1093/imrn/rnu018 (Crossref gives online publication 2 March 2014). arXiv:1306.1767v1 (7 June 2013). Theorem 1, PDF p. 2, and Corollary 9, PDF p. 5. Corollary 9 explicitly gives unbounded FMSF degree over ordinary finite symmetric generating SETS. Local source: spectral_pdf.pdf and spectral.txt. The retrieved Crossref record omits final issue/pagination; those are not guessed here.

## Every online request/search

- 2026-10-11 | source_pdf | OK
  URL/query: https://arxiv.org/pdf/math/0412263

- 2026-10-11 | openalex_search | ERROR
  URL/query: https://api.openalex.org/works?search=expected%20degree%20minimal%20spanning%20forests&per-page=15
  Error: HTTP Error 429: Too Many Requests

- 2026-10-11 | crossref_search | OK
  URL/query: https://api.crossref.org/works?query=expected%20degree%20minimal%20spanning%20forests&rows=10

- 2026-10-11 | arxiv_search | OK
  URL/query: https://export.arxiv.org/api/query?search_query=all%3A%22minimal%20spanning%20forests%22%20AND%20all%3A%22degree%22&max_results=20

- 2026-10-11 | semantic_search | ERROR
  URL/query: https://api.semanticscholar.org/graph/v1/paper/search?query=expected%20degree%20minimal%20spanning%20forests&limit=10&fields=title,authors,year,url,externalIds,abstract
  Error: HTTP Error 429: 

- 2026-10-11 | github_search | OK
  URL/query: https://api.github.com/search/repositories?q=minimal%20spanning%20forest%20expected%20degree

- 2026-10-11 | thom_pdf | OK
  URL/query: https://arxiv.org/pdf/1306.0303

- 2026-10-11 | thom_crossref | OK
  URL/query: https://api.crossref.org/works/10.1007/s00493-014-3160-x

- 2026-10-11 | openalex_source | ERROR
  URL/query: https://api.openalex.org/works/https://doi.org/10.1214/009117906000000269
  Error: HTTP Error 429: Too Many Requests

- 2026-10-11 | openalex_thom | ERROR
  URL/query: https://api.openalex.org/works/https://doi.org/10.1007/s00493-014-3160-x
  Error: HTTP Error 429: Too Many Requests

- 2026-10-11 | semantic_source | OK
  URL/query: https://api.semanticscholar.org/graph/v1/paper/DOI:10.1214/009117906000000269?fields=title,citations.title,citations.year,citations.externalIds

- 2026-10-11 | arxiv_http | OK
  URL/query: http://export.arxiv.org/api/query?search_query=ti%3A%22The%20expected%20degree%20of%20minimal%20spanning%20forests%22&max_results=5

- 2026-10-11 | spectral_pdf | OK
  URL/query: https://arxiv.org/pdf/1306.1767

- 2026-10-11 | spectral_crossref | OK
  URL/query: https://api.crossref.org/works/10.1093/imrn/rnu018

- 2026-10-11 | openalex_citing_source | ERROR
  URL/query: https://api.openalex.org/works?filter=cites%3Adoi%3A10.1214/009117906000000269&per-page=100
  Error: HTTP Error 429: Too Many Requests

- 2026-10-11 | openalex_source_filter | ERROR
  URL/query: https://api.openalex.org/works?filter=doi%3Ahttps%3A//doi.org/10.1214/009117906000000269&per-page=1
  Error: HTTP Error 429: Too Many Requests

## Search limitations and citation verification

OpenAlex search and DOI lookups returned HTTP 429. The source could not be resolved to an OpenAlex work ID, so no usable OpenAlex citing-works list was obtained. The attempted DOI-form citing filter also returned 429 before its validity could be checked; it is not treated as a successful citation search. Semantic Scholar keyword search returned 429, but its DOI-specific source lookup succeeded and returned 95 citing records, including Thom's paper (both arXiv and journal records). GitHub returned zero repositories for the stated query; that has no bearing on mathematical status. Both requested HTTP and HTTPS arXiv API routes succeeded.

Raw responses and logs are preserved in search_log.json, search_followup.json, search_scope.json and the named API response files. No built-in web-search tools were used.

## Read-only research-brain and earlier-work searches

- math_recall.py query: "Timar minimal spanning forest expected degree generating set spectral radius". Results were hints, with no relevant solution supplied.
- brain.py recall: "minimal spanning forest expected degree" and "minimal spanning forest mistakes". Recall warned about adjacent-object errors in prior MSF work; no conclusion was imported.
- rg search for F0080 in probability_1000_intake_* and codex_pool_2026_10_10. The first PowerShell wildcard path was rejected by rg; retried with Python-expanded directory names. Recovered F0080-A001 and the original problem row in probability_1000_intake_F_20260908. Their status was unverified and the attempted reduction did not settle the problem.
- Read-only git ls-tree of origin/master in math-open-problems, then git show origin/master:operations/claims/F0080.md. This 2026-09-17 record missed the 2013 literature and proposed another attempt. Its search miss is superseded by the fetched primary papers; no repository files were changed.
