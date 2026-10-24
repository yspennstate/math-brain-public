# BT4 account02/B05 — heavy entry lifts to a genuine cross, a clean opposite pair, or an exact neutral heavy pivot

Run: `20260922T092501Z-b05-bt4-f61322da`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Candidate: `BT4-R4-F3-HEAVY-ENTRY-LIFT-OR-NEUTRAL-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and fresh controls

Target: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Digons are allowed in the source statement. The inherited minimal-counterexample branch used below is oriented; no one-reversed-arc or nearly-directed object is counted.

Fresh governing controls were read from `yspennstate/math-research-brain` at main commit `b7b15853b2661b547adf861d0e5a85014375b3cc`: `AGENTS.md`, `scheduled_tasks/README.md` including OWNER MESSAGE, `fleet.json`, `roles.json`, `PROTOCOL.md`, and the collective `ORDER.md`, `TARGETS.md`, and `ASSIGNMENTS.json`. OWNER revision was `2026-09-22.2`; B05 remained assigned to BT4 and no later B05 stop was present at run start. Older brain-installation and benchmark work remains superseded. No authenticated mathematical-brain retrieval/context was used.

## 2. Exact mathematical inputs consumed

### Campaign lead account02/B04

Latest complete lead report consumed: account02/B04 run `20260922T0619Z-b04-bt4-r11`, report Git blob `713053330313bf5906035c7bfd5841eb4e6b88ef`.

The inherited normal form is a hypothetical oriented exact-outdegree-seven BT4 counterexample, arc-dominated and 3-vertex-strong, with three disjoint directed cycles chosen lexicographically: first minimum total packed order, then maximum number of arcs induced by the acyclic remainder. Packed cycles are chordless. The lead's corrected `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1` turns a clean four-port mixed cycle into a genuine packed CROSS or a taxed same-support BYPASS; it explicitly leaves endpoint coalescence/disjoint splice closure unpaid.

### Named OTHER-account partner account03/B06 actually applied

I apply account03/B06 run `20260922T072201Z-account03-B06-bt4-r11`, candidate `BT4-R4-F3-APEX-COLLAR-v1`, report Git blob `102e3a54d5cac3a14afd00122e3d485d99a1b632`.

In its canonical four-remainder F3 both-repeat two-indirect state,

`S* = p -> x -> s -> p`,

`U` is the other light packed cycle, the current remainder is `R*={q,a,b,c}`, and the short return is

`W = u -> a -> p -> b -> u`.

In the second-predecessor apex case `z=u^{--}`, the partner proves that

`C_z = z -> b -> u -> U[u,z] -> z`

is a genuine directed cycle with exactly `|U|` vertices. Replacing `U` by `C_z` is therefore size-neutral. In a true counterexample the new remainder is exactly

`R'={q,a,c,t}`, where `t:=u^-`,

and `D[R']` is acyclic. The new packing `(H,S*,C_z)` is still globally minimum-total.

I also read the partner's newer account03/B06 run `20260922T081958Z-account03-B06-bt4-r12`, candidate `BT4-F3-R3-MIXED-APEX-NEUTRAL-FORK-v1`, blob `c5ad4eb921bc040f4464e1ca0a9cfda23ef36b49`. That theorem is an R3-D statement with a three-vertex remainder and is not silently transferred to the present R4 state; its neutral-fork mechanism is compatible motivation only.

### Other exact dependencies

Account04/B04 `BT4-R4-F3-RETURN-CUT-v1`, blob `425b7f0491ef4caf794ce862783c811edd26b110`, supplies the two-indirect return geometry and the one-cut acyclicity on `(U-{u}) union {s}`. Account04/B04 `BT4-R4-ARCMAX-TRIANGLE-COLLAPSE-v1`, blob `2f802a03755394931009175d7b6a5f94b0b2b084`, supplies the canonical triangular source state and the `(3,2,2)` heavy/light sink-fan structure.

The immediate account02/B05 predecessor, report blob `8985ff19de977969e5c21558edcfffd05502fa75`, proves `BT4-R4-F3-SECOND-COLLAR-TWOEXIT-v1`: for the newly exposed `t=u^-`, chordlessness of `U`, the four-vertex remainder budget and exact outdegree seven force

`|N^+(t) intersect (H union S*)| >= 2`.

If `t` hits some `y in S*\{p}`, the inherited path `p->b->u` gives a clean opposite light-cross pair. Otherwise the previous report stopped at a fresh direct heavy entry `t->h`. The present run attacks exactly that remaining heavy-entry alternative.

## 3. Compact conditional end-to-end route

