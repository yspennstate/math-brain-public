# E0027 literature audit

Audit date: 2026-10-12. No paper found that states and proves the unrestricted independent-sum question. This is a bounded search result, not a proof that no solution exists. Verdict remains PARTIAL, not SOLVED_IN_LITERATURE.

## Verified source and exact scope

Ze-Chun Hu and Wei Sun, *Hunt's Hypothesis (H) for Markov Processes: Survey and Beyond*, arXiv:1908.06825v1, 19 August 2019. Published as *Acta Mathematica Sinica, English Series* 37(3) (2021), 491-508, DOI 10.1007/s10114-021-9343-7. The question locator refers to the arXiv PDF p. 25, Question 7; that PDF was downloaded and its text extracted in source.txt.

The following is the exact wording, with the PDF's split lines rejoined and its accented character normalized to Unicode:

> Question 7. Suppose that X and Y are two independent n-dimensional Lévy processes satisfying (H). Does X + Y satisfy (H)? We have mentioned this question in [21].

The only hypotheses are independent n-dimensional Levy processes and (H) for each. No extra hypotheses appear. (H) means every semipolar set is polar, with hitting times defined as inf{t>0: X_t is in D}.

Remark 5.1(i) links a positive answer to Question 6 (the unbounded-variation one-dimensional problem), citing Kesten's Theorem 1(f). Remark 5.1(ii) reduces it to the independent-product problem, Question 4. These are implications, not solutions.

## Relevant references and what they actually prove

1. Hu and Sun, source above. Theorems 2.14 and 2.15, arXiv PDF p. 8: compound Poisson perturbations of (H) processes, and independent sums of two processes satisfying condition (S). Theorem 2.16, pp. 8-9: a result with resolvent densities, finite-energy inclusion, and control of the second exponent's imaginary part. It explicitly leaves Question 7 open. Lemma 3.1, pp. 13-14, gives preservation under projection; Question 4', p. 18, asks product stability. Proposition 2.13, p. 8, gives the criterion used in ATTEMPT.md.
2. Ze-Chun Hu and Wei Sun, *Hunt's Hypothesis (H) for the Sum of Two Independent Levy Processes*, *Communications in Mathematics and Statistics* 6(2) (2018), 227-247, DOI 10.1007/s40304-018-0136-y; arXiv:1702.07396. Full arXiv PDF downloaded, 21 pages. Despite the matching title, it is NOT an answer under just (H)+(H). Theorem 4.1 and Proposition 4.2, PDF p. 14, require extra energy/exponent hypotheses. Theorem 3.2 treats condition (S). Proposition 4.5, PDF p. 15, extends a Rao-type argument with an integrable remainder; it still imposes explicit bounds. The survey also records a correction to an auxiliary lemma of this paper in Remark 3.8, PDF p. 18: an additional projection-(H) hypothesis is needed in its Lemma 3.5; Theorem 3.1 remains valid.
3. Murali Rao, *Hunt's hypothesis for Levy processes*, *Proceedings of the American Mathematical Society* 104(2) (1988), 621-624, DOI 10.1090/S0002-9939-1988-0962838-6. Theorem 2, journal p. 622 / PDF p. 2, is the increasing-envelope sufficient condition. Actual four-page PDF downloaded as rao_actual.pdf. The first AMS URL returned a 93-page rendering of a journal contents page despite HTTP 200; this is NOT treated as the paper. The alternate /journals/proc/ URL returned the real article.
4. Ze-Chun Hu, Wei Sun and Li-Fei Wang, *Two Theorems on Hunt's Hypothesis (H) for Markov Processes*, arXiv:1903.00050; published *Potential Analysis* (2020 online), DOI 10.1007/s11118-020-09848-2. Full 25-page arXiv PDF downloaded. Theorem 1.1, p. 3, concerns local absolute continuity of process laws; Theorem 1.3, p. 4, concerns subordination by an independent subordinator with positive drift. Neither asserts the independent-sum question. This is a lead if one could verify local absolute continuity for a particular sum; it is not automatic.
5. Liping Li, *Hunt's hypothesis and symmetrization for general 1-dimensional diffusions*, arXiv:2107.06163v2, 23 July 2021. Full 14-page PDF downloaded. Concerns continuous one-dimensional strong Markov diffusions, symmetry and shunt-point classifications; not arbitrary Levy sums. No theorem matching Question 7 found there.
6. Ze-Chun Hu and Wei Sun, *Further study on Hunt's hypothesis (H) for Levy processes*, *Science China Mathematics* 59 (2016), 2205-2226, DOI 10.1007/s11425-015-0600-2; arXiv:1406.2013. Identified from the source references and API records; not independently downloaded in this attempt. Survey Theorems 2.11-2.12 cite its measure-dependent criteria. These criteria cannot simply be replaced by a global pointwise envelope.
7. Ze-Chun Hu, Wei Sun and Jing Zhang, *New Results on Hunt's Hypothesis (H) for Levy Processes*, *Potential Analysis* 42 (2015), 585-605, DOI 10.1007/s11118-014-9446-1; arXiv:1210.2016. Identified in survey and API records; not independently downloaded. The survey's Theorem 2.8 attributes an extended Kanda-Forst-Rao condition to it; it is a lead outside ordinary global-envelope arguments.
8. Ze-Chun Hu and Wei Sun, *Hunt's hypothesis (H) and Getoor's conjecture for Levy processes*, *Stochastic Processes and their Applications* 122 (2012), 2319-2328, DOI 10.1016/j.spa.2012.03.013; arXiv:1101.3038. Survey Theorems 2.5-2.6 cite its Gaussian/condition-(S) results. Identified, not independently downloaded.

