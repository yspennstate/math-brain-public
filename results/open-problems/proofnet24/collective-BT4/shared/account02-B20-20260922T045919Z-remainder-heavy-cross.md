# BT4 handoff — remainder-heavy fan escape

Source run: `20260922T045919Z-account02-B20-bt4-r14`  
Scientific report commit: `660a34ccd083ebd63977fcdbb67fd76dbb66a8db`  
Outcome: `ESSENTIAL_STEP_APPLIED`; BT4 remains open.

Consumed lead: account02/B04 controlling heavy-triangle strengthening `1277bd8435045651114cb6500f47674603f3f522`.
Consumed named other-account partner: account04/B06 `BT4-R4-LOWFAN-INPORT-TRIANGLE-v1`, `caf1e01c679dd319fb80fc434bf5c9707c722f92`.
Consumed compatible other-account reduction: account01/B04 `BT4-R4-MAX-REMAINDER-ARC-COLLAPSE-v1`, `c6f43034c0e20bc92d12ea98e091867ae134173e`.

New lemma `BT4-R-HEAVY-CROSS-v1`: in the inherited globally minimum three-cycle packing normal form, if a remainder vertex `w` has at least three outneighbors on a packed cycle `A`, then `A` cannot send to `w`; otherwise `b->w->a->A[a,b]` gives a strictly shorter replacement of `A`. Arc domination plus acyclicity of the remainder then forces a genuine packed-to-packed directed transition into `A` with all internal vertices in the remainder.

Applied to the compatible long-F2 double-pivot state: maximal-remainder-arc collapse gives `e<=1`; `e=0` is SIX, while `e=1` leaves five arcs from the freed remainder vertex into two complementary packed cycles, hence a 3-fan on one and therefore a genuine CROSS by the new lemma. Thus

`long-source F2 + |R|=4 => SIX OR genuine CROSS`

for the lexicographically chosen minimum packing. The remainder-supported exact-five output is no longer a separate terminal branch.

First unpaid target-level interface: convert the resulting CROSS/SIX data, together with reciprocal/third-port information, into two vertex-disjoint replacement cycles, a strict smaller three-packing, an exchanged-remainder cycle, or a fourth disjoint directed cycle. A single CROSS is not itself closure.
