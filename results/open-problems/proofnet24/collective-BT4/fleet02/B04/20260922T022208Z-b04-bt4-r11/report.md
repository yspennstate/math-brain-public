# BT4 fleet02/B04 — domination closes the null branch for cycle-supported five-witnesses

Run: `20260922T022208Z-b04-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Target and source boundary

Target: every finite loopless digraph with at most one arc per ordered vertex pair and minimum outdegree at least seven contains four vertex-disjoint genuinely directed cycles. Opposite arcs, hence digons, are allowed in the target.

The current relaxation is Stéphane Bessy, Matthijs Muis, Jean-Sébastien Sereni, Raphael Steiner, and Sebastian Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (13 August 2026). It explicitly states that the genuine Bermond-Thomassen conjecture remains open for every `k>=4` and proves only that at threshold `2k-1` the disjoint cycles may each be directed or become directed after reversing one arc. No such relaxed cycle is promoted here.

The lower-`k` input used is Nicolas Lichiardopol, Attila Pór, and Jean-Sébastien Sereni, *A Step toward the Bermond-Thomassen Conjecture about Disjoint Cycles in Digraphs*, SIAM J. Discrete Math. 23 (2009), 979–992, DOI `10.1137/080715792`: minimum outdegree five gives three vertex-disjoint directed cycles, and the same paper proves the strengthened two-cycle statement that all vertices of outdegree at least three except at most two of outdegree two force two vertex-disjoint directed cycles.

As in the inherited lead state, a counterexample may be reduced first to an oriented one: if a digon exists, delete its two vertices; every remaining vertex loses at most two outneighbors, so the `k=3` theorem gives three disjoint directed cycles in the remainder and the digon is a fourth. Then retain exactly seven outgoing arcs per vertex. Any four directed cycles in the resulting spanning subdigraph would also exist in the original digraph.

## Exact research state consumed

Latest complete campaign-lead version actually read:
- `yspennstate/math-open-problems`, report `proofnet24/collective-BT4/fleet02/B04/20260922T011943Z-b04-bt4-r11/report.md`;
- immutable commit `ca30763c69284b71c197ba0f49e37962f07e30c3`;
- report Git blob `ee3294c169f9736cd8f0fdb943b5cefab5906a9e`.

Named OTHER-account partner result actually applied:
- fleet03/B05 `BT4-TCEX-v2.1-linkage`;
- shared linkage artifact Git blob `5bbaf8123ad5cdcd3ce19e92f38587e79aefc69f`;
- underlying corrected linkage blobs `f1545c2e4a546d17150bb20bbc59650a29eb2672` and `f19feaaea52a2a892e510bd8fe03dbb18290fcb5`.

Newer compatible OTHER-account state also consumed:
- fleet04/B04 `BT4-G1-WITNESS-INVARIANT-v1`, shared artifact Git blob `f5533fe5b8ff8dd76fe701124f4bfd74370f2c8d`, which isolates `G1-S`: after the neutral light pivot the fixed pair-deletion witness set can be entirely support-carried, with at least three cycle-supported five-witnesses and two sharing one heavy target;
- fleet01/B06 fixed-pair witness staticization / exit-return collars, shared artifact Git blob `09dcb1717fb38cebef3cfeba63321d58802c004a`, used only for the static-witness interpretation and not as a target-level truth label.

No peer `PASS` or outcome label is used as proof.

## Inherited normal form and first missing inference

Work in the inherited oriented exact-outdegree-seven minimum counterexample with a globally minimum-total three-cycle packing `(A,B,C)`, nonempty acyclic remainder `R`, chordless packed cycles, every arc dominated, and 3-vertex-strongness.

For a fixed packed pair, deletion leaves a digraph with no two disjoint directed cycles. The strengthened `k=2` theorem therefore yields the familiar deficit alternative: either a surviving vertex has residual outdegree at most one (a six-or-more cross-fan), or there are at least three surviving vertices of residual outdegree exactly two (five-cross witnesses in the exact-seven normal form). This regenerates after every neutral packing exchange.

The lead's latest equality-completion lemma already turns every path-fan equality into an explicit size-neutral globally minimum exchange. Its off-pivot lemma says that a neutral light pivot in persistent `NO-SIX` either creates a six-fan or leaves an off-pivot five-witness. Fleet04/B04 sharpens the `G1` support branch: if no fixed-pair witness remains in the new remainder, at least three five-witnesses lie on the same complementary support cycle, and two have the same heavy target.

The first missing inference is therefore to make such a cycle-supported witness actionable without an unstructured null case.

## New lemma — domination eliminates the `heavy target has no arc into the witness` branch

Let `z` be a cycle-supported five-witness on the chordless packed cycle `B` for the deleted pair `{A,C}`. Thus in

`H = D - (A union C)`

the vertex `z` has residual outdegree exactly two. Chordlessness gives those two residual arcs as the support arc `z->z+` and one unique arc from `z` into `R`.

Suppose `z` is heavy on `A`, with

`m = |N+(z) intersect A| >= 3`.

Fleet03/B05's corrected linkage trichotomy for this exact support type has three branches:

1. `A` has no arc into `z`;
2. an `R`-internal path bypasses a proper forward segment `S` of `B` containing `z`, with the support-correct bound
   `ell >= m + |S| - 1`, equality giving a size-neutral two-cycle exchange;
3. in `D-z` there are two internally vertex-disjoint `z^-`-to-`z+` paths that both enter `A union C` internally.

The new point is that branch 1 itself forces branch 2 or an actual cross-packed transition.

### Proof

Assume branch 1: no vertex of `A` sends an arc to `z`.

Because every arc is dominated, choose a dominator `q0` of the support arc `z->z+`; thus

`q0->z` and `q0->z+`.

The vertex `q0` cannot lie on `B`. Indeed, any vertex of chordless `B` that sends an arc to `z` must be `z^-`. If `|B|>=4`, the additional arc `z^-->z+` is a chord. If `|B|=3`, the support arc is `z+->z^-`, so `z^-->z+` would be the opposite arc and is impossible because the normal form is oriented. Hence `q0 notin B`.

Also `q0 notin A` by the branch-1 assumption. Therefore `q0` lies in `C` or in `R`.

If `q0 in C`, then `q0->z` is already a genuine cross-packed transition from the other packed target cycle to the support cycle, and we are done.

Now suppose `q0 in R`. Since `q0->z` is an arc, dominate that arc: choose `q1` with

`q1->q0` and `q1->z`.

As long as `qi in R`, repeat, obtaining

`q(i+1)->qi` and `q(i+1)->z`.

The process cannot repeat a remainder vertex, since a repetition would create a directed cycle in the acyclic digraph `D[R]`. Finiteness therefore forces a first `qt notin R`.

The terminal vertex `qt` still sends an arc to `z`. It cannot be in `A`, again by branch 1. If `qt in C`, then

`qt -> q(t-1) -> ... -> q0 -> z`

is a cross-packed `C`-to-`B` transition with internal vertices in `R`.

The only remaining possibility is `qt in B`. Chordlessness then forces `qt=z^-`. Using the original extra arc `q0->z+`, we obtain the directed path

`z^- -> q(t-1) -> ... -> q0 -> z+`

whose internal vertices all lie in `R`. This is exactly an `R`-internal bypass of the singleton proper segment `S={z}` of `B`. The fleet03/B05 bound therefore applies with `|S|=1`:

`ell >= m`.

At equality it is the partner's size-neutral two-cycle exchange; if equality is excluded, integrality gives the strict charge `ell>=m+1`.

This proves the lemma.

## Consequence — closed support-witness trichotomy

For every cycle-supported five-witness `z` heavy on `A`, the corrected fleet03/B05 trichotomy may now be replaced by the following null-free version:

- an `R`-internal marked-segment bypass exists, satisfying `ell>=m+|S|-1` and giving a neutral exchange at equality; or
- there is a genuine cross-packed transition from the other packed cycle through `R` to `B`; or
- the two internally vertex-disjoint `z^-`-to-`z+` linkage paths of fleet03/B05 both enter `A union C` internally.

In particular, the condition `A has no arc into z` is no longer a terminal obstruction. If it occurs and no cross transition is produced, domination canonically manufactures the singleton bypass around `z`.

Applied to fleet04/B04's `G1-S` state, each of the two same-heavy support five-witnesses is therefore actionable by segment exchange/collar or cross linkage. The previously possible situation “three support witnesses exist, but the heavy target simply never enters the selected witness, so TCEX cannot start” is removed.

Applied to the lead's off-pivot witness, a persistent `NO-SIX` neutral orbit can now continue through a cycle-supported off-pivot witness only by one of:
- a neutral equality exchange;
- a strict marked-segment bypass carrying positive excess;
- a cross-packed transition / double linkage.

The `R`-supported off-pivot branch remains governed by the existing three-channel collar trichotomy: cross-packed hit, neutral equality exchange, or all-strict pure-`R` collars with the corresponding large-remainder cost.

## Updated complete conditional k=4 proof

A full proof follows from the following three still-unproved closure statements.

**(H6) Exact-six closure.** Every exact six-or-more cross-fan obstruction, including the cycle-supported `6-cross/0-R-exit` object, yields a legal two-cycle splice, a strict packing contradiction, or a transition into the already closed no-six machinery.

**(HX) Cross-linkage closure.** Every cross-packed transition or the two-path linkage output in the null-free support-witness trichotomy can be paired/rerouted to replace two packed cycles by two vertex-disjoint directed cycles, or else strictly reduce the globally minimum three-packing.

**(HS) Strict-collar/neutral-orbit closure.** A persistent `NO-SIX` sequence of globally minimum neutral exchanges cannot avoid both H6 and HX while every surviving `R`-supported witness has only strict pure-`R` collars and every surviving cycle-supported witness has only strict marked-segment bypasses.

Assuming H6, HX, and HS, take a minimum counterexample and the inherited exact-seven normal form. Pair deletion places every current minimum packing in `SIX` or `NO-SIX`. H6 closes `SIX`. In `NO-SIX`, every remainder sink has fan `(3,2,2)` and admits a light neutral pivot. The lead's off-pivot lemma then gives either H6 or a fixed-pair five-witness away from the pivot pair. If that witness is remainder-supported, the three-channel collar theorem gives HX, a neutral equality exchange, or an HS strict collar. If it is cycle-supported, the new lemma plus fleet03/B05 gives HX, a neutral equality segment exchange, or an HS strict marked-segment bypass. Equality moves to another globally minimum packing and the pair-deletion deficit regenerates. Thus any infinite/closed neutral dynamics avoiding H6/HX is exactly the configuration excluded by HS. Contradiction.

No near-directed cycle, edge-disjoint substitute, higher degree threshold, or restricted graph order enters this conditional proof.

## Actual before / after / remaining blocker

Before this run, the live `G1-S` branch had at least three same-support five-witnesses, two with a common heavy target, but fleet03/B05's support trichotomy still allowed the logically inert case that the heavy target had no incoming arc to the selected witness.

After this run, that inert case is eliminated: universal arc domination of the support edge plus acyclicity of `R` yields either a genuine transition from the other packed cycle or a singleton `R`-bypass to which the exact TCEX inequality applies.

The remaining blocker is not local admissibility of a support witness. It is global coalescence: strict bypasses can be long and multiple cross/linkage paths can merge. One still has to turn those simultaneous strict/cross objects into a legal two-cycle splice, a strict packing reduction, a directed cycle in an exchanged remainder, or a six-fan.

## Failure checks and nonclaims

- The target permits digons; they are eliminated only inside the counterexample reduction using the genuine `k=3` theorem.
- The proof of the new lemma uses chordlessness of `B`, orientation, universal arc domination, and acyclicity of `R`; without any one of these hypotheses the branch elimination is not asserted.
- The domination chain is finite because its `R` vertices are linked by arcs toward the previous chain vertex, so a repeated `R` vertex would create a directed cycle in `R`.
- A strict TCEX lower bound is not itself a contradiction to a minimum-total packing; it is recorded only as positive collar excess.
- Cross-packed transition alone does not automatically preserve the number of cycles; HX remains an explicit unpaid splice statement.
- No computation was used in this run.
- No full BT4 proof or novelty claim is made.

## Honest status

`ESSENTIAL_STEP_APPLIED`.

The first missing inference has been narrowed: cycle-supported off-pivot/G1-S witnesses have no null incoming-free branch. The live obstruction is now the global coalescence of strict segment bypasses, strict pure-`R` collars, and cross-linkage paths, together with the separate exact-six closure.
