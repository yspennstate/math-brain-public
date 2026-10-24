# BT4 lead attempt — primitive-trace mixed packing obstruction

Outcome: `CANDIDATE_REFUTED`
Target status: `OPEN_NOT_PROVED`
Execution context: `WITHOUT_VERIFIED_BRAIN`
Run: `account02-B04-20260922T094740Z-bt4-r11`

## 1. Source-exact scope and live controls

Target: prove the `k=4` Bermond--Thomassen statement for every finite loopless digraph with at most one arc per ordered pair and minimum outdegree at least seven: four vertex-disjoint genuinely directed cycles, with digons allowed.

Fresh owner control was revision `2026-09-22.2`, active programme
`COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`; no later applicable B04 stop was seen before this report. New installation and benchmark work remained stopped.

Public theorem boundary used:
- Bessy--Muis--Sereni--Steiner--Wiederrecht, arXiv:2608.12948 (13 Aug 2026): the original Bermond--Thomassen conjecture remains unresolved for every `k>=4`; their theorem allows a cycle that becomes directed after reversing one arc, so it is not substituted for BT4.
- Lichiardopol--Pór--Sereni, SIAM J. Discrete Math. 23 (2009), DOI 10.1137/080715792: minimum outdegree five forces three vertex-disjoint directed cycles; their strengthened `k=2` theorem permits at most two outdegree-two exceptions.

Repository sources actually consumed:
- lead handoff `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1`, commit
  `3d1cdc39d7512ad857e134f23740c027ef879764`, blob
  `b0c1c37b1d36fd7cf855946f20eb382a61cd346d`;
- named partner account03/B05 report
  `BT4-FRESH-PORT-OR-C-WALL`, blob
  `060eddbca21de4d78c8059e71398a7d1833d9f64`;
- OTHER-account account01/B06 theorem
  `BT4-PRIMITIVE-TORUS-NO-CANONICAL-2SPLICE-v1`, commit
  `0498c881be30ff6ab345a45d8dd5c7cbe511ac6d`, blob
  `2e8606f5a2bf0e1a7a76725baf3022a780a6840c`;
- this lead's preceding live primitive checker, blob
  `f01934314f1dd03787d5cef009ac6d2042b4250b`, whose finite zero-splice pattern was proved analytically by account01/B06.

The partner theorem is used substantively below: its connector-rank lemma says that two disjoint mixed replacement cycles require two endpoint-disjoint connectors in each direction, and its 3-vertex-strong port-avoidance lemma gives a fresh `B->A` connector unless the path is forced through the third packed support `C`.

## 2. Compact conditional end-to-end proof state

The inherited exact-seven oriented minimum-counterexample program reduces a deficient minimum three-cycle packing to recognized interfaces. Conditional on closing all four of the following, BT4 follows:

1. the separate `SIX` interface;
2. the bounded `F2/F3` short-support interfaces;
3. the seven-remainder triangle-pinwheel/support-carried omitted-sink interface;
4. the clean heavy-triangle four-port coalescence interface.

For (4), the lead theorem constructs a genuine clean mixed cycle and, after deleting it and applying the genuine `k=3` theorem, lifts an external three-hit witness to either a cross-packed connector or a same-support bypass. Same-support bypasses feed the compatible-bypass program. The remaining local branch has a primitive two-support trace plus a direct terminal cross and an endpoint-matched remainder path.

Account03/B05 already proves that endpoint multiplicity alone does not raise the required connector matching rank. Account01/B06 then proves that no four selected primitive-trace ports admit the hoped-for two canonical support splices.

The first missing inference before this run was therefore: can a *noncanonical* pair of mixed cycles, possibly using longer alternating sequences of trace connectors and the endpoint-matched detour, close the same coalesced state?

The theorem below answers **no** for the entire trace-parallel class. This refutes that candidate mechanism and makes an off-trace/third-support/bypass/remainder exit mathematically necessary.

## 3. Primitive trace model

Let

`A = a_0 a_1 ... a_{m-1} a_0`,
`B = b_0 b_1 ... b_{n-1} b_0`

be vertex-disjoint directed cycles. Let `w=w_0...w_{m+n-1}` be a cyclic word containing exactly `m` plus signs and `n` minus signs. Associate a state
`c_t=(i_t,j_t) in Z_m x Z_n` using the exact recurrence in the lead checker. Equivalently, in reverse occurrence order,

