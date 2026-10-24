# BT4 proof attempt — account01/B05

Run: `20260922T080526Z-b05-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Fresh source state consumed

This run read the fresh owner controls and collective ORDER/TARGETS/ASSIGNMENTS at initial main `3f1d96c637b5e444261e0396a02e830c5c6a269a`, owner-control revision `2026-09-22.2`. The active instruction remains collective BT4 research; old brain-installation and benchmark work remains stopped.

The current campaign-lead dependency actually used is account02/B04 `BT4-HANDOFF-account02-B04-20260922T0619Z.md`, Git blob `b0c1c37b1d36fd7cf855946f20eb382a61cd346d`. It preserves the exact-seven oriented, arc-dominated, globally minimum three-cycle-packing framework and warns that CROSS/BYPASS existence alone is not a fourth cycle.

The named OTHER-account partner result actually consumed and applied is account02/B06 `BT4-RANK2-PORT-PARITY-v1`, from `proofnet24/collective-BT4/account02/B06/b06-20260922T072919Z-b772b1c849cf/report.md`, Git blob `0e2262187f4ba70675c24940d913532224bc88c1`. B06 proves that even very strong local rank-two connector data do not auto-splice: on each support the four ports can be `ID`, `SW`, or `BLOCK`, and a canonical two-splice exists only for matching non-`BLOCK` parity. Its explicit oriented minimum-outdegree-seven adversary shows that local strong connectivity, domination, chordless designated supports, distinct ports, and disjoint connector interiors still do not force compatibility. I therefore do not use a connector-existence shortcut below; the new step is a packing-changing exchange forced by the global minimum objective.

The immediate B05 predecessor used is `BT4-F3-RETURN-RESTART-v1` (report blob `3168133fc59a3f9b5740f54d397e7a4962f15f47`). It reduced the canonical F3 BOTH-return branch to the following live state, conditional on the shared candidate hypotheses:

- a globally minimum old three-cycle packing covers `n-4` vertices;
- a legal return packing `(H,C,T_c)` covers `n-3` vertices and has acyclic remainder `R'` of order three;
- `T_c` is a directed triangle and `C` has order three or four;
- a canonical sink `t` of `D[R']` has no outneighbor in `R'`;
- outside the already-separated SIX branch, the fan profile of `t` on `(H,C,T_c)` is a permutation of `(3,2,2)`;
- the live case is the one where the three-fan lies on the potentially long heavy cycle `H`.

## New mechanism: defect-one return compression

The key point is that the return packing is exactly one covered vertex above the global three-packing minimum. That one-unit defect gives a sharper exchange tax than the earlier generic bypass arguments.

### Lemma 1 — defect-one return collar

Let `P=(Z1,Z2,Z3)` be any three disjoint directed cycles covering `n-3` vertices in the current digraph, while some globally minimum three-cycle packing covers `n-4` vertices. Let `t` be an uncovered vertex. Fix a packed directed cycle `Z` and suppose `b in Z` satisfies `b->t`.

For every `a in N+(t) intersect Z`, let `d=d_Z(b,a)` be the forward directed distance from `b` to `a` on `Z`. Then

`d <= 3`.

Proof. The directed cycle

`L(a) = b -> t -> a -> Z[a,b]`

is genuine: `t` is outside the packing, `a!=b` by orientedness from `b->t`, and `Z[a,b]` is the forward support segment from `a` back to `b`. If `z=|Z|`, then `Z[a,b]` contains `z-d+1` vertices, so

`|L(a)| = z-d+2`.

Replacing `Z` by `L(a)` and leaving the other two packed cycles untouched gives a three-cycle packing covering

`(n-3)-z+(z-d+2)=n-d-1`

vertices. Since the global minimum is `n-4`, necessarily

`n-d-1 >= n-4`,

hence `d<=3`. Every affected vertex is explicit: `t` enters the packed cycle, the vertices strictly between `b` and `a` on the forward `b->a` segment leave it, every other vertex of `Z` remains packed, and the other two cycles are untouched. QED.

