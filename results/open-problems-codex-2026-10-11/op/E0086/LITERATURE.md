# E0086 literature and status audit

Search date: 2026-10-11. Bounded searches used Python urllib from PowerShell, not a built-in web search. No theorem proving the main moving-offset question under its full hypotheses was located. This is not an exhaustive claim that the question is currently open. OpenAlex was rate-limited on every attempted route. The annular-scanning counterexample in ATTEMPT.md result 6 is our deduction from classical inputs and the independently checked prior upper-bound argument; it is not a solution found in print. The final mathematical verdict concerns this negative answer under the literal hypotheses, not a SOLVED_IN_LITERATURE claim.

## Source, exact statement, and corrections

Izumi Okada (2016), *Topics and problems on favorite sites of random walks*, RIMS Kôkyûroku Bessatsu B59, 129–139; arXiv:1606.03787v1 (13 June 2016). Fetched https://arxiv.org/pdf/1606.03787 and saved source.pdf/source.txt. Open problem 2 is PDF p. 6; the definitions needed to interpret it are PDF pp. 2–4.

“Open problem 2. Consider D̃_n ∈ H with D̃_n ⊂ D(0,a_n)^c and a_n → ∞ as n → ∞. Then, how is the asymptotic of M_{D̃_n}(n) with probability one?”

The membership symbol is ∈, not an intersection symbol. H is a class of bounded-cardinality offset sets, and M_H(n) maximizes local time on ∂_H R(n), where x qualifies exactly when every translated offset x+h is unvisited. It is not an annular site maximum. The special case is n^β<|h|≤2n^β, 0<β<1/2. The printed conjecture for a_n≥n^{1/2+ε} equates M_{D̃_n}(n) with max_x K(τ_n,x). This equality is incompatible with the two maximum-local-time constants quoted by the same source; ATTEMPT.md proves that discrepancy. We do not infer the author's intended correction.

The class H(M), PDF p. 3, fixes |H|≤M and requires 0∉H and P(T_x<T_H)>0 for each x∈Hᶜ. It excludes sets surrounding 0. The literal cardinality bound includes H=∅. The notation for origin exclusion is imperfect in the PDF. T_A is a positive-time hitting time; τ_n is first hit of the inner boundary of D(0,n), not first exit outside the disc.

## Every API search

All queries below were run on 2026-10-11. Full URLs, HTTP results, and response sizes are saved in search_log.json through search_log5.json. Raw successful responses are search_*.txt.

| Service | Query / route | Result |
|---|---|---|
| arXiv export API | all:"favorite sites" AND all:"random walks", max_results=30 | Success; source and later favorite-site papers returned. |
| arXiv export API | all:"random walk" AND (all:"boundary" AND all:"local time"), max_results=40, submittedDate descending | Success; no moving-offset boundary theorem identified in results. |
| arXiv export API | all:"disc" AND all:"covered" AND all:"random walk", max_results=15 | Success; located Dembo–Peres–Rosen (2007), arXiv:math/0503139. Several unrelated astronomical matches were ignored. |
| arXiv export API | au:Okada AND (all:"boundary" OR all:"favorite"), max_results=30 | Success; retrieved the source, its older boundary papers, pair-counting papers, and the Hao et al. paper below. Some other authors named Okada produced unrelated matches. |
| arXiv export API | ti:"Thick points for planar Brownian motion", max_results=5 | Success; zero entries. The original 2001 article was not located by this exact-title query. |
| OpenAlex works search | Topics and problems on favorite sites of random walks, per-page=5 | HTTP 429. |
| OpenAlex works search | random walk generalized boundary local time annulus, per-page=15 | HTTP 429. |
| OpenAlex retry | source title, per_page=3 | HTTP 429. |
| OpenAlex DOI lookup | works/https://doi.org/10.48550/arXiv.1606.03787 | HTTP 429; verified OpenAlex work ID could not be obtained. |
| OpenAlex citing works attempt | filter=cites:https://doi.org/10.48550/arXiv.1606.03787, per-page=100 | HTTP 429; this DOI-based filter was not validated by the service. No OpenAlex citation list was obtained. |
| Crossref works | query=Topics and problems on favorite sites of random walks, rows=8 | Success, but relevance was poor and the exact source was not matched. |
| Crossref works | query=random walk frequently visited sites generalized boundary Okada, rows=15 | Success; found the older inner-boundary article and other related work. |
| Semantic Scholar | paper/ARXIV:1606.03787 with title, authors, year, citationCount, citations.title/year/externalIds | HTTP 429. |
| Semantic Scholar retry | paper/search with source title, limit=5 | HTTP 429. |
| Semantic Scholar citations | paper/ARXIV:1606.03787/citations?fields=title,year,externalIds&limit=100 | Success; seven citing records, no next-page marker. |
| GitHub repository search | "favorite sites" "random walk", per_page=10 | Success; total_count=0. Repository search is not a publication-status proof. |

