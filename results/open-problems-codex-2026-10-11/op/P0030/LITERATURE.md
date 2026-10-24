# Literature verification for P0030

Date: 2026-10-12. All network requests used Python urllib from the shell; no built-in web search was used. Raw responses and request URLs are saved in this folder. This is a bounded search, not proof of absence from the literature.

## Outcome

No inspected paper states and proves Problems 7.1–7.3 with their exact hypotheses. Verdict is PARTIAL, not SOLVED_IN_LITERATURE. OpenAlex returned HTTP 429 on every attempt, so its source record and works-citing-source coverage could not be completed. Semantic Scholar search/source metadata returned HTTP 429, but its source-citations endpoint succeeded and returned one citing paper without a next-page marker. Coverage is limited by the services' indexes as well as the rate limit.

## Exact source and statements

Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian motion*, Probability Theory and Related Fields **160** (2014), nos.1–2, 95–126. DOI: 10.1007/s00440-013-0524-x. arXiv:1302.6958v4, 29 March 2013. Crossref's online publication date is 27 August 2013; the volume citation is 2014. Downloaded Washington-hosted PDF has 27 pages; Definitions 2.1–2.2 on pp.2–3 and Problems 7.1–7.3 on pp.25–26. The exact transcribed questions and definitions appear in ATTEMPT.md. The provided source URL is https://math.washington.edu/sites/math/files/documents/research/1302.6958.pdf (saved as source.pdf and source.txt).

Theorem 5.1, p.18, says word for word:

> Theorem 5.1. If X is strongly decomposable and ET_k < ∞ then X is 2BM.

The subscript is transcribed from PDF notation. This is a proved special case in the source, not a solution to Problem 7.1: Definition 2.2 permits independent nonidentically distributed stopped pieces and infinite means, while Theorem 5.1 assumes identical distributions and finite mean. Its proof uses renewal stationarization and total variation convergence. Theorems 5.2 and 5.3 give decomposable processes not BBM, so they do not supply counterexamples with the additional BBM hypothesis. Theorem 6.1 and Proposition 6.2 give FBM+BBM without 2BM, but that process is not decomposable and does not admit the independent cut needed in 7.2/7.3.

## Citing paper inspected

Jim Pitman and Wenpin Tang, *The Slepian zero set, and Brownian bridge embedded in Brownian motion by a spacetime shift*, Electronic Journal of Probability **20** (2015), paper 61, 1–28. DOI: 10.1214/EJP.v20-3911. arXiv:1411.0040v2, 11 June 2015. Semantic Scholar labels the initial preprint 2014. Full PDF downloaded from https://arxiv.org/pdf/1411.0040 and saved as pitman_tang.pdf and pitman_tang.txt.

Theorem 1.3 on PDF p.3 says:

> Theorem 1.3. There exists a random time T ≥ 0 such that (B_{T+u} − B_T; 0 ≤ u ≤ 1) has the same distribution as (b^0_u; 0 ≤ u ≤ 1).

This embeds one unit-length Brownian bridge into a Brownian path. It assumes an already Brownian process and gives one finite-window marginal; it neither treats arbitrary decomposable FBM+BBM nor proves a two-sided Wiener law after a common shift. It is a lead on shift-coupling, not a solution in print. Page 3 explicitly discusses Burdzy–Scheutzow and says the general case with pieces not identically distributed is left open (their informal summary must not be read as an exact restatement of Problem 7.1). The cited general shift-coupling and allocation results are possible tools, not automatically a solution to the compatibility question.

## Further exact references (leads cited in inspected papers)

- Günter Last, Peter Mörters and Hermann Thorisson, *Unbiased shifts of Brownian motion*, Annals of Probability **42** (2014), no.2, 431–463. This starts from Brownian motion and characterizes certain shifts preserving its law; it does not by that description stationarize an arbitrary FBM+BBM. Reference and relevance checked against Pitman–Tang pp.3 and 26–27; full theorem not checked here.
- Hermann Thorisson, *Transforming random elements and shifting random fields*, Annals of Probability **24** (1996), no.4, 2057–2064. General shift-coupling lead, cited as [83] by Pitman–Tang, and used in their Theorem 5.9. No application supplying the missing invariant-law hypotheses has been proved here.
- Hermann Thorisson, *Coupling, stationarity, and regeneration*, Springer, New York, 2000. Background in source Theorem 5.1 and Pitman–Tang references; no claim that its general theorems alone answer this question.
- J. Bertoin and M. Savov, *Some applications of duality for Lévy processes in a half-line*, Bulletin of the London Mathematical Society **43** (2011), no.1, 97–110. Source's Example 2.8 cites it for a duality example, not a compatibility solution.

