# Literature record

Search date: 2026-10-12. All network access uses Python HTTP requests.

- 2026-10-12 openalex: `https://api.openalex.org/works?search=Hamilton+cycles+random+graphs+minimum+degree+three&per-page=30`. openalex: ERROR HTTP Error 429: Too Many Requests

- 2026-10-12 semantic: `https://api.semanticscholar.org/graph/v1/paper/search?query=Hamilton+cycles+random+graphs+minimum+degree+three&limit=20&fields=title%2Cauthors%2Cyear%2Curl%2CexternalIds%2Cabstract`. semantic: ERROR HTTP Error 429: 

- 2026-10-12 github: `https://api.github.com/search/repositories?q=Hamilton+minimum+degree+random+graph&per_page=10`. github: OK 55 bytes -> github.txt

- 2026-10-12 frieze_home: `https://www.math.cmu.edu/~af1p/`. frieze_home: OK 4796 bytes -> frieze_home.txt

- 2026-10-12 arxiv: `http://export.arxiv.org/api/query?search_query=all%3A%22Hamilton+cycles%22+AND+all%3A%22minimum+degree%22&max_results=30`. arxiv: OK 48853 bytes -> arxiv.txt

- 2026-10-12 crossref: `https://api.crossref.org/works?query=Hamilton+cycles+random+graphs+minimum+degree+at+least+3&rows=20`. crossref: OK 82660 bytes -> crossref.txt

- 2026-10-12 source: `https://www.math.cmu.edu/~af1p/ICM.pdf`. source: OK 3150444 bytes -> source.pdf

- 2026-10-12 openalex_source: `https://api.openalex.org/works?search=Alan+Frieze+Random+structures+algorithms+ICM&per_page=5`. openalex_source: ERROR HTTP Error 429: Too Many Requests

- 2026-10-12 openalex_retry: `https://api.openalex.org/works?search=Hamilton+cycles+random+graphs+minimum+degree&per_page=10`. openalex_retry: ERROR HTTP Error 429: Too Many Requests

- 2026-10-12 openalex_improved: `https://api.openalex.org/works/https://doi.org/10.1002/rsa.20978`. openalex_improved: ERROR HTTP Error 429: Too Many Requests

- 2026-10-12 improved: `https://arxiv.org/pdf/1906.01433`. improved: OK 199996 bytes -> improved.txt

- 2026-10-12 semantic_doi: `https://api.semanticscholar.org/graph/v1/paper/DOI:10.1002/rsa.20978?fields=title,year,citations.title,citations.year,citations.externalIds`. semantic_doi: OK 2757 bytes -> semantic_doi.txt

- 2026-10-12 publications: `https://www.math.cmu.edu/~af1p/papers.html`. publications: OK 102802 bytes -> publications.txt

- 2026-10-12 arxiv_recent: `http://export.arxiv.org/api/query?search_query=%28all%3Ahamiltonicity+OR+all%3A%22Hamilton+cycles%22%29+AND+%28all%3A%22degree+sequence%22+OR+all%3A%22minimum+degree+three%22+OR+all%3A%22minimum+degree+3%22%29&sortBy=submittedDate&sortOrder=descending&max_results=60`. arxiv_recent: OK 39337 bytes -> arxiv_recent.txt

- 2026-10-12 janson: `https://arxiv.org/pdf/math/0609802`. janson: OK 231287 bytes -> janson.txt

- 2026-10-12 semantic_source_search: `https://api.semanticscholar.org/graph/v1/paper/search?query=Random%20structures%20algorithms%20Frieze%20ICM&limit=5&fields=title,year,externalIds`. semantic_source_search: ERROR HTTP Error 429: 

- 2026-10-12 bibliography: `https://www.math.cmu.edu/~af1p/Texfiles/HamSurvey.pdf`. bibliography: OK 397095 bytes -> bibliography.txt

## Source verification
Alan Frieze, *Random Structures and Algorithms*, ICM 2014 lecture slides,
https://www.math.cmu.edu/~af1p/ICM.pdf, PDF pp. 166?170 (downloaded source.pdf).
PDF p. 166: ?We now consider conditoning on minimum degree at least three. Let?
followed by L_c = lim_{n??} Pr(G_{n,cn;3} is Hamiltonian), and
?Conjecture: L_c = 1 for all c ? 3/2.? [Source spelling retained.]
PDF p. 167 gives the cubic endpoint, attributed there to Robinson and Wormald (1984).
PDF pp. 168?170 give c?128, c?10, and c?3 conditional on numerical ODE solutions.
For cn nonintegral take m_n=floor(cn); at c=3/2 use even n, since odd n and floor(3n/2) have an empty sample space. This is an admissibility convention, not a counterexample.

