# BT4 handoff — fleet04/B05 six-remainder sink overload

Source run: `proofnet24/collective-BT4/fleet04/B05/b05-20260922t041051z-r33/report.md`  
Candidate: `BT4-COUNT-v5-SIX-R-SINK-OVERLOAD`  
Outcome: `ESSENTIAL_STEP_APPLIED`, not a full proof.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

## Exact dependencies consumed

- Team lead fleet02/B04 `20260922T022208Z-b04-bt4-r11`, report blob `930c6906cc2532269bc35e0d0b0ea8e246eb250b`, controlling correction blob `117d9760b66cfb5930c79ade79d2b449ce329b9b`.
- Named OTHER-account partner fleet01/B06 fixed-pair collar theorem, run `20260922T013522Z-b06-bt4-r11`, blob `0ffb3fb1b521920e0a9cb3693fda8fd5bbb6a588`.
- Newer partner fleet01/B06 `BT4-GATE-ESCAPE-v1`, blob `adb2dcf7289ec7290cfc75ad760355ff540dff3d`, read for compatibility but not needed in the final six-vertex contradiction.
- Immediate predecessor fleet04/B05 `BT4-COUNT-v4-FIVE-R-EXCLUSION`, blob `f3d20a757d23ce7d835f8605d3105504b58a7b07`.

## New proved step

In the inherited oriented exact-outdegree-seven minimum-counterexample normal form, assume global `NO-SIX`, no cross-packed transition, no neutral minimum-packing exchange, and `|R|=6`.

The partner collar theorem excludes any `R`-supported five-witness at size six. Hence each deleted packed pair has at least three five-witnesses on its complementary packed cycle.

For every such support witness `z`, the predecessor's exact-six theorem gives two length-four bypasses

`z^- -> r1 -> r2 -> r3 -> z+`,

`z^- -> s1 -> s2 -> s3 -> z+`,

whose six internal vertices partition `R`.

Choose one sink `x` of the acyclic remainder. It cannot be `r1,r2,s1,s2`, since each has an outgoing `R`-arc displayed above. Therefore `x` is `r3` or `s3`, so `x->z+`.

For one deleted pair there are at least three distinct support witnesses and hence three distinct successors on the complementary packed cycle. Thus `x` has at least three outneighbors on that packed cycle. Repeating for all three pair deletions gives at least `3+3+3=9` distinct packed outneighbors of `x`, contradicting exact outdegree seven.

Therefore global `NO-SIX` with `|R|<=6` always exports a genuine cross-packed transition or a size-neutral globally minimum exchange.

## Next unpaid implication

The first possible equality-free/no-cross strict-collar size is now `|R|>=7`. At size seven, an `R`-supported witness can meet the partner lower bound tightly and a cycle-supported two-collar system can omit one remainder vertex. The next finite boundary is to rule out concentration of these omissions on a common acyclic remainder sink, or turn that concentration into cross / neutral / exchanged-remainder cycle / SIX geometry.

Campaign-level `H6` and `HX` remain open. Full BT4 remains open.
