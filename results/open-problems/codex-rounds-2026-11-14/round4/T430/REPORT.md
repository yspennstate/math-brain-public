VERDICT: PARTIAL quantitative full-state finite-time product-mixture bound retaining the random initial empirical measure

The earlier result holds. Conditional competitor sampling independently recovers the append-shorter factor \((N+1-d)/N\) and the periodic witness's strict decreases. The original transient initial-mixture obstruction also checks out. Neither result was a stationary counterexample.

New beyond the earlier reports: PROOF.md replaces the false arrival-rate monotonicity step by a uniform routing estimate and a quantitative full-state path coupling. For arbitrary exchangeable initial states, fixed \(k\), \(N\geq d\), and horizon \(T\), the total variation distance between the actual tagged paths and the product-mixture directed by the nonlinear queue started from \(L_N(0)\) is at most

\[
 \min\left\{1,\
 k\left(\frac4{\sqrt N}+\frac d{2N}\right)
       (e^{\lambda d(d-1)T}-1)
 +\frac{k(k-1)}{2N}\right\}.
\]

The same estimate holds conditional on the empirical initial measure. It concerns residual requirements and ordered waiting requirements, and can retain service age. It assumes no service density, hazard monotonicity, second moment, or positive limiting queue-length class masses. Atoms at zero are allowed. The proof constructs the nonlinear reference law and proves the independent, nonidentically distributed empirical-tail estimate it uses. This is progress within this work sequence; no literature novelty claim is made for the transient coupling method.

For stationary initial laws, the comparison remains a mixture. For a measurable full-state test \(f:E\to[0,1]\), the actual two-tag covariance differs from \(\operatorname{Var}(\mu_t^{L_N(0)}f)\) by at most three times the two-path error above. The bound also vanishes on \(T_N=a\log N\) for \(0<a<1/[2\lambda d(d-1)]\). No concentration or forgetting estimate on such horizons has been obtained. The arbitrary-\(G\) stationary independence assertion remains unresolved.

Validation: every load-bearing constant has a second symbolic derivation in PROOF.md, Section 7. Command:

    OMP_NUM_THREADS=1 nice -n 15 python3 check_bounds.py

Output: 4,770 exact routing count cases passed, 378 independent subset enumerations passed, 8,190 fair-sign walks passed, and 36 earlier periodic-witness cases passed. The inherited priority was independently certified as 20; peak RSS was 14,057,472 bytes, one thread, and runtime was under one second. These finite checks supplement the all-parameter proof. Full output and commands are in LOG.md.

What failed or required correction: the sandbox rejected address-space and data-segment resource-limit setters before computation; the final small streamed audit used a 30-second CPU cap and reported RSS. A draft sentence incorrectly excluded zero-size departures coinciding with arrivals; the final proof treats these as part of the candidate update. No constant changed. No numerical simulation, stationary convergence computation, or proof of empirical concentration is claimed.

The literature check took less than five minutes and found no verified later solution. Opened Maria Clara Fittipaldi, Matthieu Jonckheere, Sergio I. Lopez, *Convergence properties of many parallel servers under power-of-D load balancing*, [arXiv:1809.05373](https://arxiv.org/abs/1809.05373), including its PDF; and Pooja Agarwal and Kavita Ramanan, *Invariant states of hydrodynamic limits of randomized load balancing networks*, [arXiv:2008.08510](https://arxiv.org/pdf/2008.08510), whose retrieved Section 4.2 still leaves the relevant stationary identification conjectural. This brief check is not an exhaustive literature certification. No SOLVED_ELSEWHERE.md was created.

Next worker: under stationary starts, prove \(\operatorname{Var}(\mu_{t_N}^{L_N(0)}f)\to0\) for a convergence-determining collection of full-state tests, on horizons where the displayed error tends to zero, and identify a unique limit for their means. Alternatively, establish a strict dissipation or attraction argument which forces invariant probability laws of the nonlinear evolution to concentrate on one fixed point. Uniqueness of the fixed point alone does not rule out a nontrivial invariant law of the evolution. The routing and transient steps here do not establish that missing fact.

All writes stayed in this folder. No git, subagents, external posts, messages, accounts, global mesh writes, or brain writes were used.

Task: “Open problem T430: Asymptotic independence in the supermarket model with general service times”; received 15 November 2026, approximately 06:41 Asia/Tbilisi (02:41 UTC).
