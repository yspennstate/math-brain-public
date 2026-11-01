# P0170 literature and status audit

Date: 2026-10-12. **No paper determining the least k(d,epsilon) under the problem's exact hypotheses was identified in this bounded search.** This is not a proof that no such paper exists. Verdict is PARTIAL, not SOLVED_IN_LITERATURE. Successful and failed requests are listed below and raw responses are retained.

## Exact source

Ryan O'Donnell, *Open problems in analysis of Boolean functions*, arXiv:1204.6447, 2012, PDF page 9, “k-wise Independence for PTFs”. Downloaded successfully from https://arxiv.org/pdf/1204.6447; retained as source.pdf and page-marked source.txt.

The statement, with mathematical layout restored from the PDF, reads:

> Statement: Fix d ∈ N and ǫ ∈ (0,1). Determine the least k = k(d,ǫ) such that the following holds: If p : R^n → R is any degree-d multivariate polynomial, and X is any R^n-valued random variable with the property that each X_i has the standard Gaussian distribution and each collection X_i1,...,X_ik is independent, then |Pr[p(X) ≥ 0] − Pr[p(Z) ≥ 0]| ≤ ǫ, where Z has the standard n-dimensional Gaussian distribution.

Source attribution there: [DGJ+09]. The hypotheses require full product Gaussian laws on coordinate subsets. The problem does not assume X has a multivariate Gaussian law. Moment matching alone is a weaker hypothesis.

The same page reports O(1/epsilon^2) sufficiency for d=1, O(1/epsilon^8) for d=2, and, for general d, O_d(1) epsilon^(-2^(O(d))) sufficiency and Omega(d^2/epsilon^2) necessity. These are **bounds reported by the source**, not a determination of the least k. I verified the general upper theorem in Kane's primary paper below. I did not locate and check a primary proof of the quoted Omega(d^2/epsilon^2) lower bound; it is not promoted to an independently proved claim in CLAIMS.jsonl.

## Primary papers checked and how they relate

1. Daniel M. Kane, *k-Independent Gaussians Fool Polynomial Threshold Functions*, arXiv:1012.1614v3; Proceedings of the 26th Annual IEEE Conference on Computational Complexity (CCC 2011), pp. 252–261, DOI 10.1109/CCC.2011.13. Primary PDF fetched and retained as paper_1012_1614.json (PDF bytes) and paper_1012_1614.txt. Theorem 1, PDF page 1, gives a sufficient k=O_d(epsilon^(-2^(O(d)))) for **any** k-independent family of Gaussians. The theorem is an upper bound, not the optimal answer. Its introductory page 2 expressly points to earlier results for polynomials of a small number of linear forms, so our special-case theorem carries no novelty claim. PDF metadata/date labels are inconsistent: the arXiv banner is 11 Nov 2011 while the internal title page prints November 9, 2018. The arXiv ID/version and CCC citation identify the work unambiguously.

2. Daniel M. Kane, *A Small PRG for Polynomial Threshold Functions of Gaussians*, arXiv:1104.1209; FOCS 2011, pp. 257–266. Theorem 1, PDF pages 1–2, assumes X=N^(-1/2) sum_i X_i with the vectors X_i sampled **independently** from k-independent Gaussian families. It obtains a PRG via a convolution/sum construction. This is a restricted family of k-wise independent laws; the additional independent summands are part of the theorem. It does not prove every k-wise independent Gaussian vector fools PTFs at those parameters and does not determine minimal k. The source's bibliography calls this [Kan11]; do not silently interpret that citation as an optimality theorem.

3. Daniel M. Kane, *A Structure Theorem for Poorly Anticoncentrated Gaussian Chaoses and Applications to the Study of Polynomial Threshold Functions*, arXiv:1204.0543; FOCS 2012, pp. 91–100. PDF fetched. Theorem 22, PDF page 29, improves the independent-sum PRG to N=O_(c,d)(epsilon^(-2-c)) with k=O(d/c). It still explicitly requires independent Gaussian-family summands. Its diffuse decomposition theorem is a possible route to general bounds, but its existence does not supply an optimal dependence for arbitrary exact k-wise laws. It is recorded as a lead.

