# F0085 literature audit — 2026-10-11

## Source and exact question
Christopher Hoffman, Alexander E. Holroyd, Yuval Peres, "A stable marriage of Poisson and Lebesgue", Annals of Probability 34(4) (2006), 1241–1272. DOI 10.1214/009117906000000098; arXiv math/0505668. Downloaded source.pdf, extracted source.txt.

Section 12, PDF page 31 (journal page 1271), verbatim:
> (iii) Percolation. In the Poisson model, does the set of unclaimed sites have an infinite component for α sufficiently small? Does it fail to have an infinite component for sufficiently large α < 1? Similar questions apply to the set of claimed sites. After this paper was accepted for publication, progress on these problems was achieved in [5].

The model is homogeneous Poisson centres of intensity λ=1 in R^d with common appetite α. The source develops d≥1; the follow-up percolation results explicitly assume d≥2. Subcritical means 0<α<1; all centres are sated (Theorem 4, PDF page 5) and P(0 unclaimed)=1−α (Proposition 20, PDF page 20). Stable allocations are unique only Lebesgue-a.e. (Theorem 3). Consequently a topological version must be specified; see ATTEMPT.md.

## Verified partial solutions in print
M. V. Freire, S. Popov, M. Vachkovskaia, "Percolation for the stable marriage of Poisson and Lebesgue", Stochastic Processes and their Applications 117(4) (2007), 514–525. DOI 10.1016/j.spa.2006.09.002; arXiv math/0511186v3, version date 24 July 2006. Local fpv.json is PDF bytes, fpv.txt its extraction. The PDF's generated front-page date is July 31, 2018; use the arXiv version date and Crossref publication record, rather than interpreting this typesetting date as a new theorem.

Theorem 1.1, arXiv PDF page 4, verbatim (mathematical typography transcribed; line breaks joined):
> (i) For any dimension d ≥ 2 we have that α_p(d) > 0, that is, if the appetite α is small enough, then a.s. there is no percolation by claimed sites.
> (ii) Also, if α is small enough and d ≥ 2, then there exists percolation by unclaimed sites (i.e., a.s. there is an unbounded connected component in R^d \ C).

Theorem 1.2, arXiv PDF page 6, verbatim:
> We have lim sup_{d→∞} α_p(d) 2^d ≤ 1. (1.1)

Definition preceding these results, PDF page 3:
> Denote by C the closure of ψ^{-1}(Ξ). The set C is the main object of study in this paper; it will be referred to as the set of claimed sites (even though it may contain some x ∈ R^d with ψ(x) = ∆).

Scope mapping:
1. Same intensity-one Poisson process and constant appetite.
2. For each fixed d≥2, Theorem 1.1(ii) answers YES to small-appetite unclaimed percolation, with exactly the desired sufficiently-small quantifier for R^d\C. For the canonical version, ATTEMPT Proposition A proves R^d\C is exactly the open unclaimed set. This version-identification argument is ours, not an additional quoted theorem.
3. Theorem 1.1(i) gives NO to small-appetite CLOSED claimed percolation; closure matters and is not silently identified with the raw union.
4. Theorem 1.2 gives a claimed-percolating appetite below one in all sufficiently high dimensions, hence all sufficiently large appetites below one there by their monotonicity. It does not give this in every d≥2.
5. No statement here proves absence of UNCLAIMED percolation near one. Claimed percolation alone does not exclude vacant percolation in dimensions ≥3.

The authors explicitly state on PDF page 6:
> Note, however, that proving that α_p(2) < 1 (as well as α_p(d) < 1 for small d) is still an open problem.

This is a historical statement; the bounded current search did not find a later resolution, but that is not proof of current openness. The entire F0085 question is NOT certified SOLVED_IN_LITERATURE.

Jean-Baptiste Gouéré, "Subcritical regimes in some models of continuum percolation", Annals of Applied Probability 19(4) (2009), 1292–1318. DOI 10.1214/08-AAP575; arXiv 0712.3638. Downloaded gouere.json (PDF bytes), gouere.txt. Theorem 1.10, PDF page 10:
> If α is small enough, then for all s > 0, E(D^s) is finite.
Here D is diameter of the origin component of closed claimed C. Lemma 1.11 dominates C by a DEPENDENT, unbounded-random-radius ball process. This is a stronger subcritical estimate, not the missing near-one vacant theorem. The paper explicitly notes the measurability caveat for D and proves domination by an integrable random variable.

