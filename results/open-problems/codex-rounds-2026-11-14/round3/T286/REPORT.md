VERDICT: PROVED cubic self-covariance concentration with sharp asymptotic mean-square constants

The earlier session supplied a literature audit. This session proves one deferred self-covariance condition from Appendix B.6 of Jean Barbier, Francesco Camilli, Minh-Toan Nguyen, Mauro Pastore, Rudy Skerk, [arXiv:2510.24616v5](https://arxiv.org/html/2510.24616v5), for the activation phi(z)=(z^3-3z)/sqrt(6), independent Gaussian teacher weights, Gaussian inputs and all-ones readouts. The general Bayes-error problem and the gradient-descent question remain unresolved.

Let k/d tend to gamma>0, let q_ij=w_i·w_j/d, and define C=k^-1 sum_ij q_ij^3. For F_W(X)=k^-1/2 sum_i phi(w_i·X/sqrt(d)), put V=Var_X(F_W(X)|W). The proof establishes

    d^2 E[(C-1)^2] -> 36+18/gamma,
    d^2 E[(V-1)^2] -> 81+18/gamma.

These are self-covariance concentration constants, not Bayes prediction errors. Exact finite-dimensional identities and bounds are in [PROOF.md](PROOF.md). In particular, Gaussian row-norm fluctuations contribute a nonnegative correction B=V-C with E[B]=3/d+12/d^2 and Var(B)=O(d^-3). The result is uniform in the deterministic interpolation parameter because the averaged teacher marginal stays equal to its prior. It therefore proves the cubic Gaussian-weight instance of condition (165), including a bound for the true conditional variance.

Verification independently expands the network polynomial, integrates the Gaussian input, and computes Gaussian weight moments using exact rational arithmetic. All five cases (d,k)=(1,1),(1,3),(2,1),(2,2),(3,2) pass. Exact moment formulas also check the asymptotics at three width ratios. The reproduction command is

```
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 check_cubic.py > check_cubic.out 2>&1
```

The run takes less than a second, uses under 20 MB RAM and reports actual nice priority 20. The sandbox refuses a further relative priority adjustment; the inherited priority is already below the requested 15. See [check_cubic.py](check_cubic.py), [output](check_cubic.out) and [LOG.md](LOG.md).

The bounded five-minute literature check found no new rigorous general-activation solution. Direct reading confirms the earlier report's central finding: Remark 4 and Appendix B.6 retain unproved assumptions. Its restricted quadratic update also agrees with Theorem 2.10 of Yizhou Xu, Antoine Maillard, Lenka Zdeborová, Florent Krzakala, [arXiv:2503.14121v2](https://arxiv.org/html/2503.14121v2). The earlier directory has no PROOF.md or scripts to rerun.

Failures and limits: a shell paper download failed DNS resolution; web-tool source access worked. Independent checking caught and corrected draft higher-order coefficients. No proof of Gaussian replacement, teacher–replica concentration, a likelihood-weighted interpolation remainder, or optimizer optimality was obtained. The lemma is elementary; no literature novelty is claimed.

Next worker: keep the cubic activation and target a quantitative Gaussian integration-by-parts replacement in (158)–(161) after removing one sample from the posterior. Track its normalized accumulated error for n proportional to d^2. The present prior-marginal lemma does not justify that replacement. Treat the distinct-replica condition (166) separately, including how permutation symmetry of hidden units is handled before using a trace overlap.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, 03:44 Asia/Tbilisi.
