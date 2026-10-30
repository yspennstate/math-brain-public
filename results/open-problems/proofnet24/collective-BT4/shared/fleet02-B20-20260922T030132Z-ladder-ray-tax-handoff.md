# BT4 shared handoff — fleet02/B20 aligned ladder–ray exchange tax

Source run: `proofnet24/collective-BT4/fleet02/B20/20260922T030132Z-fleet02-B20-bt4-r12/report.md`  
Creation commit: `23156aecca7ada1efd837eb051d9cd237d436fd1`  
Outcome: **ESSENTIAL_STEP_APPLIED**; BT4 remains **OPEN**.

Consumed lead: fleet02/B04 `20260922T022208Z-b04-bt4-r11`, blob `930c6906cc2532269bc35e0d0b0ea8e246eb250b`.  
Consumed named partner: fleet04/B06 `20260922T021002Z-b06-bt4-r12`, `BT4-SIX-DUAL-COLLAR-v1`.  
Consumed newer compatible wall elimination: fleet03/B05 `20260922T024158Z-b05-bt4-r11`.

In the partner `C4` exact-six branch let `z in B`, `p=z^-`, let an incoming ladder `L:s->...->z` have `lambda` edges, apex `s in X` for `X in {A,C}`, and internal vertices in `R`; let `a in N^+(z) cap X`, with `d_X=dist_X(a,s)`. Let an outgoing ray `P:p->...->t` return to `B`, have `ell` edges, internal vertices in `R`, and `d_B=dist_B(p,t)>=2`.

If the `R` interiors of `L` and `P` are disjoint, global minimum of the three-cycle packing gives the exact exchange tax

`ell-d_B >= |X|-d_X-lambda-1`.

Proof: `L+(z->a)+X[a,s]` and `P+B[t,p]` are disjoint genuine directed cycles; the latter avoids `z` because `z` lies internally on the skipped forward segment `B[p,t]`. Keep the third packed cycle and compare total size to `(A,B,C)`.

Therefore every ladder/ray pair gives one of four structural outcomes: partner splice if the `R` interiors meet; the quantitative exchange tax if target-aligned and disjoint; an immediate strict `B` bypass if ladder apex is `p=z^-`; or six fan arcs concentrated on the opposite support if a support apex lies on a targetless cycle.

**Next unpaid step:** prove a nonreuse/merge theorem for the two outgoing rays so these compulsory excesses, fleet03/B05 switching, and fleet01/B06 transverse gate-escape cannot all coexist without a smaller three-cycle packing or four vertex-disjoint directed cycles. Do not sum taxes across rays without proving the needed disjointness/charging statement.
