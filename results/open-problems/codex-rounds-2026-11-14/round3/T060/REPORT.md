VERDICT: PARTIAL uniform-density restriction on competing ground states, assuming the published translation-invariant uniqueness and purity theorem

The new result beyond the earlier report is in [PROOF.md](PROOF.md): every algebraic ground state agrees with the known state's marginal on any fixed block outside a set of positions of vanishing upper Banach density. Convergence is uniform over competing ground states and starting positions of the averaging intervals. The mean block trace distance tends to zero as well. In particular, every ground state with any finite translation period equals the known state.

The external premise is the uniqueness and purity assertion in **Hal Tasaki**, *On the uniqueness of translation-invariant ground states of the S=1 Heisenberg and J–D antiferromagnetic chains*, [arXiv:2610.34330v2, Theorem 2.1](https://arxiv.org/html/2610.34330v2). The proposition is proved here from that premise, using compactness, translation averages and purity. It requires no additional numerical inputs. This is a new deduction relative to the earlier report; no literature priority is claimed for the abstract lemma.

The earlier report's main scope distinction holds. Its periodic-gap implication was independently re-derived from Gibbs probabilities, including ground-state multiplicity and the strict lower bound log(20)/784, conditional on the published purity estimates. There was no earlier computation or PROOF.md to rerun. Neither session independently certifies the finite trace inputs. The bounded literature check found no later resolution of unrestricted infinite-volume uniqueness; the already reported periodic result does not resolve that remaining question. The opened sources and queries are in [LOG.md](LOG.md).

The audit gives two proofs of finite-period exclusion and two independent matrix-norm estimates. It also supplies a fully worked single-defect example showing why compactness, purity and averaging alone cannot imply equality of all states. That example is a set of states, not a Heisenberg ground-state construction. Thus the attempted extension to full uniqueness fails at an identified point: sparse discrepancies remain possible under the abstract premises.

No computation script or numerical experiment was needed. Readback and final artifact checks used:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /bin/sh -c 'wc -l -c LOG.md PROOF.md; sed -n "1,240p" PROOF.md'
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /bin/sh -c 'head -n 1 REPORT.md; wc -l -c REPORT.md PROOF.md LOG.md; test -s REPORT.md && test -s PROOF.md && test -s LOG.md'
```

The sandbox rejected priority adjustment with `nice: setpriority: Operation not permitted`; only brief file reads ran. The original paper's mirror also failed to reopen. All writes stayed in this folder; no git, subagents, external messages or heavy workloads.

There is no quantitative convergence rate for Heisenberg competitors, no independent certificate verification, and no proof of unrestricted uniqueness or of the general integer-spin assertion. The next worker should use the Heisenberg local stability condition to prove a discrepancy-amplification lemma: if a competing ground state differs on some finite block, then some fixed-size local discrepancy occurs on a set of positive upper Banach density. Combined with the proposition, such a lemma would imply unrestricted uniqueness. The single-defect example shows that this step needs Hamiltonian-specific input.

Task: “take the NEXT checkable step on this problem, building on that work” — November 15, 2026, 01:06:28 Asia/Tbilisi (session start).
