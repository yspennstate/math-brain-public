# I0070 literature and source check — 2026-10-12

## Exact source

Antonio Agresti and Mark Veraar, **Nonlinear SPDEs and Maximal Regularity: An Extended Survey**, *NoDEA Nonlinear Differential Equations and Applications* **32** (2025), article 123. DOI: https://doi.org/10.1007/s00030-025-01090-2. Published version retrieved from https://repository.tudelft.nl/file/File_783e6459-5d3b-4957-bcd3-64da5b8d9025 (HTTP 200, 2,652,440 bytes; 151 PDF pages including repository cover). Saved as source.pdf and source.txt.

Problem 6, printed p.130 / repository PDF p.131:

> Problem 6. (Time regularization in Hilbert spaces) Let X0 be a Hilbert space. Does the regularization result of Theorem 5.7 extend to p = 2 in the critical case (i.e. equality in (6.1) holds for some j)?

Relevant source locations: Assumption 4.1 printed pp.38–39; Theorem 4.7 printed pp.42–43; Theorem 5.7 printed pp.59–60; equation (6.1) printed p.65; Problem 6 printed p.130. The repository PDF page is one larger than the printed page.

Theorem 5.7 assumes all conditions of Theorem 4.7, p>2 and κ=0, the extra locally X_{1−1/p,∞}-bounded growth estimate (5.21) with X_{β_j,1} powers ρ_j+1, and (A,B)∈SMR^bullet_{r,α} for every finite r>2 and 0≤α<r/2−1. It concludes almost-sure local H^{θ,r}(X_{1−θ}) and C^{θ−ε}(X_{1−θ}) regularity for θ<1/2. The p=2 endpoint specialization retains these other hypotheses. A shift λ0+A, not necessarily A itself, is sectorial in Assumption 4.1.

## Search record and limitations

All requests used Python requests or curl.exe through the shell. Raw responses and exact query URLs are saved in search_log.json, search_more_log.json and followup_log.json; search_summary.json preserves screened metadata. The complete URLs in those logs are part of this search record, including failed requests.

Initial searches:

- arXiv export API: `all:"Agresti" AND all:"regularity"`, submitted-date descending, max_results=30. HTTP 200. Screened titles/abstracts, including 2025–2026 follow-ups. Raw Atom response is arxiv.json.
- OpenAlex works search: `Nonlinear SPDEs and maximal regularity`, per-page=15. TLS EOF failure.
- Crossref works bibliographic search: `Agresti Veraar Nonlinear SPDEs maximal regularity`, rows=15. HTTP 200.
- Semantic Scholar paper search: `Agresti Veraar regularity`, limit=30, fields title/authors/year/url/externalIds. HTTP 429 (rate limited).
- GitHub repository search: `Agresti Veraar regularity`. TLS EOF failure.
- arXiv source PDF 2501.18561 and lead PDF 2509.07803. Both HTTP 200; saved PDF and extracted text.

Additional searches:

- OpenAlex DOI work lookup for `10.1007/s00030-025-01090-2`. TLS EOF failure; the Python branch for citing works could not run without the work ID.
- OpenAlex works search: `critical time regularization Hilbert`, per-page=20. TLS EOF failure.
- GitHub repository search: `"stochastic maximal regularity"`. TLS EOF failure.
- Semantic Scholar DOI lookup for the source, fields `title,year,citations.title,citations.year,citations.externalIds`. HTTP 200; returned the source and 40 citing records. Saved in semantic_doi.json. This provided a successful citing-source search despite OpenAlex access failures.
- arXiv export API, HTTP endpoint: `all:"time regularization" AND all:"stochastic"`, max_results=30. Timed out after redirect to HTTPS.
- Crossref works search: `critical Hilbert time regularization stochastic`, from-pub-date=2025-01-01, rows=20. HTTP 200; screened results were predominantly unrelated uses of regularization.

Further arXiv abstract/PDF checks and native-curl retries are recorded in followup_log.json and will be incorporated below when completed. Failed services are not treated as successful negative searches. This bounded check cannot certify worldwide openness or novelty.

## Relevant references and scope

