# F0084 literature audit — 2026-10-11

## Superseding result: the upper-bound question is SOLVED_IN_LITERATURE

The second attempt retrieved Alexander E. Holroyd, Robin Pemantle, Yuval Peres and Oded Schramm, **Poisson Matching**, *Annales de l'Institut Henri Poincaré, Probabilités et Statistiques* **45** (2009), 266–287, DOI **10.1214/08-AIHP170**, arXiv:**0712.1867v3**. PDF saved as `matching_pdf.pdf`, page-labelled text as `matching_pdf.txt`. This was a published answer overlooked in the first search. The earlier no-solution-found entries below describe the first attempt and are superseded.

### Exact theorem and explicit same-model extension

The published journal PDF was independently fetched from `https://www.numdam.org/item/AIHPB_2009__45_1_266_0.pdf` (HTTP 200 on 2026-10-11), saved as `matching_journal_pdf.pdf`, with text in `matching_journal.txt`. Theorem 6 is on **printed p.269, journal PDF p.4** (arXiv PDF p.6). It reads word for word below, with mathematical typography normalized:

> **Theorem 6 (2-color stable matching).** Let R, B be independent Poisson processes of intensity 1. For d ≥ 1, the two-color stable matching satisfies:
>
> (i) E* X^d = ∞ (Theorem 2 gives a better bound in d = 1, 2);
>
> (ii) P*(X > r) ≤ C r^(-s) ∀ r > 0,
>
> where s = s(d) ∈ (0, 1) satisfies s(1) = 1/2, and C = C(d) ∈ (0, ∞).

The explicit extension is on **printed p.270, journal PDF p.5** (arXiv PDF pp.7–8), and reads:

> **Extensions to other processes**
>
> The results on 2-color matchings in Theorems 1, 2, 6 all extend, with similar proofs, to the following two variant settings:

Item (ii) on that same printed page reads:

> (ii) Fair allocations of Lebesgue measure to a Poisson process (see [11] and also [5, 10, 14] for definitions and background). Here X denotes the distance from the origin to its allocated Poisson point. The resulting upper bounds on the stable allocation in Theorem 6(ii) represent a considerable improvement on the previous best results: X was known to have a finite (1/18)th moment in d = 1, and no quantitative upper bound was known in d ≥ 2 [10].

The allocation proof is explicitly supplied by the remark following the proof of Theorem 19, **printed p.286, journal PDF p.21** (arXiv PDF p.34):

> **Remarks.** In order to adapt the proof of Theorem 19 to the stable allocation of Lebesgue to Poisson, we replace #Y_R with the volume of sites z ∈ B whose Poisson point is at a distance greater than R + |z|, and replace #Y_B with the sum over Poisson points x ∈ B of the volume of x’s territory that is at a distance greater than R + |x|. The mass transport principle easily shows that these two quantities have the same expectation. A similar remark applies to #Q_R and #Q_B. This allows us to obtain the analog of (23).

### Line-by-line implication for F0084

1. Theorem 6(ii) gives constants C(d)<∞ and s(d)>0, for every d>=1, and all r>0, in the unit-intensity stable model.
2. The **explicit printed extension**, not an analogy inferred by this attempt, includes stable fair Poisson–Lebesgue allocation and identifies X as the origin-to-allocated-Poisson-centre distance. This is exactly the source's site distance, not the centre's maximum territory radius. The point-matching theorem uses P* for the Palm law of a typical source point; for deterministic Lebesgue source measure its Palm law is just the ordinary stationary law P. Indeed E integral_Q f(theta_x Pi) dx=volume(Q) E f(Pi) by stationarity, which is the defining Palm identity at source intensity 1.
3. “Fair” here is unit territory volume at unit Poisson intensity, i.e. appetite alpha=1 and lambda=1, the same critical model. The cited background includes HHP's *A stable marriage of Poisson and Lebesgue* and its tail-bounds paper (references [11] and [10] of this PDF respectively).
4. Thus for each d>=2 the printed extended theorem gives P(X>r)<=C(d) r^(-s(d)) for every r>0. Since s(d)>0, this is a quantitative upper bound tending to zero.
5. The paper expressly compares it to the formerly missing d>=2 bound, confirming that it addresses this question, not just another allocation rule. The p.34 remark describes the proof substitutions; the full independent version of that transfer, using the simpler inequality (25), is written out in SOLUTION.md.
6. Theorem 19, PDF pp.29–33, gives the sharper exponent as the unique root s(d) in (0,1) of its equation (21), with s(2) approximately 0.496 and s(3) approximately 0.449. Sharp tail asymptotics are not asserted. SOLVED_IN_LITERATURE refers to the explicitly requested any-upper-bound problem, not determination of the optimal exponent.

### Second-attempt retrievals and brain searches

