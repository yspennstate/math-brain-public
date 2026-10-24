# BT4 handoff — account01/B04 maximal-remainder-arc collapse

Run: `20260922T044536Z-b04-bt4-r11`  
Candidate: `BT4-R4-MAX-REMAINDER-ARC-COLLAPSE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`; BT4 remains open.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

Canonical scientific report: `yspennstate/math-open-problems`, `proofnet24/collective-BT4/account01/B04/20260922T044536Z-b04-bt4-r11/report.md`, creation commit `c6f43034c0e20bc92d12ea98e091867ae134173e`, Git blob `b9b700749e5723c819b6643aa16c67c38db6c569`.

Latest complete lead state actually consumed: account02/B04 controlling heavy-triangle strengthening, scientific commit `1277bd8435045651114cb6500f47674603f3f522`, shared handoff commit `d2a8f6e35cf92aa59fd540bd7a7fdacd2b595451`.

Named OTHER-account assigned partner actually applied: account02/B05 `BT4-R4-DOUBLE-PIVOT-CONFLUENCE-v1`, scientific commit `e979878752af60b802243237fee75f6d9ddb81f7`.

## New reduction

Refine the team's globally minimum-total three-cycle packing by, subject to minimum total packed order, maximizing the number `Phi(P)` of arcs induced by its acyclic remainder. This preserves every inherited argument that uses only minimum total packed order and makes every neutral pivot satisfy `Phi(P')<=Phi(P)`.

In the assigned partner's exact four-remainder long-source F2 state, old `R={x,y,z,c}` has `x,y` sinks and `z not->x,c`; hence every old remainder arc lies in

`{c->x,c->y,c->z,z->y}`

and `Phi(P)<=4`.

The partner's simultaneous neutral pivots give new remainder `R'={c,z,s,v}` with `v=u+`. Its exact budgets are

`d^+_{H union U_x}(s)=6-e_s`,  `d^+_{H union S_y}(v)=6-e_v`,

where `e_s=d^+_{R'}(s)` and `e_v=d^+_{R'}(v)`. If the former high-exit wall `e_s,e_v>=2` held, then

`Phi(P') >= e_s+e_v >=4`.

Maximality gives

`4 <= Phi(P') <= Phi(P) <=4`.

So equality holds, `e_s=e_v=2`, and old `Phi(P)=4` forces all four allowable old arcs, in particular `c->z`. But new `Phi(P')=e_s+e_v=4` leaves no new-remainder arc whose tail is `c` or `z`, forcing `c not->z`. Since `c,z` persist across the pivot, contradiction.

Therefore the high-exit branch is impossible for the lexicographic packing. At least one freed vertex has `e<=1`, so long-source F2 with `|R|=4` immediately yields either a SIX witness (`e=0`) or an exact five-witness (`e=1`). The partner's residual `|S|=6 or |U|<=4` continuation is unnecessary in this normal form.

This is a materially different potential-function mechanism from the earlier port/cross-splice route. The first unpaid implication is now deficit-witness closure (plus the lead's separate heavy-triangle packed-port splice): turn the forced SIX/five-witness and reciprocal/third-port interfaces into two disjoint replacement cycles, a strict smaller packing, an exchanged-remainder cycle, or the fourth cycle.

Exact deletion/contraction formulas retained in the canonical report. No full BT4 proof, near-directed substitution, public posting, or truth promotion is claimed.
