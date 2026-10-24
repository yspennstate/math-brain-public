# BT4 account03/B05 addendum — marked-segment exchange and 3-connectivity linkage trichotomy

Run: `account03-B05-20260922T0041Z-r11`
Candidate extension: `BT4-TCEX-v2.1-linkage`
Outcome: `ESSENTIAL_STEP_APPLIED`
Parent report: `report.md`, blob `1e08cd4e6a3db142c86033d9a63a0566f7bed172`

This addendum strengthens the segment exchange proved in the parent report and directly connects it to the exact 3-vertex-strong normal form proved by account02/B04. It does not alter or retract the parent lemma.

## Lemma A — the moved heavy vertex may lie anywhere in the bypassed segment

Use the parent setup: `(A,B,C)` is a globally minimum-total three-cycle packing with remainder `R`. Let `S=B[u,v]` be a proper forward segment of `B`, of size `s<=|B|-2`, and let

`Q: u^- -> ... -> v^+`

be a directed path of length `ell` whose internal vertices lie in `R`.

Fix **any** marked vertex `w in S`, not necessarily `u`. Assume `b in A` with `b->w`. Then for every `a in N^+(w) intersect A`, writing `t=d_A(b,a)`,

`                         t <= ell+1-s.                 (A1)`

Hence, with `m=|N^+(w) intersect A|`,

`                         ell >= m+s-1.                 (A2)`

### Proof

Replace `A` by

`A_a=b->w->a->A[a,b]`.

As before, `|A_a|=|A|+2-t`. Replace `B` by `B_Q=Q+B[v^+,u^-]`, whose size is `|B|-s+ell-1`.

The two replacements are vertex-disjoint because `w` belongs to the removed segment `S`, so `B_Q` does not use `w`; all other vertices of `A_a` lie on `A`, while all internal vertices of `Q` lie in `R`. The untouched cycle `C` is disjoint from both.

Thus the total covered-size change is again

`                         ell+1-s-t`.

Global minimum makes this nonnegative, giving (A1), and counting distinct positive fan distances gives (A2). QED.

At equality `m=ell+1-s`, the fan on `A` is consecutive from the incoming port `b`, and the neutral exchange has exact new remainder

`(R minus int(Q)) union {b^+,...,b^(+(m-1))} union (S minus {w})`.

So the parent equality/acylcity argument also holds with `S\{w}` in place of `S\{u}`.

This strengthening matters because a linkage may bypass a segment containing a heavy witness without leaving that witness as the first vertex of the segment.

## Lemma B — extracting an R-internal segment bypass from a path avoiding the other packed cycles

Let `w in B`, and let `P` be a directed path from `w^-` to `w^+` such that:

1. `P` avoids `w`;
2. every internal vertex of `P` outside `B` lies in `R` (equivalently, `P` avoids `A union C`).

Then `P` contains a subpath

`Q: p -> ... -> q`

with internal vertices in `R`, where `p,q in B`, such that the forward `B`-segment

`S=B[p^+,q^-]`

is nonempty, proper, and contains `w`.

### Proof

Read the successive visits of `P` to `B`. The path begins at `w^-` and ends at `w^+` while never using `w`. If every consecutive pair of `B`-visits advanced along the cyclic order without jumping across `w`, concatenating those advances would force a visit to `w` before reaching `w^+`. Hence for some two consecutive `B`-visits `p,q`, the forward `B`-segment strictly between them contains `w`. By consecutive choice, the `p`-to-`q` subpath has no internal vertex on `B`; by assumption it also avoids `A union C`, so every internal vertex lies in `R`. Since `p!=q`, the skipped segment has at most `|B|-2` vertices. QED.

Combining Lemmas A and B gives a quantitative tax on any packed-cycle-avoiding linkage around a heavy witness.

## Lemma C — 3-connectivity linkage trichotomy at a cycle-supported heavy witness

Work in the exact-seven normal form of account02/B04, where the counterexample is 3-vertex-strong. Let `w in B` and suppose `w` is heavy on `A`:

`m=|N^+(w) intersect A|>=3`.

Then at least one of the following holds:

1. **reverse avoidance:** `A` has no arc into `w`;
2. **quantified R-bypass:** there is a proper segment `S` of `B` containing `w` and an `R`-internal bypass of that segment of length `ell` satisfying the sharp tax

   `ell >= m+|S|-1`;
3. **two-linkage branch:** there are two internally vertex-disjoint directed `w^-`-to-`w^+` paths, both avoiding `w`, and both meeting `A union C` internally.

Moreover, if `A->w` and `|R|<m-1`, branch 2 is impossible, so branch 3 necessarily holds.

### Proof

If branch 1 fails, choose `b in A` with `b->w`.

Because the digraph is 3-vertex-strong, directed Menger gives three internally vertex-disjoint directed paths from `w^-` to `w^+`. One is the two-edge packed-cycle path `w^- -> w -> w^+`. Therefore there exist two further internally vertex-disjoint paths `P_1,P_2` from `w^-` to `w^+` that avoid `w`.

If at least one `P_i` avoids `A union C`, Lemma B extracts from it an `R`-internal bypass of a proper segment `S` containing `w`; Lemma A then gives

`ell >= m+|S|-1`,

which is branch 2.

If neither path avoids `A union C`, both meet `A union C` internally, and because `P_1,P_2` are internally vertex-disjoint they give branch 3.

Finally, an `R`-internal bypass of length `ell` has `ell-1` distinct internal vertices in `R`. Since `|S|>=1`, branch 2 requires

`|R| >= ell-1 >= m+|S|-2 >= m-1`.

Thus `|R|<m-1` excludes branch 2. QED.

## Corollary D — two disjoint R-detours force a remainder-size lower bound

Under the hypotheses of Lemma C with `A->w`, suppose both Menger alternatives `P_1,P_2` avoid `A union C`. Let their extracted bypassed segment sizes and bypass lengths be `(s_1,ell_1)` and `(s_2,ell_2)`. Their internal `R`-vertex sets are disjoint, so

`|R| >= (ell_1-1)+(ell_2-1)
     >= 2m+s_1+s_2-4
     >= 2m-2.`

Therefore, if `|R|<2m-2`, at least one of the two independent Menger paths must enter another packed cycle. If `|R|<m-1`, both must do so.

This is useful precisely in the hard cycle-supported five/six-fan branch: a heavy witness with a genuinely small remainder cannot hide all of its 3-connectivity rerouting inside `R`; the global counterexample structure supplies packed-cycle linkages that the next two-cycle splice must exploit.

## Relation to the current first missing implication

The account04/B06 saturation result says the surviving proof must turn forced packed-cycle exits into a disjoint splice; the account01/B05 result gives a one-vertex bypass exchange; the parent report gives whole-segment accounting. Lemma C now makes the alternative source-valid:

- either there is no incoming arc from the heavy target;
- or an actual `R` detour exists and pays the sharp segment tax;
- or two internally disjoint linkages are forced through the other packed cycles.

Thus the next recipient no longer needs to assert an unexplained linkage. In the small-remainder regime it is forced by 3-vertex-strongness plus the segment-exchange inequality. The unpaid step is to splice the two-linkage branch (or show it forces a forbidden exchanged-remainder cycle) while retaining vertex-disjointness.

No claim of full BT4 closure or literature novelty is made.

Next recipients: `account04/B06`, `account02/B04`, `account01/B05`.
