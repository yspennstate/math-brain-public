# Literature audit

Search date: 2026-10-11 (machine local date).

- source: https://arxiv.org/pdf/0712.1867 — OK, 968265 bytes.
- arxiv: https://export.arxiv.org/api/query?search_query=all:noncrossing%20AND%20all:Poisson&max_results=30 — OK, 7228 bytes.
- openalex: https://api.openalex.org/works?search=Poisson%20matching%20noncrossing&per-page=30 — HTTP Error 429: Too Many Requests, 0 bytes.
- crossref: https://api.crossref.org/works?query=Poisson%20matching%20noncrossing&rows=20 — OK, 80033 bytes.
- semantic: https://api.semanticscholar.org/graph/v1/paper/search?query=Poisson%20matching%20noncrossing&limit=20&fields=title,authors,year,externalIds,url — HTTP Error 429: , 0 bytes.
- github: https://api.github.com/search/repositories?q=Poisson+matching+noncrossing — OK, 55 bytes.
- openalex_source: https://api.openalex.org/works?search=Poisson%20matching%20Holroyd%20Pemantle%20Peres%20Schramm&per-page=5 — HTTP Error 429: Too Many Requests, 0 bytes.
- 2026-10-11 arxiv_matching: https://export.arxiv.org/api/query?search_query=ti:matching%20AND%20(all:Poisson%20OR%20au:Holroyd)&max_results=80 — OK (154852 bytes).
- 2026-10-11 arxiv_noncross: https://export.arxiv.org/api/query?search_query=all:%22non-crossing%22%20AND%20all:Poisson&max_results=40 — OK (29799 bytes).
- 2026-10-11 geometric: https://arxiv.org/pdf/0909.0575 — OK (208482 bytes).
- 2026-10-11 openalex_retry: https://api.openalex.org/works?search=non-crossing%20Poisson%20matching&per_page=20 — HTTP Error 429: Too Many Requests.
- 2026-10-11 openalex_doi: https://api.openalex.org/works/https://doi.org/10.1214/08-AIHP185 — HTTP Error 429: Too Many Requests.
- 2026-10-11 semantic_source: https://api.semanticscholar.org/graph/v1/paper/ARXIV:0712.1867?fields=title,citations.title,citations.year,citations.externalIds — HTTP Error 429: .
- 2026-10-11 crossref_minimal: https://api.crossref.org/works?query.title=minimal%20matchings%20point%20processes&rows=15 — OK (86007 bytes).
- 2026-10-11 github_broad: https://api.github.com/search/repositories?q=noncrossing+matching — OK (22498 bytes).
- 2026-10-11 follow-up PDF https://arxiv.org/pdf/2012.07129: OK 734402 bytes.
- 2026-10-11 follow-up PDF https://arxiv.org/pdf/2609.19426: OK 1617955 bytes.
- 2026-10-11 arxiv_planar: https://export.arxiv.org/api/query?search_query=all:%22planar%20matching%22%20AND%20all:Poisson&max_results=40 — OK 752 bytes.
- 2026-10-11 crossref_source: https://api.crossref.org/works?query.title=Poisson%20matching&query.author=Holroyd&rows=5 — OK 36908 bytes.
- 2026-10-11 openalex_correct_source: https://api.openalex.org/works/https://doi.org/10.1214/08-AIHP170 — HTTP Error 429: Too Many Requests.
- 2026-10-11 semantic_citations: https://api.semanticscholar.org/graph/v1/paper/ARXIV:0712.1867/citations?fields=title,year,externalIds&limit=100 — OK 21501 bytes.
- 2026-10-11 crossref_planar: https://api.crossref.org/works?query=translation%20invariant%20planar%20Poisson%20matching&rows=30 — OK 142506 bytes.
OpenAlex citing-works enumeration could not be run: source-ID resolution is rate-limited. No successful citation graph audit is claimed. The earlier DOI 08-AIHP185 query was incorrect; corrected to 08-AIHP170 here.
- 2026-10-11 citation follow-up https://arxiv.org/pdf/2311.17687: OK 310987 bytes.
- 2026-10-11 citation follow-up https://arxiv.org/pdf/2109.13590: OK 314377 bytes.
- 2026-10-11 citation follow-up https://arxiv.org/pdf/2106.04524: OK 96439 bytes.
- 2026-10-11 arXiv citation metadata: https://export.arxiv.org/api/query?id_list=2311.17687,2109.13590,2506.16873,2402.13705,1910.01614,2303.05137,2304.11145,2509.08659,2601.08983 — OK 14528 bytes.

