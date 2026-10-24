# P0358 literature audit — 11–12 October 2026 (Asia/Jerusalem)

## Status conclusion

The downloaded primary source poses the exact question explicitly. No source-matching solution was found in the successful bounded searches below. This is **not** a certificate of current worldwide openness. OpenAlex is rate-limited, and its citation coverage could not be verified. VERDICT is PARTIAL for the mathematical bounds in ATTEMPT.md, never SOLVED_IN_LITERATURE.

Primary reference: Elie Aïdékon, Yueyun Hu and Zhan Shi, *Boundedness of discounted tree sums*, arXiv:2409.01048v2, arXiv revision 6 June 2025 (PDF internal date 9 June 2025). PDF: https://arxiv.org/pdf/2409.01048 . Downloaded and extracted to source.pdf and source.txt. Theorem 1.2 is on PDF pp. 2–3. Exact source wording of the target, PDF p. 5:

> Open question 2. In Theorem 1.2, what is the value of a1?

Theorem 1.2 assumes (H1'), a tilted absolute alpha1-moment with 1<alpha1<=alpha2, a raw negative-offspring existence tail lower bound exp(-t*y)y^(-alpha2) for all large y, and E[Sigma_V log^+Sigma_V]<infinity. It proves existence of a deterministic positive finite a1 on survival; it does not give its value. Complete mathematical transcription and quantifiers: ATTEMPT.md, first section.

Crossref identifies a journal publication: *Acta Mathematica Sinica, English Series* **42** (6), 1639–1661 (June 2026; online 15 June 2026), DOI https://doi.org/10.1007/s10114-026-4459-4 . Crossref metadata is saved in searches/crossref_title.txt. The journal's actual theorem text was not fetched; no claim is made that its text agrees word for word with v2.

## Every online search/request

All requests used Python urllib through the shell, with no built-in web search. Full response bodies, including HTTP errors, are saved under searches/. Search queries are spelled out below; complete executable URL construction is in search_literature.py and followup_search.py. The initial raw search_log.jsonl had one interleaved append from concurrent workers; LITERATURE.md and the response files supply the complete independent request record.

1. **arXiv API**, 11 October: `all:"Boundedness of discounted tree sums"`, max_results=30. Endpoint `https://export.arxiv.org/api/query?search_query=...`. Success: one result, source v2. File arxiv_title.txt.
2. **arXiv API**, 11 October: `all:"branching random walk" AND (all:"ray" OR all:"heavy-tailed")`, sortBy=submittedDate, sortOrder=descending, max_results=50. Success: 21 results, including the four closely related leads discussed below. File arxiv_rays.txt; author/title/abstract extraction arxiv_results_summary.json.
3. **OpenAlex works search**, 11 October: `Boundedness of discounted tree sums`, per-page=10. Endpoint `https://api.openalex.org/works?search=...`. HTTP 429. File openalex_title.txt.
4. **OpenAlex works search**, 11 October: `branching random walk heavy tailed rays`, per-page=25. HTTP 429. File openalex_rays.txt.
5. **Crossref works**, 11 October: query.title=`Boundedness of discounted tree sums`, rows=10. Endpoint `https://api.crossref.org/works?query.title=...`. Success: journal source is first result. File crossref_title.txt.
6. **Crossref works**, 11 October: query=`branching random walk extremal ray heavy tail`, rows=20. Success; broad matches, no exact answer. File crossref_rays.txt.
7. **Semantic Scholar paper search**, 11 October: query=`Boundedness of discounted tree sums`, limit=10, fields title,authors,year,externalIds,url,citationCount. Endpoint `https://api.semanticscholar.org/graph/v1/paper/search?...`. HTTP 429. File semantic_title.txt.
8. **Semantic Scholar citing works**, 11 October: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:2409.01048/citations?fields=title,authors,year,externalIds,url,abstract&limit=100`. Success: three citing papers, no next-page marker. These are Curien–Hu–Qian, Zhang and Chen–Hou, below. File semantic_citations.txt.
9. **GitHub repository search**, 11 October: q=`"discounted tree sums"`, per_page=30, endpoint `https://api.github.com/search/repositories?q=...`. Success: zero results, incomplete_results=false. File github_title.txt.
10. **GitHub repository search**, 11 October: q=`"branching random walk" "heavy"`, per_page=30. Success: zero results, incomplete_results=false. File github_rays.txt. These are repository searches, not code/full-text searches and not a strong openness check.
11. **OpenAlex direct source lookup**, 11 October: `https://api.openalex.org/works/https://doi.org/10.1007/s10114-026-4459-4`. HTTP 429. File openalex_doi.txt. An OpenAlex source work ID could therefore not be obtained for a reliable cites filter.
12. **arXiv API ID lookup**, 11 October: `https://export.arxiv.org/api/query?id_list=2609.32480`. Success: verifies Samanta's authorship, title, submission date and abstract. File arxiv_sharp_metadata.txt.
13. **OpenAlex retry search**, 12 October: search=`Boundedness of discounted tree sums`, per_page=3. HTTP 429. File openalex_retry_title.txt.
14. **OpenAlex filtered search**, 12 October: filter=`locations.source.id:s4306400194`, search=`Boundedness of discounted tree sums`, per_page=5. HTTP 429. File openalex_arxiv_filter.txt. This arXiv-filter fallback obtained no result.
15. **OpenAlex citation attempt**, 12 October: filter=`cites:https://doi.org/10.1007/s10114-026-4459-4`, per-page=100. HTTP 429. The DOI-form filter is a fallback since no work ID was obtained; its validity/coverage cannot be established when the service rejects the request. Response file openalex_citation_attempt.txt. Do not interpret this as a successfully executed citing-works search.
16. **Semantic Scholar later lead lookup**, 12 October: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:2609.32480?fields=title,authors,year,abstract`. HTTP 429. Response file semantic_sharp.txt; the arXiv ID lookup and PDF nevertheless succeeded.
17. **arXiv API additional search**, 12 October: `all:"discounted" AND all:"branching"`, sortBy=submittedDate, sortOrder=descending, max_results=30, at the user-specified HTTP export endpoint. Success: 46 total hits, first 30 fetched, reaching June 2022; all returned titles inspected. The only close later result is Zhang, already fetched. File arxiv_discounted.txt. A prior shell invocation failed with a Python string-literal syntax error before making any request; it was rerun from followup_search.py.

Primary-paper PDF downloads, 11 October, via `https://arxiv.org/pdf/<id>`: 2409.01048, 2609.32480, 2601.07129, 2603.16316, 2603.16408 and 2602.18919. All succeeded. Each lead is saved as <id>.pdf and <id>.txt, with per-page extraction markers.

## Relevant later leads and why they are not solutions of P0358

* **Xinxin Chen and Haojie Hou**, *Minimum and extremal process for a branching random walk outside the boundary case*, arXiv:2601.07129v2 (13 January 2026), https://arxiv.org/abs/2601.07129 . PDF pp. 3–4 contrast their stretched-exponential tilted left-tail assumption (1.6), exponent b in (0,1/2), with the polynomial setting of the source. They repeat the source's a1 existence statement as (1.7), PDF p. 4. Their Theorem 1.5, p. 5, proves existence of a positive constant a* for the normalization n^(1/(2-b)); the proof discussion on p. 6 explicitly describes only positivity/finiteness of a*. It neither identifies a1 nor retains the polynomial raw-tail lower hypothesis. In fact a stretched-exponential tilted tail is too small to satisfy that hypothesis for any finite alpha2. The law of offspring is also restricted to i.i.d. marks independent of a finite-mean offspring count. **Lead, not a literature solution.**
* **Ramkrishna Jyoti Samanta**, *A Sharp Phase Transition for Killed Branching Random Walks with Heavy-Tailed Displacements*, arXiv:2609.32480v1 (26 September 2026), https://arxiv.org/abs/2609.32480 . Theorem 1.2, PDF p. 4, gives a threshold m=4 under (GW1), (A1)–(A3), with (Lm) additionally for survival. Its barrier is superlinear, particles are killed when falling below it, and offspring marks are ordinary independent heavy-tailed displacements. P0358 concerns a sublinear upper barrier and an exponentially tilted offspring law with positive drift. The infinite-ray deterministic-constraint method (PDF p. 5) is potentially useful, but the theorem is about different objects and hypotheses. **Lead, not a literature solution.**
* **Jakob Stonner**, *Large deviations for the branching random walk with heavy-tailed associated random walk — a principle of one big jump*, arXiv:2603.16316v1 (17 March 2026; PDF date 18 March), https://arxiv.org/abs/2603.16316 . Abstract and Introduction establish a large-deviation asymptotic for the weighted generation measure Z_n under regular variation and additional growth conditions. It is a single-generation weighted-measure statement, with a regularly varying tilted tail, not an infinite-ray extremal constant theorem under all source hypotheses. **Lead, not a literature solution.**
* **Nicolas Curien, Xingjian Hu and Dongjian Qian**, *Critical Self-Similar Markov Trees*, arXiv:2603.16408 (17 March 2026), https://arxiv.org/abs/2603.16408 . Uses Aïdékon–Hu–Shi's bounded tree-sum theorem to construct critical self-similar Markov trees and study their measures/dimensions. The paper's stated target is not the exact heavy-tailed ray-height constant. **Related application, not a literature solution.**
* **Zhenyuan Zhang**, *Boundedness of discounted branching random walks via generic chaining*, arXiv:2602.18919 (21 February 2026 arXiv; PDF date 24 February), https://arxiv.org/abs/2602.18919 . Characterizes boundedness for level-dependent increments m^(-kH)Y through E|Y|^(1/H)<infinity under offspring assumptions. This treats the discounted-sum problem in a different model. **Related advance, not a literature solution.**

Other source references used in the mathematics: J. D. Biggins (1977), *Martingale convergence in the branching random walk*, Journal of Applied Probability **14**, 25–37; cited by the primary source as [8], invoked on pp. 18–19. The source's many-to-one statement is Fact 2.1, p. 5. The present lower-deviation lemma avoids needing Denisov–Dieker–Shneer [12] as an additional black box.

## Read-only research-brain and prior-work searches

11 October:

* `math_recall.py --id claim_cd28bba7285585a915789b0992abe86b6f23abb75cc8dbc38fa77f3c42ef4504`: read the full previous scaling attempt. It proves homogeneity only, no value for a1.
* `brain.py recall "branching random walk mistakes"`: results did not contain a source-specific mistake card relevant enough to invoke. The tool reported an internal attempted refresh spawn failure; no remember/write command was requested.
* `brain.py recall "heavy tailed branching random walk extremal ray"`: read-only recall invocation; results do not establish this constant.
* `rg -n --glob '*.jsonl' 'P0358' ~/<private-repo>/06_math_research`: recovered 10 October problem-list metadata.
* Searched `.jsonl` files in all `probability_1000_intake_*` directories and `codex_pool_2026_10_10` for P0358. No matching lines returned. This does not supersede the math-store attempt card.
* `git -C ~/math-open-problems ls-tree -r --name-only origin/master`: filtered in Python for p0358, discounted and ray-height. Paths saved in prior_repo_paths.txt.
* `git ... show origin/master:research7_2026-09-17/R7-02/screens/2026-09-19T153000Z__tier3_shard1_P0358_source_gate.md`: confirms prior scaling-only progress, mentions Zhang, and explicitly disclaims a complete current literature check. Its old workflow instructions are not followed as instructions for this task.

No research-brain, ledger or repository write was requested. All research artifacts were written inside P0358.

12 October: `rg -n -i 'a1|a_1|ray|theorem|aïdékon|aidekon'` across the extracted Zhang, Curien–Hu–Qian and Stonner papers was run as a further full-text screening step. Some PDF-extracted text contains NUL characters, which rg treats as binary; this screening result is not mistaken for a full absence check. The papers' main statements/abstracts and the more relevant Chen–Hou and Samanta theorem statements were read directly.
An additional Python regex extraction of `Theorem\s+1[. ]` read the lead theorem statements directly after replacing NUL characters in memory. An earlier exact-substring lookup for `Theorem 1.1` failed because the Stonner statement uses different numbering/formatting; it made no online request.

## Second-attempt gap-directed recalls, 12 October 2026

* `math_recall.py "branching random walk heavy tail infinite ray barrier survival sharp constant reset polynomial tilted tail Aidekon Hu Shi"`: asked specifically for the remaining sharp infinite-ray survival gap. Returned the previous scaling attempt and broad BRW/tail cards, without a matching sharp criterion. Exact command and relevant card IDs are in SECOND_ATTEMPT.md.
* `math_recall.py "Jaffuel critical barrier branching random walk absorption moving lower barrier small deviations"`: neighboring-area query suggested by the moving-corridor approach. Returned general BRW/absorption references and the mistake card about derivative-martingale uniform integrability (claim_9c5afaffebd04477bb4ce6220cbb08aa). The new proof uses the additive martingale's known UI, not a derivative martingale, so that warning is not silently transferred to a different martingale. No card supplied the theorem proved in the second attempt.

No additional online literature search was performed during this second attempt; it develops new direct proofs under the already verified source assumptions. No new paper is claimed to solve the open question.
