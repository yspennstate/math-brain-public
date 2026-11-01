# Source and scope check: cactus-backbone determinant gluing

Checked 3 October 2026 UTC. This is a bounded current-source search, not a
historical priority certificate or external peer review.

## Closest identified sources

Brand--Dell--Roth, *Fine-Grained Dichotomies for the Tutte Plane and Boolean
#CSP* (IPEC 2016), Lemma 7,
https://doi.org/10.4230/LIPIcs.IPEC.2016.9, records the established general
component formula after adding an apex:

    F(G+apex)=sum_(A forest of G) w(A)
                   product_(C component of A)(1+sum_(v in C)z_v).

That identity is credited. It does not state the negative-real-root theorem
for proportional apex activities on cactus graphs, the profile-uniform
positive-definite determinant representation, the rank-one leaf lift, or the
one-vertex-sum determinant gluing proved here.

Huang, *On Negative Correlation of Arboreal Gas on Some Graphs*,
https://arxiv.org/abs/2311.00965 (v1, 2 November 2023), proves a reduction by
deleting pivotal edges and smoothing degree-two vertices, and gives special
graph consequences. Ordinary backbone-edge correlation on a bare cactus is
not the present conclusion. Here four external vertices have potentially
many proportional spokes and two disjoint external marked edges; the full
augmented graph is generally highly multicyclic.

Idriss Olivier Bado, *Negative edge correlation for uniform random forests
on wheel graphs*, Statistics & Probability Letters 241 (2026), 110960,
published online 6 September 2026,
https://doi.org/10.1016/j.spl.2026.110960, proves strict pairwise edge
negative correlation for unit-weight wheel graphs. The present theorem has
arbitrary weights, arbitrary cactus block trees, an arbitrary nonnegative
common profile, and a different pair of external marked edges. Bado's
closely related cycle-transfer result remains important prior work.

The current broader primary context is:

- Grimmett--Winkler, *Negative association in uniform forests and connected
  graphs*, https://arxiv.org/abs/math/0302185.
- Ciceksiz--Ravichandran, *Negative Correlations for Forests and the q<1
  Random Cluster Model*, https://arxiv.org/abs/2610.00549, v1 submitted
  30 September 2026. Its full paper treats general structural identities and
  high-fugacity regimes, not this finite-activity external-core family.
- Gupta, *Edges of the uniform random forest of K_n are pairwise negatively
  correlated for every n*, https://arxiv.org/abs/2609.26134.
- Borcea--Branden--Liggett, *Negative dependence and the geometry of
  polynomials*, https://arxiv.org/abs/0707.2340, for established stable-
  polynomial and strong-Rayleigh background.

The bounded exact-phrase and subject searches found no primary source
stating the profile-uniform `DR` leaf/one-sum closure or this precise cactus-
backbone marked-pair theorem. Absence from a bounded search does not prove
novelty. The general forest/arboreal-gas negative-correlation conjecture is
still described as open in the 2023 and September 2026 primary sources.

## Exact new scope

Proved internally: every finite weighted cactus (each block an edge or a
cycle), arbitrary nonnegative backbone activities and profile, four arbitrary
nonnegative proportional row factors, positive marked fields, and arbitrary
positive-probability backbone cylinder conditioning. The apex polynomial has
a positive-definite determinant representation uniform in the profile,
constructed from the cycle transfer, a rank-one leaf lift, and exact
one-vertex-sum gluing. In particular the full multivariate apex-spoke
polynomial is real stable, so the whole spoke indicator vector is strongly
Rayleigh/negatively associated by established Borcea--Branden--Liggett
theory. The separate marked pair is strict exactly for four positive row
factors and at least two positive contracted profile blocks.

Not proved: a 2-connected block with two independent cycles (including theta
graphs), nonproportional spoke rows, arbitrary marked positions,
arbitrary-event conditioning, or whole-vector negative association involving
backbone or external marked edges. Internal audits and exact computations are
not external peer review.
