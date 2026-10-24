
Search batch, 2026-10-12 (direct HTTP):
- source: https://www.stat.berkeley.edu/~aldous/RWG/book.pdf
  Result: OK 1861415; raw response saved when successful.
- arxiv: https://export.arxiv.org/api/query?search_query=all%3A%22last%20visited%22%20AND%20all%3A%22random%20walk%22&max_results=20
  Result: OK 12375; raw response saved when successful.
- openalex: https://api.openalex.org/works?search=last%20visited%20vertex%20transitive%20random%20walk&per-page=15
  Result: <HTTPError 429: 'Too Many Requests'>; raw response saved when successful.
- crossref: https://api.crossref.org/works?query=last%20visited%20vertex%20random%20walk%20transitive&rows=15
  Result: OK 55109; raw response saved when successful.
- semantic: https://api.semanticscholar.org/graph/v1/paper/search?query=last%20visited%20vertex%20random%20walk&limit=15&fields=title,authors,year,url,abstract
  Result: <HTTPError 429: ''>; raw response saved when successful.
- github: https://api.github.com/search/repositories?q=last%20visited%20vertex%20random%20walk
  Result: OK 55; raw response saved when successful.
- openalex_source: https://api.openalex.org/works?search=Reversible%20Markov%20Chains%20and%20Random%20Walks%20on%20Graphs&per-page=5
  Result: <HTTPError 429: 'Too Many Requests'>; raw response saved when successful.

Search batch, 2026-10-12 (direct HTTP):
- source: https://www.stat.berkeley.edu/~aldous/RWG/book.pdf
  Result: OK 1861415; raw response saved when successful.
- arxiv: https://export.arxiv.org/api/query?search_query=all%3A%22last%20visited%22%20AND%20all%3A%22random%20walk%22&max_results=20
  Result: OK 12375; raw response saved when successful.
- openalex: https://api.openalex.org/works?search=last%20visited%20vertex%20transitive%20random%20walk&per-page=15
  Result: <HTTPError 429: 'Too Many Requests'>; raw response saved when successful.
- crossref: https://api.crossref.org/works?query=last%20visited%20vertex%20random%20walk%20transitive&rows=15
  Result: OK 55106; raw response saved when successful.
- semantic: https://api.semanticscholar.org/graph/v1/paper/search?query=last%20visited%20vertex%20random%20walk&limit=15&fields=title,authors,year,url,abstract
  Result: <HTTPError 429: ''>; raw response saved when successful.
- github: https://api.github.com/search/repositories?q=last%20visited%20vertex%20random%20walk
  Result: OK 55; raw response saved when successful.
- openalex_source: https://api.openalex.org/works?search=Reversible%20Markov%20Chains%20and%20Random%20Walks%20on%20Graphs&per-page=5
  Result: <HTTPError 429: 'Too Many Requests'>; raw response saved when successful.

- 2026-10-12 openalex_retry: https://api.openalex.org/works?search=last%20visited%20vertex%20random%20walk&per_page=10
  Result: <HTTPError 429: 'Too Many Requests'>.

- 2026-10-12 openalex_source_retry: https://api.openalex.org/works?search=Reversible%20Markov%20Chains%20Random%20Walks%20Graphs%20Aldous%20Fill&per_page=5
  Result: <HTTPError 429: 'Too Many Requests'>.

- 2026-10-12 semantic_retry: https://api.semanticscholar.org/graph/v1/paper/search?query=vertex%20transitive%20cover%20time&limit=10&fields=title,authors,year,url
  Result: <HTTPError 429: ''>.

- 2026-10-12 crossref_exact: https://api.crossref.org/works?query=Aldous%20Fill%20last%20vertex%20uniform%20distribution&rows=10
  Result: OK 36071.

- 2026-10-12 arxiv_transitive: https://export.arxiv.org/api/query?search_query=all%3A%22vertex-transitive%22%20AND%20%28all%3A%22cover%20time%22%20OR%20all%3A%22last%22%29&max_results=40
  Result: OK 28239.

