# BT4 fleet04/B04 — chain-compatible MONO collision reduction

Run: `20260922T093625Z-a04-b04-r13`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Role: fleet04/B04 structural case split  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Target and current source boundary

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Digons are allowed in the source statement; the inherited minimal-counterexample reduction used by the team is oriented.

Fresh public-source verification during this run found Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (submitted 13 August 2026). Its abstract explicitly says that the genuine conjecture remains unresolved for every `k>=4`; its theorem permits a cycle that becomes directed after reversing one arc, so it does not settle BT4.

No claim of novelty is inferred from that search. The present report is an internal proof reduction only.

## 2. Exact inherited mathematics consumed

### Latest complete team-lead source

I source-read fleet02/B04 `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1` from canonical scientific report

`proofnet24/collective-BT4/fleet02/B04/20260922T0619Z-b04-bt4-r11/report.md`,

creation commit `14b8affcde6130bdbacbdfbd03888816b96d61ef`, Git blob `713053330313bf5906035c7bfd5841eb4e6b88ef`; shared handoff commit `3d1cdc39d7512ad857e134f23740c027ef879764`.

The lead's correction is preserved: the clean four-port mixed cycle cannot directly inherit the old two-packed-port SC2 remainder-hit argument. The live lead debt is a genuine CROSS/BYPASS splice/selection problem, including coalesced ports. A newer fleet02/B04 run had started by the time of this report, but no newer complete lead handoff was source-readable, so I do not treat an in-progress start record as a theorem.

### Assigned partner fleet01/B05

I source-read and apply two exact partner results.

1. `BT4-F3-R3-DEFECT1-PIVOT-v1`, shared commit `33bf0a29c07e72bbb56fcb3a93e0b0aebd68b500`, canonical creation commit `933e76837d4bb3a4e45297b2eeb3df481edd8fff`, Git blob `06534f6cac9597ba2398b031a14ff7d7cbcf3d6a`.

   In the surviving residual-three F3 branch, a current three-packing has order `n-3` while the global minimum three-packing has order `n-4`; the remainder has three vertices and is acyclic. Outside SIX, a cyclic remainder, and exact-R4 distance-three compression, any returning light support has a unique inport `c->t`, the sink targets exactly `c+,c++`, and the size-preserving pivot

   `c -> q -> r -> ... -> c`  to  `c -> t -> r -> ... -> c`

   swaps the sink `t` into the support and frees `q=c+`. In the no-R4 branch a remainder sink has at most one in-neighbor on any given light support.

2. `BT4-COMPATIBLE-BYPASS-CONDENSATION-v1`, report commit `50a132fde1964a31eb1c3a4ab2f131f3d12fe0ca`, exact report blob `9033957c23706f309a7007530fb65868d736eb61`.

   For a compatible family of same-support bypass switches with pairwise disjoint R-interiors and disjoint support segments, simultaneous switching gives a dependency digraph on released blocks. A dependency circuit is a fourth directed cycle. If the bypass interiors consume the old remainder and no dependency circuit exists, a terminal released block supplies a sink in the exchanged remainder; in global NO-SIX its fan is the canonical `(3,2,2)` five-witness state.

The partner's later `BT4-HT-COMMONPORT-REVERSE-CROSS-v1` (shared commit `c8aa394ac9cd4dc190ab6d71c71f09ff096dee25`) is a separate heavy-triangle/common-port frontier and is not used to smuggle a conclusion into the F3 pivot orbit.

### Previous fleet04/B04 reduction retained

The immediately preceding B04 result `BT4-F3-R3-PIVOT-SWITCH-TRIANGLE-v1`, shared commit `289a6ee8a640dffc9ac197e63abc4723c6a47071`, reduced the defect-one pivot orbit to:

- `TRI`: any genuine switch between the two light supports forces the repeated light support to be a directed triangle, outside SIX/cyclic-R/exact-R4;
- `MONO`: after some point all surviving tight pivots use one fixed light support.

The present run attacks `MONO` by a different mechanism: simultaneous bypass condensation plus an exact collision collar.

## 3. Compact conditional end-to-end route

The current collective proof route is conditional on closing the explicit residual branches, not on finding another generic cross.

For the residual-three F3 orbit:

`defect-one pivot recurrence`
`-> mixed support use gives TRI (previous B04 theorem)`
`-> otherwise MONO on a fixed light support A`
`-> three chain-clean MONO pivots would be a full-remainder bypass family`
`-> partner condensation gives fourth cycle or a released sink`
`-> released sink has two A-inneighbors, contradicting the partner one-inport rule`
`-> therefore MONO must collide locally with an inserted token within at most three pivots`
`-> exact collision types L/M/R below`.

Thus the generic infinite/finite-state MONO orbit is replaced by a bounded local port problem. Full BT4 would follow only after these local collision leaves, TRI, the lead's four-port coalescence, SIX, and the remaining seven-remainder branch are all closed.

## 4. A small extension of the partner condensation theorem

