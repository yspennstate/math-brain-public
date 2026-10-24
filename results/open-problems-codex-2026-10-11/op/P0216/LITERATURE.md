# Literature check — P0216 — 2026-10-11

No matching solution theorem was verified in this bounded search. This is not a certificate that no solution exists. All retrievals use Python urllib from the shell; no built-in web search was used. OpenAlex access failed throughout, so its citing-works search could not be completed.

## Primary source

David Aldous, “Largest common substructures in probabilistic combinatorics,” author-maintained open-problem page, https://www.stat.berkeley.edu/~aldous/Research/OP/substructures.html (fetched 2026-10-11; saved as aldous_page.raw).

The page links “in this section of the original 2003 document” to common_subs.pdf and “May 2001 draft notes” to substructures_posets.pdf. Its exact account is:

> Regarding the two-dimensional partial order problem described there, a brief correspondence with Graham Brightwell had resulted (May 2001) in me writing some May 2001 draft notes, but neither of us pursued it thereafter, according to memory and files.

The updates on the page concern cladograms and permutation subsequences, not a theorem solving this poset limit problem.

David Aldous, original 2003 open-problem document, Section 2, “Largest common substructures in probabilistic combinatorics,” excerpt https://www.stat.berkeley.edu/~aldous/Research/OP/common_subs.pdf, three PDF pages corresponding to printed pages 4–6; raw original.raw, text original.txt. The general setting on printed p.4 says, verbatim:

> Given two distinct instances S1, S2 of the same type of structure on [n], we can ask for each A ⊂ [n] whether the two induced substructures on A are identical

Example 4, printed p.5 (excerpt PDF p.2), says:

> Amongst several models for random partial orders [13], consider the random two-dimensional partial order on [n]. This is the partial order obtained by taking n points (xi, yi), 1 ≤ i ≤ n uniformly randomly in the unit square [0, 1]2 and using the induced “coordinatewise” partial order [29]. Here the natural conjecture is

> E C_n ∼ c n^(1/3), for some 0 < c < ∞. (2)

The displayed equation above is transcribed with normalized mathematical notation, rather than pretending the PDF text extractor preserved typography. Printed p.6 says:

> It is not hard (Graham Brightwell, personal communication) to prove an O(n^(1/3)) upper bound using the first moment method. But establishing a value for, or existence of, the presumed limit constant c in (2) may be genuinely hard.

David Aldous/Graham Brightwell, *A Problem concerning 2-Dimensional Random Posets: notes by Aldous/Brightwell*, May 2001 draft (date supplied by maintained page), https://www.stat.berkeley.edu/~aldous/Research/OP/substructures_posets.pdf, eight PDF pages; raw notes.raw, text notes.txt. Conjecture 1, p.1 asks both E X_n ∼ c_0 n^(1/3) and n^(-1/3)X_n -> c_0 in probability. It explicitly gives equivalent independent-permutation and independent-uniform-point descriptions. It outlines liminf >=0.728 and limsup <=3.85 on p.1; these are source claims with sketched derivations, not new fully refereed theorems in this attempt. Lower bound 1 is the sparse bipartite matching grid construction, pp.2–3. Lower bound 2 is a continuous noninterference construction, pp.3–4. Proposition 5, p.6, states p(m)<=(m+1)3^m/(m!)^2 for the probability of identical m-label orders. The proof is on p.7.

Crucial correction to intake: on p.2 the draft says “but we do not know any such argument to prove existence of a limit c0 in Conjecture 1, nor do we have any conjecture for the numerical value of c0.” The preceding sentence refers to the subadditive ergodic theorem for longest increasing subsequences. That argument cannot simply be transferred to this problem.

## Search audit

All queries dated 2026-10-11. Exact URLs, response status and byte counts are in search_log.json and followup_log.json; successful raw responses are retained.

* arXiv API: `all:"common" AND all:"partial orders"`, max_results=30. Successful (arxiv.raw); titles inspected separately.
* OpenAlex works search: `largest common random substructures`, per-page=20. HTTP 429; no results inspected.
* OpenAlex works search: `common random two dimensional partial orders`, per-page=20. HTTP 429; no results inspected.
* Crossref works: `largest common random substructures`, rows=20. Successful (crossref.raw); titles inspected separately.
* Semantic Scholar paper search: `largest common random substructures`, limit=20, title/authors/year/url/abstract/externalIds. HTTP 429; no results inspected.
* GitHub repository search: `common random partial orders`. Successful, total_count=0 (github.raw). Repository search is not a paper search.
* arXiv followup: `all:"common" AND (all:"posets" OR all:"two-dimensional partial")`, max_results=50. Successful; titles and the poset-metric abstract inspected. No matching theorem identified.
* Crossref followup: `common induced random partial orders`, rows=20. Successful; titles and relevant bibliographic records inspected.
* OpenAlex retry: `Aldous common substructures`, per_page=10. HTTP 429.
* Semantic Scholar retry: `common random posets`, limit=10. HTTP 429.
* Primary PDF requests: https://www.stat.berkeley.edu/~aldous/Research/OP/common_subs.pdf and https://www.stat.berkeley.edu/~aldous/Research/OP/substructures_posets.pdf.

