# BT4 fleet04/B06 — 3-connectivity lifts the exact-six dual wall to a packed detour

Run: `20260922T051305Z-b06-bt4-r14`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-SIX-DUAL-WALL-LIFT-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and current source boundary

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs, hence directed digons, are allowed in the source problem.

Current external status was rechecked against Stéphane Bessy, Matthijs Muis, Jean-Sébastien Sereni, Raphael Steiner and Sebastian Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948, submitted 13 August 2026. Its abstract says that the genuine conjecture remains unresolved for all `k>=4`; its theorem at the `2k-1` threshold allows a packed cycle to become directed after reversing one arc. No such relaxed object is counted below as a directed cycle. The inherited genuine lower-k input is Lichiardopol--Pór--Sereni, SIAM J. Discrete Math. 23 (2009), 979--992: minimum outdegree five forces three disjoint directed cycles, with the strengthened two-cycle theorem used elsewhere in the team reduction.

No literature search miss is used as a novelty claim.

## Fresh team state actually consumed

Latest complete team-lead package actually read before this proof:

- fleet02/B04 run `20260922T041847Z-b04-bt4-r11`, primary candidate `BT4-HT-PREDECESSOR-SPLICE-v1`, report blob `596929efe56393d3ab515544fa33ec6a19e75c83`;
- controlling same-run strengthening blob `8bfc5b33fb232c8543856d6d9ad3b0e8fdc3432c`.

The controlling lead state retains the oriented exact-outdegree-seven, arc-dominated, 3-vertex-strong minimum-counterexample normal form with a globally minimum-total three-cycle packing and acyclic remainder. In the four-remainder heavy-triangle branch it now reduces the obstruction to a two-port light-inport cover or a double heavy-fan escape cage; its first global unpaid interface is genuine port-disjointness/splicing, plus the separate SIX closure.

Named OTHER-account assigned partner actually consumed and applied:

- fleet01/B04 run `20260922T044536Z-b04-bt4-r11`, candidate `BT4-R4-MAX-REMAINDER-ARC-COLLAPSE-v1`, report blob `b9b700749e5723c819b6643aa16c67c38db6c569`.

I adopt its legitimate lexicographic choice of the three-cycle packing: first minimize total packed order, then maximize the number of arcs induced by the remainder. Every older argument that uses only minimum total packed order remains valid for this choice. On the long-source four-remainder F2 double-pivot state, this partner theorem rules out the high-exit wall and forces `SIX` or an exact remainder-supported five-witness.

A newer compatible OTHER-account result is also applied:

- fleet02/B20 run `20260922T045919Z-fleet02-B20-bt4-r14`, candidate `BT4-R-HEAVY-CROSS-v1`, report blob `1653289d6d3528ee9df6345871d4a447d43bf46b`.

It proves that a remainder vertex heavy on a packed cycle (at least three outgoing fan arcs) forces a genuine packed-to-packed cross into that cycle. Thus the partner's exact-five alternative in long F2 is already `CROSS`, so that branch now routes to `SIX OR CROSS` rather than a separate deficit wall.

For the exact-six branch attacked here I use the assigned partner's earlier proved structural result `BT4-MCR-v4-six-companion-ladder`, fleet01/B04 run `20260922T014146Z-b04-bt4-r12`, report blob `c97354c5427b8b8093795bdd2eea15aa03adecaf`, together with this slot's previously proved `BT4-SIX-DUAL-COLLAR-v1`, report blob `2c05883b0f7629a4a7691130f2925190283e6b11`. No peer outcome label is substituted for its theorem statement.

## Inherited exact-six dual-wall state

Assume BT4 false and use the lexicographically chosen globally minimum packing `(A,B,C)` above, with acyclic remainder

`R = V(D) \ (V(A) union V(B) union V(C))`.

Consider the corrected difficult cycle-supported exact-six state. There is a vertex `z in B` with

`|N+(z) intersect (A union C)| = 6`,
`N+(z) intersect R = empty`.

Because `B` is chordless and `d+(z)=7`, its only residual outgoing edge in `D-(A union C)` is the support edge `p->z` read in the forward direction as `p=z^-` and `z->z+`.

The assigned partner proves that either there is another same-pair five-or-more witness (`H5`), or, in the difficult alternative `C4`, at least two distinct remainder vertices `u_1,u_2` point to `z` and have support-entry domination ladders

`L_i : s_i -> ... -> u_i -> z`,

whose vertices between `s_i` and `z` lie in `R`, every ladder vertex also points directly to `z`, and

`s_i in A union C union {p}`.

