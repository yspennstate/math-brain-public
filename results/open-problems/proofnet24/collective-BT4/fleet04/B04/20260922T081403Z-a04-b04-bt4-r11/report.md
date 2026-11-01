# BT4 structural report — defect-one pivot-switch triangle reduction

Run: `20260922T081403Z-a04-b04-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Role: fleet04/B04 structural case split  
Partner: fleet01/B05  
Team lead: fleet02/B04  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Target and current external status

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Digons are allowed in the source target.

A fresh source check used Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (13 August 2026). Its abstract explicitly states that the genuine Bermond--Thomassen conjecture remains unresolved for every `k>=4`; its theorem allows each packed cycle either to be directed or to become directed after reversing one arc. No nearly-directed cycle is counted here.

## 2. Exact inherited sources used

### Team lead

The latest complete source-bound fleet02/B04 version available to this run was

`proofnet24/collective-BT4/fleet02/B04/20260922T0619Z-b04-bt4-r11/report.md`,

creation commit `14b8affcde6130bdbacbdfbd03888816b96d61ef`, report Git blob `713053330313bf5906035c7bfd5841eb4e6b88ef`.

I use its inherited normal form only at the level needed here: a hypothetical minimal counterexample may be taken oriented, exact-outdegree seven, arc-dominated and 3-vertex-strong, with a globally minimum-total three-cycle packing and an acyclic remainder. Neutral exchanges are not contradictions. The lead's live global debts include SIX, bounded F2/F3 states, and compatible splice/selection; the present report attacks the F3 residual-three pivot state and does not claim to close the lead's separate four-port heavy-triangle branch.

### Named OTHER-account partner actually applied

The newest fleet01/B05 shared source-bound handoff available in the brain was `BT4-HANDOFF-fleet01-B05-20260922T0809Z.md`, Git blob `01189044d46ddcb506113e0207f75506c33248fa`, naming the theorem

`BT4-F3-R3-DEFECT1-PIVOT-v1`.

Its advertised canonical path is

`proofnet24/collective-BT4/fleet01/B05/20260922T080526Z-b05-bt4-r11/report.md`

with advertised commit `933e76837d4bb3a4e45297b2eeb3df481edd8fff` and blob `06534f6cac9597ba2398b031a14ff7d7cbcf3d6a`. The authorized scientific repository did not resolve that advertised commit/path during this invocation, so I do **not** claim an independent canonical read of that partner report. I apply only the exact theorem statement present in the source-bound shared handoff, and preserve this source discrepancy as a provenance limitation.

The partner theorem's surviving state is the following. A current three-cycle packing `(H,A,B)` covers `n-3` vertices, while the global minimum three-packing covers `n-4`. Its remainder `R={u,v,t}` is acyclic and `t` is a sink. Outside SIX, its sink fan is `(3,2,2)`, with the three-fan on `H`. A returning packed cycle obeys the defect-one collar `d_Z(b,a)<=3`. A distance-three target gives exact R4 compression; outside that branch `H` does not return to the sink, every returning light support has one return port `b`, exact sink targets `{b+,b++}`, and at least one light support returns. The size-preserving tight pivot

`b -> t -> b++ -> Z[b++,b]`

replaces `b+` on the support by `t` and frees `b+` into the three-vertex remainder. Repeating after any acyclic pivot gives SIX, a cyclic remainder/fourth cycle, exact R4 compression, or another tight pivot. The partner leaves `BT4-F3-R3-PIVOT-ORBIT-CLOSE-v1` unpaid.

I also read fleet02/B06 `BT4-RANK2-PORT-PARITY-v1`, shared handoff blob `9f8fdd21cec8929827f1223f71985600bc638f13`, only as a boundary: rank-two connectors do not automatically splice. Canonical two-splicing additionally needs both support orders non-BLOCK and matching ID/SW parity. I do not infer those hypotheses below.

## 3. Compact conditional end-to-end route

The inherited route is now:

1. Reduce a counterexample to the oriented exact-seven, arc-dominated, 3-vertex-strong minimum-packing normal form using the genuine `k=3` theorem and prior team reductions.
2. Split into SIX and NO-SIX. Existing team work converts the relevant NO-SIX sinks to exact fan/port states and the F3 residual-three branch to the partner's finite defect-one pivot orbit.
3. The present theorem shows that a pivot orbit cannot switch between the two light supports without, within one further pivot, either hitting the already-recognized exit set (SIX, cyclic remainder/fourth cycle, exact R4 compression) or forcing the light support that is used twice in those three pivots to be a directed triangle.
4. Therefore `BT4-F3-R3-PIVOT-ORBIT-CLOSE-v1` splits into a genuinely one-support orbit and a triangular-light mixed orbit. A later switch that repeats the other support triangularizes that support as well.
5. Full BT4 still requires closure of those two residual orbit types together with the lead's separate SIX, bounded F2/F3, four-port coalescence, and seven-remainder debts.

The first new implication proved below is Step 3.

## 4. Uniform one-inport consequence of the partner collar

Call a state **surviving** if none of SIX, cyclic remainder/fourth cycle, or distance-three exact-R4 compression has occurred.

**Lemma 4.1 (one-inport property).** In a surviving defect-one pivot state, a remainder sink cannot have two distinct in-neighbors on the same packed cycle.

**Proof.** If that packed cycle is the sink's heavy three-fan support, then any return into the sink is the partner's heavy-return branch and the third target compresses to exact R4. If it is a light two-fan support, the partner theorem says that in the no-R4 branch it contributes at most one in-neighbor of the sink. These are the only fan types in the surviving `(3,2,2)` state. QED.

This simple formulation is useful because it is invariant under relabeling which of the three packed cycles is heavy after a neutral pivot.

## 5. Fresh-successor blocking

Consider a surviving tight pivot on a light support `A`. Immediately before the pivot write the local directed support order

`c -> q -> r -> ... -> c`,

where `c->t` is the unique return port into the current sink `t` and

`N+(t) intersect A = {q,r}`.

Thus `q=c+` and `r=c++`. The tight pivot replaces `q` by `t`:

`A' : c -> t -> r -> ... -> c`,

