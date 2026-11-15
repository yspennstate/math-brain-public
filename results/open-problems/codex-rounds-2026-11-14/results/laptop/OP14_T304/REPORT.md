VERDICT: PROVED a query-preserving reduction from TV sampling to normalized Wasserstein sampling

For an m-strongly convex, L-smooth potential, take a supplied deterministic point c and a certified D>=||c-x_*||. One gradient query supplies D=||grad f(c)||/m. Define

    A=d+mD^2+log(1/epsilon),
    delta=epsilon^2*d/(512*A),
    R=2*sqrt(((d/2)*log(2)+log(1/delta))/m).

Run any delta-TV sampler and project its output onto the ball of radius D+R about c. For 0<epsilon<=1, the resulting law satisfies

    W2^2 <= (15/16)*epsilon^2*d/m.

This holds even if the original approximate sample has infinite second moment. Projection costs no oracle queries. Known m and a supplied c are part of the reduction's inputs; no optimization cost is hidden. The proof is in PROOF.md.

The opened Theorem 3 of Wei Guo, Bo Yuan, Ye He, Jiaming Liang, Molei Tao, and Yongxin Chen, [arXiv:2611.03442v1](https://arxiv.org/abs/2611.03442), supplies a subpolynomial TV bound. Conditional on that preprint theorem, the reduction gives, for C^2 strongly convex potentials and every fixed eta>0,

    Q_W2 <= C_eta*kappa*(d+kappa+epsilon^(-1)+G0)^eta,
    G0=||grad f(c)||^2/L,

with the initial gradient query included and a bound on every execution. The exponent is obtained by using the cited theorem with nu=eta/4. Neither that theorem nor its algorithm was independently implemented or fully audited here. The general minimax problem remains open; SOLVED_ELSEWHERE.md records the literature update.

AUDIT.md independently derives the radial moment bound by integration by parts and verifies the accuracy allocation through a different chain of constants. It also proves a limitation on transferring lower bounds: two C-infinity Gaussian targets, both with actual condition number 2 and a common sqrt(2)-warm start, have TV distance 0.166064074983513... but normalized W2 distance `(1-1/sqrt(2))/sqrt(d)`. Thus constant-TV lower bounds do not automatically give lower bounds at constant normalized Wasserstein accuracy.

Reproduce the diagnostic with:

    python -B resource_guard.py verify_reduction.py

It passed 294 accuracy allocations, 882 scale checks, five Gaussian moment-generating-function checks, three target quadratures, nine projection-tail integrals, an independent calculation of the Gaussian TV constant, and 81 query-exponent allocations. It ran for 9.108 seconds at BelowNormal priority, on one CPU core, with numerical thread counts set to 1 and a 768 MiB process-memory cap. Complete data: verification.json. Exact output: verification.stdout.txt. Quadrature is diagnostic; the uniform claims follow from the proofs.

What failed or remains uncertain:

- Unmodified TV output cannot imply finite W2; arbitrary heavy-tail contamination is a counterexample. Projection repairs this.
- The original fixed-conditioning preprint PDF fetch failed; no theorem was inferred from its search snippet. The corollary uses the separately opened Guo et al. theorem.
- `python -B resource_guard.py recall_local.py` failed with MemoryError under the 768 MiB cap, before returning any memory cards. Its fast path and then fallback both exceeded the guard. The cap was kept. This supplies no evidence that the memory store lacks relevant prior work.
- No novelty claim is made for the standard clipping and coupling ingredients. The piece completed here is their explicit oracle-accounted reduction, the stated corollary, and its metric-transfer limitation.
- No sharp dimension lower bound, value-only oracle bound, practical runtime bound, or optimal high-accuracy rate polynomial in log(1/epsilon) was obtained. The imported theorem requires C^2 regularity; the reduction itself does not.

The next worker should examine whether the instance-dependent tests in the existing TV lower bound can be made Lipschitz with a dimension-controlled constant and a quantitative expectation gap. That could establish a genuine normalized-Wasserstein lower bound; the Gaussian obstruction shows why TV separation alone is insufficient. Separately, audit the complete proof dependencies of the new subpolynomial TV upper theorem before using the conditional corollary as a definitive benchmark.