- 2026-10-12 arxiv_last: https://export.arxiv.org/api/query?search_query=all%3A%22last%20vertex%22%20AND%20all%3A%22random%20walk%22&max_results=30
  Result: OK 5465.

- 2026-10-12 DOI fetch: https://doi.org/10.1002/jgt.3190170505; <HTTPError 403: 'Forbidden'>.

- 2026-10-12 DOI fetch: https://doi.org/10.47443/dml.2022.158; OK 240038.

- 2026-10-12 primary paper fetch: https://www.dmlett.com/archive/v11/DML23_v11_pp96-98.pdf; OK 240038.

- 2026-10-12 primary paper fetch: https://arxiv.org/pdf/2202.02255; OK 1038044.

- 2026-10-12 primary paper fetch: https://arxiv.org/pdf/2602.21277; OK 1080440.

- 2026-10-12 primary paper fetch: https://arxiv.org/pdf/2601.03864; OK 648796.
# Source verification and assessment (2026-10-12)

Aldous, David, and James Allen Fill. *Reversible Markov Chains and Random Walks on Graphs*. Unfinished monograph, 2002; recompiled 2014. https://www.stat.berkeley.edu/~aldous/RWG/book.pdf . Downloaded as `source.pdf`; full extracted text in `source_full.txt`.

Open Problem 7.10, printed and PDF page 246, word for word (PDF line breaks normalized):

> Let V denote the last state to be hit. In a sequence of vertex-transitive graphs with n → ∞, is it always true that V converges (in variation distance, say) to the uniform distribution?

The sentence itself does not specify the initial law. The fixed-start interpretation is the substantive one investigated here: uniform initialization already gives exact uniformity, by Proposition 1 of ATTEMPT.md. The setting of §7.1.1, PDF p.238, explicitly starts with an irreducible finite transition matrix and defines symmetry as transitive action of probability-preserving permutations. The problem specifies vertex-transitive graphs, rather than all symmetric reversible chains. This attempt uses connected, undirected, unweighted simple graphs and simple random walk. No bounded-degree or aperiodicity condition appears in the problem sentence. Laziness used in our proofs preserves the ordinary walk's discovery order.

## Relevant references and their scope

1. László Lovász and Peter Winkler, “A note on the last new vertex visited by a random walk,” *Journal of Graph Theory* **17**(5) (1993), 593–596. DOI: 10.1002/jgt.3190170505. Crossref metadata and abstract inspected in `crossref.txt` and `literature_inspection.txt`. The abstract classifies the finite exact-uniformity-on-other-vertices property: only cycles and complete graphs have it. This predates the source and is NOT the asymptotic question. Our cycle and complete-graph proofs are elementary proofs of known special cases, not novelty claims. The publisher PDF was not obtained in the initial DOI fetch.

2. Calum Buchanan, Paul Horn and Puck Rombach, “On the last new vertex visited by a random walk in a directed graph,” *Discrete Mathematics Letters* **11** (2023), 96–98. DOI: 10.47443/dml.2022.158. Primary PDF: https://www.dmlett.com/archive/v11/DML23_v11_pp96-98.pdf . Downloaded and inspected (`directed_paper.pdf`, `directed_paper_full.txt`). Extends the Lovász–Winkler exact classification to directed graphs. Its abstract explicitly distinguishes exact equality from inequalities in other graphs. Lemma 1 (p.96) gives a superharmonic-type inequality for last-vertex probabilities away from adjacency. This is a structural lead, NOT a solution of asymptotic uniformity on arbitrary undirected vertex-transitive graph sequences.

