# D0064 literature audit — 11 October 2026

## Verdict and scope

No fetched theorem proves the four-case classification for all solutions under the source's intended hypotheses. This is a bounded search, not a proof of absence of a later solution. OpenAlex was rate limited; Semantic Scholar search was rate limited but its source citation endpoint succeeded. The recent supercritical uniqueness paper concerns limits of regularizations, not all star-equation fixed points. Overall result: PARTIAL, not SOLVED_IN_LITERATURE.

## Verified source

Rémi Rhodes and Vincent Vargas, *Gaussian multiplicative chaos and applications: A review*, Probability Surveys **11** (2014), 315–392, DOI 10.1214/13-PS218; arXiv:1305.6221. Source fetched from https://arxiv.org/pdf/1305.6221 using curl on 2026-10-11; stored as source_curl.pdf and source.txt. The first Python requests fetch failed with SSL UNEXPECTED_EOF; curl succeeded.

Conjecture 6.4 is on printed/PDF page 52, Section 6.3. Relevant definitions: Definition 2.17, equations (2.17)–(2.18), page 17; Definition 2.18, pages 17–18; Theorem 2.19, page 18. Section 1.2, printed page 6, states: “Finally, γ will denote the intermittency parameter. We will suppose that γ ⩾ 0.”

Section 6.3's hypothesis paragraph reads (line breaks joined):

> It is conjectured that all the non-trivial ergodic lognormal star scale invariant random measures (actually, we need to impose a stronger dependence decay than ergodicity) belong to one of the families listed below, up to a constant multiplicative factor. At least, we ask for ergodicity to get rid of the irrelevant random factor Y of Theorem 2.19.

It then requires an α in (0,1] with E[exp(α ωε(r))]=ε^d, writes the centered weight as (γ/α) X_t with the normalized continuous covariance kernel in (6.10), and gives γ²≤2d. The additional decay condition is not specified quantitatively.

Conjecture 6.4, mathematical symbols normalized from PDF extraction:

> 1. If α = 1 and γ² < 2d then the law of the solution M is the standard Gaussian multiplicative chaos, as stated in Theorem 2.19.
> 2. If α = 1 and γ² = 2d, then the law of the solution M is that of the derivative martingale M′ described in section 6.1.
> 3. If α < 1 and γ² < 2d, then M is an atomic Gaussian multiplicative chaos of the dual phase as described in subsection 6.2.
> 4. If α < 1 and γ² = 2d, then M is an atomic Gaussian multiplicative chaos of the frozen phase.

## Searches and retrieval outcomes

All queries below ran on 2026-10-11 via shell Python/curl. An initial requests-based pass attempted all eight queries in search_literature.py and failed with SSL UNEXPECTED_EOF (including HTTP arXiv after redirect). The curl pass then retried them. Importing search_literature in search_followup.py repeated that eight-query curl pass, with the same response classes; these are retries, not independent evidence. Raw responses are saved under the service names and full URLs/parameters are in search_log.json and followup_search_log.json.

### search_log.json

- **arxiv** — query {"search_query": "all:\"star-scale\" AND all:\"Gaussian\"", "max_results": 30}; HTTP 200; http://export.arxiv.org/api/query?search_query=all%3A%22star-scale%22+AND+all%3A%22Gaussian%22&max_results=30
- **arxiv_https** — query {"search_query": "all:\"star-scale\" AND all:\"classification\"", "max_results": 30}; HTTP 200; https://export.arxiv.org/api/query?search_query=all%3A%22star-scale%22+AND+all%3A%22classification%22&max_results=30
- **openalex** — query {"search": "star scale invariant random measures classification", "per-page": 30}; HTTP 429; https://api.openalex.org/works?search=star+scale+invariant+random+measures+classification&per-page=30
- **openalex_source** — query {"search": "Gaussian multiplicative chaos and applications a review", "per-page": 5}; HTTP 429; https://api.openalex.org/works?search=Gaussian+multiplicative+chaos+and+applications+a+review&per-page=5
- **crossref** — query {"query": "star scale invariant random measures classification", "rows": 25}; HTTP 200; https://api.crossref.org/works?query=star+scale+invariant+random+measures+classification&rows=25
- **semantic_scholar** — query {"query": "star scale invariant random measures", "limit": 30, "fields": "title,authors,year,abstract,externalIds,url"}; HTTP 429; https://api.semanticscholar.org/graph/v1/paper/search?query=star+scale+invariant+random+measures&limit=30&fields=title%2Cauthors%2Cyear%2Cabstract%2CexternalIds%2Curl
- **github** — query {"q": "\"star scale\" \"chaos\"", "per_page": 20}; HTTP 200; https://api.github.com/search/repositories?q=%22star+scale%22+%22chaos%22&per_page=20
- **openalex_uniqueness** — query {"search": "uniqueness critical star scale invariant Gaussian multiplicative chaos", "per-page": 30}; HTTP 429; https://api.openalex.org/works?search=uniqueness+critical+star+scale+invariant+Gaussian+multiplicative+chaos&per-page=30

### followup_search_log.json

