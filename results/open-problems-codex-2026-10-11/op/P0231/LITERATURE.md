# P0231 literature audit — 2026-10-12

No retrieved paper states and proves determinism of the Hausdorff dimension for the original two-seed Euclidean Poisson-coloring frontier. This is a bounded negative search result, not an exhaustive current-open certification. SOLVED_IN_LITERATURE is not claimed.

## Primary source and exact remaining question

Anne-Laure Basdevant, Guillaume Blanc, Nicolas Curien, Arvind Singh, “Fractal properties of the frontier in Poissonian coloring,” ALEA, Latin American Journal of Probability and Mathematical Statistics 20 (2023), 1565–1586. DOI: 10.30757/ALEA.v20-59. arXiv:2302.07254v2, updated 2023-11-27. Source URL: https://alea.impa.br/articles/v20/20-59.pdf. Download saved as source.pdf; all pages extracted into source_text.txt.

Verbatim question-containing passage, PDF page 3 / printed page 1567:

> “Although our results show the convergence in a strong sense of the colored regions and establish the fractal nature of the frontier, many questions remain open, such as the existence of a zero–one law for the Hausdorff dimension of F∞. We focus here on the planar case d = 2, which concentrates the most interesting topological questions.”

This is a prose question, not Open Question 1.2 (which concerns curves). The model on PDF pages 1–2 has fixed distinct seeds in [0,1]^d and independent uniform arrivals, with Euclidean nearest-neighbor inheritance. F∞ is the intersection of closures of both color-site sets. The strict bounds in Theorem 1.1 (PDF page 2) are already proved and are not the task. Proposition 3.8 (PDF pages 20–21) explicitly assumes d>=2 for the lower bound. The immediately following topological questions specialize to d=2. No theorem giving deterministic dimension was found in the source.

## Every network search / fetch

Raw service responses are retained locally. Entries report failures honestly. OpenAlex citation retrieval was attempted but rate-limited; the DOI-form cites filter in the attempted request is not validated and is not a completed citation traversal. A correct OpenAlex work-ID traversal requires first resolving the source work, which also returned HTTP 429. Semantic Scholar citation traversal did succeed.

- 2026-10-12T01:47:20.983990 | source | ok | query/URL: `https://alea.impa.br/articles/v20/20-59.pdf`
- 2026-10-12T01:46:51.638540 | arxiv | ok | query/URL: `https://export.arxiv.org/api/query?search_query=all%3A%22Poissonian%20coloring%22&max_results=30`
- 2026-10-12T01:46:50.971586 | openalex | HTTP Error 429: Too Many Requests | query/URL: `https://api.openalex.org/works?search=Fractal%20properties%20of%20the%20frontier%20in%20Poissonian%20coloring&per-page=15`
- 2026-10-12T01:46:52.827329 | crossref | ok | query/URL: `https://api.crossref.org/works?query=Poissonian%20coloring%20frontier&rows=15`
- 2026-10-12T01:46:51.353221 | semantic | HTTP Error 429:  | query/URL: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:2302.07254?fields=title,authors,year,externalIds,citations.title,citations.year,citations.externalIds`
- 2026-10-12T01:46:51.329459 | github | ok | query/URL: `https://api.github.com/search/repositories?q=%22Poissonian%20coloring%22`
- 2026-10-12T01:52:40.846710 | openalex_doi | HTTP Error 429: Too Many Requests | query/URL: `https://api.openalex.org/works/https://doi.org/10.30757/ALEA.v20-59`
- 2026-10-12T01:52:42.607165 | openalex_citing | HTTP Error 429: Too Many Requests | query/URL: `https://api.openalex.org/works?filter=cites:doi:10.30757/ALEA.v20-59&per-page=50`
- 2026-10-12T01:52:45.863350 | semantic_search | ok | query/URL: `https://api.semanticscholar.org/graph/v1/paper/search?query=Poissonian%20coloring&limit=20&fields=title,year,externalIds`
- 2026-10-12T01:52:45.701291 | arxiv_broad | ok | query/URL: `https://export.arxiv.org/api/query?search_query=%28all%3A%22Poisson%22%20AND%20all%3A%22coloring%22%29%20OR%20%28all%3A%22Poissonian%22%20AND%20all%3A%22colouring%22%29&max_results=60&sortBy=submittedDate&sortOrder=descending`
- 2026-10-12T01:52:47.660555 | crossref_exact | ok | query/URL: `https://api.crossref.org/works?query.title=Poisson%20coloring%20frontier%20dimension%20zero%20one&rows=15`
- 2026-10-12T01:52:46.445969 | github_broad | ok | query/URL: `https://api.github.com/search/repositories?q=Poisson%20coloring%20frontier`
- 2026-10-12T01:54:50.243447 | semantic_citations | ok | query/URL: `https://api.semanticscholar.org/graph/v1/paper/080cc8f4f1e1bf7cd266efb7e2869793e6f1c908/citations?fields=title,year,externalIds&limit=100`
- 2026-10-12T01:57:21.603694 | tree_paper | ok | query/URL: `https://arxiv.org/pdf/2606.24793`
- 2026-10-12T01:57:20.530249 | stick_paper | ok | query/URL: `https://arxiv.org/pdf/2601.19546`
- 2026-10-12T01:57:20.303258 | survey_metadata | ok | query/URL: `https://api.crossref.org/works/10.1016/j.cosrev.2025.100857`
- 2026-10-12T01:57:19.869739 | citing_arxiv_metadata | ok | query/URL: `https://export.arxiv.org/api/query?id_list=2606.24793,2601.19546,2302.10795,2212.13235,2108.13014`

