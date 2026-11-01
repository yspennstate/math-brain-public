# BT4 fleet04/B04 — sink dominator-cycle port split in the exact-seven normal form

Run: `fleet04-B04-20260922T011307Z-BT4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Candidate: `BT4-SINKPORT-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and source boundary

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four vertex-disjoint genuinely directed cycles. Opposite arcs are allowed in the target and a digon counts as a directed cycle.

Current source boundary retained from the collective target record: Bessy–Muis–Sereni–Steiner–Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (13 August 2026), explicitly leaves the exact directed-cycle conjecture unresolved for every `k>=4` and proves the `2k-1` threshold only for the one-reversed-arc relaxation. Nothing below treats a near-directed cycle as a directed one.

The lower-`k` input used through the team lead is the Lichiardopol–Pór–Sereni result that minimum outdegree five gives three disjoint directed cycles and the stronger `k=2` degree-sequence theorem: a digraph has two disjoint directed cycles if every vertex has outdegree at least three except at most two vertices of outdegree two.

## Exact peer snapshots consumed

I read the latest finalized team-lead version available before this derivation:

- fleet02/B04, exact-seven sink normal form, scientific report commit `a95b20d733b75b91a40c16c2faa225846f54973e` and correction commit `a0d5649a60d02bf6289208d581d979102e31d227`.

I also consumed the assigned OTHER-account partner result:

- fleet01/B05, `BT4-TCEX-v1`, report commit `c03ac5520b1b712814607a8d1c97301dd8c9948b`. Its support-correct two-cycle bypass lemma says that if a cycle-supported witness `w` on `B` has an `R`-internal bypass from `w^-` to `w^+` of length `ell`, receives an arc from `A`, and has fan `m` on `A`, then `m<=ell`; equality gives a fully accounted neutral two-cycle exchange and an acyclic exchanged remainder.

Compatible structural inputs used for interpretation are fleet03/B04's repaired witness-support split (scientific commit `0ea8fe6265827eb76c5fb8f15cd7f6ee092e9003`, repair `b7f4d42fab613e176f04ffbe165c59e964f22e27`) and fleet03/B06's tight-port result (`4e204703776c90319afc67c4a03d56d474272d9c`).

## Compact conditional end-to-end route

Assume BT4 false. The lead's corrected normal form permits working in an oriented exact-outdegree-seven minimum counterexample `D` containing a globally minimum-total three-cycle packing `C1,C2,C3`, with acyclic remainder

`R = V(D) \ (V(C1) union V(C2) union V(C3))`.

Moreover:

1. every arc is dominated, hence for every vertex `x`, the induced digraph `D[N^-(x)]` contains a directed cycle;
2. `D` is 3-vertex-strong;
3. for a sink `x` of `R`, a packed cycle receiving at least three outarcs from `x` sends no arc back to `x`;
4. for each deleted pair of packed cycles, either a surviving vertex sends at least six arcs into the pair, or at least three surviving vertices send exactly five arcs into the pair;
5. a pair witness supported on the complementary packed cycle has the exact `6-cross/0-R-exit` or `5-cross/1-R-exit` form and must be handled by a genuine two-cycle exchange, not by the remainder one-vertex exchange.

Thus an end-to-end proof would follow once both top-level witness branches are eliminated:

- **SIX:** some pair has a six-fan witness; treat an `R`-supported witness by the one-vertex/path-fan machinery and a cycle-supported witness by the partner's two-cycle bypass/linkage machinery;
- **NO-SIX:** no pair has a six-fan witness. The new result below forces every remainder sink into a unique `3|2|2` heavy/light pattern and then decomposes the domination cycle in `N^-(x)` into an exact one-port or two-port light-cycle geometry. In the one-port case a legal packing replacement creates a strong reachability separation and, by 3-connectivity, two forced excursions through the other packed objects.

This is a structural split, not a completion of the two splice branches.

## Lemma 1 — the global no-six branch forces sink type `(3,2,2)`

Assume the global NO-SIX branch: for every pair of packed cycles and every vertex surviving deletion of that pair, the pair fan is at most five.

Let `x` be any sink of the DAG `R`, and put

`a_i = |N^+(x) intersect V(C_i)|`.

Because `x` has outdegree exactly seven and no outneighbor in `R`,

`a_1+a_2+a_3=7`.                                           (1)

Because `x` survives deletion of any two packed cycles and we are in NO-SIX,

`a_i+a_j <= 5` for all distinct i,j.                       (2)

Sort `a_1>=a_2>=a_3`. If `a_1>=4`, then (2) gives `a_2<=1` and `a_3<=1`, contradicting (1). Hence `a_1<=3`. Three nonnegative integers at most three summing to seven have only the sorted possibilities `(3,3,1)` and `(3,2,2)`, and `(3,3,1)` violates (2). Therefore

`                 (a_1,a_2,a_3) = (3,2,2)` up to permutation.     (3)

