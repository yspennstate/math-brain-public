# C0109 literature status — 2026-10-11

No exact solution in print was verified. This is a bounded search, not a
proof of absence. OpenAlex and Semantic Scholar returned HTTP 429 on all
attempts, limiting citation coverage. No SOLVED_IN_LITERATURE verdict.

## Exact source

Terence Tao and Van Vu, “From the Littlewood-Offord problem to the
Circular Law: Universality of the spectral distribution of random matrices,”
Bulletin of the AMS 46 (2009), 377–396, DOI
10.1090/S0273-0979-09-01252-X; arXiv:0810.2994v3 (1 January 2009).
Section 6, PDF/printed p.22:

> Circular Law. A natural question here is to investigate the rate of convergence. In [54], we observed that under the extra assumption that the (2 + ε)-moment of the entries are bounded, we can have rate of convergence of order n−δ, for some positive constant δ depending on ε. The exact dependence between ε and δ is not clear.

The surrounding model (pp.1–3) is iid entries with one fixed law, mean
zero, unit variance, normalized by n^(-1/2). No bounded density is assumed.
The intake's “optimal rate” phrase is a paraphrase, not a verbatim quote.

[54] Terence Tao and Van Vu, “Random matrices: The circular law,”
Communications in Contemporary Mathematics 10 (2008), 261–307,
DOI 10.1142/S0219199708002788, arXiv:0708.2895v5. Its p.4 states:

> One can obtain some quantitative estimates on the rate of convergence as well. For example, under the (2 + η)th moment assumption, we can show that almost surely, the distance sup_{s,t} |μ_n(s, t) − μ_∞(s, t)| between μ_n and the limiting distribution μ_∞ in the uniform metric is at most n^{−η′} for some constant η′ > 0 and all sufficiently large n.

Subscripts/superscripts are transcribed into readable notation from the PDF.
This identifies random-ESD almost-sure eventual rectangle discrepancy.
Sections 13–14 discuss refinements, not a sharp dependence.

## Relevant later papers and scope

1. Friedrich Götze and Jonas Jalowy, “Rate of convergence to the Circular
   Law via smoothing inequalities for log-potentials,” Random Matrices:
   Theory and Applications 10 (2021), 2150026,
   DOI 10.1142/S201032632150026X; arXiv:1807.00489v3, 9 April 2021.
   Definition 2(A), p.4: centered variance-one independent entries, all
   absolute moments finite. Theorems 6 and 7, p.6: ball and rectangle
   discrepancy <=n^(-1/2+eta) with failure <=n^(-Q), for every eta,Q>0
   and sufficiently large n. These are inputs for EACH FIXED finite-past
   law in ATTEMPT.md. They do not assert this under only (2+eps)-moments.
   Theorem 8 excludes the edge and uses 4+delta moments: different scope.

2. Jonas Jalowy, “The Wasserstein distance to the circular law,” Annales
   de l'Institut Henri Poincaré, Probabilités et Statistiques 59 (2023),
   2285–2307, DOI 10.1214/22-AIHP1317; arXiv:2111.03595v3,
   28 October 2022. Theorem 1, p.2 gives W_1 <=n^(-1/2+eta) with failure
   <=n^(-Q) under ALL moments. Theorem 3, p.3 gives expected Ginibre
   W_1 <=4/sqrt(n). Lemma 5, p.4 is a geometric quantization bound.
   Stronger-moment/Gaussian cases do not answer the weak-moment question.

3. Friedrich Götze and Alexander Tikhomirov, “The circular law for random
   matrices,” Annals of Probability 38 (2010), 1444–1491,
   DOI 10.1214/09-AOP522; arXiv:0709.3995v4. Fetched PDF.
   Finite moments above two; circular-law convergence, not a verified
   theorem giving the optimal eps-dependent rate. Lead, not a solution.

4. Friedrich Götze, Alexey Naumov, Alexander Tikhomirov, “On local laws
   for non-Hermitian random matrices and their products,” Random Matrices:
   Theory and Applications 9 (2020), 2050004; arXiv:1708.06950v2.
   API abstract explicitly assumes finite (4+delta)-moment. Local law on
   optimal scale with logarithmic factors. Abstract-level lead only.

