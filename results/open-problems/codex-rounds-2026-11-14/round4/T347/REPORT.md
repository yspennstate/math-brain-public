VERDICT: PROVED strict decrease of a limiting shell profile does not exclude strict local minima for correlated binary Hopfield patterns

The round-3 result holds under independent rechecking. Its flat-profile
limitation is removed: [PROOF.md](PROOF.md) constructs distinct binary
patterns with a strictly decreasing limiting shell ground-state profile
around a stored reference, although that reference is a strict single-spin
local minimum with a positive limiting flip cost.

For K=2^q, B>=3, N=BK and M=2K-1, the construction has exact energy
numerator

Q=2K sum_z S_z^2-(sum_z S_z)^2.

At distance d from the all-positive stored reference, with r=d mod B,
the shell energy-gain profile is exactly

E_N(d)=1-m_d^2/2-4K r(B-r)/N^2.

It converges uniformly to E(m)=1-m^2/2, strictly decreasing on [0,1].
Nevertheless, exactly 2^K configurations are local minima: all states
constant within each block. Every stored pattern is one of them. All
are strict and every spin flip costs at least 2(1-M/N). At B=14, the
limiting load is 1/7 and the limiting minimum flip cost is 12/7.
The strict-decrease assertion concerns the constant stored reference,
not every stored reference. The patterns are correlated, with antipodal
pairs and repeated neuron rows inside blocks. This does not refute an
iid capacity theorem.

New beyond round 3: strict profile decrease replaces a flat profile;
the shell maximum is given by an exact formula; all local minima are
classified and counted; and every pattern is itself stable, with no
core correction. A block reversal gives a path to a lower-energy state
with a barrier of order one in total energy. Normalizing energy by N
removes this barrier even though the limiting profile has a strict slope
at the reference.

Reproduce from this folder:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 recheck_previous.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit_strict_profile.py
```

[recheck_previous.py](recheck_previous.py) uses weighted cuts to verify
the earlier 12-spin certificate and a different Walsh instance, with
65,536 states. [audit_strict_profile.py](audit_strict_profile.py) checks
all actual projection energies and all neighbors for instances up to
16 spins, independently checks shell optima by dynamic programming,
and checks stability at every stored pattern of a 224-spin instance.
The resource-audited run took 0.524 seconds and used 14.375 MiB peak RSS.
Actual niceness was 20: the sandbox rejects increasing it to 15.
Commands and exact output are in [LOG.md](LOG.md).

What failed: no mathematical verification failed. Boundary checks show
that B=1 loses reference stability and B=2 loses a positive limiting
margin. No iid exclusion bound was obtained. The AGS threshold and the
replica-symmetric free energy remain unresolved in this work.

The bounded literature update found no newer solution. Opened sources
still show only v1: Ayman Ali, Jeanne Boursier, Hong-Bin Chen, Fu-Hsuan Ho,
Victor Issa, Jean-Christophe Mourrat, *Free energy of the Hopfield model*,
[arXiv:2611.03306v1](https://arxiv.org/html/2611.03306v1); and Yuwen Zhou,
*THE CRITICAL CAPACITY OF THE HOPFIELD MODEL*,
[Hexagon 2611.00105v1](https://hexagonmath.org/pdf/2611.00105v1).
Their full proofs and numerical capacity certificates were not audited.

Next worker: an upper bound for iid retrieval minima needs an explicit
probabilistic estimate for simultaneous zero-diagonal stability within
a fixed numerical error cap. Strict decrease of a uniformly convergent
shell profile alone is insufficient, even with nonvanishing single-spin
stability and linearly many distinct stored patterns. Use this example
to test any proposed deterministic reduction before applying iid bounds.

Task: “take the NEXT checkable step on this problem, building on that work.” Start: 15 November 2026, 06:32 +04.
