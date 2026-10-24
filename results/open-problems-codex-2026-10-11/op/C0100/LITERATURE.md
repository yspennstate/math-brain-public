# Literature and status search (2026-10-12)

No full solution identified at this stage. Rate-limited searches do not certify absence.

## All HTTP searches and fetches
- 2026-10-12: source; https://arxiv.org/pdf/1611.00411; HTTP 200; saved raw response.
- 2026-10-12: arxiv; https://export.arxiv.org/api/query?search_query=all:sandpile+AND+(all:scaling+OR+all:identity)&start=0&max_results=60&sortBy=submittedDate&sortOrder=descending; HTTP 200; saved raw response.
- 2026-10-12: openalex; https://api.openalex.org/works?search=sandpile%20scaling%20limit&per-page=50; HTTP 429; saved raw response.
- 2026-10-12: crossref; https://api.crossref.org/works?query=sandpile%20scaling%20limit&rows=40; HTTP 200; saved raw response.
- 2026-10-12: semantic; https://api.semanticscholar.org/graph/v1/paper/search?query=sandpile%20scaling%20limit&limit=40&fields=title,year,authors,url,abstract; HTTP 429; saved raw response.
- 2026-10-12: github; https://api.github.com/search/repositories?q=sandpile+scaling+limit&per_page=30; HTTP 200; saved raw response.
- 2026-10-12: arxiv_target; https://export.arxiv.org/api/query?search_query=all:sandpile+AND+(au:Pegden+OR+au:Smart+OR+all:pattern+OR+all:identity)&start=0&max_results=100&sortBy=relevance; HTTP 200; saved raw response.
- 2026-10-12: ellipse; https://arxiv.org/pdf/2007.05792; HTTP 200; saved raw response.
- 2026-10-12: apollonian; https://arxiv.org/pdf/1208.4839; HTTP 200; saved raw response.
- 2026-10-12: openalex_source; https://api.openalex.org/works?search=Laplacian%20growth%20sandpiles%20and%20scaling%20limits&per_page=3; HTTP 429; saved raw response.
- 2026-10-12: semantic_source; https://api.semanticscholar.org/graph/v1/paper/ARXIV:1611.00411?fields=title,citations.title,citations.year,citations.externalIds; HTTP 429; saved raw response.
- 2026-10-12: crossref_target; https://api.crossref.org/works?query.bibliographic=sandpile%20identity%20Pegden%20Smart&rows=30; HTTP 200; saved raw response.
- 2026-10-12: stability; https://arxiv.org/pdf/1708.09432; HTTP 200; saved raw response.
- 2026-10-12: openalex_doi; https://api.openalex.org/works/https://doi.org/10.1090/bull/1563; HTTP 429; saved raw response.
- 2026-10-12: openalex_citing; https://api.openalex.org/works?filter=cites:W2535495547&per_page=100; HTTP 429; saved raw response.
- 2026-10-12: semantic_bulk; https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=%22sandpile%22%20%2B%22identity%22&fields=title,year,externalIds; HTTP 429; saved raw response.
- 2026-10-12: arxiv_fractions; https://export.arxiv.org/api/query?search_query=all:sandpile+AND+(all:frequency+OR+all:frequencies+OR+all:Pegden)&max_results=70&sortBy=submittedDate&sortOrder=descending; HTTP 200; saved raw response.

The OpenAlex candidate identifier W2535495547 and DOI 10.1090/bull/1563 were exploratory, not verified identifiers for the source; their requests returned 429. Do not count that as a successful citation search.

## Exact source statement
Levine and Peres, Laplacian growth, sandpiles and scaling limits, arXiv:1611.00411, section 9(3), printed/PDF p. 27:

> Recall that the weak-∗ convergence in Theorem 6.1, proved by Pegden and Smart [60], means that the average height of the sandpile s_n in any ball converges as the lattice spacing shrinks to zero. A natural refinement would be to show that for any ball B and any integer j, the fraction of sites in B with j particles converges. Understanding the scaling limit of the sandpile identity elements (Figure 8) is another appealing problem, solved in a special case by Caracciolo, Paoletti and Sportiello [13].

