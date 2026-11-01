# B05 / A023 — parity-balanced rare-activation towers

## Outcome

**AUTHOR-PROVED RESTRICTED ALL-PARAMETER THEOREM; INDEPENDENT REVIEW PENDING.**

The previous B05 endpoint controlled every adaptive restriction tree on one
fixed dense-nullity-two shield (P) by (2I(P)).  This run extends that
endpoint to a genuinely changing hierarchy: alternate a fresh parity
balancer with a fair half-activation for any depth (d).  The deepest core
then occurs with probability (2^{-d}), yet the complete retained
upper-set loss of any adaptive/pruned physical restriction tree is still at
most (2I), with no depth or rarity loss.

For the resulting tower (T_d(P)), the exact identities are
[
U(T_d(P))=2+2^{-d}(U(P)-2),qquad
I(T_d(P))=2+2^{-d}(I(P)-2).
]
Thus every base satisfying (U(P)\leq2I(P)) transfers to all depths.  In
particular, this applies to every rank-(m-2) dense shield from the prior
B05 theorem, including arbitrary terminal Boolean defect (D).

## Why this advances A023

The accepted local rare-refund obstruction rules out an all-node fixed
price.  Here the complete signed identity
(Delta_iU=B_i-\Gamma_i+KL_i) is not bounded node-by-node.  It telescopes
over the whole tree.  A common disjoint terminal core contributes the same
(U(h)) at the root and in leaf expectation, so that credit is retained and
cancels exactly once.  Fresh balancing characters ensure that the coherent
core can change at every rare layer without reusing a physical credit.

The new constant 2 is independent of:

- base dimension and rank-(m-2) orientation;
- the arbitrary defect (D);
- depth (d) and rarity (2^{-d});
- tree ordering and pruning;
- the common disjoint terminal core (h).

## Proof and verification

The analytic proof is in `PROOF.md`.  `CHECK_BALANCED_TOWER.py` independently
implements Walsh transforms and upper-set masses.  It exhausts all Boolean
bases through three variables modulo output sign, samples larger bases, and
checks depths 1--4, random pruned trees, and disjoint tensor cancellation.
The 1,076 formula checks have maximum error (2.220\times10^{-16}).

## Scope and unpaid step

This is a proper expanding restriction-closed class, not full FEI.  It uses
fair selectors, a fresh parity balancer at every level, disjoint terminal
variables, and a base with (U(P)\leq2I(P)).  Arbitrary selector bias,
balancer-free coherent cores, selector reuse/overlap, trees entering the
terminal core, and arbitrary core changes remain open.  The next useful
move is to replace exact parity balancing by a quantitative mean/correlation
defect and determine whether the resulting cumulative error has a
single-use pivotal payment.

## Source pins

- owner control: revision 2026-10-12.1, source commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`;
- assignment: `assignments/B05.json`, blob
  `05447e6d999437bb82a266b427bd76a4b37266b6`;
- protocol blob: `457358ff62cbf1141a72096bcabdf95bf18c1be2`;
- prior dense-nullity-two theorem: open-problems commit
  `97ee31ccf5dd58017837d3939ffb012af1ed034f`, proof blob
  `fc4325203296ff861c5692bf0aeac0288aa02fbf`;
- B01 balanced-activation credit (motivation only, not a proof dependency):
  commit `94e79f7d962e63d19442fc55dd872712503b3dee`, proof blob
  `bb5dbd89886a471d91366ad04882deb5130fc166`.

Full FEI remains **OPEN**.

## Delivery

The complete bundle was written to the canonical repository at commit
`454f0345d2e574a419fe92438293e8d7b64a9030` and mirrored to the Brain
handoff route at commit
`11257451a9f62300bdb70ee33374f41508cd9410`.  Independent review and
native adoption remain pending.