This lemma needs neither connector parity nor an assumption that the defect-one packing itself is globally minimum.

### Lemma 2 — heavy return forces an exact-R4 restart

Apply Lemma 1 to the F3 residual-three state, where

`|N+(t) intersect H|=3`.

If any `b in H` satisfies `b->t`, then all three distinct heavy targets lie among

`{b+, b++, b+3}`.

Orientedness excludes `b` itself, so the three targets are exactly

`N+(t) intersect H = {b+,b++,b+3}`.

Take `a=b+3`. The replacement cycle

`L_H = b -> t -> b+3 -> H[b+3,b]`

has order `|H|-1`. Replacing `H` by `L_H` changes the defect-one packing from `n-3` covered vertices to exactly `n-4`, hence the new packing is globally minimum. Its exact uncovered set is

`R'' = (R' - {t}) union {b+,b++}`,

so `|R''|=4`.

If `D[R'']` is cyclic, that residual cycle together with `L_H,C,T_c` gives four vertex-disjoint directed cycles immediately. If `D[R'']` is acyclic, the branch has returned to a globally minimum exact-R4 state and the campaign's exact-R4 machinery restarts legitimately.

Therefore, in the genuinely surviving residual-three heavy branch with no immediate fourth cycle and no exact-R4 restart,

`H ->/ t`.

This is the first essential missing implication from the preceding B05 run, now proved.

### Lemma 3 — every light return is either an exact-R4 restart or a unique tight pivot

Let `Z` be one of the two light cycles, so `|N+(t) intersect Z|=2`, and suppose `b->t` with `b in Z`.

Lemma 1 puts both fan targets among the first three successors of `b` on `Z`.

- If `b+3` is a target, choose `a=b+3` in Lemma 1. Exactly as above, replacing `Z` by `L(a)` drops the defect-one packing from `n-3` to `n-4`, producing a globally minimum exact-R4 packing (or four cycles if its four-vertex remainder is cyclic).
- Otherwise the two distinct targets must be exactly `{b+,b++}`. Then

  `L_Z = b -> t -> b++ -> Z[b++,b]`

  has the same order as `Z`. The resulting three-cycle packing still covers `n-3` vertices, and its exact remainder is

  `(R' - {t}) union {b+}`.

  This is a genuine size-preserving defect-one pivot: `t` enters `Z`, `b+` leaves `Z`, all other vertices of `Z` remain packed, and the other two packed cycles are untouched.

Moreover, in the branch excluding an exact-R4 restart, a fixed light cycle has at most one return vertex into `t`. Indeed the fixed two-target set must equal `{b+,b++}`; that ordered consecutive pair has a unique predecessor `b` on the directed support. Thus the surviving packed in-neighborhood of `t` contains at most one vertex from each light support and none from `H`.

### Lemma 4 — 3-vertex-strongness forces a tight pivot in every surviving no-restart state

The shared normal form is 3-vertex-strong, so every vertex has indegree at least three. In the no-restart state of Lemmas 2–3:

- `H` contributes zero in-neighbors of `t`;
- `C` contributes at most one;
- `T_c` contributes at most one;
- the three-vertex remainder `R'` contributes at most its other two vertices.

Hence

`3 <= d-(t) <= 4`.

In particular at least one light support must return into `t`: if neither did, `t` would have at most two in-neighbors, both from `R'-{t}`, contradicting 3-vertex-strongness. By Lemma 3 that light return is necessarily a tight pivot unless it already yields the exact-R4 restart.

More precisely, if `d^-_{R'}(t)=1`, then both light supports must have their unique return ports and `d-(t)=3`; if `d^-_{R'}(t)=2`, at least one light support has its unique return port and `d-(t)` is three or four.

