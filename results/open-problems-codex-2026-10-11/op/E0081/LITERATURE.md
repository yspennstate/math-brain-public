# Literature and status check — E0081

Date: 12 October 2026. Retrieval used Python urllib from the shell, not a built-in web search. Raw successful responses, downloaded PDFs and extracted texts remain in this folder.

## Confirmed source

Jim Pitman and Wenpin Tang, **Patterns in Random Walks and Brownian Motion**, in *In Memoriam Marc Yor – Séminaire de Probabilités XLVII*, Lecture Notes in Mathematics 2137, Springer, 2015, pp. 49–88. DOI: 10.1007/978-3-319-18585-9_4. arXiv:1411.0041v3, posted 10 September 2015, manuscript dated 11 September 2015. Download: https://arxiv.org/pdf/1411.0041 (732611 bytes), saved as source.pdf/source.txt.

Question 1.7, printed/PDF page 5, verbatim (mathematical typography normalized):

> Given for each n a collection A_n of patterns of length n, what is the order of the expected waiting time ET(A_n) until some element of A_n is observed in a random walk?

The preceding paragraph specifies **simple symmetric random walks of length n with increments ±1 starting at 0**. No regularity, closure, monotonicity or cardinality hypothesis is imposed on A_n. Theorem 1.8, page 6, handles special families: excursions have mean of order n^(3/2), positive walks and bridges have order n, and the displayed bounds for fixed-negative-level first-passage walks are c n and C n^(5/4). Theorem 2.1, page 7, already gives an exact matching-matrix formula for any fixed finite collection. This is not a later solution to the asymptotic research program.

## Relevant papers and leads

1. Min-Zhi Zhao, Dong Xu and Hui-Zeng Zhang, **Waiting times and stopping probabilities for patterns in Markov chains**, arXiv:1602.06512v2 (2016/2017 version). PDF downloaded and inspected; its Theorem 2.1 is a generating-function linear system for a finite collection in a Markov chain. It does not give the asymptotic order for every scale-indexed collection in Question 1.7. Lead only.
2. Yuuya Yoshida, **A simple proof of the formula of Solov'ev–Nielsen–Blom for the expected waiting time**, arXiv:2410.13426v1 (2024). PDF downloaded and inspected. Theorem 1.1 is explicitly for one finite word. Useful for singleton/run means; not a solution for arbitrary families.
3. Søren Riis and Mike Paterson, **Coin flipping and waiting times paradoxes: Why fair coins are exceptional**, arXiv:2601.16580v2 (2026). PDF downloaded and inspected. Theorems 1 and 2 concern stochastic ordering and independent two-player string races; Theorem 5 gives a single-pattern generating function. Distinct model/quantifiers, not a solution to Question 1.7.
4. Urszula Ostaszewska and Krzysztof Zajkowski, **On the waiting time till some patterns occur in i.i.d. sequences**, arXiv:1302.4859v1 (2013). Abstract inspected in the arXiv response: solutions of the Guibas–Odlyzko finite linear system. Predates the source; lead only.
5. Krzysztof Zajkowski, **A note on the gambling team method**, arXiv:1310.4316v2 (2013). Abstract inspected: fixed-collection generating-function system with known initial outcomes. Predates the source; lead only.
6. Jungtaek Oh, **On distribution of runs and patterns in four state trials**, arXiv:2211.00774v2 (2022). Abstract inspected: run-length and waiting-time distributions for four-state trials. No full-scope solution identified in the abstract; full theorem audit not performed.
7. M. V. Koutras and F. S. Milienos, **Exact and asymptotic results for pattern waiting times**, *Journal of Statistical Planning and Inference* 142(6) (2012), 1464–1479. DOI: 10.1016/j.jspi.2011.12.028. Crossref bibliographic record fetched. Predates the source; full text not obtained, so no claim about its theorems. Potential classical-background lead.

The run mean used in ATTEMPT.md is classical. The new record gives independent complete proofs; it does not assert originality of the sharp extremal bounds.