4. Ryan O'Donnell, Rocco A. Servedio, Li-Yang Tan, with an appendix by Daniel Kane, *Fooling Gaussian PTFs via Local Hyperconcentration*, arXiv:2103.07809v2, 9 Feb 2022 (initial arXiv posting 2021). (The original three-author STOC 2020 version has pp. 1170–1183.) PDF fetched. Definition 11 on PDF page 13 gives the exact product-coordinate meaning of k-wise Gaussian independence. Theorem 5 and the argument on PDF page 12 concern a **scaled sum** of limited-independent Gaussian vectors; the page explicitly says “Theorem 5 shows that a scaled sum of k_indep-wise independent Gaussians fools degree-d PTFs”. The new polynomial dependence of the seed length on d is a PRG improvement, not a bound saying every arbitrary such vector is fooled at the same independence parameter. The version is sometimes listed with Kane as a fourth author; the title page and appendix attribution should be retained rather than conflated.

5. Zander Kelley and Raghu Meka, *Random Restrictions and PRGs for PTFs in Gaussian Space*, arXiv:2103.14134v2, 2021; FOCS 2022 version cited as [KM22] in the 2025 paper. PDF fetched. Its target is an explicit PRG with polynomial d-dependence and nearly quadratic error dependence in seed length. This does not quantify over every arbitrary exact k-wise Gaussian law. Relevant to methods, not a solution of the optimization question.

6. Penghui Yao and Mingnan Zhao, *A Pseudorandom Generator for Functions of Low-Degree Polynomial Threshold Functions*, arXiv:2504.10904v2, 2025 (ICALP 2025 record returned by Semantic Scholar). PDF fetched. Theorem 3.1 on PDF page 7 uses Y=L^(-1/2) sum_i Y_i, where each Y_i is a 2dR-wise independent Gaussian vector; the independent-summand hypothesis is stated in the abstract/introduction. Its error is O(epsilon*k*d^3)+kdL*2^(-Omega(R)), with L=Omega(k^2 d^3 R^15/epsilon^2). Here k is the number of PTFs, not the independence level asked in P0170. The heading “Bounded independence fools functions...” must not be detached from the summation model. Not a solution of P0170.

7. Adam R. Klivans, Konstantinos Stavropoulos, and Arsen Vasilyan, *Sandwiching Polynomials for Geometric Concepts with Low Intrinsic Dimension*, arXiv:2602.24178v1, 27 Feb 2026; internal manuscript date March 2, 2026. PDF fetched. Theorem 1.2, PDF page 3, bounds sandwiching degree in terms of intrinsic dimension k, boundary smoothness sigma, error epsilon, and distribution-tail parameter gamma. Table 1 explicitly gives a dependence on intrinsic dimension for degree-q PTFs in k dimensions. This can imply limited-independence bounds for those special classes by expectation matching, but it does not eliminate arbitrary ambient/intrinsic dimension for a general degree-d polynomial. It is a newer special-case/method lead, not an optimal all-PTF answer.

8. Ilias Diakonikolas, Parikshit Gopalan, Ragesh Jaiswal, Rocco A. Servedio, and Emanuele Viola, *Bounded Independence Fools Halfspaces*, SIAM Journal on Computing 39(8):3441–3462, 2010 (FOCS 2009 original). Cited by the source and by fetched recent papers. General halfspace result; the Gaussian d=1 sufficiency is known, so rederiving it is not solving the general question.

9. Ilias Diakonikolas, Daniel M. Kane, and Jelani Nelson, *Bounded Independence Fools Degree-2 Threshold Functions*, FOCS 2010, pp. 11–20, DOI 10.1109/FOCS.2010.8. Crossref returned the exact bibliographic record. Known quadratic special case, not the least general k(d,epsilon).

Other recent arXiv hits about Boolean surface area, sensitivity, learning, and PTF testing lower bounds were screened by their returned title/abstract. They do not state a theorem solving this exact question. Their metadata is preserved below; this does not mean their full proofs were audited.

## Why no SOLVED_IN_LITERATURE verdict

The further conditional estimate in DENSITY_BOUND.md uses the standard Gaussian noise-sensitivity argument of Daniel M. Kane, *The Gaussian Surface Area and Noise Sensitivity of Degree-d Polynomial Threshold Functions*, arXiv:0912.2709, journal version 2011, DOI 10.1007/s00037-011-0012-6 (Crossref returned this title and DOI). Its circle-root proof is supplied directly in that file. This reference concerns sensitivity under the fully independent Gaussian law, not optimal exact limited independence.

The matching requirements are: arbitrary n; every degree-d polynomial; every law with exact Gaussian product coordinate marginals up to k; discrepancy for the event p>=0; and determination of the smallest k as a function of d and epsilon. The older direct theorem supplies only a sufficient bound. The newer PRGs impose independent-sum structure or output a specific constructed law, and the newer sandwiching result depends on intrinsic dimension. None of the checked theorems states and proves the requested optimal answer under all these quantifiers. No alleged solution theorem is quoted as such.

