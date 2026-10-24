# Literature and status search

Date: 2026-10-12. All web access used Python urllib; no built-in search.

## Primary source
Nicolas Curien, *Peeling random planar maps*, Saint-Flour XLIX 2019, author preliminary version, supplied URL. Downloaded as source.pdf. Corollary 27 and question are on PDF page 61, printed page 57 (the intake locator used PDF pagination).

Exact extracted source page:

```
Corollary 27 (The ﬁlled-in exploration discovers everything). Suppose that q is of type a ∈
[3/2; 5/2]. Let (en)n≥0 be a ﬁlled-in peeling exploration under P(ℓ)
∞for some algorithm A. Then
[
n≥0
en = m,
almost surely.
Proof. As in the proof of Lemma 17 one needs to prove that every “vertex” on the boundary of
en is eventually swallowed by the peeling process and becomes an interior vertex of en. We note
however that conditionally on the past exploration, if ℓis the length of the distinguished hole,
then for any given vertex v on the boundary of the distinguished hole of en and any edge to peel
on that hole there is probability of order
ℓ−1
X
k=[ℓ/2]
b(ℓ)(∗,k)
or
ℓ−1
X
k=[ℓ/2]
b(ℓ)(k, ∗),
that the peeling of the edge A(en) swallows in a ﬁnite region half of the boundary of the distin-
guished hole so that the vertex v becomes an inner vertex of en+1. Using the exact values of b(ℓ)
∞
described in Section 4.2.1 as well as the asymptotics for the tail of ν and the expression of h↑, it
follows that the last display is of order ℓ1−a. Since the half-perimeter of the only hole of en has
the same law as S↑the proof of the corollary boils down to proving that almost surely we have
∞
X
n=1
*
,
1
S↑
n
+
-
a−1
=
∞
X
n=1
1
n
*
,
n1/(a−1)
S↑
n
+
-
a−1
= ∞.
We are exactly in the conditions to apply Jeulin’s lemma [44, Proposition 4 c]. Since the proof is
very short and elementary let us recall it here. We denote by Xn =

n1/(a−1)/S↑
n
a−1 and suppose
by contradiction that the random series P 1
nXn is bounded by M ≥0 on an event A of probability
at least ε > 0. Using the convergence of Xn towards the strictly positive random variable ϒ−1
a (pq)
implied by Proposition 26 we deduce that we can ﬁnd δ > 0 such that
lim inf
n→∞P(Xn ≥δ) ≥1 −ε
2.
Then taking expectation on the event A we deduce that
E[1A
X
n≥1
1
nXn] =
X
n≥1
1
nE[1AXn] ≤M.
But using the above display we deduce that E[1AXn] ≥δ max(0,ε −P(Xn < δ)) is asymptotically
larger than δε/2. Plugging back into the last display we ﬁnd a contradiction because the series
P
n≥1
1
nεδ/2 is obviously not summable!
□
Open question. Is the last corollary true for any critical weight sequence?
57

```

The model is bipartite. Section 4.2, Theorem 8 assumes an admissible critical weight sequence and external face degree 2l, l=1. Corollary 27 allows any algorithm A; this means a continuing adapted peeling algorithm, not one that voluntarily stops. Page 60 explicitly excludes a=3/2 for S?; that is the subcritical classification endpoint, not an extra critical case.

## Search requests
- 2026-10-12; arxiv; `https://export.arxiv.org/api/query?search_query=all%3A%22peeling%22%20AND%20all%3A%22Boltzmann%22&max_results=30&sortBy=submittedDate&sortOrder=descending`; OK 31853.
- 2026-10-12; openalex; `https://api.openalex.org/works?search=filled%20peeling%20critical%20Boltzmann%20maps&per-page=30`; <HTTPError 429: 'Too Many Requests'>.
- 2026-10-12; crossref; `https://api.crossref.org/works?query=Peeling%20random%20planar%20maps%20Curien&rows=15`; OK 94600.
- 2026-10-12; semantic; `https://api.semanticscholar.org/graph/v1/paper/search?query=peeling%20Boltzmann%20maps&limit=30&fields=title,authors,year,externalIds,abstract`; <HTTPError 429: ''>.
- 2026-10-12; github; `https://api.github.com/search/repositories?q=peeling%20Boltzmann%20maps`; OK 55.
- 2026-10-12; openalex_source; `https://api.openalex.org/works/https://doi.org/10.1007/978-3-031-36854-7`; HTTP Error 429: Too Many Requests.
- 2026-10-12; openalex_retry; `https://api.openalex.org/works?search=Peeling%20Random%20Planar%20Maps&per_page=5`; HTTP Error 429: Too Many Requests.
- 2026-10-12; semantic_retry; `https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/978-3-031-36854-7?fields=title,year,citations.title,citations.year,citations.externalIds`; OK 7512.
- 2026-10-12; arxiv_exhaust; `http://export.arxiv.org/api/query?search_query=all%3A%22peeling%22%20AND%20%28all%3A%22exhaustion%22%20OR%20all%3A%22critical%20weight%22%29&max_results=30`; OK 17562.
- 2026-10-12; simple_pdf; `https://arxiv.org/pdf/1909.10217`; OK 1428946.
- 2026-10-12; markov_pdf; `https://arxiv.org/pdf/2505.05447`; OK 1364490.
- 2026-10-12; curien_page; `https://www.imo.universite-paris-saclay.fr/~nicolas.curien/`; OK 4978.

## Brain and prior records
Read the provided math-store reduction card in full and recalled topic/mistakes. Queried Budd/random-walk/harmonic/peeling cards. Read codex_pool_2026_10_10/team_O/w345/C0057_hazard_lemma.md and searched the intake JSONL records for C0057. The older equivalence is unproved; the later note correctly removes necessity for stopped target hazards. These are hints, not literature solutions. Read-only origin/master path of same hazard note was requested.

