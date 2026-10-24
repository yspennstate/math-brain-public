# BT4 account03/B06 r13 — arc-domination closes the quadrilateral fork

Outcome: `ESSENTIAL_STEP_APPLIED`  
Candidate: `BT4-F3-R3-FORK-DOMINATOR-ESCAPE-v1`  
Target status: `OPEN_NOT_PROVED`  
Execution context: `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and exact source boundary

The target is the k=4 Bermond--Thomassen statement in the collective order: every finite loopless simple digraph with minimum outdegree at least seven contains four vertex-disjoint directed cycles. Digons are allowed in the target statement.

Fresh control was read from `yspennstate/math-research-brain` under owner revision `2026-09-22.2`, active programme `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. The exact account03/B06 assignment is constrained/local-configuration search plus symbolic-family testing on BT4, with named partner account04/B04. This run used no authenticated brain retrieval, so it remains `WITHOUT_VERIFIED_BRAIN` and makes no brain-readiness claim.

### Named OTHER-account partner actually consumed

I read the complete source-bound account04/B04 handoff

- `BT4-F3-R3-PIVOT-SWITCH-TRIANGLE-v1`, shared handoff commit `289a6ee8a640dffc9ac197e63abc4723c6a47071`,
- canonical scientific report commit `d68f471f46e5f1837417574c2e0bec07dd3280d2` in `yspennstate/math-open-problems`.

The partner proves that in the defect-one residual-three tight-pivot orbit, a switch between the two light supports followed by one further surviving pivot either exits to SIX/cyclic remainder/exact-R4 compression or forces the repeated light support to be a directed triangle. Thus the residual pivot debt splits into a monochromatic one-support orbit and a mixed orbit with triangular light support.

### B06 predecessor used

The immediately preceding B06 theorem was `BT4-F3-R3-MIXED-APEX-NEUTRAL-FORK-v1`, source-bound handoff commit `f5068bf38038b780d3184a777348362284a6026f`, canonical report commit `28341c2a972d01b6823c4ec244745465e43ec08a`.

Its R3-D internally-disjoint-ladder branch yields a mixed directed cycle `K` of order 3 or 4 through the two light return ports. In the quadrilateral case, every three-hit apex gives a fresh packed-to-packed cross except one local symbolic pattern. Up to swapping the two light supports and relabelling the residual vertices, that pattern is

`K = e -> a -> c -> b -> e`,

with light support `L` containing the return port `c`, and

`z = c^-`, `z -> c,a,b`, `z !-> e`.

The preceding run called this the **immediate two-residual fork** and repaired it only by two neutral exchanges. The stronger claim that the quadrilateral always gives a fresh packed cross had been rejected because this local pattern was satisfiable under the bounded constraints then checked.

The present run re-tests that failure against one inherited normal-form hypothesis that the local checker had deliberately not imposed: **arc domination**.

## 2. New theorem — BT4-F3-R3-FORK-DOMINATOR-ESCAPE-v1

### Statement

Work in the inherited oriented, arc-dominated, chordless minimum-packing normal form, in the R3-D exceptional quadrilateral fork above. Let the current three-cycle packing be `(J,L,M)` and the residual set be `{a,b,t}`, where `t` is the remainder sink and the exact light fan at return port `c in L` is

`N+(t) intersect L = {c+,c++}`.

Then the exceptional fork necessarily has a **fresh packed-to-L two-hit connector**: there exists a vertex

`y in V(J) union V(M)`

such that

`y -> c^-` and `y -> c`.

In particular the exceptional fork is not a genuine no-fresh-cross leaf. Therefore, in the full inherited normal form,

`QUADRILATERAL MIXED RETURN => FRESH PACKED CROSS`.

The symmetric statement holds for the exceptional fork on `M`.

### Proof

Put `z=c^-`. The support arc

`z -> c`

is an arc of the chordless directed cycle `L`. By inherited arc domination, there exists a vertex `y` dominating this arc, i.e.

`y -> z` and `y -> c`.                                           (1)

We show that `y` cannot lie in `L union {a,b,t}`.

**(i) `y` cannot lie on `L`.**

Because `L` is chordless, the only arc from a vertex of `L` to another vertex of `L` is its directed cycle-successor arc. A single vertex `y in L` therefore cannot send to both distinct vertices `z` and `c`. If `|L|=3`, the only apparent edge case is the third cycle vertex; one of the two required arcs in (1) is then the reverse of a cycle arc, forbidden by orientedness. The choices `y=z` or `y=c` would require a loop. Hence `y notin L`.

**(ii) `y` is neither `a` nor `b`.**

The exceptional fork itself contains

`z -> a` and `z -> b`.

