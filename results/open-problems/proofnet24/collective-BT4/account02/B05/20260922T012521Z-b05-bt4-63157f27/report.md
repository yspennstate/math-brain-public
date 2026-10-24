# BT4 account02/B05 — boundary lift for reversed-arc defects

Run: `20260922T012521Z-b05-bt4-63157f27`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Target: `BT4`  
Candidate: `BT4-RSC-v4-boundary-lift`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Full proof candidate: **no**  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Control/source boundary

This run obeyed the later collective-open-problems allocation and did no new brain-installation or benchmark work. Initial coherent control read used `math-research-brain` main `02234bb4f9b7ea3411e0d87876b58a1f108107f0`; a later prewrite check used main `4b418b1b462704a49f8216b909c5bf2e329efd90`, where OWNER revision remained `2026-09-22.2`, the active programme remained `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`, and B05 remained BT4. The later README Git blob is `3d4a9372c87802ab734141a3374d04c8823372e3`; current roles blob is `ed17ecc94f76720c0345b3e32249b791b20ec611`. At the initial coherent read the program artifacts were ORDER blob `75d8c4b263abae1c67e20a441b3773861fb26815`, TARGETS blob `59628cbbf801067846b2109373b25324549de35d`, and ASSIGNMENTS blob `cd7597fb89b6b9b9de2ddd0bf53df6f52e783cf1`. README/OWNER-message SHA-256 was not independently computed from raw bytes this run and is recorded as `UNVERIFIED_CURRENT_RUN`, not guessed.

Exact target retained: every finite loopless digraph with at most one arc per ordered vertex pair and minimum outdegree at least seven contains four vertex-disjoint genuinely directed cycles; digons and all graph orders are included. The source package's current-source boundary, including the recent one-reversed-arc relaxation, was preserved; no nearly-directed cycle is counted as a BT4 cycle.

## Exact inherited mathematics consumed

Campaign lead `account02/B04`, latest complete version available to this run:

- scientific report `proofnet24/collective-BT4/account02/B04/20260922T001806Z-b04-bt4-a1ceeb3c/report.md`, creation commit `a95b20d733b75b91a40c16c2faa225846f54973e`, blob `d82fc84180bc66fd660c6c79f9a7f26332bdae72`;
- controlling correction `correction.md`, commit `a0d5649a60d02bf6289208d581d979102e31d227`, blob `ef92cfc95fab44c1e256757de5fae4ec4b28e36b`.

Named OTHER-account partner actually applied: `account03/B06`, candidate `BT4-RSC-v2-tight-port`, scientific commit `4e204703776c90319afc67c4a03d56d474272d9c`, blob `81a20ff15088e74009551fffd8e9f4812b781819`, shared handoff blob `eb4c48c53fe08b37119810dc8f46d497b3690c36`. Its nonsaturated-U1 normal form gives a tight path and a single heavy-cycle boundary port, plus an equal-size exchange with acyclic exchanged remainder.

A second OTHER-account result was used to test whether the new lemma removes a real live obstruction rather than merely renaming it: `account04/B05`, candidate `BT4-COUNT-v2-HALL-DESCENT`, report blob `18c7cb8b90e567453128fcdb957fc3a426ade229`, shared handoff commit `7a0bd6fd65ae398a167f05b0d31674e38441b478`. Its Hall-failure branch ended at either a cross-cycle fork or a `split-R` family of at least two distinct remainder predecessors of a heavy vertex.

The inherited source-valid normal form used below is only the already-proved one: an oriented exact-outdegree-seven minimum counterexample `D`, a globally minimum-total packing `(C1,C2,C3)` of three directed cycles, acyclic remainder `R`, chordless packed cycles, domination of every arc, and heavy-target avoidance: if `u in R` has at least three outneighbors on a packed cycle `C`, then `C` sends no arc to `u`.

## Compact conditional end-to-end route

The team-level route is: reduce a hypothetical BT4 counterexample to the exact-seven/minimum-three-packing normal form; use pair deletion to split into the SIX/support-switch branch and the global NO-SIX branch; in NO-SIX, use the `(3,2,2)` sink geometry and tight-return/equal-size exchanges; finally replace every reversed-arc defect by a genuinely directed simultaneous splice or else force a directed cycle in the exchanged acyclic remainder. The SIX/cycle-supported and saturated-heavy-cycle branches remain separate obligations.

For the present assigned NO-SIX rerouting branch, the first unpaid implication before this run was sharper: an `R`-supported reversed-arc/fork certificate could be shown not to repair itself wholly inside the exchanged remainder, but it was not forced to reach a packed-cycle boundary in a way usable by a disjoint splice. The result below supplies that missing boundary lift. What is still unpaid is the **second disjoint crossing**: two lifted paths may coalesce, and one cross-pair by itself merges two cycles rather than producing two disjoint replacement cycles.

## 1. Arc-domination ladder

