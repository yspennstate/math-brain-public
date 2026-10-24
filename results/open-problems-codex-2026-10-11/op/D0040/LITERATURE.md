# D0040 literature and source audit — 2026-10-12

## Status

No inspected result establishes the full nesting question as posed. This is a bounded search, not a proof of openness. OpenAlex and Semantic Scholar rate-limited both initial and follow-up requests. No SOLVED_IN_LITERATURE verdict is justified.

## Source verified from downloaded PDF

Bálint Virág, *Operator limits of random matrices*, ICM 2014 survey; arXiv:1804.06953 (2018 posting), https://arxiv.org/pdf/1804.06953. Saved as source.pdf and source.txt.

PDF p. 5 says: “A special property of the β-Hermite matrices √n T_n is that they are minors of each other; as a result, they are the minor of a semi-infinite Jacobi matrix J = J_β.” It explicitly says the numbering is reversed compared to (1).

Theorem 4.1, PDF p. 5: “There exists a random measure μ_β so that for all n the zeros of the orthogonal polynomial p_n with respect to μ_β are distributed as the eigenvalues of the n-point β-Hermite ensemble.” Mathematical subscripts are transcribed from PDF notation.

Question 2, PDF p. 6, exact wording: “Question 2 (Nested models). Can any other Dyson β-ensembles be coupled this way? How about other natural random matrix models?”

Thus √n scaling and reversal matter. Arbitrary size-dependent rescaling of an infinite array is not itself a leading-minor coupling. The surrounding theorem asks for a common random orthogonality measure, not merely separately sampled finite tridiagonal matrices. No independent-entry or independent-Dirichlet-weight requirement is imposed in Question 2. Both a strict leading-minor construction and the common-measure formulation are proved for the Laguerre special case in ATTEMPT.md.

On PDF p. 3, equation (3) defines Dyson's ensemble using exp(−β n tr V(A)) and a Vandermonde factor (with separate spectral-weight factors). Numerical constants differ from the Hermite convention in equation (2). The source does not spell out the allowed domains or size-dependent potentials in Question 2. Our general Laguerre weight has a fixed hard-edge power; it should not be described as a new smooth full-real-line V. At power zero, choose a=2/β−1: under λ=n x its normalized density is the fixed-potential half-line ensemble with V(x)=x/2. For quartic V, x=λ/n^{1/4} relates the normalized nV convention to our unscaled constant-weight convention. No assertion is made that nV matrices themselves, without that rescaling, are literal nested minors.

## Searches performed

All requests used Python urllib from the shell, with bounded network timeouts. Exact URLs and outcomes are preserved in search_log.jsonl; successful responses are local *.response files. Date: 2026-10-12 throughout.

| Service | Query/request | Result |
|---|---|---|
| arXiv API, HTTPS export | all:"beta ensembles" AND all:"minors", max_results=20 | Two papers, listed below |
| OpenAlex | works search “tridiagonal beta ensembles nested”, per-page=15 | HTTP 429 |
| OpenAlex | works search “Operator limits of random matrices” with locations.source.id filter, per-page=5 | HTTP 429; filter was unnecessarily restrictive, followed by unfiltered title lookup |
| Crossref | “nested tridiagonal beta ensembles”, rows=15 | Successful; mostly tangential results |
| Semantic Scholar | paper search “nested tridiagonal beta ensembles”, limit=15, requested abstracts | HTTP 429 |
| GitHub repositories | “tridiagonal beta ensembles” | Successful, zero repositories |
| OpenAlex | unfiltered works search “Operator limits of random matrices”, per-page=5 | HTTP 429 |
| OpenAlex | works lookup doi:10.48550/arXiv.1804.06953 | HTTP 429 |
| arXiv API, HTTP export | all:"nested" AND all:"beta" AND all:"ensembles", max_results=30 | Successful, zero entries |
| arXiv API, HTTPS export | all:"beta" AND all:"corners", max_results=30 | Successful; abstracts saved in arxiv_summaries.txt |
| arXiv API, HTTPS export | all:"Laguerre" AND all:"minors", max_results=20 | Successful; abstracts saved in arxiv_summaries.txt |
| Crossref | “beta corners process tridiagonal nesting”, rows=15 | Successful |
| Semantic Scholar | ARXIV:1804.06953 with citation titles, years and external IDs | HTTP 429 |

The OpenAlex citing-works request cannot yet be constructed from a verified OpenAlex source ID: both source-discovery routes returned 429. This is explicitly incomplete citation coverage, not a negative citation search.

A further direct citing-works request was attempted with filter cites:https://doi.org/10.48550/arXiv.1804.06953 and per-page=100. It also returned HTTP 429 before its filter semantics could be validated. This does not replace a successful source-ID citation lookup.

## Exact relevant references and what they do

