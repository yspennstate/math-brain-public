# Literature and status search

Date: 2026-10-11. No exact solution has yet been verified.

Source page fetched successfully: https://www.stat.berkeley.edu/~aldous/Research/OP/left_Hamm.html (saved source.html).

- source1993: https://www.stat.berkeley.edu/~aldous/Research/OP/patience.pdf
  Result: OK 379915

- source1999: https://www.stat.berkeley.edu/~aldous/Papers/me86.pdf
  Result: OK 321073

- source1995: https://www.stat.berkeley.edu/~aldous/Papers/me71.pdf
  Result: OK 251104

- arxiv: http://export.arxiv.org/api/query?search_query=all%3AHammersley%20AND%20%28all%3Astationary%20OR%20all%3Adrift%29&max_results=30
  Result: OK 46790

- openalex: https://api.openalex.org/works?search=Hammersley%20drift%20jump%20stationary&per-page=20
  Result: HTTP Error 429: Too Many Requests

- crossref: https://api.crossref.org/works?query=Hammersley%20drift%20jump%20stationary&rows=20
  Result: OK 178862

- semantic: https://api.semanticscholar.org/graph/v1/paper/search?query=Hammersley%20drift%20jump&limit=20&fields=title,authors,year,url,externalIds
  Result: HTTP Error 429: 

- github: https://api.github.com/search/repositories?q=Hammersley%20stationary
  Result: OK 55

- 2026-10-11 openalex_retry: https://api.openalex.org/works?search=Longest%20increasing%20subsequences%20from%20patience%20sorting%20to%20the%20Baik%20Deift%20Johansson%20theorem&per-page=5
  Result: HTTP Error 429: Too Many Requests

- 2026-10-11 openalex_drift: https://api.openalex.org/works?search=Hammersley%20drift&per-page=10
  Result: HTTP Error 429: Too Many Requests

- 2026-10-11 semantic_retry: https://api.semanticscholar.org/graph/v1/paper/search?query=Hammersley%20stationary&limit=10&fields=title,authors,year,url,externalIds
  Result: HTTP Error 429: 

- 2026-10-11 github_drift: https://api.github.com/search/repositories?q=%22drift-jump%22%20Hammersley
  Result: OK 55

- 2026-10-11 arxiv_focused: https://export.arxiv.org/api/query?search_query=all%3A%22Hammersley%22%20AND%20%28all%3A%22drift%22%20OR%20all%3A%22Plancherel%22%20OR%20all%3A%22leftmost%22%29&max_results=30
  Result: OK 14514

- 2026-10-11 crossref_focused: https://api.crossref.org/works?query.title=Hammersley%20stationary&rows=20
  Result: OK 45159

- 2026-10-11 openalex_citations: https://api.openalex.org/works?filter=cites:doi:10.1090/S0273-0979-99-00796-X&per-page=20
  Result: HTTP Error 429: Too Many Requests
orting%22%20AND%20all%3A%22stationary%22%29&max_results=30
  Result: OK 6352

- 2026-10-11 semantic_citations: https://api.semanticscholar.org/graph/v1/paper/DOI:10.1090/S0273-0979-99-00796-X/citations?limit=100&fields=title,year,authors,url
  Result: OK 40301

- 2026-10-11 crossref_1999: https://api.crossref.org/works?query.title=Longest%20increasing%20subsequences%20from%20patience%20sorting%20to%20the%20Baik%20Deift%20Johansson%20theorem&rows=3
  Result: OK 37959

- 2026-10-11 later2020: https://arxiv.org/pdf/2005.13824
  Result: OK 438556

- 2026-10-11 later2025: https://arxiv.org/pdf/2506.19008
  Result: OK 580280

- 2026-10-11 arxiv_variations: https://export.arxiv.org/api/query?search_query=ti%3A%22Variations%20on%20Hammersley%22&max_results=5
  Result: OK 2588

- 2026-10-11 corwin2018: https://www.ams.org/journals/bull/2018-55-03/S0273-0979-2018-01623-6/S0273-0979-2018-01623-6.pdf
  Result: OK 211450

- 2026-10-11 erickson_metadata: https://api.semanticscholar.org/graph/v1/paper/53dba18293ea5da10145d1932fe93b98ae29eb33?fields=title,authors,year,abstract,externalIds,openAccessPdf
  Result: HTTP Error 429: 