Daniel Andrés Díaz Pachón, "Percolation for the stable marriage of Poisson and Lebesgue with random appetites", Stochastics 85(2) (2013), 252–261; published online 10 February 2012. DOI 10.1080/17442508.2011.651215; arXiv 0909.5325. Downloaded random_appetites.json (PDF bytes), random_appetites.txt. The fetched latest version is arXiv v6, 12 November 2021. Its Theorem 3.1, PDF page 5, gives small-appetite nonpercolation with diameter moments in (i) and small-appetite vacant percolation in (ii), under random-appetite moment assumptions. This generalizes the small-appetite results; it supplies no verified missing near-one regime solution. The revised arXiv statement is not silently identified with the 2013 printed version.

Hoffman, Holroyd, Peres, "Tail Bounds for the Stable Marriage of Poisson and Lebesgue", Canadian Journal of Mathematics 61(6) (2009), 1279–1299. DOI 10.4153/cjm-2009-060-7; arXiv math/0507324. Located via Crossref; not used as an unchecked percolation theorem.

## Brain and prior attempts (read only)
Math recall query: "Freire Popov Vachkovskaia stable marriage percolation". Returned off-topic Hall-marriage cards, no applicable theorem.
Memory recall: "stable marriage Poisson Lebesgue percolation mistakes". Returned no applicable stable-allocation result.
Read intake F0085-A001 in probability_1000_intake_F_20260908/attempts.jsonl, and F0085 problem record. Two errors: it missed FPV Theorem 1.1(ii); it said appetite monotonicity fails, contrary to HHP Proposition 22 and FPV page 4. Its proposed uniform deterministic radius domination is false (ATTEMPT Proposition E). Its chain estimate was explicitly unproved and has not been reused.
Searched codex_pool_2026_10_10 jsonl files for F0085: no match. Initial PowerShell glob passed to rg was invalid; repeated with explicit directory enumeration. Read-only git ls-tree of origin/master followed by F0085/f0085 filter found no matching path. No repository changed.

## Search log
All requests were Python urllib HTTP reads, no built-in web search. Raw responses retained; failures are not negative search results. OpenAlex returned HTTP 429 on every attempt, including source identification and citing-work queries. The W2161642397 citation filter was only a candidate identifier from Semantic Scholar MAG metadata, not an OpenAlex-verified identity. Therefore the OpenAlex citing-source search is INCOMPLETE. Semantic Scholar's keyword search was rate limited, but DOI source-citations and arXiv follow-up citation requests succeeded. GitHub returned zero repositories for the recorded query. arXiv returned four entries; the stable Poisson graph paper concerns a different discrete graph model and was excluded.

- 2026-10-11 | source | https://arxiv.org/pdf/math/0505668 | HTTP 200, 1184928 bytes
- 2026-10-11 | arxiv | https://export.arxiv.org/api/query?search_query=all%3A%22stable%20marriage%22%20AND%20all%3Apercolation&max_results=30 | HTTP 200, 7003 bytes
- 2026-10-11 | openalex | https://api.openalex.org/works?search=Percolation%20stable%20marriage%20Poisson%20Lebesgue&per-page=30 | HTTP Error 429: Too Many Requests
- 2026-10-11 | crossref | https://api.crossref.org/works?query=Percolation%20stable%20marriage%20Poisson%20Lebesgue&rows=20 | HTTP 200, 170038 bytes
- 2026-10-11 | semantic | https://api.semanticscholar.org/graph/v1/paper/search?query=Percolation%20stable%20marriage%20Poisson%20Lebesgue&limit=20&fields=title,authors,year,externalIds,openAccessPdf | HTTP Error 429: 
- 2026-10-11 | github | https://api.github.com/search/repositories?q=%22stable%20marriage%22%20percolation | HTTP 200, 55 bytes
- 2026-10-11 | fpv | https://arxiv.org/pdf/math/0511186 | HTTP 200, 528218 bytes
- 2026-10-11 | gouere | https://arxiv.org/pdf/0712.3638 | HTTP 200, 316454 bytes
- 2026-10-11 | openalex_retry | https://api.openalex.org/works?search=stable%20marriage%20Poisson&per_page=50 | HTTP Error 429: Too Many Requests
- 2026-10-11 | openalex_source | https://api.openalex.org/works/https://doi.org/10.1214/009117906000000098 | HTTP Error 429: Too Many Requests
- 2026-10-11 | semantic_retry | https://api.semanticscholar.org/graph/v1/paper/ARXIV:math/0511186?fields=title,year,citations.title,citations.year,citations.externalIds | HTTP 200, 1372 bytes
- 2026-10-11 | arxiv_vacant | https://export.arxiv.org/api/query?search_query=all%3A%22stable%20marriage%22%20AND%20%28all%3Aunclaimed%20OR%20all%3Apercolation%29&max_results=100 | HTTP 200, 7044 bytes
- 2026-10-11 | openalex_citing | https://api.openalex.org/works?filter=cites:W2161642397&per-page=100 | HTTP Error 429: Too Many Requests
- 2026-10-11 | openalex_doi | https://api.openalex.org/works?filter=doi:https://doi.org/10.1214/009117906000000098&per-page=1 | HTTP Error 429: Too Many Requests
- 2026-10-11 | semantic_source_citing | https://api.semanticscholar.org/graph/v1/paper/DOI:10.1214/009117906000000098/citations?fields=title,year,externalIds&limit=100 | HTTP 200, 23085 bytes
- 2026-10-11 | crossref_unclaimed | https://api.crossref.org/works?query=stable%20marriage%20unclaimed%20percolation&rows=30 | HTTP 200, 105609 bytes
- 2026-10-11 | random_appetites | https://arxiv.org/pdf/0909.5325 | HTTP 200, 168498 bytes

