# D0051 literature check — 2026-10-12

The source is Jian Ding, Julien Dubédat, Ewain Gwynne, Introduction to the Liouville quantum gravity metric, arXiv:2109.01252v2; ICM 2022 proceedings (2023), pp. 4212–4244, DOI 10.4171/icm2022/40. Downloaded source.pdf; extracted source.txt. Problem 5.3 is PDF page 24. The preceding definition explicitly uses limsup, not a limit. The problem is for xi > 0, not just subcritical gamma in (0,2).

Exact statement (PDF p.24):
> Problem 5.3. Let ξ > 0 and let P be a D_h-geodesic. Is it possible to compute the Hausdorff dimensions of P ∩ T^α_h for each α ∈ [−2, 2] with respect to the D_h (resp. the Euclidean metric)? More weakly, as there a unique value of α which maximizes this dimension? In other words, is there a “typical” thickness for a point on an LQG geodesic?

The apparent “as there” typo is in the retrieved PDF. Preceding definition: limsup_{ε→0} h_ε(z)/log ε^{-1}=α. The section assumes the whole-plane GFF used for the metric; the supercritical metric has infinite-distance singular points, so a nonconstant finite-length geodesic is understood between finite-distance endpoints.

## Important new lead, not a solution
Manan Bhatia and Konstantinos Kavvadias, Uniformity of extremal behaviour along geodesics in Liouville quantum gravity, arXiv:2608.22693v1 (24 August 2026). Theorem 1(2), PDF pp.2–3, asserts deterministic constants for both thickness-intersection dimensions on every nondegenerate interior segment of every geodesic, for fixed gamma in (0,2) and fixed alpha. It does not evaluate the constants. PDF p.4 explicitly says the method “would not yield any information for the ‘average’ thickness (see [DDG23, Problem 5.3])”. Moreover §2.1, PDF p.5, uses liminf for alpha ≥ 0, and sign reflection for alpha < 0. This is a different convention from the source. For alpha<0, sign reflection of their positive liminf convention is precisely limsup h/log=alpha, so Theorem 1(2) DOES apply to the source's negative levels. For alpha>=0 the conventions differ, and no transfer is claimed. The ordinary Euclidean geodesic-dimension statement is unaffected by this mismatch.

Ewain Gwynne and Joshua Pfeffer, KPZ formulas for the Liouville quantum gravity metric, arXiv:1905.11790v3 (28 December 2019), retrieved kpz.pdf. Theorem 1.4 requires field independence; it cannot be applied to an LQG geodesic. Proposition 2.5 gives a one-sided thickness dimension bound for arbitrary Borel sets, but defines thick points by an actual limit; the upper-bound proof in §2.2 uses independence. Theorem 1.8 supplies bounds for arbitrary Borel sets. These are leads, not a computation of the spectrum.

Ewain Gwynne, Joshua Pfeffer and Scott Sheffield, Geodesics and metric ball boundaries in Liouville quantum gravity, arXiv:2010.07889v2; Probability Theory and Related Fields 182 (2022), 905–954. Retrieved gps.pdf.

Riddhipratim Basu, Manan Bhatia and Shirshendu Ganguly, Environment seen from infinite geodesics in Liouville Quantum Gravity, arXiv:2107.12363v1 (26 July 2021). Retrieved environment.pdf. Environment convergence/singularity is not a thickness spectrum computation.

Xiaoyu Hu, Jason Miller and Yuval Peres, Thick points of the Gaussian free field, Annals of Probability 38 (2010), 896–926, DOI 10.1214/09-AOP498; arXiv:0902.3842. Retrieved hmp.pdf.

## Read-only prior work
Read D0051 problem and attempt D0051-A001 in probability_1000_intake_D_20260908. Its predicted negative maximizing thickness is heuristic; its identification of a geodesic hitting exponent with a Hausdorff dimension is not justified. Read origin/master:probability_campaigns/codex_pool_2026-10-10/wave300/P0297/w516_core-proof_prover/ATTEMPT.md with git show. This neighbouring metric-dimension attempt warns about field-dependent optimizers and near-tie corrections; it does not solve D0051. Brain recall on the topic and topic mistakes returned mainly unrelated memories. Math recall identified the field-independence pitfall, checked against the primary paper here. No recalled item is treated as a theorem without source verification.