1. Agresti–Veraar, the source above; arXiv:2501.18561v5. The current published source still poses Problem 6. Its subcritical Proposition 5.9 is not the critical endpoint theorem.
2. Antonio Agresti and Mark C. Veraar, **Nonlinear parabolic stochastic evolution equations in critical spaces part II: Blow-up criteria and instantaneous regularization**, *Journal of Evolution Equations* **22** (2022), article 56, 96 pp. DOI: https://doi.org/10.1007/s00028-022-00786-7. The source cites Proposition 6.8 for a restricted p=2 critical regularization argument. Corollary 3.15 provides small stochastic-leading-operator perturbation stability, as identified in earlier research notes. These are ingredients/leads; no theorem is claimed to settle Problem 6 as posed. The present attempt proves its needed zero-trace perturbation step directly from the survey's Definitions 3.7–3.8.
3. Antonio Agresti and Mark Veraar, **A Note on a threshold for temporal regularity of stochastic PDEs**, arXiv:2509.07803, downloaded current PDF. Theorem 1.1, PDF p.2, states that for positive invertible self-adjoint A and constant noise x, u∈L^2(Ω;W^{α,2}(0,T;D(A^{1/2}))) iff x∈D(A^α), 0≤α<1/2. Theorem 1.3, PDF p.3, gives the corresponding variational statement. This is a genuine obstruction to keeping the spatial level fixed. It is **not** a counterexample to the X_{1−θ} parabolic trade in Problem 6.
4. Antonio Agresti and Mark C. Veraar, **Nonlinear parabolic stochastic evolution equations in critical spaces part I: Stochastic maximal regularity and local existence**, *Nonlinearity* **35** (2022), 4100–4210. This is foundational local-existence input cited by the source; not an endpoint resolution.
5. Antonio Agresti and Mark Veraar, **The critical variational setting for stochastic evolution equations**, *Probability Theory and Related Fields* **188** (2024), 957–1015. This supplies the critical Hilbert/variational solution framework; not the higher-integrability result asked here.

## Earlier local research, not literature certification

Read-only brain/math-store recall recovered the prior P0270 diagnostic, which correctly warned against misusing the fixed-spatial-level noise obstruction. Read-only `git show origin/master:<path>` recovered R10's 2026-09-16 compact-tail, stopped-perturbation, zero-trace, and final handoff reports; saved together as prior_attempts.md. The last report labeled its compact-tail argument an author-side full-source candidate pending outside audits. Those administrative labels neither prove nor disprove its mathematics. The current ATTEMPT.md writes and checks the argument directly. No repository was edited or committed.

No paper has yet been verified to state and prove this exact endpoint question under the same hypotheses and quantifiers. Consequently **SOLVED_IN_LITERATURE is not asserted**.

## Follow-up inspection

The native curl OpenAlex DOI lookup returned a JSON rate-limit response: the shared unauthenticated daily budget is exhausted. Its lack of a work ID prevented the work-ID citation request. A separate DOI-form citing-works request was attempted and is logged in curl_followup_log.json; a failure is not counted as a successful citation search. No credentials were accessed or requested.

The native curl GitHub query `Agresti Veraar regularity` succeeded and returned `total_count: 0`, `incomplete_results: false`.

Simon Bau, Gideon Chiusole, Sarah Geiss, Katharina Klioba and Tobias Werner, **The stochastic Cahn–Hilliard equation in critical spaces**, arXiv:2608.21014v1 (2026), was downloaded and inspected. Lemma 5.9 and the surrounding Remark 5.8 treat p=q=2 in a specific fourth-order PDE on bounded smooth domains. They use flexible spatial settings and the older Part-II Proposition 6.8, followed by spatial bootstrapping. Remark 5.8 explicitly notes that direct temporal regularisation is unavailable in the general critical p=2 setting. This is a concrete model result, not a theorem with the objects and quantifiers of Problem 6.

Antonio Agresti, Fabian Germ and Mark Veraar, **An optimal local theory for reaction–diffusion equations driven by non-trace-class noise**, arXiv:2606.07417v2 (2026), was screened by the successful initial arXiv abstract response. It establishes reaction–diffusion-specific critical local theory and instantaneous regularization across noise regimes. The abstract does not state the abstract Hilbert endpoint result of Problem 6; it is a lead, not certified as a resolution.

The source-citation metadata also identified **Existence, Uniqueness, and Pathwise Regularity for Multidimensional Semilinear SPDEs with Locally Lipschitz Coefficients and Rough Initial Data**, arXiv:2607.13341 (2026). Its Python PDF request failed with TLS EOF and the native-curl retry timed out. It remains an uninspected lead; the title is not evidence of a solution.

Esmée Theewis and Mark Veraar, **Maximal regularity for evolution equations with critical singular perturbations**, arXiv:2602.00895v3, 2 September 2026, was successfully downloaded by native curl (HTTP 200, 494,585 bytes). PDF p.1 expressly says the paper focuses exclusively on deterministic evolution equations. Theorem 1.2 (PDF p.2) and the main Theorem 4.3 (PDF pp.27–28) treat deterministic maximal regularity and skeleton equations with singular time-dependent perturbations. These are related perturbation results, not the nonlinear Brownian time-regularization question of Problem 6.

The source-citation metadata additionally identified **Necessary conditions for deterministic and stochastic maximal regularity**, arXiv:2608.20266 (2026), and **The stochastic Landau–Lifshitz–Baryakhtar equation in critical spaces**, arXiv:2609.24789 (2026). Their IDs were included in the attempted arXiv abstract batch. The former concerns linear maximal-regularity criteria; the latter's initial-feed abstract concerns one concrete PDE. Neither was certified as this endpoint theorem.

## Exact machine-recorded request ledger

Each entry below was run on 2026-10-12. Raw responses remain in the folder.

