# Literature and status searches

Date for every search below: 2026-10-12. All requests used Python urllib from the shell; no built-in web search was used.

## Exact source

Leonid Petrov (organizer), Axel Saenz (organizer), Evan Sorensen (moderator), Hieu Trung Vu (scribe), **AIM Workshop: All roads to KPZ Universality Open Problems**, March 19, 2025, Section 3, PDF page 2. URL: https://lpetrov.cc/LaTeX/2025-03-19-AIM-KPZ/2025-03-19-AIM-KPZ.pdf. Saved as source.pdf and extracted as source.txt.

Verbatim problem paragraph:

> Consider continuous-time TASEP with step initial condition. There is an associated transition probability function f(a) into the configuration a. A question arises whether f(a) is log-concave. While log-concavity appears in many probabilistic models, it remains unclear how to establish it in this context. The motivation includes connections to symmetric functions.

The preceding paragraph defines f(a)f(b)<=f((a+b)/2)^2 and explicitly allows vector or matrix arguments. The source does not explicitly specify finite n, jump-rate normalization, or lattice rounding. This attempt uses the finite n, integral-midpoint interpretation stipulated by the intake; rates are normalized to one (a common positive rate is absorbed into time). The separate follow-up Q2 PDF was not successfully located; the two guessed filenames and the AIM landing page returned 403. No assertion is made about its current contents.

## Search ledger

- **Source/related source fetch**; request/query: `https://lpetrov.cc/LaTeX/2025-03-19-AIM-KPZ/2025-03-19-AIM-KPZ.pdf`; outcome: [200, 177176]; local response: source.pdf.
- **arXiv**; request/query: `https://export.arxiv.org/api/query?search_query=all%3ATASEP%20AND%20%28all%3A%22log%20concavity%22%20OR%20all%3Alog-concavity%29&max_results=30`; outcome: [200, 790]; local response: arxiv.xml.
- **OpenAlex**; request/query: `https://api.openalex.org/works?search=TASEP%20log%20concavity&per-page=30`; outcome: ['HTTP Error 429: Too Many Requests']; local response: not saved (request failed).
- **Crossref**; request/query: `https://api.crossref.org/works?query=TASEP%20log%20concavity&rows=30`; outcome: [200, 227665]; local response: crossref.json.
- **Semantic Scholar**; request/query: `https://api.semanticscholar.org/graph/v1/paper/search?query=TASEP%20log%20concavity&limit=30&fields=title,authors,year,abstract,url`; outcome: ['HTTP Error 429: ']; local response: not saved (request failed).
- **GitHub**; request/query: `https://api.github.com/search/repositories?q=TASEP%20log%20concavity`; outcome: [200, 55]; local response: github.json.
- **OpenAlex**; request/query: `https://api.openalex.org/works?search=All%20roads%20to%20KPZ%20universality&per-page=10`; outcome: ['HTTP Error 429: Too Many Requests']; local response: not saved (request failed).
- **arXiv**; request/query: `https://export.arxiv.org/api/query?search_query=all%3A%22log-concavity%22%20AND%20%28all%3Aexclusion%20OR%20all%3ATASEP%20OR%20all%3A%22Schur%20process%22%29&max_results=40`; outcome: [200, 8173]; local response: arxiv_broad.xml.
- **arXiv**; request/query: `https://arxiv.org/pdf/2412.15116`; outcome: [200, 519728]; local response: bkm.pdf.
- **Source/related source fetch**; request/query: `https://lpetrov.cc/2025/03/AIM-KPZ/`; outcome: ['HTTP Error 403: Forbidden']; local response: not saved (request failed).
- **OpenAlex**; request/query: `https://api.openalex.org/works?search=TASEP%20log-concavity&per_page=10`; outcome: ['HTTP Error 429: Too Many Requests']; local response: not saved (request failed).
- **Semantic Scholar**; request/query: `https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=TASEP%20log-concavity&fields=title,year,authors,url`; outcome: [200, 40]; local response: semantic_retry.json.
- **arXiv**; request/query: `https://arxiv.org/pdf/0804.3035`; outcome: [200, 1191857]; local response: bf.pdf.
- **arXiv**; request/query: `https://arxiv.org/pdf/1911.04392`; outcome: [200, 179892]; local response: hks.pdf.
- **arXiv**; request/query: `https://export.arxiv.org/api/query?search_query=ti%3A%22Discrete%20variants%20of%20Brunn%20Minkowski%22&max_results=5`; outcome: [200, 1861]; local response: arxiv_hks.xml.
- **arXiv**; request/query: `https://export.arxiv.org/api/query?search_query=all%3A%22TASEP%22%20AND%20all%3A%22Gelfand%22&max_results=15`; outcome: [200, 10119]; local response: arxiv_gt.xml.
- **Source/related source fetch**; request/query: `https://lpetrov.cc/LaTeX/2025-03-19-AIM-KPZ/`; outcome: ['HTTP Error 403: Forbidden']; local response: not saved (request failed).
- **arXiv**; request/query: `https://export.arxiv.org/api/query?search_query=all%3ATASEP%20AND%20all%3Aconcavity%20AND%20submittedDate%3A%5B202503190000%20TO%20202610122359%5D&max_results=40`; outcome: [200, 832]; local response: arxiv_recent.xml.
- **Crossref**; request/query: `https://api.crossref.org/works?query.bibliographic=TASEP%20transition%20log%20concavity&filter=from-pub-date:2025-03-19&rows=20`; outcome: [200, 206304]; local response: crossref_target.json.
- **OpenAlex**; request/query: `https://api.openalex.org/works?filter=title.search:All%20roads%20to%20KPZ&per-page=5`; outcome: ['HTTP Error 429: Too Many Requests']; local response: not saved (request failed).
- **GitHub**; request/query: `https://api.github.com/search/repositories?q=TASEP%20concavity`; outcome: [200, 55]; local response: github_broad.json.
- **Semantic Scholar**; request/query: `https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=TASEP%20log%20concavity&year=2025-&fields=title,year,authors,url`; outcome: [200, 40]; local response: semantic_recent.json.
- **Source/related source fetch**; request/query: `https://lpetrov.cc/LaTeX/2025-03-19-AIM-KPZ/2025-03-19-AIM-KPZ-followup.pdf`; outcome: ['HTTP Error 403: Forbidden']; local response: not saved (request failed).
- **Source/related source fetch**; request/query: `https://lpetrov.cc/LaTeX/2025-03-19-AIM-KPZ/2025-03-19-AIM-KPZ-follow-up.pdf`; outcome: ['HTTP Error 403: Forbidden']; local response: not saved (request failed).
- **Source/related source fetch**; request/query: `https://aimath.org/workshops/upcoming/roadstokpz/`; outcome: ['HTTP Error 403: Forbidden']; local response: not saved (request failed).

