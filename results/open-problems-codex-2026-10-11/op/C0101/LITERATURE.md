
## API searches, 2026-10-12
- {"date": "2026-10-12", "service": "arxiv", "query": "integer superharmonic matrices", "url": "https://export.arxiv.org/api/query", "params": {"search_query": "all:\"integer superharmonic\"", "max_results": 50}, "status": 200, "request_url": "https://export.arxiv.org/api/query?search_query=all%3A%22integer+superharmonic%22&max_results=50", "response_file": "arxiv_0.txt"}
- {"date": "2026-10-12", "service": "arxiv", "query": "higher dimensional sandpile matrices", "url": "http://export.arxiv.org/api/query", "params": {"search_query": "all:sandpile AND all:superharmonic", "max_results": 50}, "status": 200, "request_url": "https://export.arxiv.org/api/query?search_query=all%3Asandpile+AND+all%3Asuperharmonic&max_results=50", "response_file": "arxiv_1.txt"}
- {"date": "2026-10-12", "service": "openalex", "query": "integer superharmonic matrices", "url": "https://api.openalex.org/works", "params": {"search": "integer superharmonic matrices", "per-page": 100}, "status": 429, "request_url": "https://api.openalex.org/works?search=integer+superharmonic+matrices&per-page=100", "response_file": "openalex_2.txt"}
- {"date": "2026-10-12", "service": "openalex", "query": "source lookup", "url": "https://api.openalex.org/works", "params": {"search": "Laplacian growth sandpiles and scaling limits", "per-page": 5}, "status": 429, "request_url": "https://api.openalex.org/works?search=Laplacian+growth+sandpiles+and+scaling+limits&per-page=5", "response_file": "openalex_3.txt"}
- {"date": "2026-10-12", "service": "crossref", "query": "integer superharmonic matrices", "url": "https://api.crossref.org/works", "params": {"query": "integer superharmonic matrices", "rows": 40}, "status": 200, "request_url": "https://api.crossref.org/works?query=integer+superharmonic+matrices&rows=40", "response_file": "crossref_4.txt"}
- {"date": "2026-10-12", "service": "semantic_scholar", "query": "integer superharmonic matrices", "url": "https://api.semanticscholar.org/graph/v1/paper/search", "params": {"query": "integer superharmonic matrices", "limit": 50, "fields": "title,authors,year,externalIds,abstract,url"}, "status": 429, "request_url": "https://api.semanticscholar.org/graph/v1/paper/search?query=integer+superharmonic+matrices&limit=50&fields=title%2Cauthors%2Cyear%2CexternalIds%2Cabstract%2Curl", "response_file": "semantic_scholar_5.txt"}
- {"date": "2026-10-12", "service": "github", "query": "integer superharmonic", "url": "https://api.github.com/search/repositories", "params": {"q": "\"integer superharmonic\"", "per_page": 50}, "status": 200, "request_url": "https://api.github.com/search/repositories?q=%22integer+superharmonic%22&per_page=50", "response_file": "github_6.txt"}
- {"date": "2026-10-12", "service": "github", "query": "sandpile higher dimension", "url": "https://api.github.com/search/repositories", "params": {"q": "sandpile higher dimension", "per_page": 50}, "status": 200, "request_url": "https://api.github.com/search/repositories?q=sandpile+higher+dimension&per_page=50", "response_file": "github_7.txt"}