## Search results and relevance

### arxiv.txt

- Fractal properties of the frontier in Poissonian coloring; http://arxiv.org/abs/2302.07254v2; updated 2023-11-27T14:45:53Z.
- Random partitions of the plane via Poissonian coloring, and a self-similar process of coalescing planar partitions; http://arxiv.org/abs/1701.00131v1; updated 2016-12-31T16:21:31Z.
### arxiv_broad.txt

- Thresholds and Fluctuations for Colorful Arithmetic Progressions in Sparse Random Colorings; http://arxiv.org/abs/2609.15086v2; updated 2026-09-28T09:31:24Z.
- One marked-sum law determines random mass partitions and $Ξ$-coalescents; http://arxiv.org/abs/2609.12790v1; updated 2026-09-11T12:51:42Z.
- The Decoherence Exponent: Stable Phase Noise and Constraints on Objective State Reduction; http://arxiv.org/abs/2608.18335v1; updated 2026-08-18T21:36:16Z.
- RPG-VST: Robust Poisson-Gaussian Variance Stabilization for Blind RAW Denoising; http://arxiv.org/abs/2607.24291v1; updated 2026-07-27T11:39:03Z.
- Multi-Conditioned Diffusion Synthesis of Sand Boils for Low-Resource Earthen-Levee Inspection; http://arxiv.org/abs/2607.08794v1; updated 2026-07-08T01:07:23Z.
- Exploiting Task-Based Parallelism for the Red-Black Gauss-Seidel Method on 2D Grids; http://arxiv.org/abs/2607.01735v1; updated 2026-07-02T05:45:18Z.
- Cutoff profiles for colored top-m-to-random shuffles with growing block size; http://arxiv.org/abs/2606.29530v1; updated 2026-06-28T17:53:07Z.
- Hamiltonian formalism for Bose excitations in a plasma with a non-Abelian interaction: plasmon bremsstrahlung; http://arxiv.org/abs/2606.17670v1; updated 2026-06-16T08:31:55Z.
- The directed landscape in half-space; http://arxiv.org/abs/2604.10020v2; updated 2026-05-08T07:30:45Z.
- Explicit cutoff profiles for colored top-$m$-to-random shuffles; http://arxiv.org/abs/2604.09933v2; updated 2026-05-27T17:43:06Z.
- LCAMV: High-Accuracy 3D Reconstruction of Color-Varying Objects Using LCA Correction and Minimum-Variance Fusion in Structured Light; http://arxiv.org/abs/2603.10456v1; updated 2026-03-11T06:16:10Z.
- Triggered urn models for frequently asked questions (FAQ); http://arxiv.org/abs/2601.10337v1; updated 2026-01-15T12:31:45Z.
- Learning to Sense for Driving: Joint Optics-Sensor-Model Co-Design for Semantic Segmentation; http://arxiv.org/abs/2512.20815v2; updated 2025-12-25T20:26:31Z.
- Charm multiplicity distribution in high energy pp collisions with PYTHIA; http://arxiv.org/abs/2512.18739v1; updated 2025-12-21T14:01:36Z.
- The Poisson Type Operators on the Double Fock Space of Type B; http://arxiv.org/abs/2511.10219v1; updated 2025-11-13T11:47:04Z.
- Classical scattering matrix for hard and soft Bose-excitations in a non-Abelian plasma within the Hamiltonian formalism; http://arxiv.org/abs/2511.05072v1; updated 2025-11-07T08:40:03Z.
- Region-to-Region: Enhancing Generative Image Harmonization with Adaptive Regional Injection; http://arxiv.org/abs/2508.09746v1; updated 2025-08-13T12:21:51Z.
- The Hidden Symmetries of Yang-Mills Theory in (3+1)-dimensions; http://arxiv.org/abs/2506.15832v2; updated 2025-11-18T15:38:19Z.
- A Real-time Endoscopic Image Denoising System; http://arxiv.org/abs/2506.15395v1; updated 2025-06-18T12:12:10Z.
- Poisson Informed Retinex Network for Extreme Low-Light Image Enhancement; http://arxiv.org/abs/2506.04470v3; updated 2025-10-31T09:28:57Z.
- Phase transitions for the Widom--Rowlinson model in random environments; http://arxiv.org/abs/2505.05319v1; updated 2025-05-08T15:04:07Z.
- Moment estimates for solutions of SPDEs with Lévy colored noise; http://arxiv.org/abs/2504.21648v2; updated 2026-01-09T16:44:37Z.
- UV LIGHTS. New tools for revealing the low surface brightness regime in the ultraviolet; http://arxiv.org/abs/2503.17446v1; updated 2025-03-21T18:00:01Z.
- Canonical formulation of the plasmon - hard particle scattering process in a quark-gluon plasma; http://arxiv.org/abs/2412.05581v3; updated 2026-05-26T06:16:57Z.
- Joint Poisson Convergence of Monochromatic Hyperedges in Multiplex Hypergraphs; http://arxiv.org/abs/2412.00610v1; updated 2024-11-30T23:21:03Z.
- Kupershmidt operators on $3$-BiHom-Poisson color algebras and $3$-BiHom-pre-Poisson color algebras structures; http://arxiv.org/abs/2411.01413v1; updated 2024-11-03T02:46:05Z.
- NUSense: Robust Soft Optical Tactile Sensor; http://arxiv.org/abs/2410.23516v1; updated 2024-10-30T23:57:49Z.
- Brain-like Variational Inference; http://arxiv.org/abs/2410.19315v3; updated 2025-10-24T08:32:15Z.
- Laser Activation of Single Group-IV Colour Centres in Diamond; http://arxiv.org/abs/2409.07421v1; updated 2024-09-11T17:07:56Z.
- Neural Poisson Solver: A Universal and Continuous Framework for Natural Signal Blending; http://arxiv.org/abs/2407.08457v2; updated 2024-07-12T03:19:07Z.
- Furutsu-Novikov--like cross-correlation--response relations for systems driven by shot noise; http://arxiv.org/abs/2405.13508v3; updated 2024-09-27T12:12:40Z.
- Competing bootstrap processes on the random graph $G(n,p)$; http://arxiv.org/abs/2405.00363v6; updated 2026-10-06T09:34:10Z.
- New bounds for normal approximation on product spaces with applications to monochromatic edges, random sums and an infinite de Jong CLT; http://arxiv.org/abs/2403.14334v2; updated 2024-03-22T05:48:26Z.
- Cluster structure on genus 2 spherical DAHA: seven-colored flower; http://arxiv.org/abs/2402.16074v2; updated 2024-06-15T21:14:51Z.
- Edge Laplacians and Edge Poisson Transforms for Graphs; http://arxiv.org/abs/2312.09101v1; updated 2023-12-14T16:38:46Z.
- Revisiting Poisson-disk Subsampling for Massive Point Cloud Decimation; http://arxiv.org/abs/2311.17604v1; updated 2023-11-29T12:57:51Z.
- SeamlessNeRF: Stitching Part NeRFs with Gradient Propagation; http://arxiv.org/abs/2311.16127v1; updated 2023-10-30T15:52:35Z.
- Moments of polynomial functionals of spectrally positive Lévy processes; http://arxiv.org/abs/2310.11137v5; updated 2025-04-16T06:30:38Z.
- Query-Based Sampling of Heterogeneous CTMCs: Modeling and Optimization with Binary Freshness; http://arxiv.org/abs/2310.02223v2; updated 2024-05-30T22:58:12Z.
- Hamiltonian formalism for Bose excitations in a plasma with a non-Abelian interaction I: plasmon -- hard particle scattering; http://arxiv.org/abs/2307.15390v2; updated 2024-07-15T09:32:14Z.
- A Fine Grained Stochastic Geometry Based Analysis on LEO Satellite Communication Systems; http://arxiv.org/abs/2307.01512v1; updated 2023-07-04T06:49:07Z.
- Tracing attosecond electron emission from a nanometric metal tip; http://arxiv.org/abs/2305.16185v1; updated 2023-05-25T15:41:56Z.
- Self-dual gravity and color/kinematics duality in AdS$_4$; http://arxiv.org/abs/2304.07141v3; updated 2023-08-01T19:12:36Z.
- On the structure of graded Poisson color algebras; http://arxiv.org/abs/2303.13832v2; updated 2023-04-24T07:52:53Z.
- Fractal properties of the frontier in Poissonian coloring; http://arxiv.org/abs/2302.07254v2; updated 2023-11-27T14:45:53Z.
- Resonant noise amplification in a predator-prey model with quasi-discrete generations; http://arxiv.org/abs/2301.13290v1; updated 2023-01-30T21:07:25Z.
- Difference of Anisotropic and Isotropic TV for Segmentation under Blur and Poisson Noise; http://arxiv.org/abs/2301.03393v4; updated 2023-06-16T09:25:24Z.
- On the Size of Chromatic Delaunay Mosaics; http://arxiv.org/abs/2212.03121v1; updated 2022-12-06T16:37:01Z.
- Polyubles, Poisson homogeneous spaces and multi-flag varieties; http://arxiv.org/abs/2210.00246v2; updated 2023-01-10T03:25:08Z.
- Impact of random alloy fluctuations on the carrier distribution in multi-color (In,Ga)N/GaN quantum well systems; http://arxiv.org/abs/2209.11657v1; updated 2022-09-23T15:41:45Z.
- Ternary Leibniz color algebras and beyond; http://arxiv.org/abs/2208.09631v1; updated 2022-08-20T08:03:37Z.
- The cortical V1 transform as a heterogeneous Poisson problem; http://arxiv.org/abs/2206.06895v2; updated 2023-07-29T18:10:18Z.
- Denoising Fast X-Ray Fluorescence Raster Scans of Paintings; http://arxiv.org/abs/2206.01740v1; updated 2022-06-03T03:17:18Z.
- Multiview Textured Mesh Recovery by Differentiable Rendering; http://arxiv.org/abs/2205.12468v3; updated 2022-10-12T02:38:42Z.
- Hierarchical Vectorization for Portrait Images; http://arxiv.org/abs/2205.11880v1; updated 2022-05-24T07:58:41Z.
- Admissible Hom-Novikov-Poisson and Hom-Gelfand-Dorfman color Hom-algebras; http://arxiv.org/abs/2205.03723v1; updated 2022-05-07T21:10:18Z.
- FSGANv2: Improved Subject Agnostic Face Swapping and Reenactment; http://arxiv.org/abs/2202.12972v1; updated 2022-02-25T21:04:39Z.
- Off-Shell Color-Kinematics Duality for Chern-Simons; http://arxiv.org/abs/2112.11452v3; updated 2022-09-01T17:40:43Z.
- A Robust Lane Detection Associated with Quaternion Hardy Filter; http://arxiv.org/abs/2108.04356v1; updated 2021-08-06T09:06:14Z.
- Extended Chern-Simons model for a vector multiplet; http://arxiv.org/abs/2105.01292v1; updated 2021-05-04T05:17:02Z.

