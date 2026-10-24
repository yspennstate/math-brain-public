# Literature check - 2026-10-11

## Status and exact source statement

No paper proving the complete posed inequality was identified. This is a bounded, incomplete search, not a certification that no solution exists. In particular, OpenAlex and Semantic Scholar returned HTTP 429 on every attempted request. An OpenAlex work identifier could not be resolved, so a valid cited-work-ID citation search could not be completed; the logged URL-based `cites` attempt is not evidence about the citation list. The broad post-April arXiv query returned 100 entries and was capped; two narrower follow-up queries are logged below.

Pritish Kamath, Ravi Kumar and Pasin Manurangsi, *When Majority Fails: Tight Bounds for Correlation Distillation Conjectures*, arXiv:2604.06590v1, 8 April 2026, Section 1.4, Conjecture 1, PDF p.4. Exact words, with mathematical typesetting transcribed:

> Conjecture 1 (Refined MLS (Gopi, 2013)). For all ρ ∈ (0, 1), odd n, and unbiased LTF f : {−1, 1}ⁿ → {−1, 1}, it holds that Stabρ(f) ≥ 2/π arcsin(ρ).

The p.2 definition is a homogeneous threshold `sign(sum_i w_i x_i)` and the noise model is the uniform doubly symmetric binary source with coordinate correlation ρ. Adding an unused coordinate handles even dimension. The earlier finite-majority conjecture is distinct and false. The source also proves a special near-one finite-majority comparison in Theorem 10, PDF pp.5–6, and the three-variable case in Theorem 11, PDF p.6; these are leads/special cases, not solutions to Conjecture 1.

## Relevant references and assessment

- Sivakanth Gopi, *Stability of Linear Threshold Functions*, B.Tech. project, Indian Institute of Technology Bombay, 2013; downloaded from the URL logged below. Section 3.3, Conjecture 3, printed p.18 / PDF p.21, states the arcsine conjecture. Section 3.4 gives evidence, not a general proof. Theorem 13, printed p.18 / PDF pp.21–22, proves the majority special case. Caution: the displayed five-variable majority polynomial in Section 3.2 has incorrect coefficients (it gives the two-edge-star spectrum); our independent calculation and Lean check use the correct majority spectrum `(45,10,9)/64`.
- Vishesh Jain, *A Counterexample to the “Majority is Least Stable” Conjecture*, arXiv:1703.07657v2, 23 March 2017, PDF p.1. It computes `W1=44/64` for `sign(2x1+2x2+x3+x4+x5)` versus `45/64` for majority. It refutes only the finite-majority comparison, not the arcsine bound. The local fetch filename `gopi_pdf.pdf` is a misleading historical label: the downloaded paper is Jain's.
- Ryan O'Donnell, *Analysis of Boolean Functions*, Barbados Workshop lecture notes, scribed by Li-Yang Tan (guest lecture by Per Austrin), arXiv:1205.0314v1, 2 May 2012. This attempted background fetch is not the supplied unspecified “O'Donnell 2012 p.5” locator: its p.5 contains Plancherel and expectation/variance formulas. It provides background on thresholds, majority and invariance, but does not verify that locator. The intended 2012 reference remains unresolved; it is not evidence of a solution.
- Xuan Fang and Tianyu Wang, *A Two-regime Khintchine Inequality and an Improved Bound on the Degree-1 Fourier Weight for Linear Threshold Functions*, arXiv:2608.27908v1, 28 August 2026. Theorem 4, PDF p.21, proves `W^{<=1}[LTF] >= (1/sqrt(2)+277/12000)^2 > 0.53317`. The introduction still formulates `2/pi` as a conjectured lower bound. For balanced functions the degree-zero weight vanishes. Even the stronger conjectural degree-one estimate alone would not supply the full arcsine inequality at every correlation. Thus this is a post-source lead, explicitly not `SOLVED_IN_LITERATURE`.
- Anindya De, Ilias Diakonikolas and Rocco A. Servedio, *A robust Khintchine inequality, and algorithms for computing optimal constants in Fourier analysis and high-dimensional geometry*, SIAM Journal on Discrete Mathematics 30(2) (2016), 1058–1094; cited by the Fang–Wang paper as earlier quantitative progress. No claim here that it proves the arcsine inequality.
- Elchanan Mossel, Ryan O'Donnell and Krzysztof Oleszkiewicz, *Noise stability of functions with low influences: invariance and optimality*, Annals of Mathematics 171(1) (2010), 295–341, arXiv:math/0503503. Brain recall lead; low-influence Gaussian limiting comparisons do not prove the conjectured lower bound for arbitrary thresholds.

## Search screening and local recall

All online requests below were run on 2026-10-11 through Python urllib from the shell. Successful responses are retained locally. Crossref title/keyword results did not identify the source or an exact later solution. Both GitHub repository searches returned zero repositories. The arXiv exact-title search identified the source's v1; the refined-MLS/least-stable query found the source and earlier finite-majority papers among many unrelated results. The broad later-title search revealed the Fang–Wang lead. `arxiv_after_screened.txt` retains its returned titles and abstracts.

