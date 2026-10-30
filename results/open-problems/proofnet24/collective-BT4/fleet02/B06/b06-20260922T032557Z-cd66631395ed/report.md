# BT4 fleet02/B06 — SIX-support bypass tax with exact inport obstruction

Run: `b06-20260922T032557Z-cd66631395ed`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Candidate: `BT4-SIX-SUPPORT-MENGER-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED` with local `CANDIDATE_REFUTED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`  
Model self-report: `GPT-5.6 Sol`; requested effort `maximum actually supported`; configured effort `UNKNOWN_NOT_EXPOSED`; known/self-observed effort `UNKNOWN`; provider reasoning/thinking/total counters `null / NOT_EXPOSED`.

## Exact target and source boundary

Target: every finite loopless digraph with at most one arc per ordered pair and minimum outdegree at least seven contains four vertex-disjoint genuinely directed cycles. Opposite arcs and therefore digons are allowed.

Current literature check: Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (13 August 2026), explicitly states that the exact conjecture remains unresolved for every `k>=4`; its theorem allows each packed cycle either to be directed or to become directed after reversing one arc. No relaxed cycle is promoted here.

Latest complete campaign-lead state actually consumed:
- fleet02/B04 run `20260922T022208Z-b04-bt4-r11`;
- canonical science commit `99c1f5c0ddb596d7bd3b1910bb59be58d94f30cc`;
- controlling same-run correction commit `fa3038109977a1f4490d4efd616e7ae8acc45bf8`, correction blob `b32e4df1b401aec955dcc7bb949739b3d0bd532e`;
- shared correction handoff commit `d25d993e360d2b9624de75d56a1eb8afa08cba42`.

The controlling lead input used below is the heavy-fan domination escape: for a vertex on one packed cycle that sends at least three arcs to a target packed cycle `A`, if `A` has no arc into that vertex, universal arc domination plus acyclicity of the remainder produces a genuine cross-packed transition. The proof uses orientation, chordlessness, domination and remainder acyclicity, not the five-witness-specific unique-exit property, so it applies verbatim to the SIX-support vertex treated here.

Named OTHER-account partner actually consumed and applied:
- fleet03/B04 run `20260922T025224Z-fleet03-B04-BT4-r11`;
- candidate `BT4-R4-MENGER-SAT-v1`;
- science commit `3d662c678d5462df72278ef623cb4f8bf7d89afa`, report blob `4d55c10525881316530d09f1fab72ef6e6cd1c92`;
- shared handoff commit `f49521f1cf607e17b8fd56fc8a0b42bcffbd9ca2`.

The partner's mechanism used essentially is the two-path Menger saturation template: in the 3-vertex-strong normal form, two internally disjoint bypass paths around a packed vertex cannot both consume too little remainder once each extracted pure-remainder collar has an exact minimum-packing length tax. I extend that template below from cycle-supported five-witnesses to cycle-supported SIX witnesses.

## Inherited normal form and compact conditional route

Assume BT4 false. The lead's inherited reductions allow work in an oriented exact-outdegree-seven counterexample `D` with a globally minimum-total packing `(A,B,C)` of three directed cycles, nonempty acyclic remainder `R`, chordless packed cycles, every arc dominated, and 3-vertex-strongness. Pair deletion then produces either a SIX witness (residual outdegree at most one) or at least three five-witnesses (residual outdegree exactly two).

A complete proof would follow if the remaining outputs of these deficit objects could always be closed into a legal two-cycle replacement, a strict reduction of the minimum three-packing, or a fourth cycle in the exchanged remainder. The first missing implication attacked here is the cycle-supported SIX branch: can a SIX vertex support arbitrarily short pure-remainder bypasses, or does minimum packing force a usable length tax?

## False intermediate statement and exact adversary

The tempting unguarded statement is false:

> If `u` is a cycle-supported SIX witness, heavy with fan `m>=3` on a packed target `A`, then every pure-`R` bypass of the singleton segment through `u` has length at least `m`.

An exact 16-vertex adversary is encoded in `checker.py`. It is oriented, every vertex has outdegree exactly seven, every arc is dominated, deletion of any at most two vertices leaves a strongly connected digraph, the packed directed triangles

`A=(0,1,2), B=(3,4,5), C=(6,7,8)`

have total size nine and hence are globally minimum among all three-cycle packings in an oriented graph, and the seven-vertex complement `R={9,...,15}` is acyclic.

