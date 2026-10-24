# C0021 literature and status check — 2026-10-12

No checked paper found that states and proves the requested asymptotic exponent. This is a bounded search with access failures, not a certificate of worldwide openness. VERDICT is not SOLVED_IN_LITERATURE.

## Exact source and hypotheses

Christophe Garban and Jeffrey E. Steif, *Noise sensitivity of Boolean functions and percolation*, arXiv:1102.5761. Downloaded https://arxiv.org/pdf/1102.5761 to source.pdf and extracted source.txt. Exercise VIII.5 is on **PDF page 97, printed page 95**:

> Exercise VIII.5. What can you say about the sequence of revealments for the Iterated 3-Majority function? [It can be shown that the sequence of revealments decays like 1/n^σ for some σ but it is an open question what σ is.]

The superscript was linearized here; the words are those of the PDF. Definition VIII.1, printed page 84, defines δ_A=max_i P(i∈J_A), and δ_f=inf_A δ_A. Printed page 83 defines an algorithm as querying bits singly and stopping once the output is determined for every completion. Randomness of the algorithm is independent of the input. The ambient measure is uniform on {−1,1}^n. Example 4 defines majority on a depth-k ternary tree with n=3^k leaves. This is **zero error under iid fair bits**, with unrestricted adaptive interleaving; not worst-case expected cost or parity queries.

Theorem VIII.6, printed pages 89–90: monotone f has C(f)≥I(f)^2 and δ_f≥I(f)^2/n. Theorem VIII.7 is weaker for this specific problem. The source itself therefore supplies the 0.2618595 upper bound on σ after computing the influence.

## Relevant primary sources

* Julia Jansson and Patrik Jansson, *Level-p-complexity of Boolean Functions using Thinning, Memoization, and Polynomials*, arXiv:2302.02473v4, 2 November 2023; downloaded from https://arxiv.org/pdf/2302.02473. Pages 19–20 give the exact two-level complexity polynomial P*. The coefficients in increasing order are [4,4,6,9,−61,23,67,−64,16]. At p=1/2 this is 393/64. Page 20 says: “The conjecture in (Jansson, 2022) is thus false and the correct formula for the level-p-complexity of maj²₃ is P*.” This proves a finite special case; it does not compute the requested asymptotic exponent.
* Frédéric Magniez, Ashwin Nayak, Miklós Santha, Jonah Sherman, Gábor Tardos, and David Xiao, *Improved bounds for the randomized decision tree complexity of recursive majority*, arXiv:1309.7565; *Random Structures & Algorithms* (2016), DOI 10.1002/rsa.20598. Downloaded https://arxiv.org/pdf/1309.7565. Lower base 2.57143 and zero-error upper base 2.64944 concern **worst-case randomized query complexity**. The hard-distribution lower bound cannot simply be applied to fixed uniform input. Lead, not a solution to C0021.
* Nikos Leonardos, *An Improved Lower Bound for the Randomized Decision Tree Complexity of Recursive Majority*, ICALP 2013, DOI 10.1007/978-3-642-39206-1_59. Crossref recovered the reference. Worst-case model, not a verified solution here.
* O'Donnell and Servedio, the monotone expected-query lower bound cited as [OS07] by the source. Used through the fully checked source theorem, whose proof is reproduced in ATTEMPT.md.

## Read-only brain and prior-work recovery

Commands used: math_recall.py "iterated majority randomized decision tree query complexity"; math_recall.py --id claim_1f15162755e516e55609d34405c2da7b0fc126d2c2cfb76352aaab5f77a7a1dd; brain.py recall "iterated majority mistakes"; brain.py recall "Revealment exponent of the iterated 3-majority function"; brain.py node compaction_claude_e63c4483_20261011T004947. The last memory is mainly off topic. Intake records were searched for C0021 with rg. No brain or repository was modified.

Read origin/master with git show in ~/math-open-problems: operations/claims/C0021.md; prob1000_lean_20260908/ultracode_20260909/C0021/{memo.md,dp_exact.py,policy_heur2.py,policy_heur2_K5.log}; and P13 C0021 checkers/reports under proofnet24/P13-outside-successor. The earlier memo already gives the reduction δ_k=D_k/3^k, exponent existence, D_3, and a depth-four upper policy. Later P13 reports record a stronger bound σ≥0.1784023402720471 through patched depth-four policies. These are internal research claims, not papers solving the problem. They must not be mistaken for new results of this run or promoted without checking the policy.

## Search ledger

Every request, including failures, is logged with full URL and date in search_log.json, search_more_log.json, and search_final_log.json. These are authoritative request logs; scripts search.py, fetch_more.py and fetch_final.py reproduce the requests. All accesses use Python urllib from the shell. No built-in web search was used.

Initial search queries (2026-10-12):

* arXiv API: all:"recursive majority" OR all:"iterated majority", 40 results. Relevant: Magniez et al.; Jansson–Jansson. Other hits concern noise thresholds, sketches and parity decision trees, different questions.
* OpenAlex works search: recursive majority randomized query complexity; source title Noise sensitivity of Boolean functions and percolation. Both HTTP 429.
* Crossref works query: recursive majority randomized decision tree, 20 results. Relevant references listed above.
* Semantic Scholar paper search: recursive majority, limit 30 with abstracts. HTTP 429.
* GitHub repositories: recursive majority. Relevant leads: zpotthoff/Recursive-Majority and tulasimohan/rec-maj-visualizer, followed by README requests. Repositories alone are not a proof in print.

