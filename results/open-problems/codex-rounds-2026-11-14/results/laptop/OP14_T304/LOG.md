# T304 working log

## 2026-11-14: scope and initialization
- Work is confined to this directory. No git, external writes, or communication.
- Read ~/AGENTS.md. The explicit session restrictions take priority over standing instructions to upload or update shared memory.
- Literature check started at approximately 17:41 UTC; ten-minute deadline approximately 17:51 UTC.
- Initial web searches: `"2611.05813" sampling`; `strongly log concave sampling query complexity lower bound 2026 Zhou Suzuki`.
- Search found the stated Zhou--Suzuki preprint and a September 2026 preprint entitled "Subpolynomial query complexity for well-conditioned log-concave sampling". These are leads, not verified theorems yet. Opening original papers next.

## Literature checkpoint (17:48 UTC)
- Opened primary arXiv pages and HTML for Huanjian Zhou and Taiji Suzuki, arXiv:2611.05813, and for Wei Guo, Bo Yuan, Ye He, Jiaming Liang, Molei Tao, Yongxin Chen, arXiv:2611.03442.
- Guo et al., Theorem 3, gives gradient-query upper bound C_nu*kappa*(d+kappa+epsilon^(-1)+G0)^nu under LSI, for every fixed nu>0. This is a substantial update to the brief's polynomial upper-bound benchmark, but does not match the superpolylogarithmic lower bound or settle all parameters.
- OpenAI September 26 preprint README opened; its PDF fetch was unsupported. Do not treat search snippets as an audited proof.
- Existing math-recall script documents co-use logging and cache writes outside the permitted directory. Inspecting read-only alternatives before invoking; no shared-memory mutation is authorized.

## Choice of concrete piece (before proof work)
Prove a query-preserving, contamination-safe reduction from TV sampling to normalized W2 sampling for strongly log-concave targets. Use radial projection about a point certified by one gradient query. Derive explicit error/radius constants and a worst-case query bound; then apply the opened subpolynomial TV theorem, with all regularity and initialization assumptions stated. This is a reduction and its corollary, not a claim to close the minimax gap.

Why this piece: the problem conflates two metrics. TV alone does not control the second moment of an approximate output. A precise clipping reduction makes the updated upper bound usable in the Wasserstein regime and identifies exactly what does and does not transfer to lower bounds.

Proposed route: prove a Gaussian radial exponential-moment bound using strong convexity and dilation; combine a maximal coupling after projection with an integrated target-tail bound; choose the TV tolerance explicitly as a function of epsilon, d, and a certified distance to the minimizer. Independently check constants and search for a missed contamination or centering case.

## Proof checkpoint
- Saved PROOF.md with the query-preserving clipping theorem and explicit allocation delta=epsilon^2*d/[512*(d+mD^2+log(1/epsilon))]. The derived squared-error factor is 480/512=15/16.
- Saved SOLVED_ELSEWHERE.md, explicitly headed as substantial updates, not a complete solution. It distinguishes sequential query count from Dogariu's newer parallel-depth result.
- The main reduction assumes only differentiability, strong convexity, and smoothness. The corollary invoking Guo et al. is explicitly restricted to their C^2 setting and conditional on their preprint theorem.
- Literature search is now closed. Work continues on a proof and audit, not an additional literature survey.
- Need independently verify the dilation moment estimate, all constants, gradient-based centering, and the exponent substitution nu=eta/4.

## Independent verification command (about to run)
Command: `python -B resource_guard.py verify_reduction.py`
- The guard sets BelowNormal priority, single-core affinity, all numerical thread environment variables to 1, and a Windows Job Object process-memory limit of 768 MiB. It blocks Python-level writes outside this directory and child-process launches.
- The diagnostic uses only the standard library, no GPU, no torch, no training, no random Monte Carlo. Its internal deadline is three minutes and all quadrature sizes are fixed.
- Planned output: verification.json plus an exact stdout transcript saved locally. Numerical quadrature supplements, rather than replaces, the proof.

## Verification result
Exact command: `python -B resource_guard.py verify_reduction.py`
Exit status: 0. Exact stdout is in verification.stdout.txt. Output:
```
{"priority": "BelowNormal", "affinity_mask": 1, "process_memory_limit_MiB": 768, "thread_environment": 1}
PASS: exact constant 480/512 = 15/16
PASS: 294 accuracy allocations and 882 physical-scale checks
Maximum normalized error bound on grid: 0.542104176265376
PASS: 5 Gaussian MGF series and gamma-function moment checks
PASS: 3 target quadratures, asymmetric mode/mean check, 9 tail integrals
PASS: Gaussian TV by CDF and quadrature: 0.166064074983513
PASS: 81 query-exponent allocations
Data: verification.json
Elapsed seconds: 9.108
```
- Saved AUDIT.md: independent integration-by-parts proof of the radial MGF; separate constant chain giving factor 81/128; common-warm-start Gaussian obstruction to transferring TV lower bounds to normalized W2; explicit scope and failure-mode checks.
- A guarded read-only attempt at math_recall.py follows. Its local wrapper disables shared logging, shared cache writes, helper threads, and SQLite writes. It may miss WAL-only records. No shared memory will be updated.
Command: `python -B resource_guard.py recall_local.py`

## Recall attempt result and final scope
- `python -B resource_guard.py recall_local.py` exited 1 with MemoryError. The tool reported its fast path failed with MemoryError, then its fallback failed in derive_tool while building the title map. No memory cards were returned. No relaxation of the memory cap was attempted. This is not a negative search result.
- Primary mathematical diagnostics remain passing. The independent proof audit is in AUDIT.md, including a separate bound 324/512=81/128 below the advertised 15/16.
- Saved REPORT.md with the required verdict line. It states the main reduction unconditionally, separates the corollary's dependence on a preprint theorem, and explicitly leaves T304's minimax gap open.
- Final review checks: no use of unprojected approximate-output moments; target projection bias paid for; center radius includes D; mode differs from mean in the asymmetric diagnostic; d=1 restricted appropriately in the external corollary; C^2, exact gradients, known curvature bounds, and initialization dependence are explicit; no polylogarithmic-accuracy conclusion claimed.
- All created files and data stay in this directory. No git or external writes were used. The guarded recall attempt created only local cache files, if any; no shared memory records were changed.

## Artifact readback
- Read back the required report, proof, audit, log, literature update, diagnostic script, JSON data, and stdout transcript. Verified REPORT.md begins with the required verdict text, with no UTF-8 BOM before it; verified JSON records 294 allocation cases and 81 query-bookkeeping cases.
- Final mathematical scope: explicit TV-to-normalized-W2 reduction; no claim to settle the sharp general query complexity. All completed work is ready for the coordinating agent to copy.