## Citation-graph follow-up metadata (leads, not solutions)

- Ali Khezeli, Samuel Mellick. **On the Existence of Balancing Allocations and Factor Point Processes**. http://arxiv.org/abs/2303.05137v2. Abstract: In this article, we show that every stationary random measure on $\mathbb R^d$ that is essentially free (i.e., has no symmetries a.s.) admits a point process as a factor (i.e., as a measurable and translation-equivariant function of the measure). As a result, we improve the results of Last and Thorisson (2022) on the existence of a factor balancing allocation between ergodic pairs of stationary random measures $Φ$ and $Ψ$ with equal intensities. In particular, we prove that such an allocation exists if $Φ$ is diffuse and either $(Φ,Ψ)$ is essentially free or $Φ$ assigns zero measure to every $(d-1)$-dimensional affine hyperplane. The main result is deduced from an existing result in descriptive set theory, that is, the existence of lacunary sections. We also weaken the assumption of being essentially free to the case where a discrete group of symmetries is allowed.

- Itai Benjamini, Adam Timar. **Invariant embeddings of unimodular random planar graphs**. http://arxiv.org/abs/1910.01614v3. Abstract: Consider an ergodic unimodular random one-ended planar graph $\G$ of finite expected degree. We prove that it has an isometry-invariant locally finite embedding in the Euclidean plane if and only if it is invariantly amenable. By "locally finite" we mean that any bounded open set intersects finitely many embedded edges. In particular, there exist invariant embeddings in the Euclidean plane for the Uniform Infinite Planar Triangulation and for the critical Augmented Galton-Watson Tree conditioned to survive. Roughly speaking, a unimodular embedding of $\G$ is one that is jointly unimodular with $\G$ when viewed as a decoration. We show that $\G$ has a unimodular embedding in the hyperbolic plane if it is invariantly nonamenable, and it has a unimodular embedding in the Euclidean plane if and only if it is invariantly amenable. Similar claims hold for representations by tilings instead of embeddings.

- Martin Huesmann, Francesco Mattesini, Felix Otto. **There is no stationary $p$-cyclically monotone Poisson matching in 2D**. http://arxiv.org/abs/2311.17687v1. Abstract: We show that for $p>1$ there is no $p$-cyclically monotone stationary matching of two independent Poisson processes in dimension $d=2$. The proof combines the $p$-harmonic approximation result from \cite[Theorem 1.1]{koch23} with local asymptotics for the two-dimensional matching problem. Moreover, we prove a.s. local upper bounds of the correct order in the case $p>1$, which, to the best of our knowledge, are not readily available in the current literature.

- Raphaël Lachièze-Rey, D. Yogeshwaran. **Hyperuniformity and optimal transport of point processes**. http://arxiv.org/abs/2402.13705v4. Abstract: We examine optimal matchings or transport between two stationary random measures. It covers allocation from the Lebesgue measure to a point process and matching a point process to a regular (shifted) lattice. The main focus of the article is the impact of hyperuniformity(reduced variance fluctuations in point processes) to optimal transport: in dimension 2, we show that the typical matching cost has finite second moment under a mild logarithmic integrability condition on the reduced pair correlation measure, showing that most planar hyperuniform point processes are L2-perturbed lattices. Our method also retrieves known sharp bounds in finite windows for neutral integrable systems such as Poisson processes, and also applies to hyperfluctuating systems. Further, in three dimensions onwards, all point processes with an integrable pair correlation measure are L2-perturbed lattices without requiring hyperuniformity.