For `u=6`, deleting `A union B` leaves exactly the support successor `7`; hence `u` is a genuine cycle-supported SIX witness with no remainder exit. Its fan split is `(3,3)`. Nevertheless there are two internally disjoint pure-remainder bypasses

`8 -> 11 -> 7`,  `8 -> 13 -> 7`,

both of length two, so the naive tax `ell>=m=3` fails. The reason is exact: no vertex of either heavy target triangle sends an arc into `u`. This graph is not a BT4 counterexample; it contains the explicit four disjoint directed triangles/cycles

`(0,1,2), (3,4,5), (6,7,10), (8,9,12)`.

Thus the missing hypothesis is not cosmetic: the heavy-target inport, or the cross-packed transition forced when it is absent, is essential.

## Repair — exact SIX marked-segment tax

Let `u in C` be a cycle-supported SIX witness for the deleted pair `A union B`. Since `C` is chordless and `u+` survives the deletion, residual outdegree at most one means residual outdegree is exactly one: the only surviving outarc is `u->u+`. Hence `u` sends exactly six arcs into `A union B` and none into `R`.

Choose a heavy target `A` and write

`F = N+(u) intersect A`, `m=|F|>=3`.

If `A` has no arc into `u`, the lead's corrected domination escape already gives a genuine cross-packed transition. Therefore in the no-cross branch choose an inport

`b -> u`, `b in A`.

Orientation implies `u` does not send to `b`, so `b notin F`.

Now let `Q` be a directed path from `p in C` to `q in C`, with all internal vertices in `R`, replacing the forward `C`-segment from `p` to `q` whose internal vertices include `u`. Let that packed segment have `t>=2` edges, so it has `t-1` internal vertices, and let `ell` be the length of `Q` in edges.

For every `a in F`, form the directed cycle

`K_a = b -> u -> a + A[a,b]`,

where `A[a,b]` is the forward directed path on `A`. Also replace the marked segment of `C` by `Q`, obtaining a directed cycle `L_Q`. The three cycles `K_a`, `L_Q`, and untouched `B` are vertex-disjoint. Their total size is

`|B| + (d_A(a,b)+2) + (|C| + ell - t)`.

Global minimality of `(A,B,C)` gives

`d_A(a,b)+2+ell-t >= |A|`,

hence, because `a!=b`,

`ell >= t + d_A(b,a) - 2`.

The `m` fan vertices have `m` distinct positive forward distances from `b`, so one has `d_A(b,a)>=m`. Therefore every such marked bypass satisfies the exact tax

`ell >= m+t-2`.

Equivalently, if `s=t-1` is the number of internal packed vertices bypassed (including `u`),

`ell >= m+s-1`.

For the singleton segment `u^- -> u -> u+`, this is `ell>=m`.

If equality `ell=m+s-1` holds at the extremal fan vertex with distance `m`, then the displayed total-size comparison is equality, so the construction is a size-neutral two-cycle exchange yielding another globally minimum three-packing. Thus, in a branch excluding neutral exchanges, integrality upgrades the tax to

`ell >= m+s`.

This repairs the false unguarded statement: **cross transition / inport-tax dichotomy**, not the naked tax, is valid.

## Applying fleet03/B04 — SIX-support Menger saturation

Use 3-vertex-strongness exactly as in the named partner's `BT4-R4-MENGER-SAT-v1`. In `D-u`, there are two internally vertex-disjoint directed `u^-`-to-`u+` paths `P1,P2`, in addition to the packed two-edge path through `u`.

Suppose a `Pi` avoids both target cycles `A union B` internally. The partner's support-segment extraction applied with support cycle `C` yields an `R`-internal subpath `Qi` bypassing a proper forward segment of `C` whose internal vertices include `u`. If that segment contains `s_i>=1` internal packed vertices and `Qi` has length `ell_i`, the new SIX tax gives

`ell_i >= m+s_i-1`,

so `Qi` uses at least `ell_i-1 >= m+s_i-2 >= m-1` internal remainder vertices.

If both `P1,P2` avoid `A union B`, their extracted `R`-internal vertex sets are disjoint, hence

`|R| >= (ell_1-1)+(ell_2-1) >= 2m+s_1+s_2-4 >= 2m-2`.

Therefore:

- if `|R| < 2m-2`, at least one Menger path enters a target packed cycle internally;
- if `|R| = 2m-2` and both avoid the target cycles, every inequality is equality, so `s_1=s_2=1`, `ell_1=ell_2=m`, the two internal remainder sets partition `R`, and both bypasses give neutral globally minimum exchanges.