Theorem 6.1 and its preceding paragraph, p. 21: stabilize n particles at the origin in Z^d; s_n=n delta_0+Delta u_n; rescale space by n^(1/d). Thus lattice spacing is n^(-1/d), not 1/n in dimension 2. Stable heights are 0,...,2d-1. The surrounding text focuses on the square lattice. Figure 8, p. 23: Rec([0,n]^2,z), wired boundary. This is a separate family from the point-source pile.

## Relevant references inspected
- W. Pegden and C. K. Smart, Convergence of the Abelian sandpile, Duke Mathematical Journal 162(4) (2013), 627–642; arXiv:1105.0111. Weak-* convergence; not yet a frequency theorem.
- L. Levine, W. Pegden and C. K. Smart, Apollonian structure in the Abelian sandpile, arXiv:1208.4839v2 (22 May 2014); source reference [46]. Theorem 1.3 constructs special PDE solutions, Corollary 1.4 is conditional on three preexisting quadratic regions. Page 6 says the global geometry remains a considerable challenge. It does NOT unconditionally prove an a.e. periodic-patch cover for the point-source pile.
- Andrew Melchionna, The sandpile identity element on an ellipse, arXiv:2007.05792v2 (1 July 2023). Certain ellipses E_{A,k} with A in Gamma^+; local translated-pattern agreement at most sites. A special case, not wired squares.
- W. Pegden and C. K. Smart, Stability of patterns in the Abelian sandpile, arXiv:1708.09432v2. Retrieved; theorem comparison ongoing.
- S. Caracciolo, G. Paoletti and A. Sportiello, Explicit characterization of the identity configuration in an abelian sandpile model, Journal of Physics A: Mathematical and Theoretical 41 (2008), 495003; arXiv:0809.3416. The source explicitly labels this a special case.
- arXiv:2308.12183 and arXiv:2603.12006 concern Sierpinski gasket identities, a different graph.
- arXiv:2607.26169, Scaling and partial universality of the height zero probability in the 2D Abelian sandpile, concerns the stationary random sandpile; not deterministic stabilization of n delta_0.

## Brain and earlier attempts
Read-only math_recall on sandpile/Pegden/Smart/height frequencies; brain recall on sandpile mistakes and sandpile height fraction convergence. Memory matches mostly unrelated. Intake C0100-A001 and codex_pool team_O/w333 supplied conditional patch reduction and generic weak-* counterexample. The claim that the actual point-source limit is already proved a.e. piecewise quadratic is not supported by the inspected Apollonian theorem. Git origin/master paths are being checked read-only.

## Subsequent searches (same date)
- 2026-10-12: crossref_source; https://api.crossref.org/works?query.title=Laplacian%20growth%20sandpiles%20and%20scaling%20limits&rows=3; HTTP 200; raw response saved .
- 2026-10-12: arxiv_identity_recent; https://export.arxiv.org/api/query?search_query=all:sandpile+AND+(all:identity+OR+all:pattern)+AND+submittedDate:[20170101+TO+20261012]&max_results=100&sortBy=submittedDate&sortOrder=descending; HTTP 200; raw response saved .
- 2026-10-12: arxiv_convergence; https://arxiv.org/pdf/1105.0111; HTTP 200; raw response saved .
- 2026-10-12: openalex_correct_source; https://api.openalex.org/works/https://doi.org/10.1090/bull/1573; HTTP 429; raw response saved .
- 2026-10-12: github_identity; https://api.github.com/search/repositories?q=sandpile+identity&per_page=30; HTTP 200; raw response saved .
- 2026-10-12: semantic_citations; https://api.semanticscholar.org/graph/v1/paper/ARXIV:1611.00411/citations?fields=title,year,externalIds&limit=100; HTTP 200; raw response saved .

## Bibliographic clarification and exact theorem comparison

The source DOI verified from Crossref is **10.1090/bull/1573**, not the exploratory 1563. A source-resolution request to OpenAlex using the correct DOI also returned 429. Its response explicitly says the free daily budget shared by the network IP is used up. Thus a reliable OpenAlex citing-work list was not obtained. The guessed OpenAlex ID above must not be used as a verified source identifier. Semantic Scholar's direct ARXIV:1611.00411/citations endpoint subsequently succeeded with HTTP 200 (32 records, no next-page field), although the earlier search and source requests returned 429. The citing records were screened by title and selected leads were fetched from arXiv.