3. Nathanaël Berestycki, Jonathan Hermon and Lucas Teyssier, “On the universality of fluctuations for the cover time,” arXiv:2202.02255, version 4 (metadata returned by arXiv). The inspected abstract assumes bounded degree and characterizes Gumbel cover-time fluctuations and uncovered-set decorrelation through Diam(G)^2=o(n/log n). This is a relevant special-regime lead, not a theorem covering all the hypotheses of P0247. Primary PDF fetch and text inspection are logged below.

   Primary PDF examined: arXiv:2202.02255v4, 21 January 2026; manuscript date 22 January 2026, 57 pages. Theorem 1.2 (PDF/printed p.4) gives total-variation approximation of the uncovered set at deterministic times, under either the fixed-root law P_o or stationary P_pi, with the diameter condition (DC). It does not state P0247 as posed.

   Theorem 4.8 (PDF/printed p.39) reads, with line breaks normalized and formulas transcribed:

   > Let (Γ) be a collection of finite connected vertex-transitive graphs of fixed degree satisfying (DC). Let k ≥ 1. As n → ∞, we have, under Pπ, dTV(U(τk), Unifk) → 0.

   Here τ_k is the first time exactly k vertices remain uncovered, and Unif_k is uniform over k-element vertex subsets. The crucial qualifier is **under P_pi**. For k=1, U(τ_1) is the singleton containing the eventual last vertex, whose marginal under P_pi is already exactly uniform by transitivity. Thus k=1 of this theorem provides no fixed-start result. The proof on pp.41–42 likewise explicitly begins under P_pi. Remark 1.9 (p.6) explains that fixed-degree statements also apply to uniformly bounded degrees; this does not remove (DC) or the initialization qualifier in Theorem 4.8. No fixed-start claim is imported from this theorem. See `theorem_excerpts.txt` and `last_points_extract.py` for the inspected passages.

4. Nathanaël Berestycki, Jonathan Hermon and Lucas Teyssier, “Stationary hitting times on vertex-transitive graphs,” arXiv:2601.03864, version 1 (metadata returned by arXiv). The inspected abstract refines stationary hitting-time exponential approximations, with improved bounds using graph growth. Relevant estimates, not the fixed-start final-discovery statement. Primary PDF fetch and text inspection are logged below.

5. Oren Louidor and Santiago Saglietti, “A Limit in Law for the Cover Time and Last Visited Vertex of Wired Planar Domains,” arXiv:2602.21277, version 1. The arXiv abstract gives a limiting normalized critical Liouville measure for the last vertex in wired planar domains. Wired planar domains are a different, generally nontransitive graph model; the result is not a solution to P0247. Authors verified from the arXiv Atom response. Primary PDF fetched and extracted in `wired_planar.pdf` and `wired_planar_full.txt`.

## Search limitations and verdict

Both OpenAlex search and source-resolution requests returned HTTP 429. Consequently the requested OpenAlex citation traversal could not be completed: `followup.py` contains the conditional citing-works request, but no source work identifier was returned, so no successful citing-works response exists. Semantic Scholar also returned HTTP 429 on both attempts. GitHub repository search succeeded and returned zero repositories. arXiv and Crossref searches succeeded. Every HTTP query actually issued is logged below, including unsuccessful requests. The searches are bounded and do not certify current open status or exhaustiveness.

No inspected paper states and proves P0247 with the same objects, hypotheses and quantifiers. Therefore **SOLVED_IN_LITERATURE is not justified**. This is not a claim that no solution exists.

## Read-only research-brain and prior-work checks

- math_recall.py query: `last vertex cover time vertex transitive`; related cover-time cards, no direct answer.
- math_recall.py --id claim_91c7ac51f0a03c606944fa03e7c90e9ba6c62f157f42f3f34ac2440bc2d4daa9: earlier attempt proved double stochasticity and the complete-graph example, explicitly left the fixed-start problem unresolved. Those claims were independently reproved here.
- brain.py recall queries: `random walks last vertex mistakes`, `last discovered vertex random walk`. Related cautions about cycle periodicity, graph thickening and unrelated prior problems; no verdict imported.
- Initial rg command using a literal Windows wildcard directory failed. `inspect.py` subsequently expanded the intake-directory glob in Python and searched JSON/JSONL files for P0247, along with the codex pool. No P0247 lines were returned in `inspection.txt`.
- Read-only `git ls-tree origin/master` with path-name filtering for P0247/last vertex/final discovery returned no matching file paths. This is a path-name check only, not a comprehensive content search of the large repository. No working-tree changes, commits or pushes were made.

## Raw search log
