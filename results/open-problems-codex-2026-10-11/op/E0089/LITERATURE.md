# E0089 literature audit — 2026-10-12

Source fetched: Zsolt Bartha and Gabor Pete, Noise sensitivity in bootstrap percolation, arXiv:1509.08454v1 (28 September 2015), 16 pages. Local source.pdf and source.txt. Question 1.4(a), PDF page 3; Remark 3.4, PDF page 10.

IMPORTANT CORRECTION: the remark names phi(G), a conditional occupation probability, not theta(G) or a critical density. The remark itself already explains why an o(n^-1/2) switching bound is problematic. The prior intake assertion that the source overlooked the obstruction is inaccurate.

Searches (all 2026-10-12; raw responses retained):

- ['arxiv', 'https://export.arxiv.org/api/query?search_query=all%3A%22bootstrap%20percolation%22%20AND%20all%3A%22noise%22&max_results=50', 'OK', '<?xml version=\'1.0\' encoding=\'UTF-8\'?>\n<feed xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/" xmlns:arxiv="http://arxiv.org/schemas/atom" xmlns="http://www.w3.org/2005/Atom"']
- ['openalex', 'https://api.openalex.org/works?search=Noise%20sensitivity%20in%20bootstrap%20percolation&per-page=30', 'HTTP Error 429: Too Many Requests', '']
- ['crossref', 'https://api.crossref.org/works?query.title=Noise%20sensitivity%20in%20bootstrap%20percolation&rows=15', 'OK', '']
- ['semantic', 'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1509.08454?fields=title,authors,year,externalIds,citations.title,citations.year,citations.externalIds', 'HTTP Error 429: ', '']
- ['github', 'https://api.github.com/search/repositories?q=bootstrap%20percolation%20noise%20sensitivity', 'OK', '']
- ['openalex_regular', 'https://api.openalex.org/works?search=bootstrap%20percolation%20random%20regular%20noise%20sensitivity&per-page=30', 'HTTP Error 429: Too Many Requests', '']
- ['oa_retry', 'https://api.openalex.org/works?search=Noise%20sensitivity%20in%20bootstrap%20percolation&per_page=10', 'HTTP Error 429: Too Many Requests']
- ['oa_source', 'https://api.openalex.org/works/https://arxiv.org/abs/1509.08454', 'HTTP Error 429: Too Many Requests']
- ['crossref_regular', 'https://api.crossref.org/works?query=bootstrap%20percolation%20random%20regular%20graph%20noise&rows=30', 'OK']
- ['s2_search', 'https://api.semanticscholar.org/graph/v1/paper/search?query=Noise%20sensitivity%20in%20bootstrap%20percolation&limit=10&fields=title,year,externalIds', 'HTTP Error 429: ']
- ['arxiv_regular', 'https://export.arxiv.org/api/query?search_query=all%3A%22bootstrap%20percolation%22%20AND%20all%3A%22regular%22&max_results=50', 'OK']
- ['oa_citations_search', 'https://api.openalex.org/works?filter=cites:W2330601998&per-page=100', 'HTTP Error 429: Too Many Requests']

The openalex cites:W2330601998 request used an UNVERIFIED identifier, returned HTTP 429, and is discarded: it provides no citation evidence. Source identity lookup and title lookup are attempted separately. OpenAlex rate limiting prevented its forward-citation audit. Semantic Scholar initially returned 429, but its dedicated citations endpoint later succeeded and returned three citing papers, all fetched and screened. No paper proving the exact question has been found; this is a bounded-search result, not proof that none exists.
## Further searches and citation screening

All dated 2026-10-12. Exact URLs and HTTP outcomes for the third batch are in search_log3.json; source-citing PDF requests are in citation_fetch_log.json. Raw responses are retained.