- Wesley Pegden and Charles K. Smart, Stability of Patterns in the Abelian Sandpile, Annales Henri Poincare 21(4) (2020), 1383–1399, DOI 10.1007/s00023-020-00898-1; arXiv:1708.09432v2 (26 Jan 2020).
- Lionel Levine, Wesley Pegden and Charles K. Smart, Apollonian structure in the Abelian sandpile, Geometric and Functional Analysis 26(1) (2016), 306–336, DOI 10.1007/s00039-016-0358-7; arXiv:1208.4839v2.
- Andrew Melchionna, The sandpile identity element on an ellipse, Discrete and Continuous Dynamical Systems 42(8) (2022), first page 3709 (Crossref supplies no last page), DOI 10.3934/dcds.2022029; arXiv:2007.05792v2 (1 July 2023).
- Lionel Levine, Wesley Pegden and Charles K. Smart, The Apollonian structure of integer superharmonic matrices, Annals of Mathematics 186(1) (2017), 1–67, DOI 10.4007/annals.2017.186.1.1; arXiv:1309.3267. Used as the structure-theory reference recalled and cited by the pattern-stability paper; not a theorem of all height-fraction limits.

The following sentences in the pattern-stability paper are decisive for avoiding a false literature resolution (PDF/printed p. 6, section 2.5):

> Note that for the standard ≤3 cutoff, our solutions u_n correspond via Δu_n + 1 to the unique recurrent configuration equivalent to the all-ones configuration on Z² ∩ nΩ, whereas the identity element is the unique recurrent configuration equivalent to the all-zeros configuration.

(The equation notation is transcribed into Unicode; the prose is unchanged.) Thus Theorem 1's square model is not the requested square identity, and is not the point-source stabilization. The introduction, p. 2, says Sportiello's ansatz can be adapted to the cutoff-3 square and “yields the continuum limit of the sandpile identity on the square”; this sentence is a lead, not a stated and proved identity theorem here. Section 2.5 expressly distinguishes that ansatz from the rigorously treated model.

Pattern-stability Theorem 10, PDF/printed p. 7, is the precise external estimate used in ATTEMPT.md:

> There is a universal constant C_10 > 0 such that if h ≥ C_10, r ≥ C_10|V|, hr ≥ C_10|V|³, R ≥ C_10hr, and v : Z² → Z is recurrent and satisfies |v − o| ≤ h² in B_R, then, for a (1 − C_10 R⁻¹rh)-fraction of points x in B_{R−r}, there is a translation õ_x of o such that v = õ_x in B_r(x).

Mathematical notation is faithfully transcribed. The local version used in our reductions is an implication argued from its proof and local Lemma 14; hence even if that reduction closed the problem, it would be our argument rather than SOLVED_IN_LITERATURE under the requested standard.

Ellipse Theorem 4.3, PDF/printed p. 13, has r(k)=o(k^(1/4)) and r(k)≥3|V|³ and proves limsup f(k,A) k^(1/4)/r(k)≤C g(A). Its section 4 (p. 12) fixes A in Gamma^+ with positive determinant and in the fundamental domain of the Apollonian packing corresponding to (x,y) in [0,2]², with 0<lambda_1≤1<lambda_2. Thus it is not a result for arbitrary ellipses. ATTEMPT.md section 9 derives the ball-frequency special case explicitly and keeps these assumptions.

The Apollonian paper's Corollary 1.4 (p. 6) assumes three connected open regions on which the limiting odometer is already quadratic with pairwise tangent Hessians; it fills the intervening region by an Apollonian triangulation. The subsequent paragraph says the near-ubiquity of those regions is inferred from numerical evidence and that going beyond dependence on local boundary knowledge requires global geometry, a considerable challenge. Therefore the old intake's unconditional patch-cover statement is not established by that reference.

