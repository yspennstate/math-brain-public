# Literature check: C0036

Date: 2026-10-12 Asia/Jerusalem (2026-10-11 UTC at retrieval).
Outcome: no matching solution found in the material successfully retrieved. This is not a definitive claim that no solution exists. OpenAlex and Semantic Scholar returned HTTP 429, so source citation coverage is incomplete. No SOLVED_IN_LITERATURE verdict is warranted.

## Verified primary source

Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures*, Proceedings of the International Congress of Mathematicians, Seoul 2014, vol. III, pp. 137–161; arXiv:1406.2707v1 (10 June 2014). Retrieved https://arxiv.org/pdf/1406.2707; saved as lyons2014.pdf and lyons2014.txt. Conjecture 5.7 is on printed/PDF page 23.

The preceding paragraph says: “Write FK(Q) := exp tr log |Q| for the Fuglede-Kadison determinant of Q when Q is a Γ-equivariant operator. The following would extend Theorem 5.2. It is open even for finite groups.”

Exact conjecture wording (mathematical subscripts typeset in Markdown):

> Conjecture 5.7. For all Γ-equivariant positive contractions Q on ℓ²(Γ), the process P_Q stochastically dominates product measure P_{FK(Q)I} and is stochastically dominated by product measure P_{I−FK(I−Q)I}, and these bounds are optimal.

The positive contraction is self-adjoint, 0<=Q<=I; the Γ action is the regular translation action, and the normalized group trace is evaluated at the identity. The conjecture has no invertibility requirement. Section 5.2 begins in a sofic-group setting; the conjecture sentence itself does not repeat this restriction. The requested all-group version is at least as strong, and neither version is solved in this attempt.

## Search log (every API request)

- Service: arxiv; query: Fuglede Kadison determinantal; UTC date: 2026-10-11T21:53:06.392290+00:00.
  URL: https://export.arxiv.org/api/query?search_query=all:%22Fuglede%22+AND+all:%22determinantal%22&max_results=40
  Result: HTTP 200; saved arxiv_0.raw
- Service: arxiv; query: Lyons stochastic domination determinantal; UTC date: 2026-10-11T21:53:09.349295+00:00.
  URL: https://export.arxiv.org/api/query?search_query=all:%22determinantal%22+AND+all:%22domination%22&max_results=60&sortBy=submittedDate&sortOrder=descending
  Result: HTTP 200; saved arxiv_1.raw
- Service: OpenAlex; query: Fuglede Kadison determinantal; UTC date: 2026-10-11T21:53:09.575378+00:00.
  URL: https://api.openalex.org/works?search=Fuglede%20Kadison%20determinantal&per-page=40
  Result: HTTP Error 429: Too Many Requests
- Service: OpenAlex; query: Determinantal probability basic properties conjectures; UTC date: 2026-10-11T21:53:14.139144+00:00.
  URL: https://api.openalex.org/works?search=Determinantal%20probability%20basic%20properties%20conjectures&per-page=5
  Result: HTTP Error 429: Too Many Requests
- Service: Crossref; query: Fuglede Kadison determinantal; UTC date: 2026-10-11T21:53:14.129071+00:00.
  URL: https://api.crossref.org/works?query=Fuglede%20Kadison%20determinantal&rows=30
  Result: HTTP 200; saved Crossref_4.raw
- Service: SemanticScholar; query: Fuglede Kadison determinantal; UTC date: 2026-10-11T21:53:14.130104+00:00.
  URL: https://api.semanticscholar.org/graph/v1/paper/search?query=Fuglede%20Kadison%20determinantal&limit=30&fields=title,authors,year,url,abstract
  Result: HTTP Error 429: 
- Service: GitHub; query: Fuglede Kadison determinantal; UTC date: 2026-10-11T21:53:14.140058+00:00.
  URL: https://api.github.com/search/repositories?q=Fuglede+Kadison+determinantal
  Result: HTTP 200; saved GitHub_6.raw
