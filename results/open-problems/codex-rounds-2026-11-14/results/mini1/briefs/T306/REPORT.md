VERDICT: PROVED smooth pure-ODE TV instability and a uniform Euler-step obstruction

The main dimension-dependent minimax question remains open in this work. The completed piece concerns the unmodified probability-flow ODE under the stated L2 approximate-score hypothesis.

For the stationary one-dimensional OU target `p=p_delta=N(0,1)`, take the fixed time-independent oracle

\[
\widehat s_k(x)=-x+\frac c k\sin(kx),\qquad 0<c<1.
\]

Its uniform error is at most `c/k`, and its squared L2 error is exactly `c^2(1-exp(-2k^2))/(2k^2)`. Every estimate is smooth, `(1+c)`-Lipschitz, and the score of a strongly log-concave density with curvature between `1-c` and `1+c`. The target has second moment one and condition number one.

Nevertheless the exact reverse probability-flow ODE, initialized at its exact Gaussian forward marginal and run for unit time, has output `P_k` satisfying

\[
\left|\operatorname{TV}(P_k,N(0,1))
-\frac2\pi\arcsin(\tanh(c/2))\right|
\le\frac{\sqrt{2\pi}}k.
\]

Moreover its explicit Euler implementation with **any positive equal-step count N** satisfies

\[
\operatorname{TV}(P_{k,N},N(0,1))
\ge\frac{c(1-c/2)e^{-c}}4-\frac{\sqrt{2\pi}}k.
\]

For `c=1/2,k=1000`, RMS score error is below `0.000354`, exact-ODE TV is at least `0.15501589`, and Euler TV is at least `0.05435562` for every `N>=1`. Thus making the score error small and refining the integration cannot by themselves yield a uniform TV guarantee for this sampler. The estimated scores' second derivatives grow with k, and their Jacobian errors do not vanish.

The full proof, including constants and the all-N statement, is in [PROOF.md](PROOF.md). [AUDIT.md](AUDIT.md) contains independent derivations and scope checks.

The general insufficiency of L2 error alone was already known: Gen Li, Yuting Wei, Yuejie Chi and Yuxin Chen give a discontinuous discrete example in Section 3.2 of [arXiv:2408.02320](https://arxiv.org/html/2408.02320v1). The present artifact supplies a quantified smooth continuous-time version and an all-N Euler bound. Priority for this precise refinement has not been established. No matching linear lower bound for the original oracle problem was found during the literature search, which stayed below ten minutes; the search is not exhaustive.

Reproduce all numerical checks with:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 verify_obstruction.py > verification_output.txt 2>&1
```

The exact command output is saved in [verification_output.txt](verification_output.txt). Data are [phase_checks.csv](phase_checks.csv), [gaussian_checks.csv](gaussian_checks.csv), [euler_checks.csv](euler_checks.csv), [score_checks.csv](score_checks.csv), and [verification_metadata.json](verification_metadata.json). Checks compare the explicit flow and its Jacobian with RK4, compute phase TV in both source and target coordinates, compare Gaussian integrals at two resolutions, verify Gaussian score RMS by direct quadrature, and check Euler inequalities. The proof is analytic; the quadratures are not certified numerical bounds.

What failed: the first coarse Gaussian quadrature did not meet its grid-agreement tolerance; refining both grids fourfold passed a tighter tolerance. macOS rejected the requested address-space resource limit, so the script records that failure, streams its grids, measures peak RSS, and enforces a CPU-time limit. The inherited nice priority is 20; `nice -n 15` warns because it cannot raise that priority. An initial brain-recall attempt loaded an ML runtime and exceeded 1 GB; it was stopped. Subsequent verification uses only the standard library and about 16 MB. Details and all failed commands are in [LOG.md](LOG.md).

Limits and next work: this is a failure of directly using an approximate field, not an information-theoretic oracle lower bound. The known Gaussian can be sampled without any oracle query. The time-indexed estimates need not form an OU-consistent trajectory. Arbitrary deterministic algorithms, score regularization, non-Euler solvers, and stochastic correctors are not ruled out. The next worker should fix the oracle's temporal consistency/derivative assumptions and the allowed preprocessing, then investigate whether fixed positive-time smoothing yields a TV guarantee for a regularized ODE under L2 error alone. Linear necessity in d remains unresolved here.

Task: “push this problem forward by one checkable piece” — received approximately 2026-11-14 22:11 +04 (Asia/Tbilisi).