## Follow-up searches and fetches, 2026-10-12
- {"date": "2026-10-12", "service": "crossref_source", "url": "https://api.crossref.org/works", "query": {"query.title": "Laplacian growth sandpiles and scaling limits", "rows": 3}, "status": 200, "request_url": "https://api.crossref.org/works?query.title=Laplacian+growth+sandpiles+and+scaling+limits&rows=3"}
- {"date": "2026-10-12", "service": "openalex_retry", "url": "https://api.openalex.org/works", "query": {"search": "\"integer superharmonic\"", "per_page": 25}, "status": 429, "request_url": "https://api.openalex.org/works?search=%22integer+superharmonic%22&per_page=25"}
- {"date": "2026-10-12", "service": "openalex_source", "url": "https://api.openalex.org/works/https://doi.org/10.1090/bull/1553", "query": {}, "status": 429, "request_url": "https://api.openalex.org/works/https://doi.org/10.1090/bull/1553"}
- {"date": "2026-10-12", "service": "semantic_bulk", "url": "https://api.semanticscholar.org/graph/v1/paper/search/bulk", "query": {"query": "\"integer superharmonic\"", "fields": "title,year,authors,externalIds,abstract"}, "status": 200, "request_url": "https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=%22integer+superharmonic%22&fields=title%2Cyear%2Cauthors%2CexternalIds%2Cabstract"}
- {"date": "2026-10-12", "service": "semantic_source", "url": "https://api.semanticscholar.org/graph/v1/paper/ARXIV:1611.00411/citations", "query": {"limit": 100, "fields": "title,year,authors,externalIds,abstract"}, "status": 200, "request_url": "https://api.semanticscholar.org/graph/v1/paper/ARXIV:1611.00411/citations?limit=100&fields=title%2Cyear%2Cauthors%2CexternalIds%2Cabstract"}
- {"date": "2026-10-12", "service": "arxiv_higher", "url": "https://export.arxiv.org/api/query", "query": {"search_query": "all:sandpile AND (all:\"higher dimensions\" OR all:\"maximal matrices\")", "max_results": 60}, "status": 200, "request_url": "https://export.arxiv.org/api/query?search_query=all%3Asandpile+AND+%28all%3A%22higher+dimensions%22+OR+all%3A%22maximal+matrices%22%29&max_results=60"}
- {"date": "2026-10-12", "service": "f_lattice", "url": "https://arxiv.org/pdf/2110.07556", "query": {}, "error": "('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))"}
- {"date": "2026-10-12", "service": "solitons", "url": "https://arxiv.org/pdf/2212.03717", "query": {}, "status": 200, "request_url": "https://arxiv.org/pdf/2212.03717"}

## Final follow-up searches, 2026-10-12
- {"date": "2026-10-12", "service": "openalex_correct_source", "url": "https://api.openalex.org/works/https://doi.org/10.1090/bull/1573", "query": {}, "status": 429, "request_url": "https://api.openalex.org/works/https://doi.org/10.1090/bull/1573"}
- {"date": "2026-10-12", "service": "openalex_citing_source", "url": "https://api.openalex.org/works", "query": {"filter": "cites:https://doi.org/10.1090/bull/1573", "per-page": 100}, "status": 429, "request_url": "https://api.openalex.org/works?filter=cites%3Ahttps%3A%2F%2Fdoi.org%2F10.1090%2Fbull%2F1573&per-page=100"}
- {"date": "2026-10-12", "service": "semantic_citing_lps", "url": "https://api.semanticscholar.org/graph/v1/paper/ARXIV:1309.3267/citations", "query": {"limit": 100, "fields": "title,year,authors,externalIds,abstract"}, "status": 200, "request_url": "https://api.semanticscholar.org/graph/v1/paper/ARXIV:1309.3267/citations?limit=100&fields=title%2Cyear%2Cauthors%2CexternalIds%2Cabstract"}
- {"date": "2026-10-12", "service": "arxiv_superharmonic_dimension", "url": "https://export.arxiv.org/api/query", "query": {"search_query": "all:superharmonic AND (all:sandpile OR all:\"integer-valued\") AND (all:dimension OR all:matrices)", "max_results": 80}, "status": 200, "request_url": "https://export.arxiv.org/api/query?search_query=all%3Asuperharmonic+AND+%28all%3Asandpile+OR+all%3A%22integer-valued%22%29+AND+%28all%3Adimension+OR+all%3Amatrices%29&max_results=80"}
- {"date": "2026-10-12", "service": "f_lattice_retry", "url": "https://arxiv.org/pdf/2110.07556v2", "query": {}, "status": 200, "request_url": "https://arxiv.org/pdf/2110.07556v2"}

# Literature assessment — 2026-10-12

No inspected paper states and proves the d≥3 maximal-element classification or the isolation/rationality questions. This is a bounded search result, not a proof that no solution exists. Verdict is PARTIAL, not SOLVED_IN_LITERATURE.


## Source and exact question

