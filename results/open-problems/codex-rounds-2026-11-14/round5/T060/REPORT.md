VERDICT: PARTIAL a competing ground state's norm distance survives removal of every finite interval, conditional on the published local gap inequality

The new result beyond round 4 is proved in [PROOF.md](PROOF.md). For the known state omega and every competing algebraic ground state rho,

`||(rho-omega)|A_(I^c)|| = ||rho-omega||`

for every finite interval I. Thus a ground state whose discrepancy vanishes in norm outside growing intervals equals omega. Any distinct pure ground state would remain perfectly distinguishable from omega outside every finite interval: the distance there is exactly two, without the factor one half. These are general deductions from the local gap premise; no literature priority is claimed.

The proof splits a competitor into a normal ground-state component p omega and a disjoint ground-state component of weight 1-p. It verifies that the components are ground states, rather than assuming this from convexity. Removing a finite interval removes a finite matrix tensor factor and preserves the sector weight p. Both the full norm distance and every complement norm distance are exactly 2(1-p). Equivalently, for each fixed n, the reduced-state trace distances on `[-m,-n-1] union [n+1,m]` increase to the full norm distance as m tends to infinity. Purity of omega is not needed for this result.

Round 4's normal-sector exclusion holds. It was re-derived using purification and negative-frequency averages, independently of its trace-class eigenvector decomposition. The frequency sign was checked in a two-level system. The new factor two was checked using both central projections and positive/negative functional masses, and directly in a ferromagnetic Ising chain whose product-state GNS gap is exactly two. No numerical computation was required.

The external spin-1 premise remains **Hal Tasaki**, *On the uniqueness of translation-invariant ground states of the S=1 Heisenberg and J–D antiferromagnetic chains*, [arXiv:2610.34330v2, Theorem 2.1, equation (2.12)](https://arxiv.org/html/2610.34330v2). Its finite numerical inputs were not independently verified. The bounded literature check found no later resolution of unrestricted uniqueness.

The stronger attempted inference from round 3's density condition fails. A product configuration with defects at powers of two has vanishing fixed-block discrepancy density but distance two on every complement. The proof gives the uniform density count and checks that this configuration violates local stability in the Ising test model. Another limitation is that distance strictly below two forces equality only for a pure competitor; mixtures can have any distance 2(1-p). The complement algebra includes joint observables on both sides of the removed interval, of unrestricted finite support size. No estimate for one half-chain alone is proved.

Readback and validation commands:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /bin/sh -c 'wc -l -c LOG.md PROOF.md; cat PROOF.md; date "+%Y-%m-%d %H:%M:%S %Z"'
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /bin/sh -c 'head -n 1 REPORT.md; wc -l -c REPORT.md PROOF.md LOG.md; test -s REPORT.md && test -s PROOF.md && test -s LOG.md; rg -n "tag|purity|irreducib|finite-range" PROOF.md'
```

Detailed outputs and the final audit are in [LOG.md](LOG.md). The sandbox rejected priority adjustment with `nice: setpriority: Operation not permitted`; only short file operations ran. No scripts, git, subagents, external messages or outside writes were used.

Unrestricted Heisenberg uniqueness remains unproved. The next step needs a Hamiltonian-specific bound on joint observables in the two exterior intervals, uniform in their lengths. One sufficient target for excluding a pure competitor is to bound its exterior trace distances by `2-eta`, for some eta>0 and one fixed removed interval, uniformly as the exterior blocks grow. Existing fixed-support density convergence does not provide that bound. For a general mixed competitor the theorem instead requires an estimate forcing p=1; a merely positive p is insufficient. No such estimate is established here.

Task: “take the NEXT checkable step on this problem, building on that work” — November 15, 2026, 07:48:50 Asia/Tbilisi (first retained explicit clock).
