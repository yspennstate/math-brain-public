# Literature search log — 2026-10-12

## Conclusion and limitations

No full solution of Question 5.2 was found in the successful bounded searches. This does not establish nonexistence or novelty. OpenAlex and Semantic Scholar returned HTTP 429 repeatedly, so their source/citation searches remain incomplete. VERDICT: PARTIAL, not SOLVED_IN_LITERATURE. Every URL and outcome is recorded below; raw responses are retained locally. All requests used shell Python, without built-in web search.

## Verified source

Micha Christoph, Patryk Morawski, Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1, submitted 2026-08-19. https://arxiv.org/pdf/2608.19145. The downloaded source_pdf.pdf has 439071 bytes and 22 pages; its text is source.txt. The arXiv API still identifies v1.

Question 5.2 is on PDF/printed page **20**, not page 19 as the intake says. Its exact words, with only mathematical typography normalized, are:

> For a graph with given ∆(G) and λ(G), what is the tight upper bound for the typical size of the largest component of Gp, when p ⩽ (1 − ε)/λ(G)?

The next sentence is:

> An interesting special case of Question 5.2 would be to consider graphs G which are “close to regular”, in the sense that ∆(G) ⩽ (1 + δ)λ(G), for some small δ, possibly being a function of |G|.

Theorem 1.4, pages 4–5, quantifies: for every ε>0 there exist γ,L,c>0; let K>0 and a finite graph G satisfy λ(G)≥K sqrt(∆(G)). Part II says that if p≤(1−ε)/λ(G), then as |G|→∞ the probability of a component of order at least L sqrt(|G|) log|G|/K is o(1). Taking K=λ(G)/sqrt(∆(G)) gives the task's displayed bound. The source uses unnormalized adjacency spectral radius and finite undirected unweighted graphs. Question 5.2 does not impose connectedness. Connectedness enters only its discussion of regularity when λ=∆.

The complete-bipartite example and the constant-radius tree discussion on pages 19–20 are already source results. No novelty is claimed for them.

## Search interpretation

The broad later-arXiv query returned 100 entries and was not exhaustive by itself. The second targeted date-restricted query returned 12 entries, including the source; all their titles and abstracts were screened. No abstract states the full target. The OpenAlex citation fallback used a DOI in its cites field because the work ID could not be resolved; it returned 429 before validation. This is **not** a completed citing-works query, and no assertion of zero citations is made.

The Crossref exact-title query recovered older work. Its date-restricted query returned 30 mostly spectral-extremal metadata records, none asserting the target. GitHub broad search returned four unrelated/specialized repositories; the exact arXiv-identifier search returned zero repositories. Repository absence is not literature evidence.

## Relevant references and leads

