# E0007 literature and status search — 2026-10-12

No exact published solution verified. This bounded search is not evidence that no solution exists.

## Source confirmed

Rick Durrett, Coexistence in stochastic spatial models, The Annals of Applied Probability 19(2) (2009), 477–496. DOI: 10.1214/08-AAP590. arXiv:0906.2293v1. Problem 1, PDF p. 3 (downloaded source.pdf, extracted source.txt). The initial 09-PS139 DOI lookup was erroneous; later lookups used the confirmed DOI.

> Problem 1. Show that species 1 outcompetes species 2 holds if the dispersal distributions are the same and β1/δ1 > β2/δ2. The simulation in Figure 2 gives some support for this conjecture.

The model is defined on Z^2 on PDF pp. 1–2. Birth rates are total individual rates with offspring displacement probabilities p_i(y), and only vacant destinations accept births. Preceding Theorem 1, PDF p. 2, defines exclusion as P(ξ_t(x)=2)→0 for translation-invariant initial law with P(ξ_0(x)=1)>0. No irreducibility, symmetry, range, or initial ergodicity hypothesis is explicit in Problem 1. The literal initial-law mixture issue is explained in ATTEMPT.md.

## All online requests

The URLs below preserve every query, service, date, HTTP outcome and response filename. Rate-limited requests are failures, not negative search results. The OpenAlex source lookup succeeded with work ID W2057281188; citing-work requests were made but rate limited. Semantic Scholar citing-source request succeeded, returning 27 records. GitHub returned one repository; it is not a mathematical proof.

- 2026-10-12 — https://arxiv.org/pdf/0906.2293 — 200 — source.pdf
- 2026-10-12 — https://export.arxiv.org/api/query?search_query=all:%22contact%20process%22%20AND%20all:%22death%20rates%22&max_results=30 — 200 — arxiv.xml
- 2026-10-12 — https://api.openalex.org/works?search=multitype%20contact%20process%20unequal%20death%20rates&per-page=30 — 429 — openalex.json
- 2026-10-12 — https://api.crossref.org/works?query=multitype%20contact%20process%20unequal%20death%20rates&rows=20 — 200 — crossref.json
- 2026-10-12 — https://api.semanticscholar.org/graph/v1/paper/search?query=multitype%20contact%20process%20unequal%20death%20rates&limit=20&fields=title,year,authors,url,abstract — 429 — semantic.json
- 2026-10-12 — https://api.github.com/search/repositories?q=multitype+contact+process — 200 — github.json
- 2026-10-12 — https://api.openalex.org/works/https://doi.org/10.1214/09-PS139 — 429 — openalex_source.json
- 2026-10-12 — https://api.openalex.org/works?search=competing%20contact%20process&per_page=50 — 429 — openalex_retry.json
- 2026-10-12 — https://api.semanticscholar.org/graph/v1/paper/ARXIV:0906.2293/citations?limit=100&fields=title,year,authors,abstract — 200 — semantic_retry.json
- 2026-10-12 — https://export.arxiv.org/api/query?search_query=all:%22multitype%20contact%22&max_results=50 — 200 — arxiv_target.xml
- 2026-10-12 — https://api.crossref.org/works?query=%22contact%20process%22%20%22unequal%22&rows=30 — 200 — crossref_target.json
- 2026-10-12 — https://api.openalex.org/works?filter=cites:W2057281188&per_page=100 — 429 — openalex_citing.json
- 2026-10-12 — https://api.openalex.org/works/doi:10.1214/08-AAP590 — 200 — openalex_source_retry.json
- 2026-10-12 — https://api.openalex.org/works?filter=cites:W2057281188&per-page=100 — 429 — openalex_citing_retry.json
- 2026-10-12 — https://export.arxiv.org/api/query?search_query=ti:%22Voter%20Model%20Perturbations%22&max_results=10 — 200 — voter.xml
- 2026-10-12 — https://export.arxiv.org/api/query?search_query=all:%22quasi-neutral%20contact%20process%22&max_results=10 — 200 — slow.xml
- 2026-10-12 — https://arxiv.org/pdf/1803.01533 — 200 — asymmetric.pdf
- 2026-10-12 — https://arxiv.org/pdf/2602.23149 — 200 — interface.pdf
- 2026-10-12 — https://api.openalex.org/works?filter=cites:W2057281188&per_page=25&select=id,title,publication_year,doi — 429 — openalex_citing_final.json
- 2026-10-12 — https://export.arxiv.org/api/query?search_query=all:%22competitive%20exclusion%22%20AND%20all:%22contact%22&max_results=100 — 200 — arxiv_exclusion.xml
- 2026-10-12 — https://api.semanticscholar.org/graph/v1/paper/ARXIV:1908.06628/citations?limit=100&fields=title,year,authors,abstract — 200 — semantic_stover.json