5. Elizabeth S. Meckes and Mark W. Meckes, “A rate of convergence for the
   circular law for the complex Ginibre ensemble,” Annales de la Faculté
   des Sciences de Toulouse 24 (2015), 93–117,
   DOI 10.5802/afst.1443; arXiv:1406.1396v3. Ginibre Wasserstein rates;
   Gaussian special case; API/Crossref lead only.

6. Terence Tao and Van Vu (appendix by Manjunath Krishnapur), “Random
   matrices: Universality of ESDs and the circular law,” Annals of
   Probability 38 (2010), 2023–2065, DOI 10.1214/10-AOP534.
   Qualitative finite-second-moment universality differs from a sharp
   polynomial rate. Brain bibliographic lead, not newly fetched.

Recent arXiv rate-query results were inspected: band matrices,
spectral-radius results, and a 2026 spectral-properties thesis concern
other models/statistics or local laws. No matching theorem was verified.
GitHub yielded rkw0k/Random-Matrix-Theory, an examples repository.

## Search receipts (Python urllib from shell)

- Date 2026-10-11; service `source`; query/URL `https://arxiv.org/pdf/0810.2994`; result: ok; 2769596 bytes saved.

- Date 2026-10-11; service `arxiv`; query/URL `https://export.arxiv.org/api/query?search_query=all%3A%22circular%20law%22%20AND%20%28all%3Arate%20OR%20all%3Amoment%29&start=0&max_results=35`; result: ok; 64478 bytes saved.

- Date 2026-10-11; service `openalex`; query/URL `https://api.openalex.org/works?search=circular%20law%20rate%20convergence%20moment&per-page=30`; result: HTTP Error 429: Too Many Requests.

- Date 2026-10-11; service `openalex_source`; query/URL `https://api.openalex.org/works?search=From%20the%20Littlewood%20Offord%20problem%20to%20the%20circular%20law&per-page=5`; result: HTTP Error 429: Too Many Requests.

- Date 2026-10-11; service `crossref`; query/URL `https://api.crossref.org/works?query=circular%20law%20rate%20convergence%20moment&rows=25`; result: ok; 119460 bytes saved.

- Date 2026-10-11; service `semantic`; query/URL `https://api.semanticscholar.org/graph/v1/paper/search?query=circular%20law%20rate%20convergence&limit=25&fields=title,authors,year,externalIds,url,abstract`; result: HTTP Error 429: .

- Date 2026-10-11; service `github`; query/URL `https://api.github.com/search/repositories?q=circular%20law%20random%20matrix&per_page=15`; result: ok; 5422 bytes saved.

- Date 2026-10-11; service `jalowy_w1`; query/URL `https://arxiv.org/pdf/2111.03595`; result: ok; 4293485 bytes saved.

- Date 2026-10-11; service `jalowy_k`; query/URL `https://arxiv.org/pdf/1807.00489`; result: ok; 620588 bytes saved.

- Date 2026-10-11; service `gotze`; query/URL `https://arxiv.org/pdf/0709.3995`; result: ok; 447651 bytes saved.

- Date 2026-10-11; service `crossref_source`; query/URL `https://api.crossref.org/works?query.title=From%20the%20Littlewood-Offord%20problem%20to%20the%20circular%20law&rows=3`; result: ok; 34082 bytes saved.

- Date 2026-10-11; service `arxiv_recent`; query/URL `https://export.arxiv.org/api/query?search_query=all:%22circular%20law%22%20AND%20all:%22rate%22&sortBy=submittedDate&sortOrder=descending&max_results=30`; result: ok; 28553 bytes saved.

- Date 2026-10-11; service `openalex_doi`; query/URL `https://api.openalex.org/works/https://doi.org/10.1090/S0273-0979-09-01252-X`; result: HTTP Error 429: Too Many Requests.

- Date 2026-10-11; service `semantic_source`; query/URL `https://api.semanticscholar.org/graph/v1/paper/ARXIV:0810.2994?fields=title,citations.title,citations.year,citations.externalIds`; result: HTTP Error 429: .

