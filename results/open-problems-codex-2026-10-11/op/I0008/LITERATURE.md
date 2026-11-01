# Literature log

2026-10-12. Search results and failures will be recorded; absence of a result is not evidence of nonexistence.

- 2026-10-12: openalex, URL/query `https://api.openalex.org/works?search=gradient%20Gibbs%20measures%20minimal%20free%20energy&per-page=20`. openalex: ERROR HTTP Error 429: Too Many Requests

- 2026-10-12: source_abs, URL/query `https://arxiv.org/abs/2609.01499`. source_abs: HTTP 200, 41870 bytes

- 2026-10-12: semantic, URL/query `https://api.semanticscholar.org/graph/v1/paper/search?query=gradient%20Gibbs%20measures%20minimal%20free%20energy&limit=20&fields=title,authors,year,url,externalIds`. semantic: ERROR HTTP Error 429: 

- 2026-10-12: github, URL/query `https://api.github.com/search/repositories?q=gradient%20Gibbs%20measures`. github: HTTP 200, 55 bytes

- 2026-10-12: arxiv, URL/query `http://export.arxiv.org/api/query?search_query=all%3A%22gradient%20Gibbs%22%20AND%20all%3A%22free%20energy%22&max_results=30&sortBy=submittedDate&sortOrder=descending`. arxiv: HTTP 200, 4484 bytes

- 2026-10-12: source_pdf, URL/query `https://arxiv.org/pdf/2609.01499`. source_pdf: HTTP 200, 2345778 bytes

- 2026-10-12: crossref, URL/query `https://api.crossref.org/works?query=gradient%20Gibbs%20measures%20Sheffield%20minimal&rows=20`. crossref: HTTP 200, 66187 bytes

- 2026-10-12: sheffield_pdf, URL/query `https://arxiv.org/pdf/math/0304049`. sheffield_pdf: HTTP 200, 1567529 bytes

- 2026-10-12: openalex_retry: `https://api.openalex.org/works?search=%22gradient%20Gibbs%22&per_page=15`. ERROR HTTP Error 429: Too Many Requests

- 2026-10-12: openalex_source: `https://api.openalex.org/works?search=On%20the%20rigidity%20of%20sloped%20height%20functions&per_page=5`. ERROR HTTP Error 429: Too Many Requests

- 2026-10-12: openalex_citing: `https://api.openalex.org/works?filter=cites:arxiv:2609.01499&per_page=20`. ERROR HTTP Error 429: Too Many Requests

- 2026-10-12: arxiv_recent: `https://export.arxiv.org/api/query?search_query=all%3A%22gradient%20Gibbs%22%20AND%20submittedDate%3A%5B20260901%20TO%2020261012%5D&max_results=50&sortBy=submittedDate&sortOrder=descending`. HTTP 200, 820 bytes

- 2026-10-12: semantic_source: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:2609.01499?fields=title,year,citations.title,citations.year,citations.externalIds`. ERROR HTTP Error 429: 

- 2026-10-12: arxiv_minimal: `https://export.arxiv.org/api/query?search_query=all%3A%22random%20surfaces%22%20AND%20all%3A%22variational%22&max_results=30&sortBy=submittedDate&sortOrder=descending`. HTTP 200, 26573 bytes

- 2026-10-12: github_sheffield: `https://api.github.com/search/repositories?q=Sheffield%20random%20surfaces`. HTTP 200, 55 bytes

- 2026-10-12: crossref_recent: `https://api.crossref.org/works?query=%22gradient%20Gibbs%22%20%22free%20energy%22&filter=from-pub-date:2026-09-01,until-pub-date:2026-10-12&rows=20`. HTTP 200, 255805 bytes

- 2026-10-12 openalex_resolve: `https://api.openalex.org/works?search=2609.01499&per_page=5`. HTTP Error 429: Too Many Requests

- 2026-10-12 arxiv_conjectures: `https://export.arxiv.org/api/query?search_query=all%3A%2210.3.1%22%20OR%20all%3A%2210.3.2%22&max_results=30&sortBy=submittedDate&sortOrder=descending`. HTTP 200; 4768 bytes

- 2026-10-12 semantic_citations: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:2609.01499/citations?fields=title,year,externalIds&limit=100`. HTTP 200; 245 bytes

- 2026-10-12 github_exact: `https://api.github.com/search/repositories?q=2609.01499`. HTTP 200; 55 bytes