On 2026-10-11, Python requests fetched `https://arxiv.org/pdf/0712.1867` and `https://arxiv.org/pdf/1810.00265`, both HTTP 200; exact request records are in `second_search_log.json`. The latter is M.A. Klatt, G. Last and D. Yogeshwaran, *Hyperuniform and rigid stable matchings*, arXiv:1810.00265v3, DOI 10.1002/rsa.20923. Its abstract and Theorem 5.1, PDF p.13, require a lattice and point-process intensity alpha>1. It is a different, noncritical setting, and is not the solution used here.

Read-only math-store queries during the second attempt were `replete boxes critical stable allocation quantitative Hoffman Holroyd Peres` and `Holroyd Pemantle Schramm Poisson Matching power law upper bound`. Neither returned the relevant matching theorem. The decisive evidence came from reading the actual neighbouring paper.

The exact URLs, HTTP status codes, dates and saved response filenames are in `search_log.json`. All fetching uses Python requests, not built-in web search.

Initial searches: arXiv `all:"stable marriage" AND all:Poisson` (50 results requested); OpenAlex `stable marriage Poisson Lebesgue` (HTTP 429, not negative evidence); Crossref the same words (30 results); Semantic Scholar paper ARXIV:math/0505668 with citing paper titles/year/external IDs; GitHub repositories `stable marriage Poisson Lebesgue`.

Source fetched successfully: Christopher Hoffman, Alexander E. Holroyd, Yuval Peres, *A stable marriage of Poisson and Lebesgue*, Annals of Probability 34 (2006), 1241–1272, arXiv:math/0505668. Saved PDF and page-labelled extracted text in this folder.

Read-only background checks: math_recall.py query `Hoffman Holroyd Peres stable marriage critical tail`; brain.py recall `stable marriage Poisson Lebesgue` and `stable marriage Poisson Lebesgue mistakes`. No directly relevant mathematical card was returned. Intake search for F0084 found attempt F0084-A001 from 2026-09-08. Its conjectured exponent d/2 and its informal growth argument are unverified hints. In particular its statement distinguishing site and centre moments must be checked against the source; it cannot be accepted as evidence.

The prior intake lists HHP's *Tail bounds for the stable marriage of Poisson and Lebesgue* (2009) and optimal allocations as leads, not a critical-case solution.

## Source wording and exact applicability

Source PDF p.31: “(ii) Critical tail behavior. What is the tail behavior of X for the critical Poisson model? In particular, give any quantitative upper bound for d ≥ 2.” In the fetched PDF this follows Section 9, under `Open problems`; the intake's Section 12 locator is inaccurate. X is defined on p.6 as the origin's allocation distance, with infinity for an unclaimed origin. Theorem 4(ii), p.5, gives claimedness almost everywhere at lambda alpha=1. Theorem 32, p.30, explicitly concerns this X under ergodicity and insertion tolerance, rather than the centre radius. Poisson satisfies those hypotheses. Theorem 33, p.31, is the distinct Palm radius statement under deletion tolerance.

HHP, *Tail Bounds*, arXiv:math/0507324v1 (the downloaded preprint of the 2009 journal paper), p.4, Theorem 1 proves only dimension one at criticality. Theorem 2 proves noncritical bounds; part (ii) concerns Palm territory radius. Lemma 4, p.5, transfers the latter to conditional finite site distance. On p.5 the authors explicitly say: “Our proof of Theorem 2 does not in general yield any explicit bound on the exponential decay constant c(d, α).” The explicit regimes on p.6 are alpha>2^d, alpha<2^(-d), or dimension one. This pinpoints why the nearcritical comparison in ATTEMPT.md does not yield a rate.

Daniel Andrés Díaz Pachón, *A Note on Large Deviations for the Stable Marriage of Poisson and Lebesgue with Random Appetites*, arXiv:0911.1429v3, DOI 10.1007/s10959-010-0304-9. Downloaded successfully on retry. Theorems 2.1–2.3, PDF pp.5–6: respectively appetite means >2^d or <2^(-d), intensity lambda>1 with mean appetite 1, and lambda<1 with mean appetite 1 (d>2). None covers lambda=1, deterministic appetite 1. This is a related noncritical result, not a solution.

Mir-Omid Haji-Mirsadeghi and Ali Khezeli, *Stable transports between stationary random measures*, Electronic Journal of Probability 21 (2016), DOI 10.1214/16-EJP4237, arXiv:1504.02965v2. Downloaded on retry. Its introduction enumerates existence, shift-coupling, monotonicity, uniqueness, and boundedness results (Theorems 4.8, 4.9, 4.13, 4.21, 4.24, 4.25). General stable constrained transports and boundedness do not supply a numerical upper-tail rate for the source's critical stable allocation.

## First-attempt searches and limitations (historical; superseded above)