No exact later theorem answering the question has yet been verified. API failures limit negative search conclusions.

## Follow-up requests and citation checks
- 2026-10-12; budd; `https://arxiv.org/pdf/1506.01590`; OK 702597.
- 2026-10-12; conditioned; `https://arxiv.org/pdf/math/0602306`; OK 394430.
- 2026-10-12; research_page; `https://www.imo.universite-paris-saclay.fr/~nicolas.curien/recherche.html`; OK 120995.
- 2026-10-12; openalex_cites; `https://api.openalex.org/works?filter=cites:W4386255711&per-page=30`; HTTP Error 429: Too Many Requests.
- 2026-10-12; dichotomy; `https://arxiv.org/pdf/2603.13642`; OK 617198.

The attempted OpenAlex cites filter used an unverified exploratory work identifier after DOI lookup failed; it is NOT a verified citation search and produced HTTP 429. OpenAlex could not supply a source work ID or its citing works. Actual source citations were obtained from the successful Semantic Scholar DOI request; its complete returned list is semantic_retry.txt. Neither failure certifies absence of a published solution.

Relevant references and inspected scope:

- Nicolas Curien, *Peeling Random Planar Maps*, Ecole d'Ete de Probabilites de Saint-Flour XLIX - 2019, Lecture Notes in Mathematics, Springer (2023), DOI 10.1007/978-3-031-36854-7. Crossref returned the book and chapter records. The primary text verified here is the supplied author preliminary version; the final book was not fetched in full.
- Timothy Budd, *The peeling process of infinite Boltzmann planar maps*, arXiv:1506.01590v3 (2015 preprint; dated/version metadata retained in the fetched PDF). Lemma 4, equations (40)-(41), PDF p.16, and the bipartite kernel on PDF p.17, apply to all critical laws. Proposition 5, PDF p.18, concerns finite L_nu scaling. Neither states the general exhaustion conclusion. Kernel quoted and independently derived in ATTEMPT.md.
- Francesco Caravenna and Loic Chaumont, *Invariance principles for random walks conditioned to stay positive*, Annales de l'Institut Henri Poincare Probabilites et Statistiques 44(1) (2008), 170-190, DOI 10.1214/07-AIHP119, arXiv:math/0602306v2. Theorem 1.1 on PDF p.4 / printed p.173 supplies conditioned stable attraction. Used only in the auxiliary special-case proof, not in the universal proof.
- Timothy Budd and Nicolas Curien, *Simple peeling of planar maps with application to site percolation*, arXiv:1909.10217v2. Fetched and searched for exhaustion, discovery, and arbitrary critical weights. Its arbitrary-critical constructions concern maps of the half-plane with simple boundary. The text explicitly allows algorithms revealing a subregion without the root neighborhood (PDF p.19); it does not state the infinite-plane exhaustion theorem sought here.
- Pablo Araya, Luis Fredes, and Avelio Sepulveda, *Characterisation of Markov properties on planar maps*, arXiv:2505.05447v2 (2025). Fetched and inspected references to peeling and discovery; its characterization of stopping maps is not a general exhaustion theorem. See markov_pdf.pdf for author/title details.
- Adam Timar, *Parabolic-hyperbolic dichotomy through half-plane coexistence*, arXiv:2603.13642v1 (13 March 2026). Selected from the source's Semantic Scholar citations, fetched, and inspected Theorems 1 and 4. These concern invariant percolation on unimodular random maps, not filled-in peeling exhaustion.

Additional arXiv hits screened by title and abstract included *Markovian explorations of random planar maps are roundish* (1902.10624), *Infinite stable Boltzmann planar maps are subdiffusive* (1910.09623), and *On large 3/2-stable maps* (2304.01167); these concern stable/type-specific classes, not all critical sequences. Complete results and abstracts are retained in arxiv.txt and arxiv_exhaust.txt. GitHub returned zero repositories for the requested query. Curien's home and research pages were fetched as additional bibliographic leads.

Status conclusion: no exact solution-in-print theorem was verified. The affirmative answer in ATTEMPT.md is our mathematical deduction, so the final verdict is SOLVED, not SOLVED_IN_LITERATURE.

## Exact arXiv metadata for screened relevant hits
- Pablo Araya, Luis Fredes, Avelio Sepúlveda, *Characterisation of Markov property on planar maps*, http://arxiv.org/abs/2505.05447v2; first submitted 2025-05-08T17:37:43Z.
- Emmanuel Kammerer, *On large $3/2$-stable maps*, http://arxiv.org/abs/2304.01167v2; first submitted 2023-04-03T17:35:01Z.
- Nicolas Curien, Cyril Marzouk, *Infinite stable Boltzmann planar maps are subdiffusive*, http://arxiv.org/abs/1910.09623v1; first submitted 2019-10-21T19:32:27Z.
- Timothy Budd, Nicolas Curien, *Simple peeling of planar maps with application to site percolation*, http://arxiv.org/abs/1909.10217v2; first submitted 2019-09-23T08:32:18Z.
- Nicolas Curien, Cyril Marzouk, *Markovian explorations of random planar maps are roundish*, http://arxiv.org/abs/1902.10624v1; first submitted 2019-02-27T16:35:27Z.
- Timothy Budd, Nicolas Curien, *Geometry of infinite planar maps with high degrees*, http://arxiv.org/abs/1602.01328v2; first submitted 2016-02-03T15:01:42Z.
- Timothy Budd, *The peeling process of infinite Boltzmann planar maps*, http://arxiv.org/abs/1506.01590v3; first submitted 2015-06-04T13:45:12Z.
