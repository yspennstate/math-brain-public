# Literature search log: C0059
Date: 2026-10-12. Raw API responses are saved next to this file. A rate-limited request is not evidence of absence.

## Source and exact hypotheses

Nicolas Curien, *Peeling random planar maps*, Saint-Flour XLIX 2019, author preliminary version. Downloaded the supplied https://www.imo.universite-paris-saclay.fr/~nicolas.curien/cours/peccot.pdf (HTTP 200; 104 PDF pages), saved as peccot.pdf and peccot.txt. Relevant pages are also in source_excerpts.txt.

The exact question on PDF p. 93 / printed p. 89, with mathematical notation transcribed, is:

> Open question. Let q be of type a ∈ [2; 5/2), it is the case that m† is transient under P∞^(1)?

Corollary 38 immediately preceding it specifies almost-sure transience for simple random walk. Objects: rooted bipartite Boltzmann maps, root face perimeter 2 under P∞^(1), and their dual multigraphs, with parallel edges counted in simple random walk.

The type conventions are essential (PDF p. 57 / printed p. 53):

- For 2<a<5/2, admissible critical non-generic sequences with exponent a as defined in Section 5.1.3, with pure power tail rather than an arbitrary unspecified slowly varying factor.
- At a=2, **only the particular sequence (5.12) at a=2** is called type 2 in this source. It has c_q=6 and q_k=(1/4)6^(1-k) Gamma(k-3/2)/Gamma(k+1/2) for k>=2, q_1=0. Its peeling step law is nu(k)=1/(4k^2-1) for k!=0 and nu(0)=0.
- Type 5/2 means regular critical; that endpoint is excluded from C0059.

Published metadata verified through Crossref: Curien, *Peeling Random Planar Maps*, Springer (2023), DOI 10.1007/978-3-031-36854-7. Published and preliminary pagination are different.

## Relevant papers inspected: leads, not matching solutions

1. Timothy Budd and Nicolas Curien, *Geometry of infinite planar maps with high degrees*, Electron. J. Probab. **22** (2017), 1-37, DOI **10.1214/17-ejp55**, arXiv:1602.01328v2. Local PDF/text. Abstract states transience only in the dense phase 3/2<a<2. Dilute dual ball-growth exponent is (a-1/2)/(a-2); geometry is not a transience proof.
2. Timothy Budd, Nicolas Curien and Cyril Marzouk, *Infinite random planar maps related to Cauchy processes*, J. Ec. polytech. Math. **5** (2018), 749-791, DOI **10.5802/jep.82**, arXiv:1704.05297. Local author PDF dated 16 October 2018. PDF p. 4 explicitly says: “Open question 1. Is the simple random walk on M†∞ transient?” Its FPP clock estimates do not settle this. This paper covers a broader exponent-2 class than the source's type-2 convention.
3. Nicolas Curien and Cyril Marzouk, *Infinite stable Boltzmann planar maps are subdiffusive*, Probab. Math. Phys. **2** (2021), 1-26, DOI **10.2140/pmp.2021.2.1**, arXiv:1910.09623v1. Local PDF/text. Introduction explicitly refers to dilute dual transience as “still an open problem”. Primal recurrence and walk displacement bounds do not answer dual transience.
4. Emmanuel Kammerer, *On large 3/2-stable maps*, arXiv:2304.01167v2 (8 March 2024; PDF dated 11 March). Local PDF/text. Finite-map distance and diameter results; no infinite dual SRW theorem.
5. Bertrand Duplantier and Emmanuel Guitter, *Liouville Quantum Duality and Random Planar Maps II*, arXiv:2604.24180v1 (27 April 2026). Local PDF/text. Block-weighted planar maps, partition functions, metric profiles and multifractal predictions. No requested transience theorem; the model is different.
6. Ádám Timár, *Parabolic-hyperbolic dichotomy through half-plane coexistence*, arXiv:2603.13642v1 (March 2026). Local PDF/text. An embedding/percolation criterion for unimodular random maps, not C0059. Unbounded-degree SRW cannot simply be identified with conformal type.
7. Thomas Budzinski and Thomas Lehéricy, *Recurrence of the Uniform Infinite Half-Plane Map via duality of resistances*, arXiv:1912.08790 (local author PDF dated 6 November 2021). Half-plane uniform model and resistance lower bounds, not the requested plane dual family.
8. Timothy Budd, *The peeling process of infinite Boltzmann planar maps*, Electron. J. Combin. **23** (2016), DOI 10.37236/5428, arXiv:1506.01590v3. Local PDF/text. Peeling transition laws, not a solution to the requested parameter range.

