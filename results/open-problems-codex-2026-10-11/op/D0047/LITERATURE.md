# D0047 literature and status search

Date: 2026-10-12. All web retrieval used Python urllib; no built-in web search.

## Exact source

Bálint Virág, Operator limits of random matrices, ICM Seoul 2014 proceedings; manuscript dated May 25, 2014, posted arXiv:1804.06953v1 on 19 April 2018. https://arxiv.org/pdf/1804.06953.

PDF page 25, Question 9 (Painlevé in the bulk), verbatim:

> Can one deduce the gap Painlevé equation from the PDE’s corresponding to the generator of the Brownian carousel SDE?

The question itself specifies neither beta nor an explicit Painlevé equation. Sections 12–13 give Sine_beta for beta>0 with average spacing 2pi. Section 7 distinguishes the solved edge problem and the missing bulk analogue. The beta=2 scalar sigma-PV equation is a concrete classical target, not a beta restriction quoted from Question 9.

## Every online request

- 2026-10-12: source: `https://arxiv.org/pdf/1804.06953`; result [276733, 'OK'].

- 2026-10-12: arxiv: `https://export.arxiv.org/api/query?search_query=all%3A%22Brownian%20carousel%22%20AND%20all%3APainleve&max_results=30`; result [758, 'OK'].

- 2026-10-12: openalex: `https://api.openalex.org/works?search=Brownian%20carousel%20Painleve&per-page=30`; result [0, 'HTTP Error 429: Too Many Requests'].

- 2026-10-12: openalex_source: `https://api.openalex.org/works?search=Operator%20limits%20of%20random%20matrices&per-page=5`; result [0, 'HTTP Error 429: Too Many Requests'].

- 2026-10-12: crossref: `https://api.crossref.org/works?query=Brownian%20carousel%20Painleve&rows=20`; result [74384, 'OK'].

- 2026-10-12: semantic: `https://api.semanticscholar.org/graph/v1/paper/search?query=Brownian%20carousel%20Painleve&limit=20&fields=title,year,authors,url,abstract`; result [0, 'HTTP Error 429: '].

- 2026-10-12: github: `https://api.github.com/search/repositories?q=Brownian%20carousel%20Painleve`; result [55, 'OK'].

- 2026-10-12: arxiv_carousel: `https://export.arxiv.org/api/query?search_query=all%3A%22carousel%22%20AND%20%28all%3A%22Painlev%C3%A9%22%20OR%20all%3A%22Painleve%22%29&max_results=30`; result ['OK', 798].

- 2026-10-12: arxiv_gap: `https://export.arxiv.org/api/query?search_query=all%3A%22sine%22%20AND%20all%3A%22Painleve%22&max_results=40`; result ['OK', 25162].

- 2026-10-12: openalex_retry: `https://api.openalex.org/works?search=Brownian%20carousel&per_page=25`; result ['HTTP Error 429: Too Many Requests'].

- 2026-10-12: openalex_source_retry: `https://api.openalex.org/works/https://doi.org/10.48550/arXiv.1804.06953`; result ['HTTP Error 429: Too Many Requests'].

- 2026-10-12: semantic_retry: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:1804.06953?fields=title,citations.title,citations.year,citations.externalIds`; result ['HTTP Error 429: '].

- 2026-10-12: crossref_target: `https://api.crossref.org/works?query=Painleve%20Brownian%20carousel%20bulk%20gap%20generator&rows=30`; result ['OK', 112401].

- 2026-10-12: arxiv_rumanov: `https://export.arxiv.org/api/query?search_query=au%3ARumanov%20AND%20%28all%3Abulk%20OR%20all%3APainlev%2A%29&max_results=50`; result ['HTTP Error 429: Too Many Requests'].

- 2026-10-12: arxiv_carousel_all: `https://export.arxiv.org/api/query?search_query=all%3A%22Brownian%20carousel%22&max_results=80&sortBy=submittedDate&sortOrder=descending`; result ['HTTP Error 429: Too Many Requests'].