OpenAlex source discovery repeatedly returned HTTP 429, so no source work ID could be obtained and works citing the source could not be enumerated. This is an explicit incomplete part of the requested literature screen, not a negative citation search. Semantic Scholar search first returned 429, but both subsequent bulk searches succeeded with zero records. GitHub returned zero repositories for both query variants. The recent arXiv query was date-filtered from 2025-03-19 through 2026-10-12; the broader query is noisy and recovered four unrelated papers. Crossref is a ranked relevance search, not a proof of absence.

## Relevant established results (leads, not a solution in print)

1. Alexei Borodin and Patrik L. Ferrari, **Anisotropic growth of random surfaces in 2+1 dimensions**, Communications in Mathematical Physics 325, 603-684 (2014), arXiv:0804.3035, https://arxiv.org/abs/0804.3035. Saved bf.pdf/bf.txt. Section 1.1, PDF pp.3-5 gives the push/block array and its TASEP left edge; equation (2.101), PDF p.37, gives the row transition law; Proposition 2.22, PDF p.38, gives evolution of the Gibbs-form array law. These establish the representation used in PROOF.md, but do not state the target log-concavity theorem.

2. Diana Halikias, Boaz Klartag, and Boaz A. Slomka, **Discrete variants of Brunn-Minkowski type inequalities**, Annales de la Faculte des Sciences de Toulouse, Serie 6, 30(2), 267-279 (2021), arXiv:1911.04392v4, https://arxiv.org/abs/1911.04392. Saved hks.pdf/hks.txt. Theorem 1.2, PDF p.1, is the discrete four-functions inequality. Its lambda=1/2 specialization implies preservation of rounded-midpoint log-concavity under coordinate sums. It does not state a TASEP theorem.

