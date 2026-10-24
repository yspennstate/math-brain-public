# BT4 account02/B04 — four-remainder NO-SIX collapses to cross or saturated neutral exchange

Run: `20260922T031823Z-a02-b04-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-R4-SATURATION-COLLAPSE-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and source boundary

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are permitted in the source problem, so directed digons count.

The current relaxation source remains Stéphane Bessy, Matthijs Muis, Jean-Sébastien Sereni, Raphael Steiner and Sebastian Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (13 August 2026). It states that the genuine Bermond-Thomassen conjecture remains unresolved for every `k>=4` and proves instead the `2k-1` threshold for cycles that are directed or become directed after reversing one arc. No such near-directed cycle is counted below.

The genuine lower-`k` input is Nicolas Lichiardopol, Attila Pór and Jean-Sébastien Sereni, *A Step toward the Bermond-Thomassen Conjecture about Disjoint Cycles in Digraphs*, SIAM J. Discrete Math. 23 (2009), 979--992, DOI `10.1137/080715792`: minimum outdegree five yields three vertex-disjoint directed cycles, and their strengthened `k=2` result says that a digraph whose vertices all have outdegree at least three except at most two vertices of outdegree two contains two vertex-disjoint directed cycles.

The usual reduction retained by the campaign is legitimate for the exact target. If a counterexample contains a digon, remove its two vertices. Every remaining vertex loses at most two outneighbors, hence has outdegree at least five; the genuine `k=3` theorem supplies three disjoint directed cycles in the remainder, and the digon is a fourth. Thus a minimum counterexample may be taken oriented. Retaining exactly seven outgoing arcs at every vertex gives an exact-outdegree-seven spanning counterexample.

## Exact team state consumed

Latest complete campaign-lead package actually read before this derivation:

- account02/B04 `20260922T022208Z-b04-bt4-r11`, report Git blob `930c6906cc2532269bc35e0d0b0ea8e246eb250b`;
- controlling correction Git blob `117d9760b66cfb5930c79ade79d2b449ce329b9b`.

The controlling correction is essential: its heavy-fan domination escape says that a cycle-supported five-witness `z` heavy on packed cycle `A` but receiving no arc from `A` already forces a genuine cross-packed transition. Therefore, in a no-cross state, every cycle-supported heavy witness has an actual heavy-cycle inport, so the marked-segment inequality may be used without the previously quarantined hypothesis error.

Named OTHER-account partner result actually applied:

- account03/B05 `BT4-TCEX-v2.1-linkage`, shared handoff commit `5d6f5aca03679094f820de73cbd226a056a77499`, corrected linkage blobs `f1545c2e4a546d17150bb20bbc59650a29eb2672` and `f19feaaea52a2a892e510bd8fe03dbb18290fcb5`.

Its exact inputs used here are:

1. for a cycle-supported five-witness `w in B` heavy on `A` with fan `m>=3` and a genuine inport `A->w`, an `R`-internal bypass of a proper segment `S` of `B` containing `w` has edge length

   `ell >= m + |S| - 1`,

   and equality gives a size-neutral globally minimum two-cycle exchange; and
2. because the inherited normal form is 3-vertex-strong, `D-w` is 2-vertex-strong, so directed Menger gives two internally vertex-disjoint `w^-`-to-`w^+` paths avoiding `w`.

I also apply two compatible OTHER-account results:

- account03/B04 `BT4-R4-MENGER-SATURATION-v1`, shared blob `e0176457f0a7264c81c2a2aca058275b76cad053`, which performs the exact four-remainder accounting once the two Menger paths avoid the other packed cycles;
- account01/B06 fixed-pair/Menger-collar report blob `0ffb3fb1b521920e0a9cb3693fda8fd5bbb6a588`, which supplies three pairwise internally disjoint heavy-cycle-to-`R`-witness paths and the corrected path-fan inequality for an `R`-supported five-witness.

For comparison and strict strengthening, I read account04/B05 `BT4-COUNT-v3-FOUR-R-ESCAPE`, report blob `1a21f9b5ea72de714311d6927183c73062323632`. It had reduced global `NO-SIX`, `|R|=4` to a cross-packed transition, a neutral exchange, or an `R`-internal same-cycle bypass. The argument below removes the third, potentially strict, outcome.

A newer compatible account04/B06 sink-port report was also checked before delivery; it independently pushes neutral `(3,2,2)` sinks toward paired cross interfaces. It is not needed for the proof below.

No peer outcome label is used as a theorem. Only the source-bound statements above are imported.

## Inherited normal form

Assume BT4 false. Work in the inherited oriented exact-outdegree-seven counterexample `D` with:

1. a globally minimum-total packing `(A,B,C)` of three directed cycles;
2. nonempty acyclic remainder

   `R = V(D) \ (V(A) union V(B) union V(C))`;
3. chordless packed cycles;
4. every arc dominated; and
5. `D` 3-vertex-strong.

For every packed pair, delete those two cycles. The strengthened `k=2` theorem implies: either some surviving vertex has residual outdegree at most one, hence at least six outgoing arcs into the deleted pair (`SIX`), or there are at least three surviving vertices of residual outdegree exactly two, hence exactly five outgoing arcs into the deleted pair (`five-witnesses`). The global `NO-SIX` branch is the state in which every packed pair is in this second alternative.

A **cross-packed transition** means a directed path whose endpoints lie on two different packed cycles and whose internal vertices, if any, lie in `R`.

This run treats the exact branch

`global NO-SIX` and `|R|=4`.

## Lemma 1 — an internal visit to another packed cycle is already a cross transition

Let `w in B`, and let `P` be a directed `w^-`-to-`w^+` path in `D-w`. If `P` has an internal vertex on `A union C`, then a cross-packed transition exists.

### Proof

Traverse `P` from `w^-`. Let `x` be its first vertex in `A union C`. Let `y` be the last packed-cycle vertex of `P` before `x`. By the choice of `x`, every packed vertex before `x` lies on `B`; hence `y in B`. By the choice of `y`, the internal vertices of the subpath `yP x` lie outside all three packed cycles and therefore lie in `R`. Its endpoints lie on different packed cycles. QED.

Thus, in a no-cross state, every `w^-`-to-`w^+` Menger path avoiding `w` also avoids `A union C` internally.

## Lemma 2 — cycle-supported five-witnesses saturate all four remainder vertices

Assume `|R|=4` and there is no cross-packed transition. Let `w in B` be a cycle-supported five-witness for the deleted pair `{A,C}`, and suppose `w` is heavy on `A` with

`m = |N+(w) intersect A| >= 3`.

Then necessarily:

1. `m=3`;
2. there are two internally vertex-disjoint `R`-internal bypasses `Q_1,Q_2` around the singleton segment `{w}` of `B`;
3. each `Q_i` has edge length `ell_i=3`;
4. the two two-vertex internal sets `int(Q_1), int(Q_2)` partition all four vertices of `R`; and
5. both marked-segment inequalities are equalities, so each supplies a size-neutral globally minimum two-cycle exchange.

### Proof

Because there is no cross-packed transition, the lead's controlling heavy-fan domination escape forces a genuine inport from `A` to `w`. Hence the account03/B05 marked-segment theorem is hypothesis-correct for `w`.

By 3-vertex-strongness, `D-w` is 2-vertex-strong. Directed Menger gives two internally vertex-disjoint directed paths from `w^-` to `w^+` avoiding `w`. By Lemma 1 and the no-cross assumption, neither path can enter `A union C` internally.

Apply the corrected account03/B05/account03-B04 extraction to these two paths. We obtain internally vertex-disjoint `R`-internal bypasses `Q_i` of proper forward segments `S_i` of `B`, each segment containing `w`. Put `s_i=|S_i|>=1` and let `ell_i` be the edge length of `Q_i`.

The marked-segment theorem gives

`ell_i >= m + s_i - 1`.                                          (1)

Since `Q_i` has endpoints on `B` and all internal vertices in `R`, it uses `ell_i-1` remainder vertices internally. The two interiors are disjoint and `|R|=4`, so

`4 >= (ell_1-1) + (ell_2-1)`.                                   (2)

Using (1),

`4 >= (ell_1-1)+(ell_2-1)`
`  >= 2m + s_1 + s_2 - 4`
`  >= 2*3 + 1 + 1 - 4 = 4`.                                     (3)

Every inequality in (3) is therefore equality. Hence `m=3`, `s_1=s_2=1`, and `ell_1=ell_2=3`. Their internal vertex sets have size two each, are disjoint, and together contain four vertices, hence partition `R`.

Equality in the marked-segment theorem is exactly the account03/B05 size-neutral globally minimum two-cycle exchange. QED.

### Significance

There is no strict marked-bypass-only branch for a cycle-supported five-witness when `|R|=4` and cross transitions are excluded. The entire remainder is forced into two equality bypasses around the witness.

## Lemma 3 — R-supported five-witnesses also saturate all four remainder vertices

Assume again `|R|=4` and no cross-packed transition. Let `z in R` be a five-witness for a deleted packed pair, and let `T` be a heavy member of that pair with

`m = |N+(z) intersect T| >= 3`.

Then necessarily:

1. `m=3`;
2. there are three pairwise internally vertex-disjoint directed `T`-to-`z` paths, each of edge length exactly `2` and with internal vertices in `R`;
3. the three internal vertices are exactly `R \ {z}`; and
4. all three path-fan inequalities are equalities, so each is an actionable size-neutral globally minimum exchange.

### Proof

Use the account01/B06/account03/B04 Menger-collar input for an `R`-supported five-witness. There are three directed `T`-to-`z` paths, pairwise vertex-disjoint except at `z`, with distinct starts on `T`; trim them to their last `T` vertices. If a trimmed path met another packed cycle internally, it would contain a cross-packed transition. Under the no-cross assumption all its internal vertices lie in `R`.

Let the edge lengths be `L_1,L_2,L_3`. The corrected path-fan inequality gives

`L_i >= m-1`.                                                     (4)

The three interiors are pairwise disjoint and avoid `z`, so their internal remainder vertices together with `z` lie in the four-vertex set `R`. Therefore

`4 >= 1 + sum_i (L_i-1)`
`  >= 1 + 3(m-2)`.                                                (5)

Since `m>=3`, the right side is at least four. Equality must hold throughout. Thus `m=3`, every `L_i=2`, and the three one-vertex interiors are exactly the three vertices of `R\{z}`.

Every path-fan inequality is equality, and the lead's equality-completion result makes each equality an explicit size-neutral globally minimum exchange with acyclic exchanged remainder. QED.

### Significance

The older hard alternative `|R|>=3m-2>=7` is not merely absent at `|R|=4`: its failure forces complete equality saturation. An `R`-supported five-witness has three distinct neutral exchange channels exhausting the remainder.

## Theorem — four-remainder NO-SIX collapse

> **BT4-R4-SATURATION-COLLAPSE-v1.** In the inherited exact-seven, oriented, globally minimum three-cycle-packing normal form, every global `NO-SIX` state with `|R|=4` has at least one of the following:
>
> 1. a genuine cross-packed transition; or
> 2. a size-neutral globally minimum packing exchange.
>
> Moreover, if alternative 1 is absent, every selected five-witness is forced into one of the exact saturation geometries of Lemma 2 or Lemma 3. In particular, no strict `R`-collar or strict marked same-support bypass is needed to describe the four-remainder obstruction.

### Proof

Choose any packed pair. Global `NO-SIX` gives at least three surviving five-witnesses, so choose one witness `v`.

If `v in R`, apply Lemma 3. Under no cross it yields neutral equality exchanges.

Otherwise `v` lies on the complementary packed cycle, because it survives deletion of the chosen pair. It is heavy on one of the two deleted cycles by pigeonhole. Apply Lemma 2. Under no cross it again yields neutral equality exchanges.

Thus absence of a cross transition forces a neutral minimum-packing exchange. The final saturation statement is exactly Lemmas 2 and 3. QED.

## Strict strengthening of the previous four-remainder frontier

Before this run, account04/B05 `BT4-COUNT-v3-FOUR-R-ESCAPE` left three outcomes at `|R|=4`, global `NO-SIX`:

1. cross-packed transition;
2. neutral exchange; or
3. same-support `R`-bypass, possibly strict.

The new theorem removes outcome 3 as a terminal branch. If a support witness supplies the geometry, corrected 3-connectivity plus the exact four-vertex count forces *two* equality bypasses, not a lone strict bypass. If a remainder witness supplies the geometry, three path-fan channels are simultaneously tight.

Hence the exact four-remainder no-six residual is now:

`CROSS  or  SATURATED-NEUTRAL`.

No positive collar excess survives in this branch.

## Consequence for neutral dynamics

A size-neutral exchange preserves the total number of packed vertices, so it preserves `|R|=4`. The strengthened pair-deletion theorem applies again to the new minimum packing. Therefore, if a neutral exchange remains in global `NO-SIX` and still has no cross transition, the theorem applies again.

Thus any persistent four-remainder, no-cross, no-six dynamics is a finite orbit consisting entirely of saturated equality states. At every state a five-witness has at least two explicit neutral exits (two in the support case; three in the remainder case), with the corresponding path interiors exhausting `R` exactly.

This is substantially narrower than the previous `HS` strict-collar/neutral-orbit obstruction. It does **not** yet prove that such a saturated neutral orbit is impossible.

## Compact conditional end-to-end k=4 proof after this step

The inherited lead proof becomes complete under the following three closure statements.

**H6 — exact-six closure.** Every residual degree-at-most-one / six-or-more-cross-fan branch yields a legal two-cycle splice, a strict packing contradiction, or a transition to the no-six machinery.

**HX — cross-interface closure.** Every genuine cross-packed transition (including the account03/B05 switchwall outputs and the newer opposite-light cross pairs) can be paired/rerouted into a legal two-cycle replacement, a strict reduction of the global minimum three-packing, a directed cycle in the exchanged remainder, or H6.

**HN — saturated-neutral closure.** A persistent global `NO-SIX` orbit of globally minimum neutral exchanges cannot avoid H6 and HX. For `|R|=4`, it is enough to rule out the exact saturation geometries above; for larger remainders the previously derived strict-collar/linkage mechanisms remain available.

Assuming H6, HX and HN, take a counterexample in the inherited normal form. Pair deletion puts every current minimum packing into `SIX` or `NO-SIX`. H6 closes `SIX`. In `NO-SIX`, the sink/pivot and fixed-witness machinery yields remainder-supported or cycle-supported five-witnesses. Cross outputs are HX. Equality outputs move to another globally minimum packing and regenerate the deficit theorem. Strict larger-remainder collars feed the existing linkage/HS machinery. At `|R|=4`, the theorem above shows that no strict-collar branch exists at all: no-cross forces saturated equality. HN excludes the remaining neutral dynamics. Contradiction.

This conditional proof uses only genuinely directed cycles and the exact outdegree-seven target.

## First remaining inference attacked and exact blocker

The first local missing inference for the former four-remainder branch was whether a forced same-support bypass could stay strict and therefore evade both cross closure and neutral equality. It cannot: the two independent Menger paths plus the four-vertex budget force equality throughout.

The remaining first **global** inference is now sharper:

> **R4-NEUTRAL-ORBIT:** show that a finite orbit of the saturated equality configurations in Lemmas 2--3 must eventually produce a cross-packed transition, a `SIX` state, a directed cycle in an exchanged remainder, or a strict reduction of the globally minimum three-packing.

The important structural data available to that next step are exact, not asymptotic:

- support witness: heavy fan exactly three; two length-three equality bypasses; their two-vertex interiors partition `R`;
- remainder witness: heavy fan exactly three; three length-two equality return paths; their one-vertex interiors are precisely `R\{z}`.

A recurrence proof may therefore work on a finite labelled equality-state graph rather than on arbitrary positive collar lengths.

## Failure checks and nonclaims

- A cross-packed transition is not itself counted as a fourth cycle or a completed two-cycle splice.
- A neutral exchange is not a strict contradiction. The saturated neutral orbit remains unpaid.
- The cycle-supported proof uses the controlling corrected heavy-fan inport logic; the quarantined invalid TCEX invocation from the prior primary report is not reused.
- The path-count equalities use edge lengths: an `R`-internal path of length `ell` has exactly `ell-1` internal remainder vertices.
- The theorem concerns `|R|=4`; it does not replace larger-remainder strict-collar arguments.
- The exact target permits digons. Orientation is used only after the valid minimal-counterexample reduction.
- No computation was used in this proof.
- No full BT4 proof and no novelty claim is made.

## Honest status

`ESSENTIAL_STEP_APPLIED`.

Actual before: four-remainder `NO-SIX` could terminate at a strict same-support bypass/collar, leaving a quantitative coalescence branch.

Actual after: absent a genuine cross-packed transition, every five-witness at `|R|=4` is equality-saturated. Cycle-supported witnesses force two length-three neutral bypasses partitioning the four-vertex remainder; remainder-supported witnesses force three length-two neutral return paths covering it. The entire branch is reduced to a finite saturated-neutral orbit.

BT4 remains OPEN / NOT PROVED.