9. Emmanuel Kammerer, *Gaskets of O(2) loop-decorated random planar maps*, arXiv:2411.05541v2 (7 December 2025; PDF dated 9 December). Gasket weight-sequence characterisation and stable-map identification; no SRW transience theorem.
10. Emmanuel Kammerer, *Distances on the CLE4, critical Liouville quantum gravity and 3/2-stable maps*, arXiv:2311.08571v5 (12 June 2025; PDF dated 16 June). Quantum disk decompositions and boundary-to-large-face distance limits; no SRW transience theorem.
11. Emmanuel Kammerer, *Scaling limit of first passage percolation geodesics on planar maps*, arXiv:2412.02666v3 (12 September 2025; PDF dated 15 September). PDF pp. 6-9 inspected in detail. Theorem 1.1 DOES concern the infinite Boltzmann map: it gives the number of faces along a single FPP geodesic (order n^((a-2)/(a-1)) for a>2 and (log n)^2/pi^2 at a=2). Corollaries 1.2-1.3 compare infinite-map FPP and graph-distance hulls. Theorem 1.5 gives a finite-map geodesic-tree scaling limit via coalescing jump flows. These are useful possible leads for current routing, but no SRW transience result is asserted. Neither a one-path length estimate nor the finite-tree limit supplies a square-summable overlap estimate for independently resampled paths conditional on the infinite map.

No inspected paper proves the question with the same objects, hypotheses and quantifiers. This is a bounded-search conclusion, not a certification that no solution exists. No SOLVED_IN_LITERATURE verdict is warranted.

## Brain, ledgers and earlier answers (read only)

Read math-store card claim_560307c112b22749298f254ce62750fe83ec80816ddbc130e50fc600b10bc682, brain recall queries “Boltzmann planar map dual transience mistakes” and “critical Boltzmann planar maps dual random walk”, and math recall “Boltzmann Cauchy maps resistance transience”. Their statements were treated as hints; the broad memory recalls produced no relevant verified solution.

Searched intake directories for C0059; read C0059-A001 (2026-09-07). Its putative interior threshold is unsupported: excluded-endpoint recurrence does not imply recurrence below the endpoint, primal degrees are not uniformly bounded, and exponential-root-degree recurrence criteria do not apply to arbitrary polynomial dual degrees. Its dilute volume exponent is incorrect.

Read codex_pool_2026_10_10/team_O/w342/proofs/C0059.md and located the corresponding published record with read-only git ls-tree. The earlier proof correctly gives planar bounded-degree trees with equal quartic volume growth and opposite recurrence behavior. It does not realize the Boltzmann law.

## API queries actually run

Each entry below gives the service, exact URL/query, date, HTTP outcome and raw response. Initial broad searches had irrelevant kinetic-Boltzmann matches and were refined. OpenAlex returned HTTP 429 because its shared unauthenticated daily budget is exhausted, including for the query for works citing the published source DOI. The latter therefore produced no citation list. Semantic Scholar's first response was usable, but its subsequent refined requests returned 429. Crossref's query.title request returned a non-JSON response; subsequent query.bibliographic requests succeeded. GitHub returned zero repositories for the queried terms. These limitations constrain the status check.

- 2026-10-12 openalex_source: https://api.openalex.org/works?search=Peeling+random+planar+maps&per-page=8; HTTP 429; raw: search_openalex_source.txt

- 2026-10-12 openalex: https://api.openalex.org/works?search=Boltzmann+maps+random+walk+transience&per-page=30; HTTP 429; raw: search_openalex.txt

- 2026-10-12 github: https://api.github.com/search/repositories?q=Boltzmann+maps+transience&per_page=20; HTTP 200; raw: search_github.txt

- 2026-10-12 arxiv: https://export.arxiv.org/api/query?search_query=all%3A%22Boltzmann%22+AND+%28all%3A%22transience%22+OR+all%3A%22random+walk%22%29&max_results=40; HTTP 200; raw: search_arxiv.txt

- 2026-10-12 crossref: https://api.crossref.org/works?query=Boltzmann+maps+transience+random+walk&rows=25; HTTP 200; raw: search_crossref.txt

