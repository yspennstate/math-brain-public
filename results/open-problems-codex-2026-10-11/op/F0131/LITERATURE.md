# Literature check for F0131

Checked 2026-10-11 using Python requests only. No theorem answering Question 6.2 exactly was located in this bounded check. This is not a claim that the literature search is exhaustive. The later papers are inputs to the attempted counterexample, not a solution in print.

## Source verification

Alexander E. Holroyd, Lionel Levine, Karola Meszaros, Yuval Peres, James Propp, David B. Wilson, **Chip-Firing and Rotor-Routing on Directed Graphs**, in *In and Out of Equilibrium 2*, Progress in Probability 60 (2008), DOI 10.1007/978-3-7643-8786-0_17, arXiv:0801.3306. Retrieved PDF saved as downloads/source.pdf; numbered text as downloads/source.txt.

PDF page 29, Question 6.2 (line breaks removed):

> Question 6.2. In Z2, is the limiting shape of Sn,H as n → ∞ a regular (4H + 12)-gon? Simulations indicate a regular (4H + 12)-gon with some “rounding” at the corners; it remains unclear if the rounded portions of th e boundary become negligible in the limit. Even if the limiting shape is not a po lygon, it would still be very interesting to establish the weaker statement that it h as the dihedral symmetry D4H+12.

Hypotheses checked in the preceding paragraph: cubic lattice, integer background h<=2 in dimension two, H=-h, add n at the origin, ordinary four-neighbour chip firing, S the FIRED set. Theorem 6.3 explicitly says integer H>=-2. The object is neither the set of positive final heights nor the divisible sandpile.

## Relevant results and limits of their implications

1. Anne Fey-den Boer and Frank Redig, **Limiting shapes for deterministic centrally seeded growth models**, arXiv:math/0702450v2 (4 Oct 2007). Theorem 4.1 (full theorem in downloads/fr.txt; introductory references to its number occur earlier), proves the cube for h=2d-2. The source reproduces it as Theorem 6.1. This is ONLY H=-2 in Z?; it cannot answer all H. The original paper explicitly lacks an exact scale function for this case.

2. Lionel Levine and Yuval Peres, **Strong Spherical Asymptotics for Rotor-Router Aggregation and the Divisible Sandpile**, arXiv:0704.0688, *Potential Analysis* 30 (2009), 1?27. Theorem 4.1 is the fired-set inner/outer bound on hole backgrounds, reproduced as source Theorem 6.3. For H>=-1 it bounds the radius above and below by constant multiples of sqrt(n). H approaching infinity is a separate parameter limit, not fixed-H polygonality.

3. Wesley Pegden and Charles K. Smart, **Convergence of the Abelian sandpile**, *Duke Mathematical Journal* 162 (2013), 627?642, arXiv:1105.0111v2, DOI 10.1215/00127094-2079677. Theorem 1.1, PDF p. 1: weak-* convergence of the final H=0 heights. Theorem 4.2, PDF p. 9, also gives local uniform convergence of the regularized odometer; the odometer itself converges away from 0 after adding the discrete fundamental solution. This is an analytic input, not a theorem asserting a regular dodecagon.

4. Ahmed Bou-Rabee, **Convergence of the random Abelian sandpile**, *Annals of Probability* 49 (2021), 3168?3196, DOI 10.1214/21-AOP1528, arXiv:1909.07849. Theorem 9.2, retrieved PDF p. 28:

> Theorem 9.2. Let vn be the odometer function for the sandpile with n chips at the origin on a stationary, ergodic, random background ηmin≤η≤ηmax = 2d− 2, vn∈L (η +nδ0, Zd)∩S (η +nδ0, Zd). Almost surely, as n→ ∞, the rescaled functions ¯vn := n−2/dvn([n1/dx]) converge locally uniformly away from the origin to ¯v+G, whereG is the fundamental solution of the Laplacian in Rd and ¯v∈C(Rd) is the unique viscosity solution of the obstacle problem, ¯v := inf{¯v∈C(Rd)|¯v≥−G and ¯Fη(D2(¯v +G))≤ 0}.

A deterministic constant background -H is a stationary ergodic law on one configuration and satisfies these bounds for H>=-2. Thus the existence of an odometer scaling limit is no longer open in this range. Neither the theorem nor these quoted sentences assert fired-set polygonality.

