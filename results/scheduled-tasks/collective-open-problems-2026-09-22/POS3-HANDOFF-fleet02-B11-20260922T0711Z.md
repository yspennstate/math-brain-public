# POS3 source-bound handoff — fleet02/B11 r17

Outcome: `ESSENTIAL_STEP_APPLIED`. Parent target remains `OPEN / NOT PROVED`. Execution context: `WITHOUT_VERIFIED_BRAIN`.

Source report: `yspennstate/math-open-problems`, `proofnet24/collective-POS3/fleet02/B11/20260922T065006Z-b11-pos3-r17-50176f59/REPORT.md`, science commit `6e5458e1c49ddec2040bd871bc8481ed446191bc`, report blob `c1e9ea6932c90f6dfe361041c0b817dccb03bb9d`, SHA-256 `d23d6888d61027c1f9b59b9958749c9c78dd665138e4c1df6792189956c7babc`. The notation clarification is commit `572914c9069002875176f1a47902889a32188980`: the report's phrase `1/2-multiplicity` means a `{1,2}`-valued lift multiplicity, not probability one-half.

New arbitrary-size theorem: let `x` be an incomparability-graph leaf with unique incomparable neighbor `b`. Put `D=Pred(x)`, `U=Succ(x)`, `L=P[D∪{b}]`, `R=P[U∪{b}]`, and `d=e(D), u=e(U), ell=e(L), r=e(R)`. The exact full-extension factorization gives `N(b<x)=ell*u`, `N(x<b)=d*r`. With capacities `A=ell/d`, `B=r/u`, `Pr(b<x)=A/(A+B)` and `A,B>=1`.

Assume width at most three, no balanced pair, `Pr(b<x)>2/3`, and no strict strong-majority span descent inside `(b,x)`. Let `I=Pred(x)\Pred(b)={z<x:z||b}` and `T=max I`. Then `I` is an upset of width at most two, so `|T|<=2`, and every `t∈T` is a Hasse predecessor of `x`. The exact reverse union is

`Pr( exists t∈T with b<t ) = (A-1)/(A+B) > 1/3`.

No member of `T` can have probability in `[1/3,2/3]` (balanced) or above `2/3` (strict span descent). Therefore `T={t1,t2}` exactly, each `Pr(b<t_i)<1/3`, their union has probability in `(1/3,2/3)`, and at least one actual Hasse channel has probability in `(1/6,1/3)`. The order dual gives the double-successor form.

This removes an incomparability leaf as a terminal state: it is forced into the previously proved B11 successor-free double-predecessor fan, which reroutes to strict span descent or a strict successor-chain corridor. Applying named partner fleet03/B19 r13 (`proofnet24/collective-POS3/fleet03/B19/20260922T0604Z-b19-pos3-r13-crossed-recycler/REPORT.md`, blob `6dc132cfb4ecfa6f50ffc0462dc1e0b06ea4c90b`) at the first exact-two crossed state then forbids closure on a fixed five/six-vertex recycler loop and forces fresh relation structure. Applying current campaign lead fleet04/B10 r15 (`proofnet24/collective-POS3/fleet04/B10/20260922T061407Z-B10-POS3-r15/REPORT.md`, blob `b0864fe6d45a6285e0226b3eec10a2272a8eeae1`) shows this pays a concrete part of its `RAY-RETURN EXCLUSION`: `outer ray -> incomparability leaf -> fixed local double-fan/crossed loop` is no longer a possible terminal mechanism.

Exact regression through naturally labelled transitive closures on `n<=6`: 5230 total, 3701 width<=3, 3192 leaf states, 760 strong `b<x` leaf orientations, 685 with a balanced maximal delayed-predecessor channel, and 75 hard local states. All 75 hard states are exactly double-fan states and all 75 are bi-connected in the comparability and incomparability graphs. Terminal marker: `POS3_LEAF_DOUBLE_FAN_CAPACITY_V1_PASS`. Executed verifier SHA-256 `b1c5e8b94ab3e0b81f0cc9e6e1cccfc7cc939b6b0aa66514e096e69347bf7b2b`; output SHA-256 `cf9ff1a88187929431b238b6b2e2579f74581695c511d4dd112bacf3ef6ed80d`. This is regression evidence, not finite closure.

Source-valid local-shortcut adversary: a six-point width-three, complementary-graph-connected example with covers `(0,4),(1,4),(1,5),(2,3),(2,5),(3,4)` has `E=37`, leaf pair `(b,x)=(5,4)` with `N(5<4)=25`, double fan `T={0,3}`, channel counts `7,10`, and union count `13`. Thus neither fan channel is balanced even though the poset has other balanced pairs. The stronger shortcut “one fan channel must balance” is false.

First unpaid implication: `GLOBAL NON-REUSE AFTER LEAF EXPORT`. After every leaf landing is converted to the double fan and then the chain corridor, prove that successive corridor / exact-two crossed / non-crossed multi-distinguisher states cannot reuse previously exposed vertices in a directed cycle without forcing a balanced pair, strict strong-majority span descent, a four-antichain, or a proper autonomous/ordinal/parallel reduction. Partner r13 excludes the smallest exact-two crossed local closure; arbitrary-generation non-reuse remains open.

No benchmark material, held-out answers, keys, credentials, scheduler identifiers, machine paths, raw transcripts, email/Drive data, paid model/API/Codex calls, remote workflows, permission changes or public posting were used or exposed.
