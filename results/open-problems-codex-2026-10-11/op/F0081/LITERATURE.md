# F0081 literature check — 2026-10-11

## Status and exact source
No paper examined states and proves the question as posed. This is a bounded search, not a certification that no solution exists. OpenAlex requests were rate-limited; Semantic Scholar's citation endpoint did work. Verdict is not SOLVED_IN_LITERATURE.

Alexander E. Holroyd, Robin Pemantle, Yuval Peres, Oded Schramm, “Poisson matching,” Annales de l'Institut Henri Poincaré, Probabilités et Statistiques 45(1) (2009), 266–287, DOI 10.1214/08-AIHP170; arXiv:0712.1867v3, 15 March 2008. Downloaded source.pdf; extracted source.txt.

Verbatim Open Problems (i), PDF p.34, with mathematical glyphs rendered in plain text:
> For the two-color stable matching of two independent Poisson processes, what is the correct power law for the tail behavior of X in dimensions d >= 2? We conjecture that E* X^alpha < infinity if and only if alpha < d/2.

Hypotheses checked on pp.3,5–6 and the stable-matching construction: independent homogeneous red and blue Poisson processes of intensity 1, Euclidean R^d, translation/isometry invariant unique stable perfect matching, X the distance from a typical red point (red Palm law). Equal positive common intensities reduce to 1 by scaling. Positive moments are the intended question; the displayed criterion is not an assertion about arbitrary negative moments.

Theorem 6, PDF p.6: E* X^d = infinity for stable matching in all d; P*(X>r) <= C r^{-s(d)}, where 0<s(d)<1, s(1)=1/2, s(2) approx 0.496, s(3) approx 0.449. Theorem 2, PDF p.4: every invariant matching has E* X^{d/2}=infinity only for d=1,2. Theorem 19, PDF pp.29–33, proves the upper bound. Thus d>=3 divergence at d/2 does NOT follow from the printed lower bound. No exact asymptotic constant for d=1 is inferred here.

## Related papers examined (leads, not solutions)

* Holroyd, “Geometric properties of Poisson matchings,” Probability Theory and Related Fields 150 (2011), 511–527, DOI 10.1007/s00440-010-0282-y. Prior intake flagged this geometric/minimality paper, not a stable tail solution. Bibliography and Crossref checked; not used as a theorem input.
* Holroyd, James B. Martin, Yuval Peres, “Stable matchings in high dimensions via the Poisson-weighted infinite tree,” arXiv:1708.04519v2 (2017/2018). Downloaded pwit_pdf.pdf. Main results allow red-red as well as red-blue pairs, and take d tends to infinity at fixed scales. Section 8(v), PDF p.28, explicitly asks about tails of ordinary two-colour matching. This does not answer fixed d, r tends to infinity.
* Holroyd, Svante Janson, Johan Wästlund, “Minimal matchings of point processes,” Probability Theory and Related Fields (2022), DOI 10.1007/s00440-022-01151-y; arXiv:2012.07129v1 (2020). Downloaded minimal_pdf.pdf. Theorem 4, PDF p.6, concerns processes on R, not R^d for d>=2. It includes stable matching as gamma=-infinity, but only in dimension one.
* Michael A. Klatt, Günter Last, D. Yogeshwaran, “Hyperuniform and rigid stable matchings,” arXiv:1810.00265v3. Downloaded hyperuniform_pdf.pdf. Lattice versus a point process with intensity strictly greater than 1; the exponential matching-flower bounds have different input and imbalance hypotheses. They do not provide scale-uniform residual-charge moment bounds for two critical Poisson processes.
* Ádám Timár, “A factor matching of optimal tail between Poisson processes,” arXiv:2106.04524 (2021), Combinatorica, DOI 10.1007/s00493-023-00051-6. Abstract retrieved in Semantic Scholar citations. Constructs a factor perfect matching with exp(-c r^d) tail for d>=3. This solves the factor optimization question, not the stable scheme. PDF fetch failed (empty exception text recorded); not counted as inspected full text.
* Gideon Amir, Omer Angel, Holroyd, “Multicolour Poisson matching,” Ann. IHP Probab. Stat. 57(4) (2021), DOI 10.1214/21-AIHP1147; arXiv:1605.06485. General matching constructions with colour restrictions, not this particular stable tail. Abstract/search result and bibliographic metadata checked.
* Omer Angel, Nitya Gadhiwala, “Unbalanced Minimal Matchings for Measurable Scale Invariant Costs on R^d,” arXiv:2609.19426 (2026). Downloaded unbalanced_pdf.pdf and searched its full text. Classifies measurable asymmetric scale-invariant costs and discusses one-dimensional matchings. No theorem establishing the stable two-colour critical moment threshold in d>=2 was found.
* Yinon Spinka, Oren Yakir, “Optimal factor matchings for point processes on non-amenable unimodular graphs,” arXiv:2601.08983 (2026). Abstract in citation output: different space and scheme; excluded.
* Dor Elboim, Spinka, Yakir, “Optimal matchings of randomly perturbed lattices,” arXiv:2506.16873 (2025); Raphaël Lachièze-Rey, Yogeshwaran, “Hyperuniformity and optimal transport of point processes,” arXiv:2402.13705 (2024). Abstracts in citation output: different processes or optimizing matchings; excluded.

