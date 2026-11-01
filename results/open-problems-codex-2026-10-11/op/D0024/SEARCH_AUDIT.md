# Complete HTTP query audit — 2026-10-11

Source PDF and convergence PDF were fetched separately; see LITERATURE.md. All queries below retain exact URLs.

- Service: arxiv; date: 2026-10-11
  - URL: http://export.arxiv.org/api/query?search_query=all%3A%22disordered%22%20AND%20all%3A%22zero-range%22&max_results=40
  - Outcome: 200; bytes: 67583

- Service: arxiv_https; date: 2026-10-11
  - URL: https://export.arxiv.org/api/query?search_query=all%3A%22zero-range%22%20AND%20all%3A%22convergence%22&max_results=40
  - Outcome: 200; bytes: 73578

- Service: openalex; date: 2026-10-11
  - URL: https://api.openalex.org/works?search=disordered%20zero%20range%20convergence%20equilibrium&per-page=30
  - Outcome: HTTP Error 429: Too Many Requests; bytes: not saved

- Service: openalex_source; date: 2026-10-11
  - URL: https://api.openalex.org/works?search=Recent%20results%20and%20open%20problems%20on%20the%20hydrodynamics%20of%20disordered%20asymmetric%20exclusion%20and%20zero-range%20processes&per-page=5
  - Outcome: HTTP Error 429: Too Many Requests; bytes: not saved

- Service: crossref; date: 2026-10-11
  - URL: https://api.crossref.org/works?query=disordered%20zero%20range%20convergence%20equilibrium&rows=30
  - Outcome: 200; bytes: 238411

- Service: semantic; date: 2026-10-11
  - URL: https://api.semanticscholar.org/graph/v1/paper/search?query=disordered%20zero%20range%20convergence&limit=30&fields=title,authors,year,externalIds,url,abstract
  - Outcome: HTTP Error 429: ; bytes: not saved

- Service: github; date: 2026-10-11
  - URL: https://api.github.com/search/repositories?q=disordered%20zero%20range&per_page=20
  - Outcome: 200; bytes: 17645

- Service: openalex_retry; date: 2026-10-11
  - URL: https://api.openalex.org/works?search=quenched%20convergence%20zero-range&per-page=10
  - Outcome: HTTP Error 429: Too Many Requests; bytes: not saved

- Service: semantic_bulk; date: 2026-10-11
  - URL: https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=disordered%20zero%20range&fields=title,authors,year,externalIds,url
  - Outcome: 200; bytes: 586922

- Service: openalex_source_retry; date: 2026-10-11
  - URL: https://api.openalex.org/works?filter=title.search:Recent%20Results%20and%20Open%20Problems%20on%20the%20Hydrodynamics&per-page=5
  - Outcome: HTTP Error 429: Too Many Requests; bytes: not saved

- Service: math_9911205; date: 2026-10-11
  - URL: https://arxiv.org/pdf/math/9911205
  - Outcome: 200; bytes: 176364

- Service: math_0609469; date: 2026-10-11
  - URL: https://arxiv.org/pdf/math/0609469
  - Outcome: 200; bytes: 216248

- Service: 1411.4305; date: 2026-10-11
  - URL: https://arxiv.org/pdf/1411.4305
  - Outcome: 200; bytes: 520962

- Service: 1411.4318; date: 2026-10-11
  - URL: https://arxiv.org/pdf/1411.4318
  - Outcome: 200; bytes: 268511

- Service: crossref_source; date: 2026-10-11
  - URL: https://api.crossref.org/works?query.title=Recent%20results%20and%20open%20problems%20on%20the%20hydrodynamics%20of%20disordered%20asymmetric%20exclusion%20and%20zero-range%20processes&rows=5
  - Outcome: 200; bytes: 45034

- Service: openalex_citations_attempt; date: 2026-10-11
  - URL: https://api.openalex.org/works?filter=cites:arxiv:math/9906194&per-page=50
  - Outcome: HTTP Error 429: Too Many Requests; bytes: not saved

- Service: arxiv_metadata; date: 2026-10-11
  - URL: https://export.arxiv.org/api/query?id_list=math/9911205,math/0609469,1411.4305,1411.4318,1804.06148,1801.01654
  - Outcome: 200; bytes: 11283

- Service: semantic_source; date: 2026-10-11
  - URL: https://api.semanticscholar.org/graph/v1/paper/ARXIV:math/9906194?fields=title,year,externalIds,citations.title,citations.year,citations.externalIds
  - Outcome: 200; bytes: 278

- Service: openalex_source_identifier; date: 2026-10-11
  - URL: https://api.openalex.org/works/arxiv:math/9906194
  - Outcome: HTTP Error 429: Too Many Requests; bytes: not saved