## Search ledger
Every HTTP query and download, with date, URL, return status or error, is preserved in search_log.jsonl. Responses are saved locally. arXiv broad and Liouville-targeted searches, Crossref broad and source-title searches, OpenAlex source/search/citation requests, Semantic Scholar search/citations, and GitHub repository searches were attempted. OpenAlex and Semantic Scholar returned HTTP 429; their citation lists have not been inspected. First GitHub search failed TLS, second broader search succeeded with zero results. One preliminary OpenAlex citation attempt used an unverified DOI and is superseded by the verified source DOI requests; neither returned results.

## Complete dated HTTP search/download ledger

- 2026-10-12; openalex_search; `https://api.openalex.org/works?search=Liouville+quantum+gravity+geodesic+thick+points&per-page=50`; 429
- 2026-10-12; openalex_source; `https://api.openalex.org/works?search=Introduction+to+the+Liouville+quantum+gravity+metric&per-page=5`; 429
- 2026-10-12; arxiv; `https://export.arxiv.org/api/query?search_query=all%3A%22geodesic%22+AND+%28all%3A%22thick+points%22+OR+all%3A%22thickness%22+OR+all%3A%22multifractal%22%29&start=0&max_results=60&sortBy=submittedDate&sortOrder=descending`; 200
- 2026-10-12; semantic; `https://api.semanticscholar.org/graph/v1/paper/search?query=Liouville+quantum+gravity+geodesic+thick+points&limit=40&fields=title%2Cauthors%2Cyear%2CexternalIds%2Curl%2Cabstract`; 429
- 2026-10-12; source; `https://arxiv.org/pdf/2109.01252`; 200
- 2026-10-12; github; `https://api.github.com/search/repositories?q=LQG+geodesic+thick+points&per_page=30`; HTTPSConnectionPool(host='api.github.com', port=443): Max retries exceeded with url: /search/repositories?q=LQG+geodesic+thick+points&per_page=30 (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1081)')))
- 2026-10-12; crossref; `https://api.crossref.org/works?query=Liouville+quantum+gravity+geodesic+thick+points&rows=40`; 200
- 2026-10-12; openalex_citations; `https://api.openalex.org/works?filter=references.doi%3A10.4310%2Fcdm.2022.v2022.n1.a1&per_page=100`; 429
- 2026-10-12; github_retry; `https://api.github.com/search/repositories?q=%22Liouville+quantum+gravity%22&per_page=20`; 200
- 2026-10-12; semantic_source; `https://api.semanticscholar.org/graph/v1/paper/ARXIV:2109.01252?fields=title,citations.title,citations.year,citations.externalIds`; 429
- 2026-10-12; crossref_source; `https://api.crossref.org/works?query.title=Introduction+to+the+Liouville+quantum+gravity+metric&rows=3`; 200
- 2026-10-12; openalex_retry; `https://api.openalex.org/works?search=Introduction+to+the+Liouville+quantum+gravity+metric&per_page=5`; 429
- 2026-10-12; arxiv_boundary; `https://export.arxiv.org/api/query?search_query=ti%3A%22dimension%22+AND+au%3A%22Pfeffer%22+AND+au%3A%22Sheffield%22&max_results=15`; 200
- 2026-10-12; arxiv_kpz; `https://export.arxiv.org/api/query?search_query=ti%3A%22KPZ+formulas%22&max_results=10`; 200
- 2026-10-12; extremal; `https://arxiv.org/pdf/2608.22693`; 200
- 2026-10-12; arxiv_targeted; `https://export.arxiv.org/api/query?search_query=all%3A%22Liouville%22+AND+%28all%3A%22geodesic%22+OR+all%3A%22thick%22%29&max_results=100&sortBy=submittedDate&sortOrder=descending`; 200
- 2026-10-12; openalex_correct_citations; `https://api.openalex.org/works?filter=cites%3Ahttps%3A%2F%2Fdoi.org%2F10.4171%2Ficm2022%2F40&per-page=100`; 429
- 2026-10-12; openalex_correct_source; `https://api.openalex.org/works/https://doi.org/10.4171/icm2022/40`; 429
- 2026-10-12; kpz; `https://arxiv.org/pdf/1905.11790`; 200
- 2026-10-12; hmp; `https://arxiv.org/pdf/0902.3842`; 200
- 2026-10-12; environment; `https://arxiv.org/pdf/2107.12363`; 200
- 2026-10-12; arxiv_followup; `https://arxiv.org/pdf/2609.27861`; 200
- 2026-10-12; gps; `https://arxiv.org/pdf/2010.07889`; 200

