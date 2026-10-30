# BT4 fleet04/B04 — predecessor-cycle and exit-return structural split in G1-S

Run: `fleet04-B04-20260922T031050Z-BT4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-G1-PREDECESSOR-FORK-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Target and exact inherited state

The target is the genuine `k=4` Bermond–Thomassen statement: every finite loopless digraph with at most one arc per ordered vertex pair and minimum outdegree at least seven has four vertex-disjoint directed cycles. Digons are allowed in the target. The August 2026 Bessy–Muis–Sereni–Steiner–Wiederrecht result proves only the one-reversed-arc relaxation and explicitly leaves the genuine conjecture open for `k>=4`.

I use the current campaign normal form only with its stated hypotheses: an oriented exact-outdegree-seven minimum counterexample, a globally minimum-total three-cycle packing `(A,B,C)`, acyclic remainder `R`, chordless packed cycles, 3-vertex-strongness, and universal arc domination. The oriented reduction is valid because a digon can be removed and the genuine `k=3` theorem applied to the remainder.

The controlling lead input is fleet02/B04's correction to its 20260922T022208Z run. It supersedes the invalid marked-bypass bound in the original branch `A not->z`. Its valid heavy-fan domination escape says: if a cycle-supported witness `z` is heavy on packed cycle `A` but receives no arc from `A`, then an `R`-internal cross-packed transition exists. Therefore in a **no-cross** state every cycle-supported heavy witness has at least one heavy-cycle inport.

I also consume:
- fleet04/B04 `BT4-G1-WITNESS-INVARIANT-v1`: in the no-six G1 branch, after the neutral light pivot, either a fixed-pair witness survives in the new remainder (`G1-R`) or all fixed-pair degree-two witnesses lie on the short support cycle (`G1-S`); in `G1-S` there are at least three support five-witnesses and two share one heavy target;
- fleet03/B06 `BT4-G1-PORT-SPACING-v1`: for two same-heavy G1-S witnesses with distinct heavy inports `p1,p2`, global minimum forces the exact corridor alternative `F1 subseteq (p1,p2]_A` or `F2 subseteq (p2,p1]_A`;
- assigned OTHER-account partner fleet01/B05 `BT4-TCEX-v1`: if `p->z` is a heavy-cycle inport and there is an `R`-internal bypass from `z^-` to `z^+` of length `ell`, then the heavy fan size `m` satisfies `m<=ell`; equality is a neutral two-cycle exchange with an inversion prohibition in the exchanged remainder. I also read the partner's newer `BT4-RCC-v1`, which handles a different all-long collision funnel and does not replace the G1-S obligation below.

No peer outcome label is used as proof.

## Compact conditional end-to-end route

The corrected lead state reduces a full proof to three universal closures:

1. `H6`: close the exact-six / six-or-more cross-fan branch.
2. `HX`: turn every genuine cross-packed transition or two-path linkage output into a legal two-cycle splice, strict packing reduction, or fourth cycle.
3. `HS`: exclude a persistent no-six neutral orbit in which remainder-supported witnesses have only strict pure-R collars and support witnesses have only strict marked bypasses/linkages.

`G1-S` is part of `HS`. The first missing local-to-global implication is to turn its same-heavy support witnesses into a sufficiently rigid object that cannot hide behind arbitrary coalescence. The lemmas below supply a new exact structural split.

## Lemma 1 — predecessor-cycle lemma

Work in a no-cross `G1-S` state. Let `z in B` be a cycle-supported five-witness for the deleted pair `{A,C}`, heavy on `A`. Put

`F = N+(z) intersect A`, `m=|F|>=3`,
`P = N-(z) intersect A`,
`R_z = N-(z) intersect R`.

Then:

1. `P` is nonempty;
2. there is a directed cycle `Q_z` contained in `P union R_z`, disjoint from `B union C`;
3. `|Q_z| >= |A|`;
4. consequently `|Q_z intersect R| >= m`, and in particular
   `|N-(z) intersect R| >= m`.

### Proof

Nonemptiness of `P` is exactly the controlling lead correction in the no-cross branch.

Fix `p in P`. Dominate the arc `p->z`, obtaining `q0->p,z`.

- If `q0 in A`, then `q0 in P` and we already have a directed `P`-to-`P` path `q0->p`.
- If `q0 in B union C`, then `q0->p` is a cross-packed transition into `A`, contrary to no-cross.
- If `q0 in R`, repeatedly dominate the arc `qi->z`, obtaining
  `q(i+1)->qi,z` as long as `qi in R`.

A remainder vertex cannot repeat, because the backwards domination chain would then contain a directed cycle in `D[R]`. Finiteness therefore gives a first terminal vertex outside `R`. A terminal in `B union C` again gives a cross-packed transition to `A`; hence in the no-cross branch the terminal lies in `A`, and because it points to `z` it belongs to `P`.

Thus for every `p in P` there exists some `p' in P` and a directed path
`p' -> R_z -> ... -> R_z -> p`
whose internal vertices, if any, are all in `R_z`.