3. Jnaneshwar Baslingker, Manjunath Krishnapur, and Mokshay Madiman, **Log-concavity in one-dimensional Coulomb gases and related ensembles**, arXiv:2412.15116 (2024), https://arxiv.org/abs/2412.15116. Saved bkm.pdf/bkm.txt. Theorem 5, PDF p.7, states: "Assume that ai >= 0 and bi >= 0 for all i. All one dimensional marginals of the Schur measure Pa,b are discrete log-concave." Mathematical typesetting has been transcribed to ASCII; this is not an exact-target theorem. Result 6 and Corollary 4, PDF p.9, explain the HKS inequality and coordinate marginalization. This paper predates the workshop and suggests the method, but its Schur top-row marginals are not the TASEP configuration vector.

## Searches of the read-only research brain and previous work

- math_recall.py "TASEP log concavity": recovered the open-question card and claim_9474f26809f486972f89dbb365b1e60f75645b39b522942d7a593cf49aa48428 (earlier n=1 proof; independent particles do not represent TASEP).
- brain.py recall "TASEP mistakes" and "TASEP transition log concavity": no relevant mathematical memory recovered; the latter reported low separation between unrelated hits.
- math_recall.py "discrete Prekopa Leindler interlacing Schur TASEP": interlacing/Schur leads, no exact theorem.
- Intake ledger search: Python globbed probability_1000_intake_* and checked top-level problems.jsonl, attempts.jsonl and sources.jsonl for P0281, with no matching lines in files found in that bounded layout. An initial PowerShell rg wildcard request failed because the wildcard directory was not expanded.
- Read-only git ls-tree origin/master, filtered to P0281, then git show of operations/claims/P0281.md and the September 18-19 artifact notes/outputs. These preserved earlier exact ballot checks and joint clock-kernel checks. They do not give an all-n solution. Copies read are stored as prior_*.md / prior_*.out in this folder; no repository was modified.

## Status conclusion

No inspected paper states and proves this exact finite-particle TASEP configuration log-concavity question. Accordingly this work is NOT classified SOLVED_IN_LITERATURE. PROOF.md derives a positive answer by combining two established ingredients with a checked weight inequality. Search limitations prevent a claim of certified novelty or exhaustive worldwide openness.

### arxiv.xml: returned total 0

### arxiv_broad.xml: returned total 4
- Sampling the Fermi statistics and other conditional product measures; http://arxiv.org/abs/0911.4565v2
- On the excedance sets of colored permutations; http://arxiv.org/abs/0806.2114v1
- Negative dependence and the geometry of polynomials; http://arxiv.org/abs/0707.2340v2
- Blocked Gibbs sampler for hierarchical Dirichlet processes; http://arxiv.org/abs/2304.09945v2

### arxiv_recent.xml: returned total 0

### arxiv_gt.xml: returned total 5
- Limits of Multilevel TASEP and similar processes; http://arxiv.org/abs/1206.3817v1
- On the Martin boundary for discrete TASEP; http://arxiv.org/abs/2510.23430v2
- Fluctuations for stationary $q$-TASEP; http://arxiv.org/abs/1701.05991v2
- Pfaffian Transition Probability and Correlation Kernel of TASEP in Half-space; http://arxiv.org/abs/2512.02286v1
- A q-weighted version of the Robinson-Schensted algorithm; http://arxiv.org/abs/1212.6716v2

### arxiv_hks.xml: returned total 1
- Discrete variants of Brunn-Minkowski type inequalities; http://arxiv.org/abs/1911.04392v4