- Matthias Erbar, Martin Huesmann, Jonas Jalowy, Bastian Müller. **Optimal transport of stationary point processes: Metric structure, gradient flow and convexity of the specific entropy**. http://arxiv.org/abs/2304.11145v2. Abstract: We develop a theory of optimal transport for stationary random measures with a focus on stationary point processes and construct a family of distances on the set of stationary random measures. These induce a natural notion of interpolation between two stationary random measures along a shortest curve connecting them. In the setting of stationary point processes we leverage this transport distance to give a geometric interpretation for the evolution of infinite particle systems with stationary distribution. Namely, we characterise the evolution of infinitely many Brownian motions as the gradient flow of the specific relative entropy w.r.t.~the Poisson point process. Further, we establish displacement convexity of the specific relative entropy along optimal interpolations of point processes and establish an stationary analogue of the HWI inequality, relating specific entropy, transport distance, and a specific relative Fisher information.

- Yinon Spinka, Oren Yakir. **Optimal factor matchings for point processes on non-amenable unimodular graphs**. http://arxiv.org/abs/2601.08983v1. Abstract: Consider a unit-intensity point process $Π$ on the vertex set $V$ of a transitive non-amenable unimodular graph. We study invariant matchings between $Π$ and $V$ having small typical matching distances. When $Π$ is either a Poisson process or i.i.d. perturbations of the vertex set, we determine the optimal matching distance and show that it can be attained by a factor matching scheme (that is, a deterministic and equivariant function of $Π$).

- Dor Elboim, Yinon Spinka, Oren Yakir. **Optimal matchings of randomly perturbed lattices**. http://arxiv.org/abs/2506.16873v1. Abstract: Consider a point process in Euclidean space obtained by perturbing the integer lattice with independent and identically distributed random vectors. Under mild assumptions on the law of the perturbations, we construct a translation-invariant perfect matching between this point process and the lattice, such that the matching distance has the same tail behavior as the hole probability of the point process, which is a natural lower bound.

- Martin Huesmann, Francesco Mattesini, Felix Otto. **There is no stationary cyclically monotone Poisson matching in 2d**. http://arxiv.org/abs/2109.13590v1. Abstract: We show that there is no cyclically monotone stationary matching of two independent Poisson processes in dimension $d=2$. The proof combines the harmonic approximation result from \cite{GHO} with local asymptotics for the two-dimensional matching problem for which we give a new self-contained proof using martingale arguments.

- Martin Huesmann, Bastian Müller. **Gap metrics for stationary point processes and quantitative convexity of the free energy**. http://arxiv.org/abs/2509.08659v1. Abstract: In this article, we are interested in convexity properties of the free energy for stationary point processes on $\mathbb R$ w.r.t.\ a new geometry inspired by optimal transport. We will show for a rich class of pairwise interaction energies A) quantified strict convexity of the free energy implying uniqueness of minimizers B) existence of a gradient flow curve of the free energy w.r.t. the new metric converging exponentially fast to the unique minimizer. Examples for energies for which A holds include logarithmic or Riesz interactions with parameter $0<s<1$, examples for which A and B hold are hypersingular Riesz or Yukawa interactions.



## Verified source and scope

Alexander E. Holroyd, Robin Pemantle, Yuval Peres, Oded Schramm. **Poisson matching**. Annales de l'Institut Henri Poincare, Probabilites et Statistiques 45(1) (2009), 266–287. DOI: 10.1214/08-AIHP170. arXiv:0712.1867v3. Downloaded source.pdf, with page-indexed extraction source.txt.

Open Problems (ii), PDF p.34, verbatim (line breaks reflowed; mathematical superscript restored):

> Does there exist a translation-invariant matching of two independent Poisson processes in R² such that the line segments connecting matched pairs do not cross?

PDF pp.1 and 3 specify perfect bipartite matching, invariance of the joint law (R,B,M), and distinguish factors from randomized schemes. PDF p.4 explicitly gives the equal intensity-one setting. Thus the target allows randomness and requires full translation invariance, straight non-crossing edges, and perfectness. Theorem 2, PDF p.4, states the infinite first moment obstruction in dimension two, which prevents appealing to finite expected Euclidean cost. Infinite first moment is consistent with tightness of a probability distribution, so it alone does not refute the criterion proved in ATTEMPT.md.