The exact phrase arXiv search returned only the source and Aldous (2018). The broadened search returned 60 entries, including newer papers, but their titles/abstracts did not supply a matching Euclidean-frontier zero-one theorem. This query is noisy and truncated at 60; it is not exhaustive.

Crossref broad title query returned the source and Aldous among mostly unrelated works. The dimension/zero-one query produced no matching paper. GitHub exact and broader repository searches each returned total_count=0. Semantic Scholar relevance search returned the source, Aldous, a duplicate Aldous submission, and unrelated results.

## Papers citing the source

- Random sequential nearest-neighbor coloring on trees (2026); identifiers: {"ArXiv": "2606.24793", "CorpusId": 289630109}.
- Random spanning trees and forests: a geometric focus (2026); identifiers: {"DBLP": "journals/csr/LichevMP26", "DOI": "10.1016/j.cosrev.2025.100857", "CorpusId": 283232967}.
- Holder continuity of interfaces for scale-invariant Poisson stick soup (2026); identifiers: {"ArXiv": "2601.19546", "CorpusId": 285071442}.
- Geodesics in planar Poisson road random metric (2025); identifiers: {"DOI": "10.1112/plms.70070", "CorpusId": 280244314}.
- Siblings in d-dimensional nearest neighbour trees (2023); identifiers: {"ArXiv": "2302.10795", "DOI": "10.3150/24-bej1771", "CorpusId": 257050709}.
- Competing types in preferential attachment graphs with community structure (2022); identifiers: {"ArXiv": "2212.13235", "DOI": "10.1214/25-ejp1353", "CorpusId": 255124980}.
- New results for the random nearest neighbor tree (2021); identifiers: {"ArXiv": "2108.13014", "DOI": "10.1007/s00440-024-01268-2", "CorpusId": 237353335}.

