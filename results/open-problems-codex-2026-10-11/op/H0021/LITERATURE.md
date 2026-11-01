# H0021 literature and prior-work audit — 2026-10-12

## Source and exact hypotheses
Asaf Cohen Antonir, Lyuben Lichev and Maksim Zhukovskii, *Universality in random graphs via optimal linking systems: trees and beyond*, arXiv:2608.06358v1, submitted 6 August 2026, manuscript dated 7 August 2026. https://arxiv.org/abs/2608.06358
Downloaded source_pdf.pdf (44 pages), source_html.txt, source_abs.html; source_text.txt is page marked.

Conjecture 1.4, Section 1.6, page 7, verbatim with mathematical typography transcribed:
> “For every ε > 0 and every integer ∆ ≥ 2, whp G(n, (1 + ε) ln n/n) is T_{n,∆}-universal.”

Definition on page 1: universal means containing an isomorphic copy of every member of the family as a subgraph. The family T_{n,∆} consists of all n-vertex trees with maximum degree at most ∆. G(n,p) has independent unordered edges on [n]; whp means probability tending to one as n tends to infinity (page 2 footnotes). ε and ∆ are fixed, and the probability applies to simultaneous universality, not to one target at a time.

Theorem 1, page 4, verbatim:
> “There exists a constant C > 1 such that, for every constant ∆ ≥ 2, whp G(n, C ln n/n) is T-universal.”
Here T=T_{n,∆}. This is NOT a solution of the stated conjecture: its existential absolute C cannot be replaced by each prescribed 1+ε. The paragraph before Conjecture 1.4 prints C/n rather than C ln n/n, inconsistent with Theorem 1; we do not import that sentence as a theorem.

## Search conclusion and limits
No source-matching solution was found in the successfully retrieved search results. This is a bounded literature search, not a proof of global open status. OpenAlex and Semantic Scholar consistently returned HTTP 429. In particular a genuine OpenAlex citation traversal could not be completed because the source's OpenAlex work ID could not be resolved. An attempted cites:arxiv:2608.06358 URL is recorded below but is not a valid resolved OpenAlex-work citation query and returned no usable data. No API key or credential was accessed.

The broad arXiv spanning-tree/degree query returned 113 entries: both pages (80 and the remaining 33) were fetched and their abstracts screened. A second broad tree-universality query returned 79 entries and all were fetched and screened. Searches include publications from 6 August through 12 October 2026 and exact linking-system terminology. None of the relevant retrieved abstracts claims the exact conjecture. Closely titled candidates were checked separately below. No SOLVED_IN_LITERATURE verdict is warranted.

## Relevant references and leads
1. Richard Montgomery, *Spanning trees in random graphs*, Advances in Mathematics 356 (2019), 106793. Source reference [70], page 42. Establishes bounded-degree spanning-tree universality at C(∆) log n/n; this remains a constant-factor bound. Primary paper not redownloaded; scope confirmed from the source's literature survey.
2. Roman Glebov and Michael Krivelevich, *On the number of Hamilton cycles in sparse random graphs*, arXiv:1207.2748v1 (11 July 2012). Primary PDF hamilton_correct.pdf and page-marked hamilton_correct.txt. Theorem 1, page 2, verbatim mathematical transcription:
   > “Let G ∼ G(n,p) with p ≥ (ln n + ln ln n + ω(1))/n. Then the number of Hamilton cycles is n!p^n(1 − o(1))^n a.a.s.”
   ATTEMPT.md §1 checks the surplus and proves that this supplies the ∆=2 special case. It says nothing about ∆≥3, so it is not a literature solution to H0021.