* Ioana Dumitriu and Alan Edelman, “Matrix models for beta ensembles,” *Journal of Mathematical Physics* 43 (2002), 5830–5847, DOI 10.1063/1.1507823, arXiv:math-ph/0206043. PDF saved as dumitriu_edelman.pdf. Theorem 3.4, PDF p. 14, gives the Laguerre eigenvalue density for the bidiagonal Gram model and independent normalized-chi first-row eigenvector coordinates. It supplies the finite-size distribution theorem used in ATTEMPT.md. Its parameters differ from ours: their matrix size m is our n; their scalar a_DE is β(n+a)/2; their p is 1+β(n−1)/2. Hence a_DE−p=β(a+1)/2−1. Their unscaled eigenvalues are β times ours. Their independent first-row weights concern L L^T, and cannot be transferred without proof to our reversed L^T L array. This is a pre-source theorem and the nesting implication is derived here; it is not a paper explicitly resolving the full source question.

* Joseph Najnudel and Bálint Virág, “The bead process for beta ensembles,” arXiv:1904.00848 (2019). Retrieved by arXiv API. A multilevel/interlacing process is a lead, not automatically a single-tridiagonal leading-minor construction. Full-text inspection is recorded below when completed.

Full text downloaded as bead.pdf (47 pages) and extracted as bead.txt. Section 8, Proposition 19, explicitly gives a coupling of Gaussian beta ensembles in all dimensions, using the Hermite beta corner process. This remains the Gaussian case and uses an interlacing Markov chain; it is not a theorem providing another fixed-weight single-Jacobi model. Its discussion of orthogonal polynomials earlier in the paper concerns Schur functions and Verblunsky coefficients on the circle, rather than the required real-line Jacobi recurrence. Searches of the full text for tridiagonal/nested/coupling language identify no theorem answering the source's other-ensemble question.

* “Eigenvalue processes of symmetric tridiagonal matrix-valued processes associated with Gaussian beta ensemble,” arXiv:2204.00736, *Stochastic Processes and their Applications* (2023), DOI 10.1016/j.spa.2023.07.004. Retrieved by arXiv and Crossref. Its title concerns Gaussian models and dynamics; no result inspected so far answers the other-ensemble nesting question.

The arXiv metadata identifies the author as Satoshi Yabuoku. Its abstract describes independent Brownian diagonal and Bessel offdiagonal processes and eigenvalue SDEs involving indexed principal minors. This is Gaussian dynamics, not another fixed-weight nesting family.

* Alexei Borodin and Vadim Gorin, “General beta Jacobi corners process and the Gaussian Free Field,” arXiv:1305.3627v4 (first posted 2013). The inspected abstract establishes global fluctuation limits for a multilevel Jacobi extension via Macdonald processes. It does not assert a single random orthogonality measure or a positive three-term recurrence across all levels. It is also pre-source.

* Leonid Petrov and Jiaming Xu, “Perturbed Beta Corners Process,” arXiv:2607.27810v1, posted 2026-07-30. Abstract inspected. It constructs deformed interlacing arrays using multivariate Bessel functions and studies crystallization. This is a corners-process construction; no single-Jacobi recurrence claim appears in the inspected abstract. It is a lead rather than a verified solution.

* Matthew Lerner-Brecher, “On the hard edge limit of the zero temperature Laguerre beta corners process,” arXiv:2308.14707v1 (2023-08-28). Abstract inspected. It concerns a zero-temperature multilevel Laguerre limit and Gaussian fluctuations, not a finite-beta common orthogonality measure with all level laws.

* Cesar Cuenca, “Universal behavior of the corners of Orbital Beta Processes,” arXiv:1807.06134v2 (first posted 2018-07-16). Abstract inspected. It concerns orbital beta processes and Gaussian-corners universality, not strict tridiagonal nesting.

* “Stochastic domination in beta ensembles,” DOI 10.1063/5.0254593 (Crossref result). Domination is a possible coupling lead; it does not by itself produce the three-term polynomial recurrence required by one Jacobi array.

* “From superintegrability to tridiagonal representation of β-ensembles,” DOI 10.1016/j.physletb.2022.137038 (2022; Crossref result). Finite-size tridiagonal representation is not dimension consistency. No matching nesting theorem has been identified.

Additional exact API metadata remain in the downloaded responses; arxiv_summaries.txt and search_summary.txt give readable query outputs. No theorem from a later paper is quoted as a solution because none has been verified to prove this question with matching objects and quantifiers.

## Brain and earlier-record audit

Read-only calls requested: brain recall “tridiagonal beta ensembles nesting”; brain recall “random matrix minors mistakes”; math-store recall “Dumitriu Edelman beta Laguerre tridiagonal”. Math-store results were predominantly off-topic, so none is used as a mathematical premise. The mistakes recall warns to compare the SAME random sample when checking a transformation, which is followed in check_laguerre.py. The provided recall tool reported an automatic index-refresh attempt; no remember/write command was issued.