### crossref.json: all returned bibliographic items
- ['Log-concavity and strong log-concavity: A review']; DOI 10.1214/14-ss107; published {'date-parts': [[2014, 1, 1]]}
- ['Beyond Log-Concavity: Theory and Algorithm for Sum-Log-Concave Optimization']; DOI 10.21203/rs.3.rs-3380863/v1; published {'date-parts': [[2023, 9, 27]]}
- ['Beyond Log-Concavity: Theory and Algorithm for Sum-Log-Concave Optimization']; DOI 10.21203/rs.3.rs-3380863/v2; published {'date-parts': [[2023, 9, 27]]}
- ['Log-convexity and log-concavity of noncentral gamma sums and differences']; DOI 10.2139/ssrn.7356175; published {'date-parts': [[2026]]}
- ['Unimodality, log-concavity, and log-convexity']; DOI 10.1201/9781315122656-4; published {'date-parts': [[2019, 8, 19]]}
- ['Additive Augmentation Gaps Do Not Force Log-Concavity']; DOI 10.2139/ssrn.7434141; published {'date-parts': [[2026]]}
- ['Log-concavity of genus distributions for circular ladders']; DOI 10.1002/mana.201400229; published {'date-parts': [[2015, 7, 6]]}
- ['q-log-distributions: Log-concavity and log-convexity']; DOI 10.1140/epjp/i2018-12005-3; published {'date-parts': [[2018, 4]]}
- ['Unimodality, Log-concavity, Real-rootedness And Beyond']; DOI 10.1201/b18255-13; published {'date-parts': [[2015, 3, 24]]}
- ['Log-Concavity and Log-Convexity via Distributive Lattices']; DOI 10.1007/s11083-026-09735-2; published {'date-parts': [[2026, 5, 2]]}
- ['On the Log-Concavity of the Riemann Xi Kernel']; DOI 10.20944/preprints202604.0159.v2; published {'date-parts': [[2026, 6, 29]]}
- ['On the Log-Concavity of the Riemann Xi Kernel']; DOI 10.20944/preprints202604.0159.v1; published {'date-parts': [[2026, 4, 2]]}
- ['Homogeneity, Returns to Scale and (Log)Concavity']; DOI 10.2139/ssrn.3643322; published {'date-parts': [[2020]]}
- ['Log-concavity and Stock-monotone Allocation in the Bomber Problem']; DOI 10.2139/ssrn.7252938; published {'date-parts': [[2026]]}
- ['Restricted partition functions and the r-log-concavity of quasi-polynomial-like functions']; DOI 10.21203/rs.3.rs-2880181/v1; published {'date-parts': [[2023, 5, 11]]}
- ['Distinguishing Log-Concavity from Heavy Tails']; DOI 10.3390/risks5010010; published {'date-parts': [[2017, 2, 7]]}
- ['Rank-unimodality and tail log-concavity of composition ideals']; DOI 10.2139/ssrn.7385218; published {'date-parts': [[2026, 9, 3]]}
- ['Log-concavity, ultra-log-concavity, and a maximum entropy property of discrete compound Poisson measures']; DOI 10.1016/j.dam.2011.08.025; published {'date-parts': [[2013, 6]]}
- ['Preserving log-concavity and generalized triangles']; DOI 10.1063/1.3478183; published {'date-parts': [[2010]]}
- ['Bell Numbers, Log-Concavity, and Log-Convexity']; DOI 10.1007/978-94-010-0842-6_4; published {'date-parts': [[2001]]}
- ['Relative log-concavity and a pair of triangle inequalities']; DOI 10.3150/09-bej216; published {'date-parts': [[2010, 5, 1]]}
- ['Equivariant log-concavity of graph matchings']; DOI 10.5802/alco.284; published {'date-parts': [[2023, 6, 19]]}
- ['On the log-concavity of the n-th root of a sequence']; DOI 10.21203/rs.3.rs-2352868/v1; published {'date-parts': [[2022, 12, 12]]}
- ['Bell Numbers, Log-Concavity, and Log-Convexity']; DOI 10.1023/a:1010738827855; published {'date-parts': [[2000, 9]]}
- ['Preservation of log-concavity on linear transformations']; DOI 10.1016/j.disc.2026.115083; published {'date-parts': [[2026, 7]]}
- ['Q-analogue of a linear transformation preserving Log-concavity']; DOI 10.12988/ija.2007.07011; published {'date-parts': [[2007]]}
- ['Log-concavity and symplectic flows']; DOI 10.4310/mrl.2015.v22.n2.a9; published {'date-parts': [[2015]]}
- ['Inductive proofs of q-log concavity']; DOI 10.1016/0012-365x(92)90377-r; published {'date-parts': [[1992, 4]]}
- ['Log-convexity and log-concavity of hypergeometric-like functions']; DOI 10.1016/j.jmaa.2009.10.057; published {'date-parts': [[2010, 4]]}
- ['Posterior probabilities: Nonmonotonicity, asymptotic rates, log-concavity, and Turán’s inequality']; DOI 10.3150/21-bej1398; published {'date-parts': [[2022, 5, 1]]}