Assume BT4 false and enter the inherited exact-seven oriented minimum-counterexample normal form. Run the established SIX/global-NO-SIX reduction and enter the canonical four-remainder F3 both-repeat branch. Apply the partner's second-predecessor collar exchange, exposing `t=u^-` in the acyclic remainder `R'`. Apply the preceding B05 degree budget.

- A clean target in `S*\{p}` already yields a four-port opposite light pair.
- Otherwise the degree budget forces the heavy-entry alternative treated here.
- The theorem below proves that the heavy entry cannot remain an isolated one-way interface: domination through the acyclic exchanged remainder lifts it to either a genuine packed cross, a clean opposite H/S* pair, or an exact size-neutral pivot of the heavy packed cycle.

Thus this second-collar branch no longer contains a raw one-way heavy entry. Full BT4 would follow after the remaining CROSS/BYPASS or neutral-orbit splice is closed together with the separate SIX, F2, other F3, coalesced-port, and larger-remainder branches.

## 4. Packed-inport lift through an acyclic remainder

Work with the globally minimum packing `(H,S*,C_z)` and its acyclic remainder `R'={q,a,c,t}`.

### Lemma 4.1 — direct packed inport to `t`

For every arc `t->v` with `v` packed, there exists a packed vertex `d` such that

`d -> t -> v`.

#### Proof

Use the inherited arc-domination property on `t->v`. If a common predecessor is packed, call it `d` and stop. Otherwise obtain `r1 in R'` with `r1->t,v`. If `r1` is in the remainder, dominate the arc `r1->t`; if its common predecessor is still in `R'`, continue. This produces a backward chain

`... -> r2 -> r1 -> t`

in which every newly chosen remainder vertex also sends directly to `t`. The process cannot repeat a remainder vertex, because a repetition would create a directed cycle in `D[R']`. Since `R'` is finite and acyclic, the process must eventually leave `R'`; the first vertex outside is packed and sends directly to `t`. QED.

This is an actual forward reroute in the original digraph. No reversed arc is inserted.

## 5. Theorem — `BT4-R4-F3-HEAVY-ENTRY-LIFT-OR-NEUTRAL-v1`

Assume the exact partner second-collar state and assume the preceding B05 clean-light alternative does not occur, so

`N^+(t) intersect (S*\{p}) = empty`.

Then the degree-forced heavy-entry branch has one of the following source-valid outputs:

1. a genuine packed-to-packed CROSS with exactly the remainder vertex `t` as its interior;
2. a clean opposite H/S* cross pair with four distinct packed endpoints and disjoint interiors;
3. an exact size-neutral replacement of the heavy packed cycle consuming `t` and freeing one specified successor of a heavy inport.

### Case A: `t->p`

The preceding degree budget gives at least two distinct targets in `H union S*`. Since `p` is the only allowed S* target, `t` has some heavy target `h in H`.

Apply Lemma 4.1 to `t->h` and obtain a packed `d` with `d->t->h`.

- If `d notin H`, this path is already a genuine packed cross into `H`, with sole internal vertex `t`.
- Suppose `d in H`. Then `d->t->p` is a genuine H-to-S* cross. The canonical heavy fan of `x` has exactly three distinct vertices in `H`. Choose `h' in N^+(x) intersect H` with `h'!=d`. Then `x->h'` is an S*-to-H cross. The two paths

  `d -> t -> p`, and `x -> h'`

  have four distinct packed endpoints (`d!=h'`, `p!=x`) and disjoint interiors. Hence this is the clean opposite-pair output.

Thus the `p+heavy` leaf is not a raw one-way heavy entry.

### Case B: `t !-> p`

With no target in `S*\{p}` either, the preceding degree budget forces at least two distinct heavy targets; choose

`t->h1`, `t->h2`, with `h1!=h2` in `H`.

Apply Lemma 4.1 separately and obtain packed vertices `d1,d2` with

`di -> t -> hi` for `i=1,2`.

If some `di notin H`, then `di->t->hi` is the genuine-cross output. Assume therefore that both `d1,d2` lie on `H`.

Because `di->t` and `t->hj`, for every `i,j in {1,2}` there is a directed length-two replacement path

`di -> t -> hj`.                                                (1)

Let `dist_H(di,hj)` denote forward directed edge distance on the chordless directed cycle `H`. Replacing the forward support segment `H[di,hj]` by (1) gives a directed cycle disjoint from `S*` and `C_z`. If `dist_H(di,hj)>2`, the replacement cycle is strictly shorter than `H`, contradicting global minimum total packed order. Hence

`dist_H(di,hj) <= 2` for all `i,j`.                             (2)

Orientedness gives `di!=hj`, because equality would make the digon `di<->t`. Therefore each of the two distinct targets `{h1,h2}` lies in the two-successor set

`{di^+,di^{++}}`                                                (3)

for each `i`. Since both sets in (3) have exactly two vertices, they coincide. On a directed cycle a consecutive two-successor set has a unique predecessor, so

`d1=d2=:d`, and `{h1,h2}={d^+,d^{++}}`.                         (4)

Consequently

`H' = d -> t -> d^{++} -> H[d^{++},d] -> d`                    (5)

is a genuine directed cycle. It contains every old vertex of `H` except `d^+`, and contains the new vertex `t`; therefore

`|H'|=|H|`.

