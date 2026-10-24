# BT4 lead attempt — primitive-trace transversal escape

Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`  
Run: `20260922T101701Z-b04-bt4-r11`

## 1. Live scope and source boundary

Fresh main at invocation start was `aca6efb3abc84c3525eaf05e496bf5afcbbde284`. Before this substantive write main was re-resolved at `611bc5200656d36182e58c227172aee5b2c08e8f`; the owner README remained Git blob `3d4a9372c87802ab734141a3374d04c8823372e3`, revision `2026-09-22.2`, with `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z` active and no later B04 stop observed. `AGENTS.md` at the recheck was blob `94387098453b9f4a9b10179183f6f6ec780fd987`; its older installation text is expressly superseded by the later owner README for this slot. New installation and benchmark work remained stopped.

Target: every finite loopless digraph with at most one arc per ordered pair and minimum outdegree at least seven has four vertex-disjoint genuinely directed cycles; digons are allowed.

Public theorem boundary used:
- Bessy--Muis--Sereni--Steiner--Wiederrecht, arXiv:2608.12948 (13 Aug 2026): the genuine Bermond--Thomassen conjecture remains unresolved for every `k>=4`; their `2k-1` theorem allows a cycle made directed by reversing one arc, so it is not substituted for BT4.
- The genuine `k=3` input used by the campaign is the known minimum-outdegree-five theorem (Lichiardopol--Pór--Sereni, SIAM J. Discrete Math. 23 (2009), DOI 10.1137/080715792), together with the campaign's source-bound strengthened `k=2` input.

Repository mathematics actually consumed:
- latest complete B04 report before this invocation, `proofnet24/collective-BT4/account02/B04/account02-B04-20260922T094740Z-bt4-r11/REPORT.md`, blob `b768e00ab1e7f22e0cfd56d6f95ffbc36b3a1c60`, especially `TRACE-ORDER`, the reverse-gap lemma, and `BT4-PRIMITIVE-TRACE-MIXED-PACKING-ONE-v1`;
- controlling B04 handoff `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1`, commit `3d1cdc39d7512ad857e134f23740c027ef879764`, blob `b0c1c37b1d36fd7cf855946f20eb382a61cd346d`;
- named OTHER-account partner account03/B05 report `BT4-FRESH-PORT-OR-C-WALL`, blob `060eddbca21de4d78c8059e71398a7d1833d9f64`, especially its connector-rank necessity and its 3-vertex-strong port-avoidance lemma;
- account01/B06 `BT4-PRIMITIVE-TORUS-NO-CANONICAL-2SPLICE-v1`, commit `0498c881be30ff6ab345a45d8dd5c7cbe511ac6d`, blob `2e8606f5a2bf0e1a7a76725baf3022a780a6840c`, as an independent source for the primitive cyclic-order obstruction.

No peer outcome label is promoted to target truth.

## 2. Compact conditional end-to-end BT4 proof state

Assume the inherited campaign reductions: a BT4 counterexample can be put in the exact-seven, arc-dominated, 3-vertex-strong minimum-counterexample normal form, with a globally minimum packing of three genuine directed cycles `A,B,C` and acyclic remainder `R`. The existing deficit/pivot analysis reduces the surviving states to recognized interfaces: `SIX`, bounded `F2/F3`, the seven-remainder pinwheel/support-carried omitted-sink state, or the clean heavy-triangle/four-port state.

In the clean four-port state, `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1` forces a genuine cross-support connector or a same-support bypass. The preceding B04 theorem `BT4-PRIMITIVE-TRACE-MIXED-PACKING-ONE-v1` proves that no amount of routing that remains parallel to one primitive two-support trace can itself produce two vertex-disjoint mixed replacement cycles. Therefore a successful proof must force an order-breaking off-trace object or a recognized non-two-support exit.

The theorem proved below supplies exactly that existence implication from 3-vertex-strongness. Consequently a complete BT4 proof follows if the following remaining interfaces are closed without weakening the target: the separate `SIX` branch; bounded `F2/F3`; the seven-remainder pinwheel branch; and the new `BT4-OFF-TRACE-RANK-SPLICE` obligation that converts the forced off-trace connector family, together with the clean four-port geometry, into a legal disjoint replacement / strict packing decrease / cyclic exchanged remainder / fourth cycle.

No claim is made here that one off-trace connector alone is already two replacement cycles.

## 3. Primitive trace notation recalled

Let

`A=a_0 a_1 ... a_{m-1} a_0`,  `B=b_0 b_1 ... b_{n-1} b_0`

be the two packed supports in the primitive coalescence trace. A cyclic signed occurrence `s` has state

`c_s=(i_s,j_s) in Z_m x Z_n`.

A plus occurrence authorizes an `A->B` connector with support endpoints `a_{i_s},b_{j_s}`; a minus occurrence authorizes a `B->A` connector with the same endpoint pair in the reverse direction. A trace-parallel connector may have arbitrary interior disjoint from `A union B`; only its ordered support endpoints are fixed by the trace state.

A trace-respecting simple mixed cycle follows positive directed support arcs while on `A` or `B` and uses only trace-parallel connectors when switching supports.

The preceding report proved:

- `TRACE-ORDER`: connector occurrences used by any trace-respecting simple mixed cycle occur in reverse cyclic word order;
- reverse-gap: in a `+,-` gap, every occurrence inside the gap has its `B` coordinate on the positive `B` segment used by that mixed cycle; in a `-,+` gap, every occurrence inside has its `A` coordinate on the positive `A` segment.

## 4. New lemma — every trace state is a two-vertex transversal

**Lemma (`BT4-TRACE-STATE-TRANSVERSAL-v1`).** Fix any trace occurrence `s` with state `(i_s,j_s)`, and put

`S_s={a_{i_s}, b_{j_s}}`.

Every trace-respecting simple mixed directed cycle meets `S_s`.

**Proof.** Let `Z` be such a mixed cycle.

If `Z` uses occurrence `s`, it uses a connector having `a_{i_s}` and `b_{j_s}` as support endpoints, so the claim is immediate.

Otherwise the connector occurrences selected by `Z` partition the cyclic reverse occurrence order into gaps between consecutive selected states. By `TRACE-ORDER`, occurrence `s` lies strictly inside one such gap. Connector signs on a mixed cycle alternate.

If the gap has signs `+,-`, the reverse-gap lemma puts the vertex `b_{j_s}` on the positive `B` segment used by `Z` across that gap. Hence `b_{j_s} in V(Z)`.

If the gap has signs `-,+`, the reverse-gap lemma puts `a_{i_s}` on the corresponding positive `A` segment used by `Z`. Hence `a_{i_s} in V(Z)`.

Thus every trace-respecting simple mixed cycle meets `S_s`. QED.

This strengthens the preceding packing-number-one theorem: the trace-respecting mixed cycles do not merely pairwise intersect; for every signed trace occurrence there is an explicit two-vertex transversal.

## 5. New theorem — 3-strongness forces an off-trace connector or a recognized exit

**Theorem (`BT4-TRACE-TRANSVERSAL-ESCAPE-v1`).** Work in the inherited minimum-counterexample normal form. Let `A,B,C` be the packed cycles, let `R` be acyclic, and suppose `D` is 3-vertex-strong. Fix a primitive trace between `A` and `B` and one of its occurrences `s`.

Then at least one of the following occurs:

1. an `A`- or `B`-support chord / strict support reduction;
2. a same-support directed excursion whose internal vertices lie in `R` (including a same-support return, with a distinct-port bypass as the usual case);
3. third-support mediation through `C`;
4. an `A<->B` connector with interior in `R` whose ordered support endpoint pair is **not** a state of the primitive trace.

In particular, if (1)--(3) are excluded by the current branch assumptions, an off-trace cross-support connector exists in `D-S_s`.

**Proof.** Set `S_s={a_{i_s},b_{j_s}}`. Because `D` is 3-vertex-strong, `D-S_s` is strongly connected. Choose surviving vertices `a in A-S_s` and `b in B-S_s`; concatenate an `a->b` path and a `b->a` path in `D-S_s`. Thus there is a closed directed walk in `D-S_s` meeting both `A` and `B`. Choose one, `W`, of minimum length among all such closed walks.

If `W` meets `C`, conclusion (3) holds. Hence assume it avoids `C`.

Suppose `W` repeats a vertex. Split it at two consecutive occurrences of a repeated vertex into two shorter nonempty closed subwalks `W_1,W_2`. By the minimal choice of `W`, neither subwalk can meet both `A` and `B`. If one met neither support, the other would contain every support hit of `W` and would meet both, again contradicting minimality. Consequently, after swapping labels if needed, `W_1` meets `A` and not `B`, while `W_2` meets `B` and not `A`.

Consider `W_1` and choose inside it a shortest closed subwalk meeting `A`. It lies in `(A-S_s) union R`, since `W` avoids `B` and `C`. The remainder `R` is acyclic. Also `A-S_s` is a directed path when only the packed successor arcs are used. Therefore this closed subwalk cannot close using only remainder arcs and positive support arcs. It must contain either a non-successor support chord, giving (1), or a directed excursion leaving `A` through `R` and returning to `A`, giving (2). Hence if (1) and (2) are absent, `W` has no repeated vertex and is a simple directed cycle.

Now assume (1)--(3) are all absent. Every maximal subpath of `W` whose internal vertices lie in `R` and whose endpoints lie in `A union B` must have endpoints on different supports; otherwise it is (2). While `W` lies on `A` or `B`, absence of a support chord forces it to follow the positive packed successor arcs. Therefore, if every support-switching connector of `W` had an ordered endpoint pair present in the primitive trace, `W` would be a trace-respecting simple mixed cycle.

But `W` lies in `D-S_s`, whereas `BT4-TRACE-STATE-TRANSVERSAL-v1` says every such trace-respecting mixed cycle meets `S_s`. Contradiction. Therefore some support-switching connector of `W` is off-trace, proving (4). QED.

The proof uses only genuine directed walks/cycles and vertex deletion; it does not replace BT4 by edge-disjointness or by a nearly-directed relaxation.

## 6. Application of the named partner result

Account03/B05 proved `BT4-FRESH-PORT-OR-C-WALL`: for the direct reverse clean cross `Q:q->a`, 3-vertex-strongness gives a `B->A` path in `D-{q,a}`; after trimming, either it is a fresh remainder-internal connector or it mediates through `C`.

The new transversal theorem sharpens the no-`C` side whenever `Q` is a primitive trace occurrence. Take `s` to be the trace state of `Q`. If the trimmed/closed geometry remained completely trace-respecting and had no same-support return/chord, it would create a trace-respecting mixed cycle avoiding `{q,a}`, impossible by the transversal lemma. Thus the partner's port-avoidance route cannot stay forever inside the primitive trace: it must encounter an off-trace connector or one of the recognized exits above. If `Q` itself is not a primitive trace occurrence, the desired order break is already present.

This is substantive use of the partner theorem: its 3-strong port-avoidance construction supplies the same deletion geometry that the transversal argument upgrades from merely `fresh` to `off-trace-or-exit`.

## 7. Stronger anti-transversal corollary

The theorem holds for **every** primitive trace occurrence `s`. Therefore, in a branch with no chord/strict reduction, no same-support remainder return, and no third-support mediation, for every state `s=(i_s,j_s)` there is an off-trace cross-support connector avoiding both `a_{i_s}` and `b_{j_s}`.

Equivalently: no trace-state pair `S_s` is a vertex transversal of the off-trace connector family.

This is stronger than existence of one fresh port. It is not yet connector matching rank two, because distinct off-trace connectors may still coalesce at remainder vertices; preserving this distinction is essential for the partner's connector-rank gate.

## 8. First missing implication after this run

The pure primitive-trace mechanism is refuted, while the existence of an order-breaking connector is now forced. The first local debt is therefore:

**`BT4-OFF-TRACE-RANK-SPLICE-v1`.** In the exact clean heavy-triangle/four-port state, assume none of the recognized exits (`SIX`, strict smaller packing, cyclic exchanged remainder, same-support compatible bypass, or third-support mediation) occurs. Use exact outdegree seven, arc domination, 3-vertex-strongness and the off-trace anti-transversal family above to force enough vertex-disjoint opposite-direction connector rank, in the correct support order, to build two vertex-disjoint replacement cycles; or derive one of the recognized exits.

A proof must control full path interiors, not only four distinct endpoint ports. Account03/B05's connector-rank lemma remains the correct gate: two disjoint mixed replacement cycles require two vertex-disjoint connectors in each direction. The new result supplies order-breaking connectors but does not silently promote endpoint diversity to path-disjoint rank.

The separate global debts `SIX`, bounded `F2/F3`, and the seven-remainder pinwheel/support-carried omitted-sink state remain open.

## 9. Honest status and failures

Outcome is `ESSENTIAL_STEP_APPLIED`, not `FULL_PROOF_CANDIDATE`.

What changed: the previous first local existence obligation `BT4-OFF-TRACE-OR-EXIT-v1` is proved under the inherited normal-form hypotheses. The primitive trace now has explicit two-vertex transversals, and 3-vertex-strongness forces any no-exit continuation to break that trace.

What did not change: no legal two-cycle splice has yet been derived from an arbitrary off-trace connector family; no `SIX`, `F2/F3`, or seven-remainder global closure is supplied. A cross, bypass, or off-trace path is not counted as a fourth cycle.

No decisive computation is used in this report; the preceding finite trace checker remains only an audit of the already-proved trace theorem and is not needed for the new proof.

## 10. Runtime / provenance

Model self-report: `GPT-5.6 Sol`.  
Reasoning effort requested: maximum actually supported.  
Reasoning effort configured: `UNKNOWN_NOT_EXPOSED`.  
Reasoning effort known: `UNKNOWN_NOT_EXPOSED`.  
Provider reasoning-token/thinking-time usage: `null` / not exposed.  
Execution status: `WITHOUT_VERIFIED_BRAIN` (authenticated GitHub source use occurred, but no genuine authenticated brain retrieval/context receiver use occurred).

Account02 managed inventory was inspected only for this account. The current managed B01--B20 set was 20/20 enabled, hourly, role-aligned to the collective/FEI split, and quiet at task level; no missing/down/B04-role-drift deficit was observed and no scheduler mutation was made. Historical disabled tasks were left untouched.

Scoped privacy review: no credentials, scheduler identifiers, machine paths, benchmark gold, unrelated private data, raw transcripts, email or Drive content are included in this artifact.
