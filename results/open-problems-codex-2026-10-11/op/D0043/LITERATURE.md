# D0043 literature audit — 2026-10-12

No solution in print has been verified. Successful retrieval alone is not a literature verdict.

All initial HTTP requests, exact URLs/queries, dates and results are saved in search_log.json; reproducible code is search.py. The searches were:

- Source: https://arxiv.org/pdf/1804.06953 — downloaded to source.pdf and extracted to source.txt (28 PDF pages).
- arXiv API: all:"multicritical" AND (all:"beta" OR all:"operator"), max_results=30 — arxiv.xml.
- arXiv API: all:"exotic edge", max_results=30 — arxiv_exotic.xml.
- OpenAlex works: search=exotic edge operators, per-page=20 — HTTP 429.
- OpenAlex works: search=Operator limits of random matrices, per-page=5 — HTTP 429; source identifier and works citing source not yet obtained.
- OpenAlex works: search=multicritical beta ensembles, per-page=30 — HTTP 429.
- Crossref works: query=multicritical random matrix stochastic operator, rows=20 — crossref.json.
- Semantic Scholar paper/search: query=multicritical edge random matrices, limit=20; fields title,authors,year,externalIds,url,abstract — HTTP 429.
- GitHub repositories: q=multicritical random matrix — github.json (empty result).

Read-only brain queries initiated: math_recall.py "Virag exotic edge stochastic Airy multicritical"; brain.py recall "random matrix higher order edge"; brain.py recall "random matrix higher order edge mistakes". Output inspection pending. Earlier-attempt search initially used a Windows glob argument that rg rejected; needs an enumerated-directory retry. An overly broad repository file listing was truncated; use a path filter before further inspection.

## Source verified

Balint Virag, *Operator limits of random matrices*, ICM 2014 survey, arXiv:1804.06953. PDF page 14, Conjecture 5, says exactly (typesetting reconstructed from extraction):

> Conjecture 5. After scaling, T_n converges to the random operator
> S_{beta,k} = -partial_t^2 + t^{1/(2k+1)} + (2/sqrt(beta)) t^{-k/(2k+1)} b'_t.

The immediately preceding text states: "When V is analytic, the possible decay rates are x^{2k+1/2} for some integer k." It refers to the empirical equilibrium measure for V and says the convexity and analyticity of V force square-root edge decay. Thus the critical problem is outside the uniformly convex generic-edge assumptions of Theorem 8.1. Conjecture 5 itself does not state a topology, scaling constants, boundary condition, or a fully enumerated hypothesis list; it refers to [38] for a more precise version. These details must not be invented. The next sentence says beta=2 eigenvalue limits have been studied in [9] by Riemann-Hilbert methods.

Theorem 8.1 on PDF page 12, under V''>c>0 in the polynomial-potential discussion, proves generic-edge norm-resolvent convergence to SAO_beta. This is a k=0 lead, not the higher-order conjecture.

## Prior work audit

The intake ledger's D0043-A001 (2026-09-08) says the singular noise at zero obstructs operator construction. That obstruction is removed by the integrated-noise form argument in ATTEMPT.md. Its claimed simultaneous scaling balance is incorrect as stated: c^(-2), c^(1/(2k+1)) and c^(-k/(2k+1)-1/2) are not equal exponents. No scaling claim from that ledger is used.

Repository paths found by read-only git inspection include a 2026-09-18 origin-noise bound and global-form compact-resolvent attempt, followed by critical-Hessian and nonhomogeneous-Schur handoffs. Those are prior work, not proofs of convergence; full inspection is pending. Exact path list is in prior_repository_paths.txt, and the matching ledger records are in prior_ledger_matches.txt.

Follow-up searches are reproducible in search_followup.py and logged in followup_search_log.json once completed: arXiv title/higher-order plus math.PR multicritical/critical-edge searches; arXiv exact source title; OpenAlex source retry and works citing it if an identifier is returned; Semantic Scholar source/citations endpoint; Crossref higher order Tracy Widom stochastic operator; GitHub stochastic Airy repositories. No matching solution theorem has been certified.

## Primary references used in the counterexample