- Date 2026-10-11; service `original_rate`; query/URL `https://arxiv.org/pdf/0708.2895`; result: ok; 399789 bytes saved.

- Date 2026-10-11; service `openalex_citing`; query/URL `https://api.openalex.org/works?filter=cites:doi:10.1090/s0273-0979-09-01252-x&per-page=50`; result: HTTP Error 429: Too Many Requests.

- Date 2026-10-11; service `openalex_search_retry`; query/URL `https://api.openalex.org/works?search=circular%20law%202%2Bepsilon%20rate&per-page=15`; result: HTTP Error 429: Too Many Requests.

- Date 2026-10-11; service `arxiv_weak`; query/URL `https://export.arxiv.org/api/query?search_query=all:%22circular%20law%22%20AND%20(all:%22weak%20moment%22%20OR%20all:%22heavy%20tail%22%20OR%20all:%22convergence%20rate%22)&max_results=30`; result: ok; 7440 bytes saved.

- Date 2026-10-11; service `w1_crossref`; query/URL `https://api.crossref.org/works?query.title=The%20Wasserstein%20distance%20to%20the%20circular%20law&rows=3`; result: ok; 23333 bytes saved.

- Date 2026-10-11; service `arxiv_lower`; query/URL `https://export.arxiv.org/api/query?search_query=all:%22circular%20law%22%20AND%20(all:%22optimal%20rate%22%20OR%20all:%22lower%20bound%22)&max_results=30`; result: HTTP Error 429: Unknown Error.

The OpenAlex citation lookup could not be completed: the source DOI
lookup returned 429, preventing resolution to a work ID. A tentative
DOI-based cites-filter request also returned 429; it is NOT treated as
a successful or validated citing-works search. Semantic Scholar's source
and citations request also returned 429. No absence conclusion follows.

## Read-only brain and prior attempts

Ran math_recall.py “circular law rate truncation”; brain.py recall
“circular law mistakes” and “random matrices circular law”. Searched
intake/codex-pool ledgers for C0109 and read team_O/w335/C0109_proof.md.
These distinguish scalar tail bounds from spectral lower bounds and
warn against nonnormal rank/n perturbation arguments. The earlier
“caps delta” statement was not accepted as a proof.
Read-only origin/master listing with scoped *C0109* and *circular*
patterns returned no matching paths. No repository was changed.

## Search result inventories

### arxiv.xml