## Forward citations checked under the correct identities

OpenAlex distinguishes the arXiv source W2968964261 (zero citing works returned) from the journal source W3121518416 (three citing works). Both were queried. Querying just the arXiv record would miss the following three journal citations:

* Jing Zhang, Ze-Chun Hu and Wei Sun, *On the measure concentration of infinitely divisible distributions*, arXiv:2310.03471v2 (17 October 2023); journal DOI 10.1007/s10473-025-0211-x, OpenAlex reports volume 45(2), 473-492 and year 2024. The DOI contains 2025, so the journal year metadata is recorded without resolving the discrepancy. Full 25-page preprint downloaded. Main results bound standardized mass concentration of infinitely divisible laws. PDF p. 2 calls Getoor's conjecture unsolved. This is not sum stability for (H).
* Zhen-Qing Chen, *Boundary Harnack principle for jump diffusions*, *Discrete and Continuous Dynamical Systems - S* 18(10) (October 2025), 2937-2955, DOI 10.3934/dcdss.2025104. Full 19-page PDF downloaded. Theorem 4.12, PDF p. 17 / journal p. 2953, states (H) for certain subordinate Brownian motions with a positive Gaussian component and additional subordinator assumptions. This is a special class, not Question 7; its main subject is boundary Harnack principles.
* Zhen-Qing Chen and Jieming Wang, *Boundary Harnack principle for nonlocal operators on metric measure spaces*, *Annals of Probability* 53(4) (2025), 1287-1330, DOI 10.1214/24-AOP1734. OpenAlex abstract and the preceding survey's detailed account were checked. It treats weak-duality Hunt processes and subordinate Brownian motions with Gaussian components, with geometric/comparability assumptions. No unrestricted sum-stability claim was identified. Its own full text was not retrieved, so this is a metadata/survey check, not a full-paper verification.

The 2018 sum paper's journal identity W2729024139 has four indexed citing works: the survey's journal and arXiv versions, and the transformation paper's journal and arXiv versions. No later solution appeared in this citation set.