3. J. Komlós and E. Szemerédi, *Limit distributions for the existence of hamilton circuits in a random graph*, Discrete Mathematics 43 (1983), 55–63. Source reference [64], page 42; classical Hamiltonicity result, superseded for this special-case application by the directly fetched theorem in item 2.
4. Mostafa Mirabi, *Resilient forest universality in percolated dense graphs*, arXiv:2609.27927v1. Abstract retrieved in arxiv_recent2.txt and arxiv_universality_recent.txt. Gives bounded-degree forests of order at most ((1−α)λ−ξ)N in percolated dense hosts. The positive ξ deficit leaves the spanning case out; related lead only, not a solved conjecture. No theorem number or full-paper proof is asserted from the abstract.
5. Elad Aigner-Horev, Dan Hefetz, Yury Person and Michael Trushkin, *Exact-palette rainbow embeddings in uniformly coloured pseudorandom graphs*, arXiv:2609.30304v2; and the same authors, *Rainbow spanning configurations in uniformly coloured pseudorandom graphs*, arXiv:2609.26329v2. Abstracts retrieved in arxiv_recent.txt. These concern a prescribed tree, additional pseudorandomness/discrepancy or palette assumptions, and different density bounds. They do not state simultaneous sharp-density universality.
6. Csongor Beke, Vladimir Bošković, Nina Kamčev and Yiting Wang, *Optimal Bounds on Spanning Tree Embeddings*, arXiv:2610.08362v1 (6 October 2026). Abstract in candidate_abstracts.txt: proves an upper bound on the number of embeddings into a bounded-degree host, not an existence theorem at the random-graph threshold. Excluded as a solution.
7. Jesse Beisegel, Ekkehard Köhler, Robert Scheffler and Martin Strehler, *On Kernels and Leaves: Searching for Bare and Lush Trees*, arXiv:2609.29451v1 (24 September 2026). Abstract in candidate_abstracts.txt concerns parameterized complexity of search trees. Excluded as a solution.
8. Agelos Georgakopoulos, *Asymptotic connectivity, hamiltonicity and toughness*, arXiv:2610.09992v1 (7 October 2026). Abstract in candidate_abstracts.txt concerns coarse, quasi-isometry-invariant analogues. Excluded as a solution.

Crossref's successful broad query returned *Spanning universality in random graphs*, DOI 10.1002/rsa.20816 (2018), *Almost-spanning universality in random graphs*, DOI 10.1002/rsa.20661 (2016), and *Universality for Graphs of Bounded Degeneracy*, DOI 10.1002/rsa.70055 (March 2026). These are leads rather than imported theorems; the returned metadata establishes neither the exact threshold nor matching quantifiers. The date-filtered exact query returned no relevant sharp tree-universality theorem. The unrelated edge universality paper DOI 10.1214/25-aop1807 is spectral universality, not graph containment.

One erroneous guessed identifier, arXiv:1402.0771, downloaded an unrelated physics paper (*Violation of geometric scaling in DIS due to Coulomb corrections*, Kirill Tuchin). It was immediately excluded. Its stored files hamilton_source.pdf / hamilton_text.txt are not used as mathematical evidence. The correct Hamilton-cycle reference was located by a subsequent arXiv title/author query.

## Read-only research brain and earlier work
Ran math_recall.py with “bounded degree spanning tree universality random graph Montgomery”; the returned generic tree cards supplied no solution. Ran brain.py recall with “tree universality random graphs mistakes”; no relevant solution was returned. The recall tool reported an attempted detached index refresh that failed; no explicit brain write command was issued, and no brain content was saved by this task.
Searched probability_1000_intake_* and codex_pool_2026_10_10 for H0021 and 2608.06358. The H intake confirms the source's conjecture; no resolved attempt was recovered there. A first rg call used an unexpanded Windows directory glob and failed; the corrected directory enumeration succeeded.
Read with git show, without modifying the repository:
- origin/master:operations/claims/H0021.md
- origin/master:runs/R16/2026-09-17T19-47-43Z_h0021-sharp-almost-spanning-rollback-gap_c91e.md
The former reports ∆=2 only and unresolved port/absorption barriers. The latter gives an almost-spanning reduction with deficit O(n log log n/log n). These reports are hints, not imported certified theorems: their detailed reduction was not independently re-established in this attempt. Our reservoir result is independently proved in ATTEMPT.md and does not rely on those reports' correctness.

## Complete HTTP request log
Every request was made through Python requests from the shell, never a built-in web search tool. Raw responses are retained in the problem folder. The request to the arXiv abstract preceded the scripted log and returned HTTP 200, https://arxiv.org/abs/2608.06358, on 2026-10-12.

- 2026-10-12 — source_pdf: `https://arxiv.org/pdf/2608.06358`; HTTP 200; 735368 bytes. 