Classical references read from the source bibliography: Stephen Breen, Michael S. Waterman and Ning Zhang, **Renewal theory for several patterns**, *Journal of Applied Probability* 22(1) (1985), 228–234, DOI 10.2307/3213763; Leo J. Guibas and Andrew M. Odlyzko, **String overlaps, pattern matching, and nontransitive games**, *Journal of Combinatorial Theory, Series A* 30(2) (1981), 183–208; Shuo-Yen Robert Li, **A martingale approach to the study of occurrence of sequence patterns in repeated experiments**, *Annals of Probability* 8(6) (1980), 1171–1176. These are prior finite-pattern methods, not later resolutions of Question 1.7.

## Search coverage and limitations

The arXiv math.PR search returned 20 entries, including the source, fixed-pattern papers above and unrelated queueing/scaling papers. Their titles and abstracts were reviewed; three later plausible papers were fetched in full. A broader recent-first arXiv search returned mostly unrelated transport and queueing applications, prompting the targeted search. Crossref returned the source DOI and related bibliographic records. No inspected theorem states and proves Question 1.7 with the same objects, hypotheses and quantifiers.

OpenAlex source search and DOI resolution returned HTTP 429, so a valid OpenAlex work ID could not be obtained for the normal cites:<work-id> query. A DOI-form citation-filter attempt also returned 429; that attempt is **not** counted as a successful citing-works search, and its filter syntax was not validated. Semantic Scholar's source-record/citations request and search returned HTTP 429. GitHub repository search returned HTTP 403 rate-limit exceeded. These failures prevent an exhaustive citation check. The correct status is **no verified full-scope solution found in this bounded search**, not a definitive assertion that none exists.

No SOLVED_IN_LITERATURE verdict is warranted. There is no purported resolving theorem to quote or line-by-line reduction to provide.

## Read-only brain and earlier work

Executed math_recall.py with “Pitman Tang pattern matching matrix waiting time”; it returned mostly off-target cards (including a permutation-pattern inequality paper). Executed brain.py recall with “pattern waiting time mistakes” and “Pitman Tang random walk patterns”; neither returned a directly relevant research result. The recall script reported an automatic index-refresh side effect; no remember/write command was requested, and it was not invoked again after the recalls. The prescribed scripts were treated only as hints.

Searched intake and pool JSONL records for E0081. Found E0081-A001 and neighboring E0082-A001 in probability_1000_intake_E_20260908. Their finite correlation-system lead is classical, but the claimed excursion density discrepancy is erroneous and the autocorrelation-only race identity omits cross correlations. ATTEMPT.md explains the corrections. Listed origin/master paths in ~/math-open-problems read-only, then filtered for E0081/Pitman: no relevant answer path found. No repository working tree was changed.

## Every network query/download recorded

The source download above preceded the structured log. Subsequent queries are listed below exactly, with their outcome. All dates are 2026-10-12.