* OpenAlex source-resolution attempt: `filter=title.search:Largest common substructures in probabilistic combinatorics`, per_page=5. HTTP 429. No source work identifier recovered, so `works?filter=cites:<source id>` traversal was not possible; this is a specific uncompleted literature check.
* Semantic Scholar source-URL citing-paper endpoint: `paper/URL:<common_subs.pdf>/citations`, fields title/year/authors, limit=100. HTTP 404; the source URL was not resolved.
* arXiv author/topic followup: `all:"Aldous" AND (all:"coincidence" OR all:"common partial" OR all:"common substructures")`, max_results=30. Successful, 13 entries, arxiv_aldous.raw; titles/authors/abstracts inspected and saved in arxiv_aldous_summary.json. Results concern spectral gaps, trees, endogeny, random graphs and other unrelated models; none states the P0216 limit theorem.

Rate-limited searches do not count as negative results. The initial arXiv request returned 30 entries and the poset followup returned 50; these are capped, relevance-ranked searches, not exhaustive scans.

## Related leads, not solutions of P0216

* Robert Nerem, Peter Crawford-Kahrl, Bree Cummins, Tomas Gedeon, *A poset metric from the directed maximum common edge subgraph*, arXiv:1910.14638, v2. Abstract retrieved in both arXiv searches: directed maximum common edge subgraphs and metrics allowing different underlying sets; not the same-label random-point coincidence limit. No matching theorem claimed.
* David J. Aldous, *On the Largest Common Subtree of Random Leaf-Labeled Binary Trees*, SIAM Journal on Discrete Mathematics (2022), DOI 10.1137/20M1347504; arXiv:2006.10545 as linked by the maintained page. Tree model, not posets.
* Graham Brightwell, *Models of random partial orders*, in *Surveys in Combinatorics, 1993*, DOI 10.1017/CBO9780511662089.004. Model background, predates the question.
* Béla Bollobás and Graham Brightwell, *Box-spaces and random partial orders*, Transactions of the American Mathematical Society (1991), DOI 10.1090/S0002-9947-1991-0986685-9 (also catalogued as 10.2307/2001495). Background on random orders; no inspected matching coincidence-limit theorem.
* B. Bollobás, *Random partial orders: concentration of the height*, Advances in Applied Probability (1992), DOI 10.1017/S0001867800024629. Height of one order differs from coincidence of two orders.
* Marcos Kiwi and Martin Loebl, *Largest planar matching in random bipartite graphs*, Random Structures & Algorithms (2002), DOI 10.1002/rsa.10048. A matching-related lead; no claim that a planar matching theorem supplies the full common-poset limit.

These exact author/title/DOI references were read from Crossref records. Except for the poset-metric abstract and the Aldous sources, full texts of these related leads were not retrieved or audited. They are not evidence of resolution.

## Read-only prior work

math_recall.py, query `common random partial orders grid matching`: returned the prior isolated-grid expectation and its e^-2 constant (claim_59ddb177177e875bbb75451fe62be96f319f637fc4a7ca95a4b159d9abfddf50, claim_cb0c04d9b8d1a70e87308a2a726bea01bd0328c5295f75e8b2f4770c4234f4de). It does not establish existence or optimality of the limit. ATTEMPT.md reproves and optimizes that construction independently.

brain.py recalls: `two dimensional partial orders mistakes` and `common random two dimensional partial orders`. Returned hints are not literature theorems. The first recall reported an automatic index-refresh attempt by the brain reader (spawn failed); no brain write command was requested.

An initial rg intake search used a Windows wildcard in a path argument and failed; a PowerShell-expanded directory search was then launched. Read-only git ls-tree origin/master was also launched to locate recorded answers. No working tree was modified.

