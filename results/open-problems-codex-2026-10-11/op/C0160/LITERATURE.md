# C0160 literature and source audit

All searches below were run from the shell with Python requests on 2026-10-11. No built-in web search was used. HTTP errors and rate limits do not establish absence of papers. Raw responses, fetched PDFs, extracted text, and runnable scripts are retained in this folder.

## Primary source and exact scope

Olle Häggström and Johan Jonasson, **Uniqueness and non-uniqueness in percolation theory**, Probability Surveys **3** (2006), 289–344. DOI **10.1214/154957806000000096**. arXiv **math/0612812v1**. The arXiv API record explicitly identifies this DOI and journal reference. The primary PDF was successfully recovered at https://arxiv.org/pdf/math/0612812v1 and saved as survey.pdf; survey.txt is its extraction. The supplied Project Euclid URL and an alternative Euclid download URL returned an Incapsula error document (one initial request failed in TLS). The misleading .pdf extension on source.pdf must not be interpreted as a valid paper: source.txt contains that error document.

Global source conventions: infinite connected graph, iid bond percolation with retention parameter p (printed p.291 / PDF p.3); transitivity and the graph conventions are set in Section 1. We work with locally finite graphs. The explicit counterexample has bounded degree.

On printed p.300 / PDF p.12, the source says, verbatim with mathematical typography normalized:

> “Häggström and Peres [56] proved uniqueness monotonicity for transitive (and quasi-transitive) graphs under the additional assumption of so-called unimodularity (see Definition 5.2 below), and Schonmann [95] gave a different proof where the unimodularity condition was shown to be superfluous.”

And:

> “Thus for all G there exists a threshold p_u ∈ [p_c, 1] such that uniqueness of the infinite cluster holds for all p > p_u, but for no p < p_u.”

The surrounding discussion is about transitive/quasi-transitive graphs; this sentence is not used as a theorem about arbitrary connected graphs. The source immediately asks separately what happens at p_u. Therefore the intake's closed interval and claimed unresolved quasi-transitive/nonunimodular extensions are incorrect.

## Exact theorem quotes and how they answer the assertions

The following quotes reproduce the entire statements word for word, with subscripts, mathematical symbols and ligatures normalized from the PDF extraction. No hypotheses are added to or removed from the quoted statements.

**Theorem 5.6 (Schonmann [95])**, printed p.307 / PDF p.19; proof continues on printed p.308 / PDF p.20:

> “Let G be a transitive graph. Consider iid bond percolation on G and let N denote the number of infinite clusters. If p_1 < p_2 and P_{p_1}(N = 1) = 1, then also P_{p_2}(N = 1) = 1.”

Line-by-line application to the no-switching assertion:

1. Its G is exactly the asked transitive graph; no unimodularity assumption appears.
2. Its model is iid bond percolation, not a dependent or continuum model.
3. Given any p<q with almost-sure uniqueness at p, take p_1=p, p_2=q.
4. Its conclusion is almost-sure uniqueness at q. This excludes every switch from 1 back to infinity as p increases.
5. It does **not** give uniqueness at inf U when no parameter below inf U belongs to U. The interval consequence including this distinction is proved in ATTEMPT.md.

This theorem states and proves the intended no-switching assertion exactly. It was already known before the 2006 survey. We do not label the *combined literal supplied assertion* SOLVED_IN_LITERATURE because its additional closed-endpoint clause is false. The final SOLVED verdict records a fully checked counterexample deduction to that clause.

**Theorem 3.2 (Grimmett and Newman [42])**, printed p.299 / PDF p.11:

> “Let d ≥ 6, let G = T_d × Z, and consider an iid bond percolation X on G with retention parameter p. We then have p_c < 1 and the existence of p_1 and p_2 such that p_c < p_1 ≤ p_2 < 1 such that
> • for p ∈ (p_c, p_1), X contains a.s. infinitely many infinite clusters, whereas
> • if p ∈ (p_2, 1], X contains a.s. a unique infinite cluster.”

**Theorem 9.2 (Schonmann [94])**, printed p.321 / PDF p.33:

> “Let G = T_d × Z. Then a.s. percolation at p_u(G) does not produce a unique infinite cluster. In particular if d is chosen so that p_c < p_u, e.g. if d is sufficiently large, then percolation at p_u a.s. produces infinitely many infinite clusters.”

Theorem 9.2 alone is a result about a special graph, not the requested universal theorem. ATTEMPT.md explicitly verifies that T_6×Z is an allowed graph, derives p_c<p_u<1 from Theorems 3.2 and 5.6, applies Theorem 9.2 at its own p_u, and concludes U=(p_u,1]. That argument, rather than a loose comparison of related statements, is the counterexample.

Additional source checks: printed p.292 / PDF p.4 records theta_Z2(p_c)=0 and uniqueness for supercritical square-lattice percolation. Section 3, printed p.301 / PDF p.13, already contrasts uniqueness and nonuniqueness at p_u. Section 9 gives the more general product theorem (Theorem 9.3) and its proof, printed pp.321–323. We do not need to reprove that established product theorem to apply Theorem 9.2.

## Exact references used and relevant leads