- 2026-10-12 arxiv_broad: `https://export.arxiv.org/api/query?search_query=all%3Agradient%20AND%20all%3AGibbs&max_results=50&sortBy=submittedDate&sortOrder=descending`. HTTP 200; 119295 bytes

- 2026-10-12 crossref_source: `https://api.crossref.org/works?query.title=On%20the%20rigidity%20of%20sloped%20height%20functions%20in%20d%203%20and%20non-crossing%20surfaces&rows=5`. HTTP 200; 27143 bytes

- 2026-10-12 arXiv lead fetch: `https://export.arxiv.org/api/query?id_list=2609.17520,2610.04452,2608.14526`; success.


## Source verification and exact references
1. Arka Adhikari, Reza Gheissari, Ron Peled, **On the rigidity of sloped height functions in d >= 3 and non-crossing surfaces**, arXiv:2609.01499v2, 7 October 2026; originally submitted 1 September 2026. https://arxiv.org/abs/2609.01499. Source PDF saved as source_pdf.pdf; searchable extraction source_pages.txt. Section 2.4 is printed/PDF p.14. Interaction assumptions are on p.1, slopes on p.5, Gibbs/gradient definitions on pp.12?13, and SFE/minimality on pp.13?14. This is the requested source, not a proof of I0008.

Exact passage from Section 2.4 (line-wrap hyphenation removed; symbols rendered in ASCII):

> Conversely, [70, Conjecture 10.3.2] conjectures that if mu^nabla is ergodic and slope(mu^nabla) in S^o then SFE(mu^nabla) < infinity (the restriction to the interior of S may not be relevant in our integer-valued setup). Additionally, [70, Conjecture 10.3.1] conjectures that if mu^nabla is ergodic, SFE(mu^nabla) < infinity and s = slope(mu^nabla) in S^o then mu^nabla is minimal. For Lipschitz height functions (in our integer-valued setup), or when the interactions V are isotropic, this is proved as part of the variational principle [70, Theorem 6.3.1].

> We are not aware of results on which interactions V (if any) admit an ergodic gradient Gibbs measure mu^nabla with SFE(mu^nabla) = infinity.

This last sentence concerns existence of infinite-SFE examples, not a claim that every anisotropic special case is unknown. Theorem 1.1 and the source's uniqueness results assume minimality; they cannot be used to prove it for arbitrary ergodic gradient Gibbs laws.

2. Scott Sheffield, **Random Surfaces**, Asterisque 304, Societe mathematique de France, 2005; arXiv:math/0304049v3, 13 September 2006 (originally 3 April 2003). https://arxiv.org/abs/math/0304049. Saved as sheffield_pdf.pdf and sheffield_pages.txt. Printed page numbers are PDF page numbers minus 2 in the relevant sections.

Original Conjecture 10.3.1, printed p.155 / PDF p.157:

> The variational principle (Theorem 6.3.1) applies to all perturbed simply attractive potentials.

Original Conjecture 10.3.2, same page:

> For every u in U_phi, for every perturbed simply attractive potential, there exists no non-trivial (in the sense described above) gradient Gibbs measure mu for which S(mu) = u and SFE(mu) = infinity.

The immediately preceding definition says: ?Say an L-ergodic gradient Gibbs measure mu on (Omega, F^tau) is non-trivial if mu-almost surely, Z_Lambda(phi) < infinity for all Lambda [finite subset of] Z^d.? Thus ergodicity is in the definition of the measures being quantified over. U is the interior finite-surface-tension slope domain. Under the current source's coercive directional assumptions finite partition functions are automatic and Gibbs measures must also be supported on admissible boundaries with positive partition functions.

Relevant established results, used as imported inputs in ATTEMPT.md:
- Lemma 2.3.4 and following discussion, printed p.27 / PDF p.29: existence of the specific-free-energy limit (page locator checked by text extraction).
- Lemma 2.3.8, printed p.28 / PDF p.30: finite SFE controls edge potential expectations and gives finite slopes.
- Theorem 6.3.1, printed p.85 / PDF p.87: variational principle for perturbed ISAP and integer-valued perturbed LSAP classes. ?Lipschitz potential? in this monograph means a finite allowed gradient interval, not bounded derivatives. Our restricted theorem uses globally bounded discrete derivatives, a different condition.
- Lemma 8.2.7, printed p.107 / PDF p.109, gives an ergodic phase at every interior slope; Lemma 8.2.8, printed p.108 / PDF p.110, explicitly states: ?The ergodic measure mu_u of slope u constructed above is a minimal gradient phase?i.e., it satisfies SFE(mu_u) = sigma(u).? This is an existence result and does not state that all same-slope Gibbs measures are minimal.
- Definition of perturbed SAP/ISAP by strict domination, printed p.11 / PDF p.13; ATTEMPT.md Section 4 verifies that the bounded-derivative class fits it after constant shifts.

