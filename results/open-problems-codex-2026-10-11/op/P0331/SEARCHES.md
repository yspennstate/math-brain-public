# Fetch/search log

* 2026-10-12 — openalex_source
  URL: https://api.openalex.org/works?search=Lectures%20on%20Coulomb%20and%20Riesz%20gases&per-page=5
  Outcome: HTTP Error 429: Too Many Requests

* 2026-10-12 — openalex
  URL: https://api.openalex.org/works?search=Coulomb%20Debye%20Poisson&per-page=30
  Outcome: HTTP Error 429: Too Many Requests

* 2026-10-12 — semantic
  URL: https://api.semanticscholar.org/graph/v1/paper/search?query=Coulomb%20Debye%20Poisson&limit=30&fields=title,authors,year,externalIds,abstract
  Outcome: HTTP Error 429: 

* 2026-10-12 — github
  URL: https://api.github.com/search/repositories?q=Coulomb%20Debye
  Outcome: ok (bytes 55)

* 2026-10-12 — arxiv
  URL: https://export.arxiv.org/api/query?search_query=all%3A%22Coulomb%22%20AND%20%28all%3A%22Debye%22%20OR%20all%3A%22Poisson%22%29&start=0&max_results=30&sortBy=submittedDate&sortOrder=descending
  Outcome: ok (bytes 63499)

* 2026-10-12 — crossref
  URL: https://api.crossref.org/works?query=Coulomb%20gas%20Debye%20Poisson&rows=30
  Outcome: ok (bytes 223071)

* 2026-10-12 — source
  URL: https://arxiv.org/pdf/2407.21194
  Outcome: ok (bytes 3188922)

* 2026-10-12 — openalex_citing
  URL: https://api.openalex.org/works?filter=cites:W4401113170&per-page=100
  Outcome: HTTP Error 429: Too Many Requests

* 2026-10-12 — openalex_retry
  URL: https://api.openalex.org/works?search=Lectures%20on%20Coulomb%20and%20Riesz%20gases&per_page=3
  Outcome: HTTP Error 429: Too Many Requests

* 2026-10-12 — semantic_source
  URL: https://api.semanticscholar.org/graph/v1/paper/ARXIV:2407.21194?fields=title,citations.title,citations.year,citations.externalIds
  Outcome: HTTP Error 429: 

* 2026-10-12 — arxiv_debye
  URL: https://export.arxiv.org/api/query?search_query=all%3A%22Debye%22%20AND%20%28all%3A%22jellium%22%20OR%20all%3A%22sharpness%22%20OR%20all%3A%22Serfaty%22%29&max_results=30
  Outcome: ok (bytes 64256)

* 2026-10-12 — arxiv_local
  URL: https://export.arxiv.org/api/query?search_query=all%3A%22Coulomb%20gas%22%20AND%20%28all%3A%22local%20laws%22%20OR%20all%3A%22high%20temperature%22%20OR%20all%3A%22Poissonian%22%29&max_results=80&sortBy=submittedDate&sortOrder=descending
  Outcome: ok (bytes 70264)

* 2026-10-12 — arxiv_poisson
  URL: https://export.arxiv.org/api/query?search_query=ti%3APoisson%20AND%20%28all%3ACoulomb%20OR%20all%3ALambert%29&max_results=25
  Outcome: ok (bytes 43104)

* 2026-10-12 — openalex_source_alt
  URL: https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2407.21194
  Outcome: HTTP Error 429: Too Many Requests

* 2026-10-12 — thoma
  URL: https://arxiv.org/pdf/2501.02733
  Outcome: ok (bytes 664690)

* 2026-10-12 — lsi
  URL: https://arxiv.org/pdf/2608.24863
  Outcome: ok (bytes 647426)

* 2026-10-12 — intermediate
  URL: https://arxiv.org/pdf/2507.08198
  Outcome: ok (bytes 616372)

* 2026-10-12 — lambert
  URL: https://arxiv.org/pdf/1912.10261
  Outcome: ok (bytes 418484)