- Michael Krivelevich, *Percolation on Finite Graphs*, arXiv:2609.28552v1, submitted 2026-09-23. Downloaded course_pdf.pdf; extracted course.txt. These graduate lecture notes cover random graphs, general random subgraphs, hypercubes, long paths and cycles. The text contains no occurrence of “Christoph”, “2608.19145”, or “spectral radius”. Theorem 3.1.2 is the ordinary logarithmic subcritical G(n,c/n) bound. It does not state Question 5.2's solution.
- Ery Arias-Castro, *Finite Size Percolation in Regular Trees*, arXiv:1007.4508v1, 2010-07-26. Downloaded regular_trees_pdf.pdf; extracted regular_trees.txt. Page 1 defines site percolation on an **infinite** r-ary tree and allows clusters to extend beyond generation d, restricting only their highest vertex to the first d generations. Theorem 1, page 2, gives log_r(K_d)/d→2 at criticality. That is a different truncation and model from the finite-host T_{b,h} studied here. It is an extreme-value-method lead, not a solution of Question 5.2 or a direct theorem about the present finite-host cubic bound.
- Marcus Michelen, *Critical Percolation and the Incipient Infinite Cluster on Galton-Watson Trees*, arXiv:1806.00888v2. Abstract screened: quenched survival and Yaglom laws for critical root clusters on random trees, rather than largest components over all finite hosts.
- Eleanor Archer, Quirin Vogel, *Quenched critical percolation on Galton-Watson trees*, arXiv:2312.06485v1. Abstract screened: root survival, Yaglom limits and population scaling; a lead for branching methods only.
- Eleanor Archer, Tanguy Lions, *Quenched scaling limit of critical percolation clusters on Galton-Watson trees*, arXiv:2501.12088v2. Abstract screened: quenched scaling and cluster-size tails on random trees; does not state the full question.
- Tomoaki Nogawa, Takehisa Hasegawa, Koji Nemoto, *Local cluster-size statistics in the critical phase of bond percolation on the Cayley tree*, arXiv:1602.00803v2. Abstract screened: local distributions and boundary effects, not an all-host upper bound.
- Gabriel Berzunza, Cecilia Holmgren, *The asymptotic distribution of cluster sizes for supercritical percolation on random split trees*, arXiv:2003.12018v2. Abstract screened: supercritical split trees, a different host/parameter regime.
- S. Diskin, J. Erde, M. Kang, M. Krivelevich, *Percolation on high-dimensional product graphs*, Random Structures & Algorithms 66 (2025), e21268, 10 pp. Source reference [14], cited by the source for ordinary branching-process subcritical bounds; not independently treated as a full solution.
- A. Nachmias, Y. Peres, *Critical percolation on random regular graphs*, Random Structures & Algorithms 36 (2010), 111–148. Source reference [32], likewise special to regular graphs and cited for standard branching bounds.
- *A Note About Critical Percolation on Finite Graphs*, DOI 10.1007/s10959-010-0283-x (2010), and *The incipient giant component in bond percolation on general finite weighted graphs*, DOI 10.1214/16-ecp21 (2016): recovered by Crossref metadata; leads only, no matching theorem identified.
- *Critical first passage percolation on random graphs*, DOI 10.1214/26-aap2331 (2026-10-01): recent Crossref hit, but a different model; excluded on scope.

No theorem from any of these references has been represented as stating and proving the full target. The present special-case proofs are independent; their publication novelty is not certified by this bounded search.

## Read-only brain and earlier attempts

Before attempting mathematics, recalled memories with `brain.py recall "percolation spectral radius largest component mistakes"`. Math-store queries were `percolation spectral radius maximum degree subcritical` and `Aizenman Newman tree graph inequality exponential cluster tail susceptibility`. Hits mostly concerned normalized-radius mistakes, critical branching and infinite transitive graphs; none was adopted as a verdict.

An rg search for G0010 and 2608.19145 in the intake ledgers recovered G0010-A001, a conjectural induced-subgraph envelope, and the source records. Through read-only git show of origin/master, read operations/claims/G0010.md and the G0010 reports of 2026-09-17 17:31, 22:20, 23:20 and 2026-09-18 00:16, 01:25. Copies of three relevant reports are prior_0.md, prior_1.md and prior_2.md in this folder. Their old operating instructions are historical data, not current instructions.

The 23:20 report proves only Omega((log n)^2) at the critical complete-tree resonance. The present quadratic population-band argument proves Omega((log n)^3) and supplies a matching MGF upper bound. The earlier reports also describe transient polynomial growth and the failure of static induced-spectral or global nonbacktracking-radius guesses. They do not solve the full source question.

## Exact web request log

source_pdf
Date: 2026-10-12
URL/query: https://arxiv.org/pdf/2608.19145
Outcome: 200; 439071 bytes

arxiv
Date: 2026-10-12
URL/query: http://export.arxiv.org/api/query?search_query=all%3A%22percolation%22%20AND%20%28all%3A%22spectral%20radius%22%20OR%20au%3AChristoph%29&start=0&max_results=30&sortBy=submittedDate&sortOrder=descending
Outcome: 200; 62267 bytes