## Other relevant abstract-screened papers
- Miles W. Elvidge, Antal A. Járai, Scaling and partial universality of the height zero probability in the 2D Abelian sandpile, http://arxiv.org/abs/2607.26169v1, first submission 2026-07-28. Abstract/title screened; no theorem of the exact C0100 objects identified.
- Robin Kaiser, Ecaterina Sava-Huss, Julia Überbacher, On the structure of the sandpile identity element on Sierpinski gasket graphs, http://arxiv.org/abs/2603.12006v2, first submission 2026-03-12. Abstract/title screened; no theorem of the exact C0100 objects identified.
- Robin Kaiser, Ecaterina Sava-Huss, Scaling limit of the sandpile identity element on the Sierpinski gasket, http://arxiv.org/abs/2308.12183v2, first submission 2023-08-23. Abstract/title screened; no theorem of the exact C0100 objects identified.
- Moritz Lang, Mikhail Shkolnikov, Harmonic dynamics of the Abelian sandpile, http://arxiv.org/abs/1806.10823v1, first submission 2018-06-28. Abstract/title screened; no theorem of the exact C0100 objects identified.
- Sergio Caracciolo, Guglielmo Paoletti, Andrea Sportiello, Explicit characterization of the identity configuration in an Abelian Sandpile Model, http://arxiv.org/abs/0809.3416v2, first submission 2008-09-19. Abstract/title screened; no theorem of the exact C0100 objects identified.
- Nikita Kalinin, Mikhail Shkolnikov, Sandpile solitons via smoothing of superharmonic functions, http://arxiv.org/abs/1711.04285v1, first submission 2017-11-12. Abstract/title screened; no theorem of the exact C0100 objects identified.
- Nikita Kalinin, Mikhail Shkolnikov, Tropical curves in sandpile models, http://arxiv.org/abs/1502.06284v10, first submission 2015-02-22. Abstract/title screened; no theorem of the exact C0100 objects identified.

## Read-only earlier-work searches

- math_recall.py "sandpile Pegden Smart height frequencies periodic patches" (2026-10-12).
- brain.py recall "sandpile mistakes" and "sandpile height fraction convergence" (2026-10-12); the first mostly returned unrelated records, explicitly not treated as mathematical evidence.
- rg for C0100 in probability_1000_intake_* directories, after resolving the PowerShell directory glob; also in codex_pool_2026_10_10. Relevant files: claude_20260907/problems.jsonl and attempts.jsonl; team_O/w333/proofs/C0100.md and final_results.jsonl. F0132 is the neighboring square-identity conjecture; its literature status was unverified.
- git ls-tree origin/master filtered for C0100, then git show origin/master:probability_campaigns/codex_pool_2026-10-10/team_O/w333/proofs/C0100.md and its evidence/C0100_intake.json. The only recorded answers found were the prior conditional patch theorem and generic weak-* counterexample. No repository working tree was modified.

Conclusion: no paper was found that states and proves the full point-source ball-frequency refinement together with the wired-square identity question. This is a bounded unsuccessful search, with OpenAlex quota limitations and the earlier Semantic Scholar search failures, not a claim that the problem must still be open throughout the entire literature. Verdict remains PARTIAL.

## Semantic Scholar citation retrieval and GitHub screening