- arxiv: `https://export.arxiv.org/api/query?search_query=all:%22Agresti%22+AND+all:%22regularity%22&max_results=30&sortBy=submittedDate&sortOrder=descending`; outcome: 200; bytes: 52848.
- openalex: `https://api.openalex.org/works?search=Nonlinear%20SPDEs%20and%20maximal%20regularity&per-page=15`; outcome: failed; bytes: unknown. Error: HTTPSConnectionPool(host='api.openalex.org', port=443): Max retries exceeded with url: /works?search=Nonlinear%20SPDEs%20and%20maximal%20regularity&per-page=15 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)')))
- crossref: `https://api.crossref.org/works?query.bibliographic=Agresti%20Veraar%20Nonlinear%20SPDEs%20maximal%20regularity&rows=15`; outcome: 200; bytes: 375021.
- semantic: `https://api.semanticscholar.org/graph/v1/paper/search?query=Agresti%20Veraar%20regularity&limit=30&fields=title,authors,year,url,externalIds`; outcome: 429; bytes: 174.
- github: `https://api.github.com/search/repositories?q=Agresti+Veraar+regularity`; outcome: failed; bytes: unknown. Error: HTTPSConnectionPool(host='api.github.com', port=443): Max retries exceeded with url: /search/repositories?q=Agresti+Veraar+regularity (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)')))
- arxiv_source: `https://arxiv.org/pdf/2501.18561`; outcome: 200; bytes: 1591670.
- arxiv_lead: `https://arxiv.org/pdf/2509.07803`; outcome: 200; bytes: 398777.
- openalex_doi: `https://api.openalex.org/works/https://doi.org/10.1007/s00030-025-01090-2`; outcome: failed; bytes: unknown. Error: HTTPSConnectionPool(host='api.openalex.org', port=443): Max retries exceeded with url: /works/https://doi.org/10.1007/s00030-025-01090-2 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)')))
- openalex_retry: `https://api.openalex.org/works?search=critical%20time%20regularization%20Hilbert&per-page=20`; outcome: failed; bytes: unknown. Error: HTTPSConnectionPool(host='api.openalex.org', port=443): Max retries exceeded with url: /works?search=critical%20time%20regularization%20Hilbert&per-page=20 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)')))
- github_retry: `https://api.github.com/search/repositories?q=%22stochastic+maximal+regularity%22`; outcome: failed; bytes: unknown. Error: HTTPSConnectionPool(host='api.github.com', port=443): Max retries exceeded with url: /search/repositories?q=%22stochastic+maximal+regularity%22 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)')))
- semantic_doi: `https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/s00030-025-01090-2?fields=title,year,citations.title,citations.year,citations.externalIds`; outcome: 200; bytes: 9963.
- arxiv_endpoint: `http://export.arxiv.org/api/query?search_query=all:%22time+regularization%22+AND+all:%22stochastic%22&max_results=30`; outcome: failed; bytes: unknown. Error: HTTPSConnectionPool(host='export.arxiv.org', port=443): Read timed out. (read timeout=35)
- crossref_endpoint: `https://api.crossref.org/works?query=critical%20Hilbert%20time%20regularization%20stochastic&filter=from-pub-date:2025-01-01&rows=20`; outcome: 200; bytes: 171794.
- arxiv: `https://export.arxiv.org/api/query?id_list=2607.13341,2602.00895,2608.20266,2608.21014,2606.07417,2609.24789`; outcome: failed; bytes: unknown. Error: HTTPSConnectionPool(host='export.arxiv.org', port=443): Max retries exceeded with url: /api/query?id_list=2607.13341,2602.00895,2608.20266,2608.21014,2606.07417,2609.24789 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)')))
- arxiv: `https://arxiv.org/pdf/2607.13341`; outcome: failed; bytes: unknown. Error: HTTPSConnectionPool(host='arxiv.org', port=443): Max retries exceeded with url: /pdf/2607.13341 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)')))
- arxiv: `https://arxiv.org/pdf/2602.00895`; outcome: failed; bytes: unknown. Error: HTTPSConnectionPool(host='arxiv.org', port=443): Max retries exceeded with url: /pdf/2602.00895 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)')))
- arxiv: `https://arxiv.org/pdf/2608.21014`; outcome: 200; bytes: 672955.
- openalex_curl: `https://api.openalex.org/works/https://doi.org/10.1007/s00030-025-01090-2`; outcome: 0; bytes: 610.
- github_curl: `https://api.github.com/search/repositories?q=Agresti+Veraar+regularity`; outcome: 0; bytes: 73.
- rough_data_curl: `https://arxiv.org/pdf/2607.13341`; outcome: failed; bytes: unknown. Error: Command '['curl.exe', '-L', '--max-time', '35', '-sS', '-w', '\nHTTP_STATUS:%{http_code}', 'https://arxiv.org/pdf/2607.13341']' timed out after 45 seconds
- critical_perturbations_curl: `https://arxiv.org/pdf/2602.00895`; outcome: 200; bytes: 494585.
- openalex_citing_doi: `https://api.openalex.org/works?filter=cites:https%3A%2F%2Fdoi.org%2F10.1007%2Fs00030-025-01090-2&per-page=100`; outcome: 429; bytes: 610.
