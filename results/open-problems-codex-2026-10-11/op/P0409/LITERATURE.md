# Literature search

Date: 2026-10-12. Source: D’Achille, Curien, Enriquez, Lyons and Ünel, Ideal Poisson–Voronoi tessellations on hyperbolic spaces, arXiv:2303.16831.

- arxiv: `https://export.arxiv.org/api/query?search_query=all%3A%22ideal%22%20AND%20all%3A%22Voronoi%22&start=0&max_results=40` — OK
- openalex: `https://api.openalex.org/works?search=Ideal%20Poisson%20Voronoi%20tessellations&per-page=30` — OK
- crossref: `https://api.crossref.org/works?query=Ideal%20Poisson%20Voronoi%20tessellations&rows=20` — OK
- semantic: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:2303.16831/citations?fields=title,authors,year,externalIds&limit=100` — OK
- github: `https://api.github.com/search/repositories?q=ideal%20Voronoi` — OK

- openalex_citing_arxiv: `https://api.openalex.org/works?filter=cites:W4361807156&per-page=100` — OK

- openalex_citing_journal: `https://api.openalex.org/works?filter=cites:W7131653980&per-page=100` — OK

- arxiv_focused: `https://export.arxiv.org/api/query?search_query=all%3A%22Voronoi%22%20AND%20%28all%3A%22neighboring%22%20OR%20all%3A%22Palm%22%20OR%20all%3A%22Laguerre%22%29&max_results=50` — OK

- semantic_search: `https://api.semanticscholar.org/graph/v1/paper/search?query=ideal%20Voronoi%20neighboring%20vertices&limit=20&fields=title,authors,year,externalIds` — HTTP Error 429: 

## Verified source

Matteo D?Achille, Nicolas Curien, Nathana?l Enriquez, Russell Lyons, Meltem ?nel. *Ideal Poisson?Voronoi tessellations on hyperbolic spaces*. Annals of Probability **54**(2), 846?891 (2026). DOI: 10.1214/25-AOP1781. arXiv:2303.16831v3. Fetched https://arxiv.org/pdf/2303.16831 on 2026-10-12; 51-page PDF saved as source.pdf, extracted text source.txt. Question 7.3 is PDF p.48; Proposition 4.4 is PDF p.29. Exact quotations and model hypotheses are in ATTEMPT.md. Used Theorem 1.2 (p.4), Theorem 1.3 (p.4), equations (3.2), (3.3) (p.13), (3.7) (p.15), and Lemma 3.10 (p.20).

## Relevant later work inspected

Fetched the following PDFs from https://arxiv.org/pdf/<id> on 2026-10-12; PDFs, extracted texts and keyword contexts are saved locally as paper_<id>.* and followup_hits.json. Read abstracts, the main result statements and contexts of neighboring/typical/Palm terminology. None states a theorem giving the full Question 7.3 joint neighbor law.

- Matteo D?Achille and Christoph Th?le, *Face volume densities of positive-intensity and ideal Poisson--Voronoi tessellations in hyperbolic spaces*, arXiv:2606.26049 (2026), 17 PDF pages. Gives face-volume densities and typical-face volumes. Relevant to normalization and marginal geometry; not a full neighbor configuration law.
- Matteo D?Achille and Ali Khezeli, *Convergence towards Ideal Poisson--Voronoi tessellations with a focus on Diestel--Leader graphs*, arXiv:2606.30517 (2026), 52 PDF pages. Convergence and general-space IPVTs. Its own Question 7.3 concerns an L1 product metric, not this source?s Question 7.3.
- Anna Gusakova and Mathias in Wolde-L?bke, *Limits of Poisson-Laguerre tessellations*, arXiv:2602.06906 (2026), 47 PDF pages. Related limiting tessellation framework; no typical-neighbor law for the present hyperbolic IPVT was identified.
- Florian Besau, Anna Gusakova and Christoph Th?le, *Random hyperbolic polyhedra in horoballs*, arXiv:2609.10007 (2026), 38 PDF pages. Related random polyhedra and Delaunay-type limits. Corollary 13 concerns convergence of a typical simplex, not joint IPVT neighbors.
- Sam Mellick, *Indistinguishability of cells for the ideal Poisson Voronoi tessellation*, arXiv:2408.10009, 7 PDF pages; DOI 10.1090/proc/17493. Resolves cell indistinguishability, a different question.
- Matteo D?Achille, *Ideal Poisson?Voronoi tessellations beyond hyperbolic spaces*, arXiv:2412.00822; DOI 10.1214/26-ECP815. Metadata/abstract lead from arXiv/OpenAlex/Crossref; general spaces, not an identified neighbor theorem.

Other citing leads in the Semantic Scholar response: *Non-vanishing uniqueness threshold for hyperbolic Poisson-Voronoi percolation in dimension at least three*, *Seeing Through Hyperbolic Space: Visibility for lambda-Geodesic Hyperplanes*, *Wicksell?s corpuscle problem in spaces of constant curvature*, and fixed-price/group papers. These were metadata leads, not claimed solutions; exact author/external-ID metadata is retained in search_semantic.txt.

OpenAlex citing-source queries were run separately for arXiv record W4361807156 and journal record W7131653980. They returned only an intersections-of-Poisson-k-flats paper and the beyond-hyperbolic-spaces paper, respectively; Semantic Scholar returned more citing leads, illustrating index incompleteness. GitHub returned three unrelated repository leads; no matching proof repository found. The focused Semantic Scholar search returned HTTP 429; its citation endpoint succeeded.

Search outcomes are bounded negative evidence, not a certificate of worldwide openness or novelty. No source-matching theorem has been identified; SOLVED_IN_LITERATURE is not used.

## Read-only brain and prior-work checks

Ran math_recall.py with ?ideal Voronoi vertex Palm?; brain.py recall with ?hyperbolic Voronoi? and ?hyperbolic Voronoi mistakes?. The useful earlier card asserts uniform-neighbor rerooting preserves the Gamma(d+1) separation marginal; it was used as a test, not as proof of the candidate law. Searched intake JSONL directories and the codex_pool_2026_10_10 directory for P0409 (the first wildcard-path rg call failed under Windows; corrected by enumerating matching directories). Read origin/master:proofnet24/NM13-09/runs/2026-09-19/2026-09-19T22-47-30Z__post-p0245-admission-delta-screen-40-hard-releases-no-r8-ready-p0409-still-hard.md using git show. It preserves the prior Gamma marginal argument and identifies the full joint law as still missing. No brain or repository writes were performed.

Additional focused arXiv search lead: *Mixing Properties of Random Laguerre Tessellations*, arXiv:2608.13235; title-level lead concerning mixing, no source-matching neighbor theorem identified. Crossref confirmed the source journal volume 54, issue 2, pages 846?891, published March 2026.
