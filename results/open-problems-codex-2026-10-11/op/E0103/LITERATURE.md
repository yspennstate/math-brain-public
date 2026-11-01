# Literature status — E0103

Search date: 2026-10-11. No matching published solution was identified. This is a bounded search, not a proof of absence; OpenAlex was rate-limited throughout. No SOLVED_IN_LITERATURE verdict is warranted.

## Source verification

Takis Konstantopoulos, *The mobile Boolean model: an overview and further results*, arXiv:1407.6834v1, 25 July 2014, 19 pages. https://arxiv.org/abs/1407.6834 . Source PDF saved as source_pdf.pdf and page-tagged extraction as source.txt.

PDF p.18, Open problem 1, verbatim prose (mathematical notation normalized from the PDF):

> We did not touch at all the coverage problem, i.e., the law of the random variable inf{t ≥ 0 : K ⊂ W(t)}. For the Brownian Boolean model, and when the diameter of R tends to infinity, the problem has been solved in [12]. What are the corresponding asymptotics for the inertial cases?

It says R, not K, in the diameter sentence. Page 4 defines cumulative W(t); page 5 specializes to homogeneous Poisson germs; pp.8–9 specify straight-line independent velocities. The open question itself gives no velocity-tail assumption or target-scaling prescription. Its surrounding ball calculation uses finite mean speed. The cylinder coefficient in equations (14)?(15) is incorrect; see ATTEMPT.md §1 for a direct derivation of the correct coefficient.

## Papers and why they do not settle this question

1. Yuval Peres, Alistair Sinclair, Perla Sousi and Alexandre Stauffer, *Mobile Geometric Graphs: Detection, Coverage and Percolation*, arXiv:1008.0075v2 (2010/2011); Probability Theory and Related Fields **156**, 273–305 (2013); earlier SODA 2011, 412–428. The source spells the final author's given name Alexander. Our downloaded PDF is saved as brownian_pdf.pdf. Theorem 1.4 (PDF p.3) gives expected cube coverage asymptotics and concentration for independent **Brownian** motions. Theorem 4.2 (PDF p.10) treats scaled bounded targets with a Minkowski dimension. This is precisely the Brownian precedent cited in the source, and not an inertial theorem. Its packing/net strategy is useful.

2. Hanna Döring, Lianne de Jonge and Xiaochuan Yang, *Coverage of the unit cube by dynamic Boolean models*, arXiv:2506.22286v1, 27 June 2025, 19 pages. https://arxiv.org/abs/2506.22286 . Saved as dynamic2025.pdf. Theorem 1.1 (PDF p.4) gives a law of large numbers for the coverage **radius**, of order (log ρ/ρ)^(1/(d−1)), for cylinders based on a Poisson number of lines through the cube's (d−1)-dimensional base, with uniform directions. Theorem 1.3 (p.5) bounds that scale for other directional laws. The model definitions are on pp.3–4. This has: (i) initial germs restricted to a base face; (ii) a space-time unit cube to be covered; (iii) varying radius and intensity, not cumulative spatial coverage by finite ballistic segments with fixed radius. It is a lead, not a solution with the same objects, hypotheses and quantifiers.

3. Erik I. Broman and Filipe Mussini, *Random cover times using the Poisson cylinder process*, arXiv:1709.04378v2, 16 October 2018; ALEA, Latin American Journal of Probability and Mathematical Statistics **16**, 1165–1199 (2019). https://arxiv.org/abs/1709.04378 . Saved as cylinder2019.pdf. Theorem 1.1 (PDF pp.2–3) proves tightness after centering T(nA) by dim_B(A)(log n+log log n), subject to a Minkowski-content condition. Theorem 1.2 (p.3) gives Gumbel convergence for growing finite sets satisfying a separation hypothesis. Its process (pp.2,5) has infinite cylinders arriving with independent Poisson time stamps; it does not extend finite trajectories of germs that were all present at time zero. Useful geometric dependence estimates; not the inertial mobile Boolean model.

4. Nils Aschenbruck, Stephan Bussmann and Hanna Döring, *Asymptotics of a time bounded cylinder model*, Probability in the Engineering and Informational Sciences **37**(4), 1063–1083, online 27 December 2022. DOI: 10.1017/S0269964822000420. Crossref metadata/abstract saved in crossref_aschenbruck.txt. The abstract states central limit theorems for volume, isolated-cylinder counts and Euler characteristic in a fixed-time space-time model. It does not state a coverage-time theorem. Full text was not audited, so this is an abstract-level lead only.

