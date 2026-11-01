
- 2026-10-11 | openalex_scaling | https://api.openalex.org/works?search=condensation%20trees%20scaling%20limit&per-page=30 | openalex_scaling: ERROR HTTP Error 429: Too Many Requests

- 2026-10-11 | openalex_source | https://api.openalex.org/works/https://doi.org/10.1214/11-PS188 | openalex_source: ERROR HTTP Error 429: Too Many Requests

- 2026-10-11 | github | https://api.github.com/search/repositories?q=condensation%20trees%20scaling | github: OK 55 bytes

- 2026-10-11 | semantic | https://api.semanticscholar.org/graph/v1/paper/search?query=condensation%20trees%20scaling%20limit&limit=20&fields=title,authors,year,externalIds,url,abstract | semantic: ERROR HTTP Error 429: 

- 2026-10-11 | janson_source | https://arxiv.org/pdf/1112.0510 | janson_source: OK 1458367 bytes

- 2026-10-11 | crossref | https://api.crossref.org/works?query=condensation%20Galton%20Watson%20scaling%20limits&rows=20 | crossref: OK 184888 bytes

- 2026-10-11 | arxiv_condensation | https://export.arxiv.org/api/query?search_query=all%3Acondensation%20AND%20%28all%3Atrees%20OR%20all%3AGalton%29&max_results=30 | arxiv_condensation: OK 55931 bytes

- 2026-10-11 | kortchemski | https://arxiv.org/pdf/1205.3145 | kortchemski: OK 4193889 bytes

- 2026-10-11 | crossref_kort | https://api.crossref.org/works?query.title=Limit%20theorems%20for%20conditioned%20non-generic%20Galton-Watson%20trees&rows=3 | crossref_kort: OK 14674 bytes

- 2026-10-11 | openalex_retry | https://api.openalex.org/works?search=condensation%20Galton%20Watson&per_page=20 | openalex_retry: ERROR HTTP Error 429: Too Many Requests

- 2026-10-11 | semantic_source | https://api.semanticscholar.org/graph/v1/paper/ARXIV:1112.0510?fields=title,citations.title,citations.year,citations.externalIds | semantic_source: ERROR HTTP Error 429: 

- 2026-10-11 | arxiv_specific | https://export.arxiv.org/api/query?search_query=all%3Acondensation%20AND%20all%3Ascaling&max_results=50 | arxiv_specific: OK 102868 bytes

- 2026-10-11 | arxiv_dendron | https://export.arxiv.org/api/query?search_query=all%3Adendron%20OR%20%28au%3AJanson%20AND%20all%3Alimits%20AND%20all%3Atrees%29&max_results=30 | arxiv_dendron: OK 55973 bytes

- 2026-10-11 | crossref_tree_limits | https://api.crossref.org/works?query=Janson%20tree%20limits%20condensation%20dendrons&rows=15 | crossref_tree_limits: OK 111585 bytes

- 2026-10-11 | openalex_citing_source | https://api.openalex.org/works?filter=cites:https://doi.org/10.1214/11-PS188&per-page=50 | openalex_citing_source: ERROR HTTP Error 429: Too Many Requests

- 2026-10-11 | janson_tree_limits | https://arxiv.org/pdf/2005.13832 | janson_tree_limits: OK 570622 bytes

- 2026-10-11 | crossref_limits_exact | https://api.crossref.org/works?query.title=Tree%20limits%20and%20limits%20of%20random%20trees&rows=3 | crossref_limits_exact: OK 19917 bytes

- 2026-10-11 | github_tree_limits | https://api.github.com/search/repositories?q=dendron%20tree%20limits | github_tree_limits: OK 55 bytes