Fetched and examined newer close leads:

1. Anne-Laure Basdevant and Arvind Singh, “Random sequential nearest-neighbor coloring on trees,” arXiv:2606.24793v1, posted 2026-06-23 (PDF dated June 24, 2026), 39 pages. Full PDF and text retained as tree_paper.txt (PDF bytes) and tree_paper_text.txt. Its abstract and introduction explicitly distinguish regular-tree geometry from Euclidean coloring. Its theorems concern genealogical forests and local limits on trees; this is a different object, not a solution to P0231.
2. Augusto Teixeira and Daniel Ungaretti, “Holder continuity of interfaces for scale-invariant Poisson stick soup,” arXiv:2601.19546v1, posted 2026-01-27 (PDF dated January 28, 2026), 34 pages. Full PDF/text retained as stick_paper.txt and stick_paper_text.txt. The object is the covered/vacant interface of a planar Poisson stick soup; the paper proves tightness and Holder continuity, not this coloring-frontier zero-one theorem.
3. Lyuben Lichev, Dieter Mitsche, Xavier Pérez-Giménez, ['Random spanning trees and forests: a geometric focus'], ['Computer Science Review'], volume 59, article 100857, DOI 10.1016/j.cosrev.2025.100857; publication metadata {'date-parts': [[2026, 2]]}. Crossref metadata retrieved, full text not reviewed. Survey lead only.

