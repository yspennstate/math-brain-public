# D0027 literature/status check ? 2026-10-11

## Verified source

Fabio Martinelli, Assaf Shapira and Cristina Toninelli, *Long time behaviour of one facilitated kinetically constrained models: results and open problems*, arXiv:2510.20461v1, submitted 23 October 2025. https://arxiv.org/pdf/2510.20461. PDF p. 2, Section 1.1:

> Conjecture 2. If there exists ? > 0 such that ?(no infected vertices in [??, ?]) = O(e^{???}) for all ? > 0 large enough then for all q > 0 the convergence in (1.1) is exponentially fast.

Equation (1.1) refers to every function depending on finitely many vertices. Section 1.1 defines q in (0,1). Neither translation invariance nor product structure of ? is assumed. The source is saved as source.pdf; extracted text is source.txt; the HTML version is arxiv_html.response.

The source says robust tools for Conjectures 1 and 2 are unavailable and existing results are restricted to q above a threshold. This is source-era evidence, not proof that no later resolution exists.

## Search log

All requests below were made from Python urllib, without built-in web search. Search terms are encoded in the exact request URL. Raw successful responses are retained in corresponding .response files. Failures are included explicitly. No inference of absence is made from HTTP errors.

- 2026-10-11 ? `arxiv_http`: http://export.arxiv.org/api/query?search_query=all%3A%22FA-1f%22&max_results=30&sortBy=submittedDate&sortOrder=descending
  Result: OK; 4224.
- 2026-10-11 ? `arxiv_https`: https://export.arxiv.org/api/query?search_query=all%3A%22facilitated%22%20AND%20all%3A%22relaxation%22&max_results=30&sortBy=submittedDate&sortOrder=descending
  Result: OK; 136937.
- 2026-10-11 ? `openalex`: https://api.openalex.org/works?search=FA-1f%20relaxation&per-page=30
  Result: ERROR; HTTP Error 429: Too Many Requests.
- 2026-10-11 ? `openalex_source`: https://api.openalex.org/works?search=Long%20time%20behaviour%20of%20one%20facilitated%20kinetically%20constrained%20models&per-page=5
  Result: ERROR; HTTP Error 429: Too Many Requests.
- 2026-10-11 ? `crossref`: https://api.crossref.org/works?query=FA-1f%20relaxation&rows=30
  Result: OK; 127881.
- 2026-10-11 ? `semanticscholar`: https://api.semanticscholar.org/graph/v1/paper/search?query=FA-1f&limit=30&fields=title,authors,year,externalIds,url,abstract
  Result: ERROR; HTTP Error 429: .
- 2026-10-11 ? `semanticscholar_citations`: https://api.semanticscholar.org/graph/v1/paper/ARXIV:2510.20461/citations?fields=title,authors,year,externalIds&limit=100
  Result: OK; 26.
- 2026-10-11 ? `github`: https://api.github.com/search/repositories?q=%22FA-1f%22
  Result: OK; 108329.
- 2026-10-11 ? `arxiv_html`: https://arxiv.org/html/2510.20461v1
  Result: OK; 804067.
- 2026-10-11 ? `arxiv_fredrickson`: https://export.arxiv.org/api/query?search_query=all%3AFredrickson&max_results=70&sortBy=submittedDate&sortOrder=descending
  Result: OK; 141195.
- 2026-10-11 ? `arxiv_kcm`: https://export.arxiv.org/api/query?search_query=ti%3A%22kinetically%20constrained%22&max_results=40&sortBy=submittedDate&sortOrder=descending
  Result: OK; 84458.
- 2026-10-11 ? `crossref_precise`: https://api.crossref.org/works?query.title=Fredrickson%20Andersen%20one%20spin%20facilitated%20relaxation&rows=20
  Result: OK; 155252.
- 2026-10-11 ? `openalex_retry`: https://api.openalex.org/works?search=Long%20time%20behaviour%20of%20one%20facilitated&per_page=5
  Result: ERROR; <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)>.
- 2026-10-11 ? `ss_source`: https://api.semanticscholar.org/graph/v1/paper/ARXIV:2510.20461?fields=title,year,externalIds,citationCount
  Result: ERROR; HTTP Error 429: .
