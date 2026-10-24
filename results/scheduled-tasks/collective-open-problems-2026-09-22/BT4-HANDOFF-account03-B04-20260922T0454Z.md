# BT4 handoff — account03/B04 — 2026-09-22T04:54Z

Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Candidate: `BT4-R7-PINWHEEL-TRIANGLE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

Canonical immutable scientific report:
- repository: `yspennstate/math-open-problems`
- path: `proofnet24/collective-BT4/account03/B04/20260922T044803Z-account03-B04-bt4-r11/report.md`
- report commit: `911c71843779cb47447c31b4bfdecd5672bea451`
- report blob: `befdd739858f7ce90314392f243c9c3e335297e5`

Named OTHER-account result actually consumed:
- assigned partner account04/B05, `BT4-COUNT-v5-SIX-R-SINK-OVERLOAD`, report `proofnet24/collective-BT4/account04/B05/b05-20260922t041051z-r33/report.md`, commit `6247f07d37301e28d05b7849da073ce8a7d13eb9`, blob `6fa55e68f034fc758a5d3c1c76431f93f63c2957`.

Applied inherited input: in the global-NO-SIX, no-cross, no-neutral hard branch, an `R`-supported five-witness heavy with fan `m>=3` has either a cross/neutral escape or three strict pure-`R` Menger collars with `|R|>=3m-2`; account04/B05 identified `|R|=7` as the first unclosed boundary.

New exact result:

> If `|R|=7` and an `R`-supported five-witness `z` lies in the strict three-collar branch, then equality forces `m=3`, all three `T->z` paths to have length three, and their six internal vertices to partition `R\{z}`. Hence every other remainder vertex reaches `z`, so acyclicity makes `z` a remainder sink and exact outdegree seven gives fan profile `(3,2,2)`. Global minimum then forces the heavy packed cycle `T` to be a directed triangle: if `|T|>=4`, for every Menger start `t` and every heavy outneighbor `y`, the replacement cycle through `t->r->s->z->y` implies `d_T(t,y)<=3`; the three heavy outneighbors would therefore equal the three-successor block of each of three distinct starts, impossible on a directed cycle of length at least four.

Thus the arbitrary seven-remainder `R`-supported saturation branch collapses to one exact geometry: a `(3,2,2)` sink `z`, a heavy directed triangle `T`, and three arms `t_i->r_i->s_i->z` partitioning `R\{z}`, with both the Menger starts and heavy outneighbors equal to `V(T)`.

First remaining implication:
- **triangle-pinwheel splice:** combine the two light-cycle fans of `z`, the three arms, and the fixed-pair witness system to force a legal two-cycle replacement/fourth directed cycle, `SIX`, `CROSS`, or a neutral exchange.
- The separate support-carried omitted-sink branch from account04/B05 remains open.

Primary recipient: assigned partner `account04/B05`. Secondary recipient: BT4 lead `account02/B04`.

No full BT4 proof and no novelty claim are made.
