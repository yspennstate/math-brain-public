VERDICT: PARTIAL stationary variance reduction and an explicit obstruction to averaging deterministic-start estimates

PROOF.md gives an exact decomposition of stationary empirical variance into conditional fluctuations and variance of the conditional mean over the initial state. With one-server marginal convergence assumed, it identifies the additional concentration needed for full-state asymptotic independence. It also gives a quantitative sufficient condition on sets of large stationary probability.

The reduction is tested inside the FIFO supermarket model with G=δ₁. An exchangeable mixture of all-empty and all-busy initial states has

\[
\operatorname{Var}\!\left(N^{-1}\sum_i1_{\{Q_i(t)=0\}}\right)
\geq \tfrac14 e^{-2\lambda dt},\qquad 0\leq t<1.
\]

A separate calculation proves tagged emptiness covariance at least 1/8 at t=min(1/2,1/(8λd)), for every N≥max(d,2). Both sampling conventions are covered. This is a transient example, not a counterexample to stationary independence. The reduction and example use elementary identities; no novelty claim is made for those identities.

The literature check took about four minutes. No verified resolution was found. Pooja Agarwal and Kavita Ramanan characterize hydrodynamic invariant states but leave the stationary-limit identification conjectural in the opened [arXiv:2008.08510](https://arxiv.org/pdf/2008.08510), Section 4.2. Reza Aghajani and Kavita Ramanan likewise distinguish transient results from stationary convergence in [arXiv:1707.02005](https://arxiv.org/pdf/1707.02005).

A claimed stationary result deserves further audit: Maria Clara Fittipaldi, Matthieu Jonckheere, Sergio I. Lopez, [arXiv:1809.05373](https://arxiv.org/pdf/1809.05373), Proposition 4.1. Its Section 4 invokes initial-law uniformity, whereas Proposition 2.1 explicitly concerns deterministic starts. The example proves that this distinction needs an additional argument. This session does not certify or refute the proposition through a complete audit of the paper. No SOLVED_ELSEWHERE.md was created.

Validation was symbolic: conditional variance versus a direct joint-event calculation; inclusion-exclusion versus a union bound; exact t=0 values; N=d; replacement sampling; and the time-one boundary. The product-test proof independently checks the k(k-1)/(2N) sampling error. Details and limitations are in PROOF.md and LOG.md.

Commands: literature used the web search/open/find tool; files were written with apply_patch. Local checks used `OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c 'wc -l PROOF.md LOG.md'`. No computation script or numerical data is claimed. The shell reported a priority-setting restriction; no heavy computation was run. No git, external writes, or subagents were used.

What remains unproved: convergence and uniqueness of the one-server stationary marginal; the additional conditional-mean concentration; and the original arbitrary-G stationary product-limit assertion. The stationary occupation/tightness idea initially considered was replaced before proof work.

Next worker: audit the deterministic-to-stationary passage in arXiv:1809.05373 before treating its claim as a solution. For a constructive continuation, prove estimate (14) of PROOF.md at times t_N for which the conditional fluctuation error also tends to zero. An estimate only for queue-length tests will not establish the full-state assertion.

Task: “Open problem T430: Asymptotic independence in the supermarket model with general service times”; received 2026-11-14 approximately 22:16 Asia/Tbilisi (18:16 UTC).