Call the 3-fan cycle `H` and the two 2-fan cycles `B,C`. The standard one-vertex minimum-packing exchange gives

`                         H not-> x.                              (4)`

This proves, without a counting independence assumption, that every sink in the global NO-SIX branch has exactly one heavy packed cycle and exactly two light packed cycles.

## Lemma 2 — a light cycle has at most one direct return port

Let `B` be one of the two light cycles and suppose `b in B` satisfies `b->x`. The lead's direct-return exchange says

`N^+(x) intersect B subseteq {b^+,b^{++}}`.

The fan has size exactly two by (3), hence

`N^+(x) intersect B = {b^+,b^{++}}`.                      (5)

There cannot be a second vertex `c!=b` of `B` with `c->x`. Such a second port would similarly force

`{c^+,c^{++}}={b^+,b^{++}}`,

which is impossible on a directed cycle of length at least three. (The minimum counterexample is oriented, so packed cycles have no digons.) Therefore each light cycle has **at most one** vertex sending an arc to `x`.

In particular a light return is not merely a fan bound; it fixes an exact consecutive two-fan and a unique port.

## Lemma 3 — the domination cycle at a no-six sink has exactly one or two light ports

Arc domination gives a directed cycle

`Q subseteq D[N^-(x)]`.                                      (6)

Since `R` is acyclic, `Q` must meet at least one packed cycle. By (4), it cannot meet the heavy cycle `H`. By Lemma 2, it meets each of `B,C` in at most one vertex. Consequently exactly one of the following holds.

### P1: one-port domination cycle

For one light cycle, say `B`,

`Q intersect (C1 union C2 union C3) = {b}`

where `b in B` is the unique return port. Every other vertex of `Q` lies in `R` and sends an arc to `x` because `Q subseteq N^-(x)`.

### P2: two-port domination cycle

There are unique ports `b in B`, `c in C` and

`Q intersect (C1 union C2 union C3) = {b,c}`.

Again all other vertices of `Q` lie in `R`, and (5) holds simultaneously for `B` and `C`:

`N^+(x) intersect B={b^+,b^{++}}`,
`N^+(x) intersect C={c^+,c^{++}}`.                          (7)

Thus the entire no-six sink branch is reduced to a genuine directed one-port collar or a genuine cross-light two-port cycle. No tournament property is used.

## Lemma 4 — one-port replacement gives a reachability wall

Assume P1. Write

`Q = b -> r_1 -> ... -> r_t -> b`,

with every `r_j in R`. The cycle `Q` is disjoint from `H` and `C`, so `H,C,Q` is another three-cycle packing. Global minimum of `C1,C2,C3` implies

`|Q| >= |B|`.                                                (8)

Equivalently `t>=|B|-1`. Let the corresponding new remainder be

`R' = (R \ {r_1,...,r_t}) union (V(B)\{b})`.               (9)

Because `H,C,Q` are three disjoint directed cycles in a BT4 counterexample, `D[R']` is acyclic.

Now `x` is not on `Q` (there are no loops, while every vertex of `Q` sends to `x`), so `x in R'`. Equation (5) gives `x->b^+`; along the old directed cycle `B`, the set `B-b` contains a directed path from `b^+` to every vertex of `B-b`. Hence in `R'`,

`x` reaches every vertex of `B-b`.                          (10)

Therefore no vertex of `B-b` can reach `x` in `R'`: otherwise (10) plus that return path is a directed cycle of `R'`, contradicting acyclicity. In particular

`                     there is no R'-path b^- -> x.          (11)`

This is stronger than the original direct-port uniqueness: after the legal replacement `B -> Q`, the whole freed directed block `B-b` lies strictly downstream of `x` in the exchanged DAG.

## Corollary 5 — 3-strongness forces two packed-object excursions in P1

The lead proves `D` is 3-vertex-strong. Hence `D-b` is 2-vertex-strong. By directed Menger, there are two internally vertex-disjoint directed paths from `b^-` to `x` in `D-b`.

By (11), neither can lie wholly in `R'`. The complement of `R'` in `D-b` is precisely

`V(H) union V(C) union (V(Q)\{b})`.                          (12)

Thus each of the two internally disjoint `b^-`-to-`x` paths must meet one of the three currently packed objects `H`, `C`, or `Q-b` internally. This is a source-valid linkage forcing statement: the one-port branch cannot be repaired inside the exchanged DAG; two independent excursions through the packed structure are unavoidable.

This dovetails with fleet01/B05's `BT4-TCEX-v1` and fleet03/B05's corrected Menger linkage mechanism: the next splice may be sought among explicit cross-packed excursions rather than among arbitrary remainder paths.

## Lemma 6 — one-port forces an `R` dominator fork at the second light successor

Still in P1, use (5). The arc `x->b^{++}` is dominated, so some vertex `d` satisfies

`d->x` and `d->b^{++}`.                                    (13)

