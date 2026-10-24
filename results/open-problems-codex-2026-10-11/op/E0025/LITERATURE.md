# E0025 literature and status search — 12 October 2026

## Source verified
Ze-Chun Hu and Wei Sun, *Hunt’s Hypothesis (H) for Markov Processes: Survey and Beyond*, arXiv:1908.06825v1, 19 August 2019. Source PDF fetched successfully from https://arxiv.org/pdf/1908.06825 and retained as survey.pdf; text retained as survey.txt.

Question 5, PDF p. 25, verbatim (typographic Unicode normalized only):

> Does any pure jump subordinator with infinite Lévy measure satisfy (H)? More generally, does any pure jump n-dimensional Lévy process satisfy (H)? The latter question has been presented in [23].

The source defines pure jump subordinator as d=0 on PDF p. 11. The question concerns zero deterministic drift, not just zero Gaussian coefficient. Hunt’s hypothesis means every semipolar set is polar (PDF pp. 1–2). The type-(α,β) definition is Definition 2.28, PDF p. 11: density ρ with 1/(c x^(1+α)) ≤ ρ(x) ≤ c/x^(1+β) for all x in (0,1], c>1 and 0<α<β<1.

**Correction to an earlier intake characterization:** Theorem 2.29 does not give (H) for an arbitrary type-(α,β) process or just a subclass under an extra condition. Its exact statement, PDF p. 11, is:

> Any pure jump subordinator of type-(α, β) can be decomposed into the summation of two independent pure jump subordinators of type-(α, β) such that both of them satisfy (H).

Applying this to the original process requires the still-open independent-sum closure assertion, Question 7. It is not a solution to Question 5.

## All online searches

Every request used Python requests from the shell. Dates are 2026-10-12 (UTC and local date). Each response was saved, including errors. The following URLs specify the exact queries and filters. A failed shell quoting attempt to execute the first follow-up requests made no HTTP calls; it was replaced by followup.py.