## Confirmed later result, not a full solution
Michael Anastos and Alan Frieze, ?Hamilton cycles in random graphs with minimum degree at least 3: An improved analysis?, Random Structures & Algorithms 57 (2020), 865?878. DOI: 10.1002/rsa.20978. arXiv:1906.01433v2 (22 June 2020); downloaded PDF improved.txt, extracted improved_extracted.txt.
Theorem 1.1, PDF p. 2, verbatim mathematical transcription:
?Theorem 1.1. W.h.p. G_{n,m}^{??3} is Hamiltonian for m = cn, c > 2.662....?
This is precisely the conditioned simple labelled graph model, but covers only c>2.662..., not every c?3/2. Its abstract explicitly describes c>3/2 as the ultimate goal. Section 2.3 uses the Frieze?Pittel threshold 2.6616... for the needed expansion lemma. We retain the theorem's stated 2.662... range and do not silently strengthen it.
Section 3, Lemmas 3.1?3.3 and equations (8), PDF pp. 5?8, provide the conditioned truncated-Poisson random-sequence representation and a positive limiting lower bound on simplicity. These are relevant tools for the attempted reduction.

## Brain and prior-work audit
Read-only calls: math_recall.py ?Frieze Hamiltonian random graph minimum degree three?; brain.py recall ?Hamiltonicity minimum degree three mistakes?; brain.py recall ?random graphs Hamilton cycles?. The returned cards did not supply a solution.
Read-only rg for F0096 in 06_math_research found F0096-A001 (2026-09-08) in probability_1000_intake_F_20260908/attempts.jsonl and the intake problem row. They mention the Anastos?Frieze bound, verified above. The claim that the sole obstacle is unbounded maximum degree was not established and is not adopted. A sufficient configuration-model theorem is not automatically an equivalence with the conditioned-simple conjecture.
Read-only git ls-tree origin/master filtered for F0096/f0096 found no matching recorded-answer paths. No repository was changed.

## Search coverage and limits
arXiv API: initial title/topic query (30 results) and recent degree-sequence/minimum-degree query (60 requested). Raw feeds saved. Relevant directed-graph and dense-degree theorems have different hypotheses. GitHub returned zero repositories for the recorded query. Crossref returned the exact improved-analysis paper and earlier density bounds.
Semantic Scholar DOI lookup succeeded and returned ten citing papers, including arXiv:2001.05258 (requires minimum degree at least four), arXiv:2107.03527 (k-cores), and arXiv:2604.11633 (directed graphs). None of those metadata entries states the requested theorem. The direct topic and original-source searches were rate-limited.
OpenAlex topic search, retry, source-identity search, and exact DOI lookup all returned HTTP 429. The original slides therefore have no verified OpenAlex work identifier available in this search; an OpenAlex works-citing-original-source query could not be formed reliably. This is a coverage limitation, not evidence of absence of a solution. Semantic Scholar's citations of the closest verified theorem were checked instead.
The conclusion is only that this bounded search did not verify a full solution in print; SOLVED_IN_LITERATURE is not justified.

## Additional checked sources
Alan Frieze, *Hamilton Cycles in Random Graphs: a bibliography*, downloaded author-hosted HamSurvey.pdf (saved bibliography.txt); the actual PDF is dated July 4, 2021. Section 2.3, Problem 4, PDF p. 4: ?Is G^(3)_{n,cn}, c > 3/2 Hamiltonian w.h.p.?? It records the Anastos?Frieze improvement to 2.66... and still lists the target as a problem. This is evidence only through that PDF's date, not through 2026.
Svante Janson, *The probability that a random multigraph is simple*, Combinatorics, Probability and Computing 18 (2009), 205?225; arXiv:math/0609802v1 (28 September 2006), downloaded janson.txt. Theorem 1.1, PDF p. 3: for configurations with N=half the total degree tending to infinity, liminf P(simple)>0 iff sum d_i^2=O(N). Corollary 1.5, PDF p. 4, gives P(simple)=exp(-Lambda-Lambda^2)+o(1) if max d_i=o(sqrt(N)), where Lambda=sum d_i(d_i-1)/(4N). This is an auxiliary theorem, not a Hamiltonicity theorem.