## Search log


1. Date 2026-10-12; service/query `arxiv_http`; outcome `200`. Request: http://export.arxiv.org/api/query?search_query=all%3A%22forward%20Brownian%20motion%22&max_results=30 . Raw record: search_arxiv_http.txt.

2. Date 2026-10-12; service/query `arxiv_https`; outcome `200`. Request: https://export.arxiv.org/api/query?search_query=all%3A%22forward%20Brownian%20motion%22&max_results=30 . Raw record: search_arxiv_https.txt.

3. Date 2026-10-12; service/query `openalex_title`; outcome `ERROR`. Request: https://api.openalex.org/works?search=Forward%20Brownian%20motion&per-page=30 . Raw record: search_openalex_title.txt.

4. Date 2026-10-12; service/query `crossref`; outcome `200`. Request: https://api.crossref.org/works?query.title=Forward%20Brownian%20motion&rows=20 . Raw record: search_crossref.txt.

5. Date 2026-10-12; service/query `semantic`; outcome `ERROR`. Request: https://api.semanticscholar.org/graph/v1/paper/search?query=Forward%20Brownian%20motion&limit=30&fields=title,authors,year,abstract,externalIds,url . Raw record: search_semantic.txt.

6. Date 2026-10-12; service/query `github`; outcome `200`. Request: https://api.github.com/search/repositories?q=%22forward%20Brownian%22 . Raw record: search_github.txt.

7. Date 2026-10-12; service/query `openalex_compat`; outcome `ERROR`. Request: https://api.openalex.org/works?search=decomposable%20forward%20backward%20Brownian%20motion&per-page=20 . Raw record: search_openalex_compat.txt.

8. Date 2026-10-12; service/query `openalex_retry`; outcome `ERROR`. Request: https://api.openalex.org/works?search=%22Forward%20Brownian%20motion%22&per_page=10 . Raw record: search_openalex_retry.txt.

9. Date 2026-10-12; service/query `openalex_doi`; outcome `ERROR`. Request: https://api.openalex.org/works/https://doi.org/10.1214/13-EJP3343 . Raw record: search_openalex_doi.txt.

10. Date 2026-10-12; service/query `semantic_source`; outcome `ERROR`. Request: https://api.semanticscholar.org/graph/v1/paper/ARXIV:1302.6958?fields=title,year,authors,externalIds,citations.title,citations.year,citations.abstract,citations.externalIds . Raw record: search_semantic_source.txt.

11. Date 2026-10-12; service/query `arxiv_decomp`; outcome `200`. Request: https://export.arxiv.org/api/query?search_query=all%3A%22decomposable%22%20AND%20all%3A%22Brownian%22&max_results=30 . Raw record: search_arxiv_decomp.txt.

12. Date 2026-10-12; service/query `arxiv_authors`; outcome `200`. Request: https://export.arxiv.org/api/query?search_query=au%3ABurdzy%20AND%20au%3AScheutzow&max_results=40 . Raw record: search_arxiv_authors.txt.

13. Date 2026-10-12; service/query `crossref_compat`; outcome `200`. Request: https://api.crossref.org/works?query=%22backward%20Brownian%22%20%22forward%20Brownian%22&rows=20 . Raw record: search_crossref_compat.txt.

14. Date 2026-10-12; service/query `github_decomp`; outcome `200`. Request: https://api.github.com/search/repositories?q=Brownian%20decomposable . Raw record: search_github_decomp.txt.

15. Date 2026-10-12; service/query `openalex_correct_doi`; outcome `ERROR`. Request: https://api.openalex.org/works/https://doi.org/10.1007/s00440-013-0524-x . Raw record: search_openalex_correct_doi.txt.

16. Date 2026-10-12; service/query `openalex_citing_filter`; outcome `ERROR`. Request: https://api.openalex.org/works?filter=references.doi:https%3A//doi.org/10.1007/s00440-013-0524-x&per-page=100 . Raw record: search_openalex_citing_filter.txt.

