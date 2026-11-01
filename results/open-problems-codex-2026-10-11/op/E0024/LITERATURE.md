# Literature verification — E0024

Date: 2026-10-12. No paper found that states and proves Question 4/4′ under precisely its unrestricted hypotheses. This is a bounded negative search, not a proof that no solution exists. VERDICT is not SOLVED_IN_LITERATURE.

## Exact source and scope

Ze-Chun Hu and Wei Sun, *Hunt’s Hypothesis (H) for Markov Processes: Survey and Beyond*, arXiv:1908.06825v1, 19 August 2019; published in *Acta Mathematica Sinica, English Series* **37** (2021), 491–508, DOI 10.1007/s10114-021-9343-7. Downloaded the 27-page arXiv PDF into source_pdf.pdf; its extracted text is source.txt. Crossref verified the journal reference. The following quotations normalize only PDF line breaks and mathematical subscripts.

PDF p. 15:
> Question 4. Let S be a nonempty proper subspace of R^n. Assume that the two projection processes X_S and X_{S⊥} of X on S and S⊥, respectively, are independent and satisfy (H). Does X satisfy (H)?

PDF p. 18:
> Question 4’. Let X_1 and X_2 be Lévy processes on R^n and R^m, respectively. Suppose that X_1 and X_2 are independent and both of them satisfy (H). Does the R^{n+m}-valued Lévy process X = (X_1, X_2) satisfy (H)?

There are NO transition-density, resolvent-density, Gaussian, symmetry, or sector assumptions in this question. The density hypotheses at the start of Section 4 apply to that section, not to Question 4′. (H) means every semipolar set is polar; hitting times use t>0, not t≥0. The dimensions in the product question are positive. Question 4 says ?nonempty proper subspace?, not an arbitrary set. If the zero subspace is included literally, that case is tautological; the nontrivial decomposition has positive factor dimensions.

PDF p. 19 gives Proposition 3.9 (one factor compound Poisson) and Proposition 3.10 (both satisfy condition (S)); these are special cases. PDF pp. 4 and 20 give Rao’s Theorem 2.3 and the finite-energy criterion Theorem 4.2. Proposition 4.8, PDF p. 21 and proof pp. 24–25, concerns only measures η⊗ξ, not arbitrary correlated measures. Remark 5.1(ii), PDF p. 25, gives the implication from product closure to sum closure.

## Search ledger

All requests used Python urllib from the shell. Complete URLs, responses/failures, dates, and local raw-file names are retained in search_log.json. A failed request was not counted as a successful negative search.