- **arxiv_star** — query {"search_query": "all:\"scale invariant\" AND (all:\"chaos\" OR all:\"random measures\")", "max_results": 60}; HTTP 200; https://export.arxiv.org/api/query?search_query=all%3A%22scale+invariant%22+AND+%28all%3A%22chaos%22+OR+all%3A%22random+measures%22%29&max_results=60
- **arxiv_uniqueness** — query {"search_query": "all:\"multiplicative chaos\" AND (all:\"uniqueness\" OR all:\"classification\")", "max_results": 60}; HTTP 200; https://export.arxiv.org/api/query?search_query=all%3A%22multiplicative+chaos%22+AND+%28all%3A%22uniqueness%22+OR+all%3A%22classification%22%29&max_results=60
- **arxiv_freezing** — query {"search_query": "all:\"multiplicative chaos\" AND (all:\"glassy\" OR all:\"supercritical\")", "max_results": 40}; HTTP 200; https://export.arxiv.org/api/query?search_query=all%3A%22multiplicative+chaos%22+AND+%28all%3A%22glassy%22+OR+all%3A%22supercritical%22%29&max_results=40
- **crossref_source** — query {"query.title": "Gaussian multiplicative chaos and applications a review", "rows": 3}; HTTP 200; https://api.crossref.org/works?query.title=Gaussian+multiplicative+chaos+and+applications+a+review&rows=3
- **openalex_doi** — query {}; HTTP 429; https://api.openalex.org/works/https://doi.org/10.1214/13-PS218?
- **semantic_source** — query {"limit": 100, "fields": "title,year,externalIds"}; HTTP 200; https://api.semanticscholar.org/graph/v1/paper/ARXIV:1305.6221/citations?limit=100&fields=title%2Cyear%2CexternalIds
- **github_followup** — query {"q": "\"multiplicative chaos\"", "per_page": 20}; HTTP 200; https://api.github.com/search/repositories?q=%22multiplicative+chaos%22&per_page=20
- **openalex_citing_doi** — query {"filter": "cites:doi:10.1214/13-PS218", "per-page": 200}; HTTP 429; https://api.openalex.org/works?filter=cites%3Adoi%3A10.1214%2F13-PS218&per-page=200

An attempted OpenAlex DOI-to-work lookup was rate limited, so the canonical work ID could not be resolved. The fallback DOI-form citing filter also returned 429 and is not treated as a successful or validated citing-works retrieval. Semantic Scholar supplied the first 100 citing records, which were inspected. GitHub broad search returned repositories, not peer-reviewed classification theorems.

## Relevant arXiv records returned by these searches

- Janne Junnila, Eero Saksman, Christian Webb, *Decompositions of log-correlated fields with applications*, http://arxiv.org/abs/1808.06838v3 (initial publication 2018-08-21).
- Federico Bertacco, Martin Hairer, *How does the supercritical GMC converge?*, http://arxiv.org/abs/2504.06956v2 (initial publication 2025-04-09).
- Rémi Rhodes, Julien Sohier, Vincent Vargas, *Levy multiplicative chaos and star scale invariant random measures*, http://arxiv.org/abs/1201.5219v2 (initial publication 2012-01-25).
- Romain Allez, Rémi Rhodes, Vincent Vargas, *Lognormal scale invariant random measures*, http://arxiv.org/abs/1102.1895v3 (initial publication 2011-02-09).
- Shirshendu Ganguly, Kyeongsik Nam, *Universality of Poisson-Dirichlet law for log-correlated Gaussian fields via level set statistics*, http://arxiv.org/abs/2302.03010v2 (initial publication 2023-02-06).
- Janne Junnila, Eero Saksman, *The uniqueness of the Gaussian multiplicative chaos revisited*, http://arxiv.org/abs/1506.05099v2 (initial publication 2015-06-16).
- Federico Bertacco, Martin Hairer, *Uniqueness of supercritical Gaussian multiplicative chaos*, http://arxiv.org/abs/2504.07552v3 (initial publication 2025-04-10).
- Alexander Shamov, *On Gaussian multiplicative chaos*, http://arxiv.org/abs/1407.4418v4 (initial publication 2014-07-16).
- Bertrand Duplantier, Rémi Rhodes, Scott Sheffield, Vincent Vargas, *Critical Gaussian multiplicative chaos: Convergence of the derivative martingale*, http://arxiv.org/abs/1206.1671v3 (initial publication 2012-06-08).
- Thomas Madaule, Rémi Rhodes, Vincent Vargas, *Glassy phase and freezing of log-correlated Gaussian potentials*, http://arxiv.org/abs/1310.5574v1 (initial publication 2013-10-21).

## Theorems inspected and why they do not settle D0064

1. **Allez, Rhodes, Vargas**, *Lognormal star-scale invariant random measures*, arXiv:1102.1895v3; Probability Theory and Related Fields **155** (2013), 751–788, DOI 10.1007/s00440-012-0412-9. Downloaded allez.pdf; extracted allez.txt. Theorem 4, page 5, assumes a finite 1+δ moment and good covariance regularity; Theorem 10, page 6, gives the multidimensional version with an extra differentiability hypothesis. The ergodic multiplier is deterministic. This is the established moment-restricted subcritical classification. It does not classify infinite-mean critical/atomic measures. Its convention includes ε^d in the scaling of M^ε, unlike the review's shifted convention; normalized weight means differ accordingly.