Lionel Levine and Yuval Peres, *Laplacian growth, sandpiles, and scaling limits*, Bulletin of the American Mathematical Society 54 (2017), 355–382. DOI: 10.1090/bull/1573; arXiv:1611.00411v1. Downloaded `source.pdf`, extracted `source.txt`; open problem 9(4), printed/PDF p.27. The set Γ is defined on printed/PDF p.21 as the Euclidean closure of matrices A for which Δceil(x^T A x/2) stabilizes locally.

Exact question (PDF text, with line breaks retained):

```text
(4) As proved in [47] (and illustrated in Figure 7), the maximal elements of
Γ(Z2) correspond to the circles in the Apollonian band packing of R2.
Because the radius and the coordinates of the center of each such circle
are rational numbers, each maximal element of Γ(Z2) is a matrix with
rational entries. Describe the maximal elements of Γ(Zd) for d ≥3. Are
they isolated? Do they have rational entries?
```

Hypotheses: real symmetric d-by-d matrices, standard nearest-neighbor Z^d, degree 2d, integer heights, unstable at height≥2d, d≥3. The semidefinite order used by the cited classification is A≤B iff B-A is positive semidefinite (apollonian.pdf p.2). The survey does not define a different order. Isolation is interpreted relative to the maximal set.


## Relevant papers and why they do not settle C0101

1. Lionel Levine, Wesley Pegden, Charles K. Smart, *The Apollonian structure of integer superharmonic matrices*, Annals of Mathematics 186(1) (2017), 1–67. DOI: 10.4007/annals.2017.186.1.1; arXiv:1309.3267v4. Downloaded and inspected pp.1–4. Theorem 1.1, p.2, classifies 2-by-2 matrices; its Laplacian threshold is 1 and its representatives have q_A+o(|x|²) growth. These differ in normalization from the survey threshold 3 in d=2. No d≥3 classification is asserted. Theorem 1.2 constructs full-rank affine-periodic representatives: a lead for rationality, not a higher-dimensional theorem.

2. Ahmed Bou-Rabee, *Integer superharmonic matrices on the F-lattice*, Advances in Mathematics 436 (January 2024), article 109400. DOI: 10.1016/j.aim.2023.109400; arXiv:2110.07556v2 (5 November 2023). Downloaded on retry and inspected pp.1–6, Theorems 1.1–1.3. The F-lattice is a directed periodic planar graph on Z^2. Theorem 1.1 classifies its cone packing; Theorem 1.3 supplies affine-periodic odometers. Different graph and dimension: not a solution for nearest-neighbor Z^d, d≥3.

3. Nikita Kalinin, *Sandpile solitons in higher dimensions*, arXiv:2212.03717v1 (6 December 2022); DOI: 10.1007/s40598-023-00224-7. Downloaded and inspected pp.1–2. Theorem 1, p.2, classifies hyperplane-shaped movable soliton states, not quadratic Hessians. The author says on p.2: "For example, there is no classification of patterns via quadratic forms similar to [10, 8] in dimensions more than two." This is evidence for status as of that manuscript, not an exhaustive current-status theorem.

4. Nikita Kalinin and Mikhail Shkolnikov, *Sandpile solitons via smoothing of superharmonic functions*, arXiv:1711.04285; DOI: 10.1007/s00220-020-03828-8. The retrieved arXiv abstract concerns piecewise-linear functions on Z^2. A technique lead; no quadratic maximal-matrix classification.

5. Ahmed Bou-Rabee, *Dynamic Dimensional Reduction in the Abelian Sandpile*, arXiv:2009.05968; DOI: 10.1007/s00220-022-04322-z. Found in citation lists; this concerns sandpile dynamics, and no exact C0101 solution is claimed from its metadata. Do not assume arbitrary quadratic representatives separate across coordinates.


## Search results and limitations


arxiv_0.txt: 3 returned entries.

- Integer superharmonic matrices on the $F$-lattice; http://arxiv.org/abs/2110.07556v2

- The Apollonian structure of integer superharmonic matrices; http://arxiv.org/abs/1309.3267v4

- Apollonian structure in the Abelian sandpile; http://arxiv.org/abs/1208.4839v2