This slot's previous dual-collar theorem uses failure of `H5` at the predecessor `p=z^-` to force at least two distinct exits `p->r_j` into `R`. By 3-vertex-strongness each can be extended, avoiding `{p,z}`, to a boundary ray

`P_j : p -> r_j -> ... -> t_j`,

with all internal vertices in `R` and

`t_j in (A union B union C) \ {p,z}`.

Any direct `R`-reachability from an internal vertex of an incoming ladder `L_i` to an internal vertex of an outgoing ray `P_j` can already be switched into a clean support-to-support path. The previously isolated residual was therefore the **dual reachability wall**:

> for every selected pair `(L_i,P_j)`, no vertex on the `R` portion of `L_i` reaches a vertex on the `R` portion of `P_j` by a path wholly inside `R`.

The theorem below shows that this wall cannot remain a terminal object. 3-vertex-strongness forces it to detour through the packing, which itself gives a new cross/bypass interface unless a packed support is short.

## Lemma 1 — clean prefix and suffix after a packed detour

Fix one incoming ladder

`L : s -> ... -> u -> z`

and one outgoing boundary ray

`P : p -> r -> ... -> t`

in the dual-wall state. Then in `D-{p,z}` there is a directed path `W` from `u` to `r`.

Because the dual wall forbids an all-`R` path from `u` to `r`, `W` has an internal packed vertex. Let `a` be the first packed vertex of `W` after `u`, and let `b` be the last packed vertex of `W` before `r`.

Then the concatenations

`J_in : s -> L -> u -> W -> a`,
`J_out: b -> W -> r -> P -> t`

are simple directed paths whose internal vertices all lie in `R`.

### Proof

3-vertex-strongness means `D-{p,z}` is strongly connected, so `W` exists. The dual wall ensures it cannot remain wholly in `R`.

Before `a`, the path `W` has only remainder vertices. If that prefix met an earlier internal remainder vertex `q` of `L`, then `q L u` followed by `u W q` would be a directed cycle wholly inside `R`, contradicting acyclicity. Hence the ladder prefix and `W[u,a]` meet only at `u`, unless `a=s` is the packed endpoint. This proves the first assertion.

The suffix is symmetric. If `W[b,r]` met an internal remainder vertex `q` of the forward ray `P[r,t]`, then `q W r` followed by `r P q` would be a directed cycle in `R`. Hence the concatenation from `b` through `r` to `t` is also simple with only remainder vertices internally. QED.

## Lemma 2 — every nontrivial packed detour is already a source-valid cross or bypass

Let `X` be the packed cycle containing `s` and let `Y` be the packed cycle containing `t`.

For `J_in` exactly one of the following holds.

1. `a` lies on a packed cycle different from `X`: `J_in` is a genuine cross-packed transition.
2. `a in X` and `a != s`: `J_in` is an `R`-internal same-support bypass with distinct packed ports. If `ell_in` is its edge length and `d_X(s,a)` the forward distance on `X`, then global minimum of the three-packing gives

   `ell_in >= d_X(s,a)`.

   Equality is a size-neutral packing exchange; strict inequality is a quantified collar.
3. `a=s`: `L[s,u]` followed by `W[u,s]` is a genuine directed cycle meeting the old packing only at `s`, and therefore

   `|X| <= |R|+1`.

The same trichotomy holds for `J_out`: it is a cross, a distinct-port same-support bypass with the analogous segment tax, or, when `b=t`, it yields

`|Y| <= |R|+1`.

### Proof

Only the numerical assertions need verification. In case 2, replacing the forward support segment `X[s,a]` by `J_in` gives a directed cycle disjoint from the other two old packed cycles. Its order is

`|X| + ell_in - d_X(s,a)`.

A value below `|X|` would strictly reduce the globally minimum packing, so `ell_in>=d_X(s,a)`.

In case 3, Lemma 1 makes `L[s,u] union W[u,s]` a simple directed cycle with one packed vertex `s` and all other vertices in `R`. It therefore has at most `|R|+1` vertices and is disjoint from the other two packed cycles. Replacing `X` by it gives another three-packing, hence global minimum forces `|X|` to be no larger. The `J_out` proof is identical with directions as displayed. QED.

A useful sharpening: if the incoming ladder apex is `s=p=z^-`, then case 3 for `J_in` is impossible because `W` was chosen inside `D-{p,z}`. Thus a predecessor-apex ladder immediately forces a new cross or distinct-port bypass under the wall.

## Theorem — BT4-SIX-DUAL-WALL-LIFT-v1

In the exact-six / zero-`R`-exit `C4` state with its two incoming companion ladders and two outgoing predecessor rays, assume the previously isolated `2 x 2` dual reachability wall. For **every** chosen ladder/ray pair, 3-vertex-strongness forces at least one of the following:

1. a new genuine packed-to-packed cross transition with all internal vertices in `R`;
2. a new distinct-port same-support `R`-bypass carrying the exact minimum-packing tax `ell>=d` (neutral when equality holds, a strict collar otherwise);
3. one of the packed supports incident with the chosen pair has order at most `|R|+1`.

Consequently, in the all-long regime

`|A|, |B|, |C| > |R|+1`,

the dual wall **cannot** persist as a separate exact-six obstruction: each ladder/ray pair necessarily produces a cross or a distinct-port bypass. If a companion ladder has apex `p=z^-`, the same conclusion holds without any long-support assumption on the incoming side.

### Proof

Apply Lemma 1 to a path `W` in `D-{p,z}` and then Lemma 2 to its first and last packed contacts. If neither the prefix nor suffix is a cross or distinct-port bypass, both can fail only through an endpoint-return case, which gives a short support. Under the all-long hypothesis those endpoint-return cases are impossible. QED.

## Why this changes the live SIX frontier

Before this run, the corrected cycle-supported exact-six obstruction had been reduced to:

- a second high witness (`H5`), or
- two incoming companion ladders plus two outgoing predecessor rays, with an explicit four-pair `R`-reachability wall left as a terminal coalescence state.

The wall is now paid in the all-long regime. Its defining absence of an `R`-only route is exactly what makes 3-vertex-strongness useful: after deleting the adjacent support vertices `{p,z}`, any route from an incoming companion to an outgoing ray must leave `R`; the first/last packed contacts are not noise but produce clean cross/bypass interfaces. The only escape from those interfaces is a one-port return cycle, and global packing minimum then forces the relevant support to be short (`<=|R|+1`).

Thus the old `C4 + dual wall` label should no longer be treated as an autonomous all-long branch. It routes to `CROSS/BYPASS` or to an explicit short-support boundary.

## Compact conditional end-to-end route after this run

A full BT4 proof would follow once the remaining explicit interfaces below are closed.

1. Use the inherited exact-seven, oriented, arc-dominated, 3-vertex-strong normal form and the lexicographic globally minimum packing supplied compatibly by fleet01/B04.
2. In long-source four-remainder F2, the partner's maximal-remainder potential gives `SIX` or exact-five; fleet02/B20 sends exact-five to genuine `CROSS`. Hence that branch is `SIX/CROSS`.
3. In the lead's four-remainder heavy-triangle branch, the controlling strengthening gives either its two-port light-inport cover or a double heavy-fan escape cage. Both are genuine port-splice inputs, not missing-cross states.
4. In the corrected cycle-supported exact-six / zero-R-exit branch, fleet01/B04 gives `H5` or `C4`. In `C4`, the prior dual-collar theorem gives the two-in/two-out interface. The present theorem removes the all-long dual-wall residual, routing it to `CROSS/BYPASS`; otherwise a support has order at most `|R|+1`.
5. The remaining target-level obligations are therefore still genuine, but narrower: close the common packed-port splice for the accumulated cross/bypass interfaces; close the `H5` / multiple-high-witness SIX branch; handle the short-support boundary exposed here; and close the remaining larger-remainder / separate SIX configurations not covered by these reductions.

A single cross, a same-support collar, or a short support is **not** counted as four disjoint cycles. No source hypothesis is replaced by a stronger unpaid assumption.

## Failure checks and boundary cases

- The theorem uses 3-vertex-strongness only through the valid deletion of the two distinct vertices `p,z`.
- The dual wall is used exactly to force `W` to hit the old packing. If an all-`R` path exists, the previous switching lemma already applies instead.
- Simplicity of `J_in,J_out` is not assumed: it follows from acyclicity of `R`; an overlap would create a directed remainder cycle.
- The endpoint-return cycles may use many remainder vertices, but never more than `|R|`, hence the exact `|R|+1` support bound.
- The result is arbitrary-order; no finite census is used.
- Digons are allowed in the target statement; the proof works only after the team's inherited valid reduction to an oriented minimum counterexample.
- No nearly-directed cycle from the 2026 relaxation is used.
- No computation was used in this proof, so there is no computational certificate to promote.
- `FULL_PROOF_CANDIDATE` is not claimed. BT4 remains open.

## Honest status

`ESSENTIAL_STEP_APPLIED`.

The first unpaid implication in this exact-six line has moved from an opaque `2 x 2` remainder reachability wall to a source-valid trichotomy: `CROSS/BYPASS`, or an explicit support of size at most `|R|+1`. In the all-long regime the wall is eliminated entirely. The next integrator should splice the resulting port-separated interfaces or attack the short-support/H5 boundaries directly.
