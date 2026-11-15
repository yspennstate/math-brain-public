VERDICT: PARTIAL exclusion of normal competing ground states, conditional on the published local gap inequality

The new result beyond round 3 is proved in [PROOF.md](PROOF.md): every algebraic ground state normal in the GNS representation of the known state equals that state. This excludes arbitrary local filtered defects, finite mixtures of them, and their limits in the norm of state functionals. Round 3's density conclusion alone did not exclude these possibilities. This is a general consequence of the gap premise, with a complete argument supplied here; no literature priority is claimed.

The external spin-1 premise is the local gap inequality in **Hal Tasaki**, *On the uniqueness of translation-invariant ground states of the S=1 Heisenberg and J–D antiferromagnetic chains*, [arXiv:2610.34330v2, Theorem 2.1, equation (2.12)](https://arxiv.org/html/2610.34330v2). Its finite numerical inputs have not been independently verified. The bounded literature check found no later resolution of unrestricted uniqueness.

The proof uses negative-frequency averages, which annihilate a ground vector in any ground-state representation. A trace-class decomposition transfers this annihilation to the vectors representing a normal competitor. Matrix elements against the known ground vector then eliminate every strictly positive-energy component; the gap inequality makes the zero-energy subspace one dimensional. No translation invariance is assumed for the competitor.

A separate direct calculation checks local unitary defects and supplies a quantitative statement: a block trace distance at least epsilon forces a local-stability violation at most `-gamma*epsilon^2/4`, where gamma is the local gap lower bound and trace distance has no factor one half. Both the sign and the coefficient were checked independently; the coefficient is sharp for the general premises in a two-level example.

The earlier density result holds: it was re-derived using measures on the compact ground-state set, pure-state barycenters, and continuity of block trace distance. The attempted extension from normal competitors to arbitrary local limits fails. An explicit product-state example in PROOF.md proves that weak-* limits of local unitary defects can leave the normal folium. Thus density convergence cannot simply be substituted for normality.

No numerical experiment or computation script was needed. Readback and artifact commands were:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /bin/sh -c 'wc -l -c LOG.md PROOF.md; sed -n "1,280p" PROOF.md'
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /bin/sh -c 'head -n 1 REPORT.md; wc -l -c REPORT.md PROOF.md LOG.md; test -s REPORT.md && test -s PROOF.md && test -s LOG.md'
```

The sandbox reports `nice: setpriority: Operation not permitted`; only short file operations ran. Detailed queries, commands, symbolic checks and limitations are in [LOG.md](LOG.md). All new artifacts are in this folder; earlier folders were read only.

Unrestricted uniqueness remains unproved. The next worker should investigate a Hamiltonian-specific normality criterion for a competing state satisfying round 3's density restriction. One concrete sufficient target is to construct local-filter mixtures converging locally to that state whose density operators in the known GNS representation are uniformly tight on finite-rank subspaces. Such tightness would give a trace-norm convergent subsequence and hence normality; local convergence by itself is insufficient. No such tightness estimate is established here.

Task: “take the NEXT checkable step on this problem, building on that work” — November 15, 2026, 04:31:30 Asia/Tbilisi (first recorded clock).
