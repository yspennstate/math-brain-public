# Literature search

Search date: 2026-10-11. Raw responses are retained in this folder.

## Verified references and outcome

1. David Aldous (2013), *Interacting particle systems as stochastic social dynamics*, Bernoulli 19(4), 1122–1149. DOI https://doi.org/10.3150/12-BEJSP04; https://arxiv.org/abs/1309.6766. Primary PDF: aldous_pdf.pdf; text: aldous_source.txt. Section 5.5 starts PDF p.15 and Open Problem 2 is p.16. Its [42] is Oliveira below. Exact statement and scope in ATTEMPT.md.
2. Roberto Imbuzeiro Oliveira (2013), *Mean field conditions for coalescing random walks*, Annals of Probability 41(5), 3420–3461. DOI https://doi.org/10.1214/12-AOP813; https://arxiv.org/abs/1109.5684. PDF: oliveira_pdf.pdf; clean extraction: oliveira_full.txt. Theorem 1.1 gives full-coalescence Kingman law in L1 Wasserstein and expected ratio 2 when a reversible transitive chain has t_mix/tau_meet->0. Theorem 1.2 gives general-chain conditions in terms of alpha=(1+q_max t_mix)pi_max. This was already known to the source, not a subsequent solution.
3. Jonathan Hermon (2022), *Some inequalities for reversible Markov chains and branching random walks via spectral optimization*, Annales de l'Institut Henri Poincare, Probabilites et Statistiques 58(3), 1650–1668. DOI https://doi.org/10.1214/21-AIHP1208; https://arxiv.org/abs/1908.08525 (v4, 2 March 2022). PDF: hermon_pdf.pdf; clean extraction: hermon_full.txt. Theorem 1 bounds uniform mixing by relaxation time and stationary-to-target hitting times. Combined with Oliveira, this resolves the transitive spectral sufficient criterion. ATTEMPT.md derives the precise implication t_rel=o(tau_meet) => E T_coal~2 tau_meet with Aldous's normalization. The introduction explicitly discusses coalescence and Aldous–Fill Open Problem 14.12. Its suggested broader nontransitive extension is not a proved result.
4. Jonathan Hermon, Shuangping Li, Dong Yao, Lingfu Zhang (2022), *Mean field behavior during the Big Bang regime for coalescing random walks*, Annals of Probability 50(5), 1813–1884. DOI https://doi.org/10.1214/22-AOP1571; https://arxiv.org/abs/2105.11585. PDF: bigbang_pdf.pdf; clean extraction: bigbang_full.txt. Abstract checked: early density decay under transience-like conditions, including configuration-model and transitive applications. Not used as an unrestricted resolution of (5.2).
5. J. Beltran, E. Chavez, C. Landim, *From coalescing random walks on a torus to Kingman's coalescent*, arXiv:1803.03199 (2018). API abstract checked: process-level convergence of particle counts on tori in d>=2; a special-family refinement.
6. Louigi Addario-Berry, Caelan Atamanchuk, Maxwell Kaye, *Kingman's coalescent on a random graph*, arXiv:2509.16181 (2025). Abstract checked and excluded: rooted trees merge only along root edges and can stop at a forest; this is not coalescing moving random walks.
7. *Meeting, coalescence and consensus time on random directed graphs*, arXiv:2308.01832. API abstract checked: directed configuration-model results outside the symmetric standardized setting; not needed for the verdict.

## Read-only prior-work searches

- 2026-10-11: brain.py recall "coalescing random walks Kingman meeting time" and "coalescing walks mistakes"; math_recall.py "Oliveira mean field coalescing random walks". Cycle and complete-graph hints were returned; none treated as a verdict.
- 2026-10-11: rg for F0127 in probability_1000_intake_* ledgers and codex_pool_2026_10_10. Initial literal wildcard directory failed in PowerShell; corrected enumeration followed by rg succeeded. Found F0127-A001, a Stage 1 sketch leaving Stage 2 unresolved, plus leads to Oliveira and Big Bang. Its unrestricted Stage 1 claim was not adopted.
- 2026-10-11: read-only git ls-tree origin/master in ~/math-open-problems, filtered for F0127/coalesc/kingman. No named F0127 proof found. No working-tree modifications.

## Search coverage and limitations

All HTTP queries, dates, statuses and raw-response names are listed below. OpenAlex consistently returned HTTP 429 for source DOI lookup, title search, Hermon lookup and attempted source citations. The citing-source filter used the source DOI because ID lookup was blocked; no citation graph was retrieved and filter validity could not be established. Semantic Scholar search and source/Hermon citation requests also returned HTTP 429. These are attempted searches, not successful coverage.