* O. Häggström and Y. Peres (1999), **Monotonicity of uniqueness for percolation on transitive graphs: all infinite clusters are born simultaneously**, Probability Theory and Related Fields **113**, 273–285. DOI 10.1007/s004400050208. Survey reference [56]. Crossref currently gives the title with “Cayley graphs” instead of “transitive graphs”; the DOI, authors, journal pages and year identify the same item. The survey distinguishes the unimodular proof from Schonmann's unrestricted proof.
* R. H. Schonmann (1999), **Stability of infinite clusters in supercritical percolation**, Probability Theory and Related Fields **113**, 287–300. Survey [95]. This is the unrestricted monotonicity result used by Theorem 5.6. Crossref lookup details are retained in crossref_schonmann.txt.
* G. R. Grimmett and C. M. Newman (1990), **Percolation in ∞+1 dimensions**, in *Disorder in Physical Systems* (G. R. Grimmett and D. J. A. Welsh, eds.), Oxford University Press, pp.167–190. Survey [42]. Source of the two-phase product example, Theorem 3.2.
* R. H. Schonmann (1999), **Percolation in ∞+1 dimensions at the uniqueness threshold**, in *Perplexing Probability Problems: Papers in Honor of Harry Kesten* (M. Bramson and R. Durrett, eds.), Birkhäuser, Boston. Survey [94], MR1703124. The survey bibliography's printed page range appears inconsistent with the neighbouring coalescent chapter; we do not adopt that unchecked range as original-paper pagination. The precisely checked theorem location is survey Theorem 9.2, printed p.321.
* Y. Peres (2000), **Percolation on nonamenable products at the uniqueness threshold**, Annales de l'Institut Henri Poincaré, Probabilités et Statistiques **36**, 395–406. Survey [90]. Gives the more general product nonuniqueness theorem reproduced as Theorem 9.3.
* T. E. Harris (1960), **A lower bound for the critical probability in a certain percolation process**, Proceedings of the Cambridge Philosophical Society **56**, 13–20; H. Kesten (1980), **The critical probability of bond percolation on the square lattice equals 1/2**, Communications in Mathematical Physics **74**, 41–59. Survey [62], [76]. Used only for the independent Z2 endpoint check.
* **Percolation at the uniqueness threshold via subgroup relativization**, arXiv:2409.12283 (2024), fetched both as HTML and PDF. Its introduction states the classical three phases with strict inequalities and treats the endpoints separately. Theorem 1.1 proves nonuniqueness at p_u for every Cayley graph of Z2 wreath Γ when Γ is finitely generated and nonamenable. Theorem 1.4 and Corollary 1.5 concern subgroup-relative uniqueness for Cayley graphs. These are useful corroboration and leads, not substituted as an exact theorem about all transitive graphs. Author details from the fetched first page are recorded in the appended search results.
* S. Martineau and F. Severo, **Strict monotonicity of percolation thresholds under covering maps**, Annals of Probability (2019), DOI 10.1214/19-AOP1355; arXiv:1803.09686. Different question: changing graphs through coverings. Lead only.
* arXiv:2603.29420, **Uniqueness of the infinite cluster for monotone percolation models without insertion tolerance** (2026): dependent site models on Z^d, not the asked iid bond model. Abstract inspected; not an exact solution claim.
* arXiv:2606.11503, **Percolation on hierarchical lattices** (2026): hierarchical graph sequences and their limits, not the general asked theorem. Abstract inspected; lead only.

## Searches, responses and limitations

Scripts search.py, fetch_more.py and final_search.py retain the complete service URLs and queries, with dated JSON response logs search_log.json, more_log.json and final_search_log.json. Search.py was executed twice while shell startup was delayed; the first execution had TLS failures for arXiv, OpenAlex search, Crossref and GitHub and HTTP 429 for the source lookup and Semantic Scholar. On the second execution Crossref and the HTTP arXiv query succeeded; HTTPS arXiv, GitHub and OpenAlex search still failed in TLS. Responses from the later retries are separately retained.

Every search run:

1. **arXiv API HTTP**: `all:percolation AND all:uniqueness AND all:monotonicity`, max_results=20, at http://export.arxiv.org/api/query. Two executions: first TLS error after redirect; second HTTP 200, 15 entries. Inspect script read every returned title, abstract, date and identifier. Results include the 2024 subgroup paper and 2026 dependent/hierarchical papers; none purports to prove universal uniqueness at p_u.
2. **arXiv API HTTPS**: same query and limit, https://export.arxiv.org/api/query. Both executions failed in TLS.
3. **arXiv recent API**: `all:percolation AND all:uniqueness AND all:threshold`, sorted submittedDate descending, max_results=25. Both initial executions failed in TLS; a final max_results=20 retry is logged separately. No negative literature conclusion is drawn from failures.
4. **OpenAlex works search**: `percolation uniqueness monotonicity`, per-page=25. Both executions failed in TLS.
5. **OpenAlex source DOI**: `/works/https://doi.org/10.1214/154957806000000096`. Both executions returned 429. Source work ID could not be obtained; the initial dependent citation search could not run. Final direct DOI lookup and citation-filter attempt are logged separately; if the API does not accept a DOI as the cites identifier, that request cannot replace a successful citing-works search.
6. **Crossref works**: `percolation uniqueness monotonicity`, rows=20. First execution TLS failure; second HTTP 200. All returned entries inspected. Relevant hits were the 1999 monotonicity paper, the survey, and the 2019 covering-map paper; unrelated titles are retained in crossref.txt.
7. **Semantic Scholar paper search**: `percolation uniqueness monotonicity`, limit=20, fields title/authors/year/url/externalIds. Both executions 429. Final source DOI citations request logged separately.
8. **GitHub repository search**: `percolation uniqueness monotonicity`. Both executions failed in TLS. Retried as `percolation uniqueness`: HTTP 200; repository names and descriptions inspected and retained in the appended result record. Repository search is discovery, not mathematical evidence.
9. **arXiv exact-title search**: `ti:"Uniqueness and non-uniqueness in percolation theory"`, max_results=5: HTTP 200, exactly one record, math/0612812v1 with matching DOI and journal reference.
10. **OpenAlex exact-source-title search**: `Uniqueness and non-uniqueness in percolation theory`, per-page=5: 429.
11. **Crossref exact Schonmann title search**: `Stability of infinite clusters in supercritical percolation`, rows=3, final_search.py.
12. **OpenAlex direct DOI retry**: `/works/doi:10.1214/154957806000000096`, final_search.py.
13. **OpenAlex citing-works attempt**: `/works?filter=cites:https://doi.org/10.1214/154957806000000096&per-page=100&sort=publication_date:desc`, final_search.py. Attempt recorded even though the canonical OpenAlex work-ID lookup was rate-limited; no exhaustive citation check is claimed.
14. **Semantic Scholar citations**: `/graph/v1/paper/DOI:10.1214/154957806000000096/citations?fields=title,authors,year,url&limit=100`, final_search.py.

Document fetches: supplied Euclid PDF (TLS failure, then HTTP 200 error document); alternative Euclid `/journalArticle/Download?urlId=...` (HTTP 200 error document); arXiv HTML for math/0612812 (404, older paper has no HTML); arXiv PDF math/0612812v1 (200, successful PDF); HTML and PDF for 2409.12283 (200, successful). These fetches are not additional title searches.

## Brain and earlier-attempt audit (read only)