- 2026-10-11 ? `github_precise`: https://api.github.com/search/repositories?q=%22Fredrickson%22%20%22Andersen%22
  Result: OK; 10988.
- 2026-10-11 ? `spectral_pdf`: https://arxiv.org/pdf/math/0610109
  Result: OK; 185462.
- 2026-10-11 ? `fa_2013_pdf`: https://arxiv.org/pdf/1205.4582
  Result: OK; 2104916.

## Relevant prior literature and source-side leads

- O. Blondel, N. Cancrini, F. Martinelli, C. Roberto and C. Toninelli, *Fredrickson-Andersen one spin facilitated model out of equilibrium*, Markov Processes and Related Fields 19(3), 383?406 (2013). Source reference [3]. Stronger initial-law/high-q results do not settle the full initial-law and all-q statement.
- A. Ertul, *Cutoff for the Fredrickson-Andersen one spin facilitated model*, ALEA 19(1), 511?536 (2022). Source reference [8]. A cutoff result in its stated parameter regime does not establish Conjecture 2.
- L. Mar?ch?, *Exponential convergence to equilibrium in supercritical kinetically constrained models at high temperature*, Markov Processes and Related Fields 26(5), 861?884 (2020). Source reference [17]. The high-temperature restriction differs from the all-q question.
- I. Hartarsky and F. L. Toninelli, *Kinetically constrained models out of equilibrium*, Probability and Mathematical Physics 5(2), 461?489 (2024). Source reference [10]. General high-q tools; not the requested theorem.
- I. Hartarsky and C. Toninelli, *Kinetically Constrained Models*, SpringerBriefs in Mathematical Physics 53, Springer (2025). Source reference [9]. Equilibrium spectral-gap and non-equilibrium background.
- O. Blondel, A. Deshayes and C. Toninelli, *Front evolution of the Fredrickson-Andersen one spin facilitated model*, arXiv:1803.08761 (2018), retrieved arXiv version v2. The abstract explicitly assumes q above a threshold. Relevant to front control, not the full conjecture.

In the original source, Theorem 5.2, PDF p. 20, proves uniform local exponential ergodicity for the double-flip process. It is a different process. Section 5 derives BABP product-law results using its dualities; BABP differs from FA-1f when both neighbors are infected. Section 6, Theorem 6.2, PDF p. 25, proves linear growth of span/radius from finitely many infections. It gives no local-forgetting conclusion.

## Read-only prior work

Read the D0027-A001 attempt and problem entry in probability_1000_intake_D_20260908. Saved relevant rows as prior_attempts.json. Read origin/master:operations/claims/D0027.md and the two September 17 R7-04 admission/handoff files, saved as prior_repo_0.md to prior_repo_2.md. Their closure was PARTIAL, and the six-run handoff still lacks singleton-dual local exponential relaxation and arbitrary-law integration. These are research hints, not theorems accepted without checking.

Brain math recall queries: 'FA-1f relaxation infection gaps'; memory recalls: 'FA-1f mistakes' and 'Fredrickson Andersen kinetically constrained relaxation'. No on-target theorem was returned. The memory recall utility reported that it internally refreshed its index; no brain/store write command was issued by this worker, and it was not called again.

## Status adjudication

No retrieved paper has yet been found stating and proving the exact all-q, arbitrary-initial-law Conjecture 2. Semantic Scholar's citations endpoint returned an empty data list; this is only bounded negative evidence. OpenAlex requests were throttled/failed, so coverage there is incomplete. SOLVED_IN_LITERATURE is not justified. The mathematical attempt continues separately in ATTEMPT.md.

## Further focused retrievals

Two guessed identifiers (math/0610109 and 1205.4582) proved unrelated on opening their PDFs: Jacobi polynomials and literary-network analysis, respectively. They are excluded from mathematical evidence. Replaced the guesses with exact-title arXiv queries.