The final Semantic Scholar direct citation request succeeded; semantic_citations.json is retained. Titles of all 32 returned records (not a guarantee of exhaustive citation coverage):
- 2026: Kozma's centrally excited walk converges to a Euclidean ball; external IDs {"ArXiv": "2610.10162", "CorpusId": 292700558}.
- 2026: Limit shape, avalanches, and stabilisation of abelian sandpiles on comb lattices; external IDs {"ArXiv": "2609.21359", "CorpusId": 292193950}.
- 2026: Eulerian walkers on $\mathbb{Z}^2$ have range exponent $2/3$; external IDs {"ArXiv": "2608.23545", "CorpusId": 291328792}.
- 2026: Over-squashing as Transport Congestion: A Sandpile Dynamics Perspective; external IDs {"DOI": "10.1145/3770855.3817690", "CorpusId": 290858157}.
- 2026: Gaussian fluctuations for Internal DLA on cylinders; external IDs {"ArXiv": "2604.21142", "CorpusId": 287702070}.
- 2026: Divisible sandpiles via random walks in random scenery; external IDs {"ArXiv": "2604.13968", "CorpusId": 287480574}.
- 2025: On structural connections between sandpile monoids and weighted Leavitt path algebras; external IDs {"DOI": "10.1016/j.jalgebra.2025.04.034", "CorpusId": 278387703}.
- 2023: Unital algebras being Morita equivalent to weighted Leavitt path algebras; external IDs {"ArXiv": "2312.15704", "DOI": "10.1007/s10801-025-01454-y", "CorpusId": 266551876}.
- 2023: A flow‐type scaling limit for random growth with memory; external IDs {"ArXiv": "2310.17572", "DOI": "10.1002/cpa.22241", "CorpusId": 264490775}.
- 2022: Harmonic balls in Liouville quantum gravity; external IDs {"ArXiv": "2208.11795", "DOI": "10.1112/plms.70018", "CorpusId": 251800255}.
- 2021: Existence of a phase transition in harmonic activation and transport; external IDs {"ArXiv": "2110.13893", "DOI": "10.1214/23-ejp1004", "CorpusId": 239885541}.
- 2021: A shape theorem for exploding sandpiles; external IDs {"ArXiv": "2102.04422", "DOI": "10.1214/23-AAP1976", "CorpusId": 231847113}.
- 2020: The Limit Shape of the Leaky Abelian Sandpile Model; external IDs {"MAG": "3168192402", "ArXiv": "2010.01946", "DOI": "10.1093/IMRN/RNAB124", "CorpusId": 222133085}.
- 2020: Dynamic Dimensional Reduction in the Abelian Sandpile; external IDs {"ArXiv": "2009.05968", "MAG": "3084946543", "DOI": "10.1007/s00220-022-04322-z", "CorpusId": 221655055}.
- 2020: Sandpile Toppling on Penrose Tilings: Identity and Isotropic Dynamics; external IDs {"DBLP": "conf/birthday/FersulaNP22", "MAG": "3034791786", "ArXiv": "2006.06254", "DOI": "10.1007/978-3-030-92551-2_10", "CorpusId": 219573440}.
- 2020: Characterizing immutable sandpiles: A first look; external IDs {"DBLP": "journals/dm/DuncanE22", "MAG": "3031548763", "ArXiv": "2006.00041", "DOI": "10.1016/j.disc.2021.112657", "CorpusId": 219177018}.
- 2019: Asymptotic Height Distribution in High-Dimensional Sandpiles; external IDs {"DOI": "10.1007/s10959-019-00962-5", "CorpusId": 254747362}.
- 2019: Asymptotic Height Distribution in High-Dimensional Sandpiles; external IDs {"MAG": "2988752889", "ArXiv": "1911.01762", "DOI": "10.1007/s10959-019-00962-5", "CorpusId": 207870067}.
- 2019: How Hard is it to Predict Sandpiles on Lattices? A Survey; external IDs {"DBLP": "journals/corr/abs-1909-12150", "ArXiv": "1909.12150", "MAG": "2991512099", "DOI": "10.3233/FI-2020-1879", "CorpusId": 202889165}.
- 2019: Non-Archimedean Coulomb gases; external IDs {"MAG": "2964789256", "ArXiv": "1908.00571", "DOI": "10.1063/1.5127191", "CorpusId": 199405299}.
- 2019: Odometers of Divisible Sandpile Models: Scaling Limits, iDLA and Obstacle Problems. A Survey; external IDs {"MAG": "2921498481", "ArXiv": "1903.06263", "CorpusId": 119142817}.
- 2018: Averaging Principle and Shape Theorem for a Growth Model with Memory; external IDs {"ArXiv": "1812.00726", "MAG": "2902214024", "DOI": "10.1002/cpa.21965", "CorpusId": 119720190}.
- 2018: The Dispersion Time of Random Walks on Finite Graphs; external IDs {"DBLP": "journals/corr/abs-1808-09219", "MAG": "2949654691", "ArXiv": "1808.09219", "DOI": "10.1145/3323165.3323204", "CorpusId": 52111558}.
- 2018: Constructing fractional Gaussian fields from long-range divisible sandpiles on the torus; external IDs {"MAG": "3173680814", "ArXiv": "1808.06078", "DOI": "10.1016/J.SPA.2021.06.006", "CorpusId": 235446711}.
- 2018: Perturbed Divisible Sandpiles and Quadrature Surfaces; external IDs {"DOI": "10.1007/s11118-018-9722-6", "CorpusId": 254935036}.
- 2018: Laplacian growth and sandpiles on the Sierpiński gasket: limit shape universality and exact solutions; external IDs {"MAG": "3107993293", "ArXiv": "1807.08748", "DOI": "10.4171/aihpd/95", "CorpusId": 51752597}.
- 2017: DIVISIBLE SANDPILE ON SIERPINSKI GASKET GRAPHS; external IDs {"MAG": "2949835788", "ArXiv": "1702.08370", "DOI": "10.1142/S0218348X19500324", "CorpusId": 119713998}.
- 2016: Perfect boundaries in rotor-router aggregation on cylinders; external IDs {"MAG": "2562893794", "ArXiv": "1612.03701", "DOI": "10.1088/1751-8121/aa7316", "CorpusId": 119604556}.
- 2015: Tropical curves in sandpile models; external IDs {"ArXiv": "1502.06284", "MAG": "2256260167", "DOI": "10.1016/j.aim.2026.111127", "CorpusId": 119141202}.
- 2014: Sandpile models; external IDs {"MAG": "2891940028", "ArXiv": "1401.0354", "DOI": "10.1214/14-ps228", "CorpusId": 52952787}.
- 2022: Leaky Abelian Sandpile Model With Multiple Starting Points; external IDs {"CorpusId": 251537762}.
- 2021: My title; external IDs {"CorpusId": 235488559}.

