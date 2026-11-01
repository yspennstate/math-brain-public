# Source and scope check: arbitrary weighted-cycle backbone

Checked 3 October 2026 UTC.  This is a bounded current-source search, not a
historical priority certificate.

## Closest identified work

Idriss Olivier Bado, *Negative edge correlation for uniform random forests
on wheel graphs*, Statistics & Probability Letters 241 (2026), 110960,
published online 6 September 2026,
https://doi.org/10.1016/j.spl.2026.110960, proves strict pairwise edge
negative correlation for unit-weight wheel graphs using a multivariate 2x2
transfer.  It treats pairs of actual wheel edges.  That is important and
closely related prior work.

The theorem here has a different graph family and conclusion: an arbitrary
weighted cycle is a backbone; four external vertices have arbitrary
proportional spoke rows over an arbitrary nonnegative vertex profile; and
the marked edges join two disjoint pairs of external vertices.  Its new
input is real-rootedness of the **one-apex spoke-activity polynomial** for
every weighted cycle/profile, proved through a quasi-periodic Hermitian
transfer.  The previously audited four-core identity then supplies the
marked-pair inequality.  No assertion of historical novelty is made without
external specialist review.

The broader primary context remains:

- Grimmett--Winkler, *Negative association in uniform forests and connected
  graphs*, https://arxiv.org/abs/math/0302185.
- Ciceksiz--Ravichandran, *Negative Correlations for Forests and the q<1
  Random Cluster Model*, arXiv:2610.00549, v1 submitted 30 September 2026.
- Gupta, *Edges of the uniform random forest of K_n are pairwise negatively
  correlated for every n*, arXiv:2609.26134.
- Borcea--Branden--Liggett, *Negative dependence and the geometry of
  polynomials*, https://arxiv.org/abs/0707.2340, for established stable-
  polynomial and strong-Rayleigh background.

None of these sources, as stated, resolves arbitrary weighted finite graphs
or the four-external-vertex family proved here.  The general conjecture is
still described as open in the current 2026 sources.

## Exact scope and exclusions

Proved: every finite nonnegative activity assignment on a cycle, every
nonnegative common profile, arbitrary nonnegative four row factors, every
positive marked-edge field, and every positive-probability rim coordinate
conditioning.  Strictness is exactly four positive row factors and at least
two positive contracted profile components.

Not proved: backbones with two independent cycles or more, nonproportional
spoke rows, individual spoke fields, arbitrary marked positions, arbitrary-
event conditioning, or negative association of the whole indicator vector.
The full forest/arboreal-gas conjecture remains open.  Internal audits and
exact computations are not external peer review.