## Read-only prior work and corrections
Brain recall ran for “stable Poisson matching”, “stable Poisson matching mistakes”, and math-store “Poisson matching stable Holroyd Pemantle Peres Schramm”; results were off-target and not used as facts. A subsequent math-store query asked about point-process variance/covariance and hyperuniformity.

Read F0081-A001 from intake probability_1000_intake_F_20260908/attempts.jsonl and from origin/master:probability_1000/probability_1000_intake_F_20260908/attempts.jsonl via git show. No repository working tree changed. A targeted scan of codex_pool_2026_10_10 returned no F0081 hit. Earlier attempt's assertions that a specific spreading statement is equivalent to the conjecture were not proved and are NOT inherited. Its blanket claim of no monotonicity under adding points is inaccurate: source Lemma 17 proves colour-specific monotonicity on insertion of one blue point. This still does not give the desired scale-uniform fluctuation bounds.

## Every HTTP search/fetch
All requests used Python urllib from the shell; raw successful responses saved locally. Search result relevance was screened by titles and abstracts. Initial arXiv narrow search returned 7 entries; broader search returned fewer than 100 entries; Semantic Scholar citing-paper response returned 81 entries with no next page. Crossref broad search was noisy, so a title+author query verified the source's actual DOI. One earlier OpenAlex DOI request used an incorrect guessed DOI (08-AIHP167); this was corrected to 08-AIHP170 after Crossref. Neither request succeeded. OpenAlex citations filter could not be resolved to the required OpenAlex work ID because source lookup was rate-limited; it is NOT a completed citation search.

* 2026-10-11 — source — `https://arxiv.org/pdf/0712.1867` — saved source.pdf (968265 bytes)
* 2026-10-11 — arxiv — `https://export.arxiv.org/api/query?search_query=all:%22stable%20matching%22%20AND%20all:Poisson&max_results=50` — saved arxiv.xml (14894 bytes)
* 2026-10-11 — openalex — `https://api.openalex.org/works?search=two%20colour%20stable%20Poisson%20matching&per-page=50` — failed: 'HTTP Error 429: Too Many Requests'
* 2026-10-11 — crossref — `https://api.crossref.org/works?query=stable%20Poisson%20matching&rows=30` — saved crossref.json (161873 bytes)
* 2026-10-11 — semantic — `https://api.semanticscholar.org/graph/v1/paper/search?query=stable%20Poisson%20matching&limit=30&fields=title,authors,year,abstract,url,externalIds` — failed: 'HTTP Error 429: '
* 2026-10-11 — github — `https://api.github.com/search/repositories?q=stable+Poisson+matching` — saved github.json (55 bytes)
* 2026-10-11 — openalex_source — `https://api.openalex.org/works?filter=doi:10.1214/08-AIHP167&per-page=5` — failed: 'HTTP Error 429: Too Many Requests'
* 2026-10-11 — openalex_search_retry — `https://api.openalex.org/works?search=Poisson%20matching&per-page=30` — failed: 'HTTP Error 429: Too Many Requests'
* 2026-10-11 — semantic_citations — `https://api.semanticscholar.org/graph/v1/paper/ARXIV:0712.1867/citations?limit=100&fields=title,authors,year,abstract,url` — saved semantic_citations.json (120927 bytes)
* 2026-10-11 — arxiv_tail — `https://export.arxiv.org/api/query?search_query=all:matching%20AND%20all:Poisson%20AND%20(all:tail%20OR%20all:stable)&max_results=100` — saved arxiv_tail.xml (140589 bytes)
* 2026-10-11 — crossref_source — `https://api.crossref.org/works?query.title=Poisson%20matching&query.author=Holroyd&rows=5` — saved crossref_source.json (36907 bytes)
* 2026-10-11 — minimal_pdf — `https://arxiv.org/pdf/2012.07129` — saved minimal_pdf.pdf (734402 bytes)
* 2026-10-11 — pwit_pdf — `https://arxiv.org/pdf/1708.04519` — saved pwit_pdf.pdf (904032 bytes)
* 2026-10-11 — hyperuniform_pdf — `https://arxiv.org/pdf/1810.00265` — saved hyperuniform_pdf.pdf (3922122 bytes)
* 2026-10-11 — openalex_correct_source — `https://api.openalex.org/works/https://doi.org/10.1214/08-AIHP170` — failed: 'HTTP Error 429: Too Many Requests'
* 2026-10-11 — openalex_citing_source — `https://api.openalex.org/works?filter=cites:doi:10.1214/08-AIHP170&per-page=100` — failed: 'HTTP Error 429: Too Many Requests'
* 2026-10-11 — factor_pdf — `https://arxiv.org/pdf/2106.04524` — failed: ''
* 2026-10-11 — unbalanced_pdf — `https://arxiv.org/pdf/2609.19426` — saved unbalanced_pdf.pdf (1617955 bytes)