Before and during the attempt, read-only math-store queries on unbiased thresholds/noise stability/Khintchine, and brain recalls on the topic and mistakes, were used. The earlier P0164 ledger only proved `rho/3`. Local intake and 2026-10-10 pool searches and a filtered `origin/master` filename listing did not reveal a complete answer. No brain, ledger, repository or external record was modified.

## Full online request log

- source_pdf: https://arxiv.org/pdf/2604.06590 -- ok
- arxiv: https://export.arxiv.org/api/query?search_query=all%3A%22noise%20stability%22%20AND%20%28all%3Athreshold%20OR%20all%3A%22When%20Majority%20Fails%22%29&start=0&max_results=40&sortBy=submittedDate&sortOrder=descending -- ok
- openalex: https://api.openalex.org/works?search=When%20Majority%20Fails&per-page=20 -- HTTP Error 429: Too Many Requests
- crossref: https://api.crossref.org/works?query=Gaussian%20lower%20bound%20noise%20stability%20unbiased%20thresholds&rows=20 -- ok
- semantic: https://api.semanticscholar.org/graph/v1/paper/ARXIV:2604.06590?fields=title,authors,year,citations.title,citations.externalIds,citations.year -- HTTP Error 429: 
- github: https://api.github.com/search/repositories?q=%22noise%20stability%22%20threshold -- ok

- arxiv_title: https://export.arxiv.org/api/query?search_query=ti:%22When%20Majority%20Fails%22&max_results=10 -- ok
- arxiv_refined: https://export.arxiv.org/api/query?search_query=all%3A%22Refined%20MLS%22%20OR%20all%3A%22least%20stable%22%20OR%20all%3A%222604.06590%22&max_results=40&sortBy=submittedDate&sortOrder=descending -- ok
- openalex_retry: https://api.openalex.org/works?search=2604.06590&per-page=5 -- HTTP Error 429: Too Many Requests
- openalex_citing: https://api.openalex.org/works?filter=cites:https://arxiv.org/abs/2604.06590&per-page=30 -- HTTP Error 429: Too Many Requests
- crossref_title: https://api.crossref.org/works?query.title=When%20Majority%20Fails&rows=10 -- ok
- semantic_search: https://api.semanticscholar.org/graph/v1/paper/search?query=When%20Majority%20Fails&limit=10&fields=title,year,externalIds -- HTTP Error 429: 
- github_title: https://api.github.com/search/repositories?q=%22When%20Majority%20Fails%22 -- ok
- gopi_pdf: https://arxiv.org/pdf/1703.07657 -- ok

- arxiv_after: http://export.arxiv.org/api/query?search_query=%28ti%3A%22noise%20stability%22%20OR%20ti%3A%22threshold%20functions%22%20OR%20ti%3A%22majority%22%29%20AND%20submittedDate%3A%5B202604080000%20TO%20202610112359%5D&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending -- ok
- openalex_title_alt: https://api.openalex.org/works?search=When%20Majority%20Fails&per_page=5 -- HTTP Error 429: Too Many Requests
- gopi_thesis: https://gopisivakanth.github.io/files/UndergraduateThesis_IITBombay.pdf -- ok
- odonnell_2012: https://arxiv.org/pdf/1205.0314 -- ok

- Lead PDF fetch, 2026-10-11: https://arxiv.org/pdf/2608.27908; see khintchine_2026.txt.

- arxiv_noise_after (2026-10-11): https://export.arxiv.org/api/query?search_query=ti%3A%22noise%20stability%22%20AND%20submittedDate%3A%5B202604080000%20TO%20202610112359%5D&max_results=100&sortBy=submittedDate&sortOrder=descending -- HTTP Error 429: Too Many Requests
- arxiv_ltf_after (2026-10-11): https://export.arxiv.org/api/query?search_query=%28all%3A%22linear%20threshold%22%20AND%20%28all%3Astability%20OR%20all%3AKhintchine%20OR%20all%3Aarcsin%29%29%20AND%20submittedDate%3A%5B202604080000%20TO%20202610112359%5D&max_results=100&sortBy=submittedDate&sortOrder=descending -- The read operation timed out


## Second attempt, 2026-10-11: gap-specific brain queries

- math_recall.py: `Rademacher sums random partition absolute value noise stability arcsin linear threshold`.
- math_recall.py: `Esseen Kolmogorov Rogozin concentration function small ball Rademacher`.

These read-only searches returned the earlier P0164 record, Fourier/noise definitions, Rademacher/Hoeffding facts, and Esseen/Kolmogorov-Rogozin concentration cards. Relevant recalled references: C. G. Esseen, *On the Kolmogorov-Rogozin inequality for the concentration function*, Z. Wahrscheinlichkeitstheorie verw. Gebiete 5 (1966), 210-216, DOI 10.1007/BF00533057; C. G. Esseen, *On the concentration function of a sum of independent random variables*, same journal 9 (1968), 290-308, DOI 10.1007/BF00531753; V. V. Petrov, *Sums of Independent Random Variables*, Springer, 1975. Originals were not newly fetched: these are memory leads only. Their concentration estimates do not prove the sharp pivotal-slab comparison. No new online literature solution is claimed by this continuation; its progress is the exact six-variable finite result.