**Lemma 1 (arc-domination ladder).** Let `R` be the acyclic remainder of the fixed three-cycle packing. If `y,t in R` and `y->t`, then there is a packed vertex `z` and a directed path

`z=q_s -> q_{s-1} -> ... -> q_0=y -> t`

such that `q_0,...,q_{s-1}` are in `R` and every `q_i`, including `z`, has a direct arc to `t`.

**Proof.** Start with `q_0=y`. Domination of the arc `q_0->t` gives a vertex `q_1` with `q_1->q_0` and `q_1->t`. If `q_1` is outside `R`, stop. Otherwise dominate `q_1->t` to obtain `q_2->q_1,t`, and continue. While the constructed vertices stay in `R`, they are all distinct: a repetition would create a directed cycle in `R` along the predecessor chain. Since `R` is finite and acyclic, the process must terminate at a vertex `z=q_s` outside `R`. The packing and `R` partition the vertices, so `z` is on one of the three packed cycles. By construction every ladder vertex points directly to `t`. QED.

This is not a Menger existence statement and does not require choosing independent paths. It is a forced finite descent supplied by the already-proved arc-domination property.

## 2. Heavy predecessor export — the degree condition pushes an R defect to another packed cycle

**Lemma 2 (heavy predecessor export).** In the setting of Lemma 1, suppose additionally that `|N+(t) cap C|>=3` for a packed cycle `C`. Then the packed apex `z` of the ladder cannot lie on `C`. Hence every internal remainder predecessor arc `y->t` lifts to a path from one of the *other* two packed cycles into `t`, with all internal vertices in `R` and every ladder vertex also pointing directly to `t`.

**Proof.** Lemma 1 gives a packed apex `z` with `z->t`. If `z in C`, then `C->t`; but the inherited minimum-packing one-vertex exchange says that a remainder vertex receiving an arc from `C` can have at most two outneighbors on `C`. This contradicts `|N+(t) cap C|>=3`. Therefore `z` lies on a different packed cycle. QED.

This is the main new mechanism. It converts the degree-seven/minimum-counterexample domination property into a boundary rerouting certificate without assuming a reverse arc, a second cycle, or an independent path.

## 3. Applying the named partner: the nonsaturated U1 terminal defect is boundary-supported

Use `account03/B06`'s nonsaturated-U1 tight form. In the global NO-SIX hard branch, the heavy fan is three. Write the heavy packed cycle as `H`, and the partner's tight path as

`b -> p -> x`,

where `x` is the relevant remainder sink and `N+(x) cap H={b1,b2,b3}` with `b1=b+`, `b2=b++`, `b3=b+++`.

Apply Lemma 2 to the internal arc `p->x`. There is a vertex `z` on a packed cycle `K != H` and a ladder

`z -> ... -> p -> x`

whose internal vertices are in `R` and every ladder vertex also points directly to `x`. Thus `z->x`. The inherited cycle-entry cap then gives `|N+(x) cap K|<=2`; in the global NO-SIX `(3,2,2)` form this fan is exactly two, so `z` is a genuine light-cycle return port. Therefore the tight heavy collar is never supported only by `H` and `R`: it is simultaneously anchored at a light packed cycle.

Now take the terminal external fork from the previous `account02/B05` run.

- **Direct terminal:** if `d in R` satisfies `d->x` and `d->b2`, apply Lemma 2 to `d->x`. The reversed-arc defect lifts to a light packed cycle `K`: `z -> ... -> d -> x`, with `d->b2`. So the defect is a genuine light-to-heavy cross object; it cannot remain an anonymous remainder-only obstruction.
- **Two-step terminal:** if `d in R` satisfies `d->p` and `d->b2`, apply Lemma 1 to `d->p`. If its packed apex is on `H`, the named partner's single-port boundary lemma at remainder-distance one forces that apex to be the unique heavy port `b`. Otherwise the apex lies on one of the two other packed cycles. Thus this defect also reaches a packed boundary, with exactly one exceptional own-cycle support: the already-known port `b`.

This removes the earlier ambiguity “the fork is in `R`, therefore there is no internal repair” and replaces it by an explicit packed-boundary alternative.

## 4. Exchanged-remainder sharpening: only a `b1` barrier can keep the defect on the new heavy cycle

Perform the partner's neutral `m=3` heavy exchange. The new heavy cycle is

`H* = b -> p -> x -> b3 -> ... -> b`,

and the exchanged acyclic remainder is

`R*=(R-{p,x}) union {b1,b2}`.

For a terminal remainder vertex `d`, the arc `d->b2` is internal to `R*`. Apply Lemma 1 in `R*`.

If the packed apex lies on `H*`, original chordlessness of `H` shows that no surviving old `H` vertex in `H*` can point to `b2`; hence the only possible `H*` apices are the inserted vertices `p` or `x`.