5. Lionel Levine, Wesley Pegden, Charles K. Smart, **Apollonian structure in the Abelian sandpile**, *Geometric and Functional Analysis* 26 (2016), 1?28, arXiv:1208.4839. Theorems 1.1?1.3 describe the limiting obstacle problem and construct fractal PDE solutions. Those constructions are not an identification of the point-source boundary with a polygon.

6. Lionel Levine, Wesley Pegden, Charles K. Smart, **The Apollonian structure of integer superharmonic matrices**, *Annals of Mathematics* 186 (2017), 1?67, arXiv:1309.3267v4. Theorem 1.1, PDF p. 2, classifies allowed asymptotic quadratic matrices as circle-cone downsets plus trace<=0. Rational peak matrices do NOT imply rational normals at other boundary points.

7. Lionel Levine and Yuval Peres, **Laplacian growth, sandpiles, and scaling limits**, *Bulletin of the AMS* 54 (2017), 355?382, arXiv:1611.00411. Section 6, PDF pp. 21?22, discusses the sandpile scaling PDE, not a theorem solving Question 6.2.

8. Hayk Aleksanyan and Henrik Shahgholian, **Discrete Balayage and Boundary Sandpile**, arXiv:1607.01525. The main model differs. Theorem 4.7, retrieved PDF pp. 19?20, gives directional monotonicity and locally Lipschitz boundary for the H=0 abelian odometer limit. Remark 4.8 proposes extension to backgrounds; this is not polygonality.

9. Ahmed Bou-Rabee, **Dynamic Dimensional Reduction in the Abelian Sandpile**, arXiv:2009.05968, DOI 10.1007/s00220-022-04322-z. Uniform unstable mass on a finite hypercube with dissipation at its edge; different initial condition and boundary rule.

10. Ian Alevy and Sevak Mkrtchyan, **The Limit Shape of the Leaky Abelian Sandpile Model**, arXiv:2010.01946, DOI 10.1093/imrn/rnab124. A dissipative model; its circle/diamond results do not settle a fixed conservative background. Recent hits arXiv:2509.06648 (isoradial leaky model), 2501.12664 (multiple layers), 2605.10361 (stochastic one-dimensional sandpile), 2609.21359 (comb lattice) and 2607.25878 (many-point tropical relaxation) were excluded on their stated objects/hypotheses. Their abstracts are preserved in the arXiv API XML responses.

## Searches and retrievals (all 2026-10-11)