- 2026-10-11 variations_metadata: https://api.semanticscholar.org/graph/v1/paper/c84debdbf417d764a819cb4579a17bb1f99b23d7?fields=title,authors,year,abstract,externalIds,openAccessPdf
  Result: HTTP Error 429: 

- 2026-10-11 openalex_source_lookup: https://api.openalex.org/works/https://doi.org/10.1090/S0273-0979-99-00796-X
  Result: HTTP Error 429: Too Many Requests

- 2026-10-11 arxiv_erickson: https://export.arxiv.org/api/query?search_query=ti%3A%22Explicit%20marginal%20distributions%22%20AND%20all%3A%22Robinson%22&max_results=5
  Result: OK 2544

- 2026-10-11 variations2021: https://arxiv.org/pdf/2106.11186
  Result: OK 585203


## Source verification and bounded-search conclusion

The author-maintained page was fetched on 2026-10-11 and still contains the problem. Exact wording:

> Give some (fairly explicit) description of the stationary distribution.

Hypotheses checked directly: k ordered positive particles for every k>=1; deterministic drift dX_i/dt=X_i; Poisson intensity dx dt; move the nearest particle to the right of the event to that event; ignore an event with no such particle. Consistency in k and uniqueness of the stationary distribution are stated on the page. The word "speed" refers to the coordinate x, not constant-speed drift.

No paper was verified to state and prove the exact full stationary-law question. Therefore there is no SOLVED_IN_LITERATURE verdict or purported exact-solution theorem quotation. The results below are established input, leads, or different-model results. API failures and a bounded search prevent certifying global openness.

The arXiv initial query returned 22 records; focused Hammersley/drift/Plancherel/leftmost query returned 6 records. The phrase query returned unrelated uses of drift/jump, illustrating that it is weak negative evidence. GitHub searches returned zero repositories, not mathematical nonexistence evidence. Crossref broad drift/jump search was mainly irrelevant; the exact 1999-title query successfully identified the source and Corwin's commentary.

Semantic Scholar's direct citation endpoint for the verified 1999 DOI succeeded despite its general search endpoint returning 429. The first citation page contains 100 records, ordered from 2026 down to 2017, including both 2018 Corwin commentary entries, 2021 Hammersley variations, and 2026 shape-marginal formulas. Its pagination advertises more older records; those older pages were not fetched. The saved JSON is semantic_citations.raw. The source's 2018 web problem itself was not identified as an indexed paper. OpenAlex lookup of the 1999 DOI and searches repeatedly returned 429, so no OpenAlex citing-work list was obtained. The earlier cites:doi filter request was not a valid substitute for resolving an OpenAlex work ID; the properly formed DOI lookup was also blocked. No conclusions are drawn from this failure.

## Primary and related references

1. David Aldous. *A one-dimensional drift-jump particle process*. Author-maintained problem page, posted February 2018. https://www.stat.berkeley.edu/~aldous/Research/OP/left_Hamm.html . Saved source.html; exact source of the statement and hypotheses.

2. David Aldous and Persi Diaconis. *Patience Sorting, Longest Increasing Subsequences and a Continuous Space Analog of the Simple Asymmetric Exclusion Process*. Unfinished unpublished notes dated July 8, 1993. https://www.stat.berkeley.edu/~aldous/Research/OP/patience.pdf . Saved source1993.pdf and readable source1993.txt. Section 4.1, pp.36-38, gives the model and equations (41)-(42); Section 4.2, pp.39-42, gives the first-two law. The p.39 non-Markov remark is the structural target of ATTEMPT.md. The equation (43) drift-divergence coefficient is suspect (earlier internal work records -p versus -k p); none of the proof here uses it.

3. David Aldous and Persi Diaconis. "Longest increasing subsequences: from patience sorting to the Baik-Deift-Johansson theorem." *Bulletin of the American Mathematical Society* **36** (1999), 413-432. DOI: 10.1090/S0273-0979-99-00796-X. https://www.stat.berkeley.edu/~aldous/Papers/me86.pdf . Source Section 5.2 is explicitly cited on Aldous's page; saved source1999.pdf. Automatic text extraction has an unusable font mapping for this PDF, so no theorem is purportedly quoted from that extraction. Source hypotheses instead matched to the readable 1993 notes and live page. Crossref verifies the bibliographic reference.

