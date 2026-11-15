VERDICT: PARTIAL two-token deterministic merging asymptotic and joint small-noise mean merging exponent

For two equal-weight tokens on the circle with identity matrices and normalized attention including self-attention, PROOF.md proves the following. Start at fixed angular gap x and stop at first entrance into gap delta, with 0<delta<x<pi. Write a=1-cos(x).

- Deterministic time: T_beta ~ exp(beta a)/(2 beta sin(x)^2).
- Give each token independent angular noise sqrt(2 nu_beta) dW. If -log(nu_beta)/beta -> r in [0,infinity), then log(E[tau_delta])/beta -> min{a,r}.
- An exact double-integral formula and explicit finite-parameter bounds underlie the noisy result. The upper bound controls excursions toward larger, more weakly attracting gaps.

Thus exponentially small independent noise can change the deterministic exponential merging scale even in the smallest normalized-attention system. Polynomially small diffusivity gives zero exponential rate on the beta scale. This is a theorem about a mean first entrance time; it does not claim a transition-time distribution or permanent merging.

The short literature check found relevant earlier advances, documented with links and theorem limitations in LITERATURE.md. No resolution after the supplied November 2026 status was found. The 2025 multiscale paper's closest-pair limit stops before collapse; the October 2026 noisy result concerns conditional applications to unnormalized attention. No SOLVED_ELSEWHERE.md was created. Priority for this special case has not been established.

Verification command, run from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify.py
```

The successful run exited 0 in under one second. The launcher warns that changing priority is not permitted; a separate check confirmed inherited effective nice=20. Computation was single-threaded and used only the standard library with small arrays.

Two deterministic coordinate integrals agree to relative error 1.071e-11. An integrating-factor calculation and an independent finite-difference boundary-value solve agree to relative error 3.143e-07. Numerical results are in verification.json and crossover.csv; exact output is in LOG.md. These floating-point checks support the algebra but are not the proof.

What failed: the first numerical implementation integrated a sharp derivative layer with the trapezoidal rule and failed a mesh-convergence assertion at beta=160. Exact integration within each constant-drift cell fixed that issue without loosening tolerance. An argument based only on local attraction would not control rare outward excursions, so the proof bounds that contribution explicitly. Connecting the general model's phases was not attempted.

Limits and doubts: no generic cluster count, many-token noisy reduction, unequal-mass theorem, beta-dependent gap theorem, or exactly antipodal theorem is proved. Independent noises break coincidence within a larger cluster, so the noisy result cannot simply be lifted to two multi-token groups. Deterministic exact collision takes infinite time. The literature search was brief and does not establish novelty.

Next worker: extend the scalar method to unequal two-atom masses, then determine whether clusters of small but nonzero width stay concentrated over the relevant waiting scale under independent noise. That concentration estimate is needed before treating a cluster center as a single noisy token. Retain separate attention and noise parameters.

Task: T324, “push this problem forward by one checkable piece.” Date: 14 November 2026; first recorded session clock 22:13 +04 (Asia/Tbilisi). The prompt's own timestamp was not supplied.