- **source**: `https://arxiv.org/pdf/0801.3306`; HTTP 200, 763425 bytes.
- **arxiv**: `http://export.arxiv.org/api/query?search_query=all:sandpile+AND+(all:holes+OR+all:polygon+OR+all:scaling)&max_results=40`; HTTP 200, 71602 bytes.
- **openalex**: `https://api.openalex.org/works?search=sandpile%20holes%20limiting%20shape&per-page=30`; HTTP 429, 610 bytes.
- **openalex_source**: `https://api.openalex.org/works?search=Chip-firing%20and%20rotor-routing%20on%20directed%20graphs&per-page=5`; HTTP 429, 610 bytes.
- **crossref**: `https://api.crossref.org/works?query=sandpile%20holes%20limiting%20shape&rows=25`; HTTP 200, 145339 bytes.
- **semantic**: `https://api.semanticscholar.org/graph/v1/paper/search?query=sandpile%20holes%20limiting%20shape&limit=20&fields=title,authors,year,url,abstract`; HTTP 429, 174 bytes.
- **github**: `https://api.github.com/search/repositories?q=sandpile+shape&per_page=20`; HTTP 200, 55 bytes.
- **pegden_smart**: `https://arxiv.org/pdf/1105.0111`; HTTP 200, 419145 bytes.
- **apollonian**: `https://arxiv.org/pdf/1208.4839`; HTTP 200, 1959086 bytes.
- **matrices**: `https://arxiv.org/pdf/1309.3267`; HTTP 200, 1125764 bytes.
- **survey**: `https://arxiv.org/pdf/1611.00411`; HTTP 200, 2156680 bytes.
- **boundary**: `https://arxiv.org/pdf/1607.01525`; HTTP 200, 784012 bytes.
- **arxiv_target**: `https://export.arxiv.org/api/query?search_query=all:sandpile+AND+(all:background+OR+all:polygon+OR+all:shape)&max_results=80&sortBy=submittedDate&sortOrder=descending`; HTTP 200, 114417 bytes.
- **crossref_target**: `https://api.crossref.org/works?query.title=Chip-firing%20and%20rotor-routing%20on%20directed%20graphs&rows=5`; HTTP 200, 44511 bytes.
- **openalex_retry**: `https://api.openalex.org/works?search=Chip-firing%20and%20rotor-routing%20on%20directed%20graphs&per_page=5`; HTTP 429, 610 bytes.
- **semantic_source**: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:0801.3306?fields=title,citations.title,citations.year,citations.externalIds`; HTTP 200, 58970 bytes.
- **github_target**: `https://api.github.com/search/repositories?q=abelian+sandpile&per_page=30`; HTTP 200, 160029 bytes.
- **random**: `https://arxiv.org/pdf/1909.07849`; HTTP 200, 5041332 bytes.
- **reduction**: `https://arxiv.org/pdf/2009.05968`; HTTP 200, 1543264 bytes.
- **fr**: `https://arxiv.org/pdf/math/0702450`; HTTP 200, 254571 bytes.
- **lp_bounds**: `https://arxiv.org/pdf/0704.0688`; HTTP 200, 1087056 bytes.
- **openalex_citing**: `https://api.openalex.org/works?filter=cites:W2145796065&per-page=100`; HTTP 429, 610 bytes.
- **arxiv_recent**: `https://export.arxiv.org/api/query?search_query=all:sandpile+AND+(all:convergence+OR+all:holes+OR+all:polygon)&start=0&max_results=80&sortBy=submittedDate&sortOrder=descending`; HTTP 200, 125810 bytes.
- **openalex_doi**: `https://api.openalex.org/works/https://doi.org/10.1007/978-3-7643-8786-0_17`; HTTP 429, 610 bytes.
- **openalex_citing_doi**: `https://api.openalex.org/works?filter=cites:https://doi.org/10.1007/978-3-7643-8786-0_17&per-page=100`; HTTP 429, 610 bytes.

OpenAlex returned HTTP 429 on title, DOI lookup, and a citing-work filter using the verified source DOI; it says the shared free daily budget is exhausted. Consequently no OpenAlex citation results were available. The earlier OpenAlex request with W2145796065 used an unverified guessed identifier and is NOT evidence about citations of this source; it too returned 429. Semantic Scholar search was rate limited, but its ARXIV:0801.3306 lookup returned a citation list, which was screened. Crossref source-title lookup verified the exact source DOI. GitHub sandpile+shape returned zero repositories; abelian+sandpile returned repositories for simulations, not a theorem of polygonality.

## Read-only brain and prior-work checks

- math_recall queries: sandpile Pegden Smart scaling limit background holes; sandpile recurrent forbidden subconfiguration burning density; obstacle problem corner free boundary quadratic growth.
- brain.py recall queries: sandpile scaling limit; sandpile mistakes. These returned no applicable checked solution.
- Searched the permitted intake problems.jsonl, attempts.jsonl, sources.jsonl for F0131 and inspected F0131-A001. Its rational-normal premise lacked proof; it explicitly recorded an unsolved attempt.
- Inspected origin/master filenames in the read-only math-open-problems checkout for F0131/sandpile. No proved F0131 answer was identified; no working-tree changes were made.

The current counterexample argument, if verified, is our deduction using convergence and finite last-firing bounds; its verdict must therefore be SOLVED, not SOLVED_IN_LITERATURE.

Metadata query: https://api.crossref.org/works/10.1214/21-AOP1528; 2026-10-11; HTTP 200.

Metadata query: https://api.crossref.org/works?query.title=Convergence%20of%20the%20Abelian%20sandpile&rows=3; 2026-10-11; HTTP 200.

Read math-store card source_17f120df35b6274ccbe6707a7f06993c7df9ec6a2684d6a3f5f40009a23507b5 in full with --id; it records the Apollonian source and supplies no polygon theorem.
