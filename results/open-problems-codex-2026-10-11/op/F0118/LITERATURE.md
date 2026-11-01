# F0118 literature check — 12 October 2026

Second-attempt brain queries, 12 October 2026: `math_recall.py "Potts reconstruction symmetric posterior laws Blackwell comparison alphabet monotonicity Mossel Peres"`; `math_recall.py "Blackwell order symmetric binary experiments convex order posterior bias Potts reconstruction"`; `math_recall.py "Strassen martingale coupling convex order Blackwell Sherman Stein comparison experiments"`. The first two yielded no directly applicable theorem. The last returned the ordinary stochastic-order coupling card (`claim_d4ceae7714f94e59a9363adaaf91efab`) and Volker Strassen, *The existence of probability measures with given marginals* (1965), DOI 10.1214/aoms/1177700153 (`source_875c9cf98717b8c1b29752e022bea64e49a32bf2815b0362f25f4f5535e4b289`). The recalled ordinary-order theorem is not the convex-order/martingale theorem needed here. The finite convex-order-to-garbling statement was proved directly using finite linear separation in SECOND_ATTEMPT.md, so neither card is treated as proof. No new external paper is claimed to solve F0118.

## Status
No retrieved paper states and proves Mossel's full Conjecture 4 with arbitrary fixed integer q1<q2, the same positive eigenvalue, and the same b-ary tree. This is a bounded negative search result, not a claim that the problem is definitely still open. **Not SOLVED_IN_LITERATURE.** OpenAlex source and citation lookups were blocked by HTTP 429; Semantic Scholar searches were rate-limited and direct source identifiers returned 404. These limitations are material.

## Source verified directly
Elchanan Mossel, **Survey: Information flow on trees**, DIMACS Series in Discrete Mathematics and Theoretical Computer Science 63 (2004), DOI **10.1090/dimacs/063/12**, arXiv **math/0406446v1**. Download: https://arxiv.org/pdf/math/0406446 . Cached PDF: `mossel_pdf.raw`; extracted text: `mossel.txt`.

PDF page 10, Section 5.2, gives:

> Conjecture 4. Consider two symmetric channels M1 and M2 (as in (8)) on q1 and q2 symbols respectively, where q1 < q2. If 0 < λ2(M1) = λ2(M2) and the reconstruction problem is solvable for M1, then it is also solvable for M2.

The following sentences state the divisible case and q1=2 case as known. Section 2, PDF page 2, defines λ2(M) as **the eigenvalue** having second largest absolute value (possibly complex), not the nonnegative absolute value itself. Thus the positive hypothesis selects ferromagnetic channels. Ergodicity excludes λ=1. Equation (8), Section 5, PDF page 7, gives Mii=1-(q-1)ε and Mij=ε for i≠j; the displayed eigenvalue is 1-qε. For this question ε=(1-λ)/q and Mq=λI+(1-λ)J/q. The b-ary tree is the common tree in the surrounding setting. Proposition 2.1, PDF page 3, permits uniform-root mutual-information and posterior formulations.

The source's Theorem 3.1, PDF page 4, says binary reconstruction holds if and only if bλ²>1, including non-reconstruction at equality. Theorem 4.1, PDF page 6, gives the strict census inequalities and leaves its equality case unstated. Neither solves the remaining arbitrary-alphabet comparison.

## Main later leads inspected in full text