17. Date 2026-10-12; service/query `openalex_citing_search`; outcome `ERROR`. Request: https://api.openalex.org/works?search=1302.6958&per-page=50 . Raw record: search_openalex_citing_search.txt.

18. Date 2026-10-12; service/query `semantic_citations`; outcome `200`. Request: https://api.semanticscholar.org/graph/v1/paper/ARXIV:1302.6958/citations?fields=title,year,abstract,externalIds&limit=100 . Raw record: search_semantic_citations.txt.

19. Date 2026-10-12; service/query `crossref_exact`; outcome `200`. Request: https://api.crossref.org/works/10.1007/s00440-013-0524-x . Raw record: search_crossref_exact.txt.

20. Date 2026-10-12; service/query `arxiv_stationary`; outcome `200`. Request: https://export.arxiv.org/api/query?search_query=all%3A%22forward%20Brownian%22%20AND%20%28all%3Astationary%20OR%20all%3Acoupling%29&max_results=30 . Raw record: search_arxiv_stationary.txt.

21. Date 2026-10-12; service/query `arxiv_backward`; outcome `200`. Request: https://export.arxiv.org/api/query?search_query=all%3A%22backward%20Brownian%20motion%22&max_results=50 . Raw record: search_arxiv_backward.txt.

22. Date 2026-10-12; service/query `citing_paper_pdf`; outcome `download inspected`. Request: https://arxiv.org/pdf/1411.0040 . Raw record: pitman_tang.pdf.


## Search results and limitations by service

- arXiv exact phrase "forward Brownian motion" returned the source and an unrelated Brownian-web paper. HTTP and HTTPS requests had the same two entries. Author query Burdzy AND Scheutzow returned only the source. The query for decomposable AND Brownian returned 30 heterogeneous items (reflecting Brownian motion, stochastic finance, stretched Brownian motion, loop soups, etc.); titles and abstracts were inspected and none addressed the exact compatibility questions. The backward-Brownian phrase returned one unrelated SPDE/derivative-pricing paper. The forward-Brownian/stationary-or-coupling query returned no entries. Search limits and full queries are retained above.
- Crossref title search identified the correct source DOI. The compatibility query returned forward/backward stochastic differential equation papers (including G-Brownian motion), rather than this path-decomposition model. The direct DOI response confirmed authors, volume, pages and online date, and counted one reference to the source; Crossref is not used here as a comprehensive reverse-citation index.
- Semantic Scholar citation endpoint returned Pitman–Tang only. Its PDF was read for its actual theorem and discussion of the source; this is the most relevant subsequent item found.
- GitHub exact phrase query returned zero repositories. Brownian decomposable returned eleven finance/simulation repositories, all unrelated on title and description. No repository result was treated as a proved mathematical solution.
- OpenAlex source/title/compatibility/citation attempts all failed with HTTP 429. The first direct DOI guess (10.1214/13-EJP3343) was an unverified locator and is NOT the source DOI; it failed and was superseded by the Crossref-confirmed DOI. The attempted `references.doi` citation filter is not a validated OpenAlex filter; it also failed before any response data. Consequently no source OpenAlex work ID could be resolved and no valid ID-based citing-works enumeration was possible. The DOI/source-identifier searches are logged as failed attempts, not successful coverage.

## Read-only earlier work and brain checks

Before mathematics, read-only math_recall queries: "Burdzy Scheutzow forward Brownian decomposable backward"; later "Thorisson shift coupling stationary regeneration Brownian". Brain recall queries: "forward Brownian motion mistakes" and "Compatibility forward backward Brownian decompositions". Recall hints identify the earlier common-splice obstruction and a candidate solution to the different Problem 7.5; none is accepted as a verdict on 7.1–7.3.

Intake `problems.jsonl`, `attempts.jsonl`, and `sources.jsonl` were searched for P0030 in the probability_1000_intake_* directories. Campaign records were searched in codex_pool_2026_10_10. The origin/master file probability_campaigns/codex_pool_2026-10-10/team_O/w332/reports/P0030_attempt.md was read with git show. Auditor w346's rows 12–13 correct the older phrase "finite Brownian bridge" to "finite Brownian-motion segment" and retain the future-selection mean obstruction. No repository working tree, ledger, brain, or store was intentionally modified.