Potential leads requiring abstract comparison: arXiv:1911.01762 (high-dimensional height distribution), arXiv:2009.05968 (dynamic dimensional reduction), and arXiv:2609.21359 (comb lattices). Other citation titles concern distinct graphs, random growth, divisible/leaky sandpiles, or algebraic models.

The identity GitHub query returned these repositories; these are code/experimental leads, not paper proofs:
- souldeux/sandpile-identity: https://github.com/souldeux/sandpile-identity; Explorer for the Abelian sandpile identity: live page, C tool, data, and notes.
- u1630022/sandpile-identity: https://github.com/u1630022/sandpile-identity; Code for calculating large sandpile identities using multigrid methods.
- teddyscotcher/sandpiles: https://github.com/teddyscotcher/sandpiles; Python code to find the identities of MxN Sandpile groups.
- ZacZipfian/BTW-sandpile-model: https://github.com/ZacZipfian/BTW-sandpile-model; An implementation of the BTW sandpile model into Python. With some exploration of the identity element..
- selimaklibi/abelian-sandpile: https://github.com/selimaklibi/abelian-sandpile; Abelian sandpile on Z^2: proofs of the abelian property verified by a vectorised simulator, exact Green-function identities, Dhar theorem, self-organised criticality and power-law MLE..
- fushanbobfan/topple: https://github.com/fushanbobfan/topple; An Abelian sandpile in the browser: pour towers, rain grains and watch avalanches, and find the sandpile group identity..
- embeddedtower/SandPiles: https://github.com/embeddedtower/SandPiles; Haskell functions to produce images of two types of fractal: (1) identities of the abelian sandpile group and (2) sandpiles produced by collapsing large number of grains from a single cell.

## Final citation-lead checks (2026-10-12)
- 2026-10-12: arxiv_citation_leads; https://export.arxiv.org/api/query?id_list=1911.01762,2009.05968,2609.21359&max_results=3; HTTP 200; response saved.
- 2026-10-12: dimensional; https://arxiv.org/pdf/2009.05968; HTTP 200; response saved.
- 2026-10-12: height_distribution; https://arxiv.org/pdf/1911.01762; HTTP 200; response saved.