- 2026-10-12 semantic: https://api.semanticscholar.org/graph/v1/paper/search?query=Boltzmann+maps+transience&limit=30&fields=title%2Cauthors%2Cyear%2Cabstract%2Curl%2CexternalIds; HTTP 200; raw: search_semantic.txt

- 2026-10-12 oa_retry: https://api.openalex.org/works?search=Peeling+random+planar+maps&per_page=5 HTTP 429 raw search_oa_retry.txt

- 2026-10-12 arxiv_target: https://export.arxiv.org/api/query?search_query=all%3A%22planar%22+AND+all%3A%22transience%22&max_results=60&sortBy=submittedDate&sortOrder=descending HTTP 200 raw search_arxiv_target.txt

- 2026-10-12 crossref_target: https://api.crossref.org/works?query.title=Boltzmann+planar+maps&rows=30 HTTP 429 raw search_crossref_target.txt

- 2026-10-12 arxiv_cauchy: https://export.arxiv.org/api/query?search_query=all%3A%22Cauchy%22+AND+all%3A%22maps%22&max_results=30&sortBy=submittedDate&sortOrder=descending HTTP 200 raw search_arxiv_cauchy.txt

- 2026-10-12 semantic_target: https://api.semanticscholar.org/graph/v1/paper/search?query=%22planar+maps%22+%22transience%22&limit=30&fields=title%2Cauthors%2Cyear%2Cabstract%2CexternalIds HTTP 429 raw search_semantic_target.txt

- 2026-10-12 oa_citing: https://api.openalex.org/works?filter=cites%3Ahttps%3A%2F%2Fdoi.org%2F10.1007%2F978-3-031-36854-7&per-page=50 HTTP 429 raw search_oa_citing.txt

- 2026-10-12 semantic_book: https://api.semanticscholar.org/graph/v1/paper/search?query=Peeling+random+planar+maps&limit=5&fields=title%2Cauthors%2Cyear%2CexternalIds HTTP 429 raw search_semantic_book.txt

- 2026-10-12 arxiv_maps: https://export.arxiv.org/api/query?search_query=ti%3ABoltzmann+AND+ti%3Amaps&max_results=100&sortBy=submittedDate&sortOrder=descending HTTP 200 raw search_arxiv_maps.txt

- 2026-10-12 arxiv_dual: https://export.arxiv.org/api/query?search_query=all%3A%22dual%22+AND+all%3A%22planar+maps%22&max_results=80&sortBy=submittedDate&sortOrder=descending HTTP 200 raw search_arxiv_dual.txt

- 2026-10-12 crossref_book: https://api.crossref.org/works?query.bibliographic=Nicolas+Curien+Peeling+Random+Planar+Maps&rows=5 HTTP 200 raw search_crossref_book.txt

- 2026-10-12 Crossref Infinite random planar maps related to Cauchy processes: https://api.crossref.org/works?query.bibliographic=Infinite+random+planar+maps+related+to+Cauchy+processes&rows=3 HTTP 200; raw search_cauchy_ref.txt

- 2026-10-12 Crossref Geometry of infinite planar maps with high degrees: https://api.crossref.org/works?query.bibliographic=Geometry+of+infinite+planar+maps+with+high+degrees&rows=3 HTTP 200; raw search_geometry_ref.txt

- 2026-10-12 Crossref Infinite stable Boltzmann planar maps are subdiffusive: https://api.crossref.org/works?query.bibliographic=Infinite+stable+Boltzmann+planar+maps+are+subdiffusive&rows=3 HTTP 200; raw search_subdiffusive_ref.txt

- 2026-10-12 arXiv: https://export.arxiv.org/api/query?search_query=all%3A%22stable+maps%22+AND+%28all%3A%22walk%22+OR+all%3A%22resistance%22%29&max_results=60&sortBy=submittedDate&sortOrder=descending HTTP 200 raw search_arxiv_stable.txt

- 2026-10-12 arXiv: https://export.arxiv.org/api/query?search_query=ti%3Atransience+AND+all%3ABoltzmann&max_results=60&sortBy=submittedDate&sortOrder=descending HTTP 200 raw search_arxiv_transience_b.txt

- 2026-10-12 arXiv: https://export.arxiv.org/api/query?search_query=au%3AKammerer+AND+all%3Amaps&max_results=60&sortBy=submittedDate&sortOrder=descending HTTP 200 raw search_arxiv_kammerer.txt