1. M. Krishnapur, B. Rider, B. Virag, *Universality of the stochastic Airy operator*, arXiv:1306.4832 (2013), published in *Communications on Pure and Applied Mathematics* 69 (2016), 145-199. Downloaded as KRV.pdf, extracted as KRV.txt. Conjecture 45 on PDF p.57 explicitly requires Dirichlet boundary and convergence of the ordered eigenvalues. The matrix eigenvalue law is equation (1), PDF p.3. This is a conjecture, not a literature solution.
2. T. Claeys, M. Vanlessen, *Universality of a double scaling limit near singular edge points in random matrix models*, *Communications in Mathematical Physics* 273 (2007), 499-532; arXiv:math-ph/0607043. Downloaded CV.pdf/CV.txt. Assumptions 1.1 and Example 1.2, PDF p.5, contain exactly the quartic W used here and its compatible deformation W+s x+t(x^3-6x). Theorem 1.7, PDF pp.6-7, proves locally uniform critical-edge kernel convergence at scale n^(2/7). Lax equations (1.15)-(1.17) and phase (1.21), PDF p.4; RH equations (3.39)-(3.42), PDF pp.20-21, supply the positive-axis exponential bound. This theorem is an input to an ORIGINAL counterexample argument, not a theorem stating the answer to D0043.
3. T. Claeys, A. Its, I. Krasovsky, *Higher-order analogues of the Tracy-Widom distribution and the Painleve II hierarchy*, *Communications on Pure and Applied Mathematics* 63(3) (2010), 362-412; arXiv:0901.2473; DOI 10.1002/cpa.20284. Downloaded CIK.pdf/CIK.txt. Example 1.2, PDF p.2, equations (1.4)-(1.5), gives the quartic and density. Equation (1.23), PDF p.5, gives K^(k)(u,v)=O(exp(-c u^((4k+3)/2)-c v^((4k+3)/2))); (1.24) gives the corresponding positive-s determinant bound. IMPORTANT: PDF p.3 calls the largest-eigenvalue limit (1.15) expected and explicitly says the paper does not prove it. The counterexample therefore uses CV's proved local-kernel theorem and a finite-interval first-moment argument, not (1.15).

CV theorem quotation (wording reproduced; displayed formulas transcribed):

> Theorem 1.7 Let V_{s,t} = V_0 + sV_1 + tV_2 be such that Assumptions 1.1 above are satisfied. We take a double scaling limit where we let n -> infinity and at the same time s, t -> 0, in such a way that lim n^{6/7}s and lim n^{4/7}t exists, and put s_0 = c_1 * lim n^{6/7}s in R, t_0 = c_2 * lim n^{4/7}t in R, where the constants c_1 and c_2 are defined by (1.30). Then, the 2-point kernel K_n^{(s,t)} satisfies the following universality result, lim [1/(c n^{2/7})] K_n^{(s,t)}(b + u/(c n^{2/7}), b + v/(c n^{2/7})) = K_{crit,III}(u,v;s_0,t_0), uniformly for u, v in compact subsets of R.

Line-by-line application: choose V0=W, V1=x,V2=x^3-6x from the paper's Example 1.2; set all finite-n deformation parameters to zero, so both limits and s0,t0 are zero; b=2 by its equilibrium density; the positive c is equation (1.30); uniform convergence includes the diagonal on each fixed interval, allowing convergence of its integral. The theorem alone does not refute D0043: the Gaussian Rayleigh-quotient bound and Portmanteau/first-moment contradiction are supplied in COUNTEREXAMPLE.md.

## Later leads, not matching solutions

- *The multiplicative constant in asymptotics of higher-order analogues of the Tracy-Widom distribution*, arXiv:2501.12679 (2025), retrieved in arxiv_critical.xml: its abstract describes higher-order large-gap constants and transitions, not general-beta tridiagonal convergence. Lead only; author metadata remains in the XML.
- *Unitary ensembles with a critical edge point, their multiplicative statistics and the Korteweg-de-Vries hierarchy*, arXiv:2504.20721 (2025), retrieved in arxiv_critical.xml: unitary critical-edge multiplicative statistics, not the conjectured operator theorem. Lead only.
- *Multicritical Schur measures and higher-order analogues of the Tracy-Widom distribution*, arXiv:2307.05303, DOI 10.1007/s11040-023-09472-7 (2024): a different model and different universality classes; not a matching solution.

