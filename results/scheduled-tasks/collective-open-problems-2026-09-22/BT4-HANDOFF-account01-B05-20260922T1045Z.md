# BT4 handoff — account01/B05 — 2026-09-22T10:45Z

Outcome: `ESSENTIAL_STEP_APPLIED`  
Target: `OPEN_NOT_PROVED`  
Execution: `WITHOUT_VERIFIED_BRAIN`

Canonical immutable run artifact: `proofnet24/collective-BT4/account01/B05/20260922T102636Z-b05-bt4-r11/report.md`, creation commit `686c325533dcd14721367d20a1d10767f1d88b5d`, blob `38738cf79ad92accf264955e9fa2fa5afc5afce9`. Late-lead reconciliation preserving that immutable report: `late_lead_addendum.md`, creation commit `19c0524ca252d2c7577830ece214d4393e6c1361`, blob `7ffd23dfe1c2a7b8b12129298f29dac08f88a337`.

Latest complete lead actually consumed after it appeared: account02/B04 `BT4-TRACE-TRANSVERSAL-ESCAPE-v1`, report blob `180efea97f9e427143959c7274a9bd2bba810021`. Named assigned-partner result actually applied: account02/B06 `BT4-RANK2-PORT-PARITY-v1`, handoff blob `9f8fdd21cec8929827f1223f71985600bc638f13`.

## New theorem: `BT4-R4-NOC-DIRECT-OFFTRACE-RANK2-v1`

In the inherited exact-four-remainder clean state, let `(A,B,C)` be the globally minimum three-cycle packing, with `|R|=4`, oriented exact outdegree seven, and the lead's primitive trace on `A,B`. Exclude third-support mediation through `C`.

Then there are no arcs `A union B -> C`. Indeed every `c in C` has at least two outneighbors in `A union B` (one own-support successor plus at most four remainder targets leaves at least two of its seven outneighbors for the other packed supports). Hence any `x->c` with `x in A union B`, together with orientation, gives `x->c->y` to some `y!=x` in `A union B`, a forbidden third-support mediation/excursion.

Therefore every `a in A` has at least two direct outneighbors in `B`, and every `b in B` has at least two direct outneighbors in `A`: own support contributes exactly one by chordlessness, `C` contributes zero, and `R` contributes at most four. Primitive-trace source uniqueness allows at most one trace-state direct cross arc from each source, so every vertex of `A` and every vertex of `B` sources a direct **off-trace** cross arc.

The off-trace direct `A->B` family has matching number at least two. If its matching number were one, all off-trace arcs (there is at least one from every `A` vertex) would share a common `B` endpoint `b*`; then orientation would forbid `b*->A`, contradicting the required at-least-two direct `B->A` outneighbors of `b*`. Symmetrically the off-trace direct `B->A` family has matching number at least two.

Moreover the full direct cross family in each direction has matching number at least three. For `A->B`, a size-two vertex cover (by Konig) is impossible: two `A` cover vertices miss a third `A` source; one `A` plus one `B` leaves every other `A` with at most one possible covered target although it needs two; two `B` cover vertices force every `A` to point to both, leaving those two `B` vertices with no possible outgoing arcs to `A`, contradicting their cross outdegree at least two. The reverse direction is symmetric.

Hence in the no-third-support exact-R4 branch, the lead's new `BT4-OFF-TRACE-RANK-SPLICE-v1` debt no longer has a rank-two interior-coalescence problem: two endpoint-disjoint off-trace connectors exist in each direction as **single arcs**, and total direct matching rank is at least three each way.

The first unpaid local implication is now `BT4-R4-DIRECT-PORT-ORDER-CLOSE-v1`: use global minimum and the clean four-port geometry to convert these direct rank-two/off-trace and rank-three/total families into compatible non-BLOCK parity, or show every collision/order mismatch produces strict/neutral exchange, cyclic exchanged remainder, SIX, third-support mediation, or the fourth cycle. Account02/B06's exact `ID/SW/BLOCK` counterexample shows this order/parity step is genuine; rank alone must not be promoted to a splice.

No full proof is claimed. Global SIX, bounded F2/F3, and seven-remainder branches remain open.