- **openalex_patterns** — `https://api.openalex.org/works?search=Pitman+Tang+patterns+waiting+time&per-page=30` — HTTP Error 429: Too Many Requests; date 2026-10-12.
- **openalex_source** — `https://api.openalex.org/works?search=Patterns+in+random+walks+and+Brownian+motion&per-page=10` — HTTP Error 429: Too Many Requests; date 2026-10-12.
- **github** — `https://api.github.com/search/repositories?q=%22Pitman%22+%22Tang%22+patterns&per_page=20` — HTTP Error 403: rate limit exceeded; date 2026-10-12.
- **semantic_scholar** — `https://api.semanticscholar.org/graph/v1/paper/ARXIV:1411.0041?fields=title,authors,year,externalIds,citations.title,citations.year,citations.externalIds` — HTTP Error 429: ; date 2026-10-12.
- **arxiv** — `http://export.arxiv.org/api/query?search_query=all%3A%22patterns+in+random+walks%22&max_results=30` — 200; date 2026-10-12.
- **arxiv_https** — `https://export.arxiv.org/api/query?search_query=all%3A%22waiting+time%22+AND+all%3A%22patterns%22&max_results=40&sortBy=submittedDate&sortOrder=descending` — 200; date 2026-10-12.
- **crossref** — `https://api.crossref.org/works?query.bibliographic=Patterns+in+random+walks+and+Brownian+motion&rows=20` — 200; date 2026-10-12.
- **openalex_doi** — `https://api.openalex.org/works/https://doi.org/10.1007/978-3-319-18585-9_4` — HTTP Error 429: Too Many Requests; date 2026-10-12.
- **s2_search** — `https://api.semanticscholar.org/graph/v1/paper/search?query=patterns+random+walks+Brownian+motion&limit=10&fields=title%2Cyear%2CexternalIds` — HTTP Error 429: ; date 2026-10-12.
- **arxiv_pitman_tang** — `http://export.arxiv.org/api/query?search_query=all%3A%22Pitman%22+AND+all%3A%22Tang%22+AND+all%3A%22patterns%22&max_results=100` — 200; date 2026-10-12.
- **arxiv_targeted** — `http://export.arxiv.org/api/query?search_query=cat%3Amath.PR+AND+%28all%3A%22patterns%22+AND+all%3A%22waiting%22%29&max_results=100` — 200; date 2026-10-12.
- **crossref_targeted** — `https://api.crossref.org/works?query=pattern+waiting+times+Pitman+Tang&rows=40` — 200; date 2026-10-12.
- **openalex_citing_attempt** — `https://api.openalex.org/works?filter=cites%3Adoi%3A10.1007%2F978-3-319-18585-9_4&per-page=100` — HTTP Error 429: Too Many Requests; date 2026-10-12.
- **paper_2410.13426** — `https://arxiv.org/pdf/2410.13426` — 200; date 2026-10-12.
- **paper_1602.06512** — `https://arxiv.org/pdf/1602.06512` — 200; date 2026-10-12.
- **paper_2601.16580** — `https://arxiv.org/pdf/2601.16580` — 200; date 2026-10-12.
- **crossref_2012** — `https://api.crossref.org/works/10.1016/j.jspi.2011.12.028` — 200; date 2026-10-12.
- **crossref_extremal** — `https://api.crossref.org/works?query=maximum+expected+waiting+time+collection+patterns+cardinality&rows=30` — 200; date 2026-10-12.


## Second attempt, 12 October 2026

The gap itself was queried in the read-only math store twice: “ballot theorem first passage probability Pitman Tang waiting time exponent gap” and “Bertrand ballot theorem simple symmetric random walk hitting time binomial”. The first returned first-passage percolation cards; the second returned optional-stopping/general random-walk cards. No directly applicable ballot or waiting-time solution was found. None of these unrelated cards is used as a theorem in the proof.

Re-read source.txt around (2.20)–(2.23) and the first-passage simulation discussion, then checked its intended extremal-word comparison independently. The new proof does not rely on that comparison. SECOND_ATTEMPT.md records a finite rational counterexample to the downward-then-zigzag word being a maximum.

Two additional network searches were run after obtaining the new first-passage order theorem. The arXiv author/passage search returned Pitman and Tang's *Tree formulas, mean first passage times and Kemeny's constant of a Markov chain*, arXiv:1603.09017v3, DOI 10.3150/16-bej916 (Bernoulli, 2018), whose abstract concerns finite-state Markov chain tree formulas rather than scale-indexed first-passage word scanning. Crossref returned that paper and unrelated physical/inventory first-passage papers. No theorem resolving the full Question 1.7 was verified. These two searches are additional bounded checks, not a claim of exhaustive literature coverage or novelty for the theorem proved here.

The new result is an author-proved special case: E T(FP_(lambda,n))=Theta_lambda(n log n), with full proof and checks in SECOND_ATTEMPT.md. It is not being marked SOLVED_IN_LITERATURE.

Additional exact queries:
- **second_arxiv_firstpassage** — `http://export.arxiv.org/api/query?search_query=cat%3Amath.PR+AND+all%3A%22Pitman%22+AND+all%3A%22Tang%22+AND+all%3A%22passage%22&max_results=30` — 200; date 2026-10-12.
- **second_crossref_firstpassage** — `https://api.crossref.org/works?query=first+passage+patterns+waiting+time+n+log+n+Pitman+Tang&rows=20` — 200; date 2026-10-12.
