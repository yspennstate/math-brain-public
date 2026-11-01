# BT4 fleet03/B04 — four-remainder Menger saturation removes the strict-only support branch

Run: `20260922T025224Z-fleet03-B04-BT4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-R4-MENGER-SATURATION-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and source boundary

Target: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four vertex-disjoint genuinely directed cycles. Opposite arcs are allowed in the target, so digons count.

Current source check: Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (13 August 2026), still states that the exact conjecture is unresolved for every `k>=4`; its theorem permits each packed cycle either to be directed or to become directed after reversing one arc. No relaxed cycle is promoted here.

The inherited minimum-counterexample normal form used below is the team's exact one: after the standard digon reduction and retaining seven outgoing arcs per vertex, work in an oriented exact-outdegree-seven counterexample with a globally minimum-total packing `(A,B,C)` of three directed cycles, nonempty acyclic remainder `R`, chordless packed cycles, every arc dominated, and 3-vertex-strongness.

## Named other-account result consumed

The exact assigned partner `fleet04/B05` result consumed is:

- candidate `BT4-COUNT-v3-FOUR-R-ESCAPE`;
- canonical report `proofnet24/collective-BT4/fleet04/B05/b05-20260922t020746z-r31/report.md`;
- immutable commit `632e9bccbf1b5dec5db227580441652b58e85873`;
- Git blob `1a21f9b5ea72de714311d6927183c73062323632`.

Its proved input used here is the following exact four-remainder statement. In the global `NO-SIX` branch with `|R|=4`, at least one of these occurs: (i) a genuine cross-packed transition, (ii) a neutral minimum-packing exchange, or (iii) an `R`-internal same-cycle bypass produced by a proper exit footprint. In particular, if (i) and (ii) are absent, no five-witness lies in `R`; every required five-witness is cycle-supported.

I also use the campaign lead `fleet02/B04` controlling correction, blob `117d9760b66cfb5930c79ade79d2b449ce329b9b`: if a cycle-supported five-witness `w in B` is heavy on packed cycle `A` and `A` has no arc into `w`, domination of a heavy-fan arc and acyclicity of `R` force a genuine cross-packed transition. Thus in a no-cross state every such heavy witness has an actual inport `b->w` from its heavy target `A`.

Finally I use the already proved `fleet03/B05` linkage lemma `BT4-TCEX-v2.1-linkage`, blob `f1545c2e4a546d17150bb20bbc59650a29eb2672`: when `b->w` with `b in A` and `m=|N+(w) intersect A|>=3`, 3-vertex-strongness supplies two internally vertex-disjoint `w^-`-to-`w^+` paths avoiding `w`. If one of these avoids `A union C`, it contains an `R`-internal bypass of a proper segment `S` of `B` containing `w`; if its length is `ell`, then

`ell >= m + |S| - 1`.

For two such internally disjoint pure-`R` detours, their internal `R` sets are disjoint.

No peer outcome label is treated as proof; only the statements above with their hypotheses are imported.

## First missing implication attacked

The partner's four-remainder theorem still allowed its third output, a strict same-cycle bypass, to look like an isolated obstruction. The lead's global blocker likewise allowed strict support collars and packed-cycle linkages to coalesce without a splice.

The first question here is therefore exact and local:

> In the `|R|=4`, global-`NO-SIX`, no-cross branch, can a cycle-supported five-witness hide both of its 3-connectivity reroutings entirely in `R` while producing only strict bypasses and no neutral exchange?

The answer is no.

## Lemma — exact four-remainder Menger saturation

Let `w in B` be a cycle-supported five-witness for the deleted pair `A union C`, heavy on `A`, and set

`m = |N+(w) intersect A| >= 3`.

Assume `|R|=4`, the state is global `NO-SIX`, and there is no genuine cross-packed transition. Then `A->w` by the lead's corrected heavy-fan domination escape.

Let `P1,P2` be the two internally vertex-disjoint directed `w^-`-to-`w^+` paths in `D-w` supplied by 3-vertex-strongness in addition to the packed two-edge path through `w`.

Then at least one of the following holds:

1. at least one of `P1,P2` meets `A union C` internally; or
2. `m=3`, and both paths yield singleton-segment pure-`R` bypasses of length exactly three whose four internal vertices partition `R`; in particular both bypasses attain the marked-segment equality and each gives a size-neutral globally minimum packing exchange.

### Proof

Suppose neither `P1` nor `P2` meets `A union C` internally. Apply the exact segment-extraction lemma to each path. We obtain subpaths

`Qi: pi -> ... -> qi`

whose internal vertices lie in `R`, bypassing nonempty proper forward segments `Si` of `B` that contain `w`. Write

`si=|Si|>=1`, `ell_i=length(Qi)`.

The marked-segment exchange inequality gives

`ell_i >= m + si - 1`,

hence each bypass uses at least

`ell_i-1 >= m+si-2`

internal remainder vertices.

Because `P1,P2` are internally vertex-disjoint, the internal vertex sets of `Q1,Q2` are disjoint subsets of the four-vertex set `R`. Therefore

`4 = |R|
   >= (ell_1-1)+(ell_2-1)
   >= 2m+s_1+s_2-4
   >= 2*3+1+1-4
   = 4`.

Every inequality is therefore equality. Consequently

`m=3`, `s_1=s_2=1`, `ell_1=ell_2=3`,

and the two internal `R` sets, each of size two, partition all four remainder vertices.

Moreover the marked-segment lower bound is attained:

`ell_i = m+s_i-1 = 3`.

By the equality clause of the exact exchange lemma, each `Qi` is a size-neutral two-cycle exchange for the globally minimum packing. Thus the alternative in (2) holds. QED.

## Corollary — no strict-only support branch at |R|=4

In the same hypotheses, if neutral exchanges are also excluded, then alternative (2) is impossible. Hence at least one of the two independent Menger paths around every selected cycle-supported heavy five-witness must meet another packed cycle internally.

Combining this with the assigned partner's `BT4-COUNT-v3-FOUR-R-ESCAPE` gives the useful strengthened four-remainder trichotomy:

> In a global-`NO-SIX` state with `|R|=4`, one has a genuine cross-packed transition, or a neutral minimum-packing exchange, or a genuine packed-cycle-entering 3-connectivity linkage around a cycle-supported heavy five-witness. A strict pure-`R` bypass cannot be the only surviving support geometry.

Indeed, if cross and neutral outputs are absent, the partner theorem implies all required five-witnesses are cycle-supported. Choose one; its five cross-arcs make it heavy on one target cycle with `m>=3`. No cross forces the heavy-cycle inport, and the lemma above forces a packed-cycle-entering linkage.

This directly sharpens the partner's remaining third branch without assuming independent witness exits and without weakening the degree-seven or vertex-disjointness hypotheses.

## Why the degree-seven hypothesis is preserved exactly

For a cycle-supported five-witness `w`, deleting its two target cycles leaves residual outdegree exactly two. Chordlessness of its support cycle identifies one residual arc as `w->w+`, and the other is its unique remainder exit. Thus the witness is genuinely a five-cross object in the exact-seven graph; no average-degree replacement is made. The heavy target count `m>=3` is the literal pigeonhole consequence of those five target arcs.

The proof never deletes vertices and then pretends the minimum outdegree stays seven. Its only path input is the inherited 3-vertex-strong normal form, and the two paths `P1,P2` are internally vertex-disjoint by directed Menger. The disjointness of their extracted `R` bypasses is therefore genuine vertex disjointness, which is exactly what makes the four-vertex saturation count valid.

## Compact conditional route after this step

Assume a minimum counterexample and enter global `NO-SIX` with `|R|=4`. The assigned partner eliminates the featureless correlated-exit state into cross, neutral exchange, or bypass geometry. The new lemma removes the possibility that the support side persists solely through strict pure-`R` bypasses: absent cross and neutral exchange, an actual packed-cycle-entering Menger path is forced.

Therefore the first unpaid implication in this small-remainder branch is now narrower than before:

**R4-HX.** Convert a packed-cycle-entering `w^-`-to-`w^+` linkage, together with the heavy-cycle inport and five-cross fan of `w`, into either a legal vertex-disjoint two-cycle splice, a strict reduction of the globally minimum three-packing, a directed cycle in the exchanged remainder, or a six-fan.

The separate exact-six branch and larger-remainder neutral-orbit branch are untouched.

## Failure boundary / nonclaims

- A packed-cycle-entering Menger path is not itself a fourth directed cycle and is not promoted as such.
- A single cross-packed transition still does not automatically preserve the number of cycles; the global splice closure remains unpaid.
- The equality conclusion above is specific to `|R|=4`. For larger remainder, two strict pure-`R` detours can coexist and the saturation argument does not apply.
- The original BT4 target allows digons. Orientation is used only inside the inherited minimum-counterexample reduction where digons have already been eliminated using the genuine `k=3` theorem.
- No computation is used in this proof.
- No full BT4 proof or novelty claim is made.

## Honest status

`ESSENTIAL_STEP_APPLIED`.

The exact assigned partner result was applied, and the first strict-only four-remainder support obstruction was eliminated. Full BT4 remains open. The next recipient should attack `R4-HX` with the now forced packed-cycle-entering linkage rather than spend another run rediscovering exit-footprint structure.