All searches here were performed on 2026-10-11 and saved in `search_log.json` with their exact URLs. Additional arXiv queries: `all:"stable allocation" AND all:critical` (40 requested), and `all:stable AND all:Poisson AND all:critical AND all:tail` (50 requested). Only the HHP tail paper was pertinent to the requested model in these results; other hits use “stable” for different concepts. Semantic Scholar citations of both math/0505668 and math/0507324 were inspected; the former includes 2026 titles, but citation indexing is not an exhaustive proof of current status. Several optimal transport/allocation and Poisson point matching papers are different models or different allocation rules.

OpenAlex was attempted for keyword search, lookup of source DOI 10.1214/009117906000000098, and works citing that DOI; the source and citation requests were retried. Successful HTTP responses were 429 rate limits, and one attempt failed with a TLS error. Therefore OpenAlex supplied no usable citation list and is NOT negative evidence. PDF downloads for the random-appetite and stable-transport papers and the Semantic Scholar tail-paper citation request failed first with connection/TLS errors; retries succeeded.

GitHub returned `danielandresgp/stable-marriage-poisson-lebesgue`, described as simulation of Poisson–Lebesgue stable marriage. A simulation repository is not a proof of the question. Read-only `git ls-tree` of `origin/master` in the recorded-answer checkout found no tracked path matching F0084 or stable-marriage wording; no repository working tree was changed.

At the end of the first attempt, no such paper had been identified in the inspected results. That bounded-search conclusion was superseded by the exact published extension quoted above; the current verdict is SOLVED_IN_LITERATURE for the any-upper-bound question.

## Exact references from Crossref metadata

- Christopher Hoffman, Alexander E. Holroyd, Yuval Peres; A stable marriage of Poisson and Lebesgue; The Annals of Probability; [2006, 7, 1]; volume 34; pages 1241-1272; DOI 10.1214/009117906000000098.
- Daniel Andrés Díaz Pachón; Percolation for the stable marriage of Poisson and Lebesgue with random appetites; Stochastics; [2012, 2, 10]; volume 85; pages 252-261; DOI 10.1080/17442508.2011.651215.
- M.V. Freire, S. Popov, M. Vachkovskaia; Percolation for the stable marriage of Poisson and Lebesgue; Stochastic Processes and their Applications; [2007, 4]; volume 117; pages 514-525; DOI 10.1016/j.spa.2006.09.002.
- Christopher Hoffman, Alexander E. Holroyd, Yuval Peres; Tail Bounds for the Stable Marriage of Poisson and Lebesgue; Canadian Journal of Mathematics; [2009, 12, 1]; volume 61; pages 1279-1299; DOI 10.4153/cjm-2009-060-7.
- Daniel Andrés Díaz Pachón; A Note on Large Deviations for the Stable Marriage of Poisson and Lebesgue with Random Appetites; Journal of Theoretical Probability; [2010, 8, 11]; volume 25; pages 77-91; DOI 10.1007/s10959-010-0304-9.
- ; Stable Allocations; Lectures on the Poisson Process; ['unknown']; volume ?; pages 103-110; DOI 10.1017/9781316104477.012.

## First-attempt unverified lead and publication-date clarification (historical)

*Hyperuniform and rigid stable matchings*, arXiv:1810.00265, DOI 10.1002/rsa.20923 (2018 preprint), appeared among Semantic Scholar citations of the tail paper. Two PDF requests and two arXiv metadata requests for it failed with connection/TLS errors. The full paper remains an unverified lead, not an excluded candidate or a claimed solution. The metadata request also included Markó–Timár's allocation paper and Timár's factor matching paper; the latter is *A Factor Matching of Optimal Tail Between Poisson Processes*, arXiv:2106.04524, DOI 10.1007/s00493-023-00051-6. Point-to-point optimal matching is a different model; no theorem from it is used here.

Crossref's dates above include online publication dates. The random-appetite percolation paper appeared in Stochastics 85 (2013), 252–261 (online 2012); the large-deviation paper appeared in Journal of Theoretical Probability 25 (2012), 77–91 (online 2010). The two HHP publication references are Annals of Probability 34 (2006), 1241–1272, and Canadian Journal of Mathematics 61 (2009), 1279–1299.

The first attempt did not identify the solution. The second attempt retrieved both this lead and the decisive Poisson Matching paper, as recorded above. Missing OpenAlex data do not affect the positive theorem identification and are not used to infer the status of sharp asymptotics.

During the attempt, a further read-only math-store query, `Campbell Palm mass transport allocation`, returned general Palm-normalization and mass-transport cards, plus unrelated hyperbolic-cell attempts. They emphasize checking intensity normalization and that a mass-transport identity does not itself control distant-centre tails. The unit-intensity normalization in ATTEMPT.md was checked explicitly using Campbell–Palm. None of these cards supplies a missing quantitative estimate, and no unreviewed card was accepted as a theorem about F0084.