Other relevant references from the primary source:

- David Aldous, “Random partitions of the plane via Poissonian coloring and a self-similar process of coalescing planar partitions,” Annals of Probability 46(4) (2018), 2000–2037; DOI 10.1214/17-AOP1218; arXiv:1701.00131. Predecessor, not a later solution.
- John Preater, “A species of voter model driven by immigration,” Statistics & Probability Letters 79(20) (2009), 2131–2137. The source attributes zero Lebesgue measure to its Theorem 2, and island creation to Theorem 3. Neither is dimension determinism.
- Lyuben Lichev and Dieter Mitsche, “New results for the random nearest neighbor tree,” arXiv:2108.13014; DOI 10.1007/s00440-024-01268-2. Genealogical/combinatorial lead; no matching theorem identified.
- Michael Aizenman and Almut Burchard, “Hölder regularity and dimension bounds for random curves,” Duke Mathematical Journal 99(3) (1999), 419–453. Used for source dimension bounds; does not settle this model-specific question.
- Edwin Hewitt and Leonard J. Savage, “Symmetric measures on Cartesian products,” Transactions of the American Mathematical Society 80 (1955), 470–501. Standard finite-permutation zero-one law used for the envelope reduction; no claim of applicability directly to the original coloring.

## Brain and prior-work searches (read-only)

