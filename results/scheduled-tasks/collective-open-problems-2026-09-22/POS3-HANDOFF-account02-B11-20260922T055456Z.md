# POS3 handoff — account02/B11 — 20260922T055456Z

Outcome: ESSENTIAL_STEP_APPLIED. Source report: `yspennstate/math-open-problems`, `proofnet24/collective-POS3/account02/B11/20260922T055456Z-b11-pos3-r16-7136730f/REPORT.md`, source commit `f8cfad9108573a196144fcd8eada2c3b72ac00ee`, blob `09ccf73a03359bcc0545abff5a8a5bc79cc2f42d`.

New arbitrary-size reduction: if `x` has unique incomparable neighbor `b`, set `D=Pred(x)`, `U=Succ(x)`, `L=P[D∪{b}]`, `R=P[U∪{b}]`. Then `P\{x,b}=D⊕U` and exact uniform-extension counts are

`N(b<x)=e(L)e(U)`, `N(x<b)=e(D)e(R)`, `e(P)=e(L)e(U)+e(D)e(R)`.

Conditional laws factor into independent uniform smaller-poset laws on the two order branches. In a no-balanced ordinally indecomposable poset, if `Pr(b<x)>2/3` and `D` is a chain, then necessarily `D=∅`; dually if `Pr(x<b)>2/3` and `U` is a chain, then `U=∅`. Hence a surviving incomparability leaf in the minimal hard core must point its strong-majority orientation toward an empty or genuinely nonchain side.

Named partner account03/B19 r12 was applied to its exact `P_m` family. The leaf `e` with neighbor `d` has `N(e<d)=3*C(m+3,3)+2*C(m+2,2)` and `N(d<e)=2*C(m+2,2)+(m+1)`; for `m≥1` the majority-facing side is a nonchain of width three. Thus neither “leaf pair is balanced” nor “leaf majority side is a chain” is valid. The partner's `K/E→1/3+` also forbids a fixed-slack shortcut.

First unpaid implication: dominant-side balance transfer for the exact two-branch mixture when the majority-facing side is a nonchain of width≤3. Prove a balanced pair from the smaller dominant branch survives in `P`, or forces `(x,b)` balanced, or creates an ordinal reduction. Do not replace either conditional branch by an induced uniform deletion law.

Exact regression: 3701 width≤3 naturally labelled posets through n≤6; 3192 leaf states/factorizations; 49 lower-chain and 49 upper-chain strong-branch cases; partner `P_m`, m=0..8. Terminal marker `POS3_LEAF_SPLICE_V1_PASS`. POS3 remains OPEN.
