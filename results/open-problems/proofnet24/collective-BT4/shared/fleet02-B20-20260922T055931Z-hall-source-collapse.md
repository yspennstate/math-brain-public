# BT4 shared handoff — fleet02/B20 Hall-source collapse

Run: `20260922T055931Z-fleet02-B20-bt4-r15`  
Candidate: `BT4-HT-HALL-SOURCE-COLLAPSE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target: `OPEN_NOT_PROVED`

Canonical report: `proofnet24/collective-BT4/fleet02/B20/20260922T055931Z-fleet02-B20-bt4-r15/report.md`, commit `2ca474e9ceb8d0838b016d026a7fe224977df17c`, blob `aa5daebc2b328bc3b21ffc77ad8d9ba6e1f1bfc0`.

Sources actually used:
- lead fleet02/B04 `20260922T051543Z-b04-bt4-r11`, report blob `9f1ec8ca9ab3f2737b9dddf98389826f5b926933`, strengthening blob `aa71a6d910955a009b020ee77aba4a0da0052cdb`;
- named partner fleet04/B06 `BT4-SIX-DUAL-WALL-LIFT-v1`, run `20260922T051305Z-b06-bt4-r14`, report blob `c972d170864b95062330e30dcdeded0f7b76cb1e`;
- fleet04/B05 `BT4-HT-XFREE-HALL-v1`, run `b05-20260922t051421z-r34`, report blob `e63f331533e20a4a1231458a6c5c43c7eb5c4bf1`.

New reduction. In the Hall distinct-port branch for two same-heavy triangle witnesses, let the two x-free escape paths end at distinct ports of a common light support A and have disjoint R-interiors. If their packed sources are distinct, the paths are fully vertex-disjoint: starts are distinct packed vertices outside A, targets are distinct in A, and interiors are disjoint in R.

If the two paths share a packed source q, exact cage geometry forces q onto the opposite light support B. Moreover q sends to both heavy witnesses and to the two distinct first steps of the escape paths. Since B is chordless, q has only its support successor on B.

- If q has no R-outneighbor, exact outdegree seven makes q a cycle-supported exact-six witness into H union A with zero R exit. This routes to the existing SIX system; in the partner's C4 dual-wall subcase, fleet04/B06 further routes the all-long wall to CROSS/BYPASS/short support.
- If q has an R-outneighbor, take a directed continuation through acyclic R to its first packed contact t. If t lies on H or A, obtain a genuine CROSS. If t is a distinct vertex of B, obtain a same-support bypass P of length ell with `ell >= dist_B(q,t)` by global minimum packing. If t=q, obtain a directed cycle on q plus R and hence `|B| <= |R|+1`.

Therefore a generic common source is no longer an independent Hall obstruction. The surviving first universal debt is cyclic-order/reciprocal-return splicing for the fully vertex-disjoint distinct-source pair, plus the explicitly separate exact fan-collision, SIX/H5 and short-support branches.

Precision note: when q has an R-outneighbor, fix any one maximal R-continuation used in the proof; its first packed contact falls into exactly one of CROSS, BYPASS, or return-to-q. Other continuations may coexist and only strengthen the available alternatives.

No full BT4 proof is claimed. No finite search or nearly-directed cycle is used.