# BT4 proof attempt — fleet01/B05

Run: `20260922T062559Z-b05-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Source state actually consumed

Fresh owner control was read at commit `b13194a9dccab6e2420071c4fdd27d0fc33f3a3a` before research. The named OTHER-account result applied here is fleet04/B04 `BT4-R4-F3-RETURN-CUT-v1`, handoff `BT4-HANDOFF-fleet04-B04-20260922T060947Z.md`. It consumes fleet03/B06 `BT4-R4-F3-MAJORITY-CROSS-v1` and proves, in the canonical triangular F3 BOTH-repeat branch, a return cycle `C` of order 3 or 4 through the light ports and a saturation triangle `T_c=q->c->x->q`, disjoint from the heavy packed cycle `H`, with exact complementary induced graph

`R' = (U - {u}) union {s}`.

If `D[R']` is cyclic then `H,C,T_c` plus that residual cycle are already four vertex-disjoint directed cycles. Thus the only live case below is that `D[R']` is acyclic. The source handoff also gives the one-cut order on the broken `U-u` path, but the first theorem below needs only the exact residual identity and acyclicity.

The surrounding canonical candidate is the exact-outdegree-seven oriented reduction with a globally minimum three-cycle packing and old remainder of order four. All claims below are conditional on those shared candidate hypotheses.

## New result: BT4-F3-RETURN-RESTART-v1

### Lemma 1 — the return construction forces `|U| <= 4`

Let the old globally minimum three-cycle packing have complement `R` of order four. Hence its total covered order is `|V(D)|-4`.

The fleet04/B04 return construction gives the three disjoint cycles `H,C,T_c` with exact complement

`R'=(U-{u}) union {s}`.

Therefore `|R'|=|U|`, and the new three-cycle packing covers `|V(D)|-|U|` vertices. Global minimality of the old packing gives

`|V(D)|-4 <= |V(D)|-|U|`,

so

`|U| <= 4`.

Since `U` is a genuine directed cycle in the current oriented normal form, `|U|` is 3 or 4.

This is a useful collapse not present in the source handoff: the F3 BOTH-repeat return cycle cannot leave an arbitrarily long broken light cycle. It leaves at most four residual vertices.

### Lemma 2 — canonical residual sink and exact `(3,2,2)` regeneration

Write

`U = u -> v1 -> v2 -> ... -> vm -> u`,

so `R'={v1,...,vm,s}` and `m=|U|-1`.

Because `D[R']` is finite and acyclic it has a sink `t`. Every `v_i` with `i<m` has the residual support edge `v_i->v_{i+1}`, so no such vertex can be a sink. Hence

`t in {v_m,s}`.

In the exact-outdegree-seven normal form, `t` has no outneighbor in `R'`, so all seven outneighbors of `t` lie on the three packed cycles `H,C,T_c`. Put

`h=|N+(t) intersect H|`, `c=|N+(t) intersect C|`, `q=|N+(t) intersect T_c|`.

Then

`h+c+q=7`.

If some pair sum is at least six, the branch is exactly a current `SIX` output and should be handed to the campaign's SIX closure machinery. Otherwise

`h+c <= 5`, `h+q <= 5`, `c+q <= 5`.

Subtracting each pair bound from `h+c+q=7` gives `h,c,q >=2`. Therefore the multiset of fan counts is forced to be

`{h,c,q}={3,2,2}`.

Thus every acyclic F3 BOTH-repeat return state has the sharp alternative

`SIX` or a zero-remainder-exit `(3,2,2)` witness at a canonical residual sink `t in {v_m,s}`.

This converts the one-cut residual geometry back into the standard witness language.

### Lemma 3 — if `|U|=4`, the branch restarts at a globally minimum exact-R4 state

When `|U|=4`, Lemma 1 gives `|R'|=4`. The new packing `H,C,T_c` therefore covers exactly `|V(D)|-4` vertices, the same number as the old globally minimum packing. Hence `H,C,T_c` is itself globally minimum.

Consequently, unless `SIX` already occurs, the sink `t` from Lemma 2 is an exact zero-remainder-exit `(3,2,2)` witness for a new globally minimum three-cycle packing with acyclic remainder of order four. All standard pair-deletion, domination, exchange, and arc-maximality machinery may be restarted on this new state without changing the extremal objective.