arxiv_1.txt: 6 returned entries.

- Sandpile solitons via smoothing of superharmonic functions; http://arxiv.org/abs/1711.04285v1

- The Apollonian structure of integer superharmonic matrices; http://arxiv.org/abs/1309.3267v4

- Integer superharmonic matrices on the $F$-lattice; http://arxiv.org/abs/2110.07556v2

- Apollonian structure in the Abelian sandpile; http://arxiv.org/abs/1208.4839v2

- Sandpile solitons in higher dimensions; http://arxiv.org/abs/2212.03717v1

- Tropical curves in sandpile models; http://arxiv.org/abs/1502.06284v10


arxiv_higher.json: 9 returned entries.

- Strong Spherical Asymptotics for Rotor-Router Aggregation and the Divisible Sandpile; http://arxiv.org/abs/0704.0688v5

- Sandpile solitons in higher dimensions; http://arxiv.org/abs/2212.03717v1

- Computational complexity of the avalanche problem on one dimensional Kadanoff sandpiles; http://arxiv.org/abs/1803.05498v1

- Generic Sandpile Models Have Directed Percolation Exponents; http://arxiv.org/abs/cond-mat/0202345v2

- Fermionic Gaussian free field structure in the Abelian sandpile model and uniform spanning tree; http://arxiv.org/abs/2309.08349v1

- Pattern Formation in Growing Sandpiles with Multiple Sources or Sinks; http://arxiv.org/abs/0909.3192v1

- Limit Theorems for Internal Aggregation Models; http://arxiv.org/abs/0712.4358v1

- Facilitated Exclusion Process in Higher Dimensions: Recurrent Structure and Transient Dynamics; http://arxiv.org/abs/2609.18885v1

- Simplicial and Cellular Trees; http://arxiv.org/abs/1506.06819v1


arxiv_superharmonic_dimension.txt: 3 returned entries.

- The Apollonian structure of integer superharmonic matrices; http://arxiv.org/abs/1309.3267v4

- Sandpile solitons in higher dimensions; http://arxiv.org/abs/2212.03717v1

- Integer superharmonic matrices on the $F$-lattice; http://arxiv.org/abs/2110.07556v2


semantic_source.json: 32 citation records; next=None. Titles and returned abstracts screened for this question; no matching solution identified. Raw responses retained.

- Kozma's centrally excited walk converges to a Euclidean ball (2026); {"ArXiv": "2610.10162", "CorpusId": 292700558}

- Limit shape, avalanches, and stabilisation of abelian sandpiles on comb lattices (2026); {"ArXiv": "2609.21359", "CorpusId": 292193950}

- Eulerian walkers on $\mathbb{Z}^2$ have range exponent $2/3$ (2026); {"ArXiv": "2608.23545", "CorpusId": 291328792}

- Over-squashing as Transport Congestion: A Sandpile Dynamics Perspective (2026); {"DOI": "10.1145/3770855.3817690", "CorpusId": 290858157}

- Gaussian fluctuations for Internal DLA on cylinders (2026); {"ArXiv": "2604.21142", "CorpusId": 287702070}

- Divisible sandpiles via random walks in random scenery (2026); {"ArXiv": "2604.13968", "CorpusId": 287480574}

- On structural connections between sandpile monoids and weighted Leavitt path algebras (2025); {"DOI": "10.1016/j.jalgebra.2025.04.034", "CorpusId": 278387703}

- Unital algebras being Morita equivalent to weighted Leavitt path algebras (2023); {"ArXiv": "2312.15704", "DOI": "10.1007/s10801-025-01454-y", "CorpusId": 266551876}

- A flow‐type scaling limit for random growth with memory (2023); {"ArXiv": "2310.17572", "DOI": "10.1002/cpa.22241", "CorpusId": 264490775}

- Harmonic balls in Liouville quantum gravity (2022); {"ArXiv": "2208.11795", "DOI": "10.1112/plms.70018", "CorpusId": 251800255}

- Existence of a phase transition in harmonic activation and transport (2021); {"ArXiv": "2110.13893", "DOI": "10.1214/23-ejp1004", "CorpusId": 239885541}