- Semantic Scholar dedicated citations endpoint: https://api.semanticscholar.org/graph/v1/paper/ARXIV:1509.08454/citations?fields=title,year,externalIds&limit=100 — SUCCESS, three citing works, no next-page marker. This is that service's returned list, not an exhaustive citation census.
- OpenAlex exact title filter and source URL lookup: HTTP 429. The requested OpenAlex citing-works audit could not be completed because a verified OpenAlex source identifier was not obtained.
- arXiv query all:"k-core" AND (all:"quenched" OR all:"noise") — seven hits, mostly unrelated physics; none states the target. See arxiv_quenched.data. Query all:"bootstrap percolation" AND all:"regular" — 17 hits; abstracts screened, selected PDFs fetched. Query all:"bootstrap percolation" AND all:"noise" — five hits, including the source and Hartarsky below.
- Crossref query.title for the source title did not return the source in its first 15 records; broad regular-graph query returned Balogh-Pittel and Choi-Yu. These are relevance rankings, not exact-match status certificates.
- GitHub repository query bootstrap percolation noise sensitivity — zero repositories returned.

Relevant references and what they actually provide:

1. Zsolt Bartha and Gabor Pete, **Noise sensitivity in bootstrap percolation**, arXiv:1509.08454v1, 28 September 2015. Theorem 1.1, PDF page 2: the weaker probability-at-least-1-eps result. Question 1.4(a), PDF page 3: the target; Remark 3.4, PDF page 10: conditional-probability concentration suggestion and its obstacle. Not a solution to its own question. Source quote (normalized typography, no change of mathematical content):

   > Question 1.4. Consider the sequence G_{n,d}, and let 2 <= k <= d - 2.
   > (a) Is there a delta > 0 such that P_{G_{n,d}}(Corr_{p_c(n)}(f_n(omega), f_n(omega^epsilon)) > delta) -> 1, as n -> infinity?

   The fixed epsilon parameter is inherited from the preceding noise-sensitivity discussion. The meaningful range is 0<epsilon<1. The source overloads p_c(n), as discussed in ATTEMPT.md Section 1.

2. Jozsef Balogh and Boris G. Pittel, **Bootstrap percolation on the random regular graph**, Random Structures & Algorithms 30 (2007), 257-286, DOI 10.1002/rsa.20158. Crossref metadata verified. Original PDF link in the source is obsolete; https://math.illinois.edu/~jobal/cikk/bootfig.pdf returned 404. Its threshold results are quoted as Theorems 3.1-3.3 in the fetched Bartha-Pete PDF, and are used only at that level. It predates the target question and supplies annealed thresholds, not the missing quenched probability-one noise bound.

3. Svante Janson, **On percolation in random graphs with given vertex degrees**, arXiv:0804.1656; Electronic Journal of Probability 14 (2009), paper 5, 87-118. Fetched PDF identifies itself as v1. Section 5 relates bootstrap percolation to the (d+1-k)-core of initially vacant vertices; Theorems 5.5 and 5.6 concern threshold window/hitting time. Useful single-replica lead; no conditional two-replica concentration theorem for the target. This predates Bartha-Pete.

4. Jeong-Ok Choi and Unjong Yu, **Phase transition in the diffusion and bootstrap percolation models on regular random and Erdos-Renyi networks**, arXiv:2108.12082 (2021), Journal of Computational Physics, DOI 10.1016/j.jcp.2021.110670. Fetched PDF abstract says the models are studied using modified Newman-Ziff algorithms. It measures transition/order-parameter behavior and uses bootstrap terminology for a different removal convention. No theorem proves Question 1.4(a).

5. Ivailo Hartarsky, **U-bootstrap percolation: critical probability, exponential decay and applications**, arXiv:1806.11405v4, 11 June 2020; DOI 10.1214/20-AIHP1112. Returned by Semantic Scholar as a source-citing work; full PDF fetched. Theorem 3.6, PDF page 14, concerns noise sensitivity of one-arm events for finite-range update families on a lattice, at fixed density. Its discussion explicitly cites Bartha-Pete Question 1.3. Neither the graph model nor event nor target quantifiers match E0089. A lead, not a solution.

6. Vincent Tassion and Hugo Vanneuville, **Noise sensitivity of percolation via differential inequalities**, arXiv:2011.04572v2, 18 January 2023; DOI 10.1112/plms.12507. Returned as a source-citing work; full PDF fetched. Abstract and Theorem 1.1 concern critical planar Bernoulli crossing events, not bootstrap occupation on random regular graphs. The source is cited in a background sentence and bibliography; no target solution.

