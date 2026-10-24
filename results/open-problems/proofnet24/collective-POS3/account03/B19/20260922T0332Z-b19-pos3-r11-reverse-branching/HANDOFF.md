# Handoff — POS3 strict nested endpoint now branches

Recipient: `account04/B10` (assigned partner / team lead).  
Run: `20260922T0332Z-b19-pos3-r11`.  
Outcome: `ESSENTIAL_STEP_APPLIED`; parent POS3 remains OPEN / NOT PROVED.

Consumed exact partner state: account04/B10 run `20260922T031005Z-B10-POS3-r11`, which proves strict predecessor nesting and the Hasse-corridor continuation at the first-boundary sibling pair.

New exact theorem. For `a||b` with `Pred(b) proper-subset Pred(a)`, delayed predecessor-difference chain `D` with top `d`, and `U=Min{z:b<z,z||a}`, the reverse nonneutral remainder is the **original-uniform** union

`R = | {L:b<_{L}d} union (union_{u in U}{L:u<_{L}a}) |`.

Also, with `M=Min{z:a<z,z||b}`, `M union U` is an antichain, hence `|M|+|U|<=3` in width three.

Apply this to the partner's majority-late/no-span-descent branch. Every atomic event above has probability `<1/3`, while the endpoint identity forces `R/E>1/3`. Therefore no single reverse blocker can carry the continuation; at least two atomic channels are genuinely necessary. If `|U|=1`, the two events `{b<d}` and `{u<a}` each have mass `<E/3`, their union has mass `>E/3`, and neither event contains the other. This complements the partner's majority-early/no-descent branch, which has exactly two forward Hasse blockers.

Exact sharpness witness: six-element width-two poset with covers `(0,3),(1,2),(1,3),(2,4),(2,5),(3,5)`, endpoint `a=3,b=2,d=0,u=4`, `E=14`. The two reverse atoms both have size 4, intersection 2, union 6; thus each is `<E/3` while the union is `>E/3`. Its balanced pairs are `(0,1)` and `(4,5)`, so local endpoint closure is genuinely false while POS3 remains true on the witness.

Next missing implication: **GLOBAL_BRANCH_MERGER**. Combine the joint channel budget `|M|+|U|<=3`, the two-forward-blocker majority-early branch, the reverse-union majority-late branching above, delayed distinguishers, original-uniform cut-charge identities, pinned-rank atoms and heavy-slice constraints to prove that repeated finite branching must terminate in a balanced pair, a four-antichain, a proper autonomous nonchain, span descent, or signed flux contradiction. The local channel structure is now exact; the remaining work is global conservation/merger, not another one-boundary pigeonhole.

Verifier SHA-256: `423d5c9643db20e6ffb931d62df22dff6df0624291c9fb0b3e758a762e416b4a`.  
Output SHA-256: `8ceeabe0c82d61cd11b6bed4dd0b339d49d4ca0903e2e4549600267c8b5d68c1`.  
Terminal marker: `POS3_B19_REVERSE_BRANCHING_CERTIFICATE_PASS`.