- A shape theorem for exploding sandpiles (2021); {"ArXiv": "2102.04422", "DOI": "10.1214/23-AAP1976", "CorpusId": 231847113}

- The Limit Shape of the Leaky Abelian Sandpile Model (2020); {"MAG": "3168192402", "ArXiv": "2010.01946", "DOI": "10.1093/IMRN/RNAB124", "CorpusId": 222133085}

- Dynamic Dimensional Reduction in the Abelian Sandpile (2020); {"ArXiv": "2009.05968", "MAG": "3084946543", "DOI": "10.1007/s00220-022-04322-z", "CorpusId": 221655055}

- Sandpile Toppling on Penrose Tilings: Identity and Isotropic Dynamics (2020); {"DBLP": "conf/birthday/FersulaNP22", "MAG": "3034791786", "ArXiv": "2006.06254", "DOI": "10.1007/978-3-030-92551-2_10", "CorpusId": 219573440}

- Characterizing immutable sandpiles: A first look (2020); {"DBLP": "journals/dm/DuncanE22", "MAG": "3031548763", "ArXiv": "2006.00041", "DOI": "10.1016/j.disc.2021.112657", "CorpusId": 219177018}

- Asymptotic Height Distribution in High-Dimensional Sandpiles (2019); {"DOI": "10.1007/s10959-019-00962-5", "CorpusId": 254747362}

- Asymptotic Height Distribution in High-Dimensional Sandpiles (2019); {"MAG": "2988752889", "ArXiv": "1911.01762", "DOI": "10.1007/s10959-019-00962-5", "CorpusId": 207870067}

- How Hard is it to Predict Sandpiles on Lattices? A Survey (2019); {"DBLP": "journals/corr/abs-1909-12150", "ArXiv": "1909.12150", "MAG": "2991512099", "DOI": "10.3233/FI-2020-1879", "CorpusId": 202889165}

- Non-Archimedean Coulomb gases (2019); {"MAG": "2964789256", "ArXiv": "1908.00571", "DOI": "10.1063/1.5127191", "CorpusId": 199405299}

- Odometers of Divisible Sandpile Models: Scaling Limits, iDLA and Obstacle Problems. A Survey (2019); {"MAG": "2921498481", "ArXiv": "1903.06263", "CorpusId": 119142817}

- Averaging Principle and Shape Theorem for a Growth Model with Memory (2018); {"ArXiv": "1812.00726", "MAG": "2902214024", "DOI": "10.1002/cpa.21965", "CorpusId": 119720190}

- The Dispersion Time of Random Walks on Finite Graphs (2018); {"DBLP": "journals/corr/abs-1808-09219", "MAG": "2949654691", "ArXiv": "1808.09219", "DOI": "10.1145/3323165.3323204", "CorpusId": 52111558}

- Constructing fractional Gaussian fields from long-range divisible sandpiles on the torus (2018); {"MAG": "3173680814", "ArXiv": "1808.06078", "DOI": "10.1016/J.SPA.2021.06.006", "CorpusId": 235446711}

- Perturbed Divisible Sandpiles and Quadrature Surfaces (2018); {"DOI": "10.1007/s11118-018-9722-6", "CorpusId": 254935036}

- Laplacian growth and sandpiles on the Sierpiński gasket: limit shape universality and exact solutions (2018); {"MAG": "3107993293", "ArXiv": "1807.08748", "DOI": "10.4171/aihpd/95", "CorpusId": 51752597}

- DIVISIBLE SANDPILE ON SIERPINSKI GASKET GRAPHS (2017); {"MAG": "2949835788", "ArXiv": "1702.08370", "DOI": "10.1142/S0218348X19500324", "CorpusId": 119713998}

- Perfect boundaries in rotor-router aggregation on cylinders (2016); {"MAG": "2562893794", "ArXiv": "1612.03701", "DOI": "10.1088/1751-8121/aa7316", "CorpusId": 119604556}

- Tropical curves in sandpile models (2015); {"ArXiv": "1502.06284", "MAG": "2256260167", "DOI": "10.1016/j.aim.2026.111127", "CorpusId": 119141202}

- Sandpile models (2014); {"MAG": "2891940028", "ArXiv": "1401.0354", "DOI": "10.1214/14-ps228", "CorpusId": 52952787}