- The strong circular law: a combinatorial view; http://arxiv.org/abs/1904.11108v3
- The circular law for non-Hermitian random band matrices up to bandwidth $N^{2/3+c}$; http://arxiv.org/abs/2508.18143v3
- Rate of Convergence to the Circular Law via Smoothing Inequalities for Log-Potentials; http://arxiv.org/abs/1807.00489v3
- A rate of convergence for the circular law for the complex Ginibre ensemble; http://arxiv.org/abs/1406.1396v3
- The Local Circular Law III: General Case; http://arxiv.org/abs/1212.6599v2
- The local circular law II: the edge case; http://arxiv.org/abs/1206.3187v3
- The circular law for non-Hermitian random band matrices: optimal bandwidth, periodic profile and discrete law; http://arxiv.org/abs/2609.01295v2
- Circular law for non-Hermitian block band matrices with slowly growing bandwidth; http://arxiv.org/abs/2511.01744v3
- Local circular law for the product of a deterministic matrix with a random matrix; http://arxiv.org/abs/1603.04066v2
- Rate of Convergence of the Empirical Spectral Distribution Function to the Semi-Circular Law; http://arxiv.org/abs/1407.2780v3
- The Circular Law for Random Matrices with Intra-row Dependence; http://arxiv.org/abs/1801.04659v1
- The Wasserstein distance to the Circular Law; http://arxiv.org/abs/2111.03595v3
- Circular law, Extreme Singular values and Potential theory; http://arxiv.org/abs/0705.3773v2
- On the rate of convergence to the semi-circular law; http://arxiv.org/abs/1109.0611v3
- Optimal bounds for convergence of expected spectral distributions to the semi-circular law for the $4+ε$ moment ensemble; http://arxiv.org/abs/1511.03692v1
- Random Matrices: The circular Law; http://arxiv.org/abs/0708.2895v5
- The heterogeneous gas with singular interaction: Generalized circular law and heterogeneous renormalized energy; http://arxiv.org/abs/1402.7007v2
- Circular Law for Random Block Band Matrices with Genuinely Sublinear Bandwidth; http://arxiv.org/abs/2008.03850v2
- On the spectral radius of a random matrix: an upper bound without fourth moment; http://arxiv.org/abs/1607.05484v2
- Optimal Bounds for Convergence of Expected Spectral Distributions to the Semi-Circular Law; http://arxiv.org/abs/1405.7820v4
- Rate of convergence for products of independent non-Hermitian random matrices; http://arxiv.org/abs/1912.09300v2
- Heat flow and repeated differentiation of polynomials with i.i.d. roots; http://arxiv.org/abs/2609.24867v2
- The circular law for random matrices; http://arxiv.org/abs/0709.3995v4
- The circular law for random regular digraphs with random edge weights; http://arxiv.org/abs/1508.00208v3
- Inhomogeneous Circular Law for Correlated Matrices; http://arxiv.org/abs/2005.13533v2
- Products of Independent Non-Hermitian Random Matrices; http://arxiv.org/abs/1012.4497v3
- Fluctuation Around the Circular Law for Random Matrices with Real Entries; http://arxiv.org/abs/2002.02438v8
- Convergence of the spectral radius of a random matrix through its characteristic polynomial; http://arxiv.org/abs/2012.05602v2
- Gaussian fluctuations for non-Hermitian random matrix ensembles; http://arxiv.org/abs/math/0502400v2
- Spectral radius of random matrices with independent entries; http://arxiv.org/abs/1907.13631v5
- On Local laws for non-Hermitian random matrices and their products; http://arxiv.org/abs/1708.06950v2
- Spectral properties of Random Matrices; http://arxiv.org/abs/2609.11011v1
- Partial linear eigenvalue statistics for non-Hermitian random matrices; http://arxiv.org/abs/1912.08856v2
- Large deviation theorem for zeros of polynomials and Hermitian random matrices; http://arxiv.org/abs/1611.04271v1
- On $*$-Convergence of Schur-Hadamard Products of Independent Nonsymmetric Random Matrices; http://arxiv.org/abs/2008.05916v2

### arxiv_recent.json

- Spectral properties of Random Matrices; http://arxiv.org/abs/2609.11011v1
- The Wasserstein distance to the Circular Law; http://arxiv.org/abs/2111.03595v3
- Inhomogeneous Circular Law for Correlated Matrices; http://arxiv.org/abs/2005.13533v2
- Rate of convergence for products of independent non-Hermitian random matrices; http://arxiv.org/abs/1912.09300v2
- Partial linear eigenvalue statistics for non-Hermitian random matrices; http://arxiv.org/abs/1912.08856v2
- Quantitative invertibility of random matrices: a combinatorial perspective; http://arxiv.org/abs/1908.11255v3
- Spectral radius of random matrices with independent entries; http://arxiv.org/abs/1907.13631v5
- The strong circular law: a combinatorial view; http://arxiv.org/abs/1904.11108v3
- Rate of Convergence to the Circular Law via Smoothing Inequalities for Log-Potentials; http://arxiv.org/abs/1807.00489v3
- Optimal bounds for convergence of expected spectral distributions to the semi-circular law for the $4+ε$ moment ensemble; http://arxiv.org/abs/1511.03692v1
- Rate of Convergence of the Empirical Spectral Distribution Function to the Semi-Circular Law; http://arxiv.org/abs/1407.2780v3
- A rate of convergence for the circular law for the complex Ginibre ensemble; http://arxiv.org/abs/1406.1396v3
- Optimal Bounds for Convergence of Expected Spectral Distributions to the Semi-Circular Law; http://arxiv.org/abs/1405.7820v4
- The heterogeneous gas with singular interaction: Generalized circular law and heterogeneous renormalized energy; http://arxiv.org/abs/1402.7007v2
- On the rate of convergence to the semi-circular law; http://arxiv.org/abs/1109.0611v3

### arxiv_weak.json

