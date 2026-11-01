# P04 Theorem 31 scope addendum

This immutable addendum records one scoping point noticed after the exact-commit readback of `2026-09-17T21-42-30Z__run-report.md`. The report itself is not edited.

Theorem 31 is stated correctly for any finite simple graph `K` **whose fractional perfect-matching polytope `F(K)` is nonempty**. In the P04 specialization, the notation `mu_p=mu(K_p)` and the universal-embedding equivalence are therefore to be read under the same hypothesis `F(K_p) != empty` (equivalently, there exists at least one symmetric zero-diagonal stochastic matrix supported on `K_p`).

For the stronger positive-Markov sufficient route this is not an additional source-level assumption: nonemptiness is a prerequisite of the route itself. If `F(K_p)` is empty, that stronger route simply fails at that prime and Theorem 31 does not define `mu_p` there. The source Conjecture 27 is unaffected because the positive-Markov route is only sufficient, not equivalent to theta feasibility.

No all-prime proof of `F(K_p) != empty` is promoted in this run. Any future asymptotic use of Theorem 31 must either establish nonemptiness for the relevant prime family or build the stochastic chain directly, which establishes it automatically.

This addendum changes no metric, no status, and no theorem statement; it only makes the P04 application domain explicit.