Follow-up OpenAlex source lookup and Semantic Scholar source/citations request both again returned HTTP 429. An OpenAlex citation list could not be obtained because a source work ID was not returned. GitHub stochastic-Airy repository search returned a repository result, not a published solution. These failures prevent a complete citation audit; they do not affect the primary-theorem counterexample proof. Worldwide novelty is not established. Verdict is SOLVED by counterexample, not SOLVED_IN_LITERATURE.

## Exact metadata for later/related leads

- Haruna Aida, Taro Kimura. *Multicritical Scaling Limit of Shifted Schur Measure*. http://arxiv.org/abs/2605.15744v1; first posted 2026-05-15T08:54:12Z. Lead only; not a matching operator-convergence theorem.
- Dan Betea, Jérémie Bouttier, Harriet Walsh. *Multicritical Schur measures and higher-order analogues of the Tracy-Widom distribution*. http://arxiv.org/abs/2307.05303v3; first posted 2023-07-09T21:33:48Z. Lead only; not a matching operator-convergence theorem.
- Pierre Le Doussal, Satya N. Majumdar, Grégory Schehr. *Multicritical edge statistics for the momenta of fermions in non-harmonic traps*. http://arxiv.org/abs/1802.06436v1; first posted 2018-02-18T20:06:36Z. Lead only; not a matching operator-convergence theorem.
- Mattia Cafasso, Carla Mariana da Silva Pinheiro. *Unitary ensembles with a critical edge point, their multiplicative statistics and the Korteweg-de-Vries hierarchy*. http://arxiv.org/abs/2504.20721v2; first posted 2025-04-29T13:01:51Z. Lead only; not a matching operator-convergence theorem.
- Dan Dai, Wen-Gao Long, Shuai-Xia Xu, Lu-Ming Yao, Lun Zhang. *The multiplicative constant in asymptotics of higher-order analogues of the Tracy-Widom distribution*. http://arxiv.org/abs/2501.12679v2; first posted 2025-01-22T06:49:34Z. Lead only; not a matching operator-convergence theorem.

## Complete HTTP search audit

- 2026-10-12 04:21:38.282128: source: https://arxiv.org/pdf/1804.06953 — source: 276733 bytes
- 2026-10-12 04:21:37.711286: arxiv: https://export.arxiv.org/api/query?search_query=all%3A%22multicritical%22+AND+%28all%3A%22beta%22+OR+all%3A%22operator%22%29&max_results=30 — arxiv: 63763 bytes
- 2026-10-12 04:21:37.076470: openalex: https://api.openalex.org/works?search=exotic+edge+operators&per-page=20 — openalex: ERROR HTTP Error 429: Too Many Requests
- 2026-10-12 04:21:37.077905: openalex_source: https://api.openalex.org/works?search=Operator+limits+of+random+matrices&per-page=5 — openalex_source: ERROR HTTP Error 429: Too Many Requests
- 2026-10-12 04:21:39.399955: crossref: https://api.crossref.org/works?query=multicritical+random+matrix+stochastic+operator&rows=20 — crossref: 186855 bytes
- 2026-10-12 04:21:37.649702: semantic: https://api.semanticscholar.org/graph/v1/paper/search?query=multicritical+edge+random+matrices&limit=20&fields=title%2Cauthors%2Cyear%2CexternalIds%2Curl%2Cabstract — semantic: ERROR HTTP Error 429: 
- 2026-10-12 04:21:37.603398: github: https://api.github.com/search/repositories?q=multicritical+random+matrix — github: 55 bytes
- 2026-10-12 04:21:38.132971: arxiv_exotic: https://export.arxiv.org/api/query?search_query=all%3A%22exotic+edge%22&max_results=30 — arxiv_exotic: 23549 bytes
- 2026-10-12 04:21:37.771859: openalex_multi: https://api.openalex.org/works?search=multicritical+beta+ensembles&per-page=30 — openalex_multi: ERROR HTTP Error 429: Too Many Requests
- 2026-10-12 04:33:44.745574: arxiv_higher: https://export.arxiv.org/api/query?search_query=%28ti%3A%22higher+order%22+AND+all%3A%22random+matrices%22%29+OR+%28all%3A%22multicritical%22+AND+cat%3Amath.PR%29+OR+%28all%3A%22exotic%22+AND+au%3AVirag%29&max_results=60 — arxiv_higher: 45965 bytes
- 2026-10-12 04:33:44.535693: arxiv_critical: https://export.arxiv.org/api/query?search_query=all%3A%22critical+edge%22+AND+%28cat%3Amath.PR+OR+cat%3Amath-ph%29&max_results=40 — arxiv_critical: 31436 bytes
- 2026-10-12 04:33:49.299494: arxiv_virag: https://export.arxiv.org/api/query?search_query=ti%3A%22Operator+limits+of+random+matrices%22&max_results=5 — arxiv_virag: 1786 bytes
- 2026-10-12 04:33:44.198723: openalex_retry: https://api.openalex.org/works?search=Operator+limits+of+random+matrices&per_page=5 — openalex_retry: ERROR HTTP Error 429: Too Many Requests
- 2026-10-12 04:33:44.701649: semantic_source: https://api.semanticscholar.org/graph/v1/paper/ARXIV:1804.06953?fields=title,authors,year,citations.title,citations.year,citations.externalIds — semantic_source: ERROR HTTP Error 429: 
- 2026-10-12 04:33:46.434854: crossref_higher: https://api.crossref.org/works?query.bibliographic=higher+order+Tracy+Widom+stochastic+operator&rows=15 — crossref_higher: 101921 bytes
- 2026-10-12 04:33:45.247048: github_exotic: https://api.github.com/search/repositories?q=%22stochastic+Airy%22 — github_exotic: 5688 bytes

