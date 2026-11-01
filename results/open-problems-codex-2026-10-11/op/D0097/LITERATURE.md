# D0097 literature audit — 2026-10-12

## Verified source

Leonardo T. Rolla, *Activated Random Walks on Z^d*, Probability Surveys 17 (2020), 478–544, DOI 10.1214/19-PS339, arXiv:1906.05037v2 (28 September 2020). Downloaded https://arxiv.org/pdf/1906.05037 into source.pdf; extracted text in source.txt.

PDF page 35, printed page 512:

> Theorem 7.2. If d > 2, then ζc < 1 for every λ < ∞ and ζc → 0 as λ → 0.
>
> Open Problem. Prove a similar statement for unbiased walks on Z2.

Section 1.1, PDF page 3: continuous-time jump rate 1, translation-invariant nearest-neighbour jump distribution p supported on ±e_i, whose support spans Z^d. Sleep rate 0 < λ ≤ ∞; sleep attempts only succeed when the particle is alone. Section 1.2–1.3: infinite-volume conservative ARW; translation-ergodic initially active configurations, with Poisson initial counts as the standard definition of the threshold. The threshold is independent of the initially active ergodic law of a given density. For a nearest-neighbour zero-drift kernel on Z², p(e_i)=p(-e_i), but the two coordinate weights need not be equal.

## Search log (results retained in *.response and search_log.jsonl)

All searches below were run on 2026-10-12, using Python requests from the shell, without built-in web search.

- arXiv API, `http://export.arxiv.org/api/query?search_query=all:%22activated%20random%20walks%22&start=0&max_results=60&sortBy=submittedDate&sortOrder=descending`: HTTP 429.
- OpenAlex works search, `https://api.openalex.org/works?search=activated%20random%20walks%20critical%20density&per-page=40`: HTTP 429 (shared unauthenticated daily budget exhausted).
- Crossref, `https://api.crossref.org/works?query=activated%20random%20walks%20critical%20density&rows=30`: HTTP 200, matching papers below.
- Semantic Scholar, `https://api.semanticscholar.org/graph/v1/paper/search?query=activated%20random%20walks%20critical%20density&limit=30&fields=title,authors,year,abstract,externalIds,url`: HTTP 429.
- GitHub repositories, `https://api.github.com/search/repositories?q=activated+random+walks&per_page=20`: HTTP 200, five repositories; no theorem certificate from repository search.
- Follow-up arXiv HTTPS API, title query `ti:"activated random walks"`, max_results=60: TLS EOF failure.
- OpenAlex source DOI lookup `https://api.openalex.org/works/https://doi.org/10.1214/19-PS339`: TLS EOF failure.
- OpenAlex provisional citation query `filter=cites:W2995486210&per-page=100`: TLS EOF failure; the identifier has NOT been verified; this query does not establish coverage of works citing the source.
- OpenAlex DOI-filter follow-up `https://api.openalex.org/works?filter=doi:https://doi.org/10.1214/19-PS339`: request underway.
- Crossref title query `Diffusive bounds for the critical density of activated random walks`, rows=3: HTTP 429.
- Crossref title query `activated random walks small sleeping rate`, rows=15: HTTP 200; response retained.

## Relevant leads, not yet theorem certificates

- Amine Asselah, Nicolas Forien and Alexandre Gaudillière, *The critical density for activated random walks is always less than 1*, Annals of Probability 52(5) (2024), 1607–1649, DOI 10.1214/23-AOP1674. Abstract explicitly states simple random walk, all dimensions, all finite sleep rates, and small-rate upper bounds. Full statement and kernel scope still to be checked.
- Amine Asselah, Leonardo T. Rolla and Bruno Schapira, *Diffusive bounds for the critical density of activated random walks*, ALEA 19 (2022), 457–465, DOI 10.30757/alea.v19-17, arXiv:1907.12694. Download requested from https://alea.impa.br/articles/v19/19-17.pdf.
- Y. Hu, *Active Phase for Activated Random Walk on Z²*, arXiv:2203.14406 (2022), cited in the published Asselah–Forien–Gaudillière article. Download requested.
- Nicolas Forien and Alexandre Gaudillière, *Active phase for activated random walks on the lattice in all dimensions*, Annales de l'Institut Henri Poincaré, Probabilités et Statistiques 60 (2024), 1188–1214, DOI 10.1214/22-AIHP1341. Identified in AFG references.
- Alexandre Stauffer and Lorenzo Taggi, *Critical density of activated random walks on transitive graphs*, Annals of Probability 46(4) (2018), 2190–2220, DOI 10.1214/17-AOP1224. Transient-graph small-sleep limit; not a recurrent Z² result.
- Lorenzo Taggi, *Active phase for activated random walks on Z^d, d≥3, with density less than one and arbitrary sleeping rate*, AIHP 55 (2019), 1751–1764, DOI 10.1214/18-AIHP933. Transient scope only.
- arXiv:2512.00720, title reported by the earlier ledger as *Asymptotic behavior of the critical density of activated random walk*. Identity and scope not yet checked; download requested.

## Read-only brain and prior work

Read `brain.py recall "activated random walks critical density"`, `brain.py recall "activated random walks mistakes"`, and `math_recall.py "activated random walks small sleep critical density"`. No matching verified theorem was returned. Relevant warning: a source's open-problem label can survive a later solution; inspect full theorem statements.

Searched intake directories and codex_pool_2026_10_10 with rg for D0097. The September intake says the strict-below-one half is resolved and conjectures a truncated-Green-function small-rate bound; that conjecture is not a proved result. The earlier attempt also confuses this problem with an odometer moment question in another entry; those labels must not be used as evidence.

Read-only `git ls-tree -r --name-only origin/master` in ~/math-open-problems found no path containing D0097/d0097; no working-tree writes were made.