Semantic Scholar's seven citing records were: arXiv:2610.02727, *Favorite sites of one-dimensional transient random walk* (2026); arXiv:2511.21602, *The Exact Limsup Constant for Once-Visited Sites of One-Dimensional Simple Random Walk* (2025); arXiv:2509.19809, *Exact Limsup Growth of Rarely Visited Sites for One-Dimensional Simple Random Walk* (2025); arXiv:2409.00995, *Favorite sites for simple random walk in two and more dimensions* (2024 preprint, DOI 10.1007/s00440-025-01441-1); arXiv:2207.10846, *Favorite Downcrossing Sites of One-Dimensional Simple Random Walk* (2022); arXiv:2111.00688, *Three Favorite Edges Occurs Infinitely Often for One-Dimensional Simple Random Walk* (2021 preprint, DOI 10.1007/s40304-023-00382-2); arXiv:1612.01983, *Three favorite sites occurs infinitely often for one-dimensional simple random walk* (2016 preprint, DOI 10.1214/17-AOP1232). The one-dimensional titles concern a different model; full author metadata was not requested for those irrelevant records.

## Relevant papers and checked inputs

1. Chenxu Hao, Xinyi Li, Izumi Okada, Yushu Zheng, *Favorite Sites for Simple Random Walk in Two and More Dimensions*, arXiv:2409.00995v2; published DOI 10.1007/s00440-025-01441-1. PDF fetched and text extracted as search_favorite_2024.pdf/.txt. Theorem 1.1 concerns the simultaneous number of favorite sites in dimension 2, not local time on a moving-offset boundary: almost surely limsup #K^(2)(n)=3. Theorem 1.2 concerns dimension ≥3. The fetched full text has no occurrence of “boundary” or “annul”; it cites Okada's source as reference [28]. This is related literature, not a resolution of Open problem 2.

2. Amir Dembo, Yuval Peres, Jay Rosen, *How large a disc is covered by a random walk in n steps?*, Annals of Probability 35 (2007), 577–601, arXiv:math/0503139v3. PDF fetched as covered_2007.pdf and extracted as covered_2007.txt. Theorem 1.1, PDF p. 2, gives largest completely covered disc radius n^{1/4+o(1)} after n deterministic steps and the corresponding radius-r exit-time exponent 1/2. It does not say that a prescribed finite family of offsets remains unvisited around a favorite site. Theorem 1.2 concerns multiply covered discs. These are leads only.

3. Amir Dembo, Yuval Peres, Jay Rosen, Ofer Zeitouni, *Thick points for planar Brownian motion and the Erdős–Taylor conjecture on random walk*, Acta Mathematica 186 (2001), 239–270. Used input: deterministic-time maximum divided by (log n)² tends to 1/π, while the radius-n stopped maximum divided by (log n)² tends to 4/π, a.s. These limits are explicitly stated on Okada PDF p. 2. We have checked that secondary statement against the source definitions; the original 2001 paper has not been fetched in this attempt. These are classical inputs, not a later solution of the moving-offset question.