Thus the old `BT4-F3-R3-HEAVY-SPLICE` leaf cannot remain static. After excluding SIX, a cyclic exchanged remainder, and the heavy-return exact-R4 compression, it always has a concrete legal light-cycle pivot.

### Corollary 5 — the surviving branch is a finite defect-one pivot dynamics, not a free connector problem

Perform any forced tight pivot from Lemma 4. If the new three-vertex remainder is cyclic, its directed cycle plus the new three-cycle packing gives four disjoint cycles. Otherwise choose a sink in the new acyclic three-vertex remainder. Exact outdegree seven again gives either SIX or a `(3,2,2)` fan profile. Lemma 1 applies again because the packing still covers `n-3` while the fixed global minimum remains `n-4`.

Consequently every live state in this defect-one class has the alternative

1. SIX;
2. cyclic three-vertex remainder, hence four cycles;
3. a distance-three return compression to a globally minimum exact-R4 state; or
4. another size-preserving tight pivot.

There are finitely many three-cycle packings on a finite digraph, so if none of the first three outputs occurs, repeated legal pivots eventually enter a finite pivot orbit. This is an exact reduction, not yet a contradiction.

When the pivoted light support is a directed triangle, the immediate inverse swap through the same inserted vertex is impossible by orientation: the released successor has its original arc to the next support vertex, but a second arc needed to hit the other successor of the inserted return port would reverse an existing triangle arc. No analogous no-backtracking claim is made for the four-cycle return support without an additional chordlessness premise.

## Application of account02/B06 `BT4-RANK2-PORT-PARITY-v1`

The forced pivot dynamics can generate new cross/support connectors through arc domination, but B06's exact adversary rules out the tempting step “two connectors each way automatically splice.” Any later two-support rank-two splice must explicitly verify that both support port orders are non-`BLOCK` and have matching `ID/SW` parity, or else use a packing-changing pivot/exchange to alter the state. The present lemmas do the latter: they use the global minimum objective to force an adjacent support exchange even when local connector compatibility is absent.

Accordingly the first unpaid implication is now

`BT4-F3-R3-PIVOT-ORBIT-CLOSE-v1`:

> In a genuine no-four-pack counterexample, prove that the finite defect-one pivot dynamics above cannot cycle forever without producing SIX, a cyclic residual, a distance-three compression to exact R4, a globally improving three-packing, or a rank-two interface whose two support orders satisfy the B06 matching non-BLOCK parity criterion.

The B06 adversary shows that the last alternative cannot be obtained from local linkage strength alone; the proof must exploit the global no-four-pack/minimum-packing constraints or a monotone quantity along the pivot orbit.

## Compact conditional end-to-end route

Within the canonical F3 BOTH branch:

1. account04/B04's return construction gives `(H,C,T_c)` and exact residual `(U-{u}) union {s}`; a cyclic residual already gives four cycles;
2. `BT4-F3-RETURN-RESTART-v1` forces `|U| in {3,4}` and reduces `|U|=4` to exact R4;
3. in `|U|=3`, a sink `t` gives SIX or `(3,2,2)`; short-heavy returns were already reduced;
4. the new defect-one collar proves that a return from the heavy three-fan support gives an exact-R4 globally minimum packing, so the only live heavy case has `H ->/ t`;
5. 3-vertex-strongness then forces a light return; every such return is either another exact-R4 compression or a legal tight pivot;
6. iteration therefore reduces the previously open local branch to the finite pivot-orbit closure problem above, with B06's port-parity theorem supplying the exact acceptance condition for any rank-two connector closure encountered along that orbit.

## Honest status

Outcome: `ESSENTIAL_STEP_APPLIED`. BT4 remains `OPEN_NOT_PROVED`.

This run proves the heavy-return compression and the forced-light-pivot recurrence, but does not prove that every resulting finite pivot orbit closes. No fourth cycle is claimed merely from CROSS/BYPASS or rank-two connector existence. No benchmark gold, protected controls, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive, public posting, paid compute, remote workflows, or permission changes were used.