The during-attempt math-store recall again returned the candidate Problem 7.5 prefix-filling argument and standard ergodicity cards. Prefix insertion concerns a different problem and may change the path rather than only center it; it was not used to claim a solution to 7.1–7.3.


# Second-attempt literature and brain checks, 2026-10-12

The gap itself was queried, read-only, with math_recall.py:

- "Thorisson shift coupling invariant sigma field ergodic absolutely continuous random shift".
- "Kakutani product measures Hellinger equivalence independent stopping times regeneration".
- Linked card read in full: claim_2b15255aa3a9ad0d5f14525fa3513e2c3fed532d5e9ecbdaa534014e943ad3e7, *A randomized forward filling lemma for an ergodic stationary law*.

The first recall returned the candidate Problem 7.5 filling scheme and standard ergodicity cards. The recalled filling lemma transports an invariant law P to a biased law fP; this attempt instead proved the needed opposite transport direction fP to P in ATTEMPT.md, Lemma E. Auxiliary uniform randomness is an explicit assumption of the card and of the newly proved lemma. The second query returned Hellinger definitions and nearby stopping-time cards, but no card proving the proposed stopped-piece compatibility implication. These cards were hints, not verdicts.

New exact references checked:

1. Shizuo Kakutani, *On Equivalence of Infinite Product Measures*, Annals of Mathematics, second series, **49** (1948), no.1, 214–224. DOI 10.2307/1969123. Crossref confirmed title, author, volume, January 1948, and starting page 214. The one-way sufficient domination argument needed here was proved in full independently as Lemma G; no unstated use of the equivalence half of Kakutani's theorem occurs.
2. Hermann Thorisson, *Transforming random elements and shifting random fields*, Annals of Probability **24** (1996), no.4, 2057–2064. DOI 10.1214/aop/1041903217 (Crossref confirmed title, author, volume, date and DOI). The theorem is reproduced as Theorem 5.9 on PDF p.19 in the already downloaded Pitman–Tang paper:

> Theorem 5.9. [83] Let (Z_t; t ∈ R) and (Z'_t; t ∈ R) be two path-measurable processes with a state space (E, E). Then there exists a random time T-hat ∈ R such that theta_{T-hat} Z has the same distribution as Z' if and only if the distributions of Z and Z' agree on the invariant sigma-field I.

Subscripts, prime, theta, hat and sigma-field symbols are transcribed from PDF typography. This is an abstract shift-coupling theorem. It does not prove that the exact P0030 objects agree on the invariant sigma-field; establishing that agreement is the remaining gap. It is therefore a neighbouring-area tool, not SOLVED_IN_LITERATURE for Problems 7.1–7.3. For centered Brownian paths the recentering action can be represented by the trajectory of centered-window states; this attempt's integer filling proof directly uses the recentering action and avoids silently identifying it with raw spatially uncentered path translation.

Second-attempt searches, all by Python urllib from the shell:

- Date 2026-10-12; service/query `crossref_kakutani`; status `200`; request https://api.crossref.org/works?query.title=On%20equivalence%20of%20infinite%20product%20measures&rows=3 ; raw response second_search_crossref_kakutani.txt.

- Date 2026-10-12; service/query `crossref_thorisson`; status `200`; request https://api.crossref.org/works?query.title=Transforming%20random%20elements%20and%20shifting%20random%20fields&rows=3 ; raw response second_search_crossref_thorisson.txt.

- Date 2026-10-12; service/query `arxiv_hellinger_fbm`; status `200`; request https://export.arxiv.org/api/query?search_query=all%3A%22forward%20Brownian%22%20AND%20%28all%3AKakutani%20OR%20all%3AHellinger%20OR%20all%3A%22absolute%20continuity%22%29&max_results=20 ; raw response second_search_arxiv_hellinger_fbm.txt.

The combined arXiv forward-Brownian/Kakutani/Hellinger/absolute-continuity query returned no entries. Crossref searches found the two classical references above, rather than a new paper resolving the source questions. This second attempt establishes additional special cases by combining known tools and a fully checked filling argument; no novelty or full literature-solution claim is made.

Reduction M applies the cited invariant-sigma-field theorem to the continuous centered-window-state process, with a full proof of the recentering/ordinary-shift correspondence in ATTEMPT.md. The new finite-shift results are conditional special cases obtained from classical tools; none is recorded as a published solution to Problems 7.1–7.3.
