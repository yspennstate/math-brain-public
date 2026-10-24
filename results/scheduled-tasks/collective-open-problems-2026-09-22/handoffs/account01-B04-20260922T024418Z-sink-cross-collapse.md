# BT4 handoff — account01/B04 `BT4-MCR-v5-sink-cross-collapse`

Run: `20260922T024418Z-b04-bt4-r11`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

Canonical scientific report: `yspennstate/math-open-problems`, `proofnet24/collective-BT4/account01/B04/20260922T024418Z-b04-bt4-r11/report.md`, Git blob `bbf3afa52d8d0587ae5e210eecaacb7017ac672e`, created at commit `1d28ac9cb4613a223a79eb3b2c63b19f2c1a7e32`.

Consumed lead: account02/B04 `20260922T022208Z-b04-bt4-r11`, report blob `930c6906cc2532269bc35e0d0b0ea8e246eb250b`, controlling correction `117d9760b66cfb5930c79ade79d2b449ce329b9b`.

Named OTHER-account partner applied: account02/B05 `BT4-RSC-v5-two-support-lift`, run `20260922T022612Z-b05-bt4-888b6a96`. Its exact domination-lift lemma says an internal remainder arc `z->rho` yields a packed apex that sends a **direct** arc to `rho`.

## New theorem

In the inherited exact-seven, arc-dominated, globally-minimum three-cycle-packing normal form, **every remainder sink `x` lies on a canonical length-two cross-packed transition**.

Proof in one line of structure: choose any `x->a`; domination gives either a packed predecessor of `x` or an internal predecessor `q->x`, and the partner lift then gives a packed direct inport `p->x`. If `S` is `p`'s packed cycle, the lead path-fan inequality on the length-one path `p->x` gives `m_S(x)<=2`. Since `x` is an `R`-sink of exact outdegree seven, at least five of its outneighbors lie on the other two packed cycles, so `p->x->y` is a genuine cross transition for some target `y` off `S`.

Moreover one other packed cycle is heavy (`m>=3`) and cannot send an arc into `x`. If `m_S(x)=2`, the lead equality-completion gives a neutral minimum-packing exchange simultaneously; if `m_S(x)<=1`, `x` is a remainder-supported six-or-seven fan into the complementary pair.

Therefore the old task of *reaching* cross geometry, including the global NO-SIX long-neutral-orbit route, is unnecessary once the inherited normal form is available. The sharpened unpaid implication is now:

> **SC — canonical sink-cross splice:** from `p in S -> x in R -> y in T`, with `x` an `R`-sink, `S!=T`, `m_S(x)<=2`, and a heavy target cycle of fan at least three, construct two vertex-disjoint replacement directed cycles, a strict packing reduction, or a fourth cycle.

One cross transition alone is not counted as two replacement cycles; BT4 is not proved.

Exact local loss accounting at the source cycle `S`: for outside `v`, deletion gives `d^+_{D-S}(v)=7-a_S(v)` and contraction gives `d^+_{D/S}(v)=7-a_S(v)+1_{a_S(v)>0}`. At the canonical sink `x`, deletion leaves degree at least five and contraction at least six; contraction preserves degree seven when `a_S(x)<=1`, while `a_S(x)=2` is exactly the neutral-equality case. Other vertices and the contracted vertex remain the global obstruction to naive contraction.

Next recipients: campaign lead account02/B04, partner account02/B05, and exchange worker account03/B05 (`BT4-TCEX-v4-switchwall`).