Choose one such predecessor path for every `p`. The resulting finite directed relation on `P` has indegree at least one at every vertex, so it contains a directed relation-cycle. Expanding its relation edges gives a closed directed walk inside `P union R_z`. Extract a directed cycle `Q_z`. It cannot lie entirely in `R`, since `R` is acyclic, hence it is a genuine replacement for `A`; it is disjoint from `B,C`.

Therefore `(Q_z,B,C)` is a three-cycle packing. Global minimum of `(A,B,C)` gives
`|Q_z| >= |A|`.

Because the counterexample is oriented, no vertex of `A` can be both an inport and an outfan target of `z`: `P intersect F` is empty. Hence
`|P| <= |A|-m`.
All `A`-vertices of `Q_z` lie in `P`, so
`|Q_z intersect R| = |Q_z|-|Q_z intersect A|`
`>= |A|-|P| >= m`.
Every remainder vertex used by the domination construction points to `z`, so `Q_z intersect R subseteq R_z`. QED.

### Significance

A heavy support witness does not merely have one heavy inport. In the no-cross branch it has at least `m>=3` distinct remainder predecessors, and those predecessors participate with heavy inports in an alternative directed cycle at least as long as the heavy packed cycle.

## Lemma 2 — same-heavy predecessor-fork

Let `z1,z2 in B` be two G1-S five-witnesses heavy on the same packed cycle `A`. For `i=1,2` write
`Fi=N+(zi) intersect A`, `mi=|Fi|>=3`,
`Pi=N-(zi) intersect A`,
`Ri=N-(zi) intersect R`,
and let `Qi subseteq Pi union Ri` be cycles from Lemma 1.

Then `Q1` and `Q2` intersect. Consequently:

- if `P1 intersect P2` is nonempty, the witnesses have a common heavy-cycle inport;
- if `P1 intersect P2` is empty, they have a common remainder predecessor
  `r in R` with `r->z1,z2`.

Moreover, in the second branch this `r` has residual outdegree at least three in
`Gamma = D-(A union C)`.

### Proof

If `Q1,Q2` were vertex-disjoint, then `Q1,Q2,B,C` would be four vertex-disjoint directed cycles, impossible in the counterexample. Thus they intersect. Since `Qi subseteq Pi union Ri`, disjointness of `P1,P2` forces any common vertex into `R1 intersect R2`, giving `r->z1,z2`.

In G1-S the entire fixed-pair degree-two witness set for `Gamma` lies on the support cycle `B`; no remainder vertex has residual outdegree exactly two. The no-six hypothesis excludes residual outdegree at most one. Therefore a common remainder predecessor has
`d_Gamma^+(r)>=3`.
It already uses two residual arcs on `z1,z2`, so it has at least one additional residual outarc into `B union R`. QED.

### Port-axis sharpening

There is a complementary exact split using fleet03/B06's port-spacing theorem.

- If every choice `p1 in P1`, `p2 in P2` has `p1=p2`, then necessarily
  `P1=P2={p}`: a **singleton heavy-inport lock**.
- Otherwise choose distinct `p1,p2`. Then the verified port-spacing result gives
  `F1 subseteq (p1,p2]_A` or `F2 subseteq (p2,p1]_A`,
  hence one directed port gap has length at least the corresponding heavy fan size.

Thus a persistent same-heavy pair has either an exact singleton-inport lock or a genuine heavy-cycle fan corridor. If the inport sets are disjoint, that corridor coexists with the residual-rich common-R fork above.

## Lemma 3 — exit-return collar

Keep one G1-S witness `z in B`, with heavy fan size `m`, and let `e in R` be its unique remainder outneighbor. Let `Q_z` be the predecessor cycle from Lemma 1 and put
`S_z = Q_z intersect R`.
Then `|S_z|>=m` and every `q in S_z` satisfies `q->z`.

Exactly one of the following holds:

- **separation:** `e` reaches no vertex of `S_z` in `R`; or
- **return:** for some `q in S_z` there is an `R`-path from `e` to `q`. If the shortest such path has `d` edges, then
  `d >= |B|-2`.

At equality `d=|B|-2`, replacing `B` by
`T = z -> e -> ... -> q -> z`
is a size-neutral globally minimum exchange. Its new remainder
`R* = (R - V(e...q)) union (B-{z})`
is acyclic, and therefore contains no directed path from `z^-` to `z^+`; otherwise that path together with the surviving directed path `z^+ -> ... -> z^-` in `B-{z}` would be a fourth disjoint cycle. If equality is excluded, integrality gives `d>=|B|-1`.

### Proof

The split is tautological once `S_z` is fixed. In the return case choose a shortest `R`-path from `e` to `q`. The cycle `T` is disjoint from `A,C`. Therefore `(A,T,C)` is a three-cycle packing, and global minimum gives
`|T|=d+2 >= |B|`.
The equality and acyclicity statements follow by exact vertex accounting and the no-four-cycle assumption. QED.