OpenAlex's search, direct source-resolution, and attempted citing-source requests all returned HTTP 429. Consequently no validated OpenAlex W-ID or complete citing-work list was obtained. The DOI-based citing filter was attempted as an external-ID query but its syntax/ID resolution could not be validated under rate limiting. This is an incomplete citation audit, not a claim of no citing solutions. Semantic Scholar ordinary search and direct source-with-citations also returned 429; its bulk keyword endpoint succeeded and found four records, including the 2025 paper. GitHub repository search succeeded and returned zero repositories for the narrow query. ArXiv and Crossref were available.

## Read-only brain and prior-attempt audit

Used math_recall.py with “Gaussian polynomial threshold bounded independence Kane”, and walked claim_54ceec8878c6a894c9ea01e079f157f5f75e684800bb1b49d97136d2142376a2. The recalled prior attempt was the n=d parity obstruction. It was rederived in ATTEMPT.md rather than accepted as a verdict. Used brain.py recall for “Gaussian polynomial threshold independence mistakes” and “Gaussian polynomial thresholds bounded independence”. The warnings about confusing marginal and joint independence were incorporated into the proof audit. No remember/write commands were issued. The recall utility printed its own unsuccessful automatic refresh notice; no refresh was requested by this worker.

Searched the provided probability_1000_intake_* ledgers and codex_pool_2026_10_10 JSONL files for P0170, and listed origin/master paths of math-open-problems with a P0170/p0170 filter. No additional matching record was returned. The first rg request using a wildcard directory literal failed on Windows and was corrected by enumerating the named intake directories in PowerShell. Two intake directories lacked attempts.jsonl/sources.jsonl; these read errors do not establish absence of earlier work. Git was used read-only; no repository working tree was changed.

## Complete HTTP search and fetch log

All requests below were made on 2026-10-12 using Python urllib from the shell. Raw successful responses are retained in this folder; search_log.jsonl contains the same request ledger. Errors are search limitations, not negative literature evidence.

