# Source and scope check: uniform cyclic backbone extension

Checked 3 October 2026 UTC.  This is a bounded primary-source/status search,
not a historical priority certificate.

## Closest current work

Idriss Olivier Bado, *Negative edge correlation for uniform random forests
on wheel graphs*, Statistics & Probability Letters 241 (2026), 110960,
published online 6 September 2026,
https://doi.org/10.1016/j.spl.2026.110960, proves strict pairwise edge
negative correlation for the **unit-weight wheel graph** by a 2x2 transfer
matrix, treating spoke--spoke, rim--rim, and spoke--rim pairs.  That is close
and must be credited.  The theorem in this bundle is structurally different:
the cycle is a backbone for four additional vertices, the marked edges join
two disjoint pairs of those vertices, the common rim activity is arbitrary,
and the spoke row factors are arbitrary.  Its input is a complete
Chebyshev factorization of the one-apex spoke polynomial, followed by the
previously audited four-core identity.  No claim of historical novelty is
made without a broader specialist search.

The general conjectural context remains:

- Grimmett--Winkler, *Negative association in uniform forests and connected
  graphs*, https://arxiv.org/abs/math/0302185.
- Ciceksiz--Ravichandran, *Negative Correlations for Forests and the q<1
  Random Cluster Model*, arXiv:2610.00549, v1 submitted 30 September 2026.
- Gupta, *Edges of the uniform random forest of K_n are pairwise negatively
  correlated for every n*, arXiv:2609.26134.

These sources do not, as stated, settle arbitrary weighted finite graphs or
the present four-external-vertex proportional-attachment family.

## Exact scope

Proved here: a simple cycle `C_n`, `n>=3`; one common finite nonnegative rim
activity; one common positive vertex profile; arbitrary nonnegative four
row factors; and two positive marked-edge activities.  The pair is NC at
all activities and is strict iff all four row factors are positive.  Any
rim-edge cylinder conditioning forcing at least one rim edge absent reduces
to the prior arbitrary-profile forest theorem.

Not proved: unequal rim activities, unequal profiles on an unconditioned
cycle, conditioning that only contracts rim edges, arbitrary cyclic
backbones, individual spoke fields, arbitrary marked positions, or
whole-vector negative association.  The full forest/arboreal-gas conjecture
remains open.  Internal exact checks and audits are not external peer review.