- Leaky Abelian Sandpile Model With Multiple Starting Points (2022); {"CorpusId": 251537762}

- My title (2021); {"CorpusId": 235488559}


semantic_citing_lps.txt: 44 citation records; next=None. Titles and returned abstracts screened for this question; no matching solution identified. Raw responses retained.

- Eulerian walkers on $\mathbb{Z}^2$ have range exponent $2/3$ (2026); {"ArXiv": "2608.23545", "CorpusId": 291328792}

- Scaling and partial universality of the height zero probability in the 2D Abelian sandpile (2026); {"ArXiv": "2607.26169", "CorpusId": 290644744}

- Activated random walk exhibits self-organized criticality (2026); {"ArXiv": "2605.00207", "CorpusId": 287929293}

- The odometer in subcritical activated random walk (2025); {"ArXiv": "2510.05514", "CorpusId": 281887014}

- Cutoff for activated random walk (2025); {"ArXiv": "2501.17938", "CorpusId": 275993840}

- Sandpile patterns on a regular graph of degree eight (2025); {"DOI": "10.22405/2226-8383-2024-25-3-47-69", "CorpusId": 278850405}

- Evolutive sandpiles (2024); {"ArXiv": "2404.13137", "DOI": "10.1016/j.physa.2024.130248", "CorpusId": 269292946}

- Sandpiles on the Vicsek fractal explode with probability 14 (2023); {"ArXiv": "2312.13647", "DOI": "10.3150/24-bej1814", "CorpusId": 266435646}

- Fermionic Gaussian free field structure in the Abelian sandpile model and uniform spanning tree (2023); {"ArXiv": "2309.08349", "CorpusId": 262013621}

- On the Importance of Illustration for Mathematical Research (2023); {"ArXiv": "2307.04636", "DOI": "10.1090/noti2839", "CorpusId": 259501580}

- Universality conjectures for activated random walk (2023); {"ArXiv": "2306.01698", "DOI": "10.1214/24-ps25", "CorpusId": 259064234}

- Sandpile group of infinite graphs (2023); {"ArXiv": "2305.05346", "CorpusId": 258564909}

- Sandpile Solitons in Higher Dimensions (2022); {"ArXiv": "2212.03717", "DOI": "10.1007/s40598-023-00224-7", "CorpusId": 254366423}

- Exact sampling and fast mixing of activated random walk (2021); {"ArXiv": "2110.14008", "DOI": "10.1214/24-ejp1220", "CorpusId": 239998377}

- Integer superharmonic matrices on the F-lattice (2021); {"ArXiv": "2110.07556", "DOI": "10.1016/j.aim.2023.109400", "CorpusId": 238857112}

- A shape theorem for exploding sandpiles (2021); {"ArXiv": "2102.04422", "DOI": "10.1214/23-AAP1976", "CorpusId": 231847113}

- Pattern Formation and Tropical Geometry (2020); {"MAG": "3095984714", "DOI": "10.3389/fphy.2020.581126", "CorpusId": 227059864}

- How Far do Activated Random Walkers Spread from a Single Source? (2020); {"MAG": "3094972408", "ArXiv": "2011.02535", "DOI": "10.1007/s10955-021-02836-9", "CorpusId": 226254455}

- Dynamic Dimensional Reduction in the Abelian Sandpile (2020); {"ArXiv": "2009.05968", "MAG": "3084946543", "DOI": "10.1007/s00220-022-04322-z", "CorpusId": 221655055}

- Computing sandpile configurations using integer linear programming (2020); {"ArXiv": "2008.13672", "MAG": "3081645493", "DOI": "10.1016/j.chaos.2023.113356", "CorpusId": 221377182}

- The sandpile identity element on an ellipse (2020); {"ArXiv": "2007.05792", "MAG": "3041383117", "DOI": "10.3934/dcds.2022029", "CorpusId": 220495800}

- Sandpile Toppling on Penrose Tilings: Identity and Isotropic Dynamics (2020); {"DBLP": "conf/birthday/FersulaNP22", "MAG": "3034791786", "ArXiv": "2006.06254", "DOI": "10.1007/978-3-030-92551-2_10", "CorpusId": 219573440}