Follow-up requests (2026-10-12):

* arXiv API: all:revealment AND (all:majority OR all:recursive), max_results 40. Returned noisy unrelated hits; no relevant theorem found. Followed with a title-focused query logged in search_final_log.json.
* OpenAlex works search: iterated majority revealment; work lookup by arXiv URL. HTTP 429.
* Semantic Scholar source-paper lookup with citation titles, years and external identifiers. HTTP 429.
* OpenAlex source DOI lookup and a citing-works request are logged in search_final_log.json. A DOI must first resolve to an OpenAlex work ID for a successful cites filter; if lookup fails, a complete citing-works search is unavailable and is not claimed completed.

Further results and their relevance are appended below after inspection.

Bibliographic detail confirmed by Crossref: Magniez et al., *Random Structures & Algorithms* 48(3) (2016), 612–638, first published online 8 July 2015; Leonardos, ICALP 2013, pp.696–708. Jacka, Warren and Windridge, *Minimizing the time to a decision*, *Annals of Applied Probability* 21(5) (2011), 1795–1826, DOI 10.1214/10-AAP737, arXiv:0911.5413v3.

The Jacka–Warren–Windridge PDF was fetched and read (jacka.txt). PDF/reprint page 2 explicitly states that the same discrete uniform expected-cost growth constant exists by subadditivity, records 9/4≤γ≤2.471, and cautions: “However, we caution that the results we present here do not shed light on the value of γ.” Theorem 1.1, same page, solves a three-diffusion control problem. It does **not** solve C0021. This independently confirms that the diffusion analogy cannot be imported as a solution. No proof of a 2.28 lower base was found in this fetched version; any such internal-memory hint remains unverified.

### Further inspected results

Jansson–Jansson's exact journal reference: *Journal of Functional Programming* (2023), DOI 10.1017/S0956796823000102, recovered from Crossref.

Xia Zong, Tuomo Lehtonen, and Jussi Rintanen, *Cost-Optimal Decision Diagrams for Stochastic Boolean Function Evaluation*, arXiv:2606.24672v1, 23 June 2026. Downloaded and text inspected: general branch-and-bound optimization, #P-hardness and PSPACE containment. No recursive-majority revealment exponent theorem appears.

GitHub tulasimohan/rec-maj-visualizer README gives depth-one cost 2.6667 and depth-three cost 18.6923. These are different from the fair-input costs 2.5 and 15.064288. The numerical claims are therefore not applicable to the object here; no exponent proof appears in the README. zpotthoff/Recursive-Majority README request returned 404.

The focused arXiv title-majority query returned 100 entries, with no inspected title/abstract containing recursive majority, iterated majority or revealment; it was noisy and is not a comprehensive negative result. The subsequent exact phrase iterated majority query returned Jansson–Jansson and a threshold-window paper, plus irrelevant iterative-majorization hits. No source-matching theorem found.

Additional searches, all 2026-10-12: arXiv au:Jacka AND au:Windridge; Crossref Jacka Warren Windridge Boolean expected cost; arXiv all:"iterated majority". Full requests/statuses in search_jacka_log.json. Found Saul Jacka, Jon Warren and Peter Windridge, *Minimizing the time to a decision*, arXiv:0911.5413v3. Direct PDF request is separately logged in search_jacka_pdf_log.json. The diffusion-control model is a lead, not automatically the discrete query model.

### Complete request list

