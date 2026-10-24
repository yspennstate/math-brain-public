# BT4 account03/B04 — neutral-bypass support switch for cycle-supported pair witnesses

Run: `20260922T005218Z-account03-B04-r11b`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-SUPPORT-SWITCH-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Target and live source state

The target is the `k=4` Bermond–Thomassen statement: every finite loopless digraph with at most one arc per ordered pair and minimum outdegree at least seven contains four vertex-disjoint genuinely directed cycles. Opposite arcs are allowed and a directed digon counts as a cycle.

A fresh source check during this run still found Bessy–Muis–Sereni–Steiner–Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (13 August 2026), explicitly stating that the exact conjecture remains unresolved for every `k>=4`; its theorem permits each packed cycle to become directed after reversing one arc and therefore does not settle BT4.

Fresh owner control revision `2026-09-22.2` supersedes this slot's older brain-retrieval/FEI prompt. The live account03/B04 assignment is the BT4 extremal/shortest-cycle or longest-path mechanism with an explicit seven-outdegree budget. No new brain-installation or benchmark work is performed here.

## Exact peer mathematics consumed

Assigned partner consumed exactly:

- account04/B05 `BT4-COUNT-v1`, shared handoff blob `9ce99798e661e4d14b2b27a0f647b909eff715b4`, complete derivation blob `28fdfb0b4449ef6d196b05de51d868e0df6a582a`.

That report supplied the exact-seven pair-deletion `6`-fan / three-`5`-fan certificate system and the remainder-witness collision algebra. My immediately preceding B04 correction, shared blob `4c16f36c8a711b9730a5abf2ed529cd967329c53`, repaired its support gap: a pair-deletion witness may lie on the complementary packed cycle, where the one-vertex heavy-target avoidance exchange is not directly legal. In the exact-seven/chordless normal form, such a cycle-supported six-witness has `6-cross/0-R-exit`, while a cycle-supported five-witness has `5-cross/1-R-exit`.

I also use the newer two-cycle exchange mechanism of account03/B05, `BT4-TCEX-v2-segment`, report blob `1e08cd4e6a3db142c86033d9a63a0566f7bed172`, only as compatibility context. The lemma below is logically simpler and attacks the support defect itself: it needs no return arc from a target cycle.

## Setup

Assume BT4 false and work in the current exact-seven normal form with a globally minimum-total three-cycle packing

`(A,B,C)`

and acyclic remainder `R`. Each packed cycle is chordless. For a vertex `w` on `C` write `w^-` and `w^+` for its predecessor and successor on `C`.

For the pair `{A,B}`, a cycle-supported pair-deletion witness `w in C` has one of the repaired exact forms:

- six-fan: `|N+(w) intersect (A union B)|=6`, and the only residual outarc after deleting `A union B` is `w->w^+`; in particular `w` has no outarc into `R`;
- five-fan: `|N+(w) intersect (A union B)|=5`, and besides `w->w^+` it has exactly one outarc `w->r` with `r in R`.

The unresolved issue was that `w` is not in the remainder, so an exchange through `w` against a heavy target cycle can collide with `C`.

## Lemma 1 — singleton neutral-bypass support switch

Suppose `w in C` is any cycle-supported five- or six-fan witness for `{A,B}` and there exists `q in R` with

`w^- -> q -> w^+`.

Then there is another globally minimum-total three-cycle packing `(A,B,C')` for which `w` lies in the new acyclic remainder. Relative to this new packing, every heavy-target avoidance inference for `w` is legitimate: if

`|N+(w) intersect A| >= 3`, then there is no arc from `A` to `w`,

and likewise with `B` in place of `A`.

### Proof

Replace the two-edge section

`w^- -> w -> w^+`

of `C` by

`w^- -> q -> w^+`.

Because `q` is in the old remainder, the resulting `C'` is a directed cycle disjoint from `A` and `B`. It has exactly the same number of vertices as `C`. Hence `(A,B,C')` is another three-cycle packing with the same total covered size as the global minimum; it is therefore itself globally minimum.

Its remainder is

`R'=(R minus {q}) union {w}`.

`D[R']` must be acyclic: otherwise a directed cycle in `R'` together with `A,B,C'` would be four vertex-disjoint directed cycles in the original digraph.

Now suppose `w` has at least three outneighbors on `A` and some `b in A` satisfies `b->w`. For each `a in N+(w) intersect A`, let `t=d_A(b,a)` be the positive forward distance from `b` to `a` on the directed cycle `A`. Because there are at least three distinct such outneighbors, one has `t>=3`. Then

`b -> w -> a -> A[a,b]`

is a directed cycle with `|A|+2-t <= |A|-1` vertices. It is disjoint from `B` and `C'` because `w` lies in `R'`. Replacing `A` by this strictly shorter cycle contradicts global minimum total size. Therefore no arc from `A` to `w` exists. The proof for `B` is identical. QED.

### Exact residual-degree effect

The support switch preserves the pair-deletion witness while relocating it into the remainder.

- If `w` was a six-fan witness, it had no old `R` exit. Hence it has no outneighbor in `R'`: it becomes an `R'` sink while still sending six arcs into `A union B`.
- If `w` was a five-fan witness with unique old exit `r in R`, then `w` has at most one outneighbor in `R'`. If `q=r`, that exit is consumed by `C'` and `w` becomes an `R'` sink. If `q!=r`, then `r` is its unique `R'` outneighbor. In both cases `w` remains a five-fan witness for `{A,B}`.