- Stability of Patterns in the Abelian Sandpile (2020); {"DOI": "10.1007/s00023-020-00898-1", "CorpusId": 253591760}

- How Hard is it to Predict Sandpiles on Lattices? A Survey (2019); {"DBLP": "journals/corr/abs-1909-12150", "ArXiv": "1909.12150", "MAG": "2991512099", "DOI": "10.3233/FI-2020-1879", "CorpusId": 202889165}

- Convergence of the random Abelian sandpile (2019); {"MAG": "2974173547", "ArXiv": "1909.07849", "DOI": "10.1214/21-AOP1528", "CorpusId": 202583283}

- Flow-firing processes (2019); {"MAG": "3049115133", "ArXiv": "1902.02404", "DBLP": "journals/jcta/FelzenszwalbK21", "DOI": "10.1016/j.jcta.2020.105308", "CorpusId": 119578391}

- Laplacian growth and sandpiles on the Sierpiński gasket: limit shape universality and exact solutions (2018); {"MAG": "3107993293", "ArXiv": "1807.08748", "DOI": "10.4171/aihpd/95", "CorpusId": 51752597}

- Self-organized criticality and pattern emergence through the lens of tropical geometry (2018); {"MAG": "2952897042", "ArXiv": "1806.09153", "DOI": "10.1073/pnas.1805847115", "CorpusId": 52013494, "PubMed": "30111541"}

- Sandpile Solitons via Smoothing of Superharmonic Functions (2017); {"ArXiv": "1711.04285", "MAG": "3068355630", "DOI": "10.1007/s00220-020-03828-8", "CorpusId": 119300354}

- Stability of Patterns in the Abelian Sandpile (2017); {"MAG": "2752899549", "ArXiv": "1708.09432", "DOI": "10.1007/s00023-020-00898-1", "CorpusId": 119695913}

- Strong Emergence of Wave Patterns on Kadanoff Sandpiles (2017); {"MAG": "2602194643", "DBLP": "journals/combinatorics/PerrotR17", "DOI": "10.37236/5619", "CorpusId": 9471930}

- Laplacian growth, sandpiles, and scaling limits (2016); {"MAG": "2949698800", "ArXiv": "1611.00411", "DOI": "10.1090/BULL/1573", "CorpusId": 37365612}

- Do Sums of Squares Dream of Free Resolutions? (2016); {"DBLP": "journals/siaga/BlekhermanSV17", "MAG": "2469025900", "ArXiv": "1607.03551", "DOI": "10.1137/16M1084560", "CorpusId": 119134695}

- Deterministic Abelian Sandpile and square-triangle tilings (2015); {"MAG": "3099793590", "ArXiv": "1508.06107", "DOI": "10.1007/978-3-319-20155-9_23", "CorpusId": 119179819}

- Tropical curves in sandpile models (2015); {"ArXiv": "1502.06284", "MAG": "2256260167", "DOI": "10.1016/j.aim.2026.111127", "CorpusId": 119141202}

- PDEs with Compressed Solutions (2013); {"ArXiv": "1311.5850", "MAG": "2964216518", "DOI": "10.4310/CMS.2015.V13.N8.A8", "CorpusId": 117747221}

- Apollonian structure in the Abelian sandpile (2012); {"MAG": "2951312002", "ArXiv": "1208.4839", "DOI": "10.1007/s00039-016-0358-7", "CorpusId": 7455032}

- The sensual Apollonian circle packing (2012); {"MAG": "1581427425", "ArXiv": "1208.4836", "DOI": "10.1016/J.EXMATH.2016.01.001", "CorpusId": 12774652}

- Convergence of a sandpile model on a triangular lattice (2023); {"DOI": "10.4213/sm9789", "CorpusId": 265636722}

- Convergence of a sandpile on a triangular lattice under rescaling (2023); {"DOI": "10.4213/sm9789e", "CorpusId": 269098332}

- Geometry and Topology (2021); {"MAG": "3199717002", "DOI": "10.1007/978-3-030-80627-9_5", "CorpusId": 240586680}

