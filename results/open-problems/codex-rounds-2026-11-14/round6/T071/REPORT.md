VERDICT: PARTIAL exact rank-occupation formula for the filtered descendant kernel

The round-5 propagation estimate holds. Its independent recheck is in
[LOG.md](LOG.md). The opening literature check found no later solution;
the N-BBM genealogy conjecture remains unproved here.

## New beyond round 5

[PROOF.md](PROOF.md) simplifies its selection correction exactly. For a
homogeneous multilinear degree-four family polynomial F, and b the color
of the current leftmost particle,

    generator F = 4F-(N+3)partial_b F.

Thus the loss depends on a single spatially identified derivative. The
previous report left it as a sum over all possible branching parents.

The proof also represents the full four-distinct-root descendant kernel:

    E[W_a(L)W_b(L)W_c(L)W_d(L)]
      = exp(4L) E^circ exp(-(N+3)A_L).

Here four distinguished particles branch at rate two and other particles
at rate one. The conservative auxiliary process suppresses births while
its minimum is distinguished; A_L is the time spent in that condition.
This is an explicitly specified auxiliary spatial law. A killed version,
with ordinary leftmost deletions, gives the identity by marked-history
counting. Its killing rate is N+3 when its minimum is distinguished.

Summing over the frozen admissible quadruples retains both the terminal
weights and the older-ancestor filter. Equations (7)–(9) give conditional
identities, and (13) averages over the genuine younger forest in the
regime tau_N=(log N)^4, a_N=(log N)^3. This identifies the spatial
exponential moment required by the previous averaged criterion.

The argument works for k distinct roots, with growth k and killing
coefficient N+k-1. It yields a uniform occupation lower-tail constraint,
(11), but that bound alone returns the elementary descendant-product
bound. These are auxiliary finite-N identities; no literature novelty is
claimed.

## Verification and limits

[AUDIT.md](AUDIT.md) checks the coefficient by direct monomial expansion
and the kernel formula by an independent generator intertwining. When
k=N, direct extinction gives exp(-(N-1)L); the occupation formula gives
exactly the same value. In particular N=k=4 gives exp(-3L). For one root
chosen uniformly, mass conservation gives the independent exact check
E^circ exp(-N A_L)=exp(-L). Empty filters, extinct colors, ties, same-color
deletions and endpoint times were checked.

Replacing this auxiliary law by ordinary N-BBM fails. Assuming uniform
distinguished ranks fails for the ancestral-filtered tuple mixture.
Mean occupation cannot upper-bound the needed exponential moment by
Jensen's inequality. No averaged log-cubed-time kernel estimate, marked
transform limit, physical rate constant or genealogy convergence was
obtained. The original problem remains open in this work.

## Literature and commands

The web check ended between the readbacks at 10:24:25 and 10:26:17
Asia/Tbilisi, within five minutes. Opened primary sources:

- [Pascal Maillard, arXiv:1304.0562v4](https://arxiv.org/html/1304.0562v4):
  front speed and fluctuations.
- [Alexandre Legrand and Pascal Maillard,
  arXiv:2402.04917](https://arxiv.org/abs/2402.04917): still v4, 9 April
  2026, displacement results.
- [Julien Berestycki and Oliver Tough,
  arXiv:2407.05792](https://arxiv.org/abs/2407.05792): stationary empirical
  measure selection principle.
- [Jacob Mercer, arXiv:2605.04860](https://arxiv.org/abs/2605.04860):
  rank selection, hydrodynamics and velocity.

No qualifying solution was located. This bounded search does not certify
absence from the literature. No SOLVED_ELSEWHERE.md was created.

Read all four predecessors' REPORT.md, LOG.md and PROOF.md; their folders
contain no mathematical scripts. Verification was analytic. Commands and
outputs are recorded in LOG.md, including

    env OMP_NUM_THREADS=1 nice -n 15 sh -c 'cat PROOF.md; date "+%Y-%m-%d %H:%M:%S %Z"'
    env OMP_NUM_THREADS=1 nice -n 15 sh -c 'cat AUDIT.md REPORT.md; wc -l LOG.md PROOF.md AUDIT.md REPORT.md'

The sandbox rejects the requested priority change with
`nice: setpriority: Operation not permitted`. No numerical workload or
background job was launched. All writes stayed in this folder. No git,
subagents, external messages or predecessor edits were used.

## Next checkable step

Estimate the filtered sum of auxiliary survival probabilities in (13)
after averaging over the actual younger marked configuration. A concrete
target is round 4's uniform quadratic bound in delta, or its weaker
integrated criterion. Any estimate must retain the dependence of the
admissible quadruples on positions and older ancestry, and control the
occupation exponential with the exp(4L) factor restored. The lower-tail
bound (11) and a mean-occupation estimate alone are insufficient.

Even successful disjoint-burst exclusion would leave both four-lineage
transform limits from round 3 and larger sample sizes.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, approximately 10:24 Asia/Tbilisi.