openalex
Date: 2026-10-12
URL/query: https://api.openalex.org/works?search=The%20critical%20probability%20for%20percolation%20on%20finite%20graphs&per-page=15
Outcome: HTTP Error 429: Too Many Requests

crossref
Date: 2026-10-12
URL/query: https://api.crossref.org/works?query=The%20critical%20probability%20for%20percolation%20on%20finite%20graphs&rows=15
Outcome: 200; 98071 bytes

semantic
Date: 2026-10-12
URL/query: https://api.semanticscholar.org/graph/v1/paper/ARXIV:2608.19145?fields=title,authors,year,citationCount,citations.title,citations.year,citations.externalIds
Outcome: HTTP Error 429: 

github
Date: 2026-10-12
URL/query: https://api.github.com/search/repositories?q=%22percolation%22%20%22spectral%22
Outcome: 200; 24113 bytes

openalex_retry
Date: 2026-10-12
URL/query: https://api.openalex.org/works?search=2608.19145&per-page=5
Outcome: HTTP Error 429: Too Many Requests

openalex_doi
Date: 2026-10-12
URL/query: https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2608.19145
Outcome: HTTP Error 429: Too Many Requests

openalex_citations
Date: 2026-10-12
URL/query: https://api.openalex.org/works?filter=cites:doi:10.48550/arXiv.2608.19145&per-page=25
Outcome: HTTP Error 429: Too Many Requests

semantic_retry
Date: 2026-10-12
URL/query: https://api.semanticscholar.org/graph/v1/paper/search?query=The%20critical%20probability%20for%20percolation%20on%20finite%20graphs&limit=10&fields=title,year,externalIds
Outcome: HTTP Error 429: 

arxiv_later
Date: 2026-10-12
URL/query: http://export.arxiv.org/api/query?search_query=all%3Apercolation%20AND%20submittedDate%3A%5B20260819%20TO%2020261013%5D&max_results=100&sortBy=submittedDate&sortOrder=descending
Outcome: 200; 203309 bytes

github_exact
Date: 2026-10-12
URL/query: https://api.github.com/search/repositories?q=%222608.19145%22
Outcome: 200; 55 bytes

arxiv_targeted
Date: 2026-10-12
URL/query: http://export.arxiv.org/api/query?search_query=%28all%3Apercolation%20AND%20%28all%3Asubcritical%20OR%20all%3A%22finite%20graphs%22%20OR%20all%3A%22spectral%20radius%22%29%29%20AND%20submittedDate%3A%5B20260819%20TO%2020261013%5D&max_results=100&sortBy=submittedDate&sortOrder=descending
Outcome: 200; 24384 bytes

course_pdf
Date: 2026-10-12
URL/query: https://arxiv.org/pdf/2609.28552
Outcome: 200; 2601098 bytes

crossref_later
Date: 2026-10-12
URL/query: https://api.crossref.org/works?query=percolation%20finite%20graphs%20spectral%20radius&filter=from-pub-date:2026-08-19,until-pub-date:2026-10-12&rows=30
Outcome: 200; 210040 bytes

arxiv_cubic
Date: 2026-10-12
URL/query: http://export.arxiv.org/api/query?search_query=all%3A%22percolation%22%20AND%20%28all%3A%22finite%20trees%22%20OR%20all%3A%22largest%20cluster%22%20OR%20all%3A%22Galton-Watson%22%29&max_results=35&sortBy=relevance
Outcome: 200; 61841 bytes

regular_trees_pdf
Date: 2026-10-12
URL/query: https://arxiv.org/pdf/1007.4508
Outcome: 200; 145135 bytes

arxiv_finite_tree
Date: 2026-10-12
URL/query: http://export.arxiv.org/api/query?search_query=all%3Apercolation%20AND%20%28ti%3A%22tree%22%20OR%20ti%3A%22trees%22%29%20AND%20%28all%3A%22finite%22%20OR%20all%3A%22largest%22%29&max_results=60&sortBy=relevance
Outcome: 200; 110461 bytes