4. David Aldous and Persi Diaconis. "Hammersley's interacting particle process and longest increasing subsequences." *Probability Theory and Related Fields* **103** (1995), 199-213. Linked by the source: https://www.stat.berkeley.edu/~aldous/Papers/me71.pdf . Saved source1995.pdf; automatic text extraction also has an unusable font mapping. Classical Hammersley stationary measures are related but do not solve the linear-drift finite-leftmost model by themselves.

5. Ivan Corwin. "Commentary on 'Longest increasing subsequences: from patience sorting to the Baik-Deift-Johansson theorem' by David Aldous and Persi Diaconis." *Bulletin of the American Mathematical Society* **55** (2018), 363-374. DOI: 10.1090/bull/1623. PDF https://www.ams.org/journals/bull/2018-55-03/S0273-0979-2018-01623-6/S0273-0979-2018-01623-6.pdf . Saved corwin2018.pdf/.txt. Broader LIS/KPZ commentary; inspected for Hammersley, stationary, drift, and leftmost references; no exact drift-jump stationary-law theorem verified.

6. Miko?aj Marciniak, ?ukasz Ma?lanka and Piotr ?niady. *Poisson limit theorems for the Robinson-Schensted correspondence and for the multi-line Hammersley process*. arXiv:2005.13824v3, dated 14 December 2022 (first posted 28 May 2020). https://arxiv.org/abs/2005.13824 . Saved later2020.pdf/.txt. Theorem 1.1, PDF p.4, concerns asymptotic bottom-row increments under n+floor(t sqrt(n)) scaling, converging to independent Poisson processes. Corollary 1.4 concerns a bulk-scaled multi-line process. This is a different scaling object, not a theorem giving the exact finite-leftmost linear-drift joint law.

7. Leandro P. R. Pimentel and Roberto Viveros. *Sprinkled Decoupling for Hammersley's Process*. arXiv:2506.19008v1, posted 23 June 2025; manuscript dated June 25, 2025. https://arxiv.org/abs/2506.19008 . Saved later2025.pdf/.txt. PDF p.2 defines a translation-invariant process on R initially at homogeneous Poisson intensity lambda, jumping left without linear drift. Its decoupling theorem does not answer this different drift-jump problem.

8. Arda Atalik, H. S. Melihcan Erol, G?khan Y?ld?r?m and Mustafa Yilmaz. "Variations on Hammersley's interacting particle process." *Discrete Mathematics Letters* **7** (2021), 34-39. DOI: 10.47443/dml.2021.0049. arXiv:2106.11186v1. https://arxiv.org/abs/2106.11186 . Saved variations2021.pdf/.txt. Pattern-avoidance variations and planar analogues; no drift/stationary/leftmost term found in extracted text. Not the requested exact stationary-law theorem.

9. W. Q. Erickson. *Explicit marginal distributions for permutations with prescribed Robinson-Schensted shape*. arXiv:2605.00378v2, 2026. https://arxiv.org/abs/2605.00378 . Citation metadata and arXiv abstract inspected; saved arxiv_erickson.raw. Computes P^lambda_ij=P(sigma(i)=j) for fixed prescribed permutation shapes (hooks, two rows, rectangles). Different object and only selected shapes; does not supply the unconditioned all-k stationary particle law. Full paper not fetched; treated only as a lead.

10. Eric Cator and Piet Groeneboom. *Hammersley's process with sources and sinks*, arXiv:math/0506590; Pablo A. Ferrari and James B. Martin, *Multiclass Hammersley-Aldous-Diaconis process and multiclass-customer queues*, arXiv:0707.4202. Retrieved metadata only. Classical sources/sinks and multiclass stationary mechanisms are related machinery, not verified answers to this process.

## Read-only research-brain and earlier-work audit

Read-only recalls were run on "Hammersley stationary patience sorting first row", "Hammersley drift jump mistakes", and "Hammersley stationary particles". Math recall returned the earlier conditional tableau mixture and cautioned that it repackages a known representation. Memory recalls did not contain an on-target Hammersley result. These are hints, not proof inputs.

The intake-ledger directory glob was expanded with PowerShell and searched for P0220; it yielded no records in the directories found. The initial rg call with a literal Windows wildcard failed and was corrected. The codex_pool_2026_10_10 tree gave team_O/w330/reports/P0220_certified_series.md, read in full. It records exact truncation bounds and the known first-two consequence, with no full-solution claim.

