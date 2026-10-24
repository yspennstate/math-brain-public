# E0112 literature and source audit (2026-10-11)

Source downloaded: Francis Comets and Cl?ment Cosco, Brownian Polymers in Poissonian Environment: a survey, arXiv:1805.10899v2, 19 June 2023 (title-page date June 21, 2023). Local copy survey.pdf. Conjecture 4.3.2 starts PDF p.24 (printed p.22), continues PDF p.25 (printed p.23).

Exact source conditions: d-dimensional Brownian motion, d>=1, Poisson intensity nu>0, r>0, balls of volume r^d, beta real, fixed direction xi in R^d. Point-to-point means Brownian bridge from 0 to t xi. Normalization is exp[-nu r^d t (exp(beta)-1)].

The intake's negative definition has a transcription error: source has inf{beta <= 0: lim_t E[(W_t^{dir,xi})^(1/2)]>0}. With beta>=0 the infimum would be 0 because beta=0 belongs to the set. The source conjectures overline(beta)_c^? = overline(beta)_c^{?,dir}: BOTH thresholds are barred, confirmed from source_ch-dir.tex. PDF text extraction omits those bars. These are weak-disorder thresholds, not the unbarred free-energy thresholds of section 2. Second bullet: the local limit theorem (4.3.13) holds throughout weak disorder and would imply the first conjecture.

Earlier attempt E0112-A001 (probability_1000_intake_E_20260908/attempts.jsonl) is invalid as a reduction: it treats the two sign branches as competing thresholds, overlooks beta<=0, and confuses the P2P family with the P2L martingale. The source already proves monotonicity, Theorem 3.1.3.

Read-only brain calls: math_recall.py "Brownian polymer Poisson critical disorder"; brain.py recall "Brownian polymers Poisson disorder mistakes". No verified relevant Poissonian local-limit result returned. Read intake problems.jsonl, attempts.jsonl and sources.jsonl for E0112.

## Searches
- 2026-10-11 arxiv: `https://export.arxiv.org/api/query?search_query=all%3A%22Poissonian%22+AND+all%3A%22polymer%22&start=0&max_results=50&sortBy=submittedDate&sortOrder=descending`; HTTP 200; 22463 bytes; error None. Raw response search_arxiv.txt when successful.
- 2026-10-11 openalex: `https://api.openalex.org/works?search=Brownian+polymers+Poissonian+environment&per-page=50`; HTTP None; 0 bytes; error HTTP Error 429: Too Many Requests. Raw response search_openalex.txt when successful.
- 2026-10-11 crossref: `https://api.crossref.org/works?query=Brownian+polymers+Poissonian+environment&rows=30`; HTTP 200; 204667 bytes; error None. Raw response search_crossref.txt when successful.
- 2026-10-11 semantic: `https://api.semanticscholar.org/graph/v1/paper/search?query=Brownian+polymers+Poissonian+environment&limit=30&fields=title%2Cauthors%2Cyear%2CexternalIds%2Curl%2Cabstract`; HTTP None; 0 bytes; error HTTP Error 429: . Raw response search_semantic.txt when successful.
- 2026-10-11 github: `https://api.github.com/search/repositories?q=Brownian+polymer+Poissonian`; HTTP 200; 55 bytes; error None. Raw response search_github.txt when successful.
- 2026-10-11 arxiv_http: `http://export.arxiv.org/api/query?search_query=all%3A%22Poissonian%22+AND+all%3A%22polymer%22&max_results=30`; HTTP 200; 22463 bytes; error None. Raw response search_arxiv_http.txt when successful.
- 2026-10-11 arxiv_poisson: `https://export.arxiv.org/api/query?search_query=all%3A%22polymer%22+AND+all%3A%22Poisson%22&max_results=60&sortBy=submittedDate&sortOrder=descending`; HTTP 200, bytes 140662, error None.
- 2026-10-11 arxiv_local: `https://export.arxiv.org/api/query?search_query=all%3A%22polymer%22+AND+%28all%3A%22local+limit%22+OR+all%3A%22weak+disorder%22%29&max_results=50&sortBy=submittedDate&sortOrder=descending`; HTTP 200, bytes 88089, error None.
- 2026-10-11 oa_retry: `https://api.openalex.org/works?search=Brownian+Polymers+in+Poissonian+Environment+a+survey&per_page=10`; HTTP None, bytes 0, error HTTP Error 429: Too Many Requests.
- 2026-10-11 s2_source: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:1805.10899?fields=title,authors,year,externalIds,citations.title,citations.year,citations.externalIds`; HTTP None, bytes 0, error HTTP Error 429: .
- 2026-10-11 crossref_local: `https://api.crossref.org/works?query.bibliographic=directed+polymers+local+limit+theorem+weak+disorder&rows=25`; HTTP 200, bytes 161417, error None.
- 2026-10-11 oa_source_filter: `https://api.openalex.org/works?filter=title.search%3ABrownian+Polymers+in+Poissonian+Environment&per-page=5`; HTTP None, 0 bytes, error HTTP Error 429: Too Many Requests. The arXiv-URL cites filter is a fallback attempt, not a resolved OpenAlex work ID.
- 2026-10-11 oa_citations_arxiv: `https://api.openalex.org/works?filter=cites%3Ahttps%3A%2F%2Farxiv.org%2Fabs%2F1805.10899&per-page=100`; HTTP None, 0 bytes, error HTTP Error 429: Too Many Requests. The arXiv-URL cites filter is a fallback attempt, not a resolved OpenAlex work ID.
- 2026-10-11 s2_bulk: `https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=%22Brownian%22+%22Poissonian%22+%22polymer%22&fields=title%2Cauthors%2Cyear%2CexternalIds`; HTTP 200, 3694 bytes, error None. The arXiv-URL cites filter is a fallback attempt, not a resolved OpenAlex work ID.

