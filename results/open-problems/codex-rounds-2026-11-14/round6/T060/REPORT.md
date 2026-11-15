VERDICT: PARTIAL any distinct pure ground state remains perfectly distinguishable in one fixed half-chain direction, conditional on the published spin-1 gap premise

The new result beyond round 5 is proved in [PROOF.md](PROOF.md). A distinct pure ground state rho must be disjoint from the reference state omega on every half-chain in at least one fixed direction. Consequently either

`||(rho-omega)|A_(-infinity,a]|| = 2 for every integer a`

or

`||(rho-omega)|A_[a,infinity)|| = 2 for every integer a`.

The corresponding finite connected-interval trace distances increase to two as the intervals grow. Round 5 required joint observables on two separated exterior intervals. This result places the witness in one direction. It gives no bound on the necessary interval length. No literature priority is claimed for this general deduction.

The spin-1 premise remains Hal Tasaki, *On the uniqueness of translation-invariant ground states of the S=1 Heisenberg and J–D antiferromagnetic chains*, [arXiv:2610.34330v2, Theorem 2.1 and (2.12)](https://arxiv.org/html/2610.34330v2). Purity and the local gap imply a split representation by Taku Matsui, *Boundedness of Entanglement Entropy, and Split Property of Quantum Spin Chains*, [arXiv:1109.5778, Corollary 1.6](https://arxiv.org/pdf/1109.5778). The published finite numerical premises were not independently certified. The bounded initial search found no later resolution of unrestricted uniqueness.

Round 5's exact exterior-norm identity holds. Its finite-deletion step was checked independently using intertwiners rather than bidual factorization; the distance 2(1-p) follows from the positive and negative masses of the sector difference. For the extension, each half-chain representation of a pure competitor is a factor. If neither is disjoint from the reference, both are normal in its type I factors. Joining them makes the competitor normal in the full reference representation, where the earlier normal-sector lemma forces equality. The joining step has two proofs: successive matrix-unit decompositions and finite-rank corner approximation. No gap or split assumption is imposed on rho.

An actual Ising kink ground state checks the boundary cases. It agrees with the reference sufficiently far left and has distance two on every right half-chain, so both directions cannot be required. Mixtures of that kink and the vacuum show that the strict-distance criterion needs purity. Mere norm distance two does not survive finite deletion; disjointness does. These distinctions are proved explicitly. No numerical computation or script was needed.

Readback and validation commands:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /bin/sh -c 'sed -n "1,125p" PROOF.md'
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /bin/sh -c 'sed -n "126,300p" PROOF.md'
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /bin/sh -c 'head -n 1 REPORT.md; wc -l -c REPORT.md PROOF.md LOG.md; test -s REPORT.md && test -s PROOF.md && test -s LOG.md'
```

The sandbox rejected priority adjustment with `nice: setpriority: Operation not permitted`. Only brief file operations ran. All new files remain here; no git, subagents, external messages or outside writes were used. Detailed checks are in [LOG.md](LOG.md).

Unrestricted Heisenberg uniqueness remains unproved. A concrete next target is a Hamiltonian-specific bound strictly below two for each of a pure competitor's left and right half-chain distances, with possibly different cutoffs. Equivalently, bound the connected-interval trace distances by `2-eta_L` and `2-eta_R`, uniformly in interval length, for positive eta_L, eta_R. The theorem would then exclude that pure competitor. Fixed-block density convergence supplies neither bound. No criterion for all mixed competitors or proof of the general integer-spin assertion is claimed.

Task: “take the NEXT checkable step on this problem, building on that work” — November 15, 2026, 10:17:39 Asia/Tbilisi (first explicit clock).
