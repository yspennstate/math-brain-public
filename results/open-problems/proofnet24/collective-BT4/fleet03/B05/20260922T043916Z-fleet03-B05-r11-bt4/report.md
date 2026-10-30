# BT4 fleet03/B05 — the Case-A double-pivot residual has a strict 5-cycle exchange

Run: `20260922T043916Z-fleet03-B05-r11-bt4`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-R4-CASEA-SHORTCYCLE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and role

Target: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs and hence directed digons are allowed in the source problem.

The fleet03/B05 assignment is to prove the disjointness-preserving exchange promised by the current two-partition/linkage candidate, without replacing minimum-degree information by averages. This report works inside the team's inherited minimum-counterexample normal form and does not claim full BT4.

## Source and team state actually consumed

The external source boundary remains the one fixed by the collective target record: the genuine k=4 Bermond--Thomassen problem remains open; the 2026 Bessy--Muis--Sereni--Steiner--Wiederrecht theorem permits one reversed arc and is not counted here as a directed-cycle theorem. The genuine lower-k input retained by the team is the minimum-outdegree-five theorem giving three vertex-disjoint directed cycles.

Latest complete lead state read before this report: fleet02/B04 run `20260922T041847Z-b04-bt4-r11`, primary mathematical blob `596929efe56393d3ab515544fa33ec6a19e75c83` with controlling strengthening blob `8bfc5b33fb232c8543856d6d9ad3b0e8fdc3432c`. Its current global unpaid interface is a genuine packed-port disjointness/splice theorem (plus the separate SIX closure), not mere existence of cross paths.

Named OTHER-account partner result actually applied: fleet04/B06 `BT4-R4-LOWFAN-INPORT-TRIANGLE-v1`, run `20260922T041133Z-b06-bt4-r13`, canonical scientific blob `d95ac60508cb0a415c33106169d1527da385406f`. The exact part used is its four-remainder long-source F2 state: two old remainder sinks occur at adjacent source ports, the old sink has a unique other-light inport, and its three inports form a directed triangle.

Compatible cross-account refinement also consumed: fleet02/B05 `BT4-R4-DOUBLE-PIVOT-CONFLUENCE-v1`, run `20260922T042100Z-b05-bt4-e5df42d4`, which performs the two neutral sink pivots simultaneously and derives the high-exit split used below. No peer outcome label is substituted for its proved statements.

## Inherited exact state

Assume BT4 false and work in the inherited oriented exact-outdegree-seven, arc-dominated, 3-vertex-strong minimum-counterexample normal form. Let `(H,S,U)` be a globally minimum-total packing of three directed cycles, with nonempty acyclic remainder. Packed cycles are chordless.

In the named partner's `|R|=4`, global-`NO-SIX`, long-source F2 branch, write consecutive source vertices

`p -> q -> s -> t -> ... -> p`,

with `|S|>=6`. There are distinct old remainder sinks `x,y`, a unique other-light inport `u in U -> x`, and a remainder inport `c->x`. The three vertices `{p,u,c}` form a directed triangle. Put

`v=u+`.

The compatible double-pivot result gives two disjoint neutral replacement cycles

`S_y = q -> y -> t -> S[t,q]`,

`U_x = u -> x -> u++ -> U[u++,u]`,

and the new remainder

`R''={c,z,s,v}`

is acyclic. Both replacements preserve cycle order, so `(H,S_y,U_x)` is again globally minimum. The freed vertices have exact one-support-edge budgets. Let

`e_s=d^+_{R''}(s)`, `e_v=d^+_{R''}(v)`.

If either is zero, the existing SIX interface is reached; if either is one, the existing five-witness interface is reached. Thus the only high-exit residual has

`e_s>=2`, `e_v>=2`.                                              (1)

The double-pivot proof also gives

`s->c or v->c`.                                                  (2)

The two orientations of the inport triangle are

Case A: `p->u->c->p`,

Case B: `u->p->c->u`.

The previous report stopped Case A at the boundary `|S|=6`. The next lemma removes that residual entirely.

## Lemma — Case A is impossible in the high-exit residual

Under (1), the triangle orientation

`p->u->c->p`                                                     (3)

cannot occur.

### Proof

If `s->c`, then the already visible cycle

`c -> p -> q -> y -> s -> c`

has order five, is disjoint from `H` and `U_x`, and can replace `S_y`. Since `|S_y|=|S|>=6`, this strictly decreases the total order of the globally minimum three-cycle packing, contradiction.

