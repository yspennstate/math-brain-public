# Literature record — G0006

Search date: 2026-10-11. All web requests used Python urllib, not built-in web search.

## Verified source

John Fernley and Emmanuel Jacob, *Percolation of the contact process on the regular tree*, arXiv:2609.09972v1, posted 9 September 2026; PDF dated 10 September 2026, 19 pages. https://arxiv.org/abs/2609.09972

Definition on PDF pp. 1–2: nearest-neighbor graph Z^d, recovery rate 1, rate lambda along each infected–healthy edge. nu_lambda is the upper invariant law. lambda_1 is the survival critical value; lambda_p is the supremum of rates having zero probability of an infinite nearest-neighbor infected component. The relevant open-question paragraph is actually PDF p. 3, not pp. 1–2 in the intake locator.

Exact question paragraph on PDF p. 3 (typographical ligatures normalized):

> The same paper also raises the natural question whether we have λ₁ < λₚ on Zᵈ when d ≥ 2, which remains a difficult open problem. To the best of our knowledge, such a result has previously never been proven for any graph with λₚ < +∞.

Theorem 2.1(a), PDF p. 3, says on the d-regular tree T_d with d >= 3, lambda_1 < lambda_p. This is NOT the lattice theorem. Tree degree d must not be confused with lattice dimension d (degree 2d).

Reference [8]: Thomas M. Liggett and Jeffrey E. Steif, *Stochastic domination: the contact process, Ising models and FKG measures*, Ann. Inst. H. Poincare Probab. Statist. 42(2) (2006), 223–243, arXiv:math/0504530. Downloaded original preprint. Theorem 1.1, preprint PDF p. 2, proves domination from BELOW by product measures for sufficiently LARGE rates. This yields percolation, not nonpercolation.

Reference [11]: Balazs Rath and Daniel Valesin, *On the threshold of spread-out contact process percolation*, Ann. Inst. Henri Poincare Probab. Stat. 58(3) (2022), 1808–1848, DOI 10.1214/21-AIHP1214, arXiv:1912.09825. Different infection graph; must not count as solving nearest-neighbor model.

## Requests and outcomes

- source_pdf: `https://arxiv.org/pdf/2609.09972` — HTTP 200, 241284 bytes.
- source_abs: `https://arxiv.org/abs/2609.09972` — HTTP 200, 40272 bytes.
- arxiv: `https://export.arxiv.org/api/query?search_query=all:contact%20AND%20all:percolation&sortBy=submittedDate&sortOrder=descending&max_results=40` — HTTP 200, 86452 bytes.
- openalex: `https://api.openalex.org/works?search=Percolation%20of%20the%20contact%20process%20on%20the%20regular%20tree&per-page=20` — HTTP Error 429: Too Many Requests.
- crossref: `https://api.crossref.org/works?query=contact%20process%20upper%20invariant%20measure%20percolation&rows=20` — HTTP 200, 158823 bytes.
- semantic: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:2609.09972?fields=title,authors,year,abstract,citations.title,citations.year,citations.externalIds` — HTTP Error 429: .
- github: `https://api.github.com/search/repositories?q=contact+process+percolation` — HTTP 200, 6684 bytes.
- arxiv_exact: `https://export.arxiv.org/api/query?search_query=all:%22contact%20process%22%20AND%20(all:%22percolation%22%20OR%20all:%22invariant%22)&sortBy=submittedDate&sortOrder=descending&max_results=100` — HTTP 200, 190256 bytes.
- arxiv_since: `http://export.arxiv.org/api/query?search_query=all:%22contact%20process%22%20AND%20submittedDate:[20260909%20TO%20261012]&max_results=100` — HTTP 200, 19495 bytes.
- openalex_retry: `https://api.openalex.org/works?search=contact%20process%20percolation&per_page=25` — HTTP Error 429: Too Many Requests.
- openalex_source: `https://api.openalex.org/works/https://arxiv.org/abs/2609.09972` — HTTP Error 429: Too Many Requests.
- semantic_search: `https://api.semanticscholar.org/graph/v1/paper/search?query=contact%20process%20percolation&limit=20&fields=title,year,externalIds` — HTTP Error 429: .
- liggett_pdf: `https://arxiv.org/pdf/math/0504530` — HTTP 200, 288995 bytes.
- rath_search: `https://export.arxiv.org/api/query?search_query=ti:%22threshold%20of%20spread-out%20contact%20process%22&max_results=5` — HTTP 200, 2605 bytes.
- openalex_citing: `https://api.openalex.org/works?filter=cites:arxiv:2609.09972&per-page=25` — HTTP Error 429: Too Many Requests.
- crossref_since: `https://api.crossref.org/works?query.bibliographic=contact%20process%20percolation&filter=from-pub-date:2026-09-09&rows=30` — HTTP 200, 284515 bytes.
- arxiv_sharpness: `https://export.arxiv.org/api/query?search_query=ti:%22Sharpness%20of%20the%20percolation%20transition%22&max_results=10` — HTTP 200, 7844 bytes.
- sharpness_all: `https://arxiv.org/pdf/1807.05591` — HTTP Error 404: Not Found.
- spreadout: `https://arxiv.org/pdf/1912.09825` — HTTP 200, 1034417 bytes.
- sharpness_2_search: `https://export.arxiv.org/api/query?search_query=ti:%22Sharpness%20of%20the%20percolation%20transition%20in%20the%20two-dimensional%20contact%20process%22&max_results=5` — HTTP 200, 3389 bytes.