All arXiv hits, titles, authors, dates and abstracts retained in arxiv_results.json. The broad search is noisy (many unrelated geometry/astrophysics hits); the Liouville-targeted query supplies the relevant recent candidates.

Chunhao Cai, Closed Response Calculus and Joint Densities for the Liouville Quantum Gravity Metric, arXiv:2609.27861v1 (PDF displays 20 August 2026). Retrieved response_calculus.pdf. Main results concern a closed response calculus and densities for logarithmic distance ratios indexed by finite forests; neither a thick-point intersection spectrum nor its optimizer is computed. Not a solution to D0051.

Additional leads from targeted arXiv: Zherui Fan and Subhajit Goswami, Roughness of geodesics in Liouville quantum gravity, arXiv:2205.00676v1; Bhatia–Kavvadias, Strong confluence of geodesics in Liouville quantum gravity, arXiv:2512.09219v2; Ding–Gwynne, Regularity and confluence of geodesics for the supercritical Liouville quantum gravity metric, arXiv:2104.06502v4; Dimension lower bounds in random geometry via Lipschitz functions, arXiv:2606.10496v1. Their retrieved abstracts concern roughness, confluence or other sets, not an evaluation of the requested spectrum. No results from these papers are assumed in the proofs here.

GPS Remark 1.12 (retrieved PDF p.7) first defines metric thick points via an actual limit of metric-ball diameter exponents and states analogous zero-one-law arguments for ordinary thick points. It does not give the spectrum values. The source's use of this remark for all xi and limsup thickness is reported as the source's assertion; we do not independently extend the remark beyond its stated subcritical framework.

Refined scope of 2608.22693: for each fixed alpha<0 and subcritical gamma, the theorem's negative-thickness convention equals the source's. Its uniformity/determinism result therefore supplies a rigorous reduction for negative spectrum levels, still leaving their values unknown. See ATTEMPT.md §G.

## Second attempt: gap-directed brain and source checks, 2026-10-12

- Math store query: geodesic occupation measure Gaussian integration by parts Weyl response Frostman thickness lower bound. Relevant hints: Gaussian integration-by-parts card claim_1564c803ed1f4f740d9c5f603549c04916aaed26f09262fdb378ee739b59ba18; unresolved response-defect card claim_d63808133bd4ac23d51981a64943e5f6e9c692bdd9a12d825ad837dd594937af. The latter was walked by id and saved in brain_gap_response.txt. It explicitly records an open input, not a proved occupation law.
- Math store query: Frostman lemma disintegration Hausdorff dimension level sets dimension conservation. No LQG-specific dimension-conservation theorem was returned. The general Hausdorff-dimension card claim_e8f3827645b13dbf1ff1701188ae2135 was walked and saved in brain_frostman_response.txt.
- Rechecked GPS arXiv:2010.07889v2 Lemma 1.6, PDF p.5, for finite-energy Frostman measures on compact sets. Rechecked HMP arXiv:0902.3842v3 Theorem 1.2 and following paragraph, PDF p.3, for the circle-average limsup-at-least extension and emptiness above thickness 2 (with the field normalization conversion in ATTEMPT.md). No new literature theorem solving D0051 is claimed.
- New compact Cantor construction is proved directly in SECOND_ATTEMPT.md, with no unverified fractal dimension formula assumed.
