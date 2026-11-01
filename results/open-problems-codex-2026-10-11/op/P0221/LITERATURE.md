# P0221 literature search — 2026-10-11

Second-attempt brain queries, 2026-10-11: `controlled coagulation empirical state continuity optimal cost mean field control convergence`; `online random spanning tree Poisson combinatorial asymptotic equivalence Aldous Angel Berestycki`; `Hoeffding hypergeometric sampling without replacement Chernoff random graph cuts`. The last returned Hoeffding's 1963 source (DOI 10.1080/01621459.1963.10500830) and finite-population covariance/variance warnings. The hypergeometric lower-tail bound used in SECOND_ATTEMPT.md is proved directly by falling-factorial expansion, not taken on trust from these cards. Re-read source section 4, pp. 16–20, especially Proposition 12 and the stated conditional-completion gap.

## Result and exact references

No located paper settles existence and value of the limit. This is a bounded search result, not proof that no solution exists. The author-maintained open page still explicitly says there is no rigorous existence proof. OpenAlex queries were rate-limited, so its source identification and required citing-works search could not be completed. Semantic Scholar eventually identified the source through the references of Frieze–Pegden (paper ID 19d8db39ea0a731ef6ad138eee9d4d572ec6dc5a), but direct retrieval of its citing works remained rate-limited. These coverage gaps are material and preserved in the log.

1. **David Aldous, Omer Angel, Nathanael Berestycki.** *Online Random Weight Minimal Spanning Trees and a Stochastic Coalescent*. Draft, June 16, 2008. https://www.stat.berkeley.edu/~aldous/Research/OP/Beres2008.pdf. Primary source, saved as source.pdf, with source_extracted.txt. Conjecture and model distinction: p. 2; finite Poisson recursion: Theorem 3, p. 4; limit PDE and continuity claim: p. 7. The author page https://www.stat.berkeley.edu/~aldous/Research/OP/online_zeta3.html still lists the limit question and calls the draft incomplete. The page says it was posted in 2018; retrieval today alone does not certify a later editorial update.

2. **Alan Frieze, Wesley Pegden.** *Online purchasing under uncertainty*. Random Structures & Algorithms **53** (2018), no. 2, 327–351. DOI: **10.1002/rsa.20764**. arXiv: **1605.06072**, v2 January 10, 2017. Theorem 1.6 gives constant-order bounds for randomly ordered online spanning trees, with displayed bounds 1.38 and 2*zeta(3); its algorithmic upper estimate is below 2.31. The text explicitly says that Theorems 1.6–1.9 do not determine an asymptotic constant. It cites the Aldous–Angel–Berestycki draft. Both arXiv text and the author's current posted PDF https://www.math.cmu.edu/~af1p/Texfiles/Purchasing.pdf were fetched and read; the latter uses FOM for the purchaser-ordered model. This paper does not establish the target limit. Its bounds for the combinatorial ROM model must not be transferred to the source's Poisson model without proof.

3. **Corrigendum to “Online purchasing under uncertainty”.** Random Structures & Algorithms **59** (2021), no. 2, p. 288. DOI: **10.1002/rsa.21012**. Crossref metadata identifies it as a correction to 10.1002/rsa.20764, published online April 19, 2021. The retrieved metadata does not list authors. The full text returned 403, so its content and which theorem it corrects are not verified. We therefore do not use the original paper's sharper lower bound as an independently verified theorem in our proof. Metadata saved as corrigendum_metadata.json.

4. **Alan Frieze, Michael Krivelevich, Peleg Michaeli.** *Fast Construction on a Restricted Budget*. arXiv: **2207.07251**, v4 November 25, 2024 (PDF dated November 26, 2024); Semantic Scholar lists DOI **10.1002/rsa.70031**. This is a controlled unweighted random-graph process with an edge-count budget and a time budget. It cites Frieze–Pegden and discusses the weighted purchasing model as related work. Its connectivity and Hamiltonicity results do not settle the weighted mean-cost limit.

5. **Karthekeyan Chandrasekaran, Chandra Chekuri, Weihao Zhu.** *Online Disjoint Spanning Trees and Polymatroid Bases*. arXiv: **2503.19999**, v1 March 25, 2025. Concerns online packing of disjoint bases and polylogarithmic competitive ratios, not the random-weight cost limit. PDF fetched and checked.

6. **Magnus Berg, Joan Boyar, Lene M. Favrholdt, Kim S. Larsen.** *Online Minimum Spanning Trees with Weight Predictions*. arXiv: **2302.12029**, v1 February 23, 2023. Concerns prediction errors and competitive/random-order analysis rather than the optimal random-weight asymptotic constant. arXiv abstract and author metadata retrieved; no claim that its full PDF was read.

The successful Semantic Scholar lookup of Frieze–Pegden returned citations including *Some online Maker-Breaker games* (arXiv:2407.02288), *Fast Construction on a Restricted Budget*, and *Purchasing a C_4 online* (arXiv:1611.07503). The latter concerns another target structure; these citation titles provide leads rather than a verified resolution of P0221.