## Relevant full-text follow-ups

1. Alexander E. Holroyd. **Geometric properties of Poisson matchings**. Probability Theory and Related Fields 150 (2011), 511–527. DOI: 10.1007/s00440-010-0282-y. arXiv:0909.0575. Downloaded geometric.pdf and geometric.txt. Theorem 1, PDF p.2: planar perfect matching without stationarity; stationary one-colour planar matching; stationary partial matching at unequal intensities saturating the lower-intensity colour; and stationary matching with disjoint polygonal arcs. These separately change a required hypothesis or the type of edges. Theorem 2, PDF p.3, excludes stationary minimal matchings on a strip and supplies minimal matchings for d=1 and d>=3. Question 1, PDF p.4, retains the requested planar question. Question 2 retains the analogous planar strip question; it is not the same as the strip minimality impossibility. Theorem 4, PDF p.3, shows that stationary minimal matchings in d>=2 must be locally finite. None settles F0082.

2. Alexander E. Holroyd, Svante Janson, Johan Wastlund. **Minimal matchings of point processes**. Probability Theory and Related Fields 184 (2022), 571–611. DOI: 10.1007/s00440-022-01151-y. arXiv:2012.07129v1. Downloaded minimal.pdf and minimal.txt. Theorem 7, PDF p.8, verbatim (line breaks reflowed):

> Theorem 7 (Higher dimensions). Let R (and B) be (independent) Poisson process(es) of intensity 1 on Rᵈ and let γ ∈ [−∞, ∞]. There exists an invariant perfect γ-minimal matching scheme in each of the following three cases: (i) 1-colour, d ≥ 2, γ < ∞; (ii) 2-colour, d = 2, γ < 1; (iii) 2-colour, d ≥ 3, γ < ∞.

The following paragraph states that the gamma=1 and infinity two-colour cases in R² remain unresolved. The gamma<1 case is not a non-crossing theorem: the finite gamma=1/2 example in ATTEMPT.md gives a crossing minimum. Proposition 28, PDF p.29, provides quasistability with a constant depending on gamma. Section 7 of ATTEMPT.md proves that a generic constant uniform up to gamma=1 is impossible.

3. Martin Huesmann, Francesco Mattesini, Felix Otto. **There is no stationary cyclically monotone Poisson matching in 2d**. Probability Theory and Related Fields (2023). DOI: 10.1007/s00440-023-01225-5. arXiv:2109.13590v1. Downloaded cyclic.pdf and cyclic.txt. Theorem 1.1, PDF p.2, excludes stationary ergodic cyclically monotone bijections in d<=2. The condition here is local optimality for SQUARED length, as equation (1.2), PDF p.1, explicitly shows. It is not equivalent to arbitrary non-crossing straight segments. The discussion on PDF p.3 distinguishes gamma=1 as an unresolved case.

4. Martin Huesmann, Francesco Mattesini, Felix Otto. **There is no stationary p-cyclically monotone Poisson matching in 2d**. Electronic Journal of Probability 29 (2024), DOI: 10.1214/24-EJP1171. arXiv:2311.17687v1. Downloaded p_cyclic.pdf and p_cyclic.txt. Theorem 1.3, PDF p.2, concerns stationary ergodic bijections locally optimal for |x-y|^p with p>1. The preceding paragraph says verbatim:

> Our result, together with the one obtained in [13], complements the one of [10] in the regime p > 1 and d = 2, leaving unsolved the case p = 1 and of course the question on planarity.

Thus this is a substantial related negative theorem, explicitly not a solution of F0082. Caveat: the same introduction says Holroyd excluded planar strip matchings, but the downloaded Holroyd paper actually excludes MINIMAL strip matchings and lists planar strip matching as Question 2. I do not treat that secondary statement about strips as a verified theorem.