## Candidate references and disposition

Joseph P. Stover, A stochastic comparison result for the multitype contact process with unequal death rates, Statistics & Probability Letters 162 (2020), 108763. DOI 10.1016/j.spl.2020.108763; arXiv:1908.06628v2 (17 May 2021). Full text downloaded as comparison.pdf and comparison.txt. Proposition 2.1, PDF pp. 4–5, concerns coordinatewise favorable birth and death rates. Theorem 2.2, PDF p. 5, gives a sufficient inequality involving λ(β,c,α)>λ_c for strong survival from one particle against an all-opponent background. It does not assert type-opponent density tends to zero and does not cover all ratio-ordered parameters. Theorem 2.2 is therefore a lead, not SOLVED_IN_LITERATURE. Per-neighbor birth rates in this paper must be multiplied by 2d to match Durrett's total-rate convention. Its introduction explicitly labels the birth/death ratio assertion a conjecture.

Thomas Mountford, Pedro Luis Barrios Pantoja, Daniel Valesin, The asymmetric multitype contact process, Stochastic Processes and their Applications 129(8) (2019), 2783–2820. DOI 10.1016/j.spa.2018.08.006; arXiv:1803.01533v1. Downloaded asymmetric.pdf/txt. Theorems 1.1 and 1.2, PDF pp. 2–3, prove survival/takeover and complete convergence under birth-rate ordering; the generator and introduction on PDF p. 1 explicitly set BOTH death rates to 1. Thus these are equal-death special cases, not an answer to unequal-death ratio ordering. It clarifies the initial-state quantifier: convergence from arbitrary states includes a component with only type 2 when type 1 becomes extinct.

Isabella Alvarenga and Daniel Valesin, Interface for variants of the contact process, arXiv:2602.23149v1 (26 February 2026). Downloaded interface.pdf/txt. Theorems 4 and 5, PDF p. 4, concern one-dimensional Heaviside initial states and interface tightness/CLT. The same page explicitly says every occupied site dies at rate 1. Different initial states/dimension and equal death rates; not a solution.

Marcelo Martins de Oliveira and Ronald Dickman, The advantage of being slow: the quasi-neutral contact process, Physical Review E 96 (2017), 032113; arXiv:1705.03819v2. Abstract checked via arXiv API (slow.xml). It concerns equal birth/death ratios, extinction advantage in finite spatial systems, and environmental variation. No full-text theorem verified; numerical/finite-size lead, not a counterexample to infinite-volume strict ratio ordering.

J. Theodore Cox, Richard Durrett and Edwin A. Perkins, Voter model perturbations and reaction diffusion equations, Astérisque 349 (2013); arXiv:1103.1676v1. Abstract checked through voter.xml; focuses on two-state voter perturbations in d≥3 (Lotka–Volterra/cooperation/nonlinear voter examples), not the entire three-state competing contact-process parameter space on Z^2. A potential technique, not an exact-match theorem.

Claudia Neuhauser, Ergodic theorems for the multitype contact process, Probability Theory and Related Fields 91 (1992), 467–506. DOI 10.1007/BF01192067. Metadata verified with Crossref; equal-death theorem quoted by the original source and discussed in the two full-text later papers. Not an unequal-death solution.

Other returned arXiv entries include contact processes with seasons, frozen/sterile states, mutating species, symbiosis, density-dependent births, allelopathy, and tree coexistence. Those change the model or parameter hypotheses. Their exact titles/authors/IDs are retained below to keep search results auditable.

