# F0086 literature and search log

All searches below were run on 2026-10-11 using Python requests or local
read-only commands. Raw network responses are retained in this folder.
No built-in web search was used.

## Verified relevant references
* Hough, J. Ben; Krishnapur, Manjunath; Peres, Yuval; Virag, Balint.
  Determinantal Processes and Independence. Probability Surveys 3 (2006),
  206?229. DOI: 10.1214/154957806000000078. arXiv:math/0503110.
  Conjecture 40 at PDF p.22 (printed p.227); source.pdf and source_readable.txt.
* Branden, Petter. Solutions to two problems on permanents.
  Linear Algebra and its Applications 436 (2012), no.1, 53?58.
  DOI: 10.1016/j.laa.2011.06.022. arXiv:1104.3531v2.
  Theorem 2.3 exactly classifies universal real and complex PSD positivity;
  the real positive parameters are exactly 2/m for positive integers m.
  Primary PDF read, proof pp.4?6 checked; Crossref metadata independently
  confirms title, author, journal, pages, DOI and publication date.
* Frenkel, Peter E. Remarks on the alpha-permanent.
  Mathematical Research Letters 17 (2010), no.4, 795-802.
  DOI: 10.4310/MRL.2010.V17.N4.A17. arXiv:0912.1018.
  Primary PDF downloaded as branden.pdf (filename reflects an initial
  author misattribution; the actual author is Frenkel). This paper gives
  partial positivity results and explicitly leaves the conjecture open;
  it is NOT the decisive solution.
* Shirai, Tomoyuki. Remarks on the positivity of alpha-determinants.
  Kyushu Journal of Mathematics 61 (2007), no.1, 169?189.
  Referenced by both primary later PDFs and September intake records;
  earlier interval conjecture and exclusion beyond 2. Its PDF was not newly
  fetched here, and the conclusion of this report does not depend on
  independently verifying its theorem.
* Scott, Alexander D.; Sokal, Alan D. Complete monotonicity for inverse powers
  of some combinatorially defined polynomials. Cited as a preprint in
  Branden's paper, Theorem 2.6. Not independently fetched here; dependency
  of the published solution, not a separate verified result in this report.

## Network searches and fetches
* source: https://arxiv.org/pdf/math/0503110
  HTTP 200. Primary PDF fetched and read.
* arxiv: https://export.arxiv.org/api/query?search_query=all:alpha-permanent&max_results=20
  HTTP 200. Broad alpha-permanent query noisy; found Frenkel and Crane.
* openalex: https://api.openalex.org/works?search=alpha%20permanent%20Branden&per-page=10
  HTTP 429: shared unauthenticated IP budget exhausted. No results obtained.
* crossref: https://api.crossref.org/works?query=alpha%20permanent%20Branden&rows=10
  HTTP 200. Broad alpha permanent Branden query; found Frenkel DOI among noisy results.
* semantic: https://api.semanticscholar.org/graph/v1/paper/search?query=alpha%20permanent&limit=10&fields=title,authors,year,url,externalIds
  HTTP 200. alpha permanent search; identified Frenkel arXiv:0912.1018 and DOI.
* github: https://api.github.com/search/repositories?q=alpha+permanent
  HTTP 200. q=alpha permanent, 32 repository matches; no mathematical resolution established from repositories.
* branden_search: https://export.arxiv.org/api/query?search_query=au:Branden+AND+all:determinants&max_results=20
  HTTP 200. au:Branden AND all:determinants; found arXiv:1104.3531, explicit complete solution.
* crossref_exact: https://api.crossref.org/works?query.bibliographic=Branden%20alpha%20determinants%20conjectures&rows=5
  HTTP 200. Branden alpha determinants conjectures bibliographic search; retained response.
* openalex_source: https://api.openalex.org/works/https://doi.org/10.1214/154957806000000078
  HTTP 429: shared unauthenticated IP budget exhausted. No results obtained.
* openalex_citing: https://api.openalex.org/works?filter=cites:W2109297066&per-page=100
  HTTP 429: shared unauthenticated IP budget exhausted. No results obtained.
* openalex_citing_doi: https://api.openalex.org/works?filter=cites:https%3A%2F%2Fdoi.org%2F10.1214%2F154957806000000078&per-page=100
  HTTP 429: shared unauthenticated IP budget exhausted. No results obtained.
* crossref_solution: https://api.crossref.org/works?query.title=Solutions%20to%20two%20problems%20on%20permanents&rows=3
  HTTP 200. Exact solution title; publication metadata verified.
* branden_solution: https://arxiv.org/pdf/1104.3531
  HTTP 200. Primary PDF fetched and read.
* frenkel: https://arxiv.org/pdf/0912.1018
  HTTP 200. Primary PDF fetched and read.

OpenAlex citation limitation: the first citing request used an unverified
candidate work ID W2109297066 and yielded only HTTP 429; it is not evidence
that this ID identifies the source. A DOI-resolution request for the source
and a subsequent DOI-based citing-works request were also rate limited.
No claim about the contents of the citing-works list is made.

## Read-only brain and earlier-work searches
* brain.py recall "alpha determinantal processes mistakes" and
  "alpha determinantal processes": unrelated hints; no resolution found.
* math_recall.py "alpha permanent positivity Branden": unrelated cards;
  no pertinent theorem or linked card to follow.
* First rg search of a literal wildcard intake directory failed under Windows;
  corrected by enumerating probability_1000_intake_* directories.
* Searched those intake directories for F0086 and read exact matching entries
  in problems.jsonl and attempts.jsonl of probability_1000_intake_F_20260908.
  Their open-status statement was stale in light of Branden (2012).
  Their immanant speculation was not relied on.
* Searched codex_pool_2026_10_10 for F0086: no matching output.
* git ls-tree -r --name-only origin/master in math-open-problems and filtered
  for F0086/f0086: no matching problem artifact found. Working tree untouched.

## Decision
The problem is answered in published literature; stop at status-first stage.
Conjecture 40's universal interval is disproved. Its alpha>2 exclusion follows
from the same exact classification. ATTEMPT.md provides the full implication
from a negative finite PSD alpha-determinant to a regular kernel with no point
process. No explicit numerical matrix or new theorem is claimed.

2026-10-11 continuation: re-read local branden_solution.txt, Theorem 2.3,
and ATTEMPT.md. No additional network search needed for the already verified
literature resolution. Corrected claim citation encoding.