- 2026-10-12 — openalex_source: `https://api.openalex.org/works?search=Open+problems+in+analysis+of+Boolean+functions&per-page=5`. Outcome: HTTP Error 429: Too Many Requests.
- 2026-10-12 — openalex_search: `https://api.openalex.org/works?search=Gaussian+polynomial+thresholds+bounded+independence&per-page=30`. Outcome: HTTP Error 429: Too Many Requests.
- 2026-10-12 — source: `https://arxiv.org/pdf/1204.6447`. Outcome: 200; 162458 bytes.
- 2026-10-12 — kane_search: `https://api.openalex.org/works?search=Kane+k+independent+Gaussians+fool+polynomial+threshold+functions&per-page=20`. Outcome: HTTP Error 429: Too Many Requests.
- 2026-10-12 — semantic: `https://api.semanticscholar.org/graph/v1/paper/search?query=Gaussian+polynomial+threshold+bounded+independence&limit=30&fields=title%2Cauthors%2Cyear%2CexternalIds%2Curl%2Cabstract`. Outcome: HTTP Error 429: .
- 2026-10-12 — github: `https://api.github.com/search/repositories?q=Gaussian+polynomial+threshold+independence&per_page=20`. Outcome: 200; 55 bytes.
- 2026-10-12 — crossref: `https://api.crossref.org/works?query=Gaussian+polynomial+threshold+bounded+independence&rows=25`. Outcome: 200; 106641 bytes.
- 2026-10-12 — arxiv_api: `https://export.arxiv.org/api/query?search_query=all%3A%22polynomial+threshold%22+AND+%28all%3A%22independence%22+OR+all%3A%22Gaussian%22%29&max_results=40&sortBy=submittedDate&sortOrder=descending`. Outcome: 200; 66549 bytes.
- 2026-10-12 — semantic_source: `https://api.semanticscholar.org/graph/v1/paper/ARXIV:1204.6447?fields=title,year,citations.title,citations.year,citations.externalIds`. Outcome: HTTP Error 429: .
- 2026-10-12 — paper_2103_07809: `https://arxiv.org/pdf/2103.07809`. Outcome: 200; 1235959 bytes.
- 2026-10-12 — paper_2103_14134: `https://arxiv.org/pdf/2103.14134`. Outcome: 200; 303083 bytes.
- 2026-10-12 — paper_2504_10904: `https://arxiv.org/pdf/2504.10904`. Outcome: 200; 272432 bytes.
- 2026-10-12 — crossref_recent: `https://api.crossref.org/works?query=bounded+independence+polynomial+threshold+functions&filter=from-pub-date%3A2012-01-01&rows=30&sort=relevance`. Outcome: 200; 217661 bytes.
- 2026-10-12 — openalex_retry: `https://api.openalex.org/works?search=Open+problems+in+analysis+of+Boolean+functions&per_page=3`. Outcome: HTTP Error 429: Too Many Requests.
- 2026-10-12 — arxiv_kane: `https://export.arxiv.org/api/query?search_query=ti%3A%22small+PRG%22+OR+ti%3A%22poorly+anticoncentrated%22+OR+ti%3A%22bounded+independence%22&max_results=40&sortBy=relevance`. Outcome: 200; 42250 bytes.
- 2026-10-12 — arxiv_independence: `https://export.arxiv.org/api/query?search_query=all%3A%22polynomial+threshold%22+AND+all%3A%22independence%22&max_results=60&sortBy=submittedDate&sortOrder=descending`. Outcome: 200; 34839 bytes.
- 2026-10-12 — paper_1204_0543: `https://arxiv.org/pdf/1204.0543`. Outcome: 200; 504064 bytes.
- 2026-10-12 — paper_2602_24178: `https://arxiv.org/pdf/2602.24178`. Outcome: 200; 927152 bytes.
- 2026-10-12 — openalex_source_direct: `https://api.openalex.org/works/https://doi.org/10.48550/arXiv.1204.6447`. Outcome: HTTP Error 429: Too Many Requests.
- 2026-10-12 — openalex_citing_source: `https://api.openalex.org/works?filter=cites%3Adoi%3A10.48550%2FarXiv.1204.6447&per-page=50`. Outcome: HTTP Error 429: Too Many Requests.
- 2026-10-12 — paper_1012_1614: `https://arxiv.org/pdf/1012.1614`. Outcome: 200; 237465 bytes.
- 2026-10-12 — semantic_bulk: `https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=%22polynomial+threshold%22+%22independence%22&fields=title%2Cyear%2CexternalIds`. Outcome: 200; 1180 bytes.
- 2026-10-12 — paper_1104_1209: `https://arxiv.org/pdf/1104.1209`. Outcome: 200; 198407 bytes.

## Titles returned by the relevant arXiv queries

These are search hits, not theorem verification. Author names and version dates are copied from returned Atom metadata.