- 2026-10-12 — source_html: `https://arxiv.org/html/2608.06358v1`; HTTP 200; 2035063 bytes. 

- 2026-10-12 — arxiv: `http://export.arxiv.org/api/query?search_query=all%3A%22tree%20universality%22%20OR%20all%3A%22optimal%20linking%20systems%22&start=0&max_results=30&sortBy=submittedDate&sortOrder=descending`; HTTP 200; 14726 bytes. 

- 2026-10-12 — openalex: `https://api.openalex.org/works?search=tree%20universality%20random%20graphs&per-page=30`; HTTP 429; 609 bytes. 

- 2026-10-12 — openalex_source: `https://api.openalex.org/works?search=Universality%20in%20random%20graphs%20via%20optimal%20linking%20systems&per-page=5`; HTTP 429; 609 bytes. 

- 2026-10-12 — crossref: `https://api.crossref.org/works?query=tree%20universality%20random%20graphs&rows=25`; HTTP 200; 198873 bytes. 

- 2026-10-12 — semantic: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:2608.06358?fields=title,authors,year,citations.title,citations.externalIds,citations.year`; HTTP 429; 174 bytes. 

- 2026-10-12 — github: `https://api.github.com/search/repositories?q=tree%20universality%20random%20graphs`; HTTP 200; 55 bytes. 

- 2026-10-12 — openalex_lookup: `https://api.openalex.org/works?filter=locations.landing_page_url:https%3A%2F%2Farxiv.org%2Fabs%2F2608.06358&per-page=5`; HTTP 429; 609 bytes. 

- 2026-10-12 — openalex_citations: `https://api.openalex.org/works?filter=cites:arxiv:2608.06358&per-page=50`; HTTP 429; 609 bytes. 

- 2026-10-12 — semantic_search: `https://api.semanticscholar.org/graph/v1/paper/search?query=sharp%20threshold%20tree%20universality&limit=20&fields=title,year,externalIds,abstract`; HTTP 429; 174 bytes. 

- 2026-10-12 — arxiv_recent: `http://export.arxiv.org/api/query?search_query=%28all%3A%22spanning%20trees%22%20OR%20all%3A%22bounded-degree%20trees%22%20OR%20all%3A%22tree%20universality%22%29%20AND%20submittedDate%3A%5B202608060000%20TO%20202610122359%5D&max_results=80&sortBy=submittedDate&sortOrder=descending`; HTTP 200; 163359 bytes. 

- 2026-10-12 — crossref_exact: `https://api.crossref.org/works?query.title=sharp%20threshold%20tree%20universality&filter=from-pub-date:2026-08-06&rows=20`; HTTP 200; 185358 bytes. 

- 2026-10-12 — hamilton_source: `https://arxiv.org/pdf/1402.0771`; HTTP 200; 510652 bytes. 

- 2026-10-12 — arxiv_hamilton: `http://export.arxiv.org/api/query?search_query=ti%3A%22Hamilton%20cycles%22%20AND%20au%3AKrivelevich&max_results=15`; HTTP 200; not logged bytes. 

- 2026-10-12 — arxiv_recent_page2: `http://export.arxiv.org/api/query?search_query=%28all%3A%22spanning%20trees%22%20OR%20all%3A%22bounded-degree%20trees%22%20OR%20all%3A%22tree%20universality%22%29%20AND%20submittedDate%3A%5B202608060000%20TO%20202610122359%5D&start=80&max_results=80&sortBy=submittedDate&sortOrder=descending`; HTTP 200; not logged bytes. 

- 2026-10-12 — hamilton_correct: `https://arxiv.org/pdf/1207.2748`; HTTP 200; not logged bytes. 

- 2026-10-12 — arxiv_candidates: `http://export.arxiv.org/api/query?search_query=ti:%22Optimal%20Bounds%20on%20Spanning%20Tree%20Embeddings%22%20OR%20ti:%22Asymptotic%20connectivity%22%20OR%20ti:%22On%20Kernels%20and%20Leaves%22&max_results=10`; HTTP 200; not logged bytes. 