- Service: GitHub; query: determinantal stochastic domination; UTC date: 2026-10-11T21:53:14.146917+00:00.
  URL: https://api.github.com/search/repositories?q=determinantal+stochastic+domination
  Result: HTTP 200; saved GitHub_7.raw
- Service: OpenAlex; query: source DOI lookup; UTC date: 2026-10-11T21:59:39.648953+00:00.
  URL: https://api.openalex.org/works/https://doi.org/10.4310/ICM.2014.v3.21
  Result: HTTP Error 429: Too Many Requests
- Service: OpenAlex; query: citing arxiv source via DOI; UTC date: 2026-10-11T21:59:39.650370+00:00.
  URL: https://api.openalex.org/works?filter=cites:W2102466745&per-page=200
  Result: HTTP Error 429: Too Many Requests
- Service: SemanticScholar; query: source arXiv and citation metadata; UTC date: 2026-10-11T21:59:39.651193+00:00.
  URL: https://api.semanticscholar.org/graph/v1/paper/ARXIV:1406.2707?fields=title,year,citations.title,citations.year,citations.externalIds
  Result: HTTP Error 429: 
- Service: Crossref; query: determinantal stochastic domination; UTC date: 2026-10-11T21:59:39.651933+00:00.
  URL: https://api.crossref.org/works?query=determinantal%20stochastic%20domination&rows=30
  Result: HTTP 200; saved followup_3.raw
- Service: arxiv; query: determinantal product measures; UTC date: 2026-10-11T21:59:40.610441+00:00.
  URL: https://export.arxiv.org/api/query?search_query=all:%22determinantal%22+AND+all:%22product+measure%22&max_results=70
  Result: HTTP 200; saved followup_4.raw
- Service: arxiv; query: Lyons conjecture 5.7; UTC date: 2026-10-11T21:59:40.616104+00:00.
  URL: https://export.arxiv.org/api/query?search_query=all:%22Lyons%22+AND+all:%22conjecture%22+AND+all:%22determinantal%22&max_results=70
  Result: HTTP 200; saved followup_5.raw

Citation-search caveat: source-title lookup in OpenAlex was rate limited, preventing verification of an OpenAlex work ID. The later W2102466745 filter was an unverified diagnostic ID and also returned 429; it is NOT evidence about citations of Lyons. Likewise the source DOI lookup was not verified because of 429. The valid arXiv-keyed Semantic Scholar source/citation request was also rate limited. We did not retrieve a verified list of works citing the source.

## Relevant works and why they do not settle this question

1. Russell Lyons and Jeffrey E. Steif, *Stationary determinantal processes: Phase multiplicity, Bernoullicity, entropy, and domination*, Duke Mathematical Journal 120(3) (2003), 515–575. DOI 10.1215/S0012-7094-03-12032-3; arXiv:math/0204324. Source Theorem 5.2, p.22, quotes the sharp geometric-mean comparisons for scalar symbols f:T^d->[0,1] and Γ=Z^d. This is the known special case, not arbitrary Γ. Both the source bibliography and current Crossref results confirm the reference.

2. Russell Lyons and Andreas Thom, *Invariant Coupling of Determinantal Measures on Sofic Groups*, arXiv:1402.0969 (2014). Current arXiv abstract and source bibliography read. It compares equivariant kernels under Q1<=Q2 and produces invariant couplings. FK(Q)I<=Q need not hold (FK lies between extreme eigenvalues), so this does not give the requested bounds.

3. Raghavendra Tripathi, *Determinantal Processes and Stochastic Domination*, M.S. thesis, Indian Institute of Science (2019); arXiv:2009.09141v1 (19 September 2020), 60 PDF pages. Abstract and full-text theorem/keyword passages inspected; PDF and extraction saved. It studies projection-kernel domination and comparisons under different reference measures, with last-passage-percolation applications. No Fuglede-Kadison product bound or matching theorem found.