- Tropical curves, convex domains, sandpiles and amoebas (2017); {"MAG": "3083533490", "DOI": "10.13097/ARCHIVE-OUVERTE/UNIGE:96300", "CorpusId": 229806220}

- Sparsity-Inducing Methods in Imaging Sciences and Partial Differential Equations (2015); {"MAG": "1229616552", "CorpusId": 116959276}

- Problems from the Aim Chip-firing Workshop (None); {"CorpusId": 17106089}


github_6.txt: total_count=0; incomplete_results=False.


github_7.txt: total_count=0; incomplete_results=False.


OpenAlex repeatedly returned HTTP 429: the shared anonymous IP daily budget was exhausted. The correct source DOI lookup and a citing-source filter request were attempted and logged, but source-ID resolution and the OpenAlex citing-work screen could not be completed. An earlier lookup used an incorrect DOI suffix 1553, corrected to 1573 after the successful Crossref lookup. No API keys were sought. Semantic Scholar supplied both the survey and LPS citation lists instead.

Semantic Scholar standard search initially returned HTTP 429; bulk search and citation endpoints succeeded. Crossref supplied the source DOI and publication metadata and found the planar and F-lattice classification papers. GitHub repository searches yielded no relevant solution.


## Read-only research brain and earlier attempts

Ran math_recall.py "integer superharmonic matrices" and brain.py recall "integer superharmonic matrices mistakes" and "sandpile integer superharmonic". Read the C0101 entries in the seven probability_1000_intake directories (matching entries saved in earlier_intake.txt), and the w332/w346 files under codex_pool_2026_10_10. Listed matching origin/master paths in math-open-problems and read the C0101 report through git show. No repository working tree or brain store was edited.

The old bound Δceil(a n²/2)≤a+1 is false (a=1/2, n=0 gives 2>3/2). The old claim of coordinate separation does not prove diagonal classification. The binomial-quadratic identity is valid but needed the closure connection and trace bound proved in ATTEMPT.md before maximality followed. Packing analogies and higher-dimensional Descartes arithmetic provide no Γ correspondence.

## Exact bibliographic metadata follow-up (Crossref, 2026-10-12)

- 10.1007/s40598-023-00224-7; HTTP 200; {"title": ["Sandpile Solitons in Higher Dimensions"], "author": [{"ORCID": "https://orcid.org/0000-0002-1613-5175", "authenticated-orcid": false, "given": "Nikita", "family": "Kalinin", "sequence": "first", "affiliation": [], "role": [{"vocabulary": "crossref", "role": "author"}]}], "container-title": ["Arnold Mathematical Journal"], "volume": "9", "issue": "3", "page": "435-454", "published": {"date-parts": [[2023, 1, 30]]}, "DOI": "10.1007/s40598-023-00224-7"}

- 10.1007/s00220-020-03828-8; HTTP 200; {"title": ["Sandpile Solitons via Smoothing of Superharmonic Functions"], "author": [{"ORCID": "https://orcid.org/0000-0002-1613-5175", "authenticated-orcid": false, "given": "Nikita", "family": "Kalinin", "sequence": "first", "affiliation": [], "role": [{"vocabulary": "crossref", "role": "author"}]}, {"given": "Mikhail", "family": "Shkolnikov", "sequence": "additional", "affiliation": [], "role": [{"vocabulary": "crossref", "role": "author"}]}], "container-title": ["Communications in Mathematical Physics"], "volume": "378", "issue": "3", "page": "1649-1675", "published": {"date-parts": [[2020, 8, 18]]}, "DOI": "10.1007/s00220-020-03828-8"}

- 10.1007/s00220-022-04322-z; HTTP 200; {"title": ["Dynamic Dimensional Reduction in the Abelian Sandpile"], "author": [{"ORCID": "https://orcid.org/0000-0002-8794-2847", "authenticated-orcid": false, "given": "Ahmed", "family": "Bou-Rabee", "sequence": "first", "affiliation": [], "role": [{"vocabulary": "crossref", "role": "author"}]}], "container-title": ["Communications in Mathematical Physics"], "volume": "390", "issue": "2", "page": "933-958", "published": {"date-parts": [[2022, 1, 31]]}, "DOI": "10.1007/s00220-022-04322-z"}