- 2026-10-12 — `source_pdf`: https://arxiv.org/pdf/1908.06825 — ok; saved `source_pdf.pdf`.
- 2026-10-12 — `arxiv_http`: http://export.arxiv.org/api/query?search_query=all%3A%22Hunt+hypothesis%22&max_results=50 — HTTP Error 429: Unknown Error; saved `no response file`.
- 2026-10-12 — `arxiv_https`: https://export.arxiv.org/api/query?search_query=all%3A%22Hunt%22+AND+all%3A%22Levy%22&max_results=50&sortBy=submittedDate&sortOrder=descending — HTTP Error 429: Unknown Error; saved `no response file`.
- 2026-10-12 — `openalex_search`: https://api.openalex.org/works?search=Hunt+hypothesis+Levy&per-page=50 — ok; saved `openalex_search.raw`.
- 2026-10-12 — `openalex_source`: https://api.openalex.org/works?search=Hunt%27s+hypothesis+%28H%29+for+Markov+processes%3A+survey+and+beyond&per-page=5 — ok; saved `openalex_source.raw`.
- 2026-10-12 — `crossref`: https://api.crossref.org/works?query=Hunt+hypothesis+Levy+product&rows=30 — ok; saved `crossref.raw`.
- 2026-10-12 — `semantic_search`: https://api.semanticscholar.org/graph/v1/paper/search?query=Hunt+hypothesis&limit=50&fields=title%2Cyear%2Cauthors%2CexternalIds%2Curl%2Cabstract — HTTP Error 429: ; saved `no response file`.
- 2026-10-12 — `semantic_citations`: https://api.semanticscholar.org/graph/v1/paper/ARXIV:1908.06825/citations?limit=100&fields=title%2Cyear%2Cauthors%2CexternalIds%2Curl%2Cabstract — ok; saved `semantic_citations.raw`.
- 2026-10-12 — `github`: https://api.github.com/search/repositories?q=Hunt+hypothesis+Levy&per_page=30 — ok; saved `github.raw`.
- 2026-10-12 — `openalex_citations`: https://api.openalex.org/works?filter=cites%3AW2968964261&per-page=100 — ok; saved `openalex_citations.raw`.
- 2026-10-12 — `openalex_phrase`: https://api.openalex.org/works?search=%22Hunt%27s+hypothesis%22&per-page=100 — ok; saved `openalex_phrase.raw`.
- 2026-10-12 — `crossref_phrase`: https://api.crossref.org/works?query.title=Hunt%27s+hypothesis&rows=50 — ok; saved `crossref_phrase.raw`.
- 2026-10-12 — `arxiv_retry`: https://export.arxiv.org/api/query?search_query=all%3A%22Hunt%27s+hypothesis%22&max_results=30 — The read operation timed out; saved `no response file`.
- 2026-10-12 — `github_phrase`: https://api.github.com/search/repositories?q=%22Hunt+hypothesis%22&per_page=30 — ok; saved `github_phrase.raw`.
- 2026-10-12 — `crossref_math`: https://api.crossref.org/works?query.bibliographic=Hunt+hypothesis+Levy+processes+Hu+Sun&rows=30 — ok; saved `crossref_math.raw`.
- 2026-10-12 — `published_metadata`: https://api.crossref.org/works/10.1007/s10114-021-9343-7 — ok; saved `published_metadata.raw`.
- 2026-10-12 — `openalex_published`: https://api.openalex.org/works/https://doi.org/10.1007/s10114-021-9343-7 — ok; saved `openalex_published.raw`.
- 2026-10-12 — `arxiv_search_html`: https://arxiv.org/search/?query=Hunt%27s+hypothesis&searchtype=all&abstracts=show&order=-announced_date_first&size=50 — ok; saved `arxiv_search_html.raw`.
- 2026-10-12 — `li_pdf`: https://arxiv.org/pdf/2107.06163 — ok; saved `li_pdf.raw`.
- 2026-10-12 — `concentration_pdf`: https://arxiv.org/pdf/2310.03471 — ok; saved `concentration_pdf.raw`.
- 2026-10-12 — `openalex_published_citations`: https://api.openalex.org/works?filter=cites%3AW3121518416&per-page=100 — ok; saved `openalex_published_citations.raw`.
- 2026-10-12 — `bhp2026_pdf`: https://arxiv.org/pdf/2608.13976 — ok; saved `bhp2026_pdf.raw`.
- 2026-10-12 — `bhp2023_pdf`: https://arxiv.org/pdf/2312.02455 — ok; saved `bhp2023_pdf.raw`.
- 2026-10-12 — `bhp2025_pdf`: https://www.aimsciences.org/data/article/export-pdf?id=685bc7da9dd09246775c791d — ok; saved `bhp2025_pdf.raw`.
- 2026-10-12 — `two_theorems_pdf`: https://arxiv.org/pdf/1903.00050 — ok; saved `two_theorems_pdf.raw`.

## Relevant results and later leads