and the new remainder is obtained by replacing `t` with `q`.

The graph still contains both arcs

`c -> q`  and  `t -> q`.

Both `c` and `t` lie on `A'`. Hence, while `A'` remains unchanged, `q` has two packed in-neighbors on `A'` and by Lemma 4.1 **cannot be a remainder sink in any surviving state**.

Call this the **fresh-successor block**. It is stronger than merely saying that the freshly freed vertex is not the next sink: it remains sink-ineligible until its own support is changed again.

## 6. New theorem — BT4-F3-R3-PIVOT-SWITCH-TRIANGLE-v1

### Statement

Take four consecutive surviving states of the partner's defect-one tight-pivot orbit. Suppose the first two pivots use different light supports. Then after the third pivot one of the following occurs:

1. SIX, a cyclic remainder/fourth directed cycle, or exact R4 compression has already occurred; or
2. the light support used twice among those three pivots has order exactly three.

Equivalently, in a surviving no-R4/no-four orbit, **every switch from one light support to the other triangularizes, within one additional pivot, whichever of the two supports is used again**.

### Proof

Let the initial three-vertex remainder be

`R0={t,u,v}`

with sink `t`. Let the first pivot use light support `A` at return port `c`. Write

`A0 : c -> q -> r -> ... -> c`,

with

`c->t`, `t->q,r`.

After the first pivot,

`A1 : c -> t -> r -> ... -> c`,

and

`R1={u,v,q}`.

The freed vertex `q` is fresh-successor blocked because both `c,t` on `A1` point to `q`. Therefore the next remainder sink is one of `u,v`; rename so it is `u`.

By hypothesis the second pivot uses the other light support `B`. Let its freed successor be `q_B`. After that pivot the remainder is

`R2={v,q,q_B}`.

The support `A1` has not changed, so `q` is still blocked. The new vertex `q_B` is fresh-successor blocked on the newly pivoted `B`. Since `R2` is acyclic it has a sink, and the only possible sink is therefore `v`. In fact `v` is the unique remainder sink.

The third pivot must use one of the two light supports, since a surviving heavy return is excluded by the partner theorem. By symmetry assume it uses `A` again. Let its return port in `A1` be `e`; the pivot removes `e+` from `A1`, inserts `v`, and frees `q_2=e+`. Thus

`R3={q,q_B,q_2}`.

Support `B` has not changed since the second pivot, so `q_B` remains blocked. The newly freed `q_2` is blocked. Hence `q` is the unique sink of `R3`.

If `|A|=3`, conclusion (2) already holds. Assume for contradiction that `|A|>=4`.

In `A1`, both `c` and `t` point to the now-sink `q`. By Lemma 4.1 the third `A`-pivot must remove at least one of `c,t`; otherwise both remain packed in-neighbors of `q` on the same support.

There are only two ways for a single tight pivot to remove one of them.

**Case A: it removes `t`.** Since `t` is the successor of `c` in `A1`, the third pivot must reuse the same return port `e=c`. The local support becomes

`A2 : c -> v -> r -> ... -> c`.

Because the third pivot at `c` is tight for sink `v`,

`v -> t,r`.

Because `q` is now a surviving sink and `c->q` is a packed return port on `A2`, its no-R4 light fan is exactly the first two successors of `c`, so

`q -> v,r`.

From the first pivot we already have

`t -> q,r`.

Therefore

`T = t -> q -> v -> t`

is a genuine directed triangle. In state 3, `T` is disjoint from `H` and `B`: `t,q` are in the remainder and only `v` lies on `A2`. Replacing `A2` by `T` gives another three-cycle packing `(H,B,T)` of total order

`(n-3)-|A|+3 = n-|A|`.

The global minimum three-packing has order `n-4`, so

`n-|A| >= n-4`, hence `|A|<=4`.

Under the standing assumption `|A|>=4`, we get `|A|=4`. Then `(H,B,T)` is itself a globally minimum three-packing of order `n-4`, with a four-vertex complement. If that complement is cyclic we have the fourth directed cycle; if it is acyclic we have exactly the partner's R4 restart/compression state. Both are exit (1), contrary to survival. Thus Case A cannot survive with `|A|>=4`.