- Sanjeev Khanna, Ashwin Padaki, Erik Waingarten. Learning Partition Trees for Nearest Neighbor Search. http://arxiv.org/abs/2607.09909v1; version date 2026-07-10.
- Chun-Kai Tseng, Alexander Volberg. Small moments of the sensitivity of polynomial threshold functions. http://arxiv.org/abs/2606.16004v2; version date 2026-06-21.
- Fan Chang, Joseph Slote, Alexander Volberg, Haonan Zhang. The Boolean surface area of polynomial threshold functions. http://arxiv.org/abs/2604.08095v2; version date 2026-04-27.
- Lucas Pesenti, Lucas Slot, Manuel Wiedmer. Agnostic learning in (almost) optimal time via Gaussian surface area. http://arxiv.org/abs/2603.06027v1; version date 2026-03-06.
- Adam R. Klivans, Konstantinos Stavropoulos, Arsen Vasilyan. Sandwiching Polynomials for Geometric Concepts with Low Intrinsic Dimension. http://arxiv.org/abs/2602.24178v1; version date 2026-02-27.
- Shalender Singh, Vishnupriya Singh. An Algebraic Rigidity Framework for Order-Oblivious Deterministic Black-Box PIT of ROABPs. http://arxiv.org/abs/2602.13449v1; version date 2026-02-13.
- Ilias Diakonikolas, Daniel M. Kane, Sihan Liu, Thanasis Pittas. PTF Testing Lower Bounds for Non-Gaussian Component Analysis. http://arxiv.org/abs/2511.19398v1; version date 2025-11-24.
- Penghui Yao, Mingnan Zhao. A Pseudorandom Generator for Functions of Low-Degree Polynomial Threshold Functions. http://arxiv.org/abs/2504.10904v2; version date 2025-04-21.
- Lucas Slot, Stefan Tiegel, Manuel Wiedmer. Testably Learning Polynomial Threshold Functions. http://arxiv.org/abs/2406.06106v2; version date 2024-11-06.
- Ilias Diakonikolas, Daniel M. Kane, Vasilis Kontonis, Sihan Liu, Nikos Zarifis. Super Non-singular Decompositions of Polynomials and their Application to Robustly Learning Low-degree PTFs. http://arxiv.org/abs/2404.00529v1; version date 2024-03-31.
- Shiwei Zeng, Jie Shen. Attribute-Efficient PAC Learning of Low-Degree Polynomial Threshold Functions with Nasty Noise. http://arxiv.org/abs/2306.00673v2; version date 2024-03-19.
- Stefan Tiegel. Hardness of Agnostically Learning Halfspaces from Worst-Case Lattice Problems. http://arxiv.org/abs/2207.14030v2; version date 2023-02-20.
- Zander Kelley, Raghu Meka. Random restrictions and PRGs for PTFs in Gaussian Space. http://arxiv.org/abs/2103.14134v2; version date 2021-11-29.
- Ryan O'Donnell, Rocco A. Servedio, Li-Yang Tan, Daniel Kane. Fooling Gaussian PTFs via Local Hyperconcentration. http://arxiv.org/abs/2103.07809v2; version date 2022-02-09.
- Pierre Baldi, Roman Vershynin. A theory of capacity and sparse neural encoding. http://arxiv.org/abs/2102.10148v1; version date 2021-02-19.
- Ilias Diakonikolas, Daniel M. Kane, Thanasis Pittas, Nikos Zarifis. The Optimality of Polynomial Regression for Agnostic Learning under Gaussian Marginals. http://arxiv.org/abs/2102.04401v1; version date 2021-02-08.
- Vasilis Kontonis, Christos Tzamos, Manolis Zampetakis. Efficient Truncated Statistics with Unknown Truncation. http://arxiv.org/abs/1908.01034v1; version date 2019-08-02.
- Ilias Diakonikolas, Daniel M. Kane. Degree-$d$ Chow Parameters Robustly Determine Degree-$d$ PTFs (and Algorithmic Applications). http://arxiv.org/abs/1811.03491v1; version date 2018-11-07.
- Ilias Diakonikolas, Daniel M. Kane, Alistair Stewart. Learning Geometric Concepts with Nasty Noise. http://arxiv.org/abs/1707.01242v1; version date 2017-07-05.
- Daniel M. Kane. A Polylogarithmic PRG for Degree $2$ Threshold Functions in the Gaussian Setting. http://arxiv.org/abs/1404.1103v1; version date 2014-04-03.
- Varun Kanade, Justin Thaler. Distribution-Independent Reliable Learning. http://arxiv.org/abs/1402.5164v1; version date 2014-02-20.
- Anindya De, Rocco Servedio. Efficient deterministic approximate counting for low-degree polynomial threshold functions. http://arxiv.org/abs/1311.7178v1; version date 2013-11-28.
- Anindya De, Ilias Diakonikolas, Rocco A. Servedio. Deterministic Approximate Counting for Juntas of Degree-$2$ Polynomial Threshold Functions. http://arxiv.org/abs/1311.7115v1; version date 2013-11-27.
- Daniel M. Kane. A Pseudorandom Generator for Polynomial Threshold Functions of Gaussian with Subpolynomial Seed Length. http://arxiv.org/abs/1210.1280v1; version date 2012-10-04.
- Daniel M. Kane. A Structure Theorem for Poorly Anticoncentrated Gaussian Chaoses and Applications to the Study of Polynomial Threshold Functions. http://arxiv.org/abs/1204.0543v2; version date 2012-08-15.
- Daniel M. Kane. A Small PRG for Polynomial Threshold Functions of Gaussians. http://arxiv.org/abs/1104.1209v1; version date 2011-04-06.
- Daniel M. Kane. $k$-Independent Gaussians Fool Polynomial Threshold Functions. http://arxiv.org/abs/1012.1614v3; version date 2011-11-11.
- Daniel M. Kane. The Gaussian Surface Area and Noise Sensitivity of Degree-$d$ Polynomials. http://arxiv.org/abs/0912.2709v1; version date 2009-12-14.
- Ido Ben-Eliezer, Shachar Lovett, Ariel Yadin. Polynomial Threshold Functions: Structure, Approximation and Pseudorandomness. http://arxiv.org/abs/0911.3473v3; version date 2009-11-29.
- Raghu Meka, David Zuckerman. Pseudorandom Generators for Polynomial Threshold Functions. http://arxiv.org/abs/0910.4122v5; version date 2011-11-15.
- Prahladh Harsha, Adam Klivans, Raghu Meka. Bounding the Sensitivity of Polynomial Threshold Functions. http://arxiv.org/abs/0909.5175v4; version date 2009-11-09.
- Ilias Diakonikolas, Prasad Raghavendra, Rocco A. Servedio, Li-Yang Tan. Average sensitivity and noise sensitivity of polynomial threshold functions. http://arxiv.org/abs/0909.5011v2; version date 2009-10-19.
- Ilias Diakonikolas, Parikshit Gopalan, Ragesh Jaiswal, Rocco Servedio, Emanuele Viola. Bounded Independence Fools Halfspaces. http://arxiv.org/abs/0902.3757v1; version date 2009-02-21.
- Dean Doron, Jack Murtagh, Salil Vadhan, David Zuckerman. Spectral Sparsification via Bounded-Independence Sampling. http://arxiv.org/abs/2002.11237v2; version date 2020-04-20.
- Minki Kim, Alan Lew. Complexes of graphs with bounded independence number. http://arxiv.org/abs/1912.12605v1; version date 2019-12-29.
- Martijn Brehm, Yuval Ishai, Nicolas Resch. Fast Bounded-Independence Functions and Their Duals. http://arxiv.org/abs/2606.07009v1; version date 2026-06-05.
- Kosuke Suzuki. Bounded independence for the inverse star discrepancy. http://arxiv.org/abs/2608.15865v1; version date 2026-08-16.
- Ilias Diakonikolas, Daniel M. Kane, Jelani Nelson. Bounded Independence Fools Degree-2 Threshold Functions. http://arxiv.org/abs/0911.3389v2; version date 2010-02-18.
- Nicolas El Maalouly, Raphael Steiner. Exact Matching in Graphs of Bounded Independence Number. http://arxiv.org/abs/2202.11988v3; version date 2022-07-13.
- Martin Milanič, Paweł Rzążewski. Tree decompositions with bounded independence number: beyond independent sets. http://arxiv.org/abs/2209.12315v1; version date 2022-09-25.
- Aaron Putterman, Salil Vadhan, Vadim Zaripov. Bounded-Independence Sampling of Edges for Combinatorial Graph Properties. http://arxiv.org/abs/2603.25095v2; version date 2026-07-13.
- David Galvin, Phillip Marmorino. Counting independent sets in regular graphs with bounded independence number. http://arxiv.org/abs/2410.19959v1; version date 2024-10-25.
- Oleg Pikhurko, Emil R. Vaughan. Minimum Number of k-Cliques in Graphs with Bounded Independence Number. http://arxiv.org/abs/1203.4393v4; version date 2013-04-27.
- Matthias Lanzinger. FPT=PTIME for Homomorphism Problems on Sparse-Incidence and Bounded-Independence Patterns. http://arxiv.org/abs/2609.21840v1; version date 2026-09-18.
- Xue Chen, Shengtang Huang, Xin Li, Haoran Wang. Bounded Independence for $k$-Min-Wise Hashing: Tight Bounds and Limitations of Structured Hashing. http://arxiv.org/abs/2607.27157v2; version date 2026-09-06.
- Nikola Jedličková, Jan Kratochvíl. Hamiltonian path and Hamiltonian cycle are solvable in polynomial time in graphs of bounded independence number. http://arxiv.org/abs/2309.09228v3; version date 2025-04-01.
- Jackson Loper, Jeffrey Regier. A new tail bound for the sum of bounded independent random variables. http://arxiv.org/abs/2503.17594v1; version date 2025-03-22.
- Charis Papadopoulos, Spyridon Tzimas. Subset Feedback Vertex Set on Graphs of Bounded Independent Set Size. http://arxiv.org/abs/1805.07141v1; version date 2018-05-18.
- Yuhang Bai, Kristóf Bérczi, Johanna K. Siemelink. Approximating maximum properly colored forests via degree bounded independent sets. http://arxiv.org/abs/2511.18263v1; version date 2025-11-23.
- Ross Pinsky. Universal bound independent of geometry for solution to symmetric diffusion equation in exterior domain with boundary flux. http://arxiv.org/abs/1312.3432v1; version date 2013-12-12.
- Murdock Aubry, James Bremer. A solver for linear scalar ordinary differential equations whose running time is bounded independent of frequency. http://arxiv.org/abs/2311.08578v1; version date 2023-11-14.
