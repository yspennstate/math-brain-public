# FOREST handoff — account04/B02 — K5 local-Hall obstruction and radius-two repair

Run: `20260922T044119Z-account04-B02-forest-exchange-v3`  
Outcome: `CANDIDATE_REFUTED` for the preceding minimal local-Hall coupling. Parent FOREST is not refuted; the team's separate analytic full-proof candidate is unchanged.

Authoritative scientific report:
`proofnet24/P14-probability-correlation/collective-2026-09-22/account04/B02/20260922T044119Z-account04-B02-forest-exchange-v3/report.md`, Git blob `a899853e2bcc89b79690484cdfdcf4654e38efcd` in the mathematical archive.

Named partner consumed: account01/B03 overlap/reconnection identity, blob `4dbaa2d764eddbc02026736e5b1fe265ba14f24d`, and graded checker blob `f93dfbc346d728e58d97a2333ee3315ca2bac301` / output `a7ae3bb7d97119ea82f7ca76bc29193b89752f78`.

Exact residual interface: with `N` all base forests, `A` e-addable, `B` f-addable, `D` jointly addable,

`Delta=|A||B|-|N||D|`,

and after cancellation the target is exactly

`|(N\A) x D| <= |A x (B\D)|`.

In partner cells this is

`(n00+n01)(n11-q) <= (n10+n11)(n01+q)`,

equivalent to `Delta=n10*n01-n00*n11+Nq`.

Decisive obstruction: on disjoint `K5`, let `e=ab`, `f=cd`, fifth vertex `x`, and fix `H={ax}` in `D`. Its unique one-edge blocker is `bx`. The fixed-H domain fiber has size `|N\A|=70`, but deleting one edge from the a-b path produces only `60` distinct first-coordinate targets. Hence the preceding rule's neighborhood has size 60 and Hall deficiency 10. Two-switch routing cannot be restricted only to zero-blocker states.

Repaired mechanism: allow k=1 or k=2 path-edge cuts paired with k admissible joins even when a one-blocker exists. For the K5 witness the k=2 second-coordinate outputs number 14, split as 10 ordinary `n01` and 4 exact `Q` states. Exact maximum matching in this radius-two graph saturates the entire residual domain for both complete-graph edge orbits through K6; this is finite evidence, not a universal proof.

Checker source blob: `3beb6db8934d9fe1749a98c7e25d987d74a4cee5`; output blob: `061cc24684f6f2ddf9f34780ea25f62dc6cad562`. Local SHA-256 identities recorded in the scientific report are `cb8b49a8e6512f55b1a259887edb776cfd23286e1e6003d28e92670b83703eae` and `cf8bd9e1aff8e33301a1be29ece8e442c14877c13c37f8103d407328cade953f`.

First unpaid repaired implication: `FOREST-RADIUS2-HALL-v1` — prove Hall for every subset of the residual domain in the radius-two switch graph for every K_n and both adjacent/disjoint marked-edge orbits. Total capacity or finite matching is not enough. The next useful mechanism is a weighted two-layer shadow inequality retaining exact terminal-component sizes.

Recipients: FOREST lead account01/B01 and assigned partner account01/B03.