4. Gregory F. Lawler and Vlada Limic, *Random Walk: A Modern Introduction*, Cambridge University Press (2010). Author-hosted PDF fetched from https://www.math.uchicago.edu/~lawler/srwbook.pdf as search_potential_book.pdf/.txt. In this fetched manuscript, PDF page numbers equal its displayed page numbers: potential kernel definition (4.15) and a(0)=0 on p. 86; Proposition 4.4.1 on pp. 86–87 says 2a(x) is the expected number of visits to x before the first hit of 0 from x. Proposition 4.4.2, p. 87, gives La=δ_0. Theorem 4.4.4, p. 88, gives for simple random walk a(x)=(2/π)log|x|+(2γ+log 8)/π+O(|x|^{-2}). These verify the exact normalization used in ATTEMPT.md. The killed-return identity is also proved there independently from the kernel identities. This book is a tool for our partial proof, not a solution in print.

5. Izumi Okada, *Frequently visited sites of the inner boundary of simple random walk range*, Stochastic Processes and their Applications 126 (2016), 1412–1432, DOI 10.1016/j.spa.2015.11.008, arXiv:1409.8368v2. Retrieved as a Crossref/arXiv record and cited by the source. Its fixed nearest-neighbor boundary result does not settle a changing far-offset boundary.

6. Izumi Okada, *The inner boundary of random walk range*, arXiv:1407.2081v2; *Exponents for the number of pairs of α-favorite points of simple random walk in Z²*, arXiv:1602.05641v2; *Geometric structures of late points of a two-dimensional simple random walk*, arXiv:1605.01158v3. Search hits and source references; no exact moving-offset theorem identified. No full-text claim about their contents is made.

Other arXiv leads returned were *Exceptional points of discrete-time random walks in planar domains*, arXiv:1911.11810v1, and *Exceptional points of two-dimensional random walks at multiples of the cover time*, arXiv:1903.04045v2. These concern thick/thin-point processes in other stopping/time regimes; their abstracts were retrieved by the API. They were not used as a proof of this question.

## Brain, earlier attempt, and repository audit

Executed the prescribed brain recall for “planar random walk favorite sites annulus” and “planar random walk local time mistakes”, and math recall for “planar random walk maximal local time restricted disc Csaki Revesz”. No usable verified theorem about this exact offset problem was returned. The brain recall utility itself printed that it merged fresh memories and handed off an automatic index refresh; no remember command or manual write to the brain was issued, and the utility was not invoked again.

Read intake E_20260908 attempts.jsonl, E0086-A001, and problems.jsonl, E0086. That attempt misread the offset class as an annular region of candidate sites and predicted vanishing local time beyond the diffusive radius. For the actual boundary maximum, the opposite equality holds there (ATTEMPT.md result 1). Its scaling conjecture is not used.

During the attempt, a second math-store recall asked “potential kernel planar random walk Green function hitting probability”. It returned general potential-theory cards and unrelated local-time work; no new source-matching theorem was adopted.

Read-only inspection of origin/master in ~/math-open-problems found operations/claims/E0086.md and NM13-12's 2026-09-18 reports. The following were read using git show origin/master:<path>:

- operations/claims/E0086.md;
- proofnet24/NM13-12/runs/2026-09-18/2026-09-18T07-51-25Z__e0086-potential-kernel-hazard-upper-bound.md;
- proofnet24/NM13-12/runs/2026-09-18/2026-09-18T08-59-30Z__e0086-two-trap-green-upper-bound.md;
- proofnet24/NM13-12/runs/2026-09-18/2026-09-18T14-05-00Z__e0086-packet-second-moment-handoff.md.

The earlier hazard report already proves the same finite-time tail and the 4α(1+2α)/π almost-sure upper bound we derived. The two-trap report gives the sharper probability upper constant 4α(1−α)/π and almost-sure bound with a temporal-offset factor. The analytic core of the latter was extracted to prior_two_trap_excerpt.md and independently checked in ATTEMPT.md result 5. Thus these upper results carry no novelty claim in our work history.

The packet handoff claims a finite-volume positive-probability lower theorem for singleton offsets and α<1/5, near the candidate 4α(1−α)/π, but explicitly leaves the almost-sure deterministic-time amplification unproved. It labels its full source status PARTIAL and has no independent closure audits. We treat its detailed lower estimates as a lead, not as a checked theorem or literature solution. No repository working tree was changed.
