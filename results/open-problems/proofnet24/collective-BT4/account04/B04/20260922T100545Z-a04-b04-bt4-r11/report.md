# BT4 account04/B04 — common-port reverse crosses force an off-trace exit

Run: `20260922T100545Z-a04-b04-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-HT-COMMONPORT-OFFTRACE-COLLAPSE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and source boundary

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Digons are allowed in the source statement.

Fresh public status check: Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (13 August 2026), explicitly states that the genuine conjecture remains unresolved for all `k>=4`; its result permits each selected cycle to become directed after reversing at most one arc and therefore is not substituted for BT4.

Latest complete team-lead mathematics source-read in this run:
- account02/B04, `BT4-PRIMITIVE-TRACE-MIXED-PACKING-ONE-v1`, report blob `b768e00ab1e7f22e0cfd56d6f95ffbc36b3a1c60`, path `proofnet24/collective-BT4/account02/B04/account02-B04-20260922T094740Z-bt4-r11/REPORT.md` in `yspennstate/math-research-brain`.
- Essential predecessor handoff: account02/B04 `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1`, commit `3d1cdc39d7512ad857e134f23740c027ef879764`, handoff blob `b0c1c37b1d36fd7cf855946f20eb382a61cd346d`.

Named OTHER-account partner result consumed and applied:
- account01/B05, `BT4-HT-COMMONPORT-REVERSE-CROSS-v1`, canonical science commit `5f4ad4452b7b940cbe8f9106a934745496a75a36`, report blob `2536e90a7442fd90deab441243f0feb90e33db4a`, shared handoff commit `c8aa394ac9cd4dc190ab6d71c71f09ff096dee25`.

No code or computation is used in the new argument below.

## 2. Compact conditional end-to-end state

The inherited exact-seven oriented minimum-counterexample programme has several global debts: SIX/HX closure, bounded F2/F3 short-support states, the seven-remainder pinwheel/support-carried branch, and the heavy-triangle packed-port branch. The newest lead theorem closes an entire *candidate mechanism* inside the heavy-triangle packed-port branch: no two vertex-disjoint mixed cycles can be built if every support switch remains on one primitive two-support trace, even when each trace edge is replaced by arbitrary endpoint-matched parallel paths.

Consequently the lead's first local obligation is `BT4-OFF-TRACE-OR-EXIT-v1`: force an ordered cross endpoint pair outside the primitive trace, or a same-support bypass, third-support mediation, exchanged-remainder cycle/strict packing decrease, SIX, or the fourth cycle.

The assigned partner's common-port theorem supplies exactly the missing input in one important heavy-triangle subbranch: two target-distinct x-free packed-to-B reverse cross transitions plus the strong no-inport fact `B not->u,v`. The theorem below shows that these two transitions cannot remain a pure primitive-trace pair. Thus `BT4-OFF-TRACE-OR-EXIT-v1` is **proved for the aligned triangular common-port branch**.

## 3. Partner state used exactly

Use the partner's aligned triangular common-port state

`A = p -> u -> v -> p`,

with old remainder `R={x,r0,r1,r2}`, common remainder target

`N_R^+(u)=N_R^+(v)={r_k}`

for the surviving `k in {1,2}` collar alternatives, and the partner's proved fact

`B not->u,v`.                                                    (1)

The partner chooses distinct vertices

`a_u,a_v in B`, `a_u != a_v`,                                  (2)

outside the two-target sink fan and, by repeated arc domination, constructs for each `z in {u,v}` a transition

`J_z : s_z -> q_{m-1} -> ... -> q_0 -> a_z`,                    (3)

where

- `s_z` is packed and lies on `H` or `A`;
- every `q_i` is in `R`;
- the whole transition avoids `x` internally;
- crucially, the domination construction maintains

`s_z -> z` and `q_i -> z` for every internal `q_i`.              (4)

The last invariant is explicit in the partner proof: after dominating `q_i->z`, the next dominator is chosen to point to both `q_i` and `z`.

## 4. First new lemma — every nontrivial A-source reverse transition is already a bypass

**Lemma 4.1 (`APEX-BYPASS`).** For `z=u`, if `s_u` lies on `A`, then `s_u=p`. For `z=v`, if `s_v` lies on `A`, then `s_v=u`. Moreover, if such an A-source transition has any remainder interior at all, then it immediately yields a same-support bypass of a directed edge of `A`.

**Proof.** The triangle `A=p->u->v->p` is oriented. Hence the only A-vertex sending to `u` is `p`, and the only A-vertex sending to `v` is `u`. This proves the source claims.

Suppose `J_u` has A-source `p` and at least one internal remainder vertex. Let `q` be the first internal vertex after `p` in (3). By (4), `q->u`. Hence

`p -> q -> u`

is a same-support bypass of the support edge `p->u`, with interior outside the packing. Similarly, any nontrivial A-source `J_v` contains

`u -> q -> v`,

a same-support bypass of `u->v`. QED.

Therefore, in the lead's residual branch where neither a same-support bypass nor third-support mediation is allowed, both partner transitions must be direct A-to-B arcs:

`p -> a_u`, `u -> a_v`, with `a_u != a_v`.                      (5)

Indeed, a source on `H` is already third-support mediation, while Lemma 4.1 eliminates every non-direct A-source transition.

A useful side observation is that the partner's domination paths are automatically `r_k`-free: by (4) every internal vertex of `J_z` points to `z`, whereas `z->r_k`; orientation forbids `r_k->z`. Thus the apparent arbitrary R-ladder coalescence is even smaller than the partner needed. The main proof below does not require this extra localization.

## 5. Primitive-trace recurrence recalled

The latest lead encodes a primitive trace between directed supports `A` and `B` by a cyclic signed word `w`. A `+` occurrence with state `(i,j)` is an `A->B` connector `a_i->b_j`; a `-` occurrence is a `B->A` connector. In **reverse occurrence order**, crossing a `+` advances the A-coordinate by one, and crossing a `-` advances the B-coordinate by one.

Two consequences from the lead's exact recurrence are all that are needed here:

1. if two `+` states have consecutive A-sources, then in the reverse interval from the first `+` to the second there is no other `+` occurrence;
2. throughout that interval, after crossing the first `+`, the A-coordinate is the successor source and remains constant until the second `+` is reached.

Thus every intervening `-` occurrence is a `B->A` connector into that successor A-vertex.

## 6. Main theorem — the direct pair cannot both lie on the primitive trace

**Theorem (`BT4-HT-COMMONPORT-OFFTRACE-COLLAPSE-v1`).** In the account01/B05 aligned triangular common-port state, the two target-distinct reverse transitions force at least one of the following lead-recognized exits:

1. third-support mediation through `H`;
2. a same-support bypass on `A`;
3. an A-to-B cross whose ordered endpoint pair is **not** a state of the primitive trace.

In particular, the partner's remaining packed-source/R-ladder coalescence cannot survive as a pure trace-parallel two-support obstruction.

**Proof.** Apply Lemma 4.1 to the partner transitions `J_u,J_v`.

If either packed apex lies on `H`, outcome 1 holds. If an A-source transition has nonempty R-interior, outcome 2 holds. Hence assume neither exit occurs. Then (5) holds: the two transitions are the direct arcs

`p->a_u` and `u->a_v`, `a_u!=a_v`.

Assume for contradiction that both ordered endpoint pairs are `+` states of the same primitive trace. Since `p,u` are consecutive on the directed support `A`, their two `+` occurrences are consecutive in **plus-order** in the lead's reverse trace recurrence. Choose the reverse interval from the `p->a_u` occurrence to the `u->a_v` occurrence. There is no other `+` in this interval.

After crossing the first `+`, the A-coordinate is `u`; with no further `+` before the terminal occurrence, every intervening `-` state is therefore a connector from `B` into `u`. But (1) says `B not->u`. Hence there are **no** `-` occurrences in the interval either.

With neither `+` nor `-` strictly between the two occurrences, the B-coordinate does not change. Therefore the two `+` states have the same B endpoint:

`a_u=a_v`,

contradicting (2). Thus the two direct arcs cannot both be primitive-trace states. At least one is an order-breaking off-trace A-to-B cross, giving outcome 3. QED.

The symmetric choice of reverse interval is harmless: the recurrence direction is chosen so that crossing the first `+` advances the A-coordinate from `p` to its successor `u`. This is precisely the lead's convention.

## 7. Application to the lead frontier

The lead's newest theorem `BT4-PRIMITIVE-TRACE-MIXED-PACKING-ONE-v1` proves that adding more trace states or endpoint-matched trace-parallel detours cannot produce two disjoint mixed cycles. The theorem above shows that the assigned partner's common-port branch is **not trapped inside that obstruction**:

- an H-apex leaves the two-support trace through the third packed support;
- an A-apex with R-interior yields a same-support bypass immediately, before the B endpoint is even used;
- if both A-apex transitions are direct, target-distinctness plus `B not->u,v` forces at least one endpoint pair off the trace.

Thus the lead obligation `BT4-OFF-TRACE-OR-EXIT-v1` is discharged for the aligned triangular common-port branch. No attempt is made to claim that an off-trace cross alone is already a fourth cycle; it is the exact stronger interface requested by the lead after its trace-packing obstruction.

## 8. Updated structural case split

For this heavy-triangle common-port branch, there is no longer a separate "packed-source / R-ladder coalescence" terminal leaf. It collapses to:

- `HT-3SUPPORT`: a reverse transition starts on `H`;
- `HT-BYPASS`: a reverse transition starts on `A` and uses any remainder interior;
- `HT-OFFTRACE`: both reverse transitions are direct A-to-B arcs, and at least one is off the primitive trace.

The first two are existing recognized interfaces. The third is exactly the order-breaking input that the newest lead theorem says is necessary.

## 9. First unpaid implication after this run

`BT4-HT-OFFTRACE-SPLICE-v1`:

> Starting from the aligned triangular common-port state and an off-trace direct A-to-B arc supplied by the theorem above, combine that arc with the inherited B-to-A/H return and the target-distinct second reverse transition to force two vertex-disjoint replacement cycles, a strict lexicographic packing decrease, a cyclic exchanged remainder, SIX/HX, or the fourth directed cycle.

This is strictly narrower than the previous `BT4-OFF-TRACE-OR-EXIT-v1`: existence of the order-breaking exit is now proved in this branch, and only its splice consequence remains.

Separate campaign debts remain: the global SIX/HX branch, bounded F2/F3 short-support states outside this common-port configuration, the seven-remainder pinwheel/support-carried branch, and other heavy-triangle non-common-port leaves. BT4 is not claimed proved.

## 10. Failure checks and nonclaims

- The proof uses only the partner transitions whose endpoints are source-bound and target-distinct; it does not assume their R-interiors are disjoint.
- It does not convert a CROSS or BYPASS into a fourth cycle by fiat.
- It preserves the latest lead correction: no four-port mixed cycle is fed into the two-packed-port SC2 witness lemma.
- The primitive-trace step uses the lead's exact reverse recurrence, not a drawing-dependent crossing intuition.
- No computation, tournament-only reduction, near-directed cycle, or one-arc reversal is used.
- No full BT4 proof or novelty claim is made.

Honest outcome: `ESSENTIAL_STEP_APPLIED`.