## TeX verification
Fetched https://arxiv.org/src/1805.10899 on 2026-10-11; saved survey_source.tar and source_*.tex. In source_ch-dir.tex the exact first equality is `\overline{\b}_c^\pm = \overline{\b}_c^{\pm,{dir}}`. Negative definition is `\inf\{ \b \leq 0: \lim_t \P[ (W_t^{{dir}, \xi})^{1/2}] >0\}`. The local-limit theorem display uses unnormalized Z despite its earlier definition; we verify the normalized version in Vargas, the cited primary source, rather than adopt this normalization slip literally.

- 2026-10-11 primary-source fetch: https://www.numdam.org/item/AIHPB_2006__42_5_521_0.pdf; see vargas2006.pdf/txt if successful.

## Relevant references and applicability

- Ryoki Fukushima, Stefan Junk. **Zero temperature limit for the Brownian directed polymer among Poissonian disasters**. arXiv:1810.09600, first posted 2018-10-22T23:41:16Z, version returned http://arxiv.org/abs/1810.09600v2. Abstract: We study a continuum model of directed polymer in random environment. The law of the polymer is defined as the Brownian motion conditioned to survive among space-time Poissonian disasters. This model is well-studied in the positive temperature regime. However, at zero-temperature, even the existence of the free energy has not been proved. In this article, we prove that the free energy exists and is continuous at zero-temperature.

- Clément Cosco. **The Intermediate Disorder Regime for Brownian Directed Polymers in Poisson Environment**. arXiv:1804.09571, first posted 2018-04-25T13:51:34Z, version returned http://arxiv.org/abs/1804.09571v2. Abstract: We consider the Brownian directed polymer in Poissonian environment in dimension 1+1, under the so-called intermediate disorder regime, which is a crossover regime between the strong and weak disorder regions. We show that, under a diffusive scaling involving different parameters of the system, the renormalized point-to-point partition function of the polymer converges in law to the solution of the stochastic heat equation with Gaussian multiplicative noise. The Poissonian environment provides a natural setting and strong tools, such as the Wiener-Ito chaos expansion, which, applied to the partition function, is the basic ingredient of the proof.

- Min Wang. **The intermediate disorder regime for stable directed polymer in Poisson environment**. arXiv:2401.04459, first posted 2024-01-09T09:50:26Z, version returned http://arxiv.org/abs/2401.04459v1. Abstract: We consider the stable directed polymer in Poisson random environment in dimension 1+1, under the intermediate disorder regime. We show that, under a diffusive scaling involving different parameters of the system, the normalized point-to-point partition function of the polymer converges in law to the solution of the stochastic heat equation with fractional Laplacian and Gaussian multiplicative noise.