- 2026-10-11 — arxiv_gap_title: https://export.arxiv.org/api/query?search_query=ti%3A%22Kinetically%20constrained%20spin%20models%22&max_results=20; OK: 19639.
- 2026-10-11 — arxiv_fa_title: https://export.arxiv.org/api/query?search_query=ti%3A%22Fredrickson%20Andersen%20one%20spin%20facilitated%20model%20out%20of%20equilibrium%22&max_results=10; OK: 2735.
- 2026-10-11 — arxiv_exp_title: https://export.arxiv.org/api/query?search_query=all%3AFredrickson%20AND%20ti%3A%22Exponential%20Convergence%22&max_results=10; OK: 774.
- 2026-10-11 — crossref_source_title: https://api.crossref.org/works?query.title=Long%20time%20behaviour%20of%20one%20facilitated%20kinetically%20constrained%20models%20results%20and%20open%20problems&rows=5; OK: 52988.
- 2026-10-11 — openalex_source_lookup: https://api.openalex.org/works/https://arxiv.org/abs/2510.20461; ERROR: HTTP Error 429: Too Many Requests.
- 2026-10-11 — openalex_citing_source_attempt: https://api.openalex.org/works?filter=cites:https%3A%2F%2Farxiv.org%2Fabs%2F2510.20461&per-page=100; ERROR: HTTP Error 429: Too Many Requests.

## Verified identifiers and date-filtered search

- 2026-10-11 — cmrt_correct: https://arxiv.org/pdf/math/0610106; OK: 493960.
- 2026-10-11 — fa2013_correct: https://arxiv.org/pdf/1205.4584; OK: 264820.
- 2026-10-11 — arxiv_since_source: https://export.arxiv.org/api/query?search_query=cat%3Amath.PR%20AND%20%28all%3A%22facilitated%22%20OR%20all%3A%22kinetically%20constrained%22%29%20AND%20submittedDate%3A%5B202510230000%20TO%20202610112359%5D&max_results=100&sortBy=submittedDate&sortOrder=descending; OK: 66990.
- 2026-10-11 — crossref_exp: https://api.crossref.org/works/10.1007/s10959-018-0812-6; OK: 7400.

## Verified equilibrium input (not a solution of D0027)

N. Cancrini, F. Martinelli, C. Roberto and C. Toninelli, *Kinetically constrained spin models*, arXiv:math/0610106v1 (3 October 2006), https://arxiv.org/pdf/math/0610106. Correct downloaded file: cmrt_correct.pdf; extracted text: cmrt_correct.txt.

Theorem 6.3, PDF p. 20, verbatim:

> Theorem 6.3. For any q ? (0, 1) the spectral gap of the FA-1f model is positive.

Theorem 6.1, PDF p. 18, begins verbatim:

> Theorem 6.1. For any q ? (0, 1) the spectral gap of the East model is positive.

Theorem 6.4, PDF p. 20, gives in dimension one C^{-1}q^3 <= gap(L) <= Cq^3. These are equilibrium L2 assertions. ATTEMPT.md uses the positive gap for absolutely continuous finite-window replacements; the replacement density cost prevents application to arbitrary singular initial laws. Thus none of these theorems is classified as SOLVED_IN_LITERATURE for the present question.

The exact-title search verified that the 2013 out-of-equilibrium paper's arXiv identifier is 1205.4584 (not the discarded 1205.4582 guess). Its abstract assumes a uniform mean-distance condition on initial vacancies and q above a threshold, confirming it is a lead rather than the all-q result.

OpenAlex citation-search limitations: an arXiv URL is not a verified OpenAlex work ID. The URL-based citation-filter request was throttled before its validity could be assessed. No successful OpenAlex citing-works traversal was obtained. This limitation is reported rather than presenting an unsupported empty citation list.

## Date-filtered post-source candidates

The math.PR query over 2025-10-23 through 2026-10-11 returned 32 entries. Metadata of all model-relevant hits is in postsource_relevant.json. These include a new oriented-model theorem, which is being checked for scope.