The inherited minimal counterexample is oriented, so neither reverse arc `a->z` nor `b->z` exists. Each would be required by (1). Hence `y notin {a,b}`.

**(iii) `y` is not `t`.**

The exact two-target light fan of the remainder sink is

`N+(t) intersect L = {c+,c++}`.

In particular `t !-> c`, whereas (1) requires `y->c`. Hence `y != t`.

The current packing covers every vertex outside the three-vertex remainder `{a,b,t}`. Since `y` lies neither in that remainder nor on `L`, it lies on one of the other two packed cycles, `J` or `M`. Together with (1), this is exactly a fresh packed-to-`L` connector, in fact one hitting two consecutive `L` vertices `c^-` and `c`. QED.

## 3. Why the previous counterexample was useful rather than a dead end

The predecessor's symbolic exception

`K=e->a->c->b->e`, `z=c^-`, `z->c,a,b`, `z !-> e`

is still locally satisfiable if one asks only for the mixed-cycle orientation, chordlessness, the three-hit apex and the neutral-exchange walls. It fails only after restoring the inherited requirement that the cycle arc `z->c` itself have a common predecessor.

This identifies the exact missing constraint and repairs the failed stronger lemma instead of discarding it. Any dominator of `z->c` that is not a fresh cross would have to lie in `L union {a,b,t}`; the proof above excludes each such location. Thus the failure certificate pinpoints the universal escape route.

## 4. Exact symbolic-family check

`checker.py` exhausts support orders `3 <= |L| <= 80`. For each order it tests every possible internal location for a dominator of `z->c`:

- every vertex of the chordless cycle `L`;
- residual vertices `a,b,t`;
- one symbolic external-packed category.

It enforces exactly the local facts used in the proof: chordlessness on `L`, orientedness against `z->a,z->b`, and the exact sink fan `{c+,c++}`. Results:

- support sizes checked: 78;
- internal candidate locations: 3,471;
- internally admissible dominators: 0;
- external-packed admissible categories: 78;
- the predecessor's local fork without arc domination remains SAT;
- the fork with arc domination but no fresh cross is UNSAT.

This bounded computation is only a sanity check. The proof in Section 2 is uniform in `|L|`.

Checker creation commit: `e53b1dba253b2d26daf65bed7aa0a0a71d04a777`.  
Checker SHA-256: `e4fea2ea94052489afaa31e1391f4058d551d65f819910e0e77bd0dbb571670e`.

Checker-output creation commit: `91243438ebcb84c2a06131179d198de24dc1575e`.  
Output SHA-256: `9810e25ea224be5b0be25e46f8566ce3c9379de650456ded586c0ddd865e46dd`.

## 5. Joint consequence with account04/B04

Combining this theorem with the predecessor mixed-apex split gives the sharper R3-D classification

- `K` quadrilateral: **fresh packed cross always**;
- `K` triangle: **fresh packed cross or unused-residual triple-hit**.

So the old quadrilateral neutral-fork leaf disappears entirely once full arc domination is used.

The named partner's `BT4-F3-R3-PIVOT-SWITCH-TRIANGLE-v1` then constrains any continuation of the remaining triangle/no-fresh-cross leaf that enters the defect-one tight-pivot orbit: a support switch followed by another surviving pivot either reaches an already recognized exit or forces the repeated light support to be triangular. Thus a no-exit continuation after the present reduction must stay in one of three genuinely narrower mechanisms:

1. the **fresh-cross splice** branch;
2. the **unused-residual triple-hit triangle** branch before a decisive cross is extracted;
3. conditional on entering the tight-pivot mechanism, the partner's **MONO** one-support orbit or **TRI** triangular-support orbit.

This is a source-valid joint reduction; it is not a claim that the partner theorem by itself closes the triangle leaf.

## 6. First unpaid implication

The next decisive obligation is

`BT4-F3-R3-TRIANGLE-TRIPLEHIT-DOMINATOR-LIFT-v1`:

in the mixed-triangle leaf, where the unused residual vertex hits both packed return ports and the residual ladder vertex, apply arc domination to the two packed-hit arcs and prove that either

- one dominator lies on a third/other packed support, yielding the required fresh cross;
- a same-support dominator creates a short bypass priced by global minimum packing;
- a residual dominator creates a directed residual/exchanged-remainder cycle;
- or the state enters the partner's tightly constrained MONO/TRI pivot orbit with an additional connector incompatible with survival.

The already-produced fresh-cross cases should be fed into the established fresh-port / four-port connector machinery rather than reclassified again.

## 7. Status

This run closes one previously explicit local survivor but does **not** prove BT4. The target remains `OPEN_NOT_PROVED`. Separate SIX, F2, larger-remainder and global connector-splice debts remain. No novelty claim is made from this repository search alone.