OpenAlex source lookup and both searches were rate limited. Its citing-works query could not be completed because no OpenAlex source work ID could be resolved; the provisional arXiv-valued `cites` request is not a valid completed citation search. Semantic Scholar source citation request and title search both returned 429. These are coverage gaps, not evidence of no citations.

## Initial search findings

arXiv post-source date search returned the tree source, generalized deterministic-cure processes, social clusters/asymptomatic models, machine-learning of the contact process, comparison of infection rules, k-creation processes, and quenched-disorder bootstrap work. None of the inspected abstracts states the requested nearest-neighbor upper-invariant strict inequality. GitHub returned one simulation repository, lorenzomancini1/SIS_and_SIR_model_percolation; not a proof.

Crossref broad search identified sharpness papers and spread-out work; these are leads requiring hypothesis inspection. No SOLVED_IN_LITERATURE verdict is warranted.

## Read-only brain and earlier attempts

Ran math_recall.py with "contact process percolation Liggett Steif"; results were mostly off topic. Ran brain.py recall separately on "contact process upper invariant measure percolation mistakes" and "contact process upper invariant measure spatial percolation"; no trustworthy directly relevant proof surfaced.

Read G0006-A001 from probability_1000_intake_G_20260910/attempts.jsonl. It reverses a stochastic-domination direction and misdescribes the tree proof. Neither lower product domination below p_c nor failure to dominate a product law above p_c implies nonpercolation. Only an UPPER subcritical product comparison would do so. Source itself warns that arbitrarily low density alone is insufficient.

Searched codex_pool_2026_10_10 and origin/master tree paths for G0006/contact_process/contact.process; no matching paths. No repositories or brain data modified.


## Completed lead inspection

J. van den Berg, *Sharpness of the percolation transition in the two-dimensional contact process*, Annals of Applied Probability 21(1) (2011), 374–395, DOI 10.1214/10-AAP702, arXiv:0907.2843v2. Downloaded full PDF. Theorem 1.1 (PDF p. 4) assumes a parameter lambda at which there is already no percolation and gives exponential decay at every smaller parameter. To deduce the desired gap one would first need a nonpercolating parameter strictly above lambda_c; the theorem does not provide one. Thus it cannot prove the gap by itself.

Thomas Beekenkamp, *Sharpness of the Percolation Phase Transition for the Contact Process on Z^d*, arXiv:1807.05591v3 (metadata updated 4 August 2020). The arXiv API summary discusses sharpness, not separation of survival and percolation thresholds. Both unversioned and v3 PDF URLs returned 404. The metadata comment reads "Problem in third displayed equation of page 9". Accordingly this is an unverified lead and no theorem from it is used.