Local intake problems.jsonl and attempts.jsonl contain D0040-A001 (2026-09-08), whose claim that independence is necessary for nesting is false in general: consistency is a marginal identity, not independence. It also asserted Jacobi and CMV truncation consistency without checking terminal coefficients. Those assertions are not used. Local open_problems_200_2026_10_10 records still mark the question unverified. Read-only git origin/master search located a more focused Favard attempt; its contents are inspected separately before relying on it.

The inspected origin/master file runs/R15/20260918_0106Z_successor_admission_d0040_favard_q45e2c.md correctly distinguishes a common Jacobi recurrence from a generic corners process. Its elementary three-level counterexample is reproduced with a full polynomial calculation in ATTEMPT.md. Its literature and openness assertions remain hints; current API searches independently retrieved the Jacobi-corners and perturbed-corners leads.

## Additional attempt: exact searches and primary model verification

Date: 2026-10-12. The renewed attempt is written in SECOND_ATTEMPT.md. Two new approaches were explicitly recorded before pursuing the CS-angle construction. Math-store calls asked for the gap itself:

* `Jacobi ensemble canonical moments independent beta random orthogonal polynomials`
* `tridiagonal minor coupling spectral weights inverse eigenvalue Favard Dixon Anderson`
* `Edelman Sutton beta Jacobi CS decomposition`

The returned cards were generic orthogonal-polynomial definitions or off-topic results; none supplied a relevant nesting theorem or is used as a premise. No brain/store write command was issued.

Additional network requests (exact URLs/outcomes also saved in second_search_log.jsonl):

| Service | Query/request | Outcome |
|---|---|---|
| Crossref | “The beta Jacobi matrix model CS decomposition generalized singular value problems”, rows=5 | Correct Edelman–Sutton DOI and metadata retrieved |
| arXiv API | au:Sutton AND all:Jacobi, max_results=10 | Returned mostly unrelated large-collaboration papers; did not locate the required finite-model paper |
| arXiv PDF | math-ph/0607038 | Retrieved *From random matrices to stochastic operators*, not the initially sought Jacobi paper; identification checked from its first page |
| DOI resolver | 10.1007/s10208-006-0215-9 | Small HTML response, not the primary PDF |
| arXiv PDF | math/0410034 | Retrieved Killip–Nenciu *Matrix models for circular ensembles*; related finite-size model |
| Author website | https://math.mit.edu/~edelman/publications/betajacobi.pdf | HTTP 404 |
| Author website | https://math.mit.edu/~edelman/publications/beta-jacobi.pdf | Primary Jacobi PDF successfully retrieved, 262425 bytes; saved as beta_jacobi.pdf and extracted as beta_jacobi.txt |

**Primary reference used:** Alan Edelman and Brian D. Sutton, “The Beta-Jacobi Matrix Model, the CS Decomposition, and Generalized Singular Value Problems,” *Foundations of Computational Mathematics* 8(2), 259–285 (2008; Crossref online-publication date 2007-03-23), DOI https://doi.org/10.1007/s10208-006-0215-9. The cited page numbers refer to the author PDF fetched above.

Definition 1.6, PDF p. 7, spells out four bidiagonal blocks. The lower-right block B_22 has diagonal c_n s'_{n−1},c_{n−1}s'_{n−2},…,c_1 and subdiagonal −s_{n−1}c'_{n−1},…,−s_1c'_1. This is the block relevant to nesting. B_11 has a different boundary/orientation and must not be silently substituted.

Definition 1.8, PDF pp. 7–8, gives independent angle laws c_i²~Beta(β(a+i)/2,β(b+i)/2), (c'_i)²~Beta(βi/2,β(a+b+1+i)/2). These are exactly the coefficient laws used in the new construction, with a=r,b=s.

Theorem 4.1, PDF p. 17, begins verbatim:

> Theorem 4.1. Let β be any positive real number, let n be a positive integer, and let a, b > −1.

After displaying its CS decomposition, it states verbatim:

> The diagonal entries of C, squared, follow the law of the β-Jacobi ensemble with parameters a, b. Also, the first row of V1, up to sign, is distributed as a vector of i.i.d. χβ random variables, normalized to unit length.

The paper's first page defines this ensemble by exponents β(a+1)/2−1 and β(b+1)/2−1. Thus Theorem 4.1 covers the entire parameter range used here, without an analytic-continuation argument.

The complete reduction is in SECOND_ATTEMPT.md: B_22=U_2 C V_2^T has the same singular values as B_11; signed reversal/transposition identifies B_22 with the explicit lower bidiagonal factor; its Gram matrix has literal consistent leading blocks; boundedness gives one common random measure. The last all-size/common-measure steps are derived in this attempt. A finite-size theorem is not quoted as if it explicitly proves the broad Virág question. This is a pre-source classical-family special case, so SOLVED_IN_LITERATURE is not asserted.

**Other exact references retrieved:** Rowan Killip and Irina Nenciu, “Matrix models for circular ensembles,” arXiv:math/0410034 (2004); Alan Edelman and Brian D. Sutton, “From random matrices to stochastic operators,” arXiv:math-ph/0607038 (2006 posting). Neither is used to certify a general nesting classification here.