- Hu–Sun, *Hunt’s hypothesis (H) and Getoor’s conjecture for Lévy processes*, Stochastic Processes and their Applications 122 (2012), 2319–2328; DOI 10.1016/j.spa.2012.03.013. Survey Theorems 2.5–2.6 cover nondegenerate Gaussian parts and condition (S).
- Hu–Sun–Zhang, *New Results on Hunt’s Hypothesis (H) for Lévy Processes*, Potential Analysis 42 (2015), 585–605; DOI 10.1007/s11118-014-9446-1. Survey Theorem 4.2 is its Theorem 5.1; this is the criterion used in ATTEMPT.md.
- Hu–Sun, *Further study on Hunt’s hypothesis (H) for Lévy processes*, Science China Mathematics 59 (2016), 2205–2226; DOI 10.1007/s11425-015-0600-2, arXiv:1406.2013. Weaker measure-dependent criteria do not automatically tensorize.
- Hu–Sun, *Hunt’s Hypothesis (H) for the Sum of Two Independent Lévy Processes*, Communications in Mathematics and Statistics 6 (2018), 227–247; DOI 10.1007/s40304-018-0136-y, arXiv:1702.07396. Survey Theorem 2.16 has additional energy and imaginary-part hypotheses. Its title is not a proof of unrestricted sum closure.
- Hu–Sun–Wang, *Two Theorems on Hunt’s Hypothesis (H) for Markov Processes*, arXiv:1903.00050v3 (24 April 2019), published Potential Analysis, DOI 10.1007/s11118-020-09848-2. Downloaded full PDF and extracted two_theorems_pdf.txt. Main results concern local absolute continuity and subordination by a clock with positive drift, not unrestricted products. Publication after 2019 does not make it a solution of the question.
- Murali Rao, *Hunt’s hypothesis for Lévy processes*, Proceedings of the AMS 104 (1988), 621–624; DOI 10.1090/S0002-9939-1988-0962838-6 (also indexed DOI 10.2307/2047022). Rao’s sufficient criterion is reproduced as survey Theorem 2.3.
- Liping Li, *Hunt’s hypothesis and symmetrization for general 1-dimensional diffusions*, arXiv:2107.06163v2, 23 July 2021. Downloaded full paper, li_pdf.txt. Concerns continuous strong Markov processes on the line and asymmetric shunt points. Not a product-of-Lévy-processes theorem.
- Jing Zhang, Ze-Chun Hu, Wei Sun, *On the measure concentration of infinitely divisible distributions*, arXiv:2310.03471v2, 17 October 2023; DOI 10.1007/s10473-025-0211-x. Downloaded full paper, concentration_pdf.txt. A citing work about concentration probabilities, not (H) product closure. Metadata publication years differ across services; use arXiv version date for the fetched text.
- Zhen-Qing Chen and Jie-Ming Wang, *Boundary Harnack principle for non-local operators on metric measure spaces*, arXiv:2312.02455v1 (5 December 2023); DOI 10.1214/24-AOP1734. Downloaded full paper, bhp2023_pdf.txt. BHP for specified Hunt processes, not Hunt’s hypothesis product closure. “Hunt process” and “satisfies (H)” are different assertions.
- Zhen-Qing Chen, *Boundary Harnack principle for jump diffusions*, Discrete and Continuous Dynamical Systems – S 18(10) (2025), 2937–2955; DOI 10.3934/dcdss.2025104. Downloaded published PDF, bhp2025_pdf.txt. BHP survey, not the requested theorem.
- Zhen-Qing Chen and Jie-Ming Wang, *Boundary Harnack principle for diffusion with jumps on metric measure spaces*, arXiv:2608.13976 (2026). Downloaded full PDF, bhp2026_pdf.txt. BHP under quantitative assumptions, not an unrestricted product result.

OpenAlex distinguishes arXiv work W2968964261 (zero citing works in its response) from published work W3121518416 (three citing works). Both were queried. The published citing list contains concentration, nonlocal BHP, and the 2025 BHP survey. Semantic Scholar’s arXiv citing list contains concentration and the 2023/2026 BHP papers. These are all leads, not a solution in print. The arXiv API returned HTTP 429 or timed out; the successful arxiv.org HTML search was inspected title by title, with Li’s 2021 diffusion paper the only post-survey match on the mathematical (H) topic. Broad unquoted searches produced irrelevant “Hunt” results; quoted and bibliographic follow-ups were therefore run. GitHub returned zero for the mathematical query and five cybersecurity repositories for the broader phrase; none is mathematical evidence.

## Read-only brain and earlier work

Before attempting: brain.py recall "Hunt hypothesis Levy product mistakes"; math_recall.py "Hunt hypothesis Kanda Forst product Levy"; brain.py node a_pure_jump_subordinator_can_break_kanda_forst_2026_09_13. These are hints only. The subordinator memory explicitly labels its proposed polarity estimate heuristic, despite a stronger summary label; it was not used as a proved counterexample or (H) example.