- 2026-10-11 | arxiv_allocation | https://export.arxiv.org/api/query?search_query=%28all%3A%22stable%20allocation%22%20OR%20all%3A%22stable%20marriage%22%29%20AND%20%28all%3Avacant%20OR%20all%3Aunclaimed%20OR%20all%3Apercolation%29&max_results=100 | HTTP 200; four entries, same relevant papers as the first query.

Semantic Scholar source citation endpoint returned 92 records with no next page. Titles were screened; the relevant direct follow-ups were FPV, Gouéré, and Díaz-Pachón, already recorded above. Citation lists may be incomplete; titles alone are not theorem verification.
Memory topic recall also run: "stable marriage Poisson Lebesgue percolation"; no applicable result.


## Second-attempt source and brain checks (2026-10-11)
Source theorem locators were verified directly against source.pdf page text. HHP Theorems 4 and 5 are on PDF page 5 (the earlier phase-theorem page-4 locator has been corrected); Theorems 6 and 7 on PDF page 6; Theorem 24 on PDF page 24; Propositions 21 and 22 on PDF page 21.
HHP Theorem 6(ii), PDF page 6, verbatim:
> A.s. every site is coveted by infinitely many centers.
Its hypotheses are Poisson centres with λ=α=1. This is an INPUT to our compact-cover deduction, not a printed resolution of near-one vacant percolation.
HHP Theorem 7, PDF page 6, verbatim:
> (i) For d = 1,2 and α = 1, we have EX^{d/2} = ∞.
> (ii) For d ≥ 3 and α = 1, we have EX^d = ∞.
These are critical TRANSPORT moment lower bounds, not territory-radius tail upper bounds or a percolation theorem. The second attempt uses exactly these moments to obstruct fast localization of compact-cover certificates.
Read-only math-store query: "stable marriage unclaimed vacant percolation near critical appetite Freire Popov Vachkovskaia". Returned Hall marriage, Russo, bootstrap and generic critical-percolation cards, no applicable stable-allocation theorem.
Read-only named-result query: "Liggett Schonmann Stacey domination finite range dependent percolation". Returned Dewan–Muirhead, arXiv 2102.12123, and provisional card claim_0648eaf12b0e1ff97b579f46ffa55e72471594ad7ab5aab54e15733a1eec6706. Walked that card with --id. Its local-anchor claim is not taken as checked and is not used in any proof. The new heavy-tail obstruction is instead proved directly from HHP Theorem 7. No LSS or neighbouring sharp-threshold theorem is invoked without checking its hypotheses; K is a self-contained finite-range Peierls deduction.
No new web request was needed for the pursued source-based route. The alternative planar Harris-FKG/sharp-threshold approach is recorded as an unverified lead, not a solution in print.

2026-10-12: Completed the second source-based deduction audit. No additional paper is claimed to resolve the gap; compact coverage and certificate bounds are our fully written implications, not quoted solutions in print.