- If the apex is `x`, then the first ladder vertex after `x` cannot be an old remainder vertex because `x` was an original sink of `R`. It also cannot be `b2`, because that would create a directed cycle in acyclic `R*`. Therefore the first ladder vertex is forced to be `b1`.
- If the apex is `p` in the two-step terminal case `d->p`, then the ladder from `p` to `d` followed by `d->p` is a directed cycle. The only original-heavy vertex it can contain inside `R*` is `b1` (`b2` cannot occur on the ladder by acyclicity). If that cycle avoided `b1`, it would be wholly disjoint from the original three packed cycles `H,K,L`, giving a fourth directed cycle immediately. Hence in a true counterexample every such `p`-apex ladder must pass through `b1`.

So after the equal-size exchange there is no diffuse own-heavy support left: every domination ladder for the terminal reversed defect either exits to another packed cycle or is trapped through the single freed vertex `b1`. This is the **`b1` barrier**.

## 5. Applying account04/B05: the Hall `split-R` branch is not a terminal obstruction

`account04/B05`'s Hall descent produces a heavy remainder vertex `u` with at least four targets `A subset N+(u) cap C`, and in its hard `split-R` branch at least two distinct remainder predecessors `d_1,d_2` dominate two distinct arcs `u->a_1`, `u->a_2` with `a_1,a_2 in A`:

`d_i->u` and `d_i->a_i`.

Apply Lemma 2 separately to `d_i->u`. For each `i` there is a packed apex on a cycle different from `C` and a ladder through `R` ending at `d_i`. Appending `d_i->a_i` gives a genuine directed transition from another packed cycle to the heavy cycle `C`, with all internal vertices in `R`.

Hence the old dichotomy “cross-cycle fork OR split-R predecessors” collapses to: **a cross-cycle transition always exists**. More precisely, for two distinct split-R dominators either the two lifted transitions are vertex-disjoint, or their union has a last common vertex `w`; after that last common vertex the two suffixes are internally disjoint and end at distinct targets `a_1,a_2` on `C`, while `w->u` also holds because every ladder vertex points directly to `u`. Thus Hall dependence yields either two disjoint cross transitions or a common-apex two-target fork. It is no longer an unstructured collection of remainder predecessors.

No claim is made that those two transitions are automatically the two oppositely oriented, vertex-disjoint crossings needed for a two-cycle splice. That is the remaining disjointness problem.

## Before/after and first essential missing implication

**Before:** the live U1/Hall analyses could force external or split-R dominators, but a reversed-arc defect could still be represented only as an `R`-supported predecessor/fork, with no source-valid packed boundary anchor. The Hall descent explicitly left a split-R alternative.

**After:** every internal predecessor of a vertex heavy on `C` exports by finite domination descent to one of the *other* packed cycles. In nonsaturated U1 the direct terminal defect exports to a light cycle, the two-step defect exports to another packed cycle or the unique heavy port, and after the neutral exchange any own-heavy apex is trapped through `b1`. In the Hall obstruction, the split-R alternative becomes cross-cycle transition geometry (two disjoint transitions or a common-apex two-target fork).

**First essential missing implication:** prove that the resulting boundary-supported transitions supply a second vertex-disjoint opposite crossing before they coalesce, or prove that every possible coalescence through the `b1` barrier creates a directed cycle in the exchanged remainder. One lifted crossing is insufficient: with only one opposite pair, splicing two packed cycles can merge them into one cycle and does not preserve the count of disjoint cycles. The SIX/cycle-supported saturation branch and the saturated heavy-cycle U1 branch remain separate obligations and are not claimed solved here.

## Failure audit / counterexample pressure

No source-valid counterexample to Lemmas 1-2 exists inside the inherited normal form: their proofs use only finite acyclicity, universal arc domination, the packing partition, and the already-proved heavy-target avoidance exchange. The potential overclaim tested and rejected in this run is **disjointness**: separate domination ladders can share their packed apex or coalesce in `R`; therefore the present result cannot be promoted to a simultaneous two-cycle splice. Likewise, no distinctness of dominators is inferred unless it is supplied by the Hall split-R hypothesis.

No computation was used for the mathematical step in this run; there is therefore no code/output certificate to cite. The contribution is analytical.

## Operational provenance

The account02 managed inventory was inspected only for this account. All twenty current collective tasks were present, enabled, hourly and quiet; B05's BT4 role matched the live allocation. No scheduler mutation, competing repair, new task, other-account action, hold override, email or notification change was performed. No scheduler identifiers are recorded here.

Scoped privacy/secret review: this report contains no credentials, scheduler identifiers, machine paths, raw private transcripts, unrelated private data, benchmark gold or broad mixed-domain memory. It preserves private repository visibility and source provenance.

Model self-report: `GPT-5.6 Sol`. Requested effort: `maximum actually supported`. Configured reasoning effort: `UNKNOWN / not exposed by the available scheduler interface`. Known effective reasoning effort: `UNKNOWN`. Exposed provider reasoning-token/time usage: `null / not exposed`. Measured elapsed wall-clock/tool execution through report assembly was approximately `884 s`; this includes tool/network time and is not pure thinking. The final finish record records the later exact elapsed snapshot.
