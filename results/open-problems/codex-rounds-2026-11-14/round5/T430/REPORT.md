VERDICT: PARTIAL order-1/N conditional full-state transient product-mixture bound

The earlier result holds. Its routing and path-coupling constants were independently re-derived, and the round 4 script passed all its checks again. No stationary counterexample or verified later solution was found.

New beyond round 4: for uniform sampling without replacement, fixed k, N>=max(d,k), and horizon T, PROOF.md proves that the conditional k-server full-path law, given the initial empirical full-state measure L_N(0), is within total variation distance

\[
 \min\left\{1,\frac{k(k+d-1)e^{2CT}-kd e^{CT}}{2N}\right\},
 \qquad C=\lambda d(d-1),
\]

of \((Q_{L_N(0)}^T)^{\otimes k}\). The unconditional comparison is its mixture over L_N(0). This improves the preceding fixed-time error from order N^(-1/2) to order N^(-1). The proof uses an exact independent-proposal representation, backward dependency trees, and a collision bound derived from the trees' factorial second moment. It includes residual requirements, ordered waiting requirements, and optional service age. No service density, hazard monotonicity, second moment, bounded support, or positive queue-length class-mass assumption is needed; atoms at zero are allowed. The clan-of-ancestors method is already in the literature; no literature novelty is claimed.

The same estimate gives conditional empirical mean-square error at most 1/N+(N-1)*delta_(N,2)(t)/N for every measurable full-state test f in [0,1]. Under stationary starts, two-tag covariance differs from Var((S_t L_N(0))f) by at most delta_(N,2)(t)+2*delta_(N,1)(t). Equation (13) of PROOF.md makes approximate invariance of the stationary empirical directing law quantitative for finite collections of observables. That law remains random. The arbitrary-G stationary independence problem remains unresolved.

Validation commands:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r4/briefs/T430/check_bounds.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 check_collision_bound.py
```

The new script passed 4,797 exact tagged proposal-rate comparisons, 458,959 explicit label-tuple checks, 480 rational generating-function expansions, 96 initial derivative checks, and 101 centered-test checks. The generating function gives a second derivation of every branching-moment coefficient. New-script peak RSS was 13,828,096 bytes and runtime 0.097 seconds. Both Python processes independently verified priority 20; the shell's warning concerns its attempted additional nice increment. All arithmetic was single-threaded, with a 30-second CPU cap. LOG.md contains complete outputs and parameter ranges.

What failed or remains uncertain: no stationary forgetting estimate or dissipation lemma was obtained. The improved fixed-time order still permits only T_N=b*log N with b<1/(2*C), the same coefficient as round 4. Passing approximate invariance to a limiting invariant law still needs tightness and continuity in a suitable full-state topology. Uniqueness of a fixed point would not by itself exclude other invariant laws. The theorem explicitly uses sampling without replacement; no new claim for a different sampling convention is made.

The literature check ended within five minutes and found no verified change. Opened Maria Clara Fittipaldi, Matthieu Jonckheere, Sergio I. Lopez, *Convergence properties of many parallel servers under power-of-D load balancing*, [arXiv:1809.05373](https://arxiv.org/abs/1809.05373), including its PDF; and Pooja Agarwal and Kavita Ramanan, *Invariant states of hydrodynamic limits of randomized load balancing networks*, [arXiv:2008.08510](https://arxiv.org/abs/2008.08510), including its PDF. In the retrieved latter PDF, the stationary-limit conjecture is Section 4.3, correcting the preceding reports' section number. This brief check is not exhaustive. No SOLVED_ELSEWHERE.md was created.

Next worker: use the fixed-time empirical estimate to pass a tight subsequence of stationary directing laws to an invariant probability law of the nonlinear evolution, with the needed continuity proved for a full-state topology. Then find a strict Lyapunov or attraction argument forcing that invariant law to be a point mass. Alternatively, control Var((S_t L_N(0))f) directly for a convergence-determining family and identify unique marginal limits. A genuine fixed-time limiting-flow argument could avoid demanding a quantitative attraction rate on logarithmic horizons.

All writes stayed in this folder. No git, subagents, external posts, global mesh/checklist writes, or brain writes.

Task: “Open problem T430: Asymptotic independence in the supermarket model with general service times”; received 15 November 2026, approximately 09:22 Asia/Tbilisi (05:22 UTC).