* 2026-10-12 | openalex_citing | `https://api.openalex.org/works?filter=cites%3Adoi%3A10.1017%2FCBO9781139020299&per-page=100` | <HTTPError 429: 'Too Many Requests'>
* 2026-10-12 | openalex_doi | `https://api.openalex.org/works/https://doi.org/10.1017/CBO9781139020299` | <HTTPError 429: 'Too Many Requests'>
* 2026-10-12 | arxiv_narrow | `https://export.arxiv.org/api/query?search_query=ti%3A%22majority%22+AND+%28all%3A%22query%22+OR+all%3A%22revealment%22%29&max_results=100&sortBy=submittedDate&sortOrder=descending` | OK 260787 bytes
* 2026-10-12 | stochastic | `https://arxiv.org/pdf/2606.24672` | OK 480323 bytes
* 2026-10-12 | github_visualizer | `https://api.github.com/repos/tulasimohan/rec-maj-visualizer/readme` | OK 2738 bytes
* 2026-10-12 | github_recursive | `https://api.github.com/repos/zpotthoff/Recursive-Majority/readme` | <HTTPError 404: 'Not Found'>
* 2026-10-12 | crossref_levelp | `https://api.crossref.org/works?query.title=Level-p-complexity+of+Boolean+Functions+using+Thinning+Memoization+and+Polynomials&rows=3` | OK 14140 bytes
* 2026-10-12 | arxiv_jacka | `https://export.arxiv.org/api/query?search_query=au%3AJacka+AND+au%3AWindridge&max_results=15` | OK 2433 bytes
* 2026-10-12 | crossref_jacka | `https://api.crossref.org/works?query=Jacka+Warren+Windridge+Boolean+expected+cost&rows=5` | OK 30303 bytes
* 2026-10-12 | arxiv_uniform | `https://export.arxiv.org/api/query?search_query=all%3A%22iterated+majority%22&max_results=50` | OK 19244 bytes
* 2026-10-12 | jacka | `https://arxiv.org/pdf/0911.5413` | OK 342541 bytes
* 2026-10-12 | source | `https://arxiv.org/pdf/1102.5761` | OK 1522266 bytes
* 2026-10-12 | arxiv | `https://export.arxiv.org/api/query?search_query=all%3A%22recursive+majority%22+OR+all%3A%22iterated+majority%22&max_results=40` | OK 37546 bytes
* 2026-10-12 | openalex | `https://api.openalex.org/works?search=recursive+majority+randomized+query+complexity&per-page=30` | <HTTPError 429: 'Too Many Requests'>
* 2026-10-12 | openalex_source | `https://api.openalex.org/works?search=Noise+sensitivity+of+Boolean+functions+and+percolation&per-page=5` | <HTTPError 429: 'Too Many Requests'>
* 2026-10-12 | crossref | `https://api.crossref.org/works?query=recursive+majority+randomized+decision+tree&rows=20` | OK 104758 bytes
* 2026-10-12 | semantic | `https://api.semanticscholar.org/graph/v1/paper/search?query=recursive+majority&limit=30&fields=title%2Cauthors%2Cyear%2Curl%2Cabstract` | <HTTPError 429: ''>
* 2026-10-12 | github | `https://api.github.com/search/repositories?q=recursive+majority` | OK 105382 bytes
* 2026-10-12 | levelp | `https://arxiv.org/pdf/2302.02473` | OK 733879 bytes
* 2026-10-12 | worstcase | `https://arxiv.org/pdf/1309.7565` | OK 1365755 bytes
* 2026-10-12 | arxiv_revealment | `https://export.arxiv.org/api/query?search_query=all%3Arevealment+AND+%28all%3Amajority+OR+all%3Arecursive%29&max_results=40` | OK 86106 bytes
* 2026-10-12 | openalex_retry | `https://api.openalex.org/works?search=iterated+majority+revealment&per_page=15` | <HTTPError 429: 'Too Many Requests'>
* 2026-10-12 | openalex_arxiv | `https://api.openalex.org/works/https://arxiv.org/abs/1102.5761` | <HTTPError 429: 'Too Many Requests'>
* 2026-10-12 | semantic_retry | `https://api.semanticscholar.org/graph/v1/paper/ARXIV:1102.5761?fields=title,citations.title,citations.year,citations.externalIds` | <HTTPError 429: ''>

Exact source bibliography for the lower-cost theorem: Ryan O’Donnell and Rocco A. Servedio, *Learning monotone decision trees in polynomial time*, SIAM Journal on Computing 37(3) (2007), 827–844. The source also lists Ryan O’Donnell, Michael Saks, Oded Schramm and Rocco Servedio, *Every decision tree has an influential variable*, FOCS 2005, for the weaker OSSS bound.

The archived P52 policy was replayed successfully here; see prior_policy_verified.json and the mathematical prescription in ATTEMPT.md. Its sigma lower endpoint is 0.1784023402720471…, with upper endpoint 0.2618595071429149…. This is an internal checked bound, not a published determination of the exponent.

Final read-only intake traversal (2026-10-12): Python pathlib glob probability_1000_intake_*; searched problems.jsonl, attempts.jsonl, sources.jsonl for C0021; 17 files, 2 matched lines, saved in prior_intake_excerpt.txt.

## Further-attempt brain retrieval (2026-10-12)

Read-only math_recall.py query: uniform expected query complexity interleaving lower bound recursive majority Bellman dual potential. It returned no matching lower-base theorem; the revealment-average warning card (claim_baea3babc8c8e718c778c89c62b1bf3793c9c3b3a7e39ff98a401521056419b1) was relevant to scope. The earlier transitive symmetrization handles that warning.

Read-only query: Kantorovich Rubinstein Strassen monotone coupling. Relevant cards: real-valued Strassen theorem claim_d4ceae7714f94e59a9363adaaf91efab; Volker Strassen, The existence of probability measures with given marginals (1965), DOI 10.1214/aoms/1177700153; transportation-information-method card claim_6cf8db94742bfe4c0ccb7b3aae8c1a950deb1695f62f5d66ceb91e1a96d3e961. These were hints only. No multivariate theorem was imported from the real-valued card; the cube bijection and covariance proof are explicit. Full recall saved in brain_transport_recall.txt.

The already-fetched Jacka-Warren-Windridge paper motivated a discrete posterior-median policy; SECOND_ATTEMPT.md now proves its naive recursive translation suboptimal at depth three even with optimal adaptive ties. This does not contradict their diffusion theorem. No new solution-in-literature claim is made.