- arxiv_http: `http://export.arxiv.org/api/query?search_query=all:%22Hunt%27s%20hypothesis%22&start=0&max_results=60&sortBy=submittedDate&sortOrder=descending`; HTTP 429; 14 bytes. 
- arxiv_https: `https://export.arxiv.org/api/query?search_query=all:%22Hunt%27s%20hypothesis%22&start=0&max_results=60&sortBy=submittedDate&sortOrder=descending`; HTTP 429; 14 bytes. 
- openalex_search: `https://api.openalex.org/works?search=Hunt%20hypothesis%20subordinators&per-page=100`; HTTP 200; 1889085 bytes. 
- openalex_source: `https://api.openalex.org/works?search=Hunt%27s%20hypothesis%20for%20Markov%20processes%20survey%20and%20beyond&per-page=10`; HTTP 200; 184706 bytes. 
- crossref: `https://api.crossref.org/works?query=Hunt%20hypothesis%20subordinators&rows=60`; HTTP 200; 222601 bytes. 
- semantic: `https://api.semanticscholar.org/graph/v1/paper/search?query=Hunt%20hypothesis%20subordinator&limit=100&fields=title,authors,year,externalIds,url,abstract`; HTTP 429; 174 bytes. 
- semantic_source: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:1908.06825?fields=title,year,citations.title,citations.year,citations.externalIds`; HTTP 429; 174 bytes. 
- github: `https://api.github.com/search/repositories?q=Hunt+hypothesis+subordinator&per_page=100`; HTTP 200; 55 bytes. 
- oa_exact: `https://api.openalex.org/works?search=%22Hunt%27s%20hypothesis%22&per-page=100`; HTTP 200; 1023342 bytes. 
- oa_cites: `https://api.openalex.org/works?filter=cites:W2968964261&per-page=100`; HTTP 200; 384 bytes. 
- cr_exact: `https://api.crossref.org/works?query.title=Hunt%27s%20hypothesis&rows=100`; HTTP 200; 214854 bytes. 
- arxiv_retry: `https://export.arxiv.org/api/query?search_query=all:Hunt%20AND%20all:subordinator&max_results=30`; HTTP 429; 14 bytes. 
- oa_getoor: `https://api.openalex.org/works?search=%22Getoor%22%20%22conjecture%22&per-page=100`; HTTP 200; 1596558 bytes. 
- github_exact: `https://api.github.com/search/repositories?q=%22Hunt%27s+hypothesis%22&per_page=100`; HTTP 200; 55 bytes. 
- diffusions_2021_pdf: `https://arxiv.org/pdf/2107.06163`; HTTP 200; 208620 bytes. 
- concentration_2023_pdf: `https://arxiv.org/pdf/2310.03471`; HTTP 200; 453059 bytes. 
- oa_further: `https://api.openalex.org/works?search=%22Further%20study%20on%20Hunt%22&per-page=20`; HTTP 200; 28967 bytes. 
- oa_newresults: `https://api.openalex.org/works?search=%22New%20results%20on%20Hunt%22&per-page=20`; HTTP 200; 450 bytes. 
- crossref_filtered: `https://api.crossref.org/works?query.bibliographic=Hunt%20hypothesis%20Levy%20Getoor&rows=100`; HTTP 200; 620618 bytes. 
- semantic_retry: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:1908.06825?fields=title,year,citations.title,citations.year,citations.externalIds`; HTTP 429; 174 bytes. 

Search findings and limitations:

- arXiv HTTP, HTTPS, and the narrower retry returned HTTP 429. Direct arXiv PDF downloads succeeded. This is a search-coverage limitation, not evidence that no new paper exists.
- Semantic Scholar search, source citation lookup, and retry all returned HTTP 429. Its citation list could not be checked.
- OpenAlex’s source-title lookup identified W2968964261, DOI 10.48550/arXiv.1908.06825. The works-citing-source query returned zero records. Its index incompleteness means that this is not evidence of zero actual citations.
- OpenAlex exact phrase and Getoor/conjecture searches identified the survey, classical work, the 2021 diffusion paper, and a 2023 paper by Zhang–Hu–Sun that still mentions the broader conjecture as unsolved. The first broad search was noisy and was tightened. Phrase searches for Further study/New results were unhelpful (irrelevant or zero hits); the exact references are verified instead in the source bibliography.
- Crossref’s initial searches were noisy. The bibliographic query Hunt hypothesis Levy Getoor returned Rao’s 1988 paper and no identified later theorem answering the exact question.
- Both GitHub repository searches returned zero repositories.

## Relevant exact references and scope

1. Hu, Z.-C.; Sun, W. *Further study on Hunt’s hypothesis (H) for Lévy processes*. Science China Mathematics **59**, 2205–2226 (2016). Verified in survey reference [21], PDF p. 27. Its Theorem 2.3 is restated as survey Theorem 2.11, PDF p. 7: the finite-energy Clog criterion used in ATTEMPT.md. Its decomposition Theorem 4.2 is restated as survey Theorem 2.29. Neither has the universal quantifier of Question 5.
2. Hu, Z.-C.; Sun, W.; Zhang, J. *New results on Hunt’s hypothesis (H) for Lévy processes*. Potential Analysis **42**, 585–605 (2015). Survey reference [24], p. 27. Extended Kanda–Forst–Rao theorem (survey Theorem 2.8); driftless special subordinators (Theorem 2.25); locally quasi-stable case (Proposition 2.27); a class failing Rao’s condition discussed on p. 11. These are leads and special cases.
3. Hu, Z.-C.; Sun, W.; Wang, L.-F. *Two theorems on Hunt’s hypothesis (H) for Markov processes*. arXiv:1903.00050 (2019), source reference [23]. Changes of measure and subordination, summarized in Theorems 2.30–2.32; not a universal answer.
4. Hu, Z.-C.; Sun, W. *Hunt’s Hypothesis (H) for the sum of two independent Lévy processes*. Communications in Mathematics and Statistics **6**, 227–247 (2018). Survey reference [22]. Independent sums under additional hypotheses; arbitrary sum closure remains Question 7.
5. Rao, M. *Hunt’s hypothesis for Lévy processes*. Proceedings of the American Mathematical Society **104**, 621–624 (1988). DOI 10.1090/S0002-9939-1988-0962838-6; Crossref also returned JSTOR DOI 10.2307/2047022. Survey Theorem 2.3 states the increasing-function bound with divergent ∫dλ/(λ f(λ)). Our example fails this sufficient condition.
6. Hawkes, J. *Potential theory of Lévy processes*. Proceedings of the London Mathematical Society (3), **38**, 335–352 (1979). Survey [19] omits the volume and prints “3”; volume 38 is the conventional reference, not independently fetched here. Its Theorem 2.1 is explicitly invoked in the survey on p. 4 for resolvent densities/lower semicontinuity. This is an external theorem used in our proof.
7. Liping Li. *Hunt’s hypothesis and symmetrization for general 1-dimensional diffusions*. arXiv:2107.06163v2, 23 July 2021. PDF fetched and text inspected. Introduction p. 1 specifies continuous strong Markov processes on R. Its theorems concern diffusions, not the jump subordinators of Question 5. No scope-compatible solution.
8. Jing Zhang, Ze-Chun Hu, Wei Sun. *On the measure concentration of infinitely divisible distributions*. arXiv:2310.03471v2, 17 October 2023. PDF fetched. On p. 2: “Although the study of infinitely divisible distributions has a long history, there are still many important related problems remain unsolved, e.g., Getoor’s conjecture that essentially all Lévy processes satisfy Hunt’s hypothesis (H) (cf. [1, 2]).” This supports an open status in 2023, but is not an exact 2026 status certificate or a theorem answering E0025.

## Read-only brain and prior-work checks

Calls: brain.py recall "Hunt hypothesis subordinators mistakes"; brain.py recall "Hunt hypothesis pure jump subordinators"; brain.py node a_pure_jump_subordinator_can_break_kanda_forst_2026_09_13; math_recall.py --id claim_fc2810725f4f4b23a924b0d3f7cc75c4; math_recall.py "Kanda Forst Rao subordinator Hunt density". Full node was read. Its claim of point polarity is explicitly only a heuristic and is not used. Its statement that all classical sufficient conditions are pointwise controls is too broad, since the same survey has energy criteria.

rg -n E0025 over 06_math_research JSONL/Markdown found the 2026-09-08 intake and attempts plus 2026-10-10 open list. Earlier attempt gives stable-like examples and no general solution. Read-only git ls-tree origin/master with E0025/subordinator/Hunt filters found no matching recorded answer to this question. No repository working tree was touched.

## Status conclusion

No paper stating and proving the exact universal question was identified. Therefore SOLVED_IN_LITERATURE is not justified. Search coverage is explicitly limited by rate limits and indexing. We proceed with a proved special case and keep the general question unresolved. No claim of novelty is made for the explicit example.

## Second-attempt sources and brain query — 2026-10-12

No new claim of a solution in literature is made. Reused the verified Hu–Sun survey Theorem 2.11(i), Proposition 2.27, Theorem 2.30, and the Hawkes equivalence on p. 4. Lévy jump-bin Poisson counts are the standard Lévy–Itô construction (Bertoin, Lévy Processes, Cambridge University Press, 1996, survey reference [1]); the affinity and singularity argument is proved directly in SECOND_ATTEMPT.md rather than assumed from an unverified Kakutani/Sato reference.

Read-only brain query: math_recall.py "Hunt hypothesis Hu Sun finite energy Clog subordinators good frequency bands arbitrary Levy density". It returned the old atomic witness and general energy cards; none supplies the missing cutoff theorem. No external web searches were run in this continuation.
