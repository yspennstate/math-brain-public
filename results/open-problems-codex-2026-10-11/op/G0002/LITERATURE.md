# G0002 source verification and literature search (2026-10-11)

The retrieved 708-page PDF is Raphael Cerf, *theta(p_c,Z^d)=0?*, arXiv:2608.23661v1 (2026). Conjecture 53.1 is on PDF/printed page 398, not the intake locator 407. Definitions: (49.1), p.373; (51.1), p.391; (52.1), p.394.

Exact conjecture (mathematical notation transcribed): "Let n >= 1 be fixed. If A* is an increasing subset of {0,1}^n which realizes the maximum of phi_{2\\1} or of phi_2, then {omega: sum omega(i) >= n/2+1} subset A* subset {omega: sum omega(i) >= n/2-2}."

Important correction to intake: phi_2 and phi_{2\\1} sum over omega IN A, not all configurations. P_k^+ consists of coordinate indices, not k-element sets. First pivotality is tested by setting the coordinate to 0 versus 1; it can hold even when that coordinate is initially 0. The literal (49.1) can give initially zero higher pivots, but the source's small-case tables match an occupied-coordinate restriction. Example: OR on two coordinates gives phi_2=6 literally, 4 after that restriction. ATTEMPT.md uses bounds valid for BOTH interpretations, so this discrepancy does not affect the refutation.

Section 62, pp.448-453, is a decisive lead already IN THE SOURCE. It adapts Talagrand's random conjunctive construction and claims P(|P_2^+|>=cn)>=c for large n. Proposition 62.1, p.453, reads: "There exists a positive constant c such that, for any n >= 1, M_2(n) = max { phi_2(A) : A increasing subset of {0,1}^n } >= cn." As printed, this lacks a 2^n factor relative to the preceding argument and is too weak to contradict the band bound. There are also sample-position versus coordinate-index ambiguities and repeated-coordinate issues in the derivation. It does NOT state and prove Conjecture 53.1 as posed, and is NOT classified SOLVED_IN_LITERATURE. The independent argument in ATTEMPT.md repairs these issues and gives a finite refutation.

Related reference recovered through Crossref: Raphael Cerf, "The Pivotal Set of a Boolean Function", American Mathematical Monthly, DOI 10.1080/00029890.2025.2459044; preprint arXiv:2405.19541. First-order results, not a resolution of this question.

Read-only prior evidence: intake G, G0002-A001 warned of incorrect pair normalization; origin/master:operations/claims/G0002.md and R09 handoff references left Delta_8 unmeasured because definitions were unavailable. These are hints only.

## Search audit

All URLs, dates, response sizes and errors are in search_log.json; raw successful responses are the corresponding .txt files. Shell Python urllib was used, no built-in web search.

- arXiv: second-order AND pivotal, first 20 of 88 results: returned mostly unrelated statistics/physics/optimization items. This first page alone is not exhaustive negative evidence.
- arXiv: au:Cerf AND submittedDate 20260801 through 20261012: five results, source plus unrelated authors named Cerf; no matching solution identified.
- arXiv: source identifier OR pivotal AND Raphael_Cerf: zero returned entries (the author syntax may be too restrictive).
- Crossref: second order pivotal Cerf, 10 results: above first-order Cerf paper; remaining results unrelated.
- Crossref: 2608.23661, 5 results: unrelated numeric matches.
- GitHub repositories: pivotal AND Cerf; and exact 2608.23661: zero results each.
- OpenAlex works search 2608.23661: HTTP 429. Retry theta Cerf: HTTP 429. Citing-works request cites:doi:10.48550/arXiv.2608.23661: HTTP 429 before a usable response; no citation list obtained and the filter could not be validated.
- Semantic Scholar paper by ARXIV:2608.23661 including citations: HTTP 429. Search second order pivotal Cerf: HTTP 429.

Conclusion: no paper proving this exact question was identified in the bounded searches. Two services remained inaccessible. This is not a claim of an exhaustive literature search.

Source bibliography [125], p.708: Michel Talagrand, "How much are increasing sets positively correlated?", Combinatorica 16 (1996), no.2, 243-258. This is the construction lead, not a printed theorem resolving Conjecture 53.1.

Exact cached Crossref metadata for the related first-order paper: {"title": ["The Pivotal Set of a Boolean Function"], "author": [{"ORCID": "https://orcid.org/0000-0001-8552-5313", "authenticated-orcid": false, "given": "Raphaël", "family": "Cerf", "sequence": "first", "affiliation": [], "role": [{"role": "author", "vocabulary": "crossref"}]}], "container-title": ["The American Mathematical Monthly"], "volume": "132", "issue": "5", "page": "414-429", "published": {"date-parts": [[2025, 3, 26]]}, "DOI": "10.1080/00029890.2025.2459044"}