## Complete citation-result bibliography (unfiltered metadata)

* Omer Angel, Nitya Gadhiwala. Unbalanced Minimal Matchings for Measurable Scale Invariant Costs on $\mathbb{R}^d$. 2026. https://www.semanticscholar.org/paper/2200a6ba28c3bce21480689ffdac647b96554495.
* Yinon Spinka, O. Yakir. Optimal factor matchings for point processes on non-amenable unimodular graphs. 2026. https://www.semanticscholar.org/paper/a569f77d48dc25097d75b39115fbaef80f7572c4.
* Martin Huesmann, B. Muller. Gap metrics for stationary point processes and quantitative convexity of the free energy. 2025. https://www.semanticscholar.org/paper/ac5c12e04c02ed990ba1881c47a756a4417d9fa0.
* Dor Elboim, Yinon Spinka, O. Yakir. Optimal matchings of randomly perturbed lattices. 2025. https://www.semanticscholar.org/paper/96e20221c141a91f9adbe0b47537e7ae42708812.
* Raphael Lachièze-Rey, D. Yogeshwaran. Hyperuniformity and optimal transport of point processes. 2024. https://www.semanticscholar.org/paper/d1fe677da1dc359f56b4cda3e87b343b3739f61a.
* Martin Huesmann, Francesco Mattesini, Felix Otto. There is no stationary p-cyclically monotone Poisson matching in 2d. 2023. https://www.semanticscholar.org/paper/c3a8b7a9f698f552194565d3aa13e3e512860933.
* Matthias Erbar, Martin Huesmann, Jonas Jalowy, B. Muller. Optimal transport of stationary point processes: Metric structure, gradient flow and convexity of the specific entropy. 2023. https://www.semanticscholar.org/paper/043ba60912d53696694a8df10a3f8ee1e0378e62.
* Ali Khezeli, S. Mellick. On the Existence of Balancing Allocations and Factor Point Processes. 2023. https://www.semanticscholar.org/paper/a7a8c1a9f4dd7f5702bc7323efa387ef223419a5.
* Martin Huesmann, Francesco Mattesini, F. Otto. There is no stationary cyclically monotone Poisson matching in 2d. 2021. https://www.semanticscholar.org/paper/2a90e8b8bf423aa0f4214ccaa29fb79f56eb86c1.
* Ádám Timár. A Factor Matching of Optimal Tail Between Poisson Processes. 2021. https://www.semanticscholar.org/paper/5d9d1d1ac256513dd41bfc2b08d5e97b99a2f5e0.
* Sebastian Brandt, Yi-Jun Chang, Jan Grebík, Christoph Grunau, Václav Rozhoň, Zoltán Vidnyánszky. Local Problems on Trees from the Perspectives of Distributed Algorithms, Finitary Factors, and Descriptive Combinatorics. 2021. https://www.semanticscholar.org/paper/d42c31fa2eb4a027807530ad2e395558722cd9aa.
* Matt Bowen, G. Kun, Marcin Sabok. Perfect matchings in hyperfinite graphings. 2021. https://www.semanticscholar.org/paper/8aaf4371c6a42af9241558811847f9b750c7335f.
* P. Nain, Nitish K. Panigrahy, P. Basu, D. Towsley. One-dimensional service networks and batch service queues. 2021. https://www.semanticscholar.org/paper/fc7b528e7ab02deb680761d039a37a0bd0028b86.
* Omer Angel, G. Ray, Yinon Spinka. A tale of two balloons. 2021. https://www.semanticscholar.org/paper/71ccfd0f52e203bc9b1f64a1aaad109fcc3ca57d.
* Danny Nam, A. Sly, Ling-Fu Zhang. Ising Model on Trees and Factors of IID. 2020. https://www.semanticscholar.org/paper/55a65bbb29af757d61c44647a4d9d79e02ac4765.
* A. Holroyd, S. Janson, Johan Wästlund. Minimal matchings of point processes. 2020. https://www.semanticscholar.org/paper/04d852c2c369828ff7b88f4d87a783ce9971a82b.
* Zemer Kosloff, Terry Soo. The orbital equivalence of Bernoulli actions and their Sinai factors. 2020. https://www.semanticscholar.org/paper/6ff2794356069d03c7d6def9929faf24e1ad5b9d.
* B. Błaszczyszyn, C. Hirsch. Optimal stationary markings. 2020. https://www.semanticscholar.org/paper/49209cdb85111c1a8a377365ef32619d624c3487.
* Yinon Spinka. Finitary isomorphisms of renewal point processes and continuous-time regenerative processes. 2019. https://www.semanticscholar.org/paper/26924e631526e49778d39226a93508c21274f830.
* I. Benjamini, Ádám Timár. Invariant embeddings of unimodular random planar graphs. 2019. https://www.semanticscholar.org/paper/54988f872741c90f370109a4eff4ccb615511741.
* Zemer Kosloff, Terry Soo. Finitary isomorphisms of Brownian motions. 2019. https://www.semanticscholar.org/paper/5b5e5798b4908a3e52024cb5ce1047eeafdf5a01.
* Mary Cryan, Heng Guo, Giorgos Mousa. Modified log-Sobolev Inequalities for Strongly Log-Concave Distributions. 2019. https://www.semanticscholar.org/paper/019344bc3574262919a87b723cece6f8b9c10263.
* Nitish K. Panigrahy, P. Basu, D. Towsley, A. Swami, Kevin S. Chan, K. Leung. A queueing-theoretic model for resource allocation in one-dimensional distributed analytics network?. 2019. https://www.semanticscholar.org/paper/84006ca428d358b5cb55eb291690c45a93135f5a.
* Nitish K. Panigrahy, P. Basu, P. Nain, D. Towsley, A. Swami, K. Chan, K. Leung. Resource Allocation in One-Dimensional Distributed Service Networks. 2019. https://www.semanticscholar.org/paper/c4e17e676f705b29ee343c9851f8033c9220de0c.
* Nitish K. Panigrahy, P. Basu, D. Towsley, A. Swami, Kevin S. Chan, K. Leung. A queueing-theoretic model for resource allocation in one-dimensional distributed service network. 2019. https://www.semanticscholar.org/paper/3da59ba87542ef75b077b519f923ea67bdfe270a.
* N. P. Hyun, Y. Peres. Electrostatic Methods for Perfect Matching and Safe Path Planning. 2018. https://www.semanticscholar.org/paper/73571141a4a025228c3e65deae46ed290a9ccd52.
* Michael Andreas Klatt, Günter Last, D. Yogeshwaran. Hyperuniform and rigid stable matchings. 2018. https://www.semanticscholar.org/paper/0ad8603fb02b63288113bc85a5d21d0857d8015c.
* Terry Soo. Finitary isomorphisms of some infinite entropy Bernoulli flows. 2018. https://www.semanticscholar.org/paper/ce7e07df17e372948620537614958a1ba0420566.
* N. Holden, Y. Peres, A. Zhai. Gravitational allocation on the sphere. 2018. https://www.semanticscholar.org/paper/15dbb40c66ff235d499e415e95bb33bf0c051383.
* H. K. Abadi, B. Prabhakar. Stable Matchings in Metric Spaces: Modeling Real-World Preferences using Proximity. 2017. https://www.semanticscholar.org/paper/511e2ba6173af137f025b2fb8fde78244b05f516.
* J. Ortega, P. Hergovich. The Strength of Absent Ties: Social Integration via Online Dating. 2017. https://www.semanticscholar.org/paper/2c59455beba33fc7607218c3477a682baa46cf8d.
* A. Holroyd, James B. Martin, Y. Peres. Stable matchings in high dimensions via the Poisson-weighted infinite tree. 2017. https://www.semanticscholar.org/paper/87d11d5ea9bfccde75190b80156091b15a9fe157.
* N. Holden, Y. Peres, A. Zhai. Gravitational allocation for uniform points on the sphere. 2017. https://www.semanticscholar.org/paper/a1255eea206cd7976026b31f481729216a696388.
* P. Balister, B. Bollobás, Jonathan Lee, Bhargav P. Narayanan. Coalescence on the real line. 2016. https://www.semanticscholar.org/paper/b2067a3cf8749609a057529d2b4cbdbe4ca9aae3.
* Dorottya Beringer, Gábor Pete, Ádám Timár. On percolation critical probabilities and unimodular random graphs. 2016. https://www.semanticscholar.org/paper/dbade97f746b797e2753afe923b57497799dcb24.
* Peter Mörters, István Redl. Optimal embeddings by unbiased shifts of Brownian motion. 2016. https://www.semanticscholar.org/paper/f2da04f7133d0de7476c02ca7a68f5bff6797d57.
* Gideon Amir, Omer Angel, A. Holroyd. Multicolour Poisson matching. 2016. https://www.semanticscholar.org/paper/a27a9fe6740c161cc737df8fffa3cb328daf17fc.
* Maria Deijfen, A. Holroyd, James B. Martin. Friendly Frogs, Stable Marriage, and the Magic of Invariance. 2016. https://www.semanticscholar.org/paper/99d352a4b4aabfedecc02b1ebed4fee807c07fb6.
* J. Björklund, Victor Falgas-Ravry, Cecilia Holmgren. On percolation in one-dimensional stable Poisson graphs. 2015. https://www.semanticscholar.org/paper/75cd1cffa51f49879cd9b823c7a4f8be2f8606b7.
* C. Hirsch. From heavy-tailed Boolean models to scale-free Gilbert graphs. 2014. https://www.semanticscholar.org/paper/b185740abf361c3a5135fd8bdba009266eee5151.
* A. Holroyd, James B. Martin. Poisson allocations with bounded connected cells. 2014. https://www.semanticscholar.org/paper/a7a3e95ecb42ac8c8cd452a922df7c7b08ca2355.
* Fabio Lopes. Invariant Bipartite Random Graphs on Rd. 2014. https://www.semanticscholar.org/paper/6f7849f87d07caaed895aaea5f28922b43676fe4.
* Peter Mörters, István Redl. Skorokhod embeddings for two-sided Markov chains. 2014. https://www.semanticscholar.org/paper/579e4da8026d6d70d0f47ed37e6d4d98b90b723c.
* Elena Boniolo, S. Caracciolo, A. Sportiello. Correlation function for the Grid-Poisson Euclidean matching on a line and on a circle. 2014. https://www.semanticscholar.org/paper/8518487b411b0522082f642e19be76ef6110b935.
* R. Lyons. Factors of IID on Trees. 2014. https://www.semanticscholar.org/paper/b2c64cc7d06c4e67db5d12e71d0182044baa3876.
* Daniel Andrés Díaz Pachón. Percolation for the stable marriage of Poisson and Lebesgue with random appetites. 2013. https://www.semanticscholar.org/paper/77a4ad7ad1a030352d42df9d30c8ec09e51160f7.
* Martin Huesmann. Optimal transport between random measures. 2012. https://www.semanticscholar.org/paper/8632f3dca3fccaa6292e289eda605aecc3d0cd4b.
* G. Donovan, G. Lythe. T-cell movement on the reticular network.. 2012. https://www.semanticscholar.org/paper/42bcc5e20cb315427e6f546ff6019f3e336f0455.
* Maria Deijfen, Fabio Lopes. Bipartite stable Poisson graphs on R. 2012. https://www.semanticscholar.org/paper/bb9a7798191e5d38f960a37d4c0fbaae91ab9d31.
* G. Last, Peter Morters, H. Thorisson. Unbiased shifts of Brownian motion. 2011. https://www.semanticscholar.org/paper/13a5654951dc607c915f6399310adb76ee686012.
* Tom Meyerovitch. Ergodicity of Poisson products and applications. 2011. https://www.semanticscholar.org/paper/12bdf179d2ed390e15b3e419c0aa0b4cc25cd3de.
* H. Thorisson. Characterization of mass-stationarity by Bernoulli and Cox transports. 2011. https://www.semanticscholar.org/paper/4fd6b0336320295643ad902966eb43f9a27c465b.
* Roland Markó, Ádám Timár. A Poisson allocation of optimal tail. 2011. https://www.semanticscholar.org/paper/4e2e19485a844f7ebe24a25aa998b6389e402ce3.
* F. Barthe, Charles Bordenave. Combinatorial Optimization Over Two Random Point Sets. 2011. https://www.semanticscholar.org/paper/4156f8e33cf4c41ad05e02d777e72c1397b1fc3e.
* Martin Huesmann, Karl-Theodor Sturm. Optimal transport from Lebesgue to Poisson. 2010. https://www.semanticscholar.org/paper/50b775509c07e16b97a06efe7ef12d37305a3e0b.
* Daniel Andrés Díaz Pachón. A Note on Large Deviations for the Stable Marriage of Poisson and Lebesgue with Random Appetites. 2010. https://www.semanticscholar.org/paper/6017b6c4de9fcd9709e78ca9fdecbef3872ab9fb.
* M. Zerner. Interpolation percolation. 2010. https://www.semanticscholar.org/paper/e84e50bacba464ece7cd261a47f844456501b0f8.
* A. Holroyd, Terry Soo. Insertion and deletion tolerance of point processes. 2010. https://www.semanticscholar.org/paper/b7984606d6d35fd2559d6dab9a4b36a191e4ec52.
* F. Nazarov, M. Sodin. Random Complex Zeroes and Random Nodal Lines. 2010. https://www.semanticscholar.org/paper/1878c6ba7d4746a8e0a67d676655ab5ce743a6d2.
* D. Aldous, Julian Shun. Connected Spatial Networks over Random Points and a Route-Length Statistic. 2010. https://www.semanticscholar.org/paper/f198ff7f947063b3d0ff251481df536500276c4d.
* Maria Deijfen, Olle Häggström, A. Holroyd. Percolation in invariant Poisson graphs with i.i.d. degrees. 2010. https://www.semanticscholar.org/paper/9e4d3835f4098345c63c9398acd466e890ea8510.
* L. Addario-Berry, Simon Griffiths, Ross J. Kang. Invasion percolation on the Poisson-weighted infinite tree. 2009. https://www.semanticscholar.org/paper/bd9e23cc2a5bcf7250faa6ff9e82189b3b97669c.
* Daniel Andrés Díaz Pachón. A Note on Large Deviations for the Stable Marriage of Poisson and Lebesgue with Random Appetites. 2009. https://www.semanticscholar.org/paper/0b7952a4ece059de5516df263366a497237a666c.
* R. Lyons, F. Nazarov. Perfect matchings as IID factors on non-amenable groups. 2009. https://www.semanticscholar.org/paper/57fcda721fb9179b56a02151bb42134001d18a03.
* Daniel Andrés Díaz–Pachón. Percolation for the stable marriage of Poisson and Lebesgue with random appetites. 2009. https://www.semanticscholar.org/paper/3cd121331864312af9248164b68d9465d409c733.
* A. Holroyd. Geometric properties of Poisson matchings. 2009. https://www.semanticscholar.org/paper/7e098dc74e9a77b0190e1ea0002afcf1adb0b466.
* A. Holroyd, R. Lyons, Terry Soo. Poisson splitting by factors. 2009. https://www.semanticscholar.org/paper/f5e2a0a3e9d18cca30736a9d2acc798dd87a78c2.
* Omer Angel, I. Benjamini, O. Gurel-Gurevich, Tom Meyerovitch, Ron Peled. Stationary map coloring. 2009. https://www.semanticscholar.org/paper/6f148aceb2e098d8244e9db637f11e0282256e96.
* Maria Deijfen. Stationary random graphs with prescribed iid degrees on a spatial Poisson process. 2009. https://www.semanticscholar.org/paper/3d6b15c1460bdd72354fcafc3c1c4515274227cd.
* Terry Soo. Translation-Equivariant Matchings of Coin Flips on ℤ d. 2006. https://www.semanticscholar.org/paper/a6d4cf50a3437fd6d9f6bd9804374e7e37169ecf.
* C. Hoffman, A. Holroyd, Y. Peres. Tail Bounds for the Stable Marriage of Poisson and Lebesgue. 2005. https://www.semanticscholar.org/paper/7a781d9e97267fd1c492adbb3c5b12999bc09ddc.
* . Hyperuniform systems via a stable matching between Poisson and lattice points sujet. 2019. https://www.semanticscholar.org/paper/8317b9886eb38ca16bd270f9476b029109f9a2a0.
* J. Martin. Part C project : Stable matchings Supervisor : James Martin Stable marriage. 2016. https://www.semanticscholar.org/paper/4d425b1f00311a23f015cf360c04d1b921dc4331.
* Peter Mörters, H. Thorisson. UNBIASED SHIFTS OF BROWNIAN MOTION1 BY GÜNTER LAST,. 2014. https://www.semanticscholar.org/paper/bfd9ef96f891011493bac5976d74adbab676ec00.
* James B. Martin. Part C project : Stable matchings Supervisor : James Martin Stable marriage. 2013. https://www.semanticscholar.org/paper/3e996a15184b1d2e410656c58af42c1180b5c5d9.
* Fabio Lopes. Fe b 20 12 Invariant bipartite random graphs on R d. 2012. https://www.semanticscholar.org/paper/506bed1ced3704f60ccd3d4a514f7ef15f4cf2a1.
* J. Jonges, M. Heydenreich. Geometric properties of Poisson matchings. 2012. https://www.semanticscholar.org/paper/7de55e72aec63d17fb3bc6aeaa4bdb5712f19ee5.
* G. Last. Characterization of mass-stationarity by Bernoulli and Cox transports. 2010. https://www.semanticscholar.org/paper/5f6549499c831b347482c0e264f87c52174fccfa.
* Terry Soo. Coupling, matching, and equivariance. 2010. https://www.semanticscholar.org/paper/dd66ab62eb1ca2240fd6859341fa2c1e5dd4eaca.
* D. Aldous, Julian Shun. Models for Connected Networks over Random Points and a Route-Length Statistic. 2008. https://www.semanticscholar.org/paper/15b9f06c917e6e8686951d90b0d997d5f7b59f93.
* S. Caracciolo. Statistical properties of the random 2-dimensional euclidean Grid-Poisson Marriage problem. 2008. https://www.semanticscholar.org/paper/27ec23a66afcbc97581e97a73bb0a59f140debba.