- Joseph P. Stover. A stochastic comparison result for the multitype contact process with unequal death rates. http://arxiv.org/abs/1908.06628v2; 2019-08-19T07:39:46Z.
- Sergey Pirogov, Elena Zhizhina. Invariant measures for contact processes with state dependent birth and death rates. http://arxiv.org/abs/2304.14237v1; 2023-04-27T14:55:07Z.
- B. Chan, R. Durrett, N. Lanchier. Coexistence for a multitype contact process with seasons. http://arxiv.org/abs/0910.4014v1; 2009-10-21T08:19:01Z.
- J. Theodore Cox, Rinaldo B. Schinazi. Survival and coexistence for a multitype contact process. http://arxiv.org/abs/0906.4845v1; 2009-06-26T06:20:08Z.
- Rick Durrett, Dong Yao. The Symbiotic Contact Process. http://arxiv.org/abs/1904.02213v2; 2019-04-03T19:29:26Z.
- Benjamin Chan, Richard Durrett. A new coexistence result for competing contact processes. http://arxiv.org/abs/math/0610179v1; 2006-10-05T12:09:48Z.
- Jonas Köppl, Nicolas Lanchier, Max Mercer. Evolutionary games on the lattice: multitype contact process with density-dependent birth rates. http://arxiv.org/abs/2412.19957v1; 2024-12-27T23:53:34Z.
- Marcelo M. de Oliveira, Sidiney G. Alves, Silvio C. Ferreira. Dynamical correlations and pairwise theory for the symbiotic contact process on networks. http://arxiv.org/abs/1909.03981v3; 2019-09-09T16:42:29Z.
- Jonas Köppl, Nicolas Lanchier, Max Mercer. Survival and extinction for a contact process with a density-dependent birth rate. http://arxiv.org/abs/2404.09944v2; 2024-04-15T17:14:19Z.
- Marcelo Martins de Oliveira, Renato Vieira Dos Santos, Ronald Dickman. A symbiotic two-species contact process. http://arxiv.org/abs/1205.5974v1; 2012-05-27T15:05:48Z.
- Jaewook Joo, Joel L. Lebowitz. Population Dynamics in Spatially Heterogeneous Systems with Drift: the generalized contact process. http://arxiv.org/abs/cond-mat/0412180v2; 2004-12-08T07:18:38Z.
- Marcelo M. de Oliveira, Ronald Dickman. Phase diagram of the symbiotic two-species contact process. http://arxiv.org/abs/1407.1884v2; 2014-07-07T20:56:22Z.
- Rinaldo B. Schinazi. An inhomogeneous contact process model for speciation. http://arxiv.org/abs/1305.2625v1; 2013-05-12T19:53:47Z.
- Thomas M. Liggett. Conditional Association and Spin Systems. http://arxiv.org/abs/math/0507392v1; 2005-07-19T15:28:31Z.
- Konstantin Klemm, Nagi Khalil. Altruism in populations at the extinction transition. http://arxiv.org/abs/1906.04202v2; 2019-06-10T18:01:50Z.
- S. Pirogov, E Zhizhina. Persistence in perturbed contact models in continuum. http://arxiv.org/abs/2605.00148v1; 2026-04-30T19:11:26Z.
- Guilherme S. Costa, Marcelo M. de Oliveira, Silvio C. Ferreira. Heterogeneous mean-field theory for two-species symbiotic processes on networks. http://arxiv.org/abs/2203.09500v3; 2022-03-17T17:50:29Z.
- Nicolas Lanchier, Max Mercer. Durrett-Levin spatial model of allelopathy. http://arxiv.org/abs/2305.17016v1; 2023-05-26T15:23:12Z.
- Nicolas Lanchier. Multitype Contact Process with Frozen states. http://arxiv.org/abs/math/0401353v1; 2004-01-26T15:53:14Z.
- Thomas Mountford, Pedro Luis Barrios Pantoja, Daniel Valesin. The asymmetric multitype contact process. http://arxiv.org/abs/1803.01533v1; 2018-03-05T07:45:26Z.
- Thomas Mountford, Daniel Valesin. Functional central limit theorem for the interface of the multitype contact process. http://arxiv.org/abs/1509.04339v1; 2015-09-14T21:51:24Z.
- Nicolas Lanchier. Two-scale multitype contact process: coexistence in spatially explicit metapopulations. http://arxiv.org/abs/1003.0117v1; 2010-02-27T17:32:42Z.
- Nicolas Lanchier, Max Mercer, Hyunsik Yun. Multitype contact process with sterile states. http://arxiv.org/abs/2510.05397v1; 2025-10-06T21:43:43Z.
- Isabella Alvarenga, Daniel Valesin. Interface for variants of the contact process. http://arxiv.org/abs/2602.23149v1; 2026-02-26T16:13:47Z.
- Daniel Valesin. Multitype Contact Process on $\Z$: Extinction and Interface. http://arxiv.org/abs/1004.1958v1; 2010-04-12T13:56:23Z.
- Idan Alter, Gideon Amir. The Mutating Contact Process: Model Introduction and Qualitative Analysis of Phase Transitions in its Survival. http://arxiv.org/abs/1801.01530v1; 2018-01-04T19:57:01Z.
- Daniela Bertacchi, Fabio Zucca. Recent results on branching random walks. http://arxiv.org/abs/1104.5085v3; 2011-04-27T08:16:56Z.
- Hwai-Ray Tung, Rick Durrett. Competitive exclusion in a model with seasonality: three species cannot coexist in an ecosystem with two seasons. http://arxiv.org/abs/2210.00156v1; 2022-10-01T01:23:48Z.
- Joseph Stover. Attractive n-type contact processes. http://arxiv.org/abs/1006.5723v2; 2010-06-29T20:47:45Z.
- Nicolas Lanchier, Yuan Zhang. Some rigorous results for the stacked contact process. http://arxiv.org/abs/1410.3842v1; 2014-10-14T20:07:45Z.
- Davide Borrello. Stochastic order and attractiveness for particle systems with multiple births, deaths and jumps. http://arxiv.org/abs/1003.3548v3; 2010-03-18T10:55:55Z.
- Fabio Zucca. Survival, extinction and approximation of discrete-time branching random walks. http://arxiv.org/abs/1003.3671v4; 2010-03-18T20:03:54Z.
- Marcelo Martins de Oliveira, Ronald Dickman. The advantage of being slow: the quasi-neutral contact process. http://arxiv.org/abs/1705.03819v2; 2017-05-10T15:28:51Z.
- J. Theodore Cox, Richard Durrett, Edwin Perkins. Voter Model Perturbations and Reaction Diffusion Equations. http://arxiv.org/abs/1103.1676v1; 2011-03-09T00:48:30Z.
- J. Theodore Cox, Edwin A. Perkins. A complete convergence theorem for voter model perturbations. http://arxiv.org/abs/1210.0830v2; 2012-10-02T16:26:49Z.
- Ted Cox, Ed Perkins. A complete convergence theorem for the q-voter model and other voter model perturbations in two dimensions. http://arxiv.org/abs/2310.00812v2; 2023-10-01T22:55:32Z.