Hence in Case A we must have

`s not->c`.                                                      (4)

By (2), (4) forces

`v->c`.                                                          (5)

Now use the exact remainder `R''={c,z,s,v}`. Because `e_s>=2` and (4) excludes `c`, the only possible remainder outneighbors of `s` are `z` and `v`, and therefore both occur; in particular

`s->v`.                                                          (6)

The neutral source pivot changed the chosen packing but did not delete ambient arcs of the digraph, so the original source edge

`q->s`                                                           (7)

still exists. From (3) we have `c->p`, and the original source cycle gives `p->q`. Combining (5)--(7) yields the genuine directed 5-cycle

`C_5 = q -> s -> v -> c -> p -> q`.                             (8)

The vertices of (8) are pairwise distinct: `p,q,s` are old source vertices, `v` is the freed old U vertex, and `c` is an old remainder vertex. In the double-pivot packing, `q,p` lie on `S_y`, while `s,v,c` lie in `R''`; hence `C_5` is disjoint from both untouched `H` and the replacement cycle `U_x`.

Therefore `(H,C_5,U_x)` is a legal three-cycle packing of total order

`|H|+5+|U| < |H|+|S|+|U|`,

because `|S|>=6`. This contradicts global minimum. QED.

## Corollary — the high-exit long-source F2 branch is bounded entirely on U

In the double-pivot high-exit branch, Case A is eliminated. Hence only Case B survives:

`u->p->c->u`.

The compatible double-pivot analysis then gives:

- if `v->c`, the triangle `u->v->c->u` replaces `U_x`, so global minimality forces `|U|=3`;
- if `v not->c`, (2) forces `s->c`, and `c->u->x->s->c` is a directed 4-cycle disjoint from `H,S_y`, so global minimality gives `|U|<=4`.

Thus the previous high-exit alternative

`|S|=6 or |U|<=4`

sharpens to the single conclusion

`|U|<=4`,                                                        (9)

with the triangle orientation forced to Case B. In particular, the entire `|S|=6` residual from Case A was an artifact of not using the ambient edge `q->s` after the neutral pivot.

## Compact conditional end-to-end argument after this run

Within the four-remainder long-source F2 branch supplied by the named partner:

1. The adjacent old sinks and exact inport triangle permit simultaneous neutral pivots on `S` and `U`.
2. A freed vertex with zero new-remainder exits enters SIX.
3. A freed vertex with one new-remainder exit enters the existing five-witness/collar interface.
4. If both freed vertices have at least two exits, this report eliminates Case A by the strict 5-cycle exchange (8).
5. Hence every surviving high-exit state has Case-B orientation and `3<=|U|<=4`.

So `R4-TWOSINK-SPLICE` is no longer an unbounded two-light-cycle splice in the high-exit residual. Its surviving hard cases are now: the existing five-witness interface, the bounded Case-B other-light cycle of order three or four, and the separate SIX interface.

This is directly disjointness-preserving: the contradiction uses an explicit directed cycle (8) that is vertex-disjoint from the two cycles retained in the packing, rather than counting an opposite-cross pair or an edge-disjoint surrogate as two cycles.

## Failure checks and nonclaims

- The ambient edge `q->s` is legitimate after the neutral pivot because pivots alter only the selected packing, not the underlying digraph.
- The five vertices in (8) are distinct by their old support/remainder provenance.
- `v` is not on `U_x`; it is exactly the old U vertex freed by the neutral U pivot.
- `c,s,v` lie in `R''`, so (8) is disjoint from `U_x`; `p,q` lie only on the source support, so (8) is disjoint from `H` as well.
- The strict inequality uses the named partner's long-source hypothesis `|S|>=6`; no average-degree substitute is used.
- Case B with `|U|=3` or `4`, the one-exit five-witness branch, and SIX are not closed here.
- The latest lead's separate heavy-triangle two-port/double-escape splice remains unpaid.
- Full BT4 and literature novelty are not claimed.

## Honest status

`ESSENTIAL_STEP_APPLIED`.

The named partner's long-source two-sink state, together with the compatible double neutral pivot, now admits a strict disjointness-preserving packing reduction throughout triangle Case A. The surviving high-exit branch is forced into Case B with `|U|<=4`; the previous `|S|=6` Case-A residual is eliminated.
