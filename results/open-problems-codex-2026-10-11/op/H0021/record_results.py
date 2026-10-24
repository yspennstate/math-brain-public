import pathlib,json
base=pathlib.Path('.')
logs=json.loads((base/'search_log.json').read_text(encoding='utf8'))
parts=['# H0021 literature and prior-work audit — 2026-10-12\n',
'''## Source and exact hypotheses
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
''']
for a in logs:
 parts.append(f"- {a['date']} — {a['service']}: `{a['url']}`; HTTP {a.get('status','ERROR')}; {a.get('bytes','not logged')} bytes. {a.get('error','')}\n")
(base/'LITERATURE.md').write_text('\n'.join(parts),encoding='utf8')
claims=[
 dict(problem_id='H0021',claim='For every fixed ε>0, G(n,(1+ε)log n/n) is T_{n,2}-universal whp.',status='proved_special_case',proof_location='ATTEMPT.md §1; LITERATURE.md item 2',remaining_gap='Δ≥3 remains unresolved; proof imports the cited primary Hamilton-cycle theorem.',checks='Tree classification proved explicitly; density surplus εlog n−log log n→∞; primary Theorem 1 downloaded, page 2.'),
 dict(problem_id='H0021',claim='For fixed 0<c<1 and Δ≥2, G(n,c log n/n) is not T_{n,Δ}-universal whp.',status='proved',proof_location='ATTEMPT.md §2',remaining_gap='Lower bound only, not a counterexample to conjectured c>1 conclusion.',checks='Exact isolation covariance and variance; exhaustive n=5 moment check at p=0.23.'),
 dict(problem_id='H0021',claim='For fixed c>1 and k≥1, the minimum k-neighbor reservoir size is (1+o_P(1))n log log n/(c log n) in G(n,c log n/n).',status='proved',proof_location='ATTEMPT.md §3',remaining_gap='Local domination does not establish capacity, vertex-disjoint routing, or spanning tree completion. No novelty claim.',checks='Random-selection/alteration upper bound, all-subsets first-moment lower bound, explicit quantifier and dependence audit. Finite cardinality Lean verification pending.'),
 dict(problem_id='H0021',claim='A fixed independent reservoir of size (1+o(1))n log log n/(c log n) fails to dominate G(n,c log n/n) whp.',status='proved',proof_location='ATTEMPT.md §4',remaining_gap='Obstruction applies only to predetermined sets, not graph-adaptive sets.',checks='Exact Binomial(n−r,(1−p)^r) law; exhaustive n=5 moments.'),
 dict(problem_id='H0021',claim='At n=5, exactly 72 labeled graphs have a Hamilton path but are not universal for all maximum-degree-3 spanning trees.',status='proved_special_case',proof_location='experiment.py; experiment_results.json; ATTEMPT.md §6',remaining_gap='Finite deterministic examples give no asymptotic counterexample.',checks='Enumerated all 1024 graphs and all permutation image masks of the two subcubic tree isomorphism classes.'),
 dict(problem_id='H0021',claim='The reservoir repair construction satisfied its witness/cardinality postconditions in six eligible random trials with n=500,2000,8000.',status='numerical_evidence',proof_location='experiment.py; experiment_results.json',remaining_gap='Three additional trials failed the minimum-degree premise and were explicitly skipped; finite trials do not prove convergence.',checks='Fixed seed; sparse NetworkX generator; all outside vertices checked for two neighbors; union size checked; run under one second.'),
 dict(problem_id='H0021',claim='For every fixed ε>0 and integer Δ≥3, G(n,(1+ε)log n/n) is T_{n,Δ}-universal whp.',status='conjecture',proof_location='source_text.txt page 7; ATTEMPT.md §5',remaining_gap='No simultaneous spanning completion theorem was proved, already for Δ=3.',checks='Successful bounded literature searches found no exact matching theorem; two requested services remained rate limited.')
]
(base/'CLAIMS.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in claims),encoding='utf8')
print('Wrote LITERATURE.md and',len(claims),'claims.')