Additional primary-source check: section 4, pp. 16–20, formulates Proposition 12, C_n<=P_n+o(1), but explicitly describes its argument as having missing details and as sketchy. The terminal completion argument uses a conditional-edge-exchangeability assertion the author specifically asks coauthors to check. We do not invoke that incomplete proposition to transfer our Poisson bounds. This confirms that even a proposed one-sided transfer in the draft should not silently be treated as an established full equivalence theorem.

GitHub searches located a weight-prediction experiment repository and an Aldous–Broder/random-tree generation repository, neither a proof of the target limit. Unrelated hits were discarded. arXiv searches also returned many unrelated geometric, online-learning and unweighted spanning-tree papers. Negative search results are not mathematical evidence.

## Search log

The entries below give every web query run, its date and service (in the entry label), and the actual response. Python urllib was used; no built-in web search or images were used. Full successful responses are saved under their entry labels.

Read-only prior-work searches, also on 2026-10-11: math_recall.py --id claim_4d21ae7ea372b8447c051ebb79fc6ce8c452eef0d70b3ccd5c332f9199a04349 retrieved the earlier two-/three-component calculation and its hydrodynamic-limit gap. brain.py recall queries were `online random spanning tree mistakes` and `optimal online spanning tree cost Aldous Angel Berestycki`; no useful dedicated P0221 result was returned. `rg P0221` in probability_1000_intake_* found the prior attempted-unsolved ranking/summary; searches of the available top-level JSONL ledgers and codex_pool_2026_10_10 returned no additional result. A first Windows wildcard rg invocation failed and was replaced by PowerShell directory enumeration. Read-only `git ls-tree origin/master` filtered for P0221/p0221/online-spanning paths returned no path match; the repository working tree was not touched.

2026-10-11 | source | https://www.stat.berkeley.edu/~aldous/Research/OP/Beres2008.pdf | OK (234159 bytes)

2026-10-11 | author | https://www.stat.berkeley.edu/~aldous/Research/OP/index.html | OK (6517 bytes)

2026-10-11 | arxiv | https://export.arxiv.org/api/query?search_query=all:%22online%22%20AND%20%22spanning%20tree%22&max_results=30 | OK (65757 bytes)

2026-10-11 | openalex | https://api.openalex.org/works?search=Online%20random%20weight%20minimal%20spanning%20trees&per-page=20 | ERROR HTTP Error 429: Too Many Requests (0 bytes)

2026-10-11 | crossref | https://api.crossref.org/works?query.bibliographic=Online%20random%20weight%20minimal%20spanning%20trees&rows=20 | OK (91562 bytes)

2026-10-11 | semantic | https://api.semanticscholar.org/graph/v1/paper/search?query=Online%20random%20weight%20minimal%20spanning%20trees&limit=20&fields=title,authors,year,url,externalIds | ERROR HTTP Error 429:  (0 bytes)

2026-10-11 | github | https://api.github.com/search/repositories?q=online%20random%20spanning%20tree | OK (136252 bytes)

2026-10-11 | arxiv_purchasing | https://export.arxiv.org/api/query?id_list=1605.06072,2503.19999,2302.12029 | OK (6521 bytes)

2026-10-11 | arxiv_authors | https://export.arxiv.org/api/query?search_query=au%3AAldous%20AND%20%28all%3Aonline%20OR%20all%3Aspanning%29&max_results=30 | OK (11002 bytes)

2026-10-11 | openalex_retry | https://api.openalex.org/works?search=online%20random%20weight%20minimal%20spanning%20trees&per_page=5 | ERROR HTTP Error 429: Too Many Requests (0 bytes)

2026-10-11 | openalex_title | https://api.openalex.org/works?filter=title.search:Online%20Random%20Weight%20Minimal%20Spanning%20Trees&per_page=5 | ERROR HTTP Error 429: Too Many Requests (0 bytes)

2026-10-11 | semantic_retry | https://api.semanticscholar.org/graph/v1/paper/search?query=Aldous%20Angel%20Berestycki%20online&limit=5&fields=title,year,authors,citationCount,url | ERROR HTTP Error 429:  (0 bytes)

2026-10-11 | crossref_purchasing | https://api.crossref.org/works?query.title=Online%20purchasing%20under%20uncertainty&rows=5 | OK (20216 bytes)

2026-10-11 | github_exact | https://api.github.com/search/repositories?q=%22Aldous%22%20%22spanning%22 | OK (6313 bytes)

2026-10-11 | purchasing_pdf | https://arxiv.org/pdf/1605.06072 | OK (264464 bytes)

2026-10-11 | disjoint_pdf | https://arxiv.org/pdf/2503.19999 | OK (424750 bytes)

2026-10-11 | author_problem | https://www.stat.berkeley.edu/~aldous/Research/OP/online_zeta3.html | OK (1933 bytes)

