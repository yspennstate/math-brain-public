VERDICT: PROVED a finite-horizon quadratic continuation-error certificate for Robbins' problem

For r remaining observations, an approximate rule compares the exact immediate expected rank with an approximation to the optimal continuation cost. If the continuation error is uniformly at most e_r, its total expected-rank regret is at most

    sum_{r=2}^n e_r^2/a_r,
    a_2=2, a_r=r-1 for r>=3.

The constant halves if errors are one-sided, or if each approximate continuation function is nonincreasing in the current observation. For a common error e the general bound is e^2(H_{n-1}-1/2). The two-choice constants are attained by explicit examples.

The proof permits jumps at past observations. It couples histories to establish monotonicity, bounds the measure of near-indifference observations, and telescopes local decision residuals. See [PROOF.md](PROOF.md).

A corollary rounds rejected histories upward with mesh 1/M, keeps the current observation and current relative rank exact, and uses exact optimal continuation functions at the rounded histories. Its regret is at most A_n/M^2, where

    A_n = (n-1)^2((n-1)^2-1)/24 - (n-2)^2/4.

For n=5 this is 31/(4M^2), hence 31/40000 at M=100. This is an oracle reduction; those continuation functions have not been computed here. It is not a policy based only on bins. No improvement to the numerical bounds on V or V_5 is claimed.

If an implemented policy's expectation is independently enclosed in [L,U], and its certificate is B, then L-B <= V_n <= U. This is the practical reduction furnished by the result.

Verification command, from this folder:

```
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_certificate.py > audit_stdout.txt 2> audit_stderr.txt
```

The run passed 2016 exact-rational penultimate policy checks across 126 histories, 2016 third-to-last slope checks, and 29 independent stage-sum versus closed-form coefficient checks. Actual policy cost and residual integrals agreed exactly. Peak resident memory was 16,171,008 bytes; runtime was about 0.25 seconds. The sandbox rejects the requested nice adjustment, but the process inherits priority 20. Data: [penultimate_audit.csv](penultimate_audit.csv), [audit_results.json](audit_results.json); exact output and failed first run are documented in [LOG.md](LOG.md).

What failed: the sandbox rejected a memory-limit setter, so the final script measures/checks peak resident memory instead. Mathematically, threshold displacement alone does not imply quadratic loss: at r=2 and history (1/2), moving the threshold upward by delta costs delta/2+delta^2. The proof's exact immediate-rank requirement is essential.

Literature check: within ten minutes, searched for later solutions and opened the following primary sources. No advance beyond the supplied status was found:

- Alexander Goldenshluger and Yaakov Malinovsky, *On optimal stopping problems with full information and rank-dependent reward*, [arXiv:2610.33701](https://arxiv.org/abs/2610.33701), including [the full text](https://arxiv.org/html/2610.33701v1). Section 4 gives finite-horizon recursions; Section 4.3 discusses numerical approximation error. The limiting value remains open.
- Léonard Brice, F. Thomas Bruss, Anirban Majumdar, Jean-François Raskin, *Algorithms for Robbins' Problem using Markov Decision Processes*, [arXiv:2608.27419](https://arxiv.org/abs/2608.27419), including [the full text](https://arxiv.org/html/2608.27419v1). Section 3 proves approximation convergence for a different discretization retaining binned information.
- Martin Meier and Leopold Sögner, *A new strategy for Robbins' problem of optimal stopping*, [arXiv:1606.03348](https://arxiv.org/abs/1606.03348), arXiv abstract page opened.

Uncertainty: priority for the certificate is not established. It may be an elementary instance of general approximation results for optimal stopping. The proof is analytic; the finite computations check special cases rather than replace the general proof. Its constants grow with n and give no asymptotic solution.

Next worker: construct a computable continuation approximation with certified uniform error and monotonicity, then enclose its policy expectation independently. Apply the certificate to obtain a rigorous enclosure for V_5. Include numerical interpolation error; substituting an uncertified decimal table into the theorem is insufficient.

Task: “push this problem forward by one checkable piece” — 14 November 2026, approximately 20:48 Asia/Tbilisi.