5. Omer Angel, Nitya Gadhiwala. **Unbalanced Minimal Matchings for Measurable Scale Invariant Costs on Rᵈ**. arXiv:2609.19426v1 (2026). Downloaded unbalanced.pdf and unbalanced.txt. Theorem 1.1, PDF p.4, classifies measurable scale-invariant costs. Theorem 1.2, PDF p.7, compares balanced and unbalanced minimal matchings for Poisson inputs on R (dimension ONE). Theorem 1.1 is a cost-classification statement, not existence of the requested planar matching; the subsequent existence/comparison statements change dimension. No theorem proving the target was found in this paper.

6. Adam Timar. **A factor matching of optimal tail between Poisson processes**. Combinatorica (2023), DOI: 10.1007/s00493-023-00051-6. arXiv:2106.04524v1. Downloaded optimal_factor.pdf and optimal_factor.txt. Theorem 1, PDF p.1, is for d>=3 and controls tails; it neither covers d=2 nor imposes non-crossing.

All these are leads/background, not SOLVED_IN_LITERATURE. Quotes are retained for scope checking, not asserted as target-solving theorems.

## Search coverage and limits

The initial arXiv noncrossing spelling search mostly returned free-probability papers. The later matching/Poisson/Holroyd query found the minimal-matching and September 2026 cost-classification papers; the exact phrase planar matching query returned no entries. Crossref supplied the correct source DOI and bibliographic metadata but the broad planar query had mostly irrelevant results. GitHub returned no repositories for the narrow Poisson query and unrelated discrete algorithms for the broad query; repository hits are not mathematical proofs.

The Semantic Scholar source citations endpoint succeeded: semantic_citations.json contains 81 records, no next-page token. I inspected titles and identifiers and downloaded the directly relevant minimality papers, including the p>1 impossibility. Additional potentially related citation abstracts, with authors and exact arXiv identifiers, are logged above. Their objects concern perturbed lattices, hyperuniform point processes, allocations, graph embeddings with unspecified vertex locations, non-amenable graphs, or stationary transport metrics. None of their fetched abstracts asserts the target planar Poisson result. Abstract-only examination is explicitly weaker than full theorem verification.

OpenAlex returned HTTP 429 for every attempted search and source lookup, including the corrected DOI. It therefore did not furnish a source work ID or citing-work list. This is a real coverage limit, not evidence that no later solution exists. Semantic Scholar search and initial source expansion were also rate-limited, but its separate citations endpoint worked. No built-in web search was used.

Read-only internal context: recalled Poisson matching and Poisson matching mistakes with brain.py, and Poisson/minimal matching terminology with math_recall.py. The relevant prior record is F0082-A001 in probability_1000_intake_F_20260908/attempts.jsonl. It suggested uncrossing but supplied no infinite stationary construction. Its strip discussion conflated planar and minimal properties; the fetched primary source resolves that distinction. A read-only origin/master path-name scan of math-open-problems found no F0082 or Poisson-matching-labelled answer file. No internal record was accepted as a verdict.

**Status conclusion:** No paper proving or disproving THIS question was found in the completed searches. The latest directly relevant fetched nonexistence paper explicitly leaves planarity unresolved. Search failure at OpenAlex prevents any claim of exhaustive current coverage. Verdict is PARTIAL for the independently proved reductions/constructions, not SOLVED_IN_LITERATURE.


## Second-attempt brain and source checks — 2026-10-11

Read ATTEMPT.md and its exact remaining gap. Read-only math_recall.py queries:

- `Poisson planar matching uniform tightness uncrossing displacement Holroyd`: general tightness and annulus-curve hints; none supplied endpoint-displacement control.
- `uncrossing cost convex Monge Euclidean matching concave`: convexity/Jensen definitions, no matching theorem resolving the gap.
- `stationary cocycle coboundary tightness random walk balanced intervals Poisson`: random-walk/Levy-process background, no target solution.

The second attempt uses self-contained proofs of cost classification and a stationary signed-count coboundary obstruction. The only external theorem used in its finite-expected-cost no-go corollary is the already fetched source's Theorem 2 (infinite mean matching length in dimension two). Its strip special case is consistent with the already fetched Geometric properties Theorem 3(i), not a new claim of literature novelty. No additional online search was needed or performed in this second attempt.