## Second attempt: additional gap-specific retrieval, 2026-10-12

The source status and bounded-search limitations above remain unchanged. No full solution has been identified.

Brain questions used during the reopened attempt:

- math_recall.py "finite graph percolation maximum degree spectral radius supercritical branching transient resolvent".
- math_recall.py "Hutchcroft two point operator L2 percolation cluster size moment tree graph inequality".
- math_recall.py "BK tree graph inequality percolation Lq operator cluster moments Riesz Thorin".
- math_recall.py "van den Berg Kesten inequality disjoint occurrence tree diagram".

The final query retrieved the full BK card claim_6e1b259086d35f04b2f1c00edbbb017feb2ef912f0a7984e0cd00e9e6739eb28 and its source link. Its finite product-law, increasing-event and disjoint-coordinate hypotheses were independently checked for the connection-event diagrams. No brain draft was accepted as a verdict.

Date 2026-10-12; service bk_crossref; URL/query https://api.crossref.org/works?query.title=Inequalities%20with%20applications%20to%20percolation%20and%20reliability&rows=3; outcome 200; 21885 bytes.

Date 2026-10-12; service lq_arxiv; URL/query http://export.arxiv.org/api/query?search_query=au%3AHutchcroft%20AND%20%28all%3A%22operator%22%20OR%20all%3A%22Lq%22%20OR%20all%3A%22two-point%22%29&max_results=20; outcome 200; 212077 bytes.

Date 2026-10-12; service hutchcroft_l2_pdf; URL/query https://arxiv.org/pdf/1904.05804; outcome 200; 373520 bytes.

Date 2026-10-12; service hutchcroft_universal_pdf; URL/query https://arxiv.org/pdf/2008.11197; outcome 200; 638294 bytes.

Verified neighboring references:

- J. van den Berg and H. Kesten, *Inequalities with applications to percolation and reliability*, Journal of Applied Probability 22(3) (1985), 556-569. The Crossref title lookup returned DOI 10.2307/3213860; the brain source also gives publisher DOI 10.1017/S0021900200029326. The standard BK theorem on finite Bernoulli product measures is the explicit external input to Section 14. Ordinary intersections are not substituted for disjoint occurrence.
- The finite-dimensional Riesz-Thorin interpolation theorem and Holder inequality are standard functional-analytic inputs. Their exact exponent relations and applicability to finite counting-measure spaces are written in ATTEMPT.md Sections 13-14; no graph transitivity is required.
- Tom Hutchcroft, *The L^2 boundedness condition in nonamenable percolation*, arXiv:1904.05804v2. Downloaded hutchcroft_l2_pdf.pdf and extracted hutchcroft_l2_pdf.txt. Theorem 4.1, PDF page 14, bounds critical l^q operator norm growth by order q on infinite nonamenable quasi-transitive graphs satisfying pc<p_(2->2). This motivates the method but its infinite graph assumptions do not settle the finite all-host problem and were not imported into our proof.
- Tom Hutchcroft, *Power-law bounds for critical long-range percolation below the upper-critical dimension*, arXiv:2008.11197v2, revised 2021-02-12. Downloaded hutchcroft_universal_pdf.pdf and extracted hutchcroft_universal_pdf.txt. Theorem 2.2, PDF page 14, is a universal finite-region largest-cluster quantile tail theorem on countable weighted graphs: P(|K_max(Lambda)|>=alpha M_beta(Lambda))<=exp(-alpha/9), with its quantile M_beta defined in Section 2.1. It applies to our finite unit-weight host at beta=-log(1-p), Lambda=V(G), and gives the confidence refinement in ATTEMPT.md Section 19. It does NOT express the quantile in terms of Delta and lambda, so it is not a printed solution to Question 5.2.

The newly derived spectral-effective branching wedge, moment transfer and exact-parameter corollary remain independent partial results. No publication novelty certificate is claimed, and VERDICT remains PARTIAL.