Consequently, in a **no-cross, no-neutral** branch with

`|R| <= 2m-2`,

at least one of the two independent Menger paths must enter `A union B` internally.

For the named partner's live four-remainder regime, `m>=3` gives `2m-2>=4`. Thus every cycle-supported SIX witness in `|R|=4` is reduced to the same packed-cycle-entering linkage obstruction `R4-HX` already isolated by fleet03/B04. This is a genuine payment on the SIX branch: a small-remainder cycle-supported SIX object no longer constitutes a separate pure-remainder obstruction.

## Digon boundary — exact sharpness of the reduction

A second adversary repairs a common digon shortcut. On vertices `0,...,9`, start from the complete bidirected digraph and delete only arcs `2->8` and `2->9`. The digon is `0<->1`. Before deleting the digon the minimum outdegree is exactly seven, attained only at vertex `2`; after deleting vertices `0,1`, vertex `2` has surviving outdegree exactly five while every other survivor has outdegree seven.

Hence the universally valid bound after deleting a digon from a `delta+>=7` graph is `delta+>=5`, and this is sharp; one cannot silently retain threshold six or seven. The correct oriented-counterexample reduction therefore genuinely needs the proved `k=3` theorem at minimum outdegree five, followed by re-adding the digon as the fourth cycle.

## Exact computation and reproducibility

The deterministic checker was executed in this invocation and returned `PASS`. It verifies the full 16-vertex adjacency certificate, orientation, exact outdegree seven, arc domination, 3-vertex-strongness, global minimum of the three packed triangles by the absolute oriented lower bound nine, acyclic remainder, the SIX witness and two length-two bypasses, the explicit four-pack, and the sharp asymmetric digon deletion example.

- checker commit `79357fe7c64513aa874b2cee2e8961a1239dd26e`, Git blob `640f9513d9f3102ff34fcd224bd9cbcaf2e1a74c`, 3796 bytes, SHA-256 `74aff2da101dc801e4c9a38906edcba3f3386d918722f3569f7b5b0aba42fc47`;
- output commit `745a3a28592f87ca5137ef574d7b80c7fc075be5`, Git blob `0f9624a1c8f77f1e673b298b465ef43b51f5a21a`, 814 bytes, SHA-256 `794723afd00f7ee9d873672d1281b3007fec31c4f9d74b01dab3b2445e4155a5`.

The checker is evidence only for the finite adversaries and listed graph properties. The theorem-sized bypass tax and Menger corollary are proved above on the page.

## Before / after / first remaining implication

Before this run, the lead's compact conditional proof still treated the SIX branch as an independent unpaid closure, while the named partner's sharp Menger saturation applied to cycle-supported five-witnesses. A natural attempt to copy its collar tax directly to a SIX witness is false, as the 16-vertex adversary demonstrates.

After this run, the corrected inport-aware tax extends the partner's Menger saturation to cycle-supported SIX witnesses. In the four-remainder regime, and more generally whenever `|R|<=2m-2`, a SIX witness gives a cross transition, a neutral exchange, or a target-packed-entering Menger path. The purely local short-bypass SIX obstruction is removed.

The first essential remaining implication is now shared rather than SIX-specific:

**HX-SPLICE.** Convert a target-packed-entering `u^-`-to-`u+` linkage, together with the heavy fan and inport structure, into a legal pair of vertex-disjoint directed replacement cycles, a strict reduction of the globally minimum three-packing, a directed cycle in the exchanged remainder, or a new SIX/cross object that strictly advances the state.

This is precisely compatible with fleet03/B04's `R4-HX` frontier. The separate larger-remainder strict-collar/neutral-orbit closure also remains open.

## Nonclaims and status

- BT4 is not proved here and remains open in the current literature check.
- The 16-vertex adversary refutes only the stronger unguarded bypass-tax lemma; it explicitly has four disjoint directed cycles.
- A packed-cycle-entering path is not itself a fourth cycle.
- No edge-disjoint substitute, near-directed relaxed cycle, larger degree threshold, or bounded-order theorem is used as target closure.
- No genuine authenticated brain retrieval/context was used: `WITHOUT_VERIFIED_BRAIN`.

Honest status: **`ESSENTIAL_STEP_APPLIED`**, with local **`CANDIDATE_REFUTED`**.