The first prior_read.py pass found no P0216 rows at the direct ledger paths. Read-only git path filtering found one report with p0216 in its filename, saved as prior_git_0.txt: runs/R01/20260919T0424Z_successor_gate_p0219_owned_p0216_graphon_8_14_19_7d2e1c4a.md. Its context is a DIFFERENT graphon/Markov-chain campaign numbering, not this random-poset question; no theorem was imported from it. A recursive ledger-path pass was also run, with results retained in prior_records.json. The initial unfiltered shell path listing was excessively large; subsequent inspection was confined to selected records.

The recursive pass also found zero matching rows in the named problems.jsonl/attempts.jsonl/sources.jsonl paths available under these directory roots. It therefore contributes no independent historical result; the typed math-store cards above were the usable previous-attempt record.

During the attempt, math_recall.py query `self bounding Efron Stein variance certificate` returned the canonical Efron–Stein inequality (claim_86cf1e9337e554632973d7e667c68acea223b8cc18e958d4dd1752b1136526fa) and the reference B. Efron and C. Stein, *The jackknife estimate of variance* (1981), DOI 10.1214/aos/1176345462. This is a hint/reference, not an audited proof of P0216; the required variance inequality is proved from conditional expectations in ATTEMPT.md.

## Further attempt: neighboring graph-theoretic results, 2026-10-11

Brain queries: `Aldous Brightwell common random posets limit constant subadditivity balanced permutations` and `Gallai transitive orientations prime comparability graph modular decomposition simple permutations substitution decomposition`. The first returned the existing open-problem/grid cards and no resolution. The second returned largely unrelated cards, not the needed Gallai theorem. No brain hint was treated as a verdict.

New shell/Python searches, all successful, exact URLs and response sizes in modular_search_log.json:

* arXiv API: `all:"permutation graphs" AND all:"modular decomposition"`, max_results=20.
* arXiv API: `all:"simple permutations" AND all:"substitution decomposition"`, max_results=15.
* Crossref: `Gallai transitiv orientierbare Graphen`, rows=5.
* arXiv API: `all:"transitive orientations" AND all:"prime"`, max_results=15.

Those same four queries were repeated when read_modular.py imported the search module, and are counted as a second retrieval round. No additional query was concealed by this repetition; the raw responses and latest log are saved. The original main-problem citation-search limitations remain as recorded above.

PDFs retrieved and extracted (see modular_pdf_log.json):

1. Miriam Münch, Ignaz Rutter, Peter Stumpf, *Partial and Simultaneous Transitive Orientations via Modular Decompositions*, arXiv:2209.13175. PDF pp.4–5 are the structural inputs checked in CONTINUATION.md. The canonical-decomposition existence/type assertion is on p.4; the representation of **all** transitive orientations and the prime-quotient two-orientation assertion are on p.5, immediately before Lemma 2. Exact relevant quotations and the hypothesis-to-application check are written in CONTINUATION.md. This is not a P0216 solution paper.
2. Robert Brignall, Sean Mandrick, Vincent Vatter, *Chains and unique transitive orientations of prime graphs*, arXiv:2609.08057v1. Theorem 1.1, PDF p.2, with proof pp.3–4, independently verifies the prime-graph input. Exact theorem quote is in CONTINUATION.md. It does not concern the random-poset limit.
3. *The Homomorphism Poset of K_{2,n}*, arXiv:1008.1736v2. Retrieved as a permutation-graph lead (permutation_paper.raw/.txt); not needed for the final proof.
4. Ron M. Adin, Eli Bagno, Estrella Eisenberg, Shulamit Reches, Moriah Sigron, *On two-sided gamma-positivity for simple permutations*, arXiv:1711.06511v2. Retrieved as a substitution-decomposition lead (substitution_paper.raw/.txt). Not needed for the collision-rate/upper-bound proof; Proposition 5.3, PDF p.9, with s=t=1, cross-checks the auxiliary formal-series identity in CONTINUATION.md.

The underlying historical reference is Tibor Gallai, *Transitiv orientierbare Graphen*, Acta Mathematica Academiae Scientiarum Hungaricae 18 (1967), 25–66, particularly Satz 1.8, Item 5 for prime orientations. The 2026 paper identifies that exact locator. A translation is F. Maffray and M. Preissmann, *A translation of Gallai's paper: “Transitiv orientierbare Graphen”*, in *Perfect Graphs*, eds. J. L. Ramírez Alfonsín and B. A. Reed, Wiley (2001), pp.25–66, Theorem 3.1.8, Item 5. These historical originals were not fetched; the retrieved explicit restatement and proof above supply the checked input.

This continuation proves a collision-rate subproblem by applying these neighboring theorems and doing the counting argument. It does not justify VERDICT: SOLVED_IN_LITERATURE for the full random-poset question. No novelty or current best-known-bound claim is made.