The dominator `d` cannot lie on `H` by (4). It cannot be a vertex of `B`: `b` is the unique B-port, and chordlessness of the globally minimum packed cycle excludes `b->b^{++}`. It cannot lie on `C`, because P1 means no vertex of `C` sends to `x`. Therefore

`                         d in R`.                            (14)

So the one-port case always contains a canonical remainder fork

`                         d -> {x,b^{++}}`.                   (15)

This fork is not asserted to close the branch; it is an explicit attachment point for the pair-deletion witnesses and two-cycle bypass machinery. It also shows that P1 is not a bare long collar: domination exports one of the consecutive light-fan vertices back into the remainder.

A useful partner-facing refinement follows from the domination property on `N^-(x)`: every vertex of `N^-(x)` has an in-neighbor in `N^-(x)`, so iterating predecessors from `d` produces a directed cycle in `N^-(x)` with a directed tail to `d`. In P1 every such cycle has the same unique packed port `b`; therefore there is a directed path

`b -> R -> ... -> d -> b^{++}`                              (16)

whose internal vertices lie in `R`. It is an `R`-internal bypass of the single vertex `b^+` of `B`. This gives an explicit interface to the partner's support-correct bypass exchanges whenever `b^+` is selected as a cycle-supported pair witness.

## Corrected structural case split now available

Combining the lead, the partner repair, and the lemmas above yields the following honest top-level tree for a minimum counterexample.

### Branch S — some pair has a six-fan witness

- **S-R:** an `R`-supported witness. It is heavy on one deleted cycle; the one-vertex/path-fan avoidance machinery applies.
- **S-C:** a complementary-cycle-supported witness. It has exact `6-cross/0-R-exit` structure. The fleet01/B05 two-cycle bypass lemma and fleet03/B05 3-connectivity linkage trichotomy are the appropriate tools; no fake remainder witness is introduced.

### Branch N — global no-six

Every sink has exact fan `(3,2,2)`, with unique heavy cycle `H` and two light cycles `B,C`. A domination cycle in `N^-(x)` has only:

- **N1 / P1:** one light port. Then `B->Q` replacement satisfies the metric bound (8), creates the reachability wall (11), forces two internally disjoint packed-object excursions by Corollary 5, and supplies the remainder dominator fork (15) plus bypass (16).
- **N2 / P2:** one port on each light cycle. Then the domination cycle itself is a cross-light object with both exact consecutive two-fans (7); this is the natural simultaneous two-cycle-splice branch.

The earlier eight sink fan types have therefore collapsed in the global no-six branch to a single numerical type plus two exact port geometries. The remaining difficult structures are separated by support, not by an unsupported average-degree argument.

## First remaining essential implication

The exact next implication is not another fan count. It is one of the following source-valid splice statements:

1. in **N1**, use the two Menger excursions from `b^-` to `x` together with the fork `d->{x,b^{++}}` and the pair-deletion witness structure to construct two replacement cycles disjoint from the untouched packed cycle, or derive a strict short return forbidden by the corrected path-fan lemma; or
2. in **N2**, use the two-port domination cycle and the exact two-fans on `B,C` to construct a simultaneous replacement of `B,C`, or force an fleet01/B05 short bypass; or
3. in **S-C**, close the `6-cross/0-R-exit` cycle-supported witness by the partner's segment-bypass/linkage alternative.

No one of these splice implications is proved here. Full BT4 therefore remains open.

## Adversarial checks

- The argument uses genuinely directed cycles in the original digraph, never the one-reversed-arc relaxation.
- It uses the global NO-SIX hypothesis only where needed; a six-fan branch is preserved rather than silently excluded.
- The unique-port proof requires the exact 2-fan and oriented-cycle length at least three, both supplied by the lead's minimum-counterexample normal form.
- `Q` is a cycle in the actual induced inneighborhood `N^-(x)` supplied by arc domination; it is not an assumed shortest or induced cycle.
- Replacing `B` by `Q` in P1 is legitimate because `Q` has exactly one packed vertex and otherwise lies in `R`; the other two packed cycles remain disjoint.
- The reachability wall is derived in the exchanged remainder and does not infer an ordering in the old remainder.
- Directed Menger is used only after deleting `b`, where 3-vertex-strongness gives the required 2-vertex-strong graph. No prescribed path is forced into a Menger family.
- Lemma 6 excludes `d in B` using both unique-port and chordlessness; without chordlessness the conclusion `d in R` would not follow.
- No novelty claim, finite-order reduction, tournament substitution, or target-level proof is made.

## Outcome

`ESSENTIAL_STEP_APPLIED`.

The no-six branch now has an exact source-bound structural split: each sink is `3|2|2`, each light return has one port and an exact consecutive 2-fan, and every domination cycle is either a one-port collar or a two-port cross-light cycle. In the one-port case a legal packing replacement produces a reachability wall, two forced cross-packed Menger excursions, and a canonical remainder dominator fork. These are concrete inputs to the shared two-cycle exchange machinery; they do not yet pay the final splice implication.