4. Tim Austin, *Entropy and determinants for unitary representations*, arXiv:2412.13751v4 (20 March 2026; first submitted 18 December 2024), 80 pages. Abstract and full-text relevant passages inspected; PDF and extraction saved. It provides FK formulas for representation-theoretic entropy and noncommutative Szegő limits. No determinantal point-process stochastic domination theorem matching this question found.

5. Alexander I. Bufetov, Yanqi Qiu and Alexander Shamov, *Kernels of conditional determinantal measures and the proof of the Lyons–Peres Conjecture*, arXiv:1612.06751v3. Current arXiv abstract inspected: Theorem 1.5 establishes completeness of sampled reproducing kernels; Theorem 1.7 concerns tail triviality. These are different conjectures, not Conjecture 5.7.

6. Justin Cyr, *Stationary Determinantal Processes on Z^d with N Labeled Objects per Site, Part I: Basic Properties and Full Domination*, Journal of Theoretical Probability (online 2 January 2021), DOI 10.1007/s10959-020-01062-5. Crossref title/author/DOI metadata retrieved. This is a lead for matrix-valued symbols on Z^d; no full-text theorem was verified, and no general-group solution is inferred from the title.

7. Guillaume Baverez, Alexander I. Bufetov and Yanqi Qiu, *A survey on determinantal point processes*, Advanced Studies in Pure Mathematics 87 (2021), DOI 10.2969/aspm/08710059. Crossref metadata retrieved. A survey lead, not a verified solution.

arXiv query totals and full abstracts are retained in the raw Atom files. Irrelevant hits (quantum chemistry, algebraic determinantal ideals, etc.) were not treated as leads. GitHub repository searches returned zero items. Crossref Fuglede–Kadison results chiefly concerned operator determinants/entropy, without the stochastic domination objects.

## Read-only brain and earlier private work

Read math-store card claim_1e3f205f561f7c54656563b1c8fea5afca86c07c42b7412bde1de30d0bb243cb in full; recalled “determinantal stochastic domination mistakes” and “Fuglede Kadison determinantal processes”. The card is a private harmonic-mean draft, not independent literature.

Searched C0036 in the intake ledgers and codex_pool_2026_10_10. Read team_O/w343/C0036_proof.md (two-site result and finite necessary bounds). Read-only git origin/master was searched for C0036; no working tree modification was made. Read these origin/master files:
- research7_2026-09-17/R7-03/artifacts/2026-09-19/2026-09-19T224000Z__C0036_z6_spectral_mixture_local_periodic.md
- research7_2026-09-17/R7-03/artifacts/2026-09-20/2026-09-20T152000Z__C0036_full_S3_eventwise_subgroup_cover.md
The first reports cardinality comparison, lower-order cyclic work, a local Hessian and periodic lifting. The second labels a full S3 proof as a candidate requiring exact symbolic certificates and independent review. Neither is a published all-group resolution; neither was used here as a proved premise. Their mathematical proposals are leads for future checking.

## Additional attempt, 2026-10-12 local

Read ATTEMPT.md in full. New read-only math-store requests:

- Query: `determinantal stochastic domination subgroup Schur complement increasing events`.
- Query: `Russo formula pivotal influence scalar determinantal perturbation`.
- Full card walk: `claim_569ccbdb68319948c30d7d0358dc8c699ed1907ce85a36c356879bd884bd847d` (Margulis–Russo formula).

The first request returned definitions and Schur/harmonic-mean hints, not a solution.
The second supplied the finite product-measure influence formula and warned
against applying it unchanged to a dependent process. The full card cites
Margulis (1974), Russo (1981), and Grimmett's *Percolation*, 2nd edition (1999),
Section 2.4. These citations were brain hints; no new full-text theorem from
those works is claimed verified in this pass. The particular finite Russo
identity needed here is proved directly from the multilinear polynomial in
SECOND_ATTEMPT.md. The DPP derivative is computed separately by determinants.
No new online solution is claimed, and the previous literature-coverage caveats
remain in force.