7. Ivailo Hartarsky and Lyuben Lichev, **Explosive appearance of cores and bootstrap percolation on lattices**, arXiv:2501.18976 (fetched PDF dated 23 January 2026), Combinatorica, DOI 10.1007/s00493-026-00213-2. Returned as a source-citing work; full PDF fetched. Abstract proves a single-step giant core/bootstrap hitting-time transition on two-dimensional tori and related lattices. Different graph and different assertion. Not E0089.

8. Aleksandr Rodionov, **Seed thresholds and degree variance in heterogeneous bootstrap percolation with growing degrees**, arXiv:2610.04420v1 (fetched PDF dated 29 September 2026). New regular-graph-related hit, full PDF fetched. It concerns independent threshold-one/two vertex rules and degrees tending to infinity, fixed-relative-margin seed thresholds, and explicitly does not identify a shrinking random critical window. Different hypotheses; no solution to the fixed-d, homogeneous-k target.

Additional arXiv abstracts screened: 2112.01778 (Bootstrap percolation, probabilistic cellular automata and sharpness), 2410.20457 (Dynamical random field Ising model at zero temperature), 2505.00958 (Extended Persistent Homology Distinguishes Simple and Complex Contagions with High Accuracy); none addresses the target. Regular-query raw metadata includes all 17 hits and their references.

## Read-only prior-work audit

- brain.py recall queries: "bootstrap percolation random regular graphs mistakes" and "bootstrap percolation random regular graphs". Returned mostly unrelated regular-graph records and prior intake cautions; no solution card. The authorized recall command itself reported an internal detached index-refresh side effect. No remember command was used.
- math_recall.py queries: "bootstrap percolation noise sensitivity Janson" and, during the attempt, "k-core random graphs asymptotic normality Janson Luczak". Returned standard noise/Fourier and percolation cards, mostly off-target for the second query. No returned card was treated as a verdict.
- Intake ledgers searched for E0089 and 1509.08454. Read E0089-A001 in probability_1000_intake_E_20260908/attempts.jsonl; its confusion of observable and asserted unproved switching bounds are corrected in ATTEMPT.md. A broad initial rg search was too noisy because other problem rows embed this source; subsequent inspection was restricted to the E0089 record.
- Local codex_pool_2026_10_10 directory searched for an E0089 folder; none was returned. Read-only git ls-tree on origin/master in math-open-problems, filtered to /E0089/, returned no corresponding dedicated folder. No repository working tree was touched.

Verdict of the bounded literature search: no exact theorem proving Question 1.4(a) found. SOLVED_IN_LITERATURE is NOT claimed. OpenAlex access failure is a material completeness limitation.
Further exact fetch/search URLs and outcomes (2026-10-12):

- ['janson', 'https://arxiv.org/pdf/0804.1656', 'OK']
- ['choi', 'https://arxiv.org/pdf/2108.12082', 'OK']
- ['new2026', 'https://arxiv.org/pdf/2610.04420', 'OK']
- ['balogh', 'https://math.illinois.edu/~jobal/cikk/bootfig.pdf', 'HTTP Error 404: Not Found']
- ['oa_title', 'https://api.openalex.org/works?filter=title.search:Noise%20sensitivity%20in%20bootstrap%20percolation&per-page=5', 'HTTP Error 429: Too Many Requests']
- ['s2_citations', 'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1509.08454/citations?fields=title,year,externalIds&limit=100', 'OK']
- ['arxiv_quenched', 'https://export.arxiv.org/api/query?search_query=all%3A%22k-core%22%20AND%20%28all%3A%22quenched%22%20OR%20all%3A%22noise%22%29&max_results=30', 'OK']

Janson Theorem 5.6 is on PDF page 33 and explicitly concerns the configuration multigraph; its subsequent paragraph cautions about simple-graph transfer. Referenced lead: Svante Janson and Malwina J. Luczak, Asymptotic normality of the k-core in random graphs, arXiv:math/0612827 (bibliography of fetched Janson PDF; not separately fetched in this attempt).


