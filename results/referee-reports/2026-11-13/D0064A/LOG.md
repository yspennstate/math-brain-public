# D0064 work log

Task: "Open problem D0064"; work began 2026-11-13 08:26 +04 (Asia/Tbilisi).

## 08:26 — scope and orientation

Read the supplied instructions, startup memory, brain index, mesh protocol and compute governor. No subagents. All task writes stay inside this directory; no publication or git pushes. The task-specific directory-only restriction prevents writes to the global mesh, task checklist and brain logs; use this local log as the task record, and read existing memory directly. No global state is changed. Source PDFs, when needed, will be streamed in memory to pdftotext, never saved. Computation will use nice 10 and a single numeric thread.

## Literature search — literature search started

Located Rhodes–Vargas arXiv:1305.6221, Allez–Rhodes–Vargas arXiv:1102.1895, Rhodes–Sohier–Vargas arXiv:1201.5219. The exact source says nontrivial ergodic lognormal star-scale invariant measures, actually requiring stronger dependence decay than ergodicity, up to a deterministic multiplicative constant. This excludes the tempting but irrelevant random-global-multiplier counterexample. No classification conclusion yet.

## Exact source — exact source and priority check

Saved the full review as text (73 pages). Read Section 6, pp. 42–55, including the exact Conjecture 6.4 on p. 52. Its equation is Definition 2.17, equations (2.17)–(2.18), pp. 17–18, not an independent-copy equation between spatial cells. The non-Gaussian analogue is RSV Conjectures 23–24, pp. 16–17. ARV Theorems 4 and 10 require a 1+delta moment; RSV Theorem 16 gives the Lévy generalization under Assumption 15. The remembered D0064 note correctly pointed to these but had a different theorem-page locator; use the newly downloaded text for all locators.

`nice -n 10` reported a sandbox setpriority denial, but a direct `os.getpriority(PRIO_PROCESS,0)` check returned 10: the process is already at the required priority. Future numeric runs will assert priority >=10 and use one numeric thread.

## Later uniqueness — later uniqueness and candidate proof

Powell Theorems 1.1–1.2 concern convolution approximations, not arbitrary fixed points. MRV Theorem 2.2 and Corollary 2.3 identify frozen limits, not every stationary solution. Located Bertacco–Hairer arXiv:2504.07552, which must also be checked. No proof of full classification found yet.

Candidate restricted theorem: allow an arbitrary homogeneous Lévy basis over a specified subcritical or critical control chaos, with conditional compatibility of its scale decomposition. Derive the exponent psi(q)=c q^alpha, rather than assuming stability. This is a restricted result; the unrestricted conditional independence/decomposition remains the main obstruction. A second candidate is an L2 uniqueness theorem for general (including non-Gaussian) scale weights with finite total variation of the terminal measure's reduced covariance. Both must be audited before inclusion.

## Literature audit saved; reduction begins

Saved an initial REPORT.md with exact equation, scope and normalization. Downloaded the journal versions of the review and RSV as text too. The journal review updates the freezing discussion but does not turn approximation uniqueness into fixed-point classification. BH Theorem A (arXiv v3 p. 4) is also explicitly about convolution approximations. Crossref identifies the published paper as EJP 30 (2025), pp. 1–22, DOI 10.1214/25-EJP1449.

OpenAlex forward-citation search obtained 200 recent records for the review before cursor pagination returned HTTP 401, and 23 dated 2014–2026 records for RSV. This is incomplete bibliographic evidence, not proof of absence. Will fill the review's earlier years with date-partitioned queries. Searches for “Durand” and “Biermé–Durand” did not identify a star-equation classification paper; no reference or theorem will be invented from those name hints.

## Restricted proofs saved

Theorem A derives the stable exponent from an arbitrary Lévy exponent, assuming an explicit conditional scale compatibility. The normalization argument uses E[Z(B)/(1+Z(B))] instead of E Z(B), so the proof also applies to the infinite-mean critical control. This assumption is stated as additional; it is not inferred from marginal star invariance.

Theorem B proves the marginal classification for an L2, finite-reduced-covariance class, allowing non-Gaussian weights. The terminal error is bounded by exp[−(d−kappa)t]. Included a compound-Poisson cone example with kappa=lambda |B|(exp(a)−1)^2. The Gaussian specialization only reaches gamma^2<d. These are restricted results, not a claimed resolution of D0064.

## Computation and independent checks — 08:40 +04

Ran the four binary lognormal regimes with 512 roots, seeds 20261113 (depth 18) and 20261114 (depth 16), a single numeric thread, inherited nice 10. The macOS RLIMIT_AS attempt was rejected; final measured RSS remained below 1.24 GB. Saved control samples, mass/Laplace summaries, explicit stable-leaf spatial statistics, one-step residual diagnostics and seed metadata. Added conditional Laplace estimates to separate tree sampling from stable-mark noise, then reran the affected programs.

Bounded-seed dual iteration collapses (m(1)^18=1/128); critical raw masses also fall, whereas the appropriate rescalings stay of order one. Stable spatial marks preserve order-one collision mass. These checks are evidence only, with noticeable critical finite-depth bias and sampling variability. Four finite-depth critical derivative samples were negative; no clipping was used.

Independent checks passed: Gauss–Hermite and direct sampling for the weight normalization, finite differences for m'(alpha), numerical quadrature of the Lévy intensity constant, and an independent normal-variable sampler at alpha=1/2.

The date-partitioned OpenAlex requests completed: 212 earlier review-citation records; combined with the recent 200, 408 distinct review-citation records were obtained (4 overlap). This is metadata coverage, not 408 full-text theorem audits. The RSV search returned 23 forward-citation records.

## Final audit

Rechecked source locators: the published review calls this Conjecture 6.2 (p. 369), whereas the requested arXiv version calls it Conjecture 6.4 (p. 52). Corrected the DRSV renormalization Theorem 5 locator to arXiv p. 8 and ABM Theorem 8.3 to p. 14. Revisited ARV Section 5 and RSV Appendix D: their non-Gaussian moment proof follows the same conditional-expectation/terminal-replacement strategy, with technical work controlling small-scale moments. The report does not claim that the restricted L2 argument is a new literature result.

Audited Theorem A's conditional-versus-marginal distinction, infinite-mean normalization, stable Lévy constant and converse. Audited Theorem B's covariance scaling, signed-measure absolute bound, integer-time limit, extension to Borel tests and non-Gaussian example; added the atomlessness consequence. Independent Poisson terminal covariance gives the same error exponent. All 17 source manifest hashes verify. All Python files parse. Both simulation records verify nice 10, one numeric thread and RSS below 4 GB. No PDF or image files exist in the task tree.

Completed task: “Open problem D0064”; received/start clock recorded 2026-11-13 08:26 +04. Outcome: PARTIAL. REPORT.md contains the exact problem and assumptions, bounded literature audit, reduction, two complete restricted proofs, simulation evidence, limits and reproduction commands. No publication or pushes.