5. Harrison Hartle and Naoki Masuda, *Autocorrelation properties of temporal networks governed by dynamic node variables*, arXiv:2408.16270 (30 August 2024); Physical Review Research **7**, 013083 (2025), DOI: 10.1103/PhysRevResearch.7.013083. This is the sole citation returned by the successful Semantic Scholar source-citations request (no next-page token). PDF saved as arxiv_temporal_pdf.pdf. It concerns temporal edge autocorrelation, not complete coverage times. No matching theorem was identified in its title/abstract/model discussion; no claim of exhaustive theorem auditing is made.

6. Svante Janson, *Random coverings in several dimensions*, Acta Mathematica **156**, 83–118 (1986). Static/random-arrival coverage precedent, encountered in the 2025 and 2019 papers' references. Not fetched or claimed as a direct solution: our capsule lengths change with observation time.

The broad ballistic/coverage and Crossref keyword searches returned mostly unrelated wireless signal-coverage and deposition papers. Their raw responses are preserved. Such signal coverage means SINR coverage, not containment of a region in a swept random set.

## Every online request/search

Each URL below gives the exact service query. Raw responses with the corresponding service name are saved in this folder; search_log.json records statuses. Empty or blocked results are not evidence that a solution does not exist.

- 2026-10-11 — source_pdf — HTTP 200 — https://arxiv.org/pdf/1407.6834
- 2026-10-11 — arxiv — HTTP 200 — https://export.arxiv.org/api/query?search_query=all:%22inertial%22+AND+all:%22Boolean%22&max_results=30
- 2026-10-11 — openalex — HTTP 429 — https://api.openalex.org/works?search=coverage%20inertial%20Boolean%20model&per-page=30
- 2026-10-11 — source_meta — HTTP 429 — https://api.openalex.org/works?filter=locations.source.id:s4306400194&search=The%20mobile%20Boolean%20model&per-page=5
- 2026-10-11 — crossref — HTTP 200 — https://api.crossref.org/works?query=coverage%20inertial%20Boolean%20model&rows=20
- 2026-10-11 — semanticscholar — HTTP 429 — https://api.semanticscholar.org/graph/v1/paper/ARXIV:1407.6834?fields=title,authors,year,citations.title,citations.year,citations.externalIds
- 2026-10-11 — github — HTTP 200 — https://api.github.com/search/repositories?q=inertial+Boolean+coverage
- 2026-10-11 — openalex_source — HTTP 429 — https://api.openalex.org/works?search=The%20mobile%20Boolean%20model%20an%20overview%20and%20further%20results&per-page=5
- 2026-10-11 — arxiv_mobile — HTTP 200 — https://export.arxiv.org/api/query?search_query=all:%22mobile%20Boolean%22&max_results=50
- 2026-10-11 — arxiv_ballistic — HTTP 200 — https://export.arxiv.org/api/query?search_query=all:%22ballistic%22+AND+all:%22coverage%22&max_results=40
- 2026-10-11 — arxiv_brownian — HTTP 200 — https://export.arxiv.org/api/query?search_query=ti:%22Mobile%20Geometric%20Graphs%22&max_results=10
- 2026-10-11 — crossref_source — HTTP 200 — https://api.crossref.org/works?query.title=The%20mobile%20Boolean%20model%20an%20overview%20and%20further%20results&rows=5
- 2026-10-11 — crossref_mobile — HTTP 200 — https://api.crossref.org/works?query=mobile%20Boolean%20coverage&rows=30
- 2026-10-11 — openalex_exact — HTTP 429 — https://api.openalex.org/works?filter=title.search:mobile%20Boolean&per_page=10
- 2026-10-11 — s2_search — HTTP 429 — https://api.semanticscholar.org/graph/v1/paper/search?query=inertial%20Boolean%20coverage&limit=20&fields=title,year,url,abstract
- 2026-10-11 — brownian_pdf — HTTP 200 — https://arxiv.org/pdf/1008.0075
- 2026-10-11 — s2_citations — HTTP 200 — https://api.semanticscholar.org/graph/v1/paper/ARXIV:1407.6834/citations?fields=title,year,externalIds&limit=1000
- 2026-10-11 — openalex_resolve_arxiv — HTTP 429 — https://api.openalex.org/works?filter=locations.landing_page_url:https%3A%2F%2Farxiv.org%2Fabs%2F1407.6834&per-page=5
- 2026-10-11 — openalex_citing_attempt — HTTP 429 — https://api.openalex.org/works?filter=cites:arxiv:1407.6834&per-page=100
- 2026-10-11 — arxiv_straight — HTTP 200 — https://export.arxiv.org/api/query?search_query=all:%22coverage%22+AND+(all:%22Poisson%22+AND+all:%22motion%22)&max_results=60
- 2026-10-11 — github_mobile — HTTP 403 — https://api.github.com/search/repositories?q=%22mobile+Boolean%22
- 2026-10-11 — crossref_ballistic — HTTP 200 — https://api.crossref.org/works?query=ballistic%20Poisson%20coverage%20time&rows=20
- 2026-10-11 — arxiv_related_pdf — HTTP 200 — https://arxiv.org/pdf/2506.22286
- 2026-10-11 — arxiv_cylinders — HTTP 200 — https://export.arxiv.org/api/query?search_query=ti:%22Random%20cover%20times%22&max_results=10
- 2026-10-11 — arxiv_temporal_pdf — HTTP 200 — https://arxiv.org/pdf/2408.16270
- 2026-10-11 — crossref_aschenbruck — HTTP 200 — https://api.crossref.org/works?query.title=Asymptotics%20of%20a%20time%20bounded%20cylinder%20model&rows=3
- 2026-10-11 — arxiv_cylinder_pdf — HTTP 200 — https://arxiv.org/pdf/1709.04378

