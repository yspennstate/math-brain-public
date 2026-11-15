# I0078 work log

Task received: 2026-11-13, approximately 16:32 Asia/Tbilisi (UTC+4).
Task: “Open problem I0078”, literature audit and attempt on Conjecture 2.9.

## 16:33–16:36 — orientation and source identification

Read startup orientation and compute state; recalled the topic (brain has no direct record).
No subagents. All task artifacts and writes stay in this directory. The later work-only-here instruction prevents writes to the global checklist, mesh, and brain; this log is the local task record. No background services, publication, git mutation, or pushes.

Identified arXiv:2510.17257, David Dereudre and Rafaël Digneaux, Rigidity of one-dimensional point processes via optimal transport. The user's second-author initial T. does not match the listing. v1 submitted 20 October 2025 07:44:55 UTC; v2 submitted 21 September 2026 14:48:09 UTC. Both will be checked. Full texts downloaded as transient in-memory bytes and converted to plain text; PDF files are never written.

## 16:36–16:40 — decisive distinction found

Saved source v1 (24 pages) and v2 (26 pages), with page markers and SHA256 provenance. v1 Conjecture 2.9 p.10 says decreasing in s; v2 Conjecture 2.8 p.10 says increasing in s and still leaves the threshold open. Source constructions are independently tiled stationarizations of neutral interval-background gases, not periodic Gibbs gases.

Found Yan Ru Pei, arXiv:2609.28503v1, submitted 15 September 2026 01:55:59 UTC, 21 pages. Theorems 1.1–1.2 pp.2–3 prove all-beta displacement bounds and stationary L2 lattice matching for periodic limits for 0<a=-s<1. Corollary 1.4 p.3 gives bounded interval variance. The introduction p.1 explicitly states that identifying these with the Dereudre–Digneaux interval-background limits is a separate question. Therefore cannot call the precise source conjecture resolved merely by substituting ensembles.

Compute note: shell already runs at nice 10. macOS nice utility emitted a permission warning on redundant adjustment; verified actual priority is 10. Future computations inherit it and BLAS/OpenMP are restricted to one thread.

## 16:40–16:43 — variance audit and finite-size check

Read the relevant theorem statements and hypotheses in Boursier (2026 revisions), Lewin, Leblé–Serfaty, DHLM, Ghosh–Peres, Huesmann, Huesmann–Sturm, Erbar–Huesmann–Leblé, Aizenman–Goldstein–Lebowitz, Lelotte, Touzo–Le Doussal–Schehr, the perturbed-lattice paper, and the 2025 gap-metric paper. Positive-exponent results do not extend by changing the sign of s. In Boursier, counting variance is of order L^s for 0<s<1, not L^{-s} for negative s.

Checked the periodic proof's main chain: curvature sum over images; cyclic means equal one; log-concavity controls reciprocal conductances; deterministic flows compare to |i-j|^{a-2}; reciprocal Fourier eigenvalues are integrable for a=-s>0; Brascamp–Lieb; extraction retaining phase and labels; crossing-current bound. This is printed work, not a new proof of the source problem.

Ran one-thread Metropolis diagnostics, nice 10, s=-1/2, N=32,64,128, beta=0.25 and 4, lattice and uniform starts. 1200 sweeps/chain, 400 discarded, 100 measurements. Total elapsed about 62 seconds. Interaction evaluated with an 18-term convergent binomial/zeta series, not a nearest-image potential. Spatial observation-origin variance integrated analytically. Checked the count-variance formula independently by exact integration over its jump points; integer/half-integer lattice controls pass. Raw chain statistics and final configurations saved in data/. No mixing claim or asymptotic inference from these small runs.

## 16:44–16:54 — proof attempts and independent audit

Saved REPORT.md and expanded it while checking arguments. Distinguished the anchored discrepancy from a stationary primitive. Verified that unbounded first absolute discrepancy obstructs L1 transport, whereas growing variance alone does not: a mixture of clustered lattices with P(M=m) proportional to m^{-p}, 2<p<3, has finite L1 cost but variance of order L^{3-p}. This is not a Riesz-gas counterexample. Read the integrable-primitive construction in Aizenman–Goldstein–Lebowitz pp.14–18; gave a separate L2 coboundary argument showing bounded count variance suffices for finite L1 transport.

Obtained a quantitative bound for the actual interval-background limits, without ensemble substitution. With a=-s, A_s=1/((a+1)(a+2)), C_s=2 Gamma(1+a) sin(pi a/2), B_s=2^{2-s}/C_s:
Var N(0,L] <= B_s (1/beta+A_s) L^{1+s}.
Proof: source cell-method partition lower bound => expected energy <= n(1/beta+A_s); Plancherel controls the spatially integrated sharp-window discrepancy by B_s L^{1+s} times energy; tile-boundary probability L/n is removed using a bounded discrepancy-square truncation, taking n to infinity before removing the truncation. Checked the exponent and factor 2 twice. This proves hyperuniformity for these limits and excludes c L^{-s} asymptotics for s<-1/2. Huesmann Theorem 1.1(i) then gives finite mean q-transport moments for q<(1-s)/2. This does not reach q=1 and does not prove any proposed beta regime. No novelty claim for the general Fourier estimate.

Independent computations in code/audit_checks.py: kernel versus 40-digit Hurwitz zeta (max error 1.32e-13), spectral resistance versus grounded inverse (max error 6.44e-15), interval Hessian versus finite differences (max error 9.45e-7), and 36 piecewise-exact discrepancy-integral checks of the derived deterministic Fourier bound. All passed. The two equivalent Gamma formulas for C_s also agree.

The remaining barrier is an integrable primitive for the source limits, or an ensemble-comparison theorem, or a divergent first-moment discrepancy lower bound. No large-beta or small-beta L1 direction has been proved. Classification kept NO_PROGRESS under the requested phase-direction criterion; the source-specific upper bound is recorded with its proof and limitations. Periodic all-beta matching is already in print and is identified as such.

## Final validation

REPORT.md begins exactly NO_PROGRESS. Confirmed 20 full plain-text sources and seven plain-text listings, all manifest hashes matching, 12 finite simulation chains, nine independent resistance comparisons, and 36 deterministic variance-bound checks. No PDF, page image or scan exists in the task folder. All computations finished. Source-only definitions, version correction, periodic-versus-interval distinction, and the derived interval variance upper bound were rechecked before reporting. No publication, push, external message, or global-state update was performed.