- Junjie Cao, Guanglin Rang, Jianglun Wu. **Disorder Thresholds and Free Energy of Brownian Directed Polymers with Product and Radial Spatial Correlations**. arXiv:2608.29501, first posted 2026-08-30T01:35:13Z, version returned http://arxiv.org/abs/2608.29501v1. Abstract: We study a Brownian directed polymer in a centered Gaussian environment that is white in time and colored in space having long-range spatial correlations. For product-type covariances \(Q(x)\asymp\prod_{j=1}^d(1+|x_j|)^{-α_j}\), with \(α_j\in(0,1)\) and \(κ=\sum_jα_j\), we identify the disorder transition at the marginal value \(κ=2\). For \(κ>2\), weak disorder holds at sufficiently small inverse temperature; for \(κ<2\), the quenched free energy $p(β)$ satisfies \(-p(β)\asympβ^{4/(2-κ)}\) as \(β\downarrow0\). For \(κ=2\), strong disorder holds for every \(β>0\), while \(p(β)=0\) for all sufficiently small \(β\), so \(β_c=0<\barβ_c\). We also consider the radial covariance cases, where $ Q(x)\asymp(1+|x|)^{-\vartheta}$, when \(d\ge3,\vartheta=2\) and \(d=2,\vartheta\ge2\), which was left unanswered in Lacoin~\cite{Lacoin2011}. When $d=2$, we get \(\ln(-p(β))\asymp-β^{-2}\) for \(\vartheta>2\) and \(\ln(-p(β))\asymp-β^{-1}\) for \(\vartheta=2\). The proofs consist of replica coupling, Feynman--Kac variational formula, overlap methods, and continuous-space fractional moments with ordered Wiener-chaos changes of measure.

- Stefan Junk, Hubert Lacoin. **Coincidence of critical points for directed polymers for general environments and random walks**. arXiv:2502.04113, first posted 2025-02-06T14:40:33Z, version returned http://arxiv.org/abs/2502.04113v2. Abstract: For the directed polymer in a random environment (DPRE), two critical inverse-temperatures can be defined. The first one, $β_c$, separates the strong disorder regime (in which the normalized partition function $W^β_n$ tends to zero) from the weak disorder regime (in which $W^β_n$ converges to a nontrivial limit). The other, $\bar β_c$, delimits the very strong disorder regime (in which $W^β_n$ converges to zero exponentially fast). It was proved previously that $β_c=\bar β_c$ when the random environment is upper-bounded for the DPRE based on the simple random walk. We extend this result to general environment and arbitrary reference walk. We also prove that $β_c=0$ if and only the $L^2$-critical point is trivial.

- Stefan Junk, Hubert Lacoin. **Strong disorder and very strong disorder are equivalent for directed polymers**. arXiv:2402.02562, first posted 2024-02-04T16:39:59Z, version returned http://arxiv.org/abs/2402.02562v3. Abstract: We show that if the normalized partition function $W^β_n$ of the directed polymer model on $\mathbb Z^d$ converges to zero, then it does so exponentially fast. This implies that there exists a critical value $β_c$ for the inverse temperature such that the normalized partition function has a non-degenerate limit for all $β\in [0,β_c]$ -- weak disorder holds -- while for $β\in (β_c,\infty)$ it converges exponentially fast to zero -- very strong disorder holds. This solves a twenty-years-old conjecture formulated by Comets, Yoshida, Carmona and Hu. Our proof requires a technical assumption on the environment, namely, that it is bounded from above.

- Stefan Junk. **Local limit theorem for directed polymers beyond the $L^2$-phase**. arXiv:2307.05097, first posted 2023-07-11T08:11:22Z, version returned http://arxiv.org/abs/2307.05097v3. Abstract: We consider the directed polymer model in the weak disorder phase under the assumption that the partition function is $L^p$-bounded for some $p>1+\frac{2}d$. We prove that the point-to-point partition function can be approximated by two point-to-plane partition functions at the startpoint and endpoint, and in particular that it is $L^p$-bounded as well. Some consequences of this result are also discussed, the most important of which is a local limit theorem for the polymer measure. We furthermore show that the required $L^p$-boundedness holds for some range of $β$ beyond the $L^2$-critical point, and in the whole interior of the weak disorder phase for environments with finite support.

- Stefan Junk. **Stability of weak disorder phase for directed polymer with applications to limit theorems**. arXiv:2105.04082, first posted 2021-05-10T02:44:35Z, version returned http://arxiv.org/abs/2105.04082v2. Abstract: We study the directed polymer model in a bounded environment with bond disorder and show that, in the interior of the weak disorder phase, weak disorder continues to hold upon perturbation by a small bias. Using this stability result, we give a new proof for the central limit theorem (CLT) in probability for the directed polymer model in the interior of the weak disorder phase. We also show that the large deviation rate function agrees with that of the underlying random walk. For the Brownian polymer model, we improve the convergence in the CLT to almost sure convergence in the whole weak disorder phase. The main technical tools are a new moment bound from \cite{J21_1} and a quantitative comparison between the associated martingales at different inverse temperatures.

