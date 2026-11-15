VERDICT: PARTIAL profile-well implication proved; converse fails for explicit correlated binary Hopfield patterns

The earlier report's main scope conclusion holds: the located equilibrium
formula and the claimed well-capacity threshold do not by themselves
establish T347's iff statement about individual local minima. The bounded
update search found no newer solution. No SOLVED_ELSEWHERE.md is warranted
for this session.

New beyond the earlier report: [PROOF.md](PROOF.md) gives a finite-volume
proof that a strict gap between two shell ground-state energies traps a
local minimum in the inner Hamming cap. It states the correct stability
condition with the diagonal removed and makes the simultaneous-pattern
probability requirement explicit. With iid patterns, sufficiently small
caps give distinct minima by a binomial tail bound.

The converse is tested rather than assumed. An exact 12-spin, 11-pattern
example has a monotone positive-overlap shell profile and a strict local
minimum that is suboptimal on its own shell. A Walsh/block construction
extends this to extensive load M/N -> 11/B: every stored pattern has a
strict local minimum within twelve flips, yet all limiting shell profiles
are constant. The minimum single-flip cost stays bounded away from zero.
For B=79 the limiting load is 11/79 = 0.139240506329..., but the patterns
are correlated. This is a counterexample to a general landscape inference,
not to an iid capacity theorem. The asymptotic proof uses elementary
uniform bounds and does not depend on exhaustive shell maxima.

Reproduction, from this folder:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit_landscape.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit_blocks.py
```

[counterexample.json](counterexample.json) is the exact finite certificate.
The base verifier checks all 4,096 energies using both pattern projections
and the Gram quadratic form, and checks each flip from its local field.
The block verifier checks every Gram entry of an actual 18-spin,
44-pattern array, enumerates all 262,144 states independently of its block
dynamic program, and checks all flips at the minima near every pattern.
Both scripts passed; the block run took 1.138 seconds. All computations
used one thread and small memory. The sandbox rejects changing inherited
niceness 20 to 15; actual verified priority was 20 throughout.

What failed: the first search selected a minimum that was shell-optimal,
which failed an extra certificate assertion. The search was corrected to
require suboptimality on its own shell; the successful example is seed
347, trial 620. There was no failure of the earlier report's mathematical
claim. The earlier folder contained no PROOF.md or computation scripts.

Limits and uncertainty: no new iid existence bound, exclusion bound,
threshold value, or replica-symmetric free-energy theorem is proved.
The full variational proof, uniform strict merging inequality and numerical
capacity certificates remain unaudited. The asymptotic counterexample has
a flat profile and strong correlations; it leaves open an exclusion theorem
using strict decrease plus quantitative iid information. A positive-
temperature free-energy gap alone is not the ground-state gap used here.

Next worker: take the iid upper direction seriously as a separate lemma.
Fix a numerical overlap/error criterion, and seek a uniform estimate for
the existence of shell-suboptimal single-spin minima in that cap when
the limiting profile is strictly decreasing. If instead auditing the
capacity preprint, check its merging and interval certificates first;
its barrier statement plus Proposition 1 here gives the lower landscape
implication only, conditional on that preprint's correctness.

Opened primary sources: Ayman Ali, Jeanne Boursier, Hong-Bin Chen,
Fu-Hsuan Ho, Victor Issa, Jean-Christophe Mourrat, *Free energy of the
Hopfield model*, [arXiv:2611.03306v1](https://arxiv.org/html/2611.03306v1);
*THE CRITICAL CAPACITY OF THE HOPFIELD MODEL*, contributed by Yuwen Zhou,
[Hexagon 2611.00105v1](https://hexagonmath.org/pdf/2611.00105v1).
Both still show only v1. Detailed commands, output and scope checks are in
[LOG.md](LOG.md).

Task: “take the NEXT checkable step on this problem, building on that work.” Start: 15 November 2026, 03:50 +04.