- 2026-10-12 paper fetch https://arxiv.org/pdf/2411.05541 HTTP 200; 20 pages, local 2411.05541.pdf/.txt

- 2026-10-12 paper fetch https://arxiv.org/pdf/2412.02666 HTTP 200; 57 pages, local 2412.02666.pdf/.txt

- 2026-10-12 paper fetch https://arxiv.org/pdf/2311.08571 HTTP 200; 73 pages, local 2311.08571.pdf/.txt

## Download inventory (2026-10-12)
Source supplied URL fetched with Python requests, HTTP 200. Each arXiv PDF was fetched from https://arxiv.org/pdf/<id> with Python requests, HTTP 200, and extracted using PyMuPDF: 1506.01590, 1602.01328, 1704.05297, 1910.09623, 1912.08790, 2304.01167, 2603.13642, 2604.24180, 2311.08571, 2411.05541, 2412.02666. These downloads are document inspections, not additional indexed literature searches. No built-in web search was used.

- Second attempt, 2026-10-12: berger_arxiv https://export.arxiv.org/api/query?search_query=ti%3A%22Transience%22+AND+au%3A%22Berger%22&max_results=20 HTTP 200; raw second_berger_arxiv.txt

- Second attempt, 2026-10-12: berger_crossref https://api.crossref.org/works?query.bibliographic=Noam+Berger+Transience+recurrence+and+critical+behavior+for+long-range+percolation&rows=3 HTTP 200; raw second_berger_crossref.txt

- Second attempt, 2026-10-12: schur_arxiv https://export.arxiv.org/api/query?search_query=all%3A%22Kron+reduction%22+AND+all%3A%22resistance%22&max_results=10 HTTP 200; raw second_schur_arxiv.txt

- 2026-10-12 document fetch https://arxiv.org/pdf/math/0110296 HTTP 200; second_math_0110296.pdf/text

- 2026-10-12 document fetch https://arxiv.org/pdf/1102.2950 HTTP 200; second_1102.2950.pdf/text

## Second attempt: gap-oriented recalls and neighbouring literature
2026-10-12. Read ATTEMPT.md fully and its exact remaining gap. Math-store queries, each a separate read-only call: (1) "Boltzmann dual map effective resistance harmonic measure independent geodesics overlap"; (2) "star mesh Schur complement trace Dirichlet long range percolation Berger transience"; (3) "Berger transience recurrence critical behavior long range percolation". No retrieved card solved the gap. General Schur-complement and electrical identities were checked directly rather than accepted as applicable infinite-network theorems.

- Noam Berger, *Transience, Recurrence and Critical Behavior for Long-Range Percolation*, Commun. Math. Phys. 226 (2002), 531-558, DOI 10.1007/s002200200617, arXiv:math/0110296v3. Verified Theorem 1.4 at PDF p. 3 (independent Z^2 long-range percolation: transient for 2<s<4, recurrent for s>=4) and Theorem 1.9 at PDF p. 5 (iid conductances on a recurrent bounded-degree graph preserve recurrence). Neither covers the correlated face-clique trace or the correlated weighted medial comparison network. Lead only, not SOLVED_IN_LITERATURE.
- Florian Doerfler and Francesco Bullo, *Kron Reduction of Graphs with Applications to Electrical Networks*, arXiv:1102.2950. Finite-network Schur-complement background. Its finite theorem is not applied by taking an unjustified infinite matrix inverse; SECOND_ATTEMPT.md proves the particular infinite trace via compact-support energy and local flows.
- Source reinspection: Curien preliminary notes PDF p. 90, printed p. 86, explicitly state uniform-root-edge property after gluing the two root-face edges and cite Benjamini-Schramm's bounded-degree planar-limit recurrence theorem. Theorem 8 is the finite-to-infinite local-limit input. These inputs support recurrence of the medial graph, not of the nonplanar clique trace.

- Second-attempt source check, 2026-10-12: local peccot.txt Definition 7 (PDF p. 23) for h_up, Definition 17 and Proposition 22 (PDF pp. 49-51) for conditional face-discovery probabilities; (5.11)-(5.13) for positive nu tails. This corrects a tempting use of the bare nu tail in place of the size-biased discovery law. No extra online query was needed.