Ran math_recall.py on `Schonmann Haggstrom Peres uniqueness monotonicity`; read its returned cards, which contained no exact verified solution statement. Ran brain.py recall on `percolation uniqueness monotonicity mistakes` and `percolation uniqueness threshold`; no exact relevant theorem was established by recall. The recall command itself reported an internal index-refresh side effect; no brain write command was requested or executed by this worker.

Searched intake/pool ledgers for C0160 with rg. The original row explicitly encoded [p_u,1] and an alleged open extension. Its earlier attempt proposed uniqueness via two-point connectivity and conjectured extensions without source verification. These are not proof inputs.

Read only via git show origin/master the recorded `research7_2026-09-17/R7-01/admission/2026-09-18T222100Z__C0151_C0160_status_reconciliation.md`. It already flagged the Bernoulli scope mismatch and pointed to later quasi-transitive statements (Hutchcroft, *Percolation on Hyperbolic Graphs*, 2019; Tang, arXiv:1809.01284). We verified the central correction directly in the 2006 primary source, instead of treating the past worker's report as a verdict.

## Final response logs and inspected discovery results
### search_log.json

```json
[
  {
    "service": "arxiv",
    "url": "http://export.arxiv.org/api/query?search_query=all:percolation+AND+all:uniqueness+AND+all:monotonicity&max_results=20",
    "date": "2026-10-11",
    "status": 200,
    "bytes": 30486
  },
  {
    "service": "arxiv_https",
    "url": "https://export.arxiv.org/api/query?search_query=all:percolation+AND+all:uniqueness+AND+all:monotonicity&max_results=20",
    "date": "2026-10-11",
    "error": "HTTPSConnectionPool(host='export.arxiv.org', port=443): Max retries exceeded with url: /api/query?search_query=all:percolation+AND+all:uniqueness+AND+all:monotonicity&max_results=20 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)')))"
  },
  {
    "service": "openalex",
    "url": "https://api.openalex.org/works?search=percolation%20uniqueness%20monotonicity&per-page=25",
    "date": "2026-10-11",
    "error": "HTTPSConnectionPool(host='api.openalex.org', port=443): Max retries exceeded with url: /works?search=percolation%20uniqueness%20monotonicity&per-page=25 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)')))"
  },
  {
    "service": "openalex_source",
    "url": "https://api.openalex.org/works/https://doi.org/10.1214/154957806000000096",
    "date": "2026-10-11",
    "status": 429,
    "bytes": 610
  },
  {
    "service": "crossref",
    "url": "https://api.crossref.org/works?query=percolation%20uniqueness%20monotonicity&rows=20",
    "date": "2026-10-11",
    "status": 200,
    "bytes": 78654
  },
  {
    "service": "semantic_scholar",
    "url": "https://api.semanticscholar.org/graph/v1/paper/search?query=percolation%20uniqueness%20monotonicity&limit=20&fields=title,authors,year,url,externalIds",
    "date": "2026-10-11",
    "status": 429,
    "bytes": 174
  },
  {
    "service": "github",
    "url": "https://api.github.com/search/repositories?q=percolation+uniqueness+monotonicity",
    "date": "2026-10-11",
    "error": "HTTPSConnectionPool(host='api.github.com', port=443): Max retries exceeded with url: /search/repositories?q=percolation+uniqueness+monotonicity (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)')))"
  },
  {
    "service": "arxiv_endpoint",
    "url": "https://export.arxiv.org/api/query?search_query=all:percolation+AND+all:uniqueness+AND+all:threshold&sortBy=submittedDate&sortOrder=descending&max_results=25",
    "date": "2026-10-11",
    "error": "HTTPSConnectionPool(host='export.arxiv.org', port=443): Max retries exceeded with url: /api/query?search_query=all:percolation+AND+all:uniqueness+AND+all:threshold&sortBy=submittedDate&sortOrder=descending&max_results=25 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)')))"
  }
]
```
### more_log.json

```json
[
  {
    "service": "survey_arxiv_search",
    "url": "https://export.arxiv.org/api/query?search_query=ti:%22Uniqueness%20and%20non-uniqueness%20in%20percolation%20theory%22&max_results=5",
    "date": "2026-10-11",
    "status": 200,
    "bytes": 2869,
    "pdf": false
  },
  {
    "service": "survey_euclid_alt",
    "url": "https://projecteuclid.org/journalArticle/Download?urlId=10.1214%2F154957806000000096",
    "date": "2026-10-11",
    "status": 200,
    "bytes": 1163,
    "pdf": false
  },
  {
    "service": "survey_arxiv_html",
    "url": "https://arxiv.org/html/math/0612812",
    "date": "2026-10-11",
    "status": 404,
    "bytes": 7884,
    "pdf": false
  },
  {
    "service": "subgroup_html",
    "url": "https://arxiv.org/html/2409.12283v1",
    "date": "2026-10-11",
    "status": 200,
    "bytes": 692581,
    "pdf": false
  },
  {
    "service": "subgroup_pdf",
    "url": "https://arxiv.org/pdf/2409.12283",
    "date": "2026-10-11",
    "status": 200,
    "bytes": 410805,
    "pdf": true
  },
  {
    "service": "openalex_retry",
    "url": "https://api.openalex.org/works?search=Uniqueness%20and%20non-uniqueness%20in%20percolation%20theory&per-page=5",
    "date": "2026-10-11",
    "status": 429,
    "bytes": 610,
    "pdf": false
  },
  {
    "service": "github_retry",
    "url": "https://api.github.com/search/repositories?q=percolation+uniqueness",
    "date": "2026-10-11",
    "status": 200,
    "bytes": 12603,
    "pdf": false
  }
]
```
### final_search_log.json