* Allan Sly, **Reconstruction of symmetric Potts Models**, arXiv **0811.1208v1** (2008); journal version **Reconstruction for the Potts model**, Annals of Probability (2011), DOI **10.1214/10-AOP584**. Download https://arxiv.org/pdf/0811.1208 . Theorems 1.1 and 1.2, PDF page 4: the KS threshold is sharp for q=3 at sufficiently large degree; for q>=5 it is not sharp. Theorem 1.3 gives fixed-q large-degree asymptotics. These assertions do not compare every q1<q2 at a fixed arbitrary degree. Cached `sly.txt`.
* Elchanan Mossel, Allan Sly, Youngtak Sohn, **Exact Phase Transitions for Stochastic Block Models and Reconstruction on Trees**, arXiv **2212.03362v2**, https://arxiv.org/pdf/2212.03362 . Theorem 1.12, PDF page 5, proves KS sharpness for q=3,4 at sufficiently large mean degree under Assumptions 1.10 and 1.11, with non-reconstruction at equality. Theorem 1.13, PDF page 6, concerns failure of KS sharpness. The deterministic-offspring case gives the regular tree. This proves additional special cases by implication, not the posed full conjecture. Cached `mss.txt`.
* Yuzhou Gu, Yury Polyanskiy, **Non-linear Log-Sobolev inequalities for the Potts semigroup and applications to reconstruction problems**, arXiv **2005.05444v2** (2 December 2022), https://arxiv.org/pdf/2005.05444 . Theorems 5 and 6, PDF pages 8–9, give sufficient conditions for non-reconstruction via the uniform-input KL contraction coefficient. A monotone bound, even if available, is not a comparison of the exact thresholds. Cached `gu_polyanskiy.txt`.
* Yuzhou Gu, Yury Polyanskiy, **Uniqueness of BP fixed point for the Potts model and applications to community detection**, arXiv **2303.14688v2**, https://arxiv.org/pdf/2303.14688 . The abstract and main results give BP uniqueness under dλ² >= 1+C max{λ,q^(-1)} log q. Its degradation arguments operate within a common q-alphabet. It does not prove reconstruction monotonicity across all alphabet sizes. Cached `bp.txt`.
* Heon Lee, **Robust Reconstruction on Trees with a Growing Alphabet**, arXiv **2609.33263v1** (27 September 2026), https://arxiv.org/pdf/2609.33263 . Theorem 1.7, PDF page 5, compares noisy and noiseless posteriors in a joint q→∞ and depth kq→∞ limit, under Assumption 1.5; it is not a monotonicity statement for two fixed finite q's. In particular the order of limits cannot be substituted without proof. Cached `growing.txt`.

## Earlier reference and prior attempts

* Elchanan Mossel, Yuval Peres, **Information flow on trees**, Annals of Applied Probability 13(3) (2003), 817–844, DOI **10.1214/aoap/1060202828**, arXiv **math/0107033**. Download https://arxiv.org/pdf/math/0107033 . The retrieved arXiv PDF contains the alphabet monotonicity question as Conjecture 2, Section 8.3, PDF page 23. This is an earlier statement, not a solution. Its positivity wording is not identical to the later survey; we use the later survey's explicit positive hypothesis.
* Read-only intake `probability_1000_intake_F_20260908/problems.jsonl` row F0118 and `attempts.jsonl` F0118-A001 (9 September 2026) identify the independent-recoloring obstruction. It is independently re-proved in ATTEMPT.md using edge covariances. No directly matching file was returned by the filename scan of `origin/master` in the published-answer repository. This is not a repository-wide content-search claim.
* Read-only brain queries: `brain.py recall "Potts reconstruction monotonicity mistakes"`, `brain.py recall "Potts tree reconstruction"`, and `math_recall.py "Potts tree reconstruction Mossel Sly monotonicity"`. Results were largely off-topic. The methodological warning about unjustified monotonicity was retained; no brain card is used as proof.

## Every remote request / search

The following table is generated from `search_log.jsonl`, which records exact URLs and outcomes. All searches were run on **2026-10-12** by Python urllib, without built-in web search. Download requests are included for reproducibility.