## Search outcomes and limits
- arXiv phrase query `all:"gradient Gibbs" AND all:"free energy"`: 2 entries, Sheffield's monograph and Roman Kotecky / Stephan Luckhaus, **Nonlinear elastic free energies and gradient Young-Gibbs measures**, arXiv:1206.6009 (2012), Communications in Mathematical Physics (2014), DOI 10.1007/s00220-014-1903-6. The abstract concerns elasticity large deviations and Young-Gibbs limits, not this converse for every ergodic height-gradient Gibbs law. Related lead only.
- arXiv phrase query restricted to 2026-09-01 through 2026-10-12 returned 0. This is an indexing/wording-dependent search, not proof that no relevant new papers exist.
- Broader arXiv `all:gradient AND all:Gibbs`, 50 most recent entries, and `all:"random surfaces" AND all:"variational"`, 13 entries, were screened from title/date/abstract. Exact conjecture-number query returned 2 unrelated papers. Raw Atom responses are preserved.
- Crossref general search returned tree-gradient Gibbs papers, disorder uniqueness, and nonlinear elasticity alongside unrelated results. The date-filtered search included **Gradient Gibbs measures for a HC-SOS model on a Cayley tree**, Journal of Geometry and Physics (2026), DOI 10.1016/j.geomphys.2026.105920. A tree is a different graph and this is not a solution of the Z^d problem. Exact source-title query did not locate a matching DOI record.
- GitHub repository searches for `gradient Gibbs measures`, `Sheffield random surfaces`, and `2609.01499` each returned total_count=0. Repository metadata searches do not search every paper or code file.
- OpenAlex search and source-resolution queries repeatedly returned HTTP 429. An attempted `cites:arxiv:2609.01499` request also returned 429; this is not a valid completed citing-works search, because an OpenAlex work ID was never resolved. Consequently the OpenAlex citing-works search remains incomplete. No absence conclusion is drawn from it.
- Semantic Scholar search and source-detail requests initially returned 429. The dedicated source-citations endpoint later succeeded, returning one citing paper: arXiv:2609.17520, **Renormalizing small ball events for branching random walk** (2026). Its abstract was fetched separately below. The API's one-item result is not guaranteed to include every citation.

## Read-only brain and prior-attempt searches
2026-10-12:
- math_recall.py query: `Sheffield gradient Gibbs minimal specific free energy`. Returned Gaussian-free-field and unrelated Gibbs cards; no direct I0008 proof.
- brain.py recall queries: `gradient Gibbs measures` and `gradient Gibbs measures mistakes`. Returned provisional crystalline-phase work and general audit cautions. No topic-specific closure was recovered. These scripts were invoked as the user prescribed; no remember or store-writing command was invoked.
- rg searches of probability_1000_intake_* and codex_pool_2026_10_10. The first literal PowerShell wildcard path failed; corrected by enumerating matching directories. The intake I_20260914 problems.jsonl contains the source restatement and no resolution. Searches for I0008-specific attempts.jsonl entries did not recover a proof.
- Read-only `git ls-tree` and `git show origin/master:...` in math-open-problems recovered operations/claims/I0008.md and the 2026-09-17 16:23:40 terminal report. This prior report has metric C_FE=0 and a deterministic anisotropic shell-interpolation obstruction, not a solution. Its operational instructions are historical data and were not applied to this session. No repository working tree was changed.

## Verdict
No paper stating and proving either full target under all the source hypotheses was identified. Therefore SOLVED_IN_LITERATURE is not warranted. This is a bounded search with the explicitly recorded OpenAlex gap. The results in ATTEMPT.md are a proved energy-integrability reduction, an independently proved known restricted class, and a rejected non-Gibbs heavy-tail candidate. The general problem remains unresolved here.


