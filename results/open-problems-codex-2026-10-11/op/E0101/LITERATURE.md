# Literature checks

Date: 2026-10-12. Bounded search; API failures do not establish openness.

- arxiv: http://export.arxiv.org/api/query?search_query=all%3A%22branching+random+walk%22+AND+all%3A%22boundary%22&start=0&max_results=40&sortBy=submittedDate&sortOrder=descending
  Result: ok; <?xml version='1.0' encoding='UTF-8'?>
<feed xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/" xmlns:arxiv="http:/
- openalex: https://api.openalex.org/works?search=On+the+boundary+at+infinity+for+branching+random+walk&per-page=10
  Result: error; HTTP Error 429: Too Many Requests
- crossref: https://api.crossref.org/works?query=branching+random+walk+boundary+limiting+measure+support&rows=20
  Result: ok; {"status":"ok","message-type":"work-list","message-version":"1.0.0","message":{"facets":{},"total-results":1657477,"item
- semantic: https://api.semanticscholar.org/graph/v1/paper/ARXIV:2205.15287?fields=title,authors,year,citationCount,citations.title,citations.year,citations.externalIds
  Result: error; HTTP Error 429: 
- github: https://api.github.com/search/repositories?q=branching+random+walk+boundary
  Result: ok; {"total_count":0,"incomplete_results":false,"items":[]}

- Follow-up bbm, 2026-10-12: https://arxiv.org/pdf/2509.06730
  Result: ok; 1854925

- Follow-up martin, 2026-10-12: https://arxiv.org/pdf/2308.03711
  Result: ok; 368170

- Follow-up kwsearch, 2026-10-12: http://export.arxiv.org/api/query?search_query=au%3AKaimanovich+AND+au%3AWoess+AND+all%3Abranching&max_results=10
  Result: ok; 2616

- Follow-up openalex_doi, 2026-10-12: https://api.openalex.org/works/https://doi.org/10.1214/23-ECP560
  Result: error; HTTP Error 429: Too Many Requests

- Follow-up openalex_citing, 2026-10-12: https://api.openalex.org/works?filter=cites%3Adoi%3A10.1214%2F23-ECP560&per-page=50
  Result: error; HTTP Error 429: Too Many Requests

- Follow-up semantic_citing, 2026-10-12: https://api.semanticscholar.org/graph/v1/paper/DOI:10.1214/23-ECP560/citations?fields=title,year,externalIds&limit=100
  Result: ok; 2404

- Citation follow-up kw, 2026-10-12: https://arxiv.org/pdf/2205.13615
  Result: ok; 36

- Citation follow-up entropy, 2026-10-12: https://arxiv.org/pdf/2607.20097
  Result: ok; 24

- Citation follow-up woess, 2026-10-12: https://arxiv.org/pdf/2405.07301
  Result: ok; 28

## Source verified
Elisabetta Candellero and Tom Hutchcroft, *On the boundary at infinity for branching random walk*, arXiv:2205.15287v1 (30 May 2022); Electronic Communications in Probability **28** (2023), 1-12, DOI 10.1214/23-ECP560. Downloaded source.pdf, extracted source.txt. Problem 4.2 is on PDF p. 9:
> Give conditions under which the support of W coincides almost surely with the set of accumulation points of B.
The governing assumptions are Theorem 1.1, PDF p. 2: transient irreducible countable-state chain, homogeneous supercritical offspring with L log L. Page 9 itself supplies a lamplighter non-equality example and expects equality for sufficiently nice examples such as hyperbolic groups.

## Search results and limitations
The broad arXiv query returned 40 records (saved search_arxiv.txt). A narrower author query found Kaimanovich-Woess. Crossref returned 20 metadata hits and recovered the source DOI. GitHub returned zero repositories. Semantic Scholar's source lookup was rate-limited, but the DOI-based citation endpoint succeeded and returned ten citing works, listed below. OpenAlex source search and DOI resolution returned HTTP 429. The attempted OpenAlex citation URL used an unresolved DOI where that filter requires an OpenAlex work ID: it is not a valid completed citation search; no OpenAlex citation coverage is claimed. A fresh valid DOI-filter lookup is recorded separately. These are bounded checks, not an exhaustive certification of openness.

The downloaded papers were searched/read for support, accumulation, regularity, Dirichlet and Problem 4.2. No inspected paper states and proves the exact source question under the source's general hypotheses. In particular the broad sufficient criterion proved in ATTEMPT.md is our deduction, not a theorem quoted from a later paper. No SOLVED_IN_LITERATURE verdict is justified.

## Relevant references and why they are leads
1. Vadim A. Kaimanovich and Wolfgang Woess, *Limit distributions of branching Markov chains*, arXiv:2205.13615v2 (8 June 2022), Annales de l'Institut Henri Poincare, Probabilites et Statistiques **59** (2023), no. 4, 1951-1983, DOI 10.1214/22-AIHP1344. Downloaded kw.pdf/kw.txt. Proposition 3.19, PDF p. 18, characterizes Dirichlet regularity by concentration of exit measures; Proposition 3.38, PDF p. 24, supplies regularity for suitable quasi-transitive geometric compactifications; PDF p. 25 recalls the Martin/hyperbolic identification. These supply inputs to our proof. Their measure-convergence theorem is not itself the requested support equality.
2. Wolfgang Woess, *Notes on hyperbolic branching Brownian motion*, arXiv:2405.07301, downloaded latest version, published DOI reported by Semantic Scholar: 10.1016/j.spa.2026.104965. Downloaded woess.pdf/woess.txt. Questions 7.6, PDF p. 26, distinguish topological support from dimension of the measure. The same page's note added in proof attributes a support-dimension conclusion to Geldbach; this attribution does not follow from Geldbach's stated theorem. See the explicit discrepancy in ATTEMPT.md. Brownian motion is a different model and is not a solution in print for the discrete countable-state question.
3. David Geldbach, *Hyperbolic branching Brownian motion: the empirical limit measure*, arXiv:2509.06730v3 (27 May 2026), 19 PDF pages. Downloaded bbm.pdf/bbm.txt. Theorem 1.1 gives dim(mu_infinity)=min{2 beta,1}; Corollary 3.2, PDF p. 11, proves its upper bound through a countable union of typical-particle endpoint sets. The paper defines the dimension of a measure using full-measure sets; it does not prove that the closed topological support has this dimension. Its group analogue appears as a conjectural extension, PDF pp. 17-18.
4. Daniela Bertacchi, Elisabetta Candellero and Fabio Zucca, *Martin boundaries and asymptotic behavior of branching random walks*, arXiv:2308.03711v5. Downloaded martin.pdf/martin.txt (26 pages). The results concern survival/persistence in subgraphs and t-Martin boundaries; no claimed support-equality solution was located.
5. Jeremie Brieussel, Robin Kaiser, Martin Klotzer and Ecaterina Sava-Huss, *Phase transition for the asymptotic entropy of branching random walks on groups*, arXiv:2607.20097, downloaded revision dated 24 August 2026 (24 pages). Downloaded entropy.pdf/entropy.txt. Main result is an empirical-entropy transition; final discussion asks about singularity of the boundary empirical measure. It is not the support equality.
6. Matthieu Dussaule, Longmin Wang and Wenyuan Yang, *Branching Random Walks on relatively hyperbolic groups*, arXiv:2211.07213; Annals of Probability **53** (2025), 391-452 (publication information in Woess's reference list). ArXiv abstract inspected; limit-set theory, not an inspected proof of this measure-support question.
7. Vladas Sidoravicius, Longmin Wang and Kainan Xiang, *Limit set of branching random walks on hyperbolic groups*, arXiv:2007.13267; Communications on Pure and Applied Mathematics **76** (2023), no. 10, 2765-2803 (publication information in Geldbach's references). Limit-set theorem predates the source preprint; no support-measure theorem claimed here.

## Semantic Scholar citation results (2026-10-12)
- Phase transition for the asymptotic entropy of branching random walks on groups (2026), identifiers: {"ArXiv": "2607.20097", "CorpusId": 290443818}.
- Notes on hyperbolic branching Brownian motion (2026), identifiers: {"DOI": "10.1016/j.spa.2026.104965", "CorpusId": 287241153}.
- Critical parameters of germ-monotone families of branching random walks (2026), identifiers: {"ArXiv": "2602.21062", "CorpusId": 286000552}.
- Hyperbolic branching Brownian motion: the empirical limit measure (2025), identifiers: {"ArXiv": "2509.06730", "CorpusId": 281203655}.
- On the Critical Parameters of Branching Random Walks (2025), identifiers: {"ArXiv": "2507.14676", "DOI": "10.3390/math13182962", "CorpusId": 280281166}.
- Limit theorems for the empirical distribution of supercritical branching random walks on transitive graphs (2025), identifiers: {"ArXiv": "2502.07633", "DOI": "10.1214/26-ejp1504", "CorpusId": 276259021}.
- Biased branching random walks on Bienaym\'e--Galton--Watson trees (2025), identifiers: {"ArXiv": "2502.07363", "CorpusId": 276258748}.
- Multifractal spectrum of branching random walks on free groups (2024), identifiers: {"ArXiv": "2409.01346", "CorpusId": 272367408}.
- Notes on hyperbolic branching Brownian motion (2024), identifiers: {"ArXiv": "2405.07301", "CorpusId": 269758121}.
- Limit distributions of branching Markov chains (2022), identifiers: {"ArXiv": "2205.13615", "DOI": "10.1214/22-AIHP1344", "CorpusId": 249151930}.

## Broad arXiv returned titles (for reproducible screening)
- http://arxiv.org/abs/2601.21054v1 ? Trimmed branching random walk and a free obstacle problem
- http://arxiv.org/abs/2601.07129v2 ? Minimum and extremal process for a branching random walk outside the boundary case
- http://arxiv.org/abs/2512.18937v1 ? The critical percolation window in growing random graphs
- http://arxiv.org/abs/2510.13733v1 ? Internal Diffusion Limited Aggregation with Critical Branching Random Walks
- http://arxiv.org/abs/2509.06730v3 ? Hyperbolic branching Brownian motion: the empirical limit measure
- http://arxiv.org/abs/2507.09737v1 ? Spinal decomposition, martingale convergence and the Seneta-Heyde scaling for matrix branching random walks
- http://arxiv.org/abs/2412.16601v1 ? Dynamic Phenomena in Interacting Particle Systems: Phase Transitions and Equilibrium
- http://arxiv.org/abs/2409.01346v3 ? Multifractal spectrum of branching random walks on free groups
- http://arxiv.org/abs/2408.05538v2 ? Branching random walk conditioned on large martingale limit
- http://arxiv.org/abs/2402.04827v3 ? The scaling limit of the volume of loop O(n) quadrangulations
- http://arxiv.org/abs/2312.00711v1 ? Thick points of 4D critical branching Brownian motion
- http://arxiv.org/abs/2308.03711v5 ? Martin boundaries and asymptotic behavior of branching random walks
- http://arxiv.org/abs/2212.13593v1 ? Traveling/non-traveling phase transition and non-ergodic properties in the random transverse-field Ising model on the Cayley tree
- http://arxiv.org/abs/2211.07213v1 ? Branching Random Walks on relatively hyperbolic groups
- http://arxiv.org/abs/2210.01092v2 ? Multifractal analysis and Erdös-Rényi laws of large numbers for branching random walks in $\R^d$
- http://arxiv.org/abs/2206.04941v2 ? The extremal position of a branching random walk on the general linear group
- http://arxiv.org/abs/2205.15287v1 ? On the boundary at infinity for branching random walk
- http://arxiv.org/abs/2203.14737v2 ? Time spent in a ball by a critical branching random walk
- http://arxiv.org/abs/2110.10544v1 ? The probability of reaching a receding boundary by branching random walk with fading branching and heavy-tailed jump distribution
- http://arxiv.org/abs/2106.02880v4 ? Right-Most Position of a Last Progeny Modified Branching Random Walk
- http://arxiv.org/abs/2009.13866v1 ? Heavy range of the randomly biased walk on Galton-Watson trees in the slow movement regime
- http://arxiv.org/abs/2007.13267v1 ? Limit set of branching random walks on hyperbolic groups
- http://arxiv.org/abs/2004.03871v2 ? The maximum of a branching random walk with stretched exponential tails
- http://arxiv.org/abs/1911.09563v2 ? Monotonicity of escape probabilities for branching random walks on \Z^{d}
- http://arxiv.org/abs/1909.00459v2 ? Solutions to kinetic-type evolution equations: beyond the boundary case
- http://arxiv.org/abs/1907.04111v3 ? A simple method to find all solutions to the functional equation of the smoothing transform
- http://arxiv.org/abs/1810.03750v1 ? Restricted percolation critical exponents in high dimensions
- http://arxiv.org/abs/1806.09943v2 ? Fluctuations of Biggins' martingales at complex parameters
- http://arxiv.org/abs/1805.09417v2 ? Diffractive electron-nucleus scattering and ancestry in branching random walks
- http://arxiv.org/abs/1712.08979v1 ? The Minimal Position of a Stable Branching Random Walk
- http://arxiv.org/abs/1703.09792v1 ? The near-critical Gibbs measure of the branching random walk
- http://arxiv.org/abs/1611.05220v1 ? Convergence of complex martingales in the branching random walk: the boundary
- http://arxiv.org/abs/1610.03575v1 ? On Seneta-Heyde Scaling for a stable branching random walk
- http://arxiv.org/abs/1607.05501v1 ? A short proof of the asymptotic of the minimum of the branching random walk after time $n$
- http://arxiv.org/abs/1511.06932v4 ? First passage percolation on the exponential of two-dimensional branching random walk
- http://arxiv.org/abs/1510.00602v2 ? Necessary and sufficient conditions for the convergence of the consistent maximal displacement of the branching random walk
- http://arxiv.org/abs/1502.07390v3 ? Branching random walk with selection at critical rate
- http://arxiv.org/abs/1502.05655v1 ? Continuity estimates for the complex cascade model on the phase boundary
- http://arxiv.org/abs/1406.6971v2 ? The minimum of a branching random walk outside the boundary case
- http://arxiv.org/abs/1402.5864v1 ? A necessary and sufficient condition for the non-trivial limit of the derivative martingale in a branching random walk

## Read-only prior-work checks
Before the attempt, math_recall.py queried "branching random walk hyperbolic boundary limiting measure"; brain.py recall queried "branching random walk boundary" and "branching random walk boundary mistakes". During the attempt math_recall.py queried "hyperbolic group convergence action harmonic measure nonatomic". These produced broad background, no verified solution.
The intake ledger probability_1000_intake_E_20260908/attempts.jsonl contains E0101-A001: its directional-UI equivalence is unsupported and was not adopted. The problem ledger confirms Problem 4.2. Read-only rg also searched codex_pool_2026_10_10 with no matching output. A read-only origin/master filename search in math-open-problems found no E0101/2205.15287 path. No working-tree changes were made there.

- Valid OpenAlex DOI-filter lookup, 2026-10-12: https://api.openalex.org/works?filter=doi%3Ahttps%3A%2F%2Fdoi.org%2F10.1214%2F23-ecp560&per-page=5
  Result: HTTP Error 429: Too Many Requests

Further standard references used through the source and Kaimanovich-Woess: Alano Ancona, *Negatively curved manifolds, elliptic operators, and the Martin boundary*, Annals of Mathematics **125** (1987), no. 3, 495-536; Alano Ancona, *Positive harmonic functions and hyperbolicity*, in *Potential Theory?Surveys and Problems*, Lecture Notes in Mathematics **1344**, Springer (1988), 1-23. These are boundary-identification inputs, not solutions of Problem 4.2.