Replacing `H` by `H'` is an exact size-neutral three-packing exchange. Its new remainder is

`{q,a,c,d^+}`.

In a true BT4 counterexample that remainder must be acyclic; otherwise its directed cycle together with `H',S*,C_z` is the forbidden fourth cycle. Since the new packing is globally minimum-total, its remainder is also subject to the original secondary arc-max upper bound relative to the canonical arc-max minimum packing.

This is the neutral-heavy-pivot output. QED.

### Extra localization of a cross source on `C_z`

If a packed inport `d` from Lemma 4.1 lies on `C_z`, then the original support edge `t->u` gives the same-support path

`d -> t -> u`.

Global minimum again forces forward distance at most two on `C_z`. Since the two predecessors of `u` on

`C_z = z -> b -> u -> U[u,z] -> z`

are exactly `b` and `z`, any such `C_z`-source is confined to

`d in {b,z}`.

So even the cross alternative has a two-point source collar rather than arbitrary endpoint freedom.

## 6. Stronger shortcut tested and repaired

A tempting stronger statement was that two distinct heavy targets cannot both lift to heavy-cycle inports. That statement is false. The equality case of global minimum permits exactly one pattern: a common root `d` and target set `{d^+,d^{++}}`. Instead of discarding this boundary, equation (5) turns it into an exact neutral heavy pivot.

Thus the correct universal conclusion is `CROSS / CLEAN_OPPOSITE_PAIR / NEUTRAL_HEAVY_PIVOT`, not “heavy entry always becomes a cross.” This correction is internal to the present lemma and is not a counterexample to BT4.

## 7. Exact finite sanity check

The attached `checker.py` exhaustively checks the finite cyclic-index statement behind (4) for directed support orders `3<=|H|<=200`: two distinct heavy targets that are simultaneously within forward distance one or two from each of two possible heavy inports, with orientedness excluding an inport from being one of the targets, force the two inports to coincide and the targets to be the first two successors.

Executed output:

- support orders checked: `3..200`;
- surviving index configurations: `20097`;
- for every order `n`, exactly `n` configurations survive;
- violations: `0`;
- status: `PASS`.

This checker is only a sanity check for the finite-index equality case. The proof of (2)--(5) is uniform for all cycle orders and is the mathematical justification.

Artifacts in this run:

- `checker.py`, creation commit `6c04c4eba3573deb8f1415eb0a9cbf8255270a1f`;
- `checker_output.json`, creation commit `4fa9d3e01e9c62e615d7f51c08aafd28a76a73fb`.

## 8. What this pays for

Before this run, the second-collar branch ended with a clean opposite light pair or a single fresh light-to-heavy arc. The latter was insufficient for disjointness. The present theorem spends arc domination and exchanged-remainder acyclicity to remove that raw leaf.

The heavy branch now has only structured outputs:

- a genuine packed CROSS through exactly one remainder vertex `t`;
- a clean opposite H/S* pair;
- an exact neutral heavy pivot with explicitly freed vertex `d^+` and a new four-vertex acyclic remainder.

Moreover any cross source on the transported light support `C_z` lies only at `{b,z}`.

This is a direct degree/minimality rerouting mechanism for the reversed-arc defect. It still does not assert that one cross or one opposite pair automatically gives two vertex-disjoint replacement cycles.

## 9. First unpaid implication

`BT4-R4-F3-CROSS-OR-DOUBLE-NEUTRAL-CLOSURE-v1`:

> Starting from the second-collar U-neutral exchange, use either (i) the clean four-port opposite pair, (ii) the new one-remainder-interior packed CROSS with its source-collar restriction, or (iii) the exact neutral heavy pivot freeing `d^+`, together with the existing direct `S*->C_z` / `C_z->S*` interfaces and the lead's CROSS/BYPASS witness lift. Prove that repeated neutral switches cannot return to the same minimum-packing state without producing two vertex-disjoint replacement directed cycles, a strict smaller three-packing, a cyclic exchanged remainder, SIX, a compatible bypass family, or a fourth directed cycle.

The separate SIX interface, F2, immediate-predecessor/other F3 cases, generic four-port endpoint coalescence, and larger-remainder branches remain explicit debts. Hence BT4 is not proved.

## 10. Inventory, provenance, and runtime metadata

A fresh account-local managed inventory was inspected without mutation. B01--B20 were all present, enabled, hourly, quiet, and role-aligned; B05 carried the current BT4 assignment. No deficit requiring B20 action was observed and no scheduler write was performed.

Model self-report: `GPT-5.6 Sol`. Requested reasoning effort: `maximum actually supported`. Configured reasoning effort: `UNKNOWN / NOT_EXPOSED`. Known effective effort: `UNKNOWN`. Exposed provider reasoning-token/time usage: `null / NOT_EXPOSED`.

No credentials, benchmark gold, private transcripts, email, Drive, paid API/model, Codex, remote workflow, permission change, or public posting was used.