Vertex accounting is exact: the old packed triple is discarded; the new packed vertices are exactly `V(H) union V(C) union V(T_c)`; the uncovered set is exactly `(U-{u}) union {s}`, of order four.

### Lemma 4 — the `|U|=3` short-heavy return either gives no-return or a neutral restart to exact R4

Now suppose `|U|=3`. Then `|R'|=3`. Assume the non-SIX fan profile `(3,2,2)` from Lemma 2, and suppose its three-entry falls on one of the short cycles `Z in {C,T_c}`.

The saturation cycle `T_c` has order three. The return cycle `C` has order three or four.

If `|Z|=3`, then `Z` cannot send an arc to `t`: if `b->t` for some `b in Z`, orientedness forbids `t->b`, so `t` can hit at most the other two vertices of `Z`, contradicting `|N+(t) intersect Z|=3`. Thus `Z ->/ t`.

The only remaining short-heavy possibility with a return is `Z=C` and `|C|=4`. Suppose `b->t` for some `b in C`. Since the normal form is oriented and `t` has exactly three outneighbors on the four-cycle `C`, it must hit every vertex of `C-{b}`, in particular the predecessor `b^-` of `b` on `C`. Therefore

`K = b -> t -> b^- -> b`

is a genuine directed triangle.

Replace the packed four-cycle `C` by `K`, leaving `H` and `T_c` untouched. This is a legal three-cycle packing because `t` was in the old complement and `K` uses only `t,b,b^-` from `R' union V(C)`. Its exact new complement is

`R'' = (R' - {t}) union (V(C)-{b,b^-})`.

Hence `|R''|=2+2=4`. The replacement reduces the new return packing by exactly one covered vertex, from `|V(D)|-3` to `|V(D)|-4`. Since the original packing already proved that `|V(D)|-4` is the global minimum possible covered order, the packing `H,K,T_c` is globally minimum.

If `D[R'']` is cyclic, that residual cycle together with `H,K,T_c` gives four disjoint directed cycles. Otherwise we have again reached an acyclic globally minimum exact-R4 state.

Thus for `|U|=3`, whenever the regenerated three-fan lands on a short packed cycle, one obtains either:

1. a genuine no-return condition from that short heavy cycle to `t`; or
2. an explicit size-neutral-to-the-global-objective packing exchange returning the branch to an exact-R4 globally minimum state; or
3. immediately four disjoint cycles if the exchanged four-vertex complement is cyclic.

Every affected vertex is accounted for in the displayed formula for `R''`.

## Conditional end-to-end route for F3 BOTH

Starting from fleet04/B04 `BT4-R4-F3-RETURN-CUT-v1`:

1. If the exact complement `(U-{u}) union {s}` is cyclic, BT4 closes immediately in this branch.
2. Otherwise Lemma 1 forces `|U| in {3,4}`.
3. Lemma 2 selects a canonical residual sink and forces `SIX` or `(3,2,2)`.
4. If `|U|=4`, Lemma 3 returns immediately to a globally minimum exact-R4 `(3,2,2)` state (or SIX).
5. If `|U|=3` and the three-fan is on `C` or `T_c`, Lemma 4 gives no-return or a concrete exact-R4 restart (or four cycles).
6. The first genuinely unpaid local implication is therefore the `|U|=3` non-SIX case in which the regenerated three-fan lies on the potentially long heavy cycle `H`, together with the no-return short-heavy subcase after Lemma 4. This is much smaller than the original arbitrary one-cut residual problem.

## Honest status / next mechanism

Outcome: `ESSENTIAL_STEP_APPLIED`; BT4 remains `OPEN_NOT_PROVED`.

The next B05 target should be `BT4-F3-R3-HEAVY-SPLICE-v1`: in the residual-three state, exploit that the canonical sink has fan profile `(3,2,2)` and only two other residual vertices. Either a return from the heavy cycle plus one of those two residual vertices yields a legal two-cycle exchange back to exact R4, or the resulting no-return constraints should force a pair-six/cross interface. No claim of that implication is made here.

No benchmark gold, protected controls, credentials, scheduler identifiers, machine paths, email, Drive, public posting, paid compute, remote workflows, or permission changes were used.