Semantic Scholar's exact-phrase bulk query returned 31 records (including irrelevant lexical matches and duplicate journal/preprint versions); the newest relevant mathematical work found was Li's 2021 diffusion paper. Its broader query returned 1,000 of 1,526 records, so that broader query is not represented as exhaustive. The exact query and arXiv HTML search supplement it. Semantic Scholar's journal-source citation endpoint returned no citations, in conflict with OpenAlex's journal-source count; we used both rather than treating the empty response as decisive.

## Exhaustive service/query log for this attempt

Every request below was made on 2026-10-12 from Python urllib, never a built-in web-search tool. URL query parameters are the exact service query. Raw responses and error/status records are retained in this directory. HTTP 429 requests failed and carry no negative-search weight. An HTTP 200 is checked for relevance rather than assumed to be a theorem.

- **source_pdf**, 2026-10-12: `https://arxiv.org/pdf/1908.06825`; 200; raw source_pdf.pdf
- **semantic**, 2026-10-12: `https://api.semanticscholar.org/graph/v1/paper/search?query=Hunt+hypothesis&limit=50&fields=title%2Cauthors%2Cyear%2CexternalIds%2Curl%2Cabstract`; HTTP Error 429: 
- **github**, 2026-10-12: `https://api.github.com/search/repositories?q=%22Hunt+hypothesis%22&per_page=30`; 200; raw github.json
- **openalex_source**, 2026-10-12: `https://api.openalex.org/works?search=Hunt%27s+hypothesis+%28H%29+for+Markov+processes%3A+survey+and+beyond&per-page=5`; 200; raw openalex_source.json
- **openalex**, 2026-10-12: `https://api.openalex.org/works?search=Hunt+hypothesis&per-page=50`; 200; raw openalex.json
- **crossref**, 2026-10-12: `https://api.crossref.org/works?query=Hunt+hypothesis+Levy+sum&rows=30`; 200; raw crossref.json
- **arxiv**, 2026-10-12: `http://export.arxiv.org/api/query?search_query=all%3A%22Hunt+hypothesis%22+OR+all%3A%22Hunt%27s+hypothesis%22&start=0&max_results=50&sortBy=submittedDate&sortOrder=descending`; HTTP Error 429: Too Many Requests
- **github_levy**, 2026-10-12: `https://api.github.com/search/repositories?q=Hunt+Levy+hypothesis&per_page=30`; 200; raw github_levy.json
- **s2_source**, 2026-10-12: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:1908.06825?fields=title,year,citations.title,citations.year,citations.externalIds`; HTTP Error 429: 
- **oa_citing**, 2026-10-12: `https://api.openalex.org/works?filter=cites%3AW2968964261&per-page=100`; 200; raw oa_citing.json
- **cr_exact**, 2026-10-12: `https://api.crossref.org/works?query.title=Hunt%27s+hypothesis&rows=50`; 200; raw cr_exact.json
- **oa_levy**, 2026-10-12: `https://api.openalex.org/works?search=Hunt+hypothesis+Levy&per-page=50`; 200; raw oa_levy.json
- **oa_exact**, 2026-10-12: `https://api.openalex.org/works?search=Hunt%27s+hypothesis&per-page=100`; 200; raw oa_exact.json
- **arxiv_https**, 2026-10-12: `https://export.arxiv.org/api/query?search_query=all%3A%22Hunt%22+AND+all%3A%22hypothesis%22+AND+cat%3Amath.PR&max_results=50&sortBy=submittedDate&sortOrder=descending`; HTTP Error 429: Unknown Error
- **diffusion_pdf**, 2026-10-12: `https://arxiv.org/pdf/2107.06163`; 200; raw diffusion_pdf.json
- **oa_sum**, 2026-10-12: `https://api.openalex.org/works?search=Hunt%E2%80%99s+Hypothesis+for+the+sum+of+two+independent+L%C3%A9vy+processes&per-page=15`; 200; raw oa_sum.json
- **s2_bulk**, 2026-10-12: `https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=%22Hunt%22+%2B+%22hypothesis%22&fields=title%2Cyear%2Cauthors%2CexternalIds&sort=publicationDate%3Adesc`; 200; raw s2_bulk.json
- **arxiv_search**, 2026-10-12: `https://arxiv.org/search/?query=Hunt+hypothesis&searchtype=all&abstracts=show&order=-announced_date_first&size=50`; 200; raw arxiv_search.json
- **oa_title**, 2026-10-12: `https://api.openalex.org/works?filter=title.search%3AHunt&search=hypothesis&per-page=100`; 200; raw oa_title.json
- **cr_sum**, 2026-10-12: `https://api.crossref.org/works?query.bibliographic=Hu+Sun+Hunt%E2%80%99s+hypothesis+L%C3%A9vy+processes&rows=50`; 200; raw cr_sum.json
- **rao_pdf**, 2026-10-12: `https://www.ams.org/proc/1988-104-02/S0002-9939-1988-0962838-6/S0002-9939-1988-0962838-6.pdf`; 200; raw rao_pdf.json
- **sum_pdf**, 2026-10-12: `https://arxiv.org/pdf/1702.07396`; 200; raw sum_pdf.json
- **transforms_pdf**, 2026-10-12: `https://arxiv.org/pdf/1903.00050`; 200; raw transforms_pdf.json
- **oa_citing_sum**, 2026-10-12: `https://api.openalex.org/works?search=Hunt%E2%80%99s+Hypothesis+%28H%29+for+the+Sum+of+Two+Independent+L%C3%A9vy+Processes&per-page=5`; 200; raw oa_citing_sum.json
- **oa_published_sum**, 2026-10-12: `https://api.openalex.org/works/https://doi.org/10.1007/s40304-018-0136-y`; 200; raw oa_published_sum.json
- **s2_citations**, 2026-10-12: `https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/s10114-021-9343-7/citations?fields=title,year,externalIds,abstract&limit=100`; 200; raw s2_citations.json
- **s2_exact_bulk**, 2026-10-12: `https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=%22Hunt%E2%80%99s+hypothesis%22&fields=title%2Cyear%2Cauthors%2CexternalIds%2Cabstract&sort=publicationDate%3Adesc`; 200; raw s2_exact_bulk.json
- **cr_source_doi**, 2026-10-12: `https://api.crossref.org/works/10.1007/s10114-021-9343-7`; 200; raw cr_source_doi.json
- **oa_published_source**, 2026-10-12: `https://api.openalex.org/works/https://doi.org/10.1007/s10114-021-9343-7`; 200; raw oa_published_source.json
- **cr_sum_exact**, 2026-10-12: `https://api.crossref.org/works/10.1007/s40304-018-0136-y`; 200; raw cr_sum_exact.json
- **oa_citing_published**, 2026-10-12: `https://api.openalex.org/works?filter=cites%3AW3121518416&per-page=100`; 200; raw oa_citing_published.json
- **oa_citing_sum_actual**, 2026-10-12: `https://api.openalex.org/works?filter=cites%3AW2729024139&per-page=100`; 200; raw oa_citing_sum_actual.json
- **rao_alternate**, 2026-10-12: `https://www.ams.org/journals/proc/1988-104-02/S0002-9939-1988-0962838-6/S0002-9939-1988-0962838-6.pdf`; 200; raw rao_alternate.json
- **bhp_search**, 2026-10-12: `https://arxiv.org/search/?query=Boundary+Harnack+principle+for+nonlocal+operators+on+metric+measure+spaces&searchtype=title&abstracts=show&size=50`; 200; raw bhp_search.json
- **concentration_pdf**, 2026-10-12: `https://arxiv.org/pdf/2310.03471`; 200; raw concentration_pdf.json
- **bhp_survey_pdf**, 2026-10-12: `https://www.aimsciences.org/data/article/export-pdf?id=685bc7da9dd09246775c791d`; 200; raw bhp_survey_pdf.json