## Read-only local/brain searches

Called brain.py recall with "two-type contact process unequal death rates" and "contact process mistakes", and math_recall.py with "multitype contact process Neuhauser Durrett competitive exclusion". Results were largely irrelevant and are not mathematical evidence. The brain command reported an automatic cache-refresh attempt that failed; no brain write command was invoked.

Initial rg invocation on the literal Windows wildcard failed (rg does not expand it). Corrected with Path.glob over probability_1000_intake_* and a read-only search of .jsonl/.md/.json files in those directories and codex_pool_2026_10_10. No E0007 hits; saved prior_hits.txt. Read git ls-tree origin/master and filtered paths for E0007/unequal-death; no matching paths, saved repo_paths.txt. No working-tree changes or commits.

Search coverage is bounded: API result limits, missing newly indexed papers, rate limits, and title/keyword mismatches remain possible. No verdict SOLVED_IN_LITERATURE is claimed.

## Final citation check and additional fetch records

The final Semantic Scholar query for citations of arXiv:1908.06628 returned two records. They concern cooperative SIR on trees and general stochastic ordering of non-conservative particle systems; neither abstract states the ratio-exclusion result. These are abstract-level leads only. OpenAlex finally explained its HTTP 429 response as exhaustion of the unauthenticated shared-IP daily budget, so no citing-paper list could be inspected there.

- Ruibo Ma, Tai-Heng Liu, Baghdadi Othmane, Dong Yao. A note on the cooperative two-type SIR processes on Galton-Watson trees. 2025. Semantic Scholar paper ID c376fd721e5779c7feb1aeca3f92da63e4f45809.
- R. Gouet, F. López, Gerardo Sanz. Stochastic ordering, attractiveness and couplings in non-conservative particle systems. 2025. Semantic Scholar paper ID 112045f8e2adcdc29cae259b265dee94a7d63ff2.

Direct full-text/metadata fetches in inspect.py (2026-10-12): https://arxiv.org/pdf/1908.06628 (200, comparison.pdf); https://api.crossref.org/works/10.1007/BF01192067 (200, neuhauser_metadata.json).

The final arXiv competitive-exclusion/contact query returned only the seasonal-model and quasi-neutral finite-system papers already catalogued above. A further during-attempt math-store recall asked "Broman point process stochastic domination contact process"; output is retained in brain_followup.txt and is treated solely as hints.

## Second-attempt brain recall

2026-10-12, read-only math store calls:

- math_recall.py "multitype contact process unequal death rates vacancy correlation competitive exclusion"
- math_recall.py "Broman Stover contact process stochastic domination"

The first query asks directly about the remaining vacancy-correlation
gap. It returned generic IPS material and unrelated correlation,
queueing and branching cards, including claim_48be9b2fde60ef90775544c92dc25dd9,
claim_e72e75e02d0527594e059eccf53d2e760053821def0e437a4d1825a84a416179,
and claim_10d710827b89fea7a492417ab4897ceeeac651ddf0e4d26e7f75bc3739620e4e.
These do not provide a theorem controlling the needed two-type
correlation integral. The named-result query is also treated as hints,
not a verdict. No new online literature claim or novelty claim is made
in the second attempt; the earlier exact-match search limitations remain.

The named Broman/Stover query returned generic stochastic-domination
material (claim_6e108f8c5133f68c71bd2763fce36f07) and unrelated cards,
not a Broman/Stover theorem card. None of the returned cards supplies
the missing exclusion argument, and none is used as a proof premise.