```json
[
  {
    "service": "openalex_citations_attempt",
    "url": "https://api.openalex.org/works?filter=cites:https://doi.org/10.1214/154957806000000096&per-page=100&sort=publication_date:desc",
    "date": "2026-10-11",
    "error": "HTTPSConnectionPool(host='api.openalex.org', port=443): Max retries exceeded with url: /works?filter=cites:https://doi.org/10.1214/154957806000000096&per-page=100&sort=publication_date:desc (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)')))"
  },
  {
    "service": "openalex_doi_retry",
    "url": "https://api.openalex.org/works/doi:10.1214/154957806000000096",
    "date": "2026-10-11",
    "error": "HTTPSConnectionPool(host='api.openalex.org', port=443): Max retries exceeded with url: /works/doi:10.1214/154957806000000096 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)')))"
  },
  {
    "service": "semantic_citations",
    "url": "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1214/154957806000000096/citations?fields=title,authors,year,url&limit=100",
    "date": "2026-10-11",
    "status": 200,
    "bytes": 33900
  },
  {
    "service": "arxiv_recent_retry",
    "url": "https://export.arxiv.org/api/query?search_query=all:percolation+AND+all:uniqueness+AND+all:threshold&sortBy=submittedDate&sortOrder=descending&max_results=20",
    "date": "2026-10-11",
    "status": 200,
    "bytes": 45447
  },
  {
    "service": "crossref_schonmann",
    "url": "https://api.crossref.org/works?query.title=Stability%20of%20infinite%20clusters%20in%20supercritical%20percolation&rows=3",
    "date": "2026-10-11",
    "error": "HTTPSConnectionPool(host='api.crossref.org', port=443): Max retries exceeded with url: /works?query.title=Stability%20of%20infinite%20clusters%20in%20supercritical%20percolation&rows=3 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)')))"
  }
]
```
The final_search.py batch was run twice: the first run failed for all five requests (TLS or connection-aborted errors); the second response log above records the retry. Semantic Scholar citations and the recent arXiv query succeeded on retry; OpenAlex citing-works remained inaccessible.
### Inspected arxiv entries
* Uniqueness of the infinite cluster for monotone percolation models without insertion tolerance — Christoforos Panagiotis, Alexandre Stauffer — http://arxiv.org/abs/2603.29420v1 — 2026-03-31T08:26:26Z
* Percolation at the uniqueness threshold via subgroup relativization — Tom Hutchcroft, Minghao Pan — http://arxiv.org/abs/2409.12283v1 — 2024-09-18T19:36:51Z
* Percolation on hierarchical lattices — Caio Alves, Rangel Baldasso, Carlos Gustavo Moreira, Augusto Teixeira — http://arxiv.org/abs/2606.11503v1 — 2026-06-09T22:52:43Z
* Strict monotonicity of percolation thresholds under covering maps — Sébastien Martineau, Franco Severo — http://arxiv.org/abs/1803.09686v2 — 2018-03-26T16:08:41Z
* Strong existence, pathwise uniqueness and chains of collisions in infinite Brownian particle systems — Sayan Banerjee, Amarjit Budhiraja, Peter Rudzis — http://arxiv.org/abs/2501.07840v2 — 2025-01-14T04:51:57Z
* Strong local uniqueness for the vacant set of random interlacements — Subhajit Goswami, Pierre-François Rodriguez, Yuriy Shulzhenko — http://arxiv.org/abs/2503.14497v2 — 2025-03-18T17:58:47Z
* Non-uniqueness of phase transitions for graphical representations of the Ising model on tree-like graphs — Ulrik Thinggaard Hansen, Frederik Ravn Klausen, Peter Wildemann — http://arxiv.org/abs/2410.22061v2 — 2024-10-29T14:11:06Z
* Indistinguishability of unbounded components in the occupied and vacant sets of Boolean models on symmetric spaces — Yingxin Mu, Artem Sapozhnikov — http://arxiv.org/abs/2504.05027v1 — 2025-04-07T12:51:14Z
* Factor of iid's through stochastic domination — Ádám Timár — http://arxiv.org/abs/2306.15120v2 — 2023-06-27T00:09:37Z
* Generalized Hammersley Process and Phase Transition for Activated Random Walk Models — Leonardo T. Rolla — http://arxiv.org/abs/0812.2473v1 — 2008-12-14T14:32:25Z
* Connectivity of Heterogeneous Wireless Networks — Wei Ren, Qing Zhao, Ananthram Swami — http://arxiv.org/abs/0903.1684v5 — 2009-03-10T05:37:29Z
* Cutoff with an $O(1)$ window for Potts Glauber Dynamics on lattice at High Temperature — Seoyeon Yang, Allan Sly — http://arxiv.org/abs/2608.26259v1 — 2026-08-26T18:00:04Z
* Robustness analysis of bimodal networks in the whole range of degree correlation — Shogo Mizutaka, Toshihiro Tanizawa — http://arxiv.org/abs/1607.03562v1 — 2016-07-13T01:36:29Z
* Synergistic interactions between DNA and actin trigger emergent viscoelastic behavior — Robert Fitzpatrick, Davide Michieletto, Karthik R. Peddireddy, Cole Hauer, Carl Kyrillos, Bekele J. Gurmessa, Rae M. Robertson-Anderson — http://arxiv.org/abs/1805.09931v2 — 2018-05-24T23:14:37Z
### Inspected arxiv_recent_retry entries
* $β$-Skewed Maximal Spanning Forests — Shirshendu Chatterjee, Yang Chen, Grigory Terlov — http://arxiv.org/abs/2609.11845v1 — 2026-09-10T17:33:24Z
* Third-order nonlinear transport in a percolative two-dimensional superconductor — Wenjun Liu, Chenghe Wang, Xiubin Li, Kenji Watanabe, Takashi Taniguchi, Tao Zhang, Xiao-Xiao Zhang, Jing Li — http://arxiv.org/abs/2607.27641v1 — 2026-07-30T03:52:04Z
* Non-vanishing uniqueness threshold for hyperbolic Poisson-Voronoi percolation in dimension at least three — Matthias Irlbeck, Tobias Müller — http://arxiv.org/abs/2607.17764v1 — 2026-07-20T09:59:39Z
* Percolation on hierarchical lattices — Caio Alves, Rangel Baldasso, Carlos Gustavo Moreira, Augusto Teixeira — http://arxiv.org/abs/2606.11503v1 — 2026-06-09T22:52:43Z
* The critical activation density in graph bootstrap percolation — Brett Kolesnik, Tamás Makai, Rajko Nenadov, Xavier Pérez-Giménez, Paweł Prałat, Maksim Zhukovskii — http://arxiv.org/abs/2605.15066v2 — 2026-05-14T16:56:35Z
* Sharp Phase Transition for the Formation of Infinite Tubes — Shu Kanazawa, Omer Bobrowski, Primoz Skraba — http://arxiv.org/abs/2605.14910v1 — 2026-05-14T14:44:28Z
* Percolation Critical Probability of Aperiodic Smith Hat tile(1, $\sqrt3$) — Haitao Gao, Aaryash Bharadwaj — http://arxiv.org/abs/2604.21165v1 — 2026-04-23T00:16:32Z
* Uniqueness and Mixing in the Low-Temperature Random-Cluster Model on Trees and Random Graphs — Antonio Blanca, Reza Gheissari, Heehyun Park, Xusheng Zhang — http://arxiv.org/abs/2604.20693v1 — 2026-04-22T15:39:26Z
* ln(3): A Universal Percolation Constant for Collective Dynamics on One-Dimensional Proximity Networks — Jian Ji — http://arxiv.org/abs/2603.15521v1 — 2026-03-16T16:46:57Z
* Emergent Coherence at the Edge of Magnetism: Low-Doped La2-xSrxCuO4+delta Revisited — E. Yu. Beliayev, Y. K. Mishra, I. A. Chichibaba, I. G. Mirzoiev, V. A. Horielyi, A. V. Terekhov — http://arxiv.org/abs/2602.04452v1 — 2026-02-04T11:25:34Z
* Flat-band Ferromagnetism of SU$(N)$ Hubbard Model on the Kagome Lattices — Hao Jin, Wenxing Nie — http://arxiv.org/abs/2601.10549v2 — 2026-01-15T16:14:45Z
* Planar Site Percolation, End Structure, and the Benjamini-Schramm Conjecture — Zhongyang Li — http://arxiv.org/abs/2601.09958v2 — 2026-01-15T00:34:33Z
* Vanishing uniqueness thresholds in Voronoi percolation on products — Matteo D'Achille, Jan Grebík, Ali Khezeli, Konstantin Recke, Amanda Wilkens — http://arxiv.org/abs/2511.23317v1 — 2025-11-28T16:15:40Z
* Negativity Percolation in Continuous-Variable Quantum Networks — Yaqi Zhao, Kan He, Yongtao Zhang, Jinchuan Hou, Jianxi Gao, Shlomo Havlin, Xiangyi Meng — http://arxiv.org/abs/2507.16417v3 — 2025-07-22T10:09:21Z
* Representation of Archimedean Networks and Inclusion: Computational Applications to Percolation and Network Transitions — Auro Anibal Torres, José Antonio Ramirez-Pastor — http://arxiv.org/abs/2507.12229v1 — 2025-07-16T13:42:08Z
* Poisson-Voronoi percolation in higher rank — Jan Grebík, Konstantin Recke — http://arxiv.org/abs/2504.02435v1 — 2025-04-03T09:50:22Z
* Connectivity for square percolation and coarse cubical rigidity in random right-angled Coxeter groups — Jason Behrstock, R. Altar Ciceksiz, Victor Falgas-Ravry — http://arxiv.org/abs/2502.18165v1 — 2025-02-25T12:51:33Z
* Weighted-amenability and percolation — Grigory Terlov, Ádám Timár — http://arxiv.org/abs/2502.02560v2 — 2025-02-04T18:36:33Z
* Dimension jump at the uniqueness threshold for percolation in $\infty+d$ dimensions — Tom Hutchcroft, Minghao Pan — http://arxiv.org/abs/2412.15895v1 — 2024-12-20T13:49:47Z
* Percolation at the uniqueness threshold via subgroup relativization — Tom Hutchcroft, Minghao Pan — http://arxiv.org/abs/2409.12283v1 — 2024-09-18T19:36:51Z