- 2026-10-11 | arxiv_tree_scaling_recent | https://export.arxiv.org/api/query?search_query=all%3Acondensation%20AND%20%28all%3Atrees%20OR%20all%3AGalton%29%20AND%20%28all%3Ascaling%20OR%20all%3Adendron%20OR%20all%3AGromov%29&sortBy=submittedDate&sortOrder=descending&max_results=30 | arxiv_tree_scaling_recent: OK 71381 bytes

- 2026-10-11 | crossref_irregular | https://api.crossref.org/works?query=condensation%20tree%20limits%20incomplete%20condensation%20Janson&rows=20 | crossref_irregular: OK 328019 bytes

- 2026-10-11 | arxiv_probability_recent | https://export.arxiv.org/api/query?search_query=cat%3Amath.PR%20AND%20all%3Acondensation%20AND%20all%3Atrees&sortBy=submittedDate&sortOrder=descending&max_results=30 | arxiv_probability_recent: OK 53630 bytes

- 2026-10-11 | cauchy2025 | https://arxiv.org/pdf/2503.07530 | cauchy2025: OK 986122 bytes

- 2026-10-11 | crossref_cauchy2025 | https://api.crossref.org/works?query.title=Condensation%20in%20subcritical%20Cauchy%20Bienayme%20trees&rows=3 | crossref_cauchy2025: OK 28843 bytes

# Verified relevant references and reading notes (2026-10-11)