- Around the circular law; http://arxiv.org/abs/1109.3343v4
- Spectrum of non-Hermitian heavy tailed random matrices; http://arxiv.org/abs/1006.1713v5
- On Local laws for non-Hermitian random matrices and their products; http://arxiv.org/abs/1708.06950v2

## Second serious attempt — 2026-10-11

Two new routes are in SECOND_APPROACHES.md. The gap-directed brain calls
were math_recall.py on “circular law weak moments quantitative Hermitization
upper bound Götze Tikhomirov”, “small singular values Gaussian perturbation
Wegner estimate logarithmic integrability”, “local circular law sparse
matrices cumulants truncation”, “Tao Vu controlled second moment least
singular value truncation”, and “negative second moment identity singular
values distance Gaussian projection”. None returned a matching optimal
rate theorem; unrelated or withdrawn cards were not used as evidence.

Published inputs rechecked directly in downloaded PDFs:

- Tao–Vu, arXiv:0708.2895v5, Definition 2.2, pp.6–7; Lemma 2.4, p.7;
  Theorem 2.5, p.8. Its constants precede the entry-law quantifier and
  depend on a controlled second moment and the prescribed shift/failure
  exponents. It proves arbitrarily high polynomial least-singular-value
  probability bounds, not the optimal circular-law rate. Theorem 2.5
  is used for the fixed original law and fixed matching Gaussian in the
  direct upper proof; also uniform raw truncations in the transfer lemma.
- Jalowy, arXiv:2111.03595v3, Corollary 2, p.2, fixed all-moments expected
  W_1 rate. Used ONLY for a fixed matching Gaussian law, after phase
  rotation diagonalizes its real covariance. No n-dependent all-moments
  rate is imported.
- Götze–Tikhomirov, arXiv:0709.3995v4, Theorems 1.1–1.2, p.2. The
  exact checked hypothesis is finite E|X|^2(log(1+|X|))^(19+eta),
  and the stated object is the EXPECTED ESD. This is a qualitative lead,
  not a theorem resolving the requested optimal random-ESD rate.

New searches, all from Python urllib and saved raw:

- 2026-10-11; second_arxiv_sparse; `https://export.arxiv.org/api/query?search_query=all:%22local%20circular%20law%22%20AND%20all:sparse&max_results=20`; ok; 756 bytes.

- 2026-10-11; second_arxiv_gaussian; `https://export.arxiv.org/api/query?search_query=all:%22singular%20values%22%20AND%20all:%22Gaussian%20perturbation%22&max_results=15`; ok; 12671 bytes.

- 2026-10-11; second_crossref; `https://api.crossref.org/works?query=local%20circular%20law%20sparse%20moment&rows=15`; ok; 99363 bytes.


Inventory: second_arxiv_sparse.json

No entries returned. This is not an absence proof.

Inventory: second_arxiv_gaussian.json

- Probabilistic Analysis of Least Squares, Orthogonal Projection, and QR Factorization Algorithms Subject to Gaussian Noise; http://arxiv.org/abs/2409.18905v3
- Sparse Pseudospectral Shattering; http://arxiv.org/abs/2411.19926v3
- Overlaps, Eigenvalue Gaps, and Pseudospectrum under real Ginibre and Absolutely Continuous Perturbations; http://arxiv.org/abs/2005.08930v1
- Well-Conditioned Oblivious Perturbations in Linear Space; http://arxiv.org/abs/2604.23193v1
- Tight Differentially Private PCA via Matrix Coherence; http://arxiv.org/abs/2510.26679v1

The Gaussian-perturbation search yielded condition-number and
pseudospectral results rather than a matching optimal-rate theorem.
Crossref's relevant sparse-circular-law leads were Basak–Rudelson,
“The circular law for sparse non-Hermitian matrices,” Ann. Probab. 47
(2019), 2359–2416, DOI 10.1214/18-AOP1310, and Rudelson–Tikhomirov,
“The sparse circular law under minimal assumptions,” GAFA 29 (2019),
561–637, DOI 10.1007/s00039-019-00492-6. These are citation-level leads;
their full theorems were not fetched or used. No novelty claim is made
for the direct derivation, and no SOLVED_IN_LITERATURE conclusion follows.