## Read-only local research searches

* math_recall.py query "Hunt hypothesis sum Levy Kanda Forst". Returned the subordinator-envelope caution and general Levy-process cards, not a verified sum theorem.
* brain.py recall "Hunt hypothesis Levy sums" and "Hunt hypothesis mistakes". Its output unexpectedly reported an automatic detached index refresh; we did not invoke a memory-write command and made no further brain.py calls. This side effect was reported by the mandated recall script, not explicitly requested by this attempt.
* Read-only intake search for E0027 in problems.jsonl, attempts.jsonl and sources.jsonl under probability_1000_intake_* identified E0027-A001 dated 2026-09-08. Its arbitrary-Rao-envelope closure inference is corrected in ATTEMPT.md Section 3. Its claim of general resolvent-density inheritance is not used; Section 6 gives an explicit obstruction without (H).
* Checked the codex_pool_2026_10_10 top-level problem ledger, ledger and manifest for E0027: no match returned. This is not a recursive audit of every worker file.
* git ls-tree -r --name-only origin/master, filtered for E0027: no matching path. No repository was changed; no files from its working tree were read. The first unfiltered command produced excessive output; the repeat filtered it within Python.

No exact theorem proving or disproving Question 7 was located. Accordingly no SOLVED_IN_LITERATURE theorem quote or line-by-line solution attribution is claimed.


