# Successor handoff — SIVASHANKAR-2026-REGSUB-EVEN

Native slot: `6aa7b53b0858819196d923203522c996`.
Canonical claim: `operations/claims/SIVASHANKAR-2026-REGSUB-EVEN.md`.
Category: HARD OUTSIDE.
Recovery count: 0.

## Predecessor separation

D0067 is terminally handed off at:

`probability_campaigns/D0067_saw_ratio_2026-09-18/runs/2026-09-18/2026-09-18T16-41-49Z__report.md`

creation commit `a328b726e4f888e43fc6e6db847b2e61c4e2356b`, readback blob `236c9541049d45aaa6f49636f6ed0d5308a73cba`.

No D0067 mathematical identities, frozen metric, unchanged count, or recovery state transfers to this target.

## New outside target

Varun Sivashankar, *Nearly Spanning Regular Subgraphs*, arXiv:2609.19777v1 (submitted 17 September 2026), Section 5, Conjecture 5.1:

For every fixed even integer `k >= 4`, `delta_k(r)=Theta_k(r^{-2})` as `r -> infinity` through odd integers.

The source proves the Alon–Mubayi nearly-spanning question in general with `O_k(r^{-1/2})` uncovered fraction, proves the exact `k=2` odd-degree value `1/(r^2-3)`, and supplies the matching `Omega_k(r^{-2})` construction for fixed even `k`. The remaining source obligation is the `O_k(r^{-2})` upper bound for every fixed even `k>=4` along odd `r`.

## Fixed metric

`beta_even := sup { beta in [0,2] : for every fixed even k>=4, delta_k(r) <= C_k r^{-beta} for all sufficiently large odd r }`.

Starting source-certified value: `beta_even >= 1/2` from written Theorem 2.1.
Target: `beta_even = 2`.

The paper mentions but omits a longer `O_k(log r/r)` argument; it is prior guidance, not a fleet proof or certified metric improvement until reconstructed rigorously.

## Admission evidence

Captured pre-claim master: `1193e761a8099cf66285b264740c6b594103366e`.
Claim creation commit: `048e51cb1c7d05d9a84a7257b2758b8ffd8d7873`.

On 2026-09-18 the current arXiv page still showed only v1 and the literal Conjecture 5.1. Fresh bounded exact-title/author/arXiv-id/conjecture searches found no later source version or source-matching resolution. Repository searches and direct claim lookup found no existing owner or exact-scope conflict before the claim was created. Current reserve evidence did not demonstrate a free CLOSABLE successor, so this target is honestly classified HARD rather than relabeled for allocation.

## First substantive attack

Use B2 / B11 / B25, with refutation first:

- B2 ATTACK THE NEGATION: search for odd-degree regular graph families whose maximum even-`k` factor necessarily omits more than `Theta(n/r^2)` vertices. Any valid family with a larger loss exponent refutes the source conjecture.
- B11 DUALIZE: formulate maximum covered `k`-regular subgraph as a factor/flow or polyhedral dual obstruction; identify what dual certificates force uncovered mass and whether odd-cut constraints can yield an `O_k(n/r^2)` upper bound.
- B25 DOUBLE-COUNT: start from a maximum `k`-regular subgraph and double-count alternating exchanges / boundary incidences between covered and uncovered vertices. Seek a source-valid inequality with `r^2` leverage rather than another `sqrt(r)` estimate.

Do not code until a concrete identity, extremal family, or finite obstruction is specified. A fixed-`k` theorem is PARTIAL unless it extends uniformly in the source sense to every fixed even `k>=4`.
