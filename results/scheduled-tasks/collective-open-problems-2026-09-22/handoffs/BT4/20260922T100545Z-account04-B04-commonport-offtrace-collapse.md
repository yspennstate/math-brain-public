# BT4 handoff — account04/B04 common-port off-trace collapse

Run: `20260922T100545Z-a04-b04-bt4-r11`  
Candidate: `BT4-HT-COMMONPORT-OFFTRACE-COLLAPSE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

Canonical science: `yspennstate/math-open-problems`, commit `988ed72a502960d28e32a51af0232e20dd9866e5`, blob `b2d45ce88b1d6e5650901846e6f72bd4115e8e2d`, path `proofnet24/collective-BT4/account04/B04/20260922T100545Z-a04-b04-bt4-r11/report.md`.

Latest lead source applied: account02/B04 `BT4-PRIMITIVE-TRACE-MIXED-PACKING-ONE-v1`, blob `b768e00ab1e7f22e0cfd56d6f95ffbc36b3a1c60`. Essential lead predecessor: `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1`, commit `3d1cdc39d7512ad857e134f23740c027ef879764`.

Named OTHER-account partner result actually applied: account01/B05 `BT4-HT-COMMONPORT-REVERSE-CROSS-v1`, canonical science commit `5f4ad4452b7b940cbe8f9106a934745496a75a36`, blob `2536e90a7442fd90deab441243f0feb90e33db4a`, shared handoff commit `c8aa394ac9cd4dc190ab6d71c71f09ff096dee25`.

New theorem: in the aligned triangular common-port state `A=p->u->v->p`, partner supplies target-distinct reverse transitions `J_u,J_v` ending at distinct B ports and proves `B not->u,v`. Every vertex on the domination chain for `J_z` also points to `z`.

- If a transition apex is on `H`, this is already third-support mediation.
- If an apex is on `A`, chordlessness forces the apex to be `p` for `J_u` and `u` for `J_v`. If the transition has any R-interior vertex `q`, domination gives `q->u` or `q->v`, so `p->q->u` or `u->q->v` is immediately a same-support bypass.
- Therefore, absent third-support and bypass exits, the partner transitions are direct arcs `p->a_u` and `u->a_v` with `a_u!=a_v`.
- They cannot both be states of the lead's primitive trace. In reverse trace order, consecutive A-sources `p,u` give consecutive plus occurrences. Any intervening minus occurrence has constant A-coordinate `u`, hence would be a forbidden `B->u` arc. So there are no intervening minuses; then the B-coordinate does not change and `a_u=a_v`, contradicting target-distinctness.

Hence at least one direct arc is an ordered endpoint pair **off the primitive trace**. This proves the lead's `BT4-OFF-TRACE-OR-EXIT-v1` obligation for the aligned triangular common-port branch. It does not yet splice that off-trace arc into four cycles.

First remaining local implication: `BT4-HT-OFFTRACE-SPLICE-v1` — combine the forced off-trace direct A-to-B arc with the inherited B-to-A/H return and the second target-distinct reverse transition to force two disjoint replacement cycles, strict lexicographic decrease, cyclic exchanged remainder, SIX/HX, or a fourth directed cycle.

Separate global debts remain explicit. No full BT4 proof is claimed.
