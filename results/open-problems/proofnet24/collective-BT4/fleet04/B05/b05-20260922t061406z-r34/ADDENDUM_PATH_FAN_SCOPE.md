# Controlling scope correction for Lemma 2

Run: `b05-20260922t061406z-r34`  
Candidate: `BT4-HT-EQUALITY-COLLAR-ELIMINATION-v1`  
Outcome remains: `ESSENTIAL_STEP_APPLIED`.

This addendum is controlling over the statement of Lemma 2 in `REPORT.md`.

The path-fan lemma must include the support condition needed for a legal replacement of the packed cycle `B`:

> If a directed path from `b in B` to a remainder vertex `q` has length `L`, **all internal vertices lie outside all three packed cycles (in the applications below, they lie in the old remainder `R`)**, and `q` has `m=m_B(q)` distinct targets on `B`, then `L>=m-1`.

The proof is unchanged: for each `c in N^+(q)∩B`, the path, the arc `q->c`, and the directed segment `B[c,b]` form a directed cycle that is vertex-disjoint from the other two packed cycles, so global minimum packing gives the same distance bound.

Every use of Lemma 2 in `REPORT.md` already satisfies this corrected hypothesis:

- the `k=2` shortcut `b->r2` has no internal vertex;
- the `k=2` shortcut `b->r1->r2` has its sole internal vertex `r1` in `R`;
- the `k=1` shortcut `b->r2` has no internal vertex.

Therefore no conclusion of the report changes. In particular, both equality collars remain eliminated and the aligned common-port branch remains forced into the genuine cross-packed transition output.

No full BT4 proof or novelty claim is made.