Fetched 2024 paper authors: Tom Hutchcroft and Minghao Pan. Version arXiv:2409.12283v1; first-page manuscript date September 20, 2024.

GitHub query returned SamuelHaleDev/Percolation (student finite Monte Carlo assignment) and AaagIndia123/Fire-Hoses-and-Accessories-Manufacturers (unrelated). Neither supplies relevant research evidence.

### Semantic Scholar citing papers inspected

Pagination metadata: {'offset': 0}

* Infinite light rays and infinite clusters with infinitely many pivots — 2026 — M. Zerner — https://www.semanticscholar.org/paper/61afdc110dc5371cb7a6bbc9cef606f60847183b
* FIID Coloring Random Maps — 2026 — Justin Hsu, Daniel Sium, R. Thornton — https://www.semanticscholar.org/paper/0defe3c98e9222c148770c3f1700f841470f3286
* Zero-temperature stochastic Ising model on one-dimensional quasi-transitive graphs — 2026 — E. De Santis — https://www.semanticscholar.org/paper/bfb587bc76c8b72377161fe4c3582a077d5f90e3
* Uniqueness of the infinite cluster for monotone percolation models without insertion tolerance — 2026 — C. Panagiotis, Alexandre O. Stauffer — https://www.semanticscholar.org/paper/59d605d60851498952f0e93b4055fb5d5386eaeb
* The Poisson stick model in hyperbolic space — 2025 — Erik I. Broman, Johan H. Tykesson — https://www.semanticscholar.org/paper/c1e17bcb37c10cd273a7dab6d9ac795076d92c51
* Vanishing uniqueness thresholds in Voronoi percolation on products — 2025 — M. D'Achille, Jan Greb'ik, Ali Khezeli, Konstantin Recke, A. Wilkens — https://www.semanticscholar.org/paper/b30546c43e46e29d69e170982352864cd4dcd6df
* Chemical distance in graphs of polynomial growth — 2025 — C. Gorski, Eviatar B. Procaccia — https://www.semanticscholar.org/paper/c785d8577bf2f21145eeb9c99aa9bca64fdac354
* Indistinguishability of unbounded components in the occupied and vacant sets of Boolean models on symmetric spaces — 2025 — Ying-Xin Mu, A. Sapozhnikov — https://www.semanticscholar.org/paper/caac704d1575daaa716b80765b3d0ea414a00371
* Quantum percolation on Lieb Lattices. — 2024 — W. S. Oliveira, J. P. de Lima, R. R. dos Santos — https://www.semanticscholar.org/paper/6c8bae6533c7e95f1f9bd33a8fb1dc9564b48823
* Coarse embeddability, $L^1$-compression and Percolations on General Graphs — 2024 — Chiranjib Mukherjee, Konstantin Recke — https://www.semanticscholar.org/paper/b1f8647e0c1c98483c30285a6dcdcd414149bd68
* A characterization of strong percolation via disconnection — 2023 — H. Duminil-Copin, Subhajit Goswami, Pierre-François Rodriguez, Franco Severo, A. Teixeira — https://www.semanticscholar.org/paper/67d6128ebf334dd8b7b7215039d30a514de2eb99
* Zero-Temperature Stochastic Ising Model on Planar Quasi-Transitive Graphs — 2023 — E. De Santis, Leonardo Lelli — https://www.semanticscholar.org/paper/ca159d076798e3df7c818981da3047ed2867b112
* On questions of uniqueness for the vacant set of Wiener sausages and Brownian interlacements — 2023 — Ying-Xin Mu, A. Sapozhnikov — https://www.semanticscholar.org/paper/a4968409de9d971a2aa5936263110f049091ef03
* Haagerup property and group-invariant percolation — 2023 — Chiranjib Mukherjee, Konstantin Recke — https://www.semanticscholar.org/paper/c998f95eb114ebe36190c37f5c96204ee52cf3e2
* Uniqueness of the infinite connected component for the vacant set of random interlacements on amenable transient graphs — 2023 — Ying-Xin Mu, A. Sapozhnikov — https://www.semanticscholar.org/paper/8b9aa95ca1b9ef73418ab435800fcb0d551b3dc8
* Martingales for physicists: a treatise on stochastic thermodynamics and beyond — 2022 — É. Roldán, I. Neri, R. Chetrite, Shamik Gupta, S. Pigolotti, F. Jülicher, Ken Sekimoto — https://www.semanticscholar.org/paper/f81c6cbd186207358923f67db9f5f7a20653276b
* Surviving ends in Bernoulli percolation on graphs roughly isometric to a tree — 2022 — Kai-Nan Xiang, L. Zou — https://www.semanticscholar.org/paper/8cb9c7fc320dc4196fe7c04fb9783d764ccf8987
* First passage percolation with long-range correlations and applications to random Schrödinger operators — 2021 — S. Andres, Alexis Prévost — https://www.semanticscholar.org/paper/d70c140553faf046c3593db3c5a6e0ee43f3a206
* Cylinders’ percolation: Decoupling and applications — 2021 — C. Alves, Augusto Teixeira — https://www.semanticscholar.org/paper/2025eb0200c24ff1a0c260359bc3bb371b15a2de
* Phase Transition for Level-Set Percolation of the Membrane Model in Dimensions 
 
 
 
 $$d \ge 5$$
 
 
 d
 ≥
 5
 
 
 — 2021 — Alberto Chiarini, Maximilian Nitzschner — https://www.semanticscholar.org/paper/80849636f6555318d251b9e5caa7f7fc9b8cd14d