| Name / service | Exact URL (query included) | Outcome |
|---|---|---|
| openalex_source | https://api.openalex.org/works?search=Survey%20Information%20flow%20on%20trees&per-page=5 | HTTP Error 429: Too Many Requests |
| openalex_search | https://api.openalex.org/works?search=Potts%20reconstruction%20monotonicity&per-page=30 | HTTP Error 429: Too Many Requests |
| mossel_pdf | https://arxiv.org/pdf/math/0406446 | 200 |
| semantic | https://api.semanticscholar.org/graph/v1/paper/search?query=Potts%20reconstruction&limit=30&fields=title,authors,year,externalIds,url,abstract | HTTP Error 429:  |
| arxiv_https | https://export.arxiv.org/api/query?search_query=all%3APotts%20AND%20all%3Areconstruction&max_results=40 | 200 |
| arxiv_http | http://export.arxiv.org/api/query?search_query=all%3APotts%20AND%20all%3Areconstruction&max_results=40 | 200 |
| github | https://api.github.com/search/repositories?q=Potts%20reconstruction&per_page=20 | 200 |
| crossref | https://api.crossref.org/works?query=Potts%20reconstruction%20monotonicity&rows=25 | 200 |
| semantic_source | https://api.semanticscholar.org/graph/v1/paper/ARXIV:math/0406446?fields=title,year,externalIds,citations.title,citations.year,citations.externalIds | HTTP Error 404: Not Found |
| arxiv_monotone | https://export.arxiv.org/api/query?search_query=all%3Areconstruction%20AND%20%28all%3Amonotonicity%20OR%20all%3Amonotone%29%20AND%20%28all%3APotts%20OR%20all%3AMossel%29&max_results=50 | 200 |
| sly_pdf | https://arxiv.org/pdf/0811.1208 | 200 |
| gu_polyanskiy_pdf | https://arxiv.org/pdf/2005.05444 | 200 |
| arxiv_tree | https://export.arxiv.org/api/query?search_query=all%3APotts%20AND%20%28all%3Atree%20OR%20all%3Atrees%29%20AND%20all%3Areconstruction&max_results=100&sortBy=submittedDate&sortOrder=descending | 200 |
| github_monotone | https://api.github.com/search/repositories?q=Potts%20monotonicity&per_page=20 | 200 |
| openalex_retry | https://api.openalex.org/works?search=Information%20flow%20on%20trees&per_page=5 | HTTP Error 429: Too Many Requests |
| crossref_tree | https://api.crossref.org/works?query=Potts%20reconstruction%20trees%20threshold&rows=35 | 200 |
| growing_pdf | https://arxiv.org/pdf/2609.33263 | 200 |
| bp_pdf | https://arxiv.org/pdf/2303.14688 | 200 |
| openalex_title | https://api.openalex.org/works?filter=title.search%3AInformation%20flow%20on%20trees&per-page=10 | HTTP Error 429: Too Many Requests |
| crossref_source | https://api.crossref.org/works?query.title=Survey%20Information%20flow%20on%20trees&rows=5 | 200 |
| arxiv_mss | https://export.arxiv.org/api/query?search_query=au%3AMossel%20AND%20au%3ASohn%20AND%20%28all%3APotts%20OR%20all%3Areconstruction%29&max_results=20 | 200 |
| semantic_retry | https://api.semanticscholar.org/graph/v1/paper/search?query=Information%20flow%20on%20trees%20Mossel&limit=5&fields=title,externalIds,year,paperId | HTTP Error 429:  |
| openalex_doi | https://api.openalex.org/works/https://doi.org/10.1090/dimacs/063/12 | HTTP Error 429: Too Many Requests |
| mss_pdf | https://arxiv.org/pdf/2212.03362 | 200 |
| semantic_doi | https://api.semanticscholar.org/graph/v1/paper/DOI:10.1090/dimacs/063/12?fields=title,year,externalIds,citations.title,citations.year,citations.externalIds | HTTP Error 404: Not Found |
| mp_pdf | https://arxiv.org/pdf/math/0107033 | 200 |
| openalex_citing | No request could be constructed without a verified work ID. | BLOCKED: All source lookup requests rate-limited; cannot obtain a verified OpenAlex work ID for cites filter. |
| github_tree | https://api.github.com/repos/long-mathematics/openai-math-extensions/git/trees/main?recursive=1 | 200 |
| github_README_md | https://raw.githubusercontent.com/long-mathematics/openai-math-extensions/main/README.md | 200 |
| github_output_pdf_heterogeneous-potts-capacity_pdf | https://raw.githubusercontent.com/long-mathematics/openai-math-extensions/main/output/pdf/heterogeneous-potts-capacity.pdf | 200 |
| github_papers_01-heterogeneous-potts-capacity_README_md | https://raw.githubusercontent.com/long-mathematics/openai-math-extensions/main/papers/01-heterogeneous-potts-capacity/README.md | 200 |
| github_papers_01-heterogeneous-potts-capacity_heterogeneous-potts-capacity_tex | https://raw.githubusercontent.com/long-mathematics/openai-math-extensions/main/papers/01-heterogeneous-potts-capacity/heterogeneous-potts-capacity.tex | 200 |
| github_papers_01-heterogeneous-potts-capacity_sections_01-introduction_tex | https://raw.githubusercontent.com/long-mathematics/openai-math-extensions/main/papers/01-heterogeneous-potts-capacity/sections/01-introduction.tex | 200 |
| github_papers_01-heterogeneous-potts-capacity_sections_02-model-capacity-and-main-theorem_tex | https://raw.githubusercontent.com/long-mathematics/openai-math-extensions/main/papers/01-heterogeneous-potts-capacity/sections/02-model-capacity-and-main-theorem.tex | 200 |
| github_papers_01-heterogeneous-potts-capacity_sections_03-posterior-coordinates-and-two-local-inequalities_tex | https://raw.githubusercontent.com/long-mathematics/openai-math-extensions/main/papers/01-heterogeneous-potts-capacity/sections/03-posterior-coordinates-and-two-local-inequalities.tex | 200 |
| github_papers_01-heterogeneous-potts-capacity_sections_04-reconstruction-implies-capacity_tex | https://raw.githubusercontent.com/long-mathematics/openai-math-extensions/main/papers/01-heterogeneous-potts-capacity/sections/04-reconstruction-implies-capacity.tex | 200 |
| github_papers_01-heterogeneous-potts-capacity_sections_05-positive-capacity-implies-reconstruction_tex | https://raw.githubusercontent.com/long-mathematics/openai-math-extensions/main/papers/01-heterogeneous-potts-capacity/sections/05-positive-capacity-implies-reconstruction.tex | 200 |
| github_papers_01-heterogeneous-potts-capacity_sections_06-consequences-and-the-contraction-boundary_tex | https://raw.githubusercontent.com/long-mathematics/openai-math-extensions/main/papers/01-heterogeneous-potts-capacity/sections/06-consequences-and-the-contraction-boundary.tex | 200 |
| github_papers_01-heterogeneous-potts-capacity_sections_07-dependence-on-computationally-certified-input_tex | https://raw.githubusercontent.com/long-mathematics/openai-math-extensions/main/papers/01-heterogeneous-potts-capacity/sections/07-dependence-on-computationally-certified-input.tex | 200 |
| github_papers_01-heterogeneous-potts-capacity_verify_local_expansion_py | https://raw.githubusercontent.com/long-mathematics/openai-math-extensions/main/papers/01-heterogeneous-potts-capacity/verify_local_expansion.py | 200 |
| github_scripts_potts_local_audit_py | https://raw.githubusercontent.com/long-mathematics/openai-math-extensions/main/scripts/potts_local_audit.py | 200 |
| openai_tree | https://api.github.com/repos/openai/math/git/trees/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb?recursive=1 | 200 |
| openai_tree | https://api.github.com/repos/openai/math/git/trees/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb?recursive=1 | 200 |
| openai_contents_The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026 | https://api.github.com/repos/openai/math/contents/preprints/The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026?ref=fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb | 200 |
| openai_direct_The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026_README_md | https://raw.githubusercontent.com/openai/math/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026/README.md | 200 |
| openai_direct_The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026_four-state-potts_pdf | https://raw.githubusercontent.com/openai/math/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026/four-state-potts.pdf | 200 |
| openai_contents_A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026 | https://api.github.com/repos/openai/math/contents/preprints/A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026?ref=fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb | 200 |
| openai_direct_A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026_README_md | https://raw.githubusercontent.com/openai/math/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026/README.md | 200 |
| openai_direct_A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026_four-state-capacity_pdf | https://raw.githubusercontent.com/openai/math/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026/four-state-capacity.pdf | 200 |