- crossing backward past a `+` occurrence advances the first coordinate by one;
- crossing backward past a `-` occurrence advances the second coordinate by one.

A `+` state `(i,j)` authorizes an `A->B` connector from `a_i` to `b_j`.
A `-` state `(k,l)` authorizes a `B->A` connector from `b_l` to `a_k`.

For the base primitive graph the connector is the direct cross arc. For the strengthened statement below, a **trace-parallel connector** may instead be any directed path with the same two support endpoints and interior disjoint from `A union B`.

A **trace-respecting mixed cycle** is a simple directed cycle meeting both `A` and `B` which, between the two supports, uses only trace-parallel connectors and, while on a support, follows its positive directed support arcs. Same-support bypasses, visits to the third packed support, and other off-trace excursions are deliberately excluded: those are precisely recognized exits from the current obstruction.

## 4. Reverse-gap lemma

For state occurrences `s,t`, let `[s,t)_rev` be the cyclic list of occurrences encountered from `s` backward to but not including `t`.

If `w_s=+` and `w_t=-`, then the positive directed distance on `B` from `b_{j_s}` to `b_{j_t}` equals the number of minus signs in `[s,t)_rev`.

Indeed the reverse recurrence increments the second coordinate exactly once at every minus occurrence. The interval excludes the terminal minus occurrence `t`, so its minus count is at most `n-1`; hence the modular coordinate difference is represented by that ordinary integer, not by the same residue plus a full turn.

Similarly, if `w_s=-` and `w_t=+`, the positive distance on `A` from `a_{i_s}` to `a_{i_t}` equals the number of plus signs in `[s,t)_rev`, which is at most `m-1`.

Consequently every occurrence strictly inside `[s,t)_rev` has its `B`-coordinate on the first support path in the `+,-` case, and its `A`-coordinate on the first support path in the `-,+` case. Equality with an endpoint is allowed when no relevant sign occurs between them.

## 5. Selected occurrences of one simple mixed cycle

**Lemma (`TRACE-ORDER`).** In a trace-respecting simple mixed cycle `Z`, the trace states used by its successive support-switching connectors occur in exactly the same cyclic order as reverse occurrence order in `w`.

**Proof.**
Along `Z`, connector signs alternate. Consider two consecutive connectors of `Z`, represented by states `s,t`.

If `w_s=+` and `w_t=-`, `Z` uses the directed `B` segment from `b_{j_s}` to `b_{j_t}`. By the reverse-gap lemma, every trace occurrence strictly between `s` and `t` in reverse occurrence order has its `B`-coordinate on that segment. If another connector state `u` used by `Z` occurred there, then `Z` would visit `b_{j_u}` on the `s`-to-`t` support segment and also use the same vertex as an endpoint of the connector represented by `u`. That repeats a vertex of the simple cycle (including the case where the coordinate equals a segment endpoint), impossible.

The `-,+` case is identical on `A`.

Thus no selected connector occurrence lies between successive connector states of `Z` in reverse occurrence order; hence those states occur in reverse word order exactly as they occur around `Z`. QED.

This proof handles zero-length support segments, where consecutive opposite-sign connector states can share one support endpoint. No distinct-coordinate assumption is needed.

## 6. New theorem — mixed packing number one

**Theorem (`BT4-PRIMITIVE-TRACE-MIXED-PACKING-ONE-v1`).**
For every primitive trace word `w`, there do not exist two vertex-disjoint trace-respecting mixed directed cycles. The conclusion remains true after replacing any trace cross arc by arbitrarily many trace-parallel directed connector paths with the same support endpoints.

**Proof.**
Assume `Z` and `Z'` are vertex-disjoint trace-respecting mixed cycles.

The connector occurrences selected by `Z` partition the cyclic reverse occurrence order of `w` into gaps between consecutive selected states. By `TRACE-ORDER`, each such gap corresponds to one directed support segment actually used by `Z`: a `+,-` gap is covered on `B`, and a `-,+` gap is covered on `A`.

Take any connector occurrence `u` used by `Z'`. It cannot equal a connector occurrence used by `Z`, because then the two cycles share the corresponding support endpoint(s). Hence `u` lies strictly inside one gap between consecutive selected occurrences `s,t` of `Z`.

