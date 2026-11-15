# C0033B research log

Task received 2026-11-13 02:13 Asia/Tbilisi (UTC+4): “Open problem C0033: concavity of the entropy of determinantal measures in the kernel”.

## 02:19 — orientation and scope

Read C0033A/REPORT.md, LOG.md, dpp.py, search.py, and source-download code. Reusing its exact atom enumeration and analytic Hessian code, copied into this workspace with the compiled library. Read Gu's complete report and the entropy conjecture in Lyons 2003. Both PDFs and extracted texts are saved in sources/. The finite conjecture is Lyons 2003 Conjecture 9.2, not Section 5; the entropy-rate Conjecture 5.3 is in the later survey.

Shared mesh hello/digest/claim/assert and task-checklist registration were attempted; the sandbox denies writes to their shared stores. No live conflicting lease was reported. All research writes are confined to this isolated folder; no subagents or additional model workers. Read startup index, brain recall, and compute state. Governor reports owner_away_open, CPU saturated; use one numerical process, one BLAS thread, inherited nice priority, and keep allocations well below 4 GB.

The inherited report proves n=2 and coordinate-supported lifting, but does not settle any of the three requested general cases. Numerical searches are evidence only. The priority is a full three-point certificate or a verified counterexample; then arbitrary rank-two and commuting directions.

## 02:27 — analytic partial results

Derived two new certificates (proofs are being audited):

1. With one coordinate distinguished, write Q=[[a,v*],[v,C]]. For every fixed C, H is jointly concave in a and v. Conditional on the complement pattern T, the occupancy parameter is r_T=a-v*(C-D)^{-1}v. It decreases with T by conditional pairwise negative correlation. Hence h'(r_T) increases. Stochastic domination for C+sww* implies sum_T pi_T h'(r_T) w*(C-D)^{-1}w >=0, and the conditional entropy second derivative has two nonpositive terms. These one-row-and-column directions have rank at most two and need not be supported on two coordinate indices. Noncommuting Loewner domination uses Borcea–Branden–Liggett Theorem 4.13 (2009); Lyons's original theorem stated a commuting hypothesis, removed in his errata as well.

2. In dimension three, freezing f(S)=log p_S and expanding its Mobius coefficients gives sum p''_S log p_S = -2 tr(adj(A) R), where R=diag(l_23^0,l_13^0,l_12^0)-gamma Q, gamma=l_ij^0-l_ij^1. Conditional negative correlation makes both l^0 and l^1 nonnegative, so R is positive semidefinite: use Q if gamma<=0 and I-Q if gamma>=0. Thus every indefinite rank-two direction has nonpositive entropy curvature. This also controls purely imaginary directions at a real symmetric three-point kernel.

Targeted three-point search: 12,000 full Hessians and 11,217 optimization evaluations of curvature divided by squared offdiagonal norm. Near-zero double positives were checked at 110 and 160 decimal digits; all saved directions have negative curvature. The direct independent Mobius differentiation audit exposed loss of differentiation accuracy near tiny entries; the audit will use polynomial coefficient extraction instead.

General rank-two logarithmic-term tests through n=6 are positive in all 4,000 trials. Linear-program tests of the stronger claim for arbitrary submodular set functions have no violation through n=8; these remain numerical observations, not theorems. HiGHS subsequent runs explicitly set one thread.

## 02:42 — final audits and deliverables

- REPORT.md begins PARTIAL and contains complete proofs of concavity under one-row-and-column changes in arbitrary dimension, and all indefinite rank-two directions in dimension three. Conditional lifting extends the latter to three-coordinate-supported directions in arbitrary dimension. It also proves the three-point Hessian has positive index at most one and gives a scalar necessary-and-sufficient Hessian inequality when the correction matrix is invertible.
- The full three-point conjecture, general higher-dimensional rank two, rank-two semidefinite directions, and arbitrary commuting segments remain open. No entropy counterexample was found. The three-point commuting family has an exact fixed random-permutation representation, proved via Birkhoff and the unitary cofactor identity; entropy concavity of that nonlinear input family is not inferred.
- Final three-point runs: 12,000 kernels; 11,292 normalized optimization evaluations. All four saved near-zero directions have negative curvature at 110 and 160 digits. Independent polynomial/Mobius coefficient evaluation agrees to absolute error at most 1.43e-160.
- Commuting runs: 5,100 kernels and 6,183 optimization evaluations. All three saved optimized directions have negative curvature at 110/160 digits. Their binary commutator residual is recorded; exact commutation is not claimed for the decimal reconstructions.
- General indefinite rank-two runs: 4,000 directions through n=6, all nonlinear logarithmic terms nonnegative. The stronger submodular-expectation route was tested by linear programs in the interior and at projection boundaries through n=8; no violations above about 1e-14. It remains an unproved route.
- The proposed PSD extension of the three-point correction matrix is false. Full exterior matrices at strict kernels of orders 5, 6, and 8 have negative Rayleigh quotients, independently evaluated at 110/160 digits. Their bivectors have nonzero Plucker relations. An 80-digit outward-rounded interval computation at order 5 validates Q>0, I-Q>0, all 32 atoms positive, a negative exterior Rayleigh quotient, and a nonzero Plucker relation. This refutes only that matrix certificate, not entropy concavity or the weaker decomposable-vector condition.
- The local full Hermitian interval certificate covers radius 1/10000 in all nine real entries around the rational center in REPORT.md. All nine negative-Hessian LDL pivots have positive interval lower bounds. It is not a cover of the compact global parameter domain.
- Both requested sources were fetched anew, together with the stochastic-domination source, Lyons's errata and his 2014 survey. URL and SHA-256 metadata are saved in sources/manifest.json.
- Numerical audit corrections: the optimized kernel decoder now enforces exact binary Hermiticity; independent Mobius checking uses determinant polynomial coefficients rather than differentiating a numerically pivoted determinant. mpmath 1.3.0 interval-complex conjugation raises an internal error, so the validated complex routine implements conjugation explicitly as (real,-imag). No failed intermediate numerical output is used in the report. HiGHS final runs explicitly use one thread.
- Largest principal-run peak RSS: 127.94 MiB. No subagents, additional model workers, or concurrent numerical pools. The rebuilt C++ library and all Python scripts compile. A sequential reproduction runner rebuilds the library and reruns the proof certificates and arbitrary-precision audits.
- Shared brain/checklist/mesh writes remain unavailable under the sandbox. Selective durable results are preserved in MEMORY_NOTE.md, with verified scope and explicit limitations. All artifacts are confined to C0033B.

Final validation: python3 reproduce.py audit passed after rebuilding the C++ library. Every saved kernel is exactly Hermitian in binary arithmetic; all relative report links resolve; displayed math delimiters balance; all Python files compile. No final run log contains a traceback or numerical runtime warning. REPORT.md and LOG.md are complete, with code, data, primary sources, and a hash/version manifest.