Primary pre-source theorem: Vincent Vargas, A local limit theorem for directed polymers in random media: the continuous and the discrete case. Annales de l'Institut Henri Poincar?, Probabilit?s et Statistiques 42(5) (2006), 521?534. DOI 10.1016/j.anihpb.2005.08.002. Theorem 2.9 supplies the L2 Brownian Poisson bridge factorization. This is a special case known before the conjecture, not a later solution.

Junk, arXiv:2307.05097v3 (2 July 2025), Local limit theorem for directed polymers beyond the L2-phase, DOI 10.4171/JEMS/1650: PDF pp.1?3 explicitly use simple random walk and i.i.d. lattice site disorder. The sufficient condition is Lp boundedness for p>1+2/d, and the whole interior result uses finite-support environments. This is a strong methodological lead, not a theorem for the Brownian Poisson model.

Junk and Lacoin, arXiv:2502.04113v2 (10 November 2025), Coincidence of critical points for directed polymers for general environments and random walks: PDF p.1 defines walks on Z^d with i.i.d. increments and i.i.d. site variables with all exponential moments. The critical points compared are strong versus very strong disorder, not point-to-point versus point-to-level half-moment thresholds. Neither the model nor the question is identical.

Junk and Lacoin, arXiv:2402.02562: simple-random-walk lattice polymer, upper-bounded site disorder. Strong/very-strong coincidence is a different critical-point question.

Junk, Stability of weak disorder phase for directed polymer with applications to limit theorems, ALEA 20 (2023), DOI 10.30757/ALEA.v20-31, arXiv:2105.04082v2 (10 July 2023): explicitly includes a marked Poisson Brownian model. Its Brownian result (Theorem 2.2, PDF p.5) assumes upper-bounded marks and is an almost-sure central limit theorem, not the bridge local limit theorem or directional half-moment threshold equality. This is a same-model lead whose relevant theorem was inspected. Ordinary weak convergence of endpoint laws does not control point densities.

Cosco, intermediate disorder, arXiv:1804.09571, Indagationes Mathematicae (2019), DOI 10.1016/j.indag.2019.05.004: d=1 with varying parameters and diffusive scaling, not fixed-parameter weak disorder.

Fukushima and Junk, Zero temperature limit for the Brownian directed polymer among Poissonian disasters, Annals of Applied Probability (2019), DOI 10.1214/19-AAP1493, arXiv:1810.09600: existence/continuity of zero-temperature free energy, not this conjecture.

The stable Poisson intermediate-disorder paper arXiv:2401.04459 concerns stable rather than Brownian reference paths and a scaling limit, not this fixed-parameter question.

Cao, Rang and Wu, arXiv:2608.29501 (30 August 2026), Disorder Thresholds and Free Energy of Brownian Directed Polymers with Product and Radial Spatial Correlations: centered Gaussian noise with long-range correlations. Different environment and different critical-point comparison; does not settle the compact-ball Poisson model.

## Search conclusion and limits
No inspected paper states and proves Conjecture 4.3.2 for these same Brownian paths, Poisson environment, both sign branches, and directional half-moment quantifiers. Therefore SOLVED_IN_LITERATURE is not warranted. This is a bounded search, not a proof that no such paper exists. OpenAlex search and citation retrieval were rate-limited (429); initial Semantic Scholar search and source lookup were also rate-limited, but its bulk search and source citation endpoints later succeeded. The initial OpenAlex arXiv-URL cites fallback was not resolved to a work ID. GitHub returned zero repository matches for the recorded query. Read-only origin/master filename inventory had no E0112 or Poisson-polymer named artifact. Successful raw API responses and the local lead PDFs are retained.

- 2026-10-11 Semantic Scholar actual source-record citations: `https://api.semanticscholar.org/graph/v1/paper/2f4612660087fc8bc6b2e71bb2a0bb6a85966c3f/citations?fields=title,year,externalIds&limit=1000`; HTTP 200, 26 bytes.

- 2026-10-11 Semantic Scholar actual source-record citations: `https://api.semanticscholar.org/graph/v1/paper/fed33b144a5f4fdaefa0844cf8089eed0eb15371/citations?fields=title,year,externalIds&limit=1000`; HTTP 200, 3331 bytes.