- 2026-10-12: arxiv_sine_pv: `https://export.arxiv.org/api/query?search_query=all%3A%22sine-beta%22%20AND%20all%3A%22Painlev%2A%22&max_results=40`; result ['HTTP Error 429: Unknown Error'].

- 2026-10-12: openalex_citing: `https://api.openalex.org/works?filter=cites:W2797918296&per-page=50`; result ['HTTP Error 429: Too Many Requests'].

- 2026-10-12: rumanov: `https://arxiv.org/pdf/1306.2117`; result ['OK', 214453].

- 2026-10-12: valko_virag: `https://arxiv.org/pdf/0712.2000`; result ['OK', 580762].

- 2026-10-12: sine_operator: `https://arxiv.org/pdf/1604.04381`; result ['OK', 902714].

- 2026-10-12: dumaz_malvy: `https://arxiv.org/pdf/2603.15289`; result ['OK', 2129509].

- 2026-10-12: semantic_citations: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:1804.06953/citations?fields=title,year,externalIds&limit=100`; result ['OK', 7236].

- 2026-10-12: openalex_exact: `https://api.openalex.org/works?filter=title.search:Operator%20limits%20of%20random%20matrices&per-page=10`; result ['HTTP Error 429: Too Many Requests'].

The openalex_citing request used an unverified candidate work ID and was rate-limited. It is NOT evidence about citations of this source. Exact source lookup via title/arXiv DOI also failed with 429, so OpenAlex source-citation coverage was unavailable. Semantic Scholar source citations succeeded, and provide the actual citation check below.

## Search interpretation

Exact carousel/Painleve arXiv searches returned zero entries. The broader sine/Painleve query returned mainly older or unrelated works. Crossref ranked the 2009 carousel paper first, followed by mostly irrelevant works; no exact resolution theorem was located. GitHub exact query returned total_count=0. Later arXiv queries were rate-limited. These searches do not establish that no solution exists.

## Relevant references fetched in full

- Benedek Valkó and Bálint Virág, Continuum limits of random matrices and the Brownian carousel, Inventiones Mathematicae 177 (2009), 463–508, DOI 10.1007/s00222-009-0180-z; arXiv:0712.2000. Proposition 4 identifies terminal winding with counts; Proposition 9 gives monotonicity and expectation. Foundational, not a post-source solution.

- Igor Rumanov, Classical integrability for beta-ensembles and general Fokker-Planck equations, arXiv:1306.2117 (first posted 2013; retrieved PDF labeled v3, 8 June 2016). Theorem 1, PDF page 8, provides a general governing-system/Lax construction. It does not state the Brownian-carousel physical boundary selection.

- Benedek Valkó and Bálint Virág, The Sine_beta operator, Inventiones Mathematicae 209 (2017), 275–327, DOI 10.1007/s00222-016-0709-x; arXiv:1604.04381. Operator construction, not an exact Question 9 theorem.

- Laure Dumaz and Martin Malvy, Long-Range Correlation of the Sine_beta point Process, arXiv:2603.15289 (2026). Coupled diffusions for correlations; no gap-Painleve generator derivation identified.

## Rumanov theorem (lead, not a solution of D0047)

Theorem 1, PDF p. 8, extracted verbatim (line wrapping normalized):

