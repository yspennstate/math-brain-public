# BT4 handoff addendum — account04/B04 — four-remainder polarity-flip exchange

Run: `account04-B04-20260922T031050Z-BT4-r11`  
Candidate: `BT4-R4-COMPLEMENTARY-NEUTRAL-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain: `WITHOUT_VERIFIED_BRAIN`

A newer complete team-lead report arrived during this invocation after the primary B04 report was already archived. I read account02/B04 `BT4-R4-SATURATION-COLLAPSE-v1`, canonical commit `14ef93ae71f52c019c679c29fca4624e510f7b95`, blob `17d49d472779d5304d30b93c07ce89c289ab20d1`. It proves that in global NO-SIX, no-cross, `|R|=4`, a cycle-supported five-witness has heavy fan exactly three and two length-three equality bypasses partitioning the four-vertex remainder; the branch is a saturated neutral orbit rather than a strict collar.

Combining that theorem with B04's same-run predecessor-cycle lemma gives an exact additional neutral move. Let `z in B` be cycle-supported and heavy on `A`; write `F=N+(z)∩A` and let `e` be the unique R-outneighbor of `z`. The lead gives `|F|=3`. B04 gives a replacement cycle `Q_z` inside `N^-_A(z) union N^-_R(z)`, disjoint from `B,C`, with `|Q_z|>=|A|` and at least three R vertices.

Since `z->e` and the graph is oriented, `e` cannot be an R-inneighbor. As `|R|=4`, equality is forced throughout:

- `N^-_R(z)=R-{e}`;
- `N^-_A(z)=A-F`;
- `V(Q_z)=(A-F) union (R-{e})`;
- `|Q_z|=|A|`;
- replacing `A` by `Q_z` is size-neutral and leaves new remainder `R'=F union {e}`;
- `D[R']` is acyclic; and
- all relevant arcs have exact polarity `V(Q_z) -> z -> R'`.

Thus every cycle-supported witness in the lead's four-remainder saturated state has, in addition to its two equality bypass exits, a **complementary neutral / polarity-flip exchange** which swaps the witness's three heavy-fan vertices plus unique R-exit into the remainder and swaps the heavy-cycle complement plus the other three R vertices into the replacement cycle.

Canonical addendum: `proofnet24/collective-BT4/account04/B04/account04-B04-20260922T031050Z-BT4-r11/postlead_addendum.md`, commit `118d2942ce59b93455d8525cadacddf6e59ec252`, blob `5d653af3242d7353a33494e9702d800aa8691855`.

Updated first unpaid implication for `|R|=4`: `BT4-R4-POLARITY-ORBIT-v1` — show that the finite saturated-neutral orbit cannot repeatedly realize this polarity-flip move together with the lead's two equality bypass exits without generating CROSS, SIX, an exchanged-remainder cycle, or strict packing reduction. For `|R|>4`, retain the primary B04 `BT4-G1-FORK-CLOSURE-v1` branch.

No full BT4 proof is claimed.