- math_recall.py query “Poissonian coloring frontier dimension”: returned source_f99341d044db78ac6ec222b5d6a69595c260bf605fb2be6e055a242a9bb37cc1, original-question card claim_fb1674b634c48ffddc2f64fc48ad9fca6751ac3ee46a6528f9ced76aee43343b, and whole prior attempt card claim_a3f5a8e2ffcc02ceb1350467c3f66117c3179f68d3e9d89b894151251ebc2519. Prior attempt warns that early changes affect infinitely many descendant colors, and proposes regeneration as a missing ingredient. Rechecked rather than assumed.
- brain.py recall “Poisson coloring frontier” and “Poisson coloring frontier mistakes”: returned mostly off-topic memories; no proof imported.
- rg P0231 against intake and codex_pool_2026_10_10: direct wildcard path failed in PowerShell; retried by enumerating matching intake directories and searching JSONL files. No matching output in the accessible matching directories. A follow-up directory listing was requested.
- Read-only git ls-tree origin/master on ~/math-open-problems, followed by filename filtering for 0231 / poisson-color / frontier: no exact P0231 filename located. Broad frontier matches were unrelated. No repository content was changed.

Search conclusions are limited by service coverage, relevance ranking, API rate limits, and the fact that metadata alone cannot rule out an unadvertised theorem. No solved-in-literature verdict is warranted.

During the attempt, a second math-store query, “Hewitt Savage exchangeable events iid finite permutations,” returned the complete Hewitt–Savage statement (claim_2f498bfa2a2e45261395e21060f28261d050042661f5980c3c3857ba42765667) and the original-paper card (source_9798bd0219e733ced58e3ea0fb684b7529df71cba6aaa091abd95a081b0b502a, DOI 10.2307/1992999). Its iid and finite-permutation hypotheses were checked explicitly for the envelope. Its application to the original dimension was not assumed. The follow-up intake search of problems.jsonl, attempts.jsonl, and sources.jsonl returned no P0231 matches in the enumerated matching directories.

## Second-attempt brain searches — 2026-10-12

- math_recall.py: “conditional probability lower bound martingale convergence regeneration Hausdorff dimension”. Asked for the actual previous gap, rather than only the problem title. Returned uniform integrability, Doob and Levy martingale convergence, dimension/Frostman and probability-bound leads; no model-specific uniform conditional lower estimate was found.
- math_recall.py: “random recursive partition Hausdorff dimension branching process inherited colors”. Returned recursive distributional equations/endogeny and branching-process leads; these require a recursive independent-subtree structure not established for spatial descendant cells.
- math_recall.py: “maximum bottleneck path minimum cut ultrametric spanning tree”. Returned maximum-flow/minimum-cut (claim_924d6fa327ca62cb9dd0243eb71fdf24687c5fa28be3fe7e9a277db3b8e74186), spanning-tree lemmas, and a purported Hall theorem card (claim_8c5ffdc50c5cd643e4256ee3070df1e3f76e8fdf54a9612b55f2f360ea9715d7) whose statement instead concerns edge-disjoint paths. The mislabeled card was rejected as a usable authority. The bottleneck identity was proved directly; summed-capacity max-flow/min-cut was not applied.
- math_recall.py: “stochastic homogenization stationary ergodic random interface Hausdorff dimension”. Returned ergodicity and Kingman subadditivity (source_ab20b037d543e4d35bc682c24b59082deed93c887992ae957e3179a8bc113503), plus unrelated random-fractal questions. No stationary tangent law or subadditive dimension functional for this coloring was supplied. Kingman was not invoked.

No new online literature search was needed to claim these handwritten partial reductions, and no literature-solution verdict is added. The previous bounded online status audit and its rate-limit caveats remain in force.
