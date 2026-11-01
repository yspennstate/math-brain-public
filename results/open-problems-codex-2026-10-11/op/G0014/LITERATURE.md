# Literature and source audit

Date of all searches: 2026-10-11. Direct Python urllib requests; no built-in web search.

## Search log

- source_pdf: `https://arxiv.org/pdf/2608.21125` — HTTP 200, saved source_pdf.pdf

- source_html: `https://arxiv.org/html/2608.21125` — HTTP 200, saved source_html.txt

- arxiv_id: `https://export.arxiv.org/api/query?id_list=2608.21125` — HTTP 200, saved arxiv_id.txt

- arxiv_search: `https://export.arxiv.org/api/query?search_query=all%3A%22threshold%20cascades%22%20AND%20all%3A%22Bramson%22&max_results=20` — HTTP 200, saved arxiv_search.txt

- openalex_source: `https://api.openalex.org/works?search=Two%20problems%20for%20threshold%20cascades%20of%20interacting%20diffusions%20on%20unimodular%20random%20trees&per-page=5` — HTTP Error 429: Too Many Requests

- openalex_recent: `https://api.openalex.org/works?search=threshold%20cascades%20Bramson&filter=from_publication_date:2026-08-01&per-page=20` — HTTP Error 429: Too Many Requests

- crossref: `https://api.crossref.org/works?query=threshold%20cascades%20unimodular%20Bramson&rows=10` — HTTP 200, saved crossref.txt

- semantic: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:2608.21125?fields=title,authors,year,citations.title,citations.year,citations.externalIds` — HTTP Error 429: 

- github: `https://api.github.com/search/repositories?q=%22threshold%20cascades%22` — HTTP 200, saved github.txt

- openalex_retry: `https://api.openalex.org/works?search=2608.21125&per_page=5` — HTTP Error 429: Too Many Requests

- openalex_citing_identifier: `https://api.openalex.org/works?filter=cites:https%3A%2F%2Farxiv.org%2Fabs%2F2608.21125&per_page=20` — HTTP Error 429: Too Many Requests

- semantic_retry: `https://api.semanticscholar.org/graph/v1/paper/search?query=threshold%20cascades%20unimodular&limit=10&fields=title,year,externalIds` — HTTP Error 429: 

- arxiv_recent: `https://export.arxiv.org/api/query?search_query=all%3A%22threshold%20cascades%22%20AND%20submittedDate%3A%5B20260821%20TO%2020261011%5D&max_results=50` — HTTP 200, saved arxiv_recent.txt

- arxiv_chen: `https://export.arxiv.org/api/query?search_query=ti%3A%22necessary%20and%20sufficient%20condition%22%20AND%20au%3AChen%20AND%20all%3A%22derivative%20martingale%22&max_results=5` — HTTP 200, saved arxiv_chen.txt

- aidekon_pdf: `https://arxiv.org/pdf/1101.1810` — HTTP 200, saved aidekon_pdf.pdf

- companion_pdf: `https://arxiv.org/pdf/2608.15987` — HTTP 200, saved companion_pdf.pdf

- arxiv_pdf: `https://arxiv.org/pdf/2609.27972` — HTTP 200, saved PDF/extraction

- arxiv_pdf: `https://arxiv.org/pdf/1402.5864` — HTTP 200, saved PDF/extraction



## Exact source

Kumar, Achyut; Duddala, Abhinav. *Two problems for threshold cascades of interacting diffusions on unimodular random trees: front propagation with a Bramson correction, and the continuous-type limit theory*. arXiv:2608.21125v1 (21 August 2026). Fetched PDF, 9 pages; SHA256 64484fb650e510843769fb34ef14d51c0ec0b694a753880be8a4f2bd70ce3b47. Authors differ from the intake spelling Dudeja. The API returned v1, with no later revision shown.

The exact source extraction is source_extracted.txt; page markers preserve locators. Conjecture 3.2 and Proposition 3.1 are on PDF p.4. Its relevant verbal clause reads: "the derivative martingale ∂W_n is uniformly integrable (equivalently, ∂W_∞ > 0 a.s. on survival)". Its displayed front formula is F(t)=c_*t−[3/(2θ_*c_*)]log t+O_P(1). This is a mathematical transcription of the PDF, not a purported solved theorem.