### Lemma 4.1 — chain-compatible bypass condensation

The fleet01/B05 compatible-bypass theorem remains valid if, on each packed support, selected support segments are allowed to share boundary endpoints, provided:

1. their **interiors** are pairwise disjoint;
2. any intersection of two selected segments is a common endpoint only;
3. their directed order on the support is consistent (equivalently, their union is a disjoint union of directed chains, possibly closing around the whole support);
4. bypass-path interiors are pairwise disjoint and lie in the old remainder;
5. every released block `int(S_i)` is nonempty.

#### Proof

On a directed support cycle, replacing several interior-disjoint directed segments by directed paths with the same endpoints still gives one directed support cycle when adjacent selected segments meet at a common boundary vertex: concatenate at that shared packed vertex. No internal remainder vertex is shared because the bypass interiors are disjoint. The exchanged remainder is still

`(old R minus all bypass interiors) union (all released segment interiors)`.

The released blocks remain pairwise disjoint because only segment endpoints may overlap. Hence the dependency digraph proof of fleet01/B05 is unchanged: a directed circuit among released blocks concatenates block suffixes and dependency arcs into a genuine residual directed cycle, while an acyclic dependency graph has a terminal released block. If all old R vertices were consumed, that terminal block endpoint is a sink of the exchanged remainder. QED.

This is not a new global splice theorem; it only removes an inessential endpoint-disjointness restriction from the already-proved simultaneous-switch argument.

## 5. New theorem — BT4-F3-R3-MONO-COLLISION-v1

Work in a surviving no-SIX/no-cyclic-R/no-exact-R4 residual-three F3 state, and suppose the orbit is in the `MONO` branch on one fixed light support `A`.

For a tight pivot, write the pre-pivot local support as

`c -> q -> r -> ... -> c`,

where `t` is the current remainder sink, `c->t`, and `t->q,r`. The pivot changes this local part to

`c -> t -> r`

and frees `q` into the three-vertex remainder. The graph arcs

`c->q` and `t->q`

remain. Therefore `q` has two in-neighbors on the same light support and, by the partner one-inport rule, **cannot be a remainder sink in any surviving state until a later pivot modifies this local support window**.

Call the post-pivot triple

`W(c,t,r) = c -> t -> r`

the modified window.

### Claim A — three chain-clean MONO pivots are impossible

Suppose, starting from a residual-three state with old remainder `{t0,t1,t2}`, that the next pivots stay on `A` and every pivot window is chain-clean relative to the previously modified windows: on the initial support the corresponding old two-edge segments

`S_i = c_i -> q_i -> r_i`

have disjoint interiors and meet, if at all, only at common boundary endpoints.

Because a released `q_i` keeps both packed in-neighbors `c_i,t_i` until its modified window is touched, no released `q_i` can be the sink for a later chain-clean pivot. Hence the first three chain-clean pivots necessarily consume the three distinct old remainder vertices `t0,t1,t2`.

Moreover the three switches commute: each replaces

`c_i -> q_i -> r_i`

by

`c_i -> t_i -> r_i`,

with pairwise disjoint bypass interiors `{t_i}` and chain-compatible support segments. Their bypass interiors consume **all** of the old three-vertex remainder.

Apply fleet01/B05 `BT4-COMPATIBLE-BYPASS-CONDENSATION-v1` through Lemma 4.1. Either the released-block dependency graph has a directed circuit, which is a fourth directed cycle, or it has a terminal released singleton `{q_j}`. In the latter case `q_j` is a sink of the exchanged remainder `{q0,q1,q2}`.

But chain compatibility left both `c_j` and the inserted `t_j` on support `A`, and both graph arcs

`c_j -> q_j`, `t_j -> q_j`

still exist. Thus the remainder sink `q_j` has two in-neighbors on the same light support, contradicting the partner no-R4 one-inport rule.

Therefore no surviving MONO orbit can execute three chain-clean pivots.

### Claim B — every surviving MONO orbit enters a three-position collision collar

Take the earliest pivot that is not chain-clean with the preceding chain-clean family. It must meet a previously modified window

`... -> e -> c -> t -> r -> u -> ...`

in a way that is more than endpoint adjacency.

A three-vertex pivot window that stays entirely in untouched old-support vertices is still chain-clean. A window ending at `c`, namely

`c^{-2} -> e -> c`,

shares only the endpoint `c` and is chain-clean by Lemma 4.1. Likewise a window beginning at `r`,

`r -> u -> u+`,

shares only endpoint `r` and is chain-clean.

Hence a non-chain-clean three-vertex pivot window must contain the inserted vertex `t`. Since the current support has local order

`e -> c -> t -> r`,

the pivot port is forced to be exactly one of

`e`, `c`, `t`.

Thus every surviving MONO branch reaches, within at most the third pivot, one of only three local collision types:

- **L (left recapture):** port `e`, window `e->c->t`; the pivot frees `c`;
- **M (middle/same-port recapture):** port `c`, window `c->t->r`; the pivot frees the old inserted sink `t`;
- **R (right/inserted-port relay):** port `t`, window `t->r->u`; the pivot uses the old inserted sink as its packed return port and frees `r`.

This is the exact MONO structural split.

## 6. Additional sharpening of the three collision leaves

Let the first pivot free `q`, and just before the first L/M/R collision let the three-vertex remainder be `{q,s,z}`, where `s` is the sink used by the collision pivot. Since `q` still has the two packed in-neighbors from the first modified window, `q` is not a remainder sink in a surviving state.

### L and M: short replacement or a two-sink fork

In case L, the collision sink has `s->c,t`; after the pivot `c` is released. If `q->s`, then

`c -> q -> s -> c`

is a genuine directed triangle. Replacing the active light support by that triangle while leaving the other two packed cycles untouched gives a three-packing of order `n-|A|`. Since the global minimum has order `n-4`, `|A|<=4`; equality `|A|=4` is an exact-R4 restart, so outside R4 the support is triangular.

In case M, `s->t,r`; after the pivot `t` is released. If `q->s`, then

`t -> q -> s -> t`

is a genuine directed triangle, and the same conclusion holds.

If instead `q` reaches `s` by the two-edge remainder path `q->z->s`, the analogous genuine replacement cycle has order four:

L: `c -> q -> z -> s -> c`,

M: `t -> q -> z -> s -> t`.

Replacing `A` by it gives a three-packing of order `n+1-|A|`; hence `|A|<=5`, and `|A|=5` is exact-R4. Therefore outside R4 this subcase has `|A|<=4`.

The only way this short-cycle argument fails is that `q` does not reach the chosen sink `s`. With three acyclic remainder vertices and `q` not a sink, this means `q->z` and `z` is a second remainder sink. Thus L/M split exactly into:

`short support (triangle or at most four outside R4)` **or** `two-sink fork`.

No claim is made here that the two-sink fork is already contradictory.

### R: common-blocker state and forced next port

Before R, the local support after the first pivot is

`c -> t -> r -> u`.

The R collision pivots sink `s` at port `t`, producing

`c -> t -> s -> u`

and releasing `r`. The new remainder is `{q,r,z}`.

Now:

- `q` has packed in-neighbors `c,t`;
- `r` has packed in-neighbors `t,s`.

So neither `q` nor `r` can be a remainder sink in a surviving no-R4 state. Since the three-vertex remainder is acyclic, `z` is therefore its **unique** sink.

The next MONO pivot must consume `z`. Its newly freed successor is again blocked by two packed in-neighbors. For the post-pivot three-vertex remainder to have any sink at all, that pivot must remove at least one packed blocker of `q` or `r`, i.e. it must free one of `{c,t,s}`. A tight pivot frees precisely the successor of its return port. In the current local order `c->t->s`, the next return port is therefore forced to be one of

`pred(c)`, `c`, `t`.

So R does not reopen an unbounded orbit: it forces an immediate second collision in the same three-position collar.

## 7. Resulting structural tree

The residual-three F3 pivot debt is now:

1. **TRI** — a light-support switch has already triangularized a repeated support (previous B04 theorem);
2. **MONO-L** — left recapture, which is either short support or a two-sink fork;
3. **MONO-M** — same-port recapture, again either short support or a two-sink fork;
4. **MONO-R** — inserted-port relay, producing two blocked released vertices with a common packed blocker, a unique third sink, and a next return port forced to `pred(c)`, `c`, or `t`.

There is no longer a spatially separated three-pivot MONO leaf.

## 8. First exact unpaid implication

`BT4-F3-R3-COLLISION-CLOSE-v1`:

> Close the L/M two-sink forks and the R forced three-port relay, or route them into TRI, exact-R4, SIX, a cyclic remainder, a strict smaller three-packing, or a source-valid CROSS/BYPASS splice. In the bounded L/M short-support leaves, exploit the support order `|A|<=4`; in R, exploit the two blocked released vertices sharing packed blocker `t` and the forced next port set `{pred(c),c,t}`.

This is strictly narrower than the prior `MONO-OR-TRIANGLE-CLOSE` instruction: an unrestricted same-support pivot orbit is no longer an unpaid object.

## 9. Failure boundary / nonclaims

- This report does **not** prove BT4.
- It does not count a CROSS, a bypass, or a neutral pivot as a fourth cycle.
- The chain-compatible extension only allows common **boundary endpoints**; support interiors must remain disjoint.
- The L/M two-sink fork is recorded as an explicit remaining branch, not silently assumed impossible.
- The R common-blocker collar is not claimed to splice by itself.
- SIX, the lead's clean-four-port/coalescence branch, TRI closure, and the seven-remainder branch remain separate debts.
- No tournament-only argument, near-directed cycle, benchmark answer, or unverified brain output is used.

Honest outcome: `ESSENTIAL_STEP_APPLIED`; target remains `OPEN_NOT_PROVED`.