The OpenAlex works-citing-source step was specifically attempted by resolving the verified survey DOI to an OpenAlex work ID, then preparing its `filter=cites:W...` request. DOI resolution returned 429, so no valid citing-work request could be issued. This is a blocked citation search, not an empty citation list. Crossref and arXiv were usable; all resulting payloads were saved. Semantic Scholar did not provide a usable source record. GitHub returned one repository for "Potts reconstruction", long-mathematics/openai-math-extensions, containing Christopher D. Long's 11 October 2026 heterogeneous four-state capacity manuscript, and zero for "Potts monotonicity". The mathematical repository was inspected and its four-state OpenAI dependencies followed directly. These are leads rather than an arbitrary-alphabet comparison theorem.

## Other returned mathematical leads (abstract-level screening)

* Heon Lee. **Robust Reconstruction on Trees with a Growing Alphabet**. http://arxiv.org/abs/2609.33263v1, submitted 2026-09-27.
* Yuzhou Gu, Yury Polyanskiy. **Uniqueness of BP fixed point for the Potts model and applications to community detection**. http://arxiv.org/abs/2303.14688v2, submitted 2023-03-26.
* Yuzhou Gu, Yury Polyanskiy. **Non-linear Log-Sobolev inequalities for the Potts semigroup and applications to reconstruction problems**. http://arxiv.org/abs/2005.05444v2, submitted 2020-05-11.
* Federico Ricci-Tersenghi, Guilhem Semerjian, Lenka Zdeborova. **Typology of phase transitions in Bayesian inference problems**. http://arxiv.org/abs/1806.11013v2, submitted 2018-06-28.
* Wenjian Liu, Ning Ning. **Reconstruction for the Asymmetric Ising Model on Regular Trees**. http://arxiv.org/abs/1712.00395v1, submitted 2017-12-01.
* Nayantara Bhatnagar, Elitza Maneva. **A computational method for bounding the probability of reconstruction on trees**. http://arxiv.org/abs/0903.4812v1, submitted 2009-03-27.
* M. Formentin, C. Kuelske. **A symmetric entropy bound on the non-reconstruction regime of Markov chains on Galton-Watson trees**. http://arxiv.org/abs/0903.2962v3, submitted 2009-03-17.
* Allan Sly. **Reconstruction of symmetric Potts Models**. http://arxiv.org/abs/0811.1208v1, submitted 2008-11-07.
* M. Formentin, C. Kuelske. **On the Purity of the free boundary condition Potts measure on random trees**. http://arxiv.org/abs/0810.0677v2, submitted 2008-10-03.
* Marc Mezard, Andrea Montanari. **Reconstruction on trees and spin glass transition**. http://arxiv.org/abs/cond-mat/0512295v1, submitted 2005-12-14.