Rath--Valesin, arXiv:1912.09825v3 (29 July 2021), PDF p. 6 Question 1.1 explicitly repeats the nearest-neighbor lattice question. Theorem 1.2 and Corollary 1.3 on PDF p. 7 concern the limit of large spread-out range R, and imply strict inequality only for sufficiently large R. Their nearest-neighbor convention uses total rate lambda, with lambda/(2d) per edge (PDF p. 3). The infection graph of their spread-out theorem includes all l-infinity neighbors, so even R=1 is not the nearest-neighbor graph. On PDF p. 8 they leave the proposed small-parameter upper product comparison open.

Fernley--Jacob source Section 3, PDF pp. 6–7, describes its strict-gap argument via an exponential bound on occupation of a whole tree segment, using hitting probabilities near weak survival; it explicitly says this is obtained WITHOUT upper product domination. Proposition 5.3 on PDF p. 9 gives the stationary conditional degree identity for the tree. ATTEMPT.md proves the corresponding lattice identity directly, then explains why it is insufficient.

The post-source Crossref search returned mostly unrelated engineering/medical papers and no theorem answering the question. This is a noisy metadata search, not proof of absence.

- 2026-10-11 sharpness_all: `https://arxiv.org/pdf/1807.05591` — HTTP Error 404: Not Found.
- 2026-10-11 spreadout: `https://arxiv.org/pdf/1912.09825` — HTTP 200, 1034417 bytes.
- 2026-10-11 sharpness_2_search: `https://export.arxiv.org/api/query?search_query=ti:%22Sharpness%20of%20the%20percolation%20transition%20in%20the%20two-dimensional%20contact%20process%22&max_results=5` — HTTP 200, 3389 bytes.
- 2026-10-11 sharpness_2: `https://arxiv.org/pdf/0907.2843` — HTTP 200, 276338 bytes.
- 2026-10-11 sharpness_all_v3: `https://arxiv.org/pdf/1807.05591v3` — HTTP Error 404: Not Found.

Conclusion: no paper stating and proving this exact question was found. The rate-limited citation searches and unavailable Beekenkamp PDF prevent claiming comprehensive coverage. No SOLVED_IN_LITERATURE verdict.

Original Liggett--Steif preprint, Section 8, Question 2, PDF p. 25, states verbatim (subscripts normalized):

> For d ≥ 2, does there exist λ > λc such that νλ does not percolate? (In words, is the critical value for percolation different than the usual critical value?)

This is the original form of the same question. Final-paper section numbering differs from this preprint.


## Second attempt, 2026-10-11: gap-focused brain requests and verified inputs

Ran the read-only math store with the gap's key words and authors:

- `contact process near critical spatial connectivity decoupling Bezuidenhout Grimmett`
- `Liggett Schonmann Stacey domination finite dependent percolation contact process sharpness van den Berg`
- `Liggett Schonmann Stacey` (full output saved in brain_lss.txt)

Also invoked the read-only memory recall query `contact process near critical spatial mixing density correlation length mistakes`. No recalled result was accepted as a theorem proving the missing connectivity bound. The math-store outputs were mostly off topic; the BK/disjoint-occurrence hints cannot be applied to ordinary simultaneous occupation events. No LSS theorem was used or quoted: the block criterion was proved directly.

Re-examined the already downloaded van den Berg paper, arXiv:0907.2843v2, rather than running a new status search. Exact inputs (subscripts and ligatures normalized):

Theorem 1.1, PDF p. 4:

> Let λ be such that ν̄λ(|C| = ∞) = 0. Then, for every λ′ < λ there exist C1,C2 > 0 such that for all n ≥ 1, ν̄λ′(|C| ≥ n) ≤ C1 exp(−C2 n).

Theorem 2.1, PDF p. 5:

> For all λ > λc there exist C3,C4 > 0 such that for all t > 0 and all Λ finite in Z², dTV(μt;Λ, ν̄λ;Λ) ≤ |Λ| C3 exp(−C4 t).

The second quotation renders the PDF's finite-set symbol as words. These statements are used only to prove necessity of a finite certificate UNDER AN ASSUMED STRICT GAP. They are not a literature solution of the gap. Full reference: J. van den Berg, Annals of Applied Probability 21(1) (2011), 374–395, DOI 10.1214/10-AAP702.