## Second serious attempt — 2026-10-12

Read-only math-store queries on the actual gap:

- `quenched bootstrap percolation random regular graph independent replicas k-core concentration Janson Luczak`: no applicable concentration theorem found.
- `dependency graph central limit theorem bounded variables cumulants Janson Baldi Rinott`: returned generic CLT and a graph-dependent bounded-difference paper (arXiv:2110.05374), but no verified theorem needed for this attempt. The conditional CLT is proved directly by counting dependency-connected moment tuples in SECOND_ATTEMPT.md.

Shell/Python arXiv searches, exact queries, URLs, and outcomes follow (all dated 2026-10-12; XML retained):

- ['local_clt', 'all:"random regular" AND (all:"local statistics" OR all:"central limit")', 'https://export.arxiv.org/api/query?search_query=all%3A%22random%20regular%22%20AND%20%28all%3A%22local%20statistics%22%20OR%20all%3A%22central%20limit%22%29&max_results=20', 'OK']
- ['peeling', 'all:"k-core" AND (all:"critical" OR all:"peeling")', 'https://export.arxiv.org/api/query?search_query=all%3A%22k-core%22%20AND%20%28all%3A%22critical%22%20OR%20all%3A%22peeling%22%29&max_results=20', 'OK']
- ['dependency', 'ti:"A central limit theorem by differential calculus"', 'https://export.arxiv.org/api/query?search_query=ti%3A%22A%20central%20limit%20theorem%20by%20differential%20calculus%22&max_results=20', 'OK']
- ['simple', 'ti:"The probability that a random multigraph is simple"', 'https://export.arxiv.org/api/query?search_query=ti%3A%22The%20probability%20that%20a%20random%20multigraph%20is%20simple%22&max_results=20', 'OK']

Selected PDF fetches, with exact URLs/outcomes (full PDFs and extracted texts retained):

- ['math/0609802', 'https://arxiv.org/pdf/math/0609802', 'OK']
- ['1505.05484', 'https://arxiv.org/pdf/1505.05484', 'OK']
- ['1302.7014', 'https://arxiv.org/pdf/1302.7014', 'OK']

References actually used or assessed:

- Svante Janson, **The probability that a random multigraph is simple**, arXiv:math/0609802v1 (28 September 2006). Theorem 1.1, fetched PDF page 3, gives positivity of the simplicity probability when sum d_i^2=O(sum d_i). Applied to fixed d it rigorously permits conditioning configuration-model cycle moment bounds on simplicity. Theorem 1.4, fetched PDF pages 3-4, gives the asymptotic formula; at fixed d it yields exp(-(d^2-1)/4). This is a neighbouring theorem, not a solution to E0089.
- G. J. Baxter, S. N. Dorogovtsev, K.-E. Lee, J. F. F. Mendes, and A. V. Goltsev, **Critical dynamics of the k-core pruning process**, arXiv:1505.05484v1 (20 May 2015). Fetched abstract describes critical 1/t^2 relaxation and a long near-critical plateau for uncorrelated random networks. This supports the relevance of the bottleneck lead, but its statements are not used as rigorous finite-size theorems. The d=4,k=2 recursion and all claimed bounds are proved independently and their algebra kernel-checked.
- Jiayang Jiang, Michael Mitzenmacher, Justin Thaler, **Parallel Peeling Algorithms**, arXiv:1302.7014 (fetched version). Fetched abstract treats random uniform hypergraphs at fixed distances below/above threshold, with log-log versus logarithmic peeling depths. Different model/regime; does not justify any critical-window depth bound for the target. No theorem from it is used in Theorems A or B.

No newly found paper states and proves Question 1.4(a). The new mathematical conclusions are our proved local special cases, not SOLVED_IN_LITERATURE. No OpenAlex/Semantic Scholar/GitHub repeat was needed for this neighbouring-method search; the first attempt's full bounded status audit and its limitations remain recorded above.