The retrieved abstracts of the additional leads concern within-model threshold bounds, computation of posterior-distribution recursions, asymmetric binary models, or physics predictions; none states the posed general alphabet monotonicity theorem. Irrelevant imaging/Fourier/metric reconstruction hits were screened out. No related theorem has been labeled a solution in print.

## October 2026 GitHub leads, inspected after the initial service search

Christopher D. Long, **A Sharp Capacity Criterion for Heterogeneous Four-State Potts Broadcasting on Trees**, 11 October 2026, https://github.com/long-mathematics/openai-math-extensions/tree/main/papers/01-heterogeneous-potts-capacity . The retrieved source and PDF study four states with heterogeneous edges and an L3 capacity criterion. They do not compare arbitrary numbers of Potts states. Their references point to the two sources below. Repository documentation explicitly distinguishes compilation and symbolic checks from independent peer review. No imported theorem here is treated as a solution of F0118.

OpenAI, **The Reconstruction Threshold for the Ferromagnetic Four-State Potts Model**, 5 October 2026, pinned commit **fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb**, https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026 . Theorem 1.1, PDF page 2, states (mathematical formatting transcribed):

> Theorem 1.1. For the channel (1.1), if dλ² ≤ 1, then lim_{n→∞} a_n(d,λ) = 0 in each of the following models:
> 1. the rooted d-ary tree, for every integer d ≥ 2;
> 2. the Poisson(d) Galton–Watson tree, for every real d > 0.
> In particular, the assertion includes dλ² = 1.

The objects are the uniform-root **four-state** ferromagnetic channel Pλ(j|i)=λ1{i=j}+(1-λ)/4. The probabilistic proof invokes a preserved higher-moment constraint and exact polynomial certificates. The PDF's statement, model and proof mechanism were inspected; the complete polynomial certificate computations were not independently re-run. This is a significant q=4 threshold lead, not the requested arbitrary-q monotonicity theorem. If its theorem is used as published, the q1=4 case follows immediately: reconstruction implies bλ²>1, and the all-q sufficient bound in ATTEMPT.md supplies reconstruction for q2. This implication is explicitly our argument and is not classified as SOLVED_IN_LITERATURE.

OpenAI, **A Capacity Criterion for Four-State Potts Reconstruction on Trees**, 5 October 2026, same pinned commit, https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026 . Theorem 1.1, PDF page 2, equates four-state reconstruction on bounded-degree deterministic trees with positive L3 capacity for squared channel resistances. Its imported posterior-law estimate is the companion threshold paper's Proposition 3.2. This criterion still concerns four states only.

The initial recursive OpenAI tree response was **truncated**. We therefore followed the exact two cited directories using GitHub's contents API at the pinned commit, then downloaded their PDFs and README files. Thus the two manuscripts were obtained despite the truncated global listing. All requests and payloads are recorded locally. These October leads were absent from the initial bounded arXiv results, so the GitHub search materially improved this status check.
