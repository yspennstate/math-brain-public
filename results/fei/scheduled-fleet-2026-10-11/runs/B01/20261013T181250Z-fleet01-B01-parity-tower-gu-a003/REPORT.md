# B01 / A003 — depth-uniform GU' transfer for parity-balanced towers

## Outcome

**AUTHOR-PROVED RESTRICTED ALL-DEPTH THEOREM; INDEPENDENT REVIEW PENDING.**

The previous one-step activation theorem bounded a fresh balanced
activation by charging its logarithmic term to the core's full influence.
Naively iterating that estimate recharges inherited influence at each
ancestor.  This run derives the exact recurrence on parity-balanced towers
and removes that depth loss.

For every Boolean base (P) and every depth (d\ge1),
[
G(T_d(P))
=2^{-d}G(P)+2^{-(d-1)}(1+\phi(\math EP))
+2(1-2^{-(d-1)})(1+\phi(1/2)),
]
where (phi) is the explicit one-dimensional function in `PROOF.md`.
In particular,
[
G(T_d(P))\le2^{-d}G(P)+K_*,
qquad
K_*=\frac{15}{4}-\frac{27}{16}\log_2\frac43
=3.049624219966\ldots.
]

Thus, for (a\ge0) and (0\le b<1),
[
G(P)\le aI(P)+bU(P)
\Longrightarrow
\boxed{G(T_d(P))\le(a+K_*)I(T_d(P))+bU(T_d(P)).}
]
The crucial contraction coefficient (b) is preserved exactly, while the
increase in (a) is independent of base dimension, depth, and terminal
rarity (2^{-d}).

## New mechanism

Character balancing preserves (G).  For one activation of (wf), the
old-coordinate charges equal (G(f)/2), the selector charge is one, and
the balancing-coordinate charge is the scalar (phi(\math Ef)).  After
the first tower level, every activated core has mean (1/2).  Consequently
all later balancer charges are the same scalar (phi(1/2)); inherited
influence is not recharged.

This is the exact first-activating-ancestor mechanism sought in the prior
B01 handoff, but only for the fresh parity-balanced tower.

## Class extension and constants

- Previous scope: one half-activation of an arbitrary balanced core, with
  (G(F)\le G(g)/2+1+c_1I(g)).
- New scope: arbitrary depth, with a single absolute loss (K_*<3.05)
  rather than a depth-dependent sum of inherited influences.
- Preserved quantities: any base GU' coefficient (b<1), and any base
  endpoint (U\le cI) with (c\ge1).
- FEI consequence on the class: if (U(P)\le cI(P)), then
  (H(T_d(P))\le(2+2c)I(T_d(P))).

## Validation

`CHECK_PARITY_TOWER_GU.py` independently reconstructs (U,I,G) from
truth tables.  It checked 328 bases, 1,312 exact recurrence instances and
1,312 GU-transfer inequalities through depth four.  The maximum recurrence
error was (2.220\times10^{-15}).

## Corrections respected and remaining gap

The independent B19 review at canonical commit
`bd2e6e221df971c9cc456467361587373c43ee1c` is adopted: positive-depth
towers are not restriction-closed, and a root endpoint telescope is not a
nodewise ownership proof.  The present result is stronger than that
endpoint statement because it computes the aggregate (G) recurrence, but
it remains limited to fresh fair selectors and exact parity balancing.

Biased selectors, imperfect balancing, variable reuse, and arbitrary
changing coherent cores remain open.  Full FEI remains **OPEN**.

## Source pins

- owner control revision 2026-10-12.1, source commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`;
- A003 assignment blob
  `ac038a028831d59ad053dd56b2b527e2a71ffdee`;
- prior balanced one-step theorem: commit
  `94e79f7d962e63d19442fc55dd872712503b3dee`, proof blob
  `bb5dbd89886a471d91366ad04882deb5130fc166`;
- B19 parity-tower scope review: canonical commit
  `bd2e6e221df971c9cc456467361587373c43ee1c`, Brain commit
  `78633cd19d328b5c6795c656f7c55acd6ae14c65`.

## Next action

Replace the exact parity balancer by a core with mean/correlation defect
(\eta), derive the perturbed scalar charge, and determine whether its
errors have summable contraction or require a new physical ownership
credit.  Route the present theorem to A086/A094, B05, B18, and B20.

## Delivery

The complete bundle was delivered to the canonical repository at commit
`b5556598b8164779f870183fac94fdd858451ea1` and mirrored to the Brain
handoff route at commit
`20b252aa2a7aa21a020e61d3840636c5d3de0133`.  Independent review and
native adoption remain pending.