Thus the exact support defect that invalidated the original blanket use of `BT4-COUNT-v1` disappears whenever this neutral two-edge bypass exists.

## Corollary 2 — a concrete separation law in the unresolved singleton branch

After exhausting all legal neutral support switches, every still-problematic cycle-supported witness `w` must satisfy

`N_R^+(w^-) intersect N_R^-(w^+) = emptyset`.

Equivalently, there is no remainder vertex that can replace `w` on `C` by a length-two directed bypass.

This is stronger and more usable than saying merely that a two-cycle splice is unknown: the predecessor's `R`-outneighborhood and the successor's `R`-inneighborhood are forced disjoint for every unresolved saturated witness.

## Lemma 3 — segment neutral-bypass support switch

The same mechanism works for an entire proper directed segment. Let

`S=C[u,v]`

be a forward segment of `C` with `s=|S|` and `1<=s<=|C|-2`. Suppose there is a directed path

`Q: u^- -> q_1 -> ... -> q_s -> v^+`

whose `s` internal vertices all lie in `R`.

Then replacing the old segment `u^- -> S -> v^+` by `Q` produces another globally minimum-total packed cycle `C'` of the same length. The new remainder is exactly

`R'=(R minus {q_1,...,q_s}) union S`,

and `D[R']` is acyclic. Consequently every cycle-supported pair witness in `S` becomes an actual remainder witness, so the ordinary one-vertex heavy-target avoidance exchange is now valid for it relative to the unchanged other two packed cycles.

### Proof

The old segment from `u^-` to `v^+` contains the `s` internal vertices of `S`; the replacement path contains the `s` distinct internal vertices `q_1,...,q_s` of `R`. Thus the replacement preserves cycle length exactly and remains disjoint from the other packed cycles. Global minimum is preserved. The formula for `R'` follows by set subtraction/addition. A directed cycle in `R'` would be a fourth cycle disjoint from the new three-packing, so `R'` is acyclic. Each vertex of `S` now lies outside the three packed cycles, allowing the proof of Lemma 1 to be applied to it. QED.

There is also an immediate extremal trichotomy for any such segment: an `R`-internal bypass with fewer than `s` internal vertices would strictly shorten `C` and contradict global minimum; one with exactly `s` internal vertices is the neutral support switch above; therefore a segment whose support defect survives all switches admits no `R`-internal bypass of neutral-or-shorter size.

## Application to the repaired five-witness saturation branch

The previous correction split the pair-deletion certificate system into an all-remainder clean branch and a third-cycle saturation branch. Lemmas 1 and 3 now give a transfer between those branches rather than treating them as unrelated cases.

For a cycle-supported five-witness `w`, either:

1. a neutral singleton bypass exists, in which case `w` is moved into the remainder and the heavy-target avoidance logic becomes valid; or
2. the exact separation

   `N_R^+(w^-) intersect N_R^-(w^+) = emptyset`

   holds.

For several selected witnesses lying in one proper segment of the complementary cycle, either a neutral segment bypass simultaneously moves the whole segment into the remainder, or every `R`-only bypass around that segment is strictly longer than the neutral replacement.

This plugs directly into the current segment-collar work. Account03/B05 proved that, under the additional hypothesis of an arc from a heavy target cycle into the first witness, a bypass around a segment of size `s` must obey the stronger length bound `ell>=m+s-1`. The present lemma does not require that target-return hypothesis. It instead resolves the support legality: exact-neutral bypasses convert cycle witnesses into remainder witnesses; failure of that conversion produces an explicit `R`-separation obstruction to feed to the 3-vertex-strong / forced-exit machinery.

## What changed and what remains

Before this run, a cycle-supported five/six witness could not be used in the partner's avoidance orientation because the witness occupied the third packed cycle. The only generic instruction was to find a two-cycle splice.

After this run, the obstruction is sharper:

- any neutral `R` bypass around the witness or witness segment legally **switches its support into the remainder** without increasing the minimum packing;
- the moved witness then supports the same heavy-target avoidance inference used in the all-`R` branch;
- therefore a genuinely unresolved saturation witness must satisfy an exact predecessor/successor separation in `R`, and an unresolved witness segment must have no neutral-or-shorter `R` bypass.

This is a new extremal reduction on the same hard configuration, not a proof of BT4.

## First remaining implication

Combine the support-switch separation with the existing 3-vertex-strong / missing-arc-saturation / forced-exit structure to prove one of the following for a selected cycle-supported five/six witness or block:

1. a neutral `R` bypass exists, reducing that certificate to the all-remainder branch;
2. a strictly shorter disjoint two-cycle exchange exists; or
3. the forced absence of all neutral bypasses makes the predecessor-to-`R` and `R`-to-successor boundary sets so separated that the seven-outdegree budget forces a cross-cycle rerouting yielding four disjoint directed cycles.

For a singleton the first exact combinatorial obstruction is now

`N_R^+(w^-) cap N_R^-(w^+) = emptyset`.

The cycle-supported six-fan branch remains especially rigid because the witness itself has no `R` exit; the new support switch can still apply through its predecessor/successor, but no false five-fan collar is imported there.

## Outcome and recipients

`ESSENTIAL_STEP_APPLIED`.

Primary recipient: assigned partner `account04/B05`, because this lemma repairs the precise support condition needed before its `BT4-COUNT-v1` K3 avoidance machinery can be reused. Secondary recipients: BT4 lead `account02/B04`, account03/B05 and account04/B06 exchange/linkage workers.

No full BT4 proof, novelty claim, verified-brain claim, scheduler mutation, or truth promotion is made.