- Svante Janson, *Simply generated trees, conditioned Galton–Watson trees, random allocations and condensation*, Probability Surveys **9** (2012), 103–252. DOI [10.1214/11-PS188](https://doi.org/10.1214/11-PS188); [arXiv:1112.0510](https://arxiv.org/abs/1112.0510). Full PDF fetched and text extracted. Problem 20.11, Section 20.4, printed p. 136, exact wording saved in source_statement.txt. Definitions and weight assumptions verified on pp. 7–8.
- Igor Kortchemski, *Limit theorems for conditioned non-generic Galton–Watson trees*, Annales de l’Institut Henri Poincaré, Probabilités et Statistiques **51**(2) (2015), 489–511. DOI [10.1214/13-AIHP580](https://doi.org/10.1214/13-AIHP580); [arXiv:1205.3145v4](https://arxiv.org/abs/1205.3145v4), 14 September 2013. Full PDF checked. Assumption (Hθ), θ>1; Theorems 4, 5, 6, Corollary 2.7, equation (19). Theorem 5 explicitly **partially** answers Janson Problem 20.11: logarithmic GH rescaling is not tight.
- Svante Janson, *Tree limits and limits of random trees*, Combinatorics, Probability and Computing **30**(6) (2021), 849–893. DOI [10.1017/S0963548321000055](https://doi.org/10.1017/S0963548321000055); [arXiv:2005.13832](https://arxiv.org/abs/2005.13832). Full PDF checked. Theorem 10.1: geometric-arm long-dendron convergence under complete condensation. Theorem 11.1: unit-arm sampling limit in the zero-radius complete-condensation case. Remarks 10.8 and 11.3 explicitly leave incomplete/multiple condensation cases open. This is the main positive update absent from the intake summary.
- Igor Kortchemski and Leonard Vetter, *Condensation in subcritical Cauchy Bienaymé trees*, Electronic Communications in Probability **30** (2025), 1–13, DOI [10.1214/25-ECP726](https://doi.org/10.1214/25-ECP726); [arXiv:2503.07530v2](https://arxiv.org/abs/2503.07530v2), 8 October 2025. Full PDF checked; journal metadata verified by Crossref. Theorem 1.1 extends complete condensation and logarithmic height to locally regularly varying tails p_n∼L(n)/n²; centered-height tightness requires a finite offspring log-moment. Together with Janson 2021 this gives the geometric-arm sampling limit for that boundary class. Does not remove local regularity or address all weight sequences.
- Romain Abraham and Jean-François Delmas, *Local limits of conditioned Galton–Watson trees: the condensation case*, Electronic Journal of Probability **19** (2014), DOI [10.1214/EJP.v19-3164](https://doi.org/10.1214/EJP.v19-3164), [arXiv:1311.6683](https://arxiv.org/abs/1311.6683). Search metadata/abstract inspected; local limits, not a general global scaling answer.
- Gábor Elek and Gábor Tardos, *Convergence and limits of finite trees*, [arXiv:2001.00905v2](https://arxiv.org/abs/2001.00905v2). Abstract inspected: sampling-distance limits represented by dendrons, the framework used in Janson 2021. No general condensation result inferred from the abstract.
- Romain Abraham and Jean-François Delmas, *Coupling some conditioned Lévy trees with the Kesten tree*, [arXiv:2607.01877v1](https://arxiv.org/abs/2607.01877v1). Search abstract inspected: subcritical condensation explicitly remains partly outside that paper's framework; concerns already-continuous Lévy trees, not a full answer for all simply generated weights.
- Vanessa Dan, *Limits of biconditioned Bienaymé-Galton-Watson trees*, [arXiv:2507.22135v2](https://arxiv.org/abs/2507.22135v2). Abstract inspected: conditioning on total size plus leaves/internal nodes; distinct from the size-only question here.

## Read-only internal searches (2026-10-11)

- brain.py recall: `subcritical conditioned Galton Watson condensation scaling limit mistakes`. Cards about lacunary tails and earlier Janson results returned; treated as hints only.
- math_recall.py: `Kortchemski condensation trees scaling limit`. Returned mostly irrelevant cards; none used as theorem evidence.
- Intake and prior pool text search for `I0022|20\.11`; first intake glob failed in PowerShell, then resolved directory and searched again. No matching output was obtained from these local searches.
- Read-only git tree search for `I0022|20[_ .-]?11|condensation.*scal|janson`, then `git show origin/master:probability_1000_attempts_I_20260914/Probability_F0064b_Janson_problems_20_3_20_4_20_11_2026-09-14.md`. Earlier memo leaves Problem 20.11 unresolved. Its unproved universal statements about lacunary laws were not adopted.

## Search coverage and limitations

The dated URL log below/above records each executed network search, including failures, and the raw service responses are retained. All five requested services were attempted. Crossref and arXiv succeeded; GitHub returned zero repositories for both queries. OpenAlex search, source lookup, retry, and citing-source filter returned HTTP 429; the citation-filter request could not be validated because the source identifier lookup was also blocked. Semantic Scholar search and citation lookup also returned HTTP 429. No successful citation sweep of all citing papers is claimed. Broad arXiv full-text queries produced many irrelevant results; adding `cat:math.PR` gave a focused recent list, including the 2025 Cauchy update. This is a bounded status search, not proof of absence of further solutions.

## Second-attempt read-only searches (2026-10-11)

- Read ATTEMPT.md and STATUS.md in full before choosing approaches.
- math_recall.py: `Janson incomplete condensation large degree skeleton dendron tree limits Example 19.37`; received the neighbouring Janson 18.41/18.42 sparse cubic-spike hint, card claim_41f12ef0ef0f42ef93f8e1d0c4f3639a, and unrelated cards. Then walked that exact card with `--id`; it supplies no tree-sampling theorem.
- brain.py recall: `incomplete condensation sampling limit dendron mistakes`; found the entropy-omission warning in earlier zero-radius work, and no dendron-specific memory. The new proof explicitly retains full tree entropy.
- Searched the locally downloaded arXiv:1112.0510v1 text and PDF for Example 19.18, 19.37, 19.39 while following the journal-numbered leads. Those exact locators were not found in the v1 source; no assertion based on inspecting those examples is made. The construction and proof are self-contained and use only the source's weight definitions and ν=0 convention, verified in the first pass.
- No new web search was required for the selected elementary construction. Existing Janson (2021) is used only as the terminology/framework for the explicitly proved subsequential long-dendron objects, not as an input to Theorems C/D.