### crossref_target.json: all returned bibliographic items
- ['Log-convexity and log-concavity of noncentral gamma sums and differences']; DOI 10.2139/ssrn.7356175; published {'date-parts': [[2026]]}
- ['Additive Augmentation Gaps Do Not Force Log-Concavity']; DOI 10.2139/ssrn.7434141; published {'date-parts': [[2026]]}
- ['Log-Concavity and Log-Convexity via Distributive Lattices']; DOI 10.1007/s11083-026-09735-2; published {'date-parts': [[2026, 5, 2]]}
- ['On the Log-Concavity of the Riemann Xi Kernel']; DOI 10.20944/preprints202604.0159.v2; published {'date-parts': [[2026, 6, 29]]}
- ['On the Log-Concavity of the Riemann Xi Kernel']; DOI 10.20944/preprints202604.0159.v1; published {'date-parts': [[2026, 4, 2]]}
- ['Log-concavity and Stock-monotone Allocation in the Bomber Problem']; DOI 10.2139/ssrn.7252938; published {'date-parts': [[2026]]}
- ['Rank-unimodality and tail log-concavity of composition ideals']; DOI 10.2139/ssrn.7385218; published {'date-parts': [[2026, 9, 3]]}
- ['Log-concavity and log-convexity of restricted infinite products']; DOI 10.1142/s1793042127500023; published {'date-parts': [[2026, 9, 10]]}
- ['Preservation of log-concavity on linear transformations']; DOI 10.1016/j.disc.2026.115083; published {'date-parts': [[2026, 7]]}
- ['Log-Concavity and the Multiplicative Properties of Restricted Partition Functions']; DOI 10.1007/s00026-026-00847-5; published {'date-parts': [[2026, 9, 29]]}
- ['Log-Concavity and Strong\n            <i>q</i>\n            -Log-Convexity for Some Generalized Triangular Arrays']; DOI 10.1080/00150517.2024.2435332; published {'date-parts': [[2025, 7, 21]]}
- ['Shuffle Tableaux, Littlewood–Richardson Coefficients, and Schur Log-Concavity']; DOI 10.5802/alco.502; published {'date-parts': [[2026, 9, 2]]}
- ['A Combinatorial Method for Log-Concavity of Rows of Triangular Arrays']; DOI 10.37236/15031; published {'date-parts': [[2026, 8, 28]]}
- ['Log-concavity of cluster algebras of type \n$A_n$']; DOI 10.1017/nmj.2026.10110; published {'date-parts': [[2026]]}
- ['Ultra Log-Concavity and Real-Rootedness of Dependence Polynomials']; DOI 10.37236/13310; published {'date-parts': [[2026, 10, 9]]}
- ['Sharp One-Dimensional Rényi–Costa Concavity for Log-Concave Densities']; DOI 10.1109/tit.2026.3735910; published {'date-parts': [[2026]]}
- ['Log-concavity and anti-maximum principles for semilinear and linear elliptic equations']; DOI 10.5802/crmath.810; published {'date-parts': [[2025, 12, 12]]}
- ['Complex zeros, unimodality and log-concavity in independent domination polynomial of zero divisor graphs']; DOI 10.1016/j.tcs.2025.115594; published {'date-parts': [[2025, 12]]}
- ['INJECTIVE PROOFS OF LOG CONCAVITY FOR SOME COMBINATORIAL SEQUENCES']; DOI 10.1007/s10958-026-08365-8; published {'date-parts': [[2026, 3]]}
- ['Log-concavity of the Grothendieck classes of banana graphs and clasped necklaces']; DOI 10.1016/j.geomphys.2025.105666; published {'date-parts': [[2025, 12]]}