The OpenAlex source-resolution and citation requests all returned HTTP 429, citing exhaustion of the shared unauthenticated daily budget. An attempted cites:arxiv:1407.6834 filter is not a resolved OpenAlex work-ID citation query; because source resolution failed, the proper cites:<resolved OpenAlex work ID> workflow could not be completed. This is explicitly an incomplete citation search, not a negative result. Semantic Scholar metadata/search initially returned 429, but its separate citations endpoint later returned 200 and one paper. GitHub's first query returned zero repositories; the second returned 403. No credentials, API keys, or restricted files were accessed.

## Read-only local research searches

- math_recall.py "mobile Boolean coverage inertial"; walked claim_581c9552f43e1f4cf92726d32a39b9a4720c921de8094cf33857ac37ef5fce39 with --id.
- brain.py recall "inertial Boolean coverage mistakes" and "inertial Boolean coverage".
- rg E0103 in probability_1000_intake_* ledgers and codex_pool_2026_10_10. Initial literal wildcard path failed under PowerShell; directory enumeration followed by rg succeeded. E0103-A001 in intake_E_20260908 had a point-law heuristic, no coverage proof, and an incorrect claim about infinite mean speeds growing superlinearly. The present attempt corrects that issue.
- git ls-tree of origin/master in the read-only math-open-problems checkout, filtered for E0103, inertial and mobile-Boolean names. It exposed adjacent E0105 reports but no named E0103 result. No repository was modified, and this filename-only scan is not an exhaustive content search.

Brain cards were treated as hints. In particular their warning that a two-set void reduction is not a coverage solution was observed: ATTEMPT.md supplies the geometric covariance estimate and resulting probability bounds rather than stopping at the reduction.

## Second-attempt gap-directed recall and searches

Date: 2026-10-11.

- math_recall.py "Boolean interval coverage clump M/G/infinity busy period Gumbel Poisson approximation". General Poisson approximation, Le Cam, extreme-value and Last-Penrose cards; no matching coverage theorem.
- brain.py recall "one dimensional Boolean coverage random interval lengths Gumbel mistakes". Mostly off-target hits plus adjacent inertial detection memory; none used as a verdict.
- math_recall.py "Hall coverage processes Poisson clumps random intervals M/G infinity busy period". General stochastic geometry and Poisson mapping/Mecke cards; no specific busy-period theorem was supplied. The argument was derived and checked directly.
- 2026-10-11 - second_arxiv_intervals - HTTP 200 - https://export.arxiv.org/api/query?search_query=all:%22random%20intervals%22+AND+all:%22Gumbel%22&max_results=20
- 2026-10-11 - second_crossref_clumps - HTTP 200 - https://api.crossref.org/works?query=Poisson%20interval%20coverage%20clumps%20infinite%20server%20busy%20period&rows=15

The arXiv random-interval/Gumbel query returned zero entries. The Crossref query mainly returned queueing busy-period papers; none was used as a solution or as an unverified theorem. These broad queries do not establish novelty.

Neighbouring-area lead from Crossref metadata: Manuel Alberto M. Ferreira, José António Filipe, *In the search for the infinite servers queue with Poisson arrivals busy period distribution exponential behaviour*, ['International Journal of Business and Systems Research'], volume 11, issue 4, pages 453, {'date-parts': [[2017]]}. DOI 10.1504/ijbsr.2017.087094. Full text was not audited; this is an infinite-server queue lead, not a matching mobile Boolean coverage solution.