- Ahmed Bou-Rabee, Dynamic dimensional reduction in the Abelian sandpile, arXiv:2009.05968v2 (29 Dec 2021), DOI 10.1007/s00220-022-04322-z (from the citation metadata). PDF introduction and Theorem 1.1 inspected: initial configuration is constant 2d throughout a finite hypercube, not n delta_0 and not the standard identity. Dimensional reduction across d and finite-time self-similarity do not prove the requested frequencies.
- Antal A. Jarai and Minwei Sun, Asymptotic height distribution in high-dimensional sandpiles, arXiv:1911.01762v1 (5 Nov 2019), DOI 10.1007/s10959-019-00962-5. PDF p. 1 defines P as the infinite-volume stationary measure and p_d(i)=P[eta(0)=i], and Theorem 1.1 concerns d tending to infinity. It is a different quantifier and different random object, not deterministic height fractions as lattice spacing tends to zero.
- arXiv:2609.21359, Limit shape, avalanches, and stabilisation of abelian sandpiles on comb lattices: retrieved abstract says the lattice is the comb and the results concern stationary avalanches and a single-source limit shape on that graph. Different graph and different statistics.

These final citation leads do not change the partial verdict. No exact solved-in-literature theorem is asserted.

Verified source journal metadata: {"title": ["Laplacian growth, sandpiles, and scaling limits"], "author": [{"given": "Lionel", "family": "Levine", "sequence": "first", "affiliation": [], "role": [{"vocabulary": "crossref", "role": "author"}]}, {"given": "Yuval", "family": "Peres", "sequence": "additional", "affiliation": [], "role": [{"vocabulary": "crossref", "role": "author"}]}], "container-title": ["Bulletin of the American Mathematical Society"], "volume": "54", "issue": "3", "page": "355-382", "published": {"date-parts": [[2017, 4, 13]]}, "DOI": "10.1090/bull/1573"}.


## Second-attempt gap queries and dependencies (2026-10-12)

Read-only brain queries: math_recall.py "sandpile isolated maximal Hessian Gamma positive density Pegden Smart pattern stability" and "sandpile identity least integer Dirichlet recurrent representative Melchionna Pegden Smart". They returned older conditional patch records and LPS source cards, not the needed a.e. isolated-maximal-Hessian theorem or an exact identity theorem.

The new weak-identity proof uses existing cached primary sources, read again at the precise hypotheses:

- Pegden–Smart, Convergence of the Abelian sandpile, arXiv:1105.0111v2: Proposition 2.3 (p. 6, local discrete Poisson compactness), Proposition 2.4 (p. 6, a.e. second differentiability of bounded-Poisson solutions), Proposition 2.5 (p. 6, positive-measure strictly concave contact points on a ball), Lemma 4.1 (pp. 8–9, integer-superharmonic quadratic lifting for ANY upper bound K), and Theorem 4.2 proof (pp. 9–11, cross-scale leastness contradiction). The new proof adapts these ingredients rather than calling a different theorem a printed solution.
- Melchionna, The sandpile identity element on an ellipse, arXiv:2007.05792v2: section 3, Proposition 8 (pp. 10–11), gives the least integer cutoff-3 boundary-value representation and checks the zero recurrent class. The second attempt supplies its finite-domain proof for arbitrary wired lattice domains rather than relying on elliptical pattern hypotheses.

Targeted searches on the new Dirichlet lead (raw responses retained):
- 2026-10-12: arxiv_identity_dirichlet; https://export.arxiv.org/api/query?search_query=all:sandpile+AND+(all:identity+AND+all:Dirichlet)&max_results=30; HTTP 200.
- 2026-10-12: crossref_identity_dirichlet; https://api.crossref.org/works?query.bibliographic=sandpile%20identity%20Dirichlet%20scaling%20limit&rows=15; HTTP 200.

The arXiv metadata query returned no entries; this narrow search does not search every theorem in paper bodies. Crossref returned unrelated/divisible/leaky sandpile and Dirichlet-series items. No precise published theorem of the full question was identified. The new weak identity conclusion may be a known implicit consequence of general convergence machinery; novelty remains unverified, and neither SOLVED_IN_LITERATURE nor complete C0100 resolution is claimed.