- Paul Chleboun, *Linear time mixing and pre-cutoff for oriented kinetically constrained models*, http://arxiv.org/abs/2609.30585v1; submitted 2026-09-24T21:58:54Z.
- Assaf Shapira, *Universality in dimension 1 of kinetically constrained lattice gases*, http://arxiv.org/abs/2608.13208v1; submitted 2026-08-13T13:11:19Z.
- Balázs Pozsgay, *Anomalous current fluctuations in the stochastic XNOR hopping model*, http://arxiv.org/abs/2608.10536v2; submitted 2026-08-11T06:16:37Z.
- Laurent Bartholdi, Ivailo Hartarsky, Ivan Mitrofanov, *Super-Arrhenius relaxation of the triangular plaquette model in any dimension*, http://arxiv.org/abs/2606.16259v1; submitted 2026-06-15T06:05:58Z.
- Assaf Shapira, *A Thomson-type variational principle for diffusion coefficients*, http://arxiv.org/abs/2606.04636v2; submitted 2026-06-03T09:07:51Z.
- Fabio Martinelli, Assaf Shapira, Cristina Toninelli, *Long time behaviour of one facilitated kinetically constrained models: results and open problems*, http://arxiv.org/abs/2510.20461v1; submitted 2025-10-23T11:53:11Z.
- 2026-10-11 retrieval: https://arxiv.org/pdf/2609.30585; OK: 301380.
- 2026-10-11 retrieval: https://link.springer.com/article/10.1007/s10959-018-0812-6; OK: 3038.

## Scope adjudication of the new 2026 lead

Paul Chleboun, *Linear time mixing and pre-cutoff for oriented kinetically constrained models*, arXiv:2609.30585v1, submitted 24 September 2026. Read the full downloaded PDF oriented_2026.pdf (text: oriented_2026.txt). Theorem 2.4, PDF p. 5, assumes an oriented update family and a uniformly positive finite-volume gap, and concludes linear-time pre-cutoff with facilitating boundary conditions. Definitions in Section 2.1, PDF p. 3, and Definition 3.1, PDF p. 5, require the union of the update sets to lie in a single open half-space.

FA-1f's update family in dimension one is {{-1},{+1}}. No nonzero direction u puts both -1 and +1 in the open half-space {x:x*u<0}: their scalar products are opposite. Thus FA-1f fails the theorem's orientation hypothesis. Also, the conclusion concerns finite-volume pre-cutoff rather than the exact arbitrary-initial-law infinite-volume assertion. This is a genuinely later and relevant method lead, not a printed solution of D0027. The proof relies on a height function decreasing along the witness path; the symmetric FA-1f dependencies do not supply that height.

The other date-filtered candidates concern conservative lattice gases, XNOR hopping, plaquette models, and diffusion coefficients. Their model definitions differ from FA-1f and none of the retrieved abstracts claims the exact conjecture.

Additional exact Crossref reference: Thomas Mountford and Glauco Valle, *Exponential Convergence for the Fredrickson–Andersen One-Spin Facilitated Model*, DOI 10.1007/s10959-018-0812-6; Crossref publication date 2018-02-15. Journal: ['Journal of Theoretical Probability']; volume 32; pages 282-302. This predates the source. The Springer landing response was retrieved but is not usable theorem text; no full-conjecture claim is based on it.

## Final literature verdict

No retrieved theorem states and proves Conjecture 2 with the same model, arbitrary initial law, and all-q quantifiers. Therefore this attempt is NOT SOLVED_IN_LITERATURE. Search coverage is bounded, and OpenAlex throttling prevents a verified citing-works traversal. This report does not assert bibliographic completeness or worldwide openness. Mathematical output: PARTIAL, documented in ATTEMPT.md.

## Additional-attempt brain queries ? 2026-10-11

Read-only math-store questions, one call per question:

- `FA-1f uniform local forgetting single infection spectral gap killed process`: returned exclusion-with-reservoirs and generic spectral-gap cards; no FA-1f local-forgetting theorem.
- `Sudbury Lloyd quasi-duality thinnings double flip process`: returned off-target Trefethen/Bau and generic Boolean/Poisson cards; no usable quasi-duality theorem.

These results were treated as hints and were not used as proof inputs. The neighboring-model motivation comes from the already downloaded source, Section 5. Its exact reference [24] is A. Sudbury and P. Lloyd, *Quantum operators in classical probability theory. IV. Quasi-duality and thinnings of interacting particle systems*, Annals of Probability 25(1), 96?114 (1997). This follow-up independently computes its own BABP positive control rather than relying on an unverified memory card.