**Case B: it removes `c`.** Let `z` be the predecessor of `c` on `A1`; the third pivot is at `e=z`, replacing `c` by `v`. The vertex `t` remains on the packed support and still satisfies `t->q`; by Lemma 4.1 it is the unique `A`-inport into the sink `q`.

Since `|A|>=4`, the first two successors of `t` in the new support are `r` and an old `A0` vertex distinct from `q,r` (the pivot occurred at the predecessor of `c`, not at `t` or immediately after `t`). Chordlessness of the original support `A0` gives that `q`, whose old support successor was exactly `r`, has no arc to that second old support vertex. But the surviving light-return collar at inport `t` requires `q` to hit **both** first two successors of `t`. Contradiction.

(The exceptional `|A|=3` geometry is exactly why it was separated before this case: when `A1` is the triangle `c->t->r->c`, removing `c` makes the inserted vertex adjacent to `t`, and the chordlessness contradiction disappears. That is already conclusion (2).)

Thus if the first two pivot supports differ and the third pivot repeats `A`, survival forces `|A|=3`. The argument is symmetric when the third pivot repeats `B`. QED.

## 7. Structural consequences

The partner's finite pivot-orbit debt now has the following exact split.

### M — monochromatic orbit

After some state, every surviving tight pivot uses the same light support. This is a genuine residual mechanism: the proof above does not rule it out, because the fresh successor's own support changes at every step and can eventually make that vertex sink-eligible again. It must be closed using the one-support token-exchange structure rather than generic rank-two connector counting.

### T — triangular mixed orbit

The orbit uses both light supports. At the first adjacent support switch, one further pivot either exits to SIX/cyclic/R4 or makes the repeated light support a directed triangle. If later a switch is followed by a repeat of the other support, the same theorem makes the other light support a triangle as well. Thus every genuinely mixed infinite/periodic survivor lives on a state space with at least one triangular light support, and recurrent switching can force both light supports triangular.

This is stronger than merely saying the pivot orbit is finite. It identifies the only way a support switch can persist without immediately entering an already-covered exit: it must pass through a triangle-sized support.

## 8. Relation to rank-two parity and the lead frontier

Fleet02/B06's `BT4-RANK2-PORT-PARITY-v1` prevents a false closure claim: even if a triangular mixed orbit later produces two connectors each way between the light supports, two canonical mixed cycles follow only when both support cyclic orders are non-BLOCK and carry matching ID/SW parity. The theorem above does not assert that condition.

Likewise the fleet02/B04 lead theorem `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1` shows how an external three-hit witness can be lifted to a genuine CROSS/BYPASS in a different four-remainder branch. The present triangularization theorem supplies a new bounded-support entry point for that common CROSS/BYPASS programme, but it does not silently import the lead's four-port hypotheses.

## 9. First exact unpaid implication

Name the remaining F3 residual

`BT4-F3-R3-MONO-OR-TRIANGLE-CLOSE-v1`.

It has exactly two new leaves after the already-recognized exits:

- **MONO:** a finite defect-one tight-pivot orbit that from some point uses one light support only;
- **TRI:** a mixed-support orbit with at least one light support a directed triangle (and with both triangular after the corresponding repeated switches).

The next proof step should not be another generic connector-rank increase. For MONO, use the fixed union of the active light support with the three-vertex remainder and the one-inport/fresh-successor blocking rule to classify a periodic token-exchange orbit and force a smaller packing, cyclic remainder, or a source-valid bypass. For TRI, exploit the bounded three-vertex cyclic order together with the lead's fresh-port/CROSS machinery; if rank-two connectors arise, explicitly check B06's non-BLOCK/matching-parity hypotheses before splicing.

Global SIX, the lead's four-port coalescence, and the seven-remainder branches remain separate debts.

## 10. Failure checks and nonclaims

- This report does **not** prove BT4.
- It does not count a neutral tight pivot, CROSS, BYPASS, or rank-two connector as a fourth cycle.
- The triangle replacement comparison uses the partner's exact defect-one accounting: current packing order `n-3`, global minimum order `n-4`.
- The proof uses chordlessness only for arcs between vertices that were together on the original support before the pivots.
- The source discrepancy for the newest partner canonical report is preserved; the exact theorem statement used is the shared source-bound handoff, not an independently fetched canonical file.
- No finite computation was needed, so there is no numerical certificate or checker output to promote.
- No authenticated brain retrieval/context was used.

## 11. Status

`ESSENTIAL_STEP_APPLIED`.

A genuinely new implication closes the first support-switch layer of `BT4-F3-R3-PIVOT-ORBIT-CLOSE-v1`: two different consecutive pivot supports cannot continue generically. Within one further pivot, the repeated support is forced to triangle size unless the process has already reached SIX, a fourth cycle/cyclic remainder, or exact R4 compression. The residual orbit is therefore reduced to MONO versus TRI rather than an unrestricted finite pivot graph.