2026-10-11 | arxiv_exact | https://export.arxiv.org/api/query?search_query=all%3A%22online%20random%22%20AND%20all%3A%22spanning%22&max_results=40 | OK (5619 bytes)

2026-10-11 | crossref_aldous | https://api.crossref.org/works?query=Aldous%20Angel%20Berestycki%20online%20spanning&rows=15 | OK (45394 bytes)

2026-10-11 | openalex_alt | https://api.openalex.org/works?search=Online%20purchasing%20under%20uncertainty&per-page=5 | ERROR HTTP Error 429: Too Many Requests (0 bytes)

2026-10-11 | semantic_match | https://api.semanticscholar.org/graph/v1/paper/URL:https://www.stat.berkeley.edu/~aldous/Research/OP/Beres2008.pdf?fields=title,authors,year,citations.title,citations.year,citations.externalIds | ERROR HTTP Error 404: Not Found (0 bytes)

2026-10-11 | corrigendum_xml | https://onlinelibrary.wiley.com/doi/full-xml/10.1002/rsa.21012 | ERROR HTTP Error 403: Forbidden (0 bytes)

2026-10-11 | frieze_home | https://www.math.cmu.edu/~af1p/ | OK (4796 bytes)

2026-10-11 | semantic_purchasing | https://api.semanticscholar.org/graph/v1/paper/DOI:10.1002/rsa.20764?fields=title,year,citations.title,citations.year,citations.externalIds,references.title,references.paperId | OK (5940 bytes)

2026-10-11 | openalex_source_id | https://api.openalex.org/works?filter=title.search:Online%20Random%20Weight%20Minimal%20Spanning%20Trees%20and%20a%20Stochastic%20Coalescent&select=id,title,cited_by_count,cited_by_api_url | ERROR HTTP Error 429: Too Many Requests (0 bytes)

2026-10-11 | arxiv_limit | https://export.arxiv.org/api/query?search_query=all%3A%22spanning%20tree%22%20AND%20%28all%3A%22purchasing%22%20OR%20all%3A%22online%20cost%22%20OR%20all%3A%22Berestycki%22%29&max_results=40 | OK (18405 bytes)

2026-10-11 | Crossref DOI lookup | https://api.crossref.org/works/10.1002/rsa.21012 | OK; saved corrigendum_metadata.json.

2026-10-11 | semantic_source | https://api.semanticscholar.org/graph/v1/paper/19d8db39ea0a731ef6ad138eee9d4d572ec6dc5a?fields=title,authors,year,externalIds,citations.title,citations.year,citations.externalIds | ERROR HTTP Error 429:  (0 bytes)

2026-10-11 | frieze_papers | https://www.math.cmu.edu/~af1p/papers.html | OK (102802 bytes)

2026-10-11 | arxiv_budget | https://arxiv.org/pdf/2207.07251 | OK (472676 bytes)

2026-10-11 | semantic_source_retry | https://api.semanticscholar.org/graph/v1/paper/19d8db39ea0a731ef6ad138eee9d4d572ec6dc5a?fields=title,year,externalIds,citations.title,citations.year,citations.externalIds | ERROR HTTP Error 429:  (0 bytes)

2026-10-11 | frieze_paper_current | https://www.math.cmu.edu/~af1p/Texfiles/Purchasing.pdf | OK (393459 bytes)

## Second-attempt source and gap queries, 2026-10-11

Read-only math-store queries: controlled coagulation empirical state continuity optimal cost mean field control convergence; online random spanning tree Poisson combinatorial asymptotic equivalence Aldous Angel Berestycki; Hoeffding hypergeometric sampling without replacement Chernoff random graph cuts. No recalled card is treated as a verdict.

Re-read the locally fetched Aldous--Angel--Berestycki 2008 draft, section 4, especially Proposition 12 (PDF p16) and section 4.3 (PDF pp19-20). It states costcomb(n) <= costPois(n) + o(1), explicitly with details missing and a sketchy completion argument. Our second attempt writes a separate complete proof with an explicit error rate; the source does not thereby establish reverse equivalence or limit existence. No new claim of a literature resolution is made.

Relevant neighbouring reference surfaced by the brain: Wassily Hoeffding, Probability inequalities for sums of bounded random variables, Journal of the American Statistical Association 58 (1963), 13-30, DOI 10.1080/01621459.1963.10500830. The needed sampling-without-replacement moment inequality is proved directly in SECOND_ATTEMPT.md rather than quoted as an external input.

2026-10-11, read-only math-store query during reverse-transfer audit: Poisson process predictable permutation thinning coupling exchangeability. Returned standard Poisson and predictability cards and the title Last--Penrose, Lectures on the Poisson Process. No recalled transfer theorem or publication claim was used; the relevant conditional-rate uniqueness and finite permutation extension are proved directly in REVERSE_TRANSFER.md. This query is recorded as a brain search, not as a web literature resolution.
