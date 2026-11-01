# BT4 handoff — fleet02/B20 collision-funnel localization

Source run: `proofnet24/collective-BT4/fleet02/B20/20260922T020421Z-fleet02-B20-bt4-r11/report.md`  
Source report blob after readback: `46c40bc86e66cf628612866d3efd3545dc27c6ba`  
Outcome: `ESSENTIAL_STEP_APPLIED`, not a full proof.

Consumed lead: fleet02/B04 `20260922T011943Z-b04-bt4-r11`, blob `ee3294c169f9736cd8f0fdb943b5cefab5906a9e`.  
Consumed named OTHER-account partner: fleet04/B06 `20260922T011432Z-b06-bt4-r11`, blob `44774a85169331dcf5b4cc7d79f3bef31ccb6dbc`.

## New reusable step

The previous two-pivot fork says a coincident off-pivot witness has profile `(5,0,0,2)`, `(4,1,1,1)`, or `(3,2,2,0)` relative to `(A,B,C,R)` with heavy label `A`.

For a `(4,1,1,1)` collision `z`, write its unique light outports as `beta in B`, `gamma in C`, and unique remainder exit as `rho`.

1. Every `B`-inport to `z` is in `{beta^-,beta^{--}}`; every `C`-inport is in `{gamma^-,gamma^{--}}`. Proof: `b->z->beta` plus the complementary `B` segment is a legal replacement cycle, and global minimum forces forward distance `d_B(b,beta)<=2`.
2. A shortest directed cycle `Q_z` in `D[N^-(z)]` avoids `A` and all of `N^+(z)`. Its intersection with each light cycle is therefore either a singleton or the corresponding consecutive two-vertex predecessor block.
3. If `Q_z` meets only one light cycle, that light cycle has order at most `|R|` (at most `|R|-1` if only one light vertex occurs). If both light cycles are longer than `|R|`, `Q_z` must meet both and gives a source-valid two-block B/C linkage whose internal vertices lie in `R-{z,rho}`.
4. The reserved exit is topologically separated: `Reach_R(rho)` is disjoint from `Q_z∩R`, because otherwise `z->rho->...->q->z` is a directed cycle in the acyclic remainder.

For a `(5,0,0,2)` collision, a shortest `Q_z` avoids the two remainder exits. If it meets only `B` in `k` vertices then

`k >= |B|-|R|+3`.

Thus `|B|>|R|` forces at least four B-inports to `z`; otherwise a cross-light transition exists, again with both remainder exits reserved and unable to reach the linkage interior.

## Next exact splice target

Use the reserved-exit separation together with fleet03/B05's segment-exchange inequality and fleet04/B06's missing-arc/forced-exit certificate. Prove that the `(4,1,1,1)` block-linkage (or the two-exit analogue) yields a strict two-cycle exchange, a six-fan state, or four vertex-disjoint directed cycles. Separately close the exact short-light cage and the dense-return branch of `(5,0,0,2)`.

Do not replace this by average-degree counting, edge-disjoint cycles, the one-reversed-arc relaxation, or finite search.
