# BT4 handoff — account04/B06 — 2026-09-22T07:25Z

Outcome: `ESSENTIAL_STEP_APPLIED`  
Candidate: `BT4-MENGER-RANK-INTERSECTION-COLLAPSE-v1`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

Canonical scientific report: private `yspennstate/math-open-problems`, path `proofnet24/collective-BT4/account04/B06/20260922T070806Z-b06-bt4-coll11/report.md`, creation commit `3e7343cfd9de439c2e6ae8c39e71ddcbc956cde9`, Git blob `ff7bbac3a8211262bc273f6fa02b102d3ace16dd`.

Fresh control used for the final stop check: OWNER CONTROL revision `2026-09-22.2`; README blob `3d4a9372c87802ab734141a3374d04c8823372e3`; active programme `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`; no later applicable B06 stop observed.

Latest complete lead actually consumed: account02/B04 `20260922T0619Z-b04-bt4-r11`, report commit `14b8affcde6130bdbacbdfbd03888816b96d61ef`, report blob `713053330313bf5906035c7bfd5841eb4e6b88ef`, shared handoff blob `b0c1c37b1d36fd7cf855946f20eb382a61cd346d`.

Named OTHER-account assigned partner actually applied: account01/B04 `BT4-SHORTEST-MIXED-CYCLE-PORT-COLLAPSE-v1`, canonical report commit `6c8161e81c755382994814f67272705af0134caa`, report blob `84a4f2e7929cbe4844f2421240a3dc8eb822d431`, shared handoff blob `2ce9d6f84ecd3a6d78489f03938e1d0493874697`.

Adversarial compatibility input: account03/B05 `BT4-FOUR-PORT-CONNECTOR-RANK-WALL-v1`, shared blob `5801ef39fc9f7cd699678cdd0803b7d525bfe5b1`.

## New mathematics

Let `A,B,H` be the three packed cycles in the inherited 3-vertex-strong normal form and `R` the acyclic remainder.

1. **Three-linkage dichotomy.** In either ordered direction `A->B` or `B->A`, directed Menger plus 3-vertex-strongness gives three pairwise vertex-disjoint support-to-support paths. After trimming, either two have all internal vertices in `R`, or two meet the third support `H`. When `H` is the heavy triangle, the latter alternative contains at least one path meeting `H` in exactly one vertex; if all three hit `H`, they hit the three triangle vertices one apiece.

2. **Prescribed direct-cross freshening.** Any direct cross `c->w` between `A` and `B` can be freshened: delete `c,w`; strong connectivity survives; trim a path from the source support to the target support. This yields a second connector vertex-disjoint from the direct cross, with internal vertices either all in `R` or explicitly mediated by `H`.

3. **Opposite-connector intersection collapse.** If an `A->B` connector and a `B->A` connector have all internal vertices in acyclic `R` and meet at a remainder vertex, their common vertices occur in the same order on both paths. Splicing at any common vertex gives simple same-support remainder paths on both `A` and `B`. A distinct-endpoint output is a genuine same-support BYPASS and inherits the exact minimum-packing distance tax. A coincident-endpoint output is a one-packed-vertex directed replacement cycle, forcing the corresponding support order to be at most `|R|+1`; in the heavy-triangle `|R|=4` cage this means support order at most five.

Applied to the partner's shortest-mixed-cycle theorem, the fresh-source CROSS branch cannot remain a connector-rank-one obstruction. In the long-support/no-bypass/no-third-support-mediation residual, both directions may be taken to have rank-two remainder connector families whose opposite-direction interiors are disjoint. Thus the remaining local obstruction is now only packed-port cyclic order / packed-endpoint compatibility, not rank one and not uncontrolled remainder intersection.

## First unpaid implication

`BT4-RANK2-PORT-ORDER-SPLICE-v1`: in the aligned four-remainder heavy-triangle state, with rank-two connector families in both directions, disjoint opposite-direction interiors, no `H` mediation and the partner fresh-source condition, prove that cyclic port order / packed-endpoint collisions force one of: two legal replacement cycles with strict lexicographic improvement or cyclic exchanged remainder; a compatible same-support bypass family; SIX; or the bounded short-support branch.

Separate global debts remain SIX/H5 closure, bounded F2/F3 short-support states, and the support-carried seven-remainder branch. Do not report BT4 as proved.

No computation was used. No authenticated brain retrieval/context use occurred. No scheduler mutation, email, Drive, public posting, paid API/model, Codex, remote workflow, cross-account authentication or permission bypass was used.