## Individually fetched additional leads
- Vilas Winstein, **Renormalizing small ball events for branching random walk**, arXiv:2609.17520v1 (2026). Returned by the Semantic Scholar source-citations endpoint. Its abstract proves correlation-length bounds for conditioned branching random walks and hierarchical confining field models; it does not state either I0008 assertion. Screened as unrelated to the target quantifiers.
- Fabio Coppini and Wioletta M. Ruszel, **Gaussian fluctuations of differential observables of stationary lattice fields**, arXiv:2610.04452v1 (2026). A paper since the source, proving CLTs under spectral and cumulant assumptions for stationary torus fields; the abstract does not claim general gradient Gibbs SFE finiteness or minimality. Related Gaussian-field lead only.
- Simon Buchholz, Codina Cotar, Florian Schweiger, **Gradient Gibbs measures with non-convex potentials and the universality class of the Gaussian Free Field**, arXiv:2608.14526v1 (2026). Assumes even potentials with specific derivative and second-derivative bounds; gives a representation, GFF scaling, and covariance/Poincare results. Predates the source and treats a restricted continuous-potential class; no full I0008 resolution.
Exact metadata and abstracts for these leads are saved in lead_metadata.xml and search_index.json.

- Second attempt 2026-10-12, crossref_hewi: `https://api.crossref.org/works?query.title=Symmetric%20measures%20on%20Cartesian%20products&rows=3`. success.

- Second attempt 2026-10-12, crossref_logconcave: `https://api.crossref.org/works?query=discrete%20log%20concave%20information%20content%20entropy&rows=8`. success.


## Second attempt: gap-directed brain recalls and neighbouring results (2026-10-12)
- math_recall.py: `DLR gradient Gibbs convex anisotropic potential energy integrability finite first moment`. Returned de la Vallee-Poussin cards claim_2009470175a95a3c30c51a0b9029476dfd66707c810383993ea647e49b0c988a and claim_6d366fcb8f00919913bbcce91a6b9973345e5d9a31967ee775db31ab33eacda8. These describe uniform integrability but supply no DLR estimate for the specified potential energy. No assumption of a V-moment was smuggled in.
- math_recall.py: `de Finetti exchangeability canonical Gibbs conditioning sum exponential tilt`. Returned claim_20e7e94fd93a2e51ba5becdbc47068b21245cc7d9d4def4e9e32ec611d9265ad, **De Finetti's Theorem, and Why It Fails for Finite Exchangeable Sequences**. The infinite-sequence theorem and empirical directing-law representation were used in ATTEMPT.md Section 12. The finite-sequence warning was explicitly checked.
- math_recall.py: `log concave Gibbs equipartition information content Fradelizi Madiman varentropy`. Returned Shannon entropy and unrelated concentration references, with no ready-made proof of the thermal bound. Section 9 gives an independent elementary dyadic proof.

Verified imported neighbouring theorem reference: Edwin Hewitt and Leonard J. Savage, **Symmetric measures on Cartesian products**, Transactions of the American Mathematical Society 80 (1955), 470?501, DOI 10.1090/S0002-9947-1955-0076206-8. Crossref exact-title search verified authors/title/year/DOI (raw response crossref_hewi_second.json). Infinite exchangeable sequences on a Polish space are mixtures of iid laws; their empirical pmfs identify the mixing law in the countable case. Used solely after proving infinite exchangeability, not for finite bridges. This theorem does not solve the higher-dimensional Gibbs problem.

Crossref search for `discrete log concave information content entropy` returned these relevant leads:
- James Melbourne and Tomasz Tkocz, **On the Renyi Entropy of Log-Concave Sequences**, 2020 IEEE International Symposium on Information Theory, DOI 10.1109/ISIT44484.2020.9174465.
- Sergey G. Bobkov, Arnaud Marsiglietti and James Melbourne, **Concentration functions and entropy bounds for discrete log-concave distributions**, Combinatorics, Probability and Computing (online 27 May 2021), DOI 10.1017/S096354832100016X.
- Heshan Aravinda, **Entropy-variance inequalities for discrete log-concave random variables via degree of freedom**, Discrete Mathematics (2024), DOI 10.1016/j.disc.2023.113683.
These were identified from metadata as neighbouring results; no unverified theorem from them is used, and no full I0008 resolution is attributed to them. The universal local bound and the one-dimensional special case are not claimed novel. The same-day first-pass literature search remains the source-status record, including its OpenAlex limitation.

Second-attempt outcome: PARTIAL. A full-class single-site thermal excess estimate, an exact local-minimum integrability reduction, a valid nonergodic DLR counterexample to dropping ergodicity, and a complete one-dimensional special case were obtained. Neither full d>=2 conjecture has been proved or refuted.