This is an **outgoing** collar complementary to fleet01/B05's TCEX predecessor-to-successor collar. It uses the same global-minimum principle but a different cycle replacement.

## Lemma 4 — orthogonal-collar intersection

Assume the hypotheses of Lemma 3, and also suppose the assigned partner's TCEX hypotheses hold for `z`: there is an `A`-inport and an `R`-internal bypass
`U: z^- -> ... -> z^+`.

If an exit-return path
`V: e -> ... -> q`
with `q->z` exists as in Lemma 3, then the internal remainder vertices used by the TCEX repair and by `V` must intersect.

### Proof

The TCEX bypass repairs `B` into a directed cycle avoiding `z`. The exit-return path produces the directed cycle `T` containing `z` and otherwise only remainder vertices. If their remainder interiors were disjoint, those two cycles together with untouched `A` and `C` would be four vertex-disjoint directed cycles. QED.

So the global coalescence problem is no longer completely unstructured: whenever both collars occur, their coalescence is forced by the absence of a fourth cycle.

## Updated structural tree for G1-S

In persistent `NO-SIX`, no-cross `G1-S`, choose the guaranteed two same-heavy support witnesses.

For each witness:
- Lemma 1 supplies an alternative heavy replacement cycle and at least `m>=3` remainder predecessors.
- Lemma 3 gives either an `m`-vertex predecessor set separated from the unique remainder exit, or a long/neutral exit-return collar of length at least `|B|-2`.

For the same-heavy pair:
- either all heavy inports collapse to the same singleton;
- or there is a distinct-port fan corridor as in fleet03/B06;
- if the two inport sets are disjoint, there is additionally a residual-rich common remainder predecessor with residual outdegree at least three.
- whenever a partner TCEX bypass and an exit-return collar coexist, their R-parts must intersect.

Therefore the live G1-S obstruction is now localized to one of two geometric places: a locked heavy-cycle port/corridor, or an explicit R-fork/coalescence set. It cannot remain an arbitrary collection of unrelated support witnesses.

## Remaining first implication

This run does **not** prove BT4. The next exact implication is:

> `BT4-G1-FORK-CLOSURE-v1`: in the no-six, no-cross G1-S state, use either the singleton-heavy-inport lock or the distinct-port corridor together with the residual-rich common-R predecessor / forced orthogonal-collar intersection to produce one of: an HX two-cycle splice, an H6 six-fan, a strictly smaller three-cycle packing, a neutral exchange with a forbidden inversion, or a fourth directed cycle.

The separate exact-six branch remains unpaid. The general HX and HS closures also remain unpaid outside this sharpened G1-S configuration.

## Adversarial checks and failure boundaries

- The controlling lead correction, not the superseded invalid TCEX invocation, is used.
- A common remainder predecessor is claimed only when the two heavy-inport sets are disjoint. If they overlap, the correct branch is common-A-inport; no stronger conclusion is inferred.
- The residual-rich conclusion does not call the common R predecessor a five-witness. In fact G1-S forces its fixed-pair residual outdegree to be at least three.
- No claim is made that a long collar is itself contradictory.
- Lemma 3 uses a shortest path entirely in the actual old remainder; paths through packed vertices are not substituted.
- Lemma 4 is conditional on an actual support-correct TCEX bypass. It does not assert such a bypass always exists.
- The fleet03/B06 finite sharpness certificate is compatible with this result: it demonstrates why local witness counting is insufficient, not a target counterexample.
- No computation was required for the new lemmas.
- No relaxed/near-directed cycle is counted as genuine, and no target-level proof or novelty claim is made.

## Exact peer/source references consumed

- fleet02/B04 lead correction: shared handoff
  Git blob `efc49c4d0177e30caf791b471ff9a9becb2c060b`;
  canonical correction blob `117d9760b66cfb5930c79ade79d2b449ce329b9b`.
- fleet04/B04 `BT4-G1-WITNESS-INVARIANT-v1`, shared blob
  `f5533fe5b8ff8dd76fe701124f4bfd74370f2c8d`.
- fleet03/B06 `BT4-G1-PORT-SPACING-v1`, shared blob
  `2c82f2baa29017affdc5e8684af25830d9c49a00`.
- assigned OTHER-account partner fleet01/B05 `BT4-TCEX-v1`, shared blob
  `957d34c32886177662a52ac2ed5aa393a276a288`, canonical report blob
  `f61ce94c50464f2d59491377df32f7e549db7242`.
- partner fleet01/B05 `BT4-RCC-v1`, shared blob
  `3deb56019df0fa573e1f73e661f8efa48a098e35`.

## Status

`ESSENTIAL_STEP_APPLIED`.

The structural case split is strictly sharper than the prior G1-S state, but the target remains open.