The published-record checkout was accessed only through git ls-tree and git show origin/master:<path>. Relevant earlier records read:

- operations/claims/P0220.md;
- research7_2026-09-17/R7-04/handoffs/2026-09-19/2026-09-19T074800Z__P0220_six_run_retirement_handoff.md;
- research7_2026-09-17/R7-04/artifacts/2026-09-19/2026-09-19T005400Z__P0220_plancherel_hitting_and_bessel_marginals.md;
- research7_2026-09-17/R7-04/artifacts/2026-09-19/2026-09-19T033600Z__P0220_constructive_truncation_and_k3_formula.md;
- research7_2026-09-17/R7-04/artifacts/2026-09-19/2026-09-19T064100Z__P0220_schur_reconciliation_and_laplace_identities.md.

They already propose all-k Plancherel hitting, scalar Bessel determinants, positive partition sums, and extended Schur/Fredholm formulas, and explicitly leave source closure/novelty and independent audits unresolved. They also show a non-Markov certificate for the discrete hitting labels. They do not constitute a verified publication answering the source question, nor does their discrete certificate alone settle continuous-coordinate Markov behavior. The present attempt proves the latter directly using the source's established representation. No earlier ownership/retirement instruction is applied to this separately user-authorized folder; no shared record or repository was changed.

## Literature verdict

NO VERIFIED EXACT SOLUTION IN PRINT FOUND. This is a bounded-search finding, with the access limitations above. The positive result of this attempt is the fully written continuous non-Markov obstruction in ATTEMPT.md; it is a structural partial result, not a newly solved general joint-law problem.

- Continuation 2026-10-11 borodin_rains_api: https://export.arxiv.org/api/query?search_query=ti:%22Eynard%22+AND+au:%22Rains%22&max_results=5
  Result: HTTP Error 429: Unknown Error

- Continuation 2026-10-11 new_source_check: https://www.stat.berkeley.edu/~aldous/Research/OP/left_Hamm.html
  Result: OK 3171

- Continuation 2026-10-11 borodin_rains: https://arxiv.org/pdf/math-ph/0409059
  Result: OK 240836

- Continuation 2026-10-11 finite_determinant_search: https://api.crossref.org/works?query=Plancherel%20growth%20hitting%20times%20joint%20finite%20determinant%20Hammersley&rows=10
  Result: OK 37344


## Continuation: finite occupied-site determinant approach

2026-10-11. Gap-specific brain queries:

- "Okounkov Reshetikhin Schur process multi time gap Fredholm kernel Plancherel";
- "Eynard Mehta finite particle occupied sites Schur complement Borodin Rains";
- read-only walk of card source_817e43caeb37b2d8beb4461eb62faff98a4cd3c81ce7236806860f84020a0e9d.

The named-reference lead was verified by fetching the actual paper:

Alexei Borodin and Eric M. Rains, "Eynard-Mehta theorem, Schur process, and their Pfaffian analogs," Journal of Statistical Physics 121 (2005), 291-317. DOI 10.1007/s10955-005-7583-z. arXiv:math-ph/0409059v2, dated February 12, 2005. Saved borodin_rains.pdf and borodin_rains.txt. Theorem 1.4 (Eynard-Mehta), PDF p.4, gives the determinantal kernel for a finite product-of-determinants point ensemble; Lemma 1.3 on the same page gives its normalization by Cauchy-Binet. This is neighbouring-area machinery, not an in-print statement about the Aldous drift-jump stationary particles. It therefore does not qualify as SOLVED_IN_LITERATURE.

The continuation independently proves the needed finite determinant algebra directly rather than relying on a potentially mismatched infinite Schur-process convention. FINITE_DETERMINANT.md derives the new source-specific matrix from occupied checkpoint sites after transposition. This is distinct from merely repeating the historical Gamma/patience representation or an infinite tableau mixture. The final matrix dimension is at most k(k-1) for the first k particles.

The new bounded Crossref search for "Plancherel growth hitting times joint finite determinant Hammersley" returned generic hitting-time papers, not a verified exact solution. The author-maintained page was fetched again and remains unchanged. Historical priority of this source-specific finite-matrix composition is unverified. A complete mathematical proof of that composition, if accepted on its merits, is a SOLVED verdict by this task's criterion, not a SOLVED_IN_LITERATURE or verified-novelty verdict.