> Equations (2.24) and (2.23) (or (2.24 and (2.25)) constitute a closed system of two nonlinear PDEs, solvability of which ensures the relation of the general FP equation (2.1) and its solutions with classical Lax pairs and their eigenfunctions. The other components of the Lax matrices L and B can be found from b+ and b1 algebraically, using the relations (2.5) and (2.14), up to the freedom of choosing two of them arbitrarily.

No Brownian-carousel gap theorem is stated here. Compatibility of an added Lax equation does not show that the probabilistically selected solution satisfies that equation.

## Actual source-citing works returned by Semantic Scholar

- 2026: Gaussian limits for traces of circular beta-ensembles; IDs {"ArXiv": "2610.01803", "CorpusId": 292525342}.

- 2024: A convergence framework for Airyβ line ensemble via pole evolution; IDs {"ArXiv": "2411.10586", "DOI": "10.1016/j.aim.2026.111028", "CorpusId": 274130836}.

- 2023: Fluctuations in the active Dyson Brownian motion and the overdamped Calogero-Moser model.; IDs {"ArXiv": "2307.14306", "DOI": "10.1103/PhysRevE.109.014136", "CorpusId": 260164715, "PubMed": "38366440"}.

- 2023: Limits, approximation and size transferability for GNNs on sparse graphs via graphops; IDs {"ArXiv": "2306.04495", "DBLP": "journals/corr/abs-2306-04495", "DOI": "10.48550/arXiv.2306.04495", "CorpusId": 259096107}.

- 2022: Dimension results for the spectral measure of the circular β ensembles; IDs {"DOI": "10.1214/22-aap1798", "CorpusId": 254773601}.

- 2022: Random entire functions from random polynomials with real zeros; IDs {"ArXiv": "2202.03362", "DOI": "10.1016/j.aim.2022.108701", "CorpusId": 246634139}.

- 2021: Amenability of quadratic automaton groups; IDs {"ArXiv": "2111.15206", "DOI": "10.4171/GGD/821", "CorpusId": 244729302}.

- 2021: Report on scipost_202106_00033v1; IDs {"ArXiv": "2106.05014", "DOI": "10.21468/scipost.report.3446", "CorpusId": 235376736}.

- 2020: Scaling Limits of Jacobi Matrices and the Christoffel–Darboux Kernel; IDs {"DOI": "10.1007/s00365-019-09492-z", "CorpusId": 253890066}.

- 2019: Dimension Results for the Spectral Measure of the Circular Beta Ensembles; IDs {"MAG": "2996712820", "ArXiv": "1912.07788", "CorpusId": 209386446}.

- 2019: A short introduction to operator limits of
 random matrices; IDs {"MAG": "3015857158", "DOI": "10.1090/pcms/026/05", "CorpusId": 211264767}.

- 2019: The lower tail of the half-space KPZ equation; IDs {"ArXiv": "1905.07703", "MAG": "2946504750", "DOI": "10.1016/j.spa.2021.09.001", "CorpusId": 159041622}.

- 2019: On the convergence of random tridiagonal matrices to stochastic semigroups; IDs {"MAG": "2940412751", "ArXiv": "1904.07932", "DOI": "10.1214/20-aihp1055", "CorpusId": 119304652}.

- 2019: On the circle, $GMC^\gamma = \varprojlim C\beta E_n$ for $\gamma = \sqrt{\frac{2}{\beta}}, $ $( \gamma \leq 1 )$; IDs {"MAG": "2972116926", "CorpusId": 202537773}.

- 2019: Semigroups for one-dimensional Schrödinger operators with multiplicative Gaussian noise; IDs {"ArXiv": "1902.05047", "MAG": "3110096197", "DOI": "10.1214/21-ejp654", "CorpusId": 229649889}.

- 2019: Semigroups for One-Dimensional Schr\"odinger Operators with Multiplicative White Noise; IDs {"MAG": "2914080790", "CorpusId": 119142816}.

- 2018: Scaling Limits of Jacobi Matrices and the Christoffel–Darboux Kernel; IDs {"ArXiv": "1812.07256", "MAG": "3007270689", "DOI": "10.1007/s00365-019-09492-z", "CorpusId": 119294471}.

- 2018: The directed landscape; IDs {"ArXiv": "1812.00309", "MAG": "2903509700", "DOI": "10.4310/ACTA.2022.v229.n2.a1", "CorpusId": 119261074}.

- 2018: Linear statistics and pushed Coulomb gas at the edge of β-random matrices: Four paths to large deviations; IDs {"MAG": "2899448128", "ArXiv": "1811.00509", "DOI": "10.1209/0295-5075/125/20009", "CorpusId": 119151597}.

- 2018: Poisson statistics at the edge of Gaussian
beta-ensemble at high temperature; IDs {"ArXiv": "1804.08214", "MAG": "2964010404", "DOI": "10.30757/ALEA.V16-32", "CorpusId": 119143827}.

- 2018: Lower tail of the KPZ equation; IDs {"MAG": "2785971247", "ArXiv": "1802.03273", "DOI": "10.1215/00127094-2019-0079", "CorpusId": 119161383}.

- 2017: Benjamini-Schramm convergence and limiting eigenvalue density of random matrices.; IDs {"MAG": "2591632321", "ArXiv": "1702.01281", "CorpusId": 56205695}.

- 2016: The Sine$$_\beta $$β operator; IDs {"MAG": "2340124329", "ArXiv": "1604.04381", "DOI": "10.1007/s00222-016-0709-x", "CorpusId": 119340725}.

- 2015: Limit theorems for biorthogonal ensembles and related combinatorial identities; IDs {"MAG": "2275999301", "ArXiv": "1511.06121", "DOI": "10.1016/j.aim.2017.12.025", "CorpusId": 119653076}.

- 2020: Time evolution of the Kardar-Parisi-Zhang equation; IDs {"MAG": "3043194128", "DOI": "10.7916/D8-1XH3-7C82", "CorpusId": 226664550}.

- 2019: Fe b 20 19 SEMIGROUPS FOR ONE-DIMENSIONAL SCHRÖDINGER OPERATORS WITH MULTIPLICATIVE WHITE NOISE; IDs {"CorpusId": 160026160}.

- 2016: Fluctuations of smooth linear statistics of determinantal point processes; IDs {"MAG": "2357177506", "CorpusId": 124656645}.

The returned source-citing titles identify no explicit solution of Question 9. This is a bounded, metadata-level citation screen, not a full-text review of every citing paper.

## Read-only brain and prior work

Ran math_recall.py "Brownian carousel Sine beta Painleve", brain.py recall "Brownian carousel Painleve", and brain.py recall "Brownian carousel mistakes". The memory recall reported no carousel-specific memory. Math cards covered mostly unrelated results and the 2026 correlation paper.

Searched D0047 in intake directories and codex_pool_2026_10_10. Recovered D0047-A001 and six 2026-09-17 reports from origin/master of ~/math-open-problems using git show, saved locally as prior_*.md. The reports are hints, not independently certified proofs. No repository was changed.

Earlier work reduced a one-pole Lax family to sigma-PV conditional on selecting the physical solution. That selection remains unproved. Its claim that the small-gap intensity alone selects the PV branch is too weak: the exact exponential/linear-sigma branch in ATTEMPT.md has the same slope.

## Verdict

No paper was located stating and proving THIS question with the physical Brownian-carousel selection. Therefore SOLVED_IN_LITERATURE is not claimed.


## Final exact-ID lookup request

- 2026-10-12: semantic_source_ids: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:1804.06953?fields=title,externalIds,citationCount`; result ['HTTP Error 429: '].

The source-ID lookup was rate-limited, so no verified OpenAlex citing-source request could be constructed. The successful Semantic Scholar citations request remains the actual source-citation screen.


## Additional-attempt brain queries, 2026-10-12

- math_recall.py "Painleve V isomonodromy connection Fokker Planck Rumanov boundary selection": returned unrelated general cards; no carousel selection theorem.
- math_recall.py "Brownian carousel discounted hitting time Girsanov small gap level repulsion": returned generic Girsanov/generator cards and unrelated hitting-time material.
- math_recall.py "Geometric Brownian Motion Characteristic Roots Generator ODE hitting discount": retrieved the Cauchy-Euler characteristic-root card.
- math_recall.py --id claim_51bd0f2420fc622328de59f07adda2e1aead98aac1ef31a4ca8bbdbad130f247: read full card and typed links. It cites arXiv:2505.18394, Optimal stopping involving a diffusion and its running maximum: a generalisation of the maximality principle.

The characteristic polynomial is a useful hint, but the card's unrestricted assertion that the positive root exceeds 1 is false without an extra drift restriction: with sigma=1, mu=2 and discount r=1, its positive root is (-3+sqrt(17))/2<1. No such card assertion was used. Our zero-drift power calculation p(p-1)/2=c is independently verified.

No additional online literature resolution is claimed in this continuation. The added work is a direct stochastic bound and a formal PV uniqueness calculation, not a new SOLVED_IN_LITERATURE verdict.