Read intake records E0024-A001 and E0024 in probability_1000_intake_E_20260908 (saved relevant records to earlier_records.json). Read origin/master:prob1000_lean_20260908/ultracode_20260909/E0024/memo.md and U_E0024.lean using git show, with no working-tree changes. These contain a sector perturbation reduction and the unresolved symmetric-partner energy problem. This session re-proves that reduction with the sharp algebraic constant, and does not claim the reduction itself is new. The older intake’s unconditional resolvent-density product assertion is not justified; ATTEMPT.md gives the exact counterexample to that assertion and uses explicit product-density hypotheses instead. The earlier memo already had those hypotheses stated correctly.

During the attempt, also ran brain.py recall "Hunt hypothesis Levy independent product" and read math-store card claim_fc2810725f4f4b23a924b0d3f7cc75c4 in full. The card concerns Question 5, not a solution of Question 4.

## Renewed attempt: sources and searches (2026-10-12)

Read Hu-Sun-Wang arXiv:1903.00050v3 again: Theorem 1.1(i), PDF p.3, transfers (H) under local path-law absolute continuity; Theorem 4.5, PDF p.14, is the exact Levy triplet test; Remark 4.6 and Corollary 4.8, PDF p.15, check drift-integral finiteness and state only (H_m) for general symmetric references, with a density condition for promotion to (H). These are neighbouring theorems, not an unrestricted product solution.

Mamoru Kanda, Notes on energy for space-time processes over Levy processes, Nagoya Mathematical Journal 122 (1991), 63-74, DOI 10.1017/S0027763000003536. Retrieved OpenAlex W1500198325 and its Cambridge PDF, saved kanda_original.pdf and kanda_original.txt. Checked resolvent-density assumptions at printed p.65/PDF p.3 and Corollary of Lemma 2.1 at printed p.66/PDF p.4. It proves positive-measure energy monotonicity in lambda and under domination. It does not provide monotonicity for complex slices.

Crossref found Shizuo Kakutani, On Equivalence of Infinite Product Measures, Annals of Mathematics 49(1) (1948), starting p.214, DOI 10.2307/1969123. This was a Hellinger-method lead; no theorem from the unfetched paper is used in the proof. The required Levy-law criterion comes directly from fetched Hu-Sun-Wang Theorem 4.5.

Brain queries: "Hunt hypothesis Kanda energy complex measures approximation resolvent"; "Hu Sun Wang local absolute continuity Hunt hypothesis symmetric Levy"; "Kakutani Hellinger equivalence product Poisson measures"; "Glover Rao subordination Hunt hypothesis". Returned relevant cards describe energy and Hellinger distance, but none proves the missing assertion; irrelevant matches were not used.

New HTTP ledger entries follow; full URLs and responses are also in search_log.json. No exact literature solution was identified. B4 is a written derivation here, not SOLVED_IN_LITERATURE and not claimed novel.

- 2026-10-12 -- openalex_symmetric_H: https://api.openalex.org/works?search=%22symmetric+L%C3%A9vy%22+%22Hunt%22&per-page=30 -- ok; openalex_symmetric_H.raw.

- 2026-10-12 -- crossref_kakutani: https://api.crossref.org/works?query.bibliographic=Kakutani+equivalence+infinite+product+measures+1948&rows=5 -- ok; crossref_kakutani.raw.

- 2026-10-12 -- openalex_absolute_H: https://api.openalex.org/works?search=%22Hunt%22+%22absolute+continuity%22+%22L%C3%A9vy%22&per-page=30 -- ok; openalex_absolute_H.raw.

- 2026-10-12 -- kanda_original_pdf: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/4902C34821D8E5175FDC8FBB68DF81F8/S0027763000003536a.pdf/div-class-title-notes-on-energy-for-space-time-processes-over-levy-processes-div.pdf -- ok; kanda_original.pdf.

- 2026-10-12 -- kanda_metadata: https://api.openalex.org/works/W1500198325 -- ok; kanda_metadata.json.