- 2026-10-11 OpenAlex citations using source MAG identifier from successful Semantic Scholar record (candidate OpenAlex ID W2803566130): `https://api.openalex.org/works?filter=cites:W2803566130&per-page=100`; <HTTPError 429: 'Too Many Requests'>. Candidate ID not verified if request failed.

Semantic Scholar bulk fallback and actual source citations succeeded: correct source paperId fed33b144a5f4fdaefa0844cf8089eed0eb15371, arXiv 1805.10899, MAG 2803566130, CorpusId 119670590. Retrieved 12 citing records; duplicate malformed source record had zero. Full citation metadata retained in search_s2_citations_*.txt. The directly relevant later Poisson Brownian paper in this list is Junk 2105.04082 (CLT, inspected above). Other records concern Gaussian localization, SHE/KPZ, minimal surfaces, or general localization; none is identified here as a bridge half-moment threshold theorem.

## Exact conjecture as TeX from the downloaded source

```tex
\begin{conjecture}
We formulate two conjectures:

$\bullet$ It is natural to define another pair of critical inverse temperature, analogue to the weak/strong disorder transition:
\begin{eqnarray} \label{eq:betacdir}
\overline{\b}_c^{+,{dir}}&=& \sup\{ \b \geq 0: \lim_t \P[ (W_t^{{dir}, \xi})^{1/2}] >0\}, \\ \nn   \overline{\b}_c^{-,{dir}}&=& \inf\{ \b \leq 0: \lim_t \P[ (W_t^{{dir}, \xi})^{1/2}] >0\}.
\end{eqnarray}
Using Jensen inequality  in \eqref{eq:intZ}, it is not difficult to get $\overline{\b}_c^{+,{dir}} \in [\b_2^+,  \b_c^+ ]$, $\overline{\b}_c^{-,{dir}} \in [\b_c^{-}, \b_2^-]$.
We conjecture that %[local extinction does not imply global extension for BBM ??] 
the equality holds, i.e., 
$$\overline{\b}_c^\pm = \overline{\b}_c^{\pm,{dir}}. $$

$\bullet$ A long standing conjecture is that the local limit theorem  \eqref{eq:llt1} holds the way all through the weak disorder region. Note that the latter conjecture would imply that the former one holds.
\end{conjecture}
```

Primary normalization checked: Vargas Theorem 2.9, PDF pp.6?7, printed pp.526?527, uses e_(s,t)=exp(beta eta(V_(s,t))-lambda(beta)(t-s)), and P^x(e_(0,t) | B_t=y). Thus the required normalized bridge factorization is explicitly present in the primary paper; the survey Z display omits the normalization.

Additional source context: source_ch-WSD.tex, section Relations between the different critical temperatures, already states that all three negative critical points are -infinity at sufficiently small nu r^(d+2). Thus ATTEMPT.md section 5a is an explicit sufficient-constant derivation and a directional-threshold special case, not a novelty claim. The d=1,2 remark states thresholds are zero, but points to similar-model proofs and an unpublished Bertin reference; this attempt does not present that remark as an independently verified full proof for the Poisson Brownian model.

The exact corrected open target remains equality of the BARRED weak-disorder thresholds for P2P and P2L, on both sign branches at arbitrary nu>0,r>0,d. No exact-model full theorem was found among the inspected sources.

## Second-attempt brain queries (2026-10-11, read only)

math_recall.py: "Junk local limit theorem polymer beyond L2 p 1 2 d Poisson Brownian factorization"; "weak disorder Brownian bridge heat kernel Harnack stochastic exponential uniform integrability"; "Hellinger affinity conditional expectation Jensen deficit polymer planted environment uniform integrability"; "Poisson Ornstein Uhlenbeck thinning hypercontractivity reverse hypercontractivity". The first two returned generic bridge, limit and UI cards, not a gap-closing theorem. The third returned Hellinger normalization card claim_c91e26a9422d275062ca29a4c8a54230fd0f671cc71605d2c0746ba089bd5322 and conditional expectation definitions; the fourth returned general Gaussian/Boolean hypercontractivity cards. None states a suitable Brownian Poisson bridge bound. In particular a withdrawn stable-process heat-kernel card returned by the second query was not used. All new identities are proved directly in SECOND_ATTEMPT.md, not attributed as literature solutions.

- 2026-10-11 further gap-specific math-store recall: "Comets Yoshida Poisson polymer pinned Brownian bridge weighted overlap weak disorder integral". No matching pinned-overlap theorem. Returned unrelated draft criteria and unreviewed chaos reduction were not used. No new external literature solution is asserted in the second attempt.