- 2026-10-12 retry_arxiv_cubic: `http://export.arxiv.org/api/query?search_query=all%3A%22cubic%22+AND+%28all%3A%22Hamilton%22+OR+all%3A%22Hamiltonian%22%29&max_results=30`. retry_arxiv_cubic: OK 51050 bytes -> retry_arxiv_cubic.txt

- 2026-10-12 retry_arxiv_degrees: `http://export.arxiv.org/api/query?search_query=all%3A%22Hamilton%22+AND+%28all%3A%22prescribed+degree%22+OR+all%3A%22degree+sequences%22+OR+all%3A%22planted%22%29&max_results=40`. retry_arxiv_degrees: OK 73194 bytes -> retry_arxiv_degrees.txt

- 2026-10-12 retry_crossref_degrees: `https://api.crossref.org/works?query=Hamilton+cycles+random+graphs+prescribed+degree+sequence+Cooper+Frieze&rows=12`. retry_crossref_degrees: OK 50921 bytes -> retry_crossref_degrees.txt

- 2026-10-12 retry_sparse_distributions: `https://arxiv.org/pdf/1105.5913`. retry_sparse_distributions: OK 216525 bytes -> retry_sparse_distributions.txt

- 2026-10-12 retry_fixed_degrees_doi: `https://api.crossref.org/works/10.1137/080741379`. retry_fixed_degrees_doi: OK 4635 bytes -> retry_fixed_degrees_doi.txt

- 2026-10-12 retry_fixed_degrees_paper: `https://www.math.cmu.edu/~af1p/Texfiles/HamGnd.pdf`. retry_fixed_degrees_paper: OK 176789 bytes -> retry_fixed_degrees_paper.txt

## Second-attempt literature and brain checks (2026-10-12)
All new HTTP requests, service names, URLs, and errors are appended above by search.fetch, with raw artifacts retry_*.txt. The arXiv prescribed-degree/planted query and cubic-Hamilton query found no directly applicable full theorem. Crossref returned the following relevant neighboring result, fetched from its author-hosted PDF:
Colin Cooper, Alan Frieze, Michael Krivelevich, ?Hamilton Cycles in Random Graphs with a Fixed Degree Sequence?, SIAM Journal on Discrete Mathematics 24 (2010), 558?569, DOI 10.1137/080741379. Theorem 2, author PDF p.3, additionally requires A1: d_1?K_1 dbar^(1-1/(4alpha)) for sufficiently large K_1, A2: dbar?n^gamma with gamma<(2alpha-1)/(2alpha+1), and A3: dbar sufficiently large, along with tail and maximum-degree hypotheses (1),(2). It does not cover minimum degree three with the low fixed averages in F0096. The paper's exponential-tail applicability alone is insufficient. Saved retry_fixed_degrees_paper.txt and retry_fixed_degrees_extracted.txt; exact Crossref metadata saved retry_fixed_degrees_doi.txt.
Pu Gao, ?Distributions of sparse spanning subgraphs in random graphs?, arXiv:1105.5913v2, 15 January 2015. Downloaded retry_sparse_distributions.txt / retry_sparse_extracted.txt. Its abstract and framework concern G(n,p) and G(n,m), not the uniform sparse graph conditioned on minimum degree three. The overlap/likelihood idea is relevant but its model hypotheses do not supply the requested conclusion.
Read-only math-store queries were ?Hamilton cycles prescribed degree sequence small subgraph conditioning Robinson Wormald Cooper Frieze? and ?random graph minimum degree three Posa rotation expansion truncated Poisson Hamiltonicity?. Results did not contain a directly applicable theorem. REATTEMPT.md explains the used conditioning warning and the independently checked methods.
No new full solution in literature was verified in this second bounded search. The remaining-gap conclusions are mathematical results of this attempt, not attributed to these papers.

Gao arXiv:1105.5913v2, Theorem 8 requires p >> n^(-1/2) for its Hamilton-cycle concentration result in G(n,m), with m=p*binomial(n,2). F0096 has fixed m/n, so the corresponding p is of order 1/n, and also imposes rare minimum-degree conditioning. Both the density and model hypotheses fail; no transfer was claimed.
Gao Theorem 8 appears on PDF p.6 of the downloaded arXiv version; its p >> n^(-1/2) hypothesis was checked explicitly.