## Second-attempt follow-up (2026-10-11)

The brain was queried on residual-charge covariance/boundary flux, Harris association/add-one cost, and 'Poisson Poincare inequality Last Penrose add-one difference operator'. The relevant retrieved pointers were Harris association and Last-Penrose's Lectures on the Poisson Process. Generic Gaussian Poincare/fourth-chaos statements were rejected as inapplicable. The needed variance estimate is instead proved self-contained by binomial-slot tensorization in SECOND_ATTEMPT.md section C.

Primary source checked again: Holroyd-Martin-Peres, arXiv:1708.04519v2, Proposition 2.2, PDF p.8: fixed-threshold status depends on the finite set of decreasing paths. SECOND_ATTEMPT.md section D reproves the needed Poisson localization rather than treating the reference as a black box. Source Poisson matching Lemmas 16-17, PDF pp.25-27, were also rechecked for removal of matched pairs and opposite-colour insertion; the same-side comparison was derived explicitly.

No new published solution is asserted. The new upper bound and d=2 criterion are derivations in this attempt, whose novelty has not been independently assessed. The full d>=3 critical lower moment is still not obtained.

* 2026-10-11 - arxiv_second_attempt - `https://export.arxiv.org/api/query?search_query=all:%22stable%20matching%22%20AND%20all:Poisson%20AND%20(all:variance%20OR%20all:Poincare%20OR%20all:exponent)&max_results=50` - saved second_arxiv.xml; 0 entries. A zero-result keyword query is not evidence of mathematical novelty.