## User-requested second attempt, 2026-10-12

New read-only math-store queries targeted the actual gap:

* math_recall.py "Hunt hypothesis finite energy sum extended Kanda Forst Rao integrable remainder Hu Sun": subordinator/Kanda-Forst caution, general finite-energy definitions, and unrelated results; no verified closure lemma.
* math_recall.py "Levy local absolute continuity Hellinger change measure Hunt hypothesis": general absolute-continuity and Hellinger cards, not the Levy path-law theorem. These hints were not treated as proof.

Read directly from the saved PDFs:

* Hu-Sun 2018, arXiv:1702.07396, Proposition 4.5, PDF p. 15 and proof pp. 17-18. It treats one EKFR summand plus one Rao-controlled summand; its frequency split motivates the two-remainder conditional result in SECOND_ATTEMPT.md. It does not prove the unrestricted question.
* Hu-Sun-Wang, arXiv:1903.00050v3, Theorem 4.5, PDF p. 14, reproduces the local absolute-continuity criterion from Jacod-Shiryaev, Chapter IV, Theorem 4.39(c): unchanged Gaussian covariance, absolute continuity of Levy measures with finite Hellinger integral, and a drift equation. Theorem 4.7, PDF p. 15, transfers (H) under those hypotheses. Its Theorem 1.1, PDF p. 3, is the underlying general Markov-process result. Jacod-Shiryaev's book was not independently fetched. This is a verified neighbouring theorem, not an exact solution to E0027.
* Hu-Sun-Zhang, *New results on Hunt's hypothesis (H) for Levy processes*, arXiv:1210.2016v3, 15 April 2014; published *Potential Analysis* 42 (2015), 585-605, DOI 10.1007/s11118-014-9446-1. Newly downloaded full 24-page PDF. Section 4, PDF p. 11, explicitly assumes lower semicontinuity of all 1-excessive functions, equivalently resolvent densities. Theorem 4.5, PDF p. 13, gives EKFR; proof p. 14. This verifies the exact analytic input and its density hypothesis independently of the survey. Example 4.8, PDF p. 15, includes a class with strong small-jump real growth and says any independent perturbation still satisfies (H); it is a stronger special case, not a solution for two arbitrary (H) processes.

The new network request was https://arxiv.org/pdf/1210.2016 on 2026-10-12, HTTP 200, saved as ekfr_original.pdf and extracted to ekfr_original.txt; the exact status is also appended to search_log.jsonl. No fresh complete multi-service status audit was needed for this mathematical follow-up; the first attempt's bounded status audit is retained above.

No claim of novelty or SOLVED_IN_LITERATURE is made for the deductions in the renewed attempt.