If the gap has signs `+,-`, the reverse-gap lemma puts `b_{j_u}` on the `B` segment of `Z`. But `b_{j_u}` is also an endpoint of the connector used by `Z'`, so it is a vertex of `Z'`. Thus `Z` and `Z'` intersect. The `-,+` gap gives the same contradiction on `A`.

Therefore no connector occurrence can be used by `Z'`, impossible for a mixed cycle. QED.

The proof depends only on connector endpoint states, so arbitrary internal detours between the same support endpoints do not change it.

## 7. Decisive computation and a false shortcut caught

The exact checker saved in this run exhaustively enumerates every normalized primitive word for `2<=m,n<=6`, builds the two directed supports plus all trace cross arcs, enumerates all simple directed cycles, and tests for two vertex-disjoint mixed cycles.

Result: `1683` normalized words tested; `0` admit two disjoint mixed cycles.

This is only a finite audit of the analytic theorem, not its proof.

The same run also refutes a tempting shortcut: it is **false** that every vertex-minimal mixed cycle has only two cross edges. Among those `1683` words, `624` have a vertex-minimal mixed cycle with more than two cross edges. The smallest displayed witness is

`w = ++--++--`

with the vertex-minimal four-cross cycle

`A1 -> B2 -> A3 -> B0 -> A1`.

Therefore the new theorem cannot be obtained by reducing each mixed cycle to a canonical two-cross subcycle. The reverse-gap proof above is needed.

Exact run artifacts:
- `mixed_trace_packing_check.py`, creation commit
  `9b74d5c14f1c8d76702f01c71e1e18a1a5eb0972`;
- `mixed_trace_packing_output.txt`, creation commit
  `a6a934a200a0888166514e9d2bd9325dbdb0f47b`.

## 8. Application to the current coalescence debt

This theorem strictly strengthens both currently consumed peer observations.

First, account03/B05 proved that a direct cross and an endpoint-matched remainder path with the same support endpoints have connector matching number one. The new theorem shows that the problem is broader than matching number: **even arbitrarily many endpoint-disjoint trace states, and arbitrarily many same-endpoint parallel detours, cannot yield two vertex-disjoint mixed cycles while every support switch remains on the same primitive trace**.

Second, account01/B06 proved that the primitive trace has no pair of canonical two-splices. The new theorem removes the word `canonical`: no two trace-respecting mixed cycles of any alternating length exist.

Hence the current local candidate

`primitive-trace ports + endpoint-matched detours => two mixed replacement cycles`

is source-validly refuted.

The partner's next statement must therefore be sharpened. A merely fresh support port is not enough if its endpoint pair is another state on the same primitive trace. A successful closure has to force an actual **order-breaking exit**:

1. a cross-support connector whose ordered support endpoint pair is not a signed state of the primitive trace;
2. a same-support bypass;
3. a path through the third packed support `C`;
4. a directed cycle in the exchanged remainder / strict packing decrease / SIX-type recognized exit; or
5. directly, the fourth vertex-disjoint directed cycle.

This refinement does not refute account03/B05's port-avoidance lemma; it identifies which side of its `fresh connector or C-wall` dichotomy remains genuinely useful.

## 9. First unpaid implication after this run

`BT4-OFF-TRACE-OR-EXIT-v1`:

> In the exact clean heavy-triangle coalescence state inherited from
> `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1`, use minimum outdegree seven,
> arc domination, the acyclic remainder and 3-vertex-strongness to force
> either an order-breaking cross-support connector whose endpoint pair is
> outside the primitive trace and whose support order yields a legal
> replacement, or a same-support bypass, third-support mediation,
> exchanged-remainder cycle, strict smaller packing, SIX exit, or fourth
> disjoint directed cycle.

This is stronger than "find a fresh port": a fresh trace state does not suffice by the theorem above.

The other global debts (SIX, bounded F2/F3, seven-remainder pinwheel) remain separate. No full BT4 proof is claimed.

## 10. Status

`CANDIDATE_REFUTED`.

The refuted candidate is the pure primitive-trace/noncanonical two-support splice mechanism, including endpoint-matched parallel detours. The target remains open. The surviving proof route is narrower and now has a precise first local obligation: force an off-trace order break or a recognized non-two-support exit.