Theorem 2.1 (p.3) assumes R1, kappa<1, rho(M)>1, irreducibility, and a common finite positive exponential-moment parameter for all activation type pairs. Definition 1.2 on p.3 uses the reciprocal of inf log rho(B(theta))/theta with no minus sign.



## Relevant leads and why none solves this exact statement

Xinxin Chen. *A necessary and sufficient condition for the nontrivial limit of the derivative martingale in a branching random walk*. Advances in Applied Probability 47 (2015), 741–760; arXiv:1402.5864. Fetched v1, 24 pages. Theorem 1.1, PDF p.3, concerns NONTRIVIALITY, not UI: the condition is E[Z log_+ Z + Y(log_+Y)^2]<infinity. PDF p.2 explicitly calls D_n a signed martingale of mean zero. Single-type boundary BRW, not the original multitype cascade.

Elie Aidekon. *Convergence in law of the minimum of a branching random walk*. Annals of Probability 41 (2013), 1362–1426; arXiv:1101.1810v6. Theorem 1.1, PDF p.3: P(M_n >= (3/2)ln n+x) -> E[exp(-C_*exp(x)D_infinity)]. Boundary normalization p.1; nonlattice, variance, and moments p.2. Used only for the explicitly checked conditional single-type special case in ATTEMPT.md. It is not a theorem about UI or the time-depth cascade.

Achyut Kumar and Abhinav Duddala. *A multiscale front-decoupling criterion for threshold cascades on unimodular random trees*. arXiv:2609.27972v1. Found by the recent arXiv threshold-cascades search; fetched all 13 pages. PDF imprint says 24 August 2026 despite the identifier month; do not infer chronology from that discrepancy. Theorem 3.1 (PDF p.7) concerns finite-scale contraction/front decoupling; Theorem 4.6 (p.10) gives an initial-scale estimate. Searching the full text for Bramson/derivative found no derivative-martingale/front-log-correction theorem. Bramson appears in the reference title of the source. Relevant lead, not a solution.

Achyut Kumar. *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*. Companion identified in intake as arXiv:2608.15987; downloaded as companion_pdf.pdf. The source itself gives a placeholder identifier in reference [1], so its R1 remains an assumption for this report.



## Search conclusions and limits

The arXiv combined Bramson/threshold-cascades query returned only the source. The recent threshold-cascades query returned the source and the multiscale decoupling lead, which was inspected. Crossref returned mostly unrelated information/social cascade works, plus a neurodegeneration threshold-diffusions title; none supplied this exact theorem. GitHub returned six unrelated threshold-cascade repositories; their descriptions are in github.txt.

OpenAlex title lookup and recent-work search, followed by identifier lookup and a citing-work-filter request, all returned HTTP 429. The citing filter used the arXiv URL because no OpenAlex work ID could be resolved; its semantics and results could not be validated. No successful OpenAlex citation traversal is claimed. Semantic Scholar direct source-and-citations request and title-search retry also returned HTTP 429. This is incomplete coverage, not evidence of absence.

No paper was identified that states and proves THIS conjecture with the same hypotheses and quantifiers. SOLVED_IN_LITERATURE is not used.



## Read-only research-brain and prior-answer checks

Before the attempt, brain.py recall "Bramson derivative martingale mistakes" and math_recall.py --id claim_9c5afaffebd04477bb4ce6220cbb08aa flagged the UI inversion. brain.py node derivative_martingale_ui_clause_is_inverted_2026_09_14 was read in full. The broad recall contains the problem topic and its mistakes as requested.

rg searched the probability intake ledgers for G0014 and 2608.21125. Intake G attempt G0014-A001 incorrectly called the nontrivial-limit moment criterion a UI criterion; intake H/H0010 records a correction.

Read git origin/master:probability_1000_attempts_I_20260914/Probability_H0010_derivative_martingale_conjecture_is_inverted_2026-09-14.md without changing the checkout. Its UI obstruction was independently proved here; its automatic multitype-resolution claim was not adopted.