Targeted source searches/downloads, 2026-10-12: https://arxiv.org/pdf/1306.4832; https://arxiv.org/pdf/0901.2473; arXiv API title query `ti:"Universality of a double scaling limit near singular edge points"`, max_results=5, found math-ph/0607043v1; downloaded https://arxiv.org/pdf/math-ph/0607043v1. Exact query URL in targeted_search_log.json.

Bibliographic correction: the survey points to reference [38] (Ramirez-Rider-Virag) for precision, but its explicit nonregular-edge Conjecture 45 is in KRV ([31] in the survey). Both source bibliography entries were inspected. The counterexample uses actual eigenvalue densities to fix all potential-normalization factors, irrespective of notation conventions in the surveys.

## Final targeted status/novelty search

The final targeted searches returned no matching solution or refutation. arXiv:1811.00509, *Linear statistics and pushed Coulomb gas at the edge of beta random matrices: four paths to large deviations* (2018), studies ordinary Airy-beta/Gaussian-edge statistics rather than k=1 critical edges. It is a regular-edge tail-method lead only; no theorem from it is used. Other returned items were off topic. This bounded miss does not establish novelty.

- 2026-10-12: arxiv_nonregular: https://export.arxiv.org/api/query?search_query=%28cat%3Amath.PR+OR+cat%3Amath-ph%29+AND+%28all%3Anonregular+OR+all%3A%22higher-order%22%29+AND+%28all%3Atridiagonal+OR+all%3A%22stochastic+Airy%22%29&max_results=40&sortBy=submittedDate&sortOrder=descending — 12318 bytes
- 2026-10-12: arxiv_exotic_math: https://export.arxiv.org/api/query?search_query=cat%3Amath.PR+AND+all%3Aexotic+AND+all%3Aoperator&max_results=30 — 17698 bytes
- 2026-10-12: crossref_tail: https://api.crossref.org/works?query.bibliographic=exotic+stochastic+edge+operator+higher+order+tail&rows=10 — 36711 bytes

Exact metadata for the final regular-edge lead: Alexandre Krajenbrink, Pierre Le Doussal. *Linear statistics and pushed Coulomb gas at the edge of beta random matrices: four paths to large deviations*. http://arxiv.org/abs/1811.00509v1. Posted 2018-11-01T17:26:55Z. Not a source-matching solution.