## Complete request ledger

Every row was requested on 2026-10-11. Failed requests provide no negative evidence. Full bodies are preserved when received; the filename suffix for some JSON responses is `.xml`.

| Service / purpose | Exact request | Outcome |
|---|---|---|
| source_pdf | `https://arxiv.org/pdf/math/0505668` | 200 |
| arxiv | `https://export.arxiv.org/api/query?search_query=all:%22stable%20marriage%22%20AND%20all:Poisson&max_results=50` | 200 |
| openalex | `https://api.openalex.org/works?search=stable%20marriage%20Poisson%20Lebesgue&per-page=50` | 429 |
| crossref | `https://api.crossref.org/works?query=stable%20marriage%20Poisson%20Lebesgue&rows=30` | 200 |
| semantic | `https://api.semanticscholar.org/graph/v1/paper/ARXIV:math/0505668?fields=title,year,citationCount,citations.title,citations.year,citations.externalIds` | 200 |
| github | `https://api.github.com/search/repositories?q=stable+marriage+Poisson+Lebesgue` | 200 |
| tails_pdf | `https://arxiv.org/pdf/math/0507324` | 200 |
| transport_pdf | `https://arxiv.org/pdf/1504.02965` | ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None)) |
| random_pdf | `https://arxiv.org/pdf/0911.1429` | ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None)) |
| arxiv_critical | `https://export.arxiv.org/api/query?search_query=all:%22stable%20allocation%22%20AND%20all:critical&max_results=40` | 200 |
| openalex_source | `https://api.openalex.org/works/https://doi.org/10.1214/009117906000000098` | 429 |
| semantic_tails | `https://api.semanticscholar.org/graph/v1/paper/ARXIV:math/0507324?fields=title,year,citations.title,citations.year,citations.externalIds` | HTTPSConnectionPool(host='api.semanticscholar.org', port=443): Max retries exceeded with url: /graph/v1/paper/ARXIV:math/0507324?fields=title,year,citations.title,citations.year,citations.externalIds (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)'))) |
| openalex_citing_doi | `https://api.openalex.org/works?filter=cites:https://doi.org/10.1214/009117906000000098&per-page=100` | HTTPSConnectionPool(host='api.openalex.org', port=443): Max retries exceeded with url: /works?filter=cites:https://doi.org/10.1214/009117906000000098&per-page=100 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)'))) |
| transport_retry_pdf | `https://arxiv.org/pdf/1504.02965` | 200 |
| random_retry_pdf | `https://arxiv.org/pdf/0911.1429` | 200 |
| semantic_tails_retry | `https://api.semanticscholar.org/graph/v1/paper/ARXIV:math/0507324?fields=title,year,citations.title,citations.year,citations.externalIds` | 200 |
| arxiv_tail | `https://export.arxiv.org/api/query?search_query=all:stable%20AND%20all:Poisson%20AND%20all:critical%20AND%20all:tail&max_results=50` | 200 |
| openalex_citing_retry | `https://api.openalex.org/works?filter=cites:https://doi.org/10.1214/009117906000000098&per-page=100` | 429 |
| hyperuniform_pdf | `https://arxiv.org/pdf/1810.00265` | ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None)) |
| lead_metadata | `https://export.arxiv.org/api/query?id_list=1810.00265,1103.5259,2106.04524&max_results=3` | ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None)) |
| hyperuniform_pdf | `https://arxiv.org/pdf/1810.00265` | HTTPSConnectionPool(host='arxiv.org', port=443): Max retries exceeded with url: /pdf/1810.00265 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)'))) |
| lead_metadata | `https://export.arxiv.org/api/query?id_list=1810.00265,1103.5259,2106.04524&max_results=3` | HTTPSConnectionPool(host='export.arxiv.org', port=443): Max retries exceeded with url: /api/query?id_list=1810.00265,1103.5259,2106.04524&max_results=3 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)'))) |

## Additional exact arXiv references and lead screening

- Alexander E. Holroyd, Robin Pemantle, Yuval Peres, Oded Schramm. *Poisson Matching*. http://arxiv.org/abs/0712.1867v3, first posted 2007-12-12.
- Roland Markó, Ádám Timár. *A Poisson allocation of optimal tail*. http://arxiv.org/abs/1103.5259v3, first posted 2011-03-27.
- Jean-Baptiste Gouéré. *Subcritical regimes in some models of continuum percolation*. http://arxiv.org/abs/0712.3638v3, first posted 2007-12-21.

Poisson point matching and optimal allocation rules are not the Euclidean stable Poisson–Lebesgue rule. Subcritical percolation addresses other parameters and observables. These are leads rather than printed solutions to F0084. See the individual screening notes above.