arXiv API, primary PDFs, Crossref and GitHub succeeded. GitHub exact query returned zero repositories; the broader query returned lilywreeves/dlas-w-coalescence, a ring simulation, not a proof. The post-2013 arXiv Boolean query returned 40 entries, many generally about coalescents; relevant entries were inspected as stated above. The literature verdict rests on positive primary theorems, not absence of search hits or an assertion of exhaustive coverage.

- 2026-10-11 | aldous_pdf | `https://arxiv.org/pdf/1309.6766` | aldous_pdf: HTTP 200; 359787 bytes

- 2026-10-11 | arxiv_api | `http://export.arxiv.org/api/query?search_query=all%3A%22coalescing%20random%20walks%22%20AND%20all%3A%22mean%20field%22&max_results=15` | arxiv_api: HTTP 200; 17043 bytes

- 2026-10-11 | openalex_search | `https://api.openalex.org/works?search=mean%20field%20conditions%20coalescing%20random%20walks&per-page=15` | openalex_search: HTTP 429; 610 bytes

- 2026-10-11 | openalex_source | `https://api.openalex.org/works/https://doi.org/10.3150/12-BEJSP04` | openalex_source: HTTP 429; 610 bytes

- 2026-10-11 | crossref | `https://api.crossref.org/works?query=mean%20field%20conditions%20coalescing%20random%20walks&rows=10` | crossref: HTTP 200; 54617 bytes

- 2026-10-11 | semantic | `https://api.semanticscholar.org/graph/v1/paper/search?query=mean%20field%20coalescing%20random%20walks&limit=10&fields=title,authors,year,externalIds,url,abstract` | semantic: HTTP 429; 174 bytes

- 2026-10-11 | github | `https://api.github.com/search/repositories?q=coalescing%20random%20walks%20Kingman` | github: HTTP 200; 55 bytes

- 2026-10-11 | oliveira_pdf | `https://arxiv.org/pdf/1109.5684` | HTTP 200; 399965 bytes

- 2026-10-11 | hermon_pdf | `https://arxiv.org/pdf/1908.08525` | HTTP 200; 373314 bytes

- 2026-10-11 | bigbang_pdf | `https://arxiv.org/pdf/2105.11585` | HTTP 200; 807945 bytes

- 2026-10-11 | crossref_hermon | `https://api.crossref.org/works?query.title=Some%20inequalities%20for%20reversible%20Markov%20chains%20and%20branching%20random%20walks%20via%20spectral%20optimization&rows=3` | HTTP 200; 13433 bytes

- 2026-10-11 | openalex_retry | `https://api.openalex.org/works?search=Interacting%20particle%20systems%20as%20stochastic%20social%20dynamics&per_page=3` | HTTP 429; 610 bytes

- 2026-10-11 | semantic_source | `https://api.semanticscholar.org/graph/v1/paper/ARXIV:1309.6766?fields=title,citations.title,citations.year,citations.externalIds` | HTTP 429; 174 bytes

- 2026-10-11 | arxiv_later | `http://export.arxiv.org/api/query?search_query=all%3A%22coalescing%22%20AND%20%28all%3A%22Kingman%22%20OR%20all%3A%22mean%20field%22%29%20AND%20submittedDate%3A%5B201310010000%20TO%20202610112359%5D&max_results=40` | HTTP 200; 77739 bytes

- 2026-10-11 | openalex_citing_source | `https://api.openalex.org/works?filter=cites:https%3A%2F%2Fdoi.org%2F10.3150%2F12-BEJSP04&per-page=50` | HTTP 429; 610 bytes

- 2026-10-11 | openalex_hermon | `https://api.openalex.org/works/https://doi.org/10.1214/21-AIHP1208` | HTTP 429; 610 bytes

- 2026-10-11 | semantic_hermon | `https://api.semanticscholar.org/graph/v1/paper/ARXIV:1908.08525?fields=title,year,authors,externalIds,citations.title,citations.year` | HTTP 429; 174 bytes

- 2026-10-11 | github_broad | `https://api.github.com/search/repositories?q=coalescing%20random%20walks` | HTTP 200; 5643 bytes

- 2026-10-11 | crossref_exact_oliveira | `https://api.crossref.org/works/10.1214/12-AOP813` | HTTP 200; 7436 bytes

- 2026-10-11 | crossref_exact_bigbang | `https://api.crossref.org/works/10.1214/22-AOP1571` | HTTP 200; 14045 bytes