- 2026-10-12 — arxiv_recent_universality: `http://export.arxiv.org/api/query?search_query=all%3A%22universality%22%20AND%20%28all%3A%22trees%22%20OR%20all%3A%22tree%22%29%20AND%20submittedDate%3A%5B202608060000%20TO%20202610122359%5D&max_results=100&sortBy=submittedDate&sortOrder=descending`; HTTP 200; not logged bytes. 

GitHub returned total_count=0 for the recorded repository query. The unfiltered Crossref search and the exact/date-filtered query returned no exact matching theorem in their selected result windows. Literature coverage is limited as described above.


## Second-attempt literature and brain audit — 2026-10-12
Asked the read-only math store for the actual completion gap with:
- `math_recall.py "spanning tree absorption extendability Montgomery rollback completion bounded degree random graphs"`
- `math_recall.py "Hamiltonian k linked spanning linkage Hefetz Krivelevich Szabo spider"`
Neither returned a suitable sparse spanning-completion theorem. The second returned Ore/Dirac Hamiltonicity cards, whose dense minimum-degree hypotheses do not hold at the target probability; they were not used.

The second approach search was done with shell Python requests. Complete fresh request records follow below; raw responses are saved next to the original records.

Primary result newly checked: Richard Montgomery, *Sharp threshold for embedding combs and other spanning trees in random graphs*, arXiv:1405.6560v1, submitted 26 May 2014 (the fetched manuscript displays a September 2018 date). Theorem 1.2, page 2, verbatim mathematical transcription:
> “Let α, ε, ∆ > 0. The random graph G(n, (1 + ε) log n/n) almost surely contains a copy of every tree T ∈ T(n, ∆) which has at least αn/log^9 n disjoint bare paths with length ⌈log^9 n⌉.”

PDF: montgomery_combs.pdf; text: montgomery_combs.txt. This theorem is genuinely simultaneous for its restricted tree family. SECOND_ATTEMPT.md Theorem C proves that trees with at most n/[8(⌈log^9 n⌉+1)] leaves satisfy its hypotheses with α=1/3, using a fully written degree-2 path-packing argument. This includes all fixed leaf counts, so the independently proved two-chord three-leaf theorem is not claimed as an improvement over known literature. The quoted theorem does not solve H0021: the explicit subcubic trees uniformly subdivided at log n/log log n have no required bare paths. Its restricted quantifier cannot be changed to every bounded-degree tree.

Crossref resolved D. Hefetz, M. Krivelevich and T. Szabó, *Sharp threshold for the appearance of certain spanning trees in random graphs*, Random Structures & Algorithms 41(4) (2012), 391–412, DOI 10.1002/rsa.20472. The PDF was not fetched. Montgomery's introduction reports its linear-bare-path universality result, consistent with our special case. We use Montgomery's fetched Theorem 1.2 as the precise stronger imported result.

The title search also found Montgomery's *Sharp threshold for embedding combs and other spanning trees in random graphs* and unrelated random-geometric, weighted-tree and temporal-graph results. The exact arXiv author conjunction did not recover the Hefetz paper, so no completeness claim is based on that author search. No new full literature solution was identified and no SOLVED_IN_LITERATURE verdict is warranted.

- 2026-10-12 — arxiv_second_attempt: `http://export.arxiv.org/api/query?search_query=au%3AHefetz%20AND%20au%3AKrivelevich%20AND%20%28all%3A%22spanning%22%20OR%20all%3A%22threshold%22%29&max_results=25`; HTTP 200; 15471 bytes.

- 2026-10-12 — arxiv_exact_sharp_trees: `http://export.arxiv.org/api/query?search_query=ti%3A%22Sharp%20threshold%22%20AND%20all%3A%22spanning%20trees%22&max_results=30`; HTTP 200; 9568 bytes.

- 2026-10-12 — crossref_sharp_trees: `https://api.crossref.org/works?query.title=Sharp%20threshold%20for%20the%20appearance%20of%20certain%20spanning%20trees%20in%20random%20graphs&rows=3`; HTTP 200; 21509 bytes.

- 2026-10-12 — arxiv_montgomery_combs_pdf: `https://arxiv.org/pdf/1405.6560`; HTTP 200; 475463 bytes.