2. **Alexander Shamov**, *On Gaussian multiplicative chaos*, arXiv:1407.4418v4 (downloaded shamov.pdf and shamov.txt); Journal of Functional Analysis **270** (2016), 3224–3261. The subcritical uniqueness result concerns a GMC jointly coupled to a specified Gaussian field with its Cameron–Martin transformation rule and deterministic mean. The star equation alone does not establish those assumptions. The introduction on page 5 explicitly excludes atomic supercritical distributional limits from its definition. The old intake assertion that Shamov alone proves unrestricted case (1) was therefore not accepted.

3. **Thomas Madaule, Rémi Rhodes, Vincent Vargas**, *Glassy phase and freezing of log-correlated Gaussian potentials*, arXiv:1310.5574; Annals of Applied Probability **26** (2016), 643–690, DOI 10.1214/14-AAP1071. Downloaded freezing.pdf and freezing.txt. Theorem 2.2 (Freezing theorem), page 4 of the arXiv PDF, and Corollary 2.3 give convergence of a specific normalized Gaussian approximation to a stable atomic measure directed by critical derivative chaos. The seed covariance satisfies Assumption (A): continuity/nonnegativity, k(0)=1, compact support, and a Lipschitz bound near zero. This establishes an approximation limit in the frozen family, not the assertion that every star-equation solution belongs to it.

4. **Federico Bertacco, Martin Hairer**, *Uniqueness of supercritical Gaussian multiplicative chaos*, arXiv:2504.07552v3 (27 November 2025; manuscript dated 1 December 2025). Downloaded uniqueness_supercritical.pdf and uniqueness_supercritical.txt. Theorem A, PDF page 4, assumes a given log-correlated Gaussian field on a bounded domain, g in local Sobolev H^s for s>d, and a mollifier satisfying (A1)–(A2). Its conclusion is stable convergence of the particular measures in equation (1.8) to a constant times the atomic critical-directed measure. The word “uniqueness” in the title refers to independence of the regularization up to a constant. It does not quantify over arbitrary star-equation solutions. Lemma 2.7, page 8, contains the stable-weight identity used in the independently proved reduction in REDUCTIONS.md.

5. **Junnila–Saksman** arXiv:1506.05099 and **Junnila–Saksman–Webb** arXiv:1808.06838 are approximation/decomposition uniqueness leads. Their arXiv records were read; full theorem hypotheses were not used as if they proved fixed-point classification.

6. **Bertacco–Hairer**, *How does the supercritical GMC converge?*, arXiv:2504.06956v2, and arXiv:2302.03010 (*Universality of Poisson–Dirichlet law for log-correlated Gaussian fields via level set statistics*) concern extrema, approximation limits, or normalized atom sizes. No arbitrary-solution classification was extracted from their records.

These are related results and leads. No theorem is designated a solution in print, and no unproved implication from approximation uniqueness to fixed-point uniqueness is used.

## Read-only research-brain and earlier-attempt checks

- math_recall.py queried “Gaussian multiplicative chaos star scale invariance Rhodes Vargas” and later “stable independently scattered random measure subordination”. Relevant hints were the ordinary GMC construction/interpolation and the stable-distribution definition; no classification theorem card was found. The irrelevant returned cards were not used.
- brain.py recall queried “Gaussian multiplicative chaos star equation mistakes” and “Gaussian multiplicative chaos”. No specific usable solution was returned. The advertised recall printed that a detached index refresh failed; no explicit write/remember operation was invoked.
- rg searched D0064 across the allowed 06_math_research ledgers. The D_20260908 problems/attempts entries were inspected, as was the 2026-10-10 intake summary. The prior smoothing-transform analogy is a lead, not a proof. Its statement about finite Laplace exponents failing with infinite mean is incorrect for locally finite random measures.
- git ls-tree on origin/master of ~/math-open-problems, with D0064/d0064 path patterns, found no matching recorded-answer path. No working-tree or repository change was made.


## Second-attempt brain queries (11 October 2026)

- math_recall.py query: "independently scattered random measure Levy basis stable subordinator Laplace exponent". Returned stable-subordinator, Levy-process, Levy-triplet, and Cox-compensator cards. The final theorem was proved directly by Laplace additivity and scaling; no unverified Levy classification was imported.
- math_recall.py query: "Gaussian multiplicative chaos star scale invariance uniqueness finite range dependence Cox stable atomic directing measure". The result and relevance are summarized in SECOND_ATTEMPT.md.
- Read whole card claim_55e8e09f5c49b2cbb66486d438868e84fb01a1a1343ae43fbfc159ed85f2a1e6 (Compensator Measure of a Cox Process). A compensator or recovered intensity alone does not prove conditional Poisson independence; the card was treated as a hint, not a classification theorem.
- No new external literature solution is asserted in this follow-up. The new zero-gamma theorem has an explicitly additional uniform-mixing hypothesis and is a proved special case, not SOLVED_IN_LITERATURE.