* Homology-changing percolation transitions on finite graphs — 2020 — Michael Woolls, L. Pryadko — https://www.semanticscholar.org/paper/59f9839bdd446a354a7fe0b1ac462a04fb6b02b0
* On (Non-)Monotonicity and Phase Diagram of Finitary Random Interlacement — 2020 — Zhenhao Cai, Yun-Feng Xiong, Yuan Zhang — https://www.semanticscholar.org/paper/411b47eac9d73548c3cc8301eb569de0cc0b05ae
* The Constrained-degree percolation model — 2020 — B. D. de Lima, R. Sanchis, Diogo C. dos Santos, V. Sidoravicius, R. Teodoro — https://www.semanticscholar.org/paper/7312022d3eca763b14fb495dee8965acf819b79d
* Three lectures on random proper colorings of $\mathbb{Z}^d$ — 2020 — Ron Peled, Yinon Spinka — https://www.semanticscholar.org/paper/51cbac7f5e1ccaedbe776def3dd53095ffe3f456
* On the site percolation threshold of circle packings and planar graphs — 2020 — Ron Peled — https://www.semanticscholar.org/paper/0fd8503524921a29c5dd6b0533936a86b1ea56b2
* Non-intersection of transient branching random walks — 2019 — Tom Hutchcroft — https://www.semanticscholar.org/paper/a0cecd2370e6ceaba8ace9d23dfb48e0b2d592dc
* Local picture and level-set percolation of the Gaussian free field on a large discrete torus — 2019 — Angelo Abächerli — https://www.semanticscholar.org/paper/4a5a21c3a2312073a50525102a3417b1d071638d
* Percolation for the Finitary Random interlacements — 2019 — Eviatar B. Procaccia, Jiayan Ye, Yuan Zhang — https://www.semanticscholar.org/paper/1aa5f926cabebdfa6914cd1da50765e573893808
* Percolation on Hyperbolic Graphs — 2019 — Tom Hutchcroft — https://www.semanticscholar.org/paper/77e66d58dcb80275c38387d77c71649367268044
* The $L^{2}$ boundedness condition in nonamenable percolation — 2019 — Tom Hutchcroft — https://www.semanticscholar.org/paper/f62e1889602e82d03b46d239a7ebd5e3ce245eed
* Delocalization of Uniform Graph Homomorphisms from Z2\documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}$${\mathbb {Z}}^2$$ — 2018 — Nishant Chandgotia, Ron Peled, S. Sheffield, M. Tassy — https://www.semanticscholar.org/paper/50c0287a267059ffd34697408ed845e67af545f9
* Duality and free energy analyticity bounds for few-body Ising models with extensive homology rank — 2018 — Yi Jiang, I. Dumer, A. Kovalev, L. Pryadko — https://www.semanticscholar.org/paper/c789b8d837f65a0af8a720ef80fee20517d374e3
* Percolation on Hyperbolic Graphs — 2018 — Tom Hutchcroft — https://www.semanticscholar.org/paper/cdbe040f489ec72b7d41db6bae53a6eb4a85bfde
* Nonuniqueness and mean-field criticality for percolation on nonunimodular transitive graphs — 2017 — Tom Hutchcroft — https://www.semanticscholar.org/paper/886a190bbd45179b2d4ba89bcfd074de36091542
* Lectures on the Spin and Loop O(n) Models — 2017 — Ron Peled, Yinon Spinka — https://www.semanticscholar.org/paper/b98ae06b16403677da02b59e374cfcbafed06206
* Local picture and level-set percolation of the Gaussian free field on a large discrete torus — 2017 — Angelo Abächerli — https://www.semanticscholar.org/paper/2ffe92ce2e43f5439a55a176464ef8e8f552cc5c
* Amenability of Groups and G -Sets — 2017 — L. Bartholdi — https://www.semanticscholar.org/paper/7323cf789028f1f45b3426e0374827464586c6a4
* Gilbert's disc model with geostatistical marking — 2017 — Daniel Ahlberg, Johan H. Tykesson — https://www.semanticscholar.org/paper/161e3237b1dd84569734ccec1e7bf6e597fb9d3b
* Exponential decay of connectivity and uniqueness in percolation on finite and infinite graphs — 2016 — Kathleen E. Hamilton, L. Pryadko — https://www.semanticscholar.org/paper/4b1e7f161e00bbd2ec6f4e58c941fef267eed9f5
* Random coalescing geodesics in first-passage percolation — 2016 — Daniel Ahlberg, C. Hoffman — https://www.semanticscholar.org/paper/e2c3cd3fd1fcc6f02934566ebf4a09e3e812db5b
* The Incipient Giant Component in Bond Percolation on General Finite Weighted Graphs — 2016 — D. Aldous — https://www.semanticscholar.org/paper/b3f10850b14cb8e3e66fd8bb936a1ce2478f8169
* Graphical Representations for Ising and Potts Models in General External Fields — 2015 — L. Cioletti, Roberto Vila — https://www.semanticscholar.org/paper/3f4d471e6fa0caccd64b16a17e4488d7153898d0
* Poisson cylinders in hyperbolic space — 2015 — Erik I. Broman, Johan H. Tykesson — https://www.semanticscholar.org/paper/13688a5d409da5b7144f716809ddf3de1b145a07
* Percolation and local isoperimetric inequalities — 2015 — A. Teixeira — https://www.semanticscholar.org/paper/8f451979b23c6cd3d0487e3b6af789fa1010b071
* Percolation and isoperimetry on roughly transitive graphs — 2015 — Elisabetta Candellero, A. Teixeira — https://www.semanticscholar.org/paper/befea1fba3d65ca922a4e6f1967e00b58dce306e
* Percolation and isoperimetry on transitive graphs — 2015 — Elisabetta Candellero, A. Teixeira — https://www.semanticscholar.org/paper/506041d4499429c6b194e7c1bb9d9d93ef80efe2
* Graphical Representations for Ising and Potts Models in General External Fields — 2015 — L. Cioletti, Roberto Vila — https://www.semanticscholar.org/paper/de6ca91291ccc7d1d4f784a858b8a512fd48316d
* Algebraic bounds for heterogeneous site percolation on directed and undirected graphs — 2015 — Kathleen E. Hamilton, L. Pryadko — https://www.semanticscholar.org/paper/f8577f05f6b6a156b1d8190f613e32cfb52fabdc
* Sobre processos de aglomeração distribuída — 2014 — Silverio Lucio de Moura — https://www.semanticscholar.org/paper/26601f9e676746c7cbf7bb2cc6498d4dff1c47f7
* Boolean Percolation on Doubling Graphs — 2014 — Cristian F. Coletti, Daniel Miranda, Sebastián P. Grynberg — https://www.semanticscholar.org/paper/59c28666721471bdfa7af5cb0b4358d41d99fcf3
* Absence of Boolean Percolation on Doubling Graphs — 2014 — Cristian F. Coletti, Sebastián P. Grynberg, Daniel Miranda — https://www.semanticscholar.org/paper/e081ae729e1298395f03ca6ab5b47d885a98b090
* Percolation and local isoperimetric inequalities — 2014 — A. Teixeira — https://www.semanticscholar.org/paper/62bdce41f2e16449c0dc34372630ecb0c7ec445c
* From loop clusters and random interlacement to the free field — 2014 — Titus Lupu — https://www.semanticscholar.org/paper/197fa967de40039f5acf3026f53d9d3b4e50af21
* From loop clusters of parameter 1/2 to the Gaussian free field — 2014 — Titus Lupu — https://www.semanticscholar.org/paper/408d5d830e0dcf166aca9ee930460a0535905d9f
* Two Badly Behaved Percolation Processes on a Nonunimodular Graph — 2013 — Olle Häggström — https://www.semanticscholar.org/paper/e1c039760b7be24462ef35e64e0af01a4b24d258
* A lower bound on the two-arms exponent for critical percolation on the lattice — 2013 — R. Cerf — https://www.semanticscholar.org/paper/0d0f6bc18f9c80bc17d206c144b410fc079103d9
* Basic properties of critical lognormal multiplicative chaos — 2013 — J. Barral, A. Kupiainen, Miika Nikula, Eero Saksman, Christian Webb — https://www.semanticscholar.org/paper/023e96066201fc50520c6147dda9fad339d4c4cc
* Level set percolation for random interlacements and the Gaussian free field — 2013 — Pierre-François Rodriguez — https://www.semanticscholar.org/paper/88654b3f83848eb8b41a05f807910407245a63c2
* Bernoulli and self-destructive percolation on non-amenable graphs — 2013 — Daniel Ahlberg, V. Sidoravicius, Johan H. Tykesson — https://www.semanticscholar.org/paper/49703decf9feb53324eee4962d757199c89e433a
* A Pairwise Averaging Procedure with Application to Consensus Formation in the Deffuant Model — 2012 — Olle Häggström — https://www.semanticscholar.org/paper/3a0b14d09c34ba8e0be47a469aa216c6c59a737b
* Non-amenable Cayley graphs of high girth have $p_c < p_u$ and mean-field exponents — 2012 — Asaf Nachmias, Y. Peres — https://www.semanticscholar.org/paper/d256e83659b01001a00e286293d05b7b38b78967
* Phase Transition and Level-Set Percolation for the Gaussian Free Field — 2012 — Pierre-François Rodriguez, A. Sznitman — https://www.semanticscholar.org/paper/ef29e44ab5f31b2d96a40727fb98b8bf0e4866b4
* A Pairwise Averaging Procedure with Application to Consensus Formation in the Deffuant Model — 2012 — Olle Häggström — https://www.semanticscholar.org/paper/212fe2e0067749ee6622bf8abd678e2ed0ae27dd
* Two Badly Behaved Percolation Processes on a Nonunimodular Graph — 2011 — Olle Häggström — https://www.semanticscholar.org/paper/338e4300367231862d1a6cbec430efefff5f218d
* Percolation beyond ${\mathbb{Z}}^{\bolds{d}}$: The contributions of Oded Schramm — 2011 — O. Haggstrom — https://www.semanticscholar.org/paper/40024d3e4a16e7ed9831833ad9ee27cc576dd8bb
* Percolation: Inference and Applications in Hydrology — 2011 — Oscar Hammar — https://www.semanticscholar.org/paper/ddbf00a0a0bd7df51849526a1f5ffc0763c62b3b
* On the critical value function in the divide and color model — 2011 — Andr'as B'alint, V. Beffara, V. Tassion — https://www.semanticscholar.org/paper/e5bba1482d1f2375783f406e62c919b2587ee4bb
* Percolation beyond ℤd: the contributions of Oded Schramm* — 2011 — Olle Häggström — https://www.semanticscholar.org/paper/5c0a307ea58b303c943d231748b7fd1715bf0c1b
* Percolation in the secrecy graph — 2011 — Amites Sarkar, M. Haenggi — https://www.semanticscholar.org/paper/086ebe629ee39b34297d2d1bde494ee668440d19
* Random interlacements and amenability — 2011 — A. Teixeira, Johan H. Tykesson — https://www.semanticscholar.org/paper/43ebad1a184b3e486b9689212f332a0e12e42e41
* Trees, Animals, and Percolation on Hyperbolic Lattices — 2010 — N. Madras, C. Wu — https://www.semanticscholar.org/paper/eb6bbf12c1523388bcd1eaa0d42bea4e046de8d4
* Visibility to infinity in the hyperbolic plane, despite obstacles — 2008 — I. Benjamini, J. Jonasson, O. Schramm, Johan H. Tykesson — https://www.semanticscholar.org/paper/69902dedb9d2fcca9f92f79a27010c78787e9a67
* On the uniqueness of the infinite cluster of the vacant set of random interlacements — 2008 — A. Teixeira — https://www.semanticscholar.org/paper/29b67b420184583257b14aa6974bbf1e26fdfbdd
* Continuum Percolation at and above the Uniqueness Threshold on Homogeneous Spaces — 2007 — Johan H. Tykesson — https://www.semanticscholar.org/paper/c6f8e964436aa63a927c6e5328e5b92ce29dda71
* Some Group Theory Problems — 2007 — M. Sapir — https://www.semanticscholar.org/paper/800041801d2d04bbd2abacb308d2bd7b83c6ad0a
* Vacant Set of Random Interlacements and Percolation — 2007 — A. Sznitman — https://www.semanticscholar.org/paper/303ad61a723a257aca197d7caad307391edac040
* The number of unbounded components in the Poisson Boolean model in hyperbolic space — 2006 — Johan H. Tykesson — https://www.semanticscholar.org/paper/09420acca5d4701c26e9c145bb2165bd3e8b4eb4
* Poisson Boolean model of continuum percolation in hyperbolic space — 2021 — Johan H. Tykesson — https://www.semanticscholar.org/paper/56b936a98ac384496588aba7563bdee1864f6cbd
* Three lectures on random proper colorings of Z — 2020 — Ron Peled, Yinon Spinka — https://www.semanticscholar.org/paper/ad28923afd41e0fa47202ec89b02fc7f5af4e388
* PR ] 1 M ar 2 01 8 Poisson cylinders in hyperbolic space — 2018 — Erik I. Broman, Johan H. Tykesson — https://www.semanticscholar.org/paper/47854bf73979a19820b749f2e03e9b131fa511b3
* DELOCALIZATION OF UNIFORM GRAPH HOMOMORPHISMS FROM Z TO Z — 2018 — Ron Peled, S. Sheffield — https://www.semanticscholar.org/paper/481cf51bb1486cdb1b747f93e1a44ba37bf1567a
* Recueil de modèles aléatoires — 2016 — Djalil CHAFAÏ, Florent Malrieu — https://www.semanticscholar.org/paper/d331cce31fb7d2c9e6d2dbaa88ba23245cf3af72
* On level set percolation for the Gaussian free field — 2015 — Pierre-François Rodriguez — https://www.semanticscholar.org/paper/987f9bda71ed46259bdd067b53a5294c645f8c87
* From random walk trajectories to random interlacements — 2013 — A. Teixeira, J. Černý — https://www.semanticscholar.org/paper/418f3224dd06226b534d2c48f42b090afb79960d
* PR ] 2 3 Fe b 20 12 PHASE TRANSITION AND LEVEL-SET PERCOLATION FOR THE GAUSSIAN FREE FIELD Preliminary Draft — 2012 —  — None
* Percolation beyond 7 l d : the contributions of Oded Schramm — 2011 — O. Schramm, R. Lyons — https://www.semanticscholar.org/paper/daf0c6a6da437686e3ec3a04351e85154f25084f
* PERCOLATION AND THE EXISTENCE OF THE INFINITE OPEN CLUSTER — 2010 — Riley Heckel — https://www.semanticscholar.org/paper/5b352d09ac7729f63947e51f58067dac8939b100
* Percolation beyond Z d : the contributions of Oded Schramm ∗ — 2010 — Olle Häggström — https://www.semanticscholar.org/paper/8265d559ed63fdf7496f9e746f752bcc039ee3b5
* Percolative properties of random interlacements — 2010 — A. Teixeira — https://www.semanticscholar.org/paper/35115d375bf6f6d195a4a41439bfe0c3980c7b98
* Computability of Percolation Thresholds — 2008 — Olle Häggström — https://www.semanticscholar.org/paper/5723aedcf7f49b426fa22f72408a0477e43ae24b
* The Number of unbounded Components in the Poisson-Boolean Model in H2 — 2005 — Johan H. Tykesson — https://www.semanticscholar.org/paper/25c27b8948902331e0fd9a05e1f6dd6ac3ee2550
* A Complete Bibliography of Publications in Probability Surveys — None — Nelson H. F. Beebe — https://www.semanticscholar.org/paper/4caa80e44689634ad284ff86bbf93e1aa76eb430
