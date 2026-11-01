# BT4 fleet02/B05 — aligned consecutive-triple lock is absorbed by the canonical source pivot

Run: `20260922T062431Z-b05-bt4-b744a134`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-R4-ALIGNED-TRIPLE-ABSORPTION-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Parent target: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and current source boundary

Target: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs/digons are allowed in the source statement. The oriented exact-outdegree-seven model below is only the inherited minimum-counterexample normal form after the genuine digon reduction.

Fresh owner controls were read from `yspennstate/math-research-brain` on current `main`; OWNER revision is `2026-09-22.2`, the active directive is the collective open-problems programme, B05 remains BT4, and old brain-installation/benchmark work is explicitly stopped. Control Git objects used this run: AGENTS `94387098453b9f4a9b10179183f6f6ec780fd987`; README/OWNER `3d4a9372c87802ab734141a3374d04c8823372e3`; fleet `e647d5d2479749f80ce7bb4862bee0f28513c7d9`; roles `ed17ecc94f76720c0345b3e32249b791b20ec611`; PROTOCOL `83a9268bf5287ca203e4be69a79e25382397bca7`; ORDER `a70e03208ae00795ca7c6cdf9b7dbce854347138`; TARGETS `a8cafa98cdb074ed15d0e214f8f54ee514c500df`. Whole-file native SHA-256 values are not independently exposed here, so immutable Git object identities are recorded instead of invented hashes.

A fresh public-source check on 22 September 2026 still finds Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (13 August 2026), stating that the genuine conjecture remains unresolved for all `k>=4`; their theorem permits one reversed arc per cycle. Nothing below counts such a near-directed cycle.

## Exact team inputs actually consumed

### Campaign lead

Latest complete fleet02/B04 run actually read: `20260922T051543Z-b04-bt4-r11`, report blob `9f1ec8ca9ab3f2737b9dddf98389826f5b926933`, candidate “lexicographic heavy-triangle port separation.” I use its exact four-remainder heavy-triangle cage and, in particular, its aligned-port alternative:

- `H=h0->h1->h2->h0`, `R={x,r0,r1,r2}`;
- saturation triangles `Ti=hi->ri->x->hi`;
- the old remainder is the exact five-edge chain `r0->r1->r2`, together with `ri->x` for each i;
- `r0->h1`, `r1->h2`, `r2->h0`, and the neutral-exchange exclusions from the lead;
- a `T0` light witness `p` on a light cycle `A` satisfies `p->h0,r0,x` and `N+(x) intersect A={p+,p++}`;
- if `h1` is heavy on the same `A`, then either a clean four-distinct-port opposite-light-cross pair already exists, or the only remaining aligned lock is

`N+(h1) intersect A = {p,p+,p++}`.                    (L)

### Named OTHER-account partner

Newest complete assigned partner result actually read: fleet03/B06 run `20260922T052316Z-fleet03-B06-BT4-r15`, candidate `BT4-R4-F3-MAJORITY-CROSS-v1`, report blob `697fde372dee5fec64d03923523d13fc6edcab7a`.

It proves, in the arc-maximal triangular F3 source-pivot state, that the two-vertex saturation-witness cover forces a concrete short light-to-light cross, with interior either empty or one remainder vertex; when both witnesses repeat it gives opposite crosses with disjoint interiors. Its complete exact-seven certificate also refutes the stronger shortcut that the cross must always be direct. I apply both pieces below: triangular F3 no longer carries a “find a cross” debt, and I do **not** promote any downstream cross to a direct edge.

### Canonical low-fan source-pivot classification

I also use fleet04/B04 run `20260922T051604Z-fleet04-B04-BT4-r14`, candidate `BT4-R4-ARCMAX-TRIANGLE-COLLAPSE-v1`, report blob `2f802a03755394931009175d7b6a5f94b0b2b084`. Its inherited post-source-pivot classification says that, after excluding an immediate SIX output, the already-proved fan-at-least-three return-cross output, and a second neutral packed pivot, the only surviving `|R|=4` low-fan states are:

- `F2-RONLY`: the freed source vertex has remainder outdegree two and **no direct heavy/other-light inport**;
- `F3-SINGLEPORT`: it has remainder outdegree three and **no heavy-cycle inport**.

This exact no-heavy-inport clause is the contradiction used below.

My immediately preceding B05 result, report blob `739678d2c1387571ab1190a53530d1211a2ad1cf`, handled a different source-triangle lock by a two-cycle equality transport. It is preserved but not re-run here; the mechanism below is global-minimum comparison plus the canonical source-pivot classification.

## Compact conditional end-to-end route

Assume BT4 false and enter the inherited oriented, exact-outdegree-seven, arc-dominated, 3-vertex-strong minimum-counterexample normal form. Choose three disjoint chordless directed cycles with minimum total packed order and then maximum induced-remainder arc count. The remainder is acyclic.

In global-NO-SIX with four remainder vertices, the lead's heavy-triangle cage reduces the aligned `T0` branch to either a clean four-port opposite-cross pair or the exact consecutive-triple lock (L); the nonaligned support-location branch remains separate. The theorem below removes (L) as an independent terminal state. The canonical neutral source pivot either immediately enters one of the already-existing SIX/cross/equality-pivot interfaces, or it would have to be F2/F3, which is impossible because the lock itself supplies a heavy inport to the freed vertex.

Separately, when the canonical triangular F3 branch arises elsewhere, the named partner `BT4-R4-F3-MAJORITY-CROSS-v1` supplies the required short cross already. Thus the common unpaid step after this run is a **disjoint splice**, not extraction of another cross and not repair of the aligned consecutive triple.

## Theorem — `BT4-R4-ALIGNED-TRIPLE-ABSORPTION-v1`

Work in the lead's exact heavy-triangle cage and assume the aligned lock (L). Then:

1. the light support `A` is forced to be a directed triangle;
2. the canonical neutral source pivot on `A` frees `q=p+` and gives a direct heavy-cycle inport `h1->q`;
3. consequently the pivot cannot survive as either `F2-RONLY` or `F3-SINGLEPORT`;
4. hence the aligned consecutive-triple lock necessarily exits through an already-existing source-pivot interface: a cyclic exchanged remainder/fourth cycle, SIX, the fan-at-least-three return-cross interface, or a second neutral packed pivot.

In particular the exact consecutive-triple alternative in the lead's aligned branch is not a new terminal obstruction.

### Proof of (1): two disjoint triangles spend the lock

Because `H=h0->h1->h2->h0`, the lock gives `h1->p`, and the `T0` witness gives `p->h0`. Therefore

`C = h0 -> h1 -> p -> h0`

is a genuine directed triangle.

The lead's saturation triangle

`T2 = h2 -> r2 -> x -> h2`

is disjoint from `C`: `C` uses `{h0,h1,p}`, while `T2` uses `{h2,r2,x}`. Let `B` denote the other light packed cycle. Then `C`, `T2`, and `B` are three pairwise vertex-disjoint genuinely directed cycles.

Their total packed order is

`3 + 3 + |B| = 6+|B|`.

The original packing `(H,A,B)` has total packed order

`3 + |A| + |B|`.

Global minimum of the original three-cycle packing therefore gives

`3+|A|+|B| <= 6+|B|`,

so `|A|<=3`. The inherited minimum counterexample is oriented, hence contains no directed digon; every directed cycle has order at least three. Thus

`|A|=3`.                                                   (1)

Write the now-forced triangle as

`A = p -> p+ -> p++ -> p`.

This is the key new collapse: the seemingly unbounded consecutive heavy-fan lock can occur only on a three-cycle.

### Proof of (2): the lock gives a forbidden heavy inport after the neutral pivot

The sink-fan equality already gives

`p->x`, `x->p+`, `x->p++`.

Since `A` is a triangle, the canonical size-neutral source pivot is simply

`A* = p -> x -> p++ -> p`.                               (2)

It consumes the old remainder sink `x`, frees

`q=p+`,

and changes the remainder from `{x,r0,r1,r2}` to

`R*={q,r0,r1,r2}`.

The pivot preserves packed order. If `D[R*]` contains a directed cycle, that cycle together with `H,A*,B` is already the desired fourth cycle, so in a counterexample `R*` is acyclic and `(H,A*,B)` is another globally minimum three-cycle packing.

But the exact lock (L) contains the arc

`h1 -> p+ = q`.                                            (3)

Thus the freed source vertex has a **direct inport from the heavy packed cycle H**.

### Proof of (3)--(4): canonical low-fan survival is impossible

Apply the inherited `|R|=4` source-pivot split to `(H,A*,B)`.

If one of the split's earlier outputs occurs, then the lock has already entered one of the campaign's existing interfaces: immediate SIX, a fan-at-least-three return cross, a second neutral packed pivot, or a cyclic exchanged remainder as handled above.

Suppose instead that none occurs. The fleet04/B04 classification says the only surviving low-fan states are `F2-RONLY` or `F3-SINGLEPORT`.

- `F2-RONLY` has no direct inport to q from either the heavy cycle or the other light cycle.
- `F3-SINGLEPORT` has no heavy-cycle inport to q.

Both conclusions contradict the explicit heavy inport (3). Therefore neither surviving state is possible. This proves that the aligned consecutive-triple lock must exit through an already-existing source-pivot interface and cannot remain a terminal branch. QED.

## How the named fleet03/B06 result is applied

The theorem above eliminates the exact aligned triple **before** it can become a new F2/F3 terminal state. This does not eliminate triangular F3 states arising from the separate canonical low-fan branch. For those, the named partner's `BT4-R4-F3-MAJORITY-CROSS-v1` is now taken as the exact source-bound input: the F3 witness cover already yields a light-to-light cross of length one or two, and in the overlap case an internally-disjoint opposite pair.

This matters to the present B05 assignment because the reversed-arc relaxation cannot be repaired merely by saying “a cross exists.” The partner's exact full-graph certificate proves that one remainder vertex may genuinely be required, even under exact outdegree seven, arc domination, 3-vertex-strongness and the relevant acyclicity conditions. Therefore the common splice obligation after this run is formulated for a **bounded short cross with possible one-remainder interior**, not for a fictitious direct edge. This avoids reintroducing exactly the disjointness error that the B05 assignment is meant to remove.

## Corollary — updated aligned heavy-cage branch

Under the lead's Lemma 3.1 hypotheses, an aligned `T0` witness no longer leaves “clean four-port pair OR exact consecutive triple” as two terminal alternatives.

- If the clean four-port pair occurs, send it to the corrected third-port/segment splice machinery.
- If the exact triple occurs, the theorem above forces an already-existing source-pivot output; it is not a new lock.

Hence a genuinely terminal heavy-cage state with no immediate source-pivot output must lie in the lead's **support-location lock**: every available `T0` light witness is on the light support different from the heavy target of `h1`.

This is a strict reduction of the lead's branch tree.

## First exact unpaid implication after the reduction

`BT4-R4-LOCATION-OR-SHORT-CROSS-SPLICE-v1`:

> In the lexicographic `|R|=4` global-NO-SIX state, assume either (a) the lead's support-location lock, in which every `T0` light witness lies on the light support different from the heavy target of `h1`, or (b) one of the already-produced clean/short light-to-light cross interfaces, including the bounded cross from fleet03/B06. Use the two heavy-fan escape transitions, the exact five-edge cage remainders and the corrected third-port/segment machinery to force two vertex-disjoint replacement directed cycles, a strict smaller three-cycle packing, a directed cycle in an exchanged remainder, SIX, or a fourth directed cycle.

The important reduction is that the aligned consecutive-triple case itself no longer needs to be solved inside this implication.

## Failure checks and nonclaims

- The proof does not claim that a short cross is a direct edge. The named partner's exact certificate rules out that shortcut under the available local hypotheses.
- An opposite cross pair is not counted as two vertex-disjoint replacement cycles.
- The theorem uses genuine directed triangles only; no one-reversed-arc cycle or edge-disjoint surrogate appears.
- The neutral pivot is size-neutral, not itself a fourth cycle.
- The separate SIX interface remains unpaid.
- The lead's nonaligned support-location lock remains unpaid.
- The clean-cross third-port splice remains unpaid.
- The `|R|=7` triangle-pinwheel/support-carried omitted-sink branch remains separate.
- No finite computation is used to prove the theorem. The named partner's finite certificate is used only to forbid an invalid strengthening to “direct cross.”

## Before / after

Before this run, the lead's aligned heavy-triangle branch still had one exact unbounded-looking terminal alternative `N+(h1)∩A={p,p+,p++}` in addition to the clean four-port pair.

After this run, global minimum forces that support to have order exactly three; the canonical neutral source pivot then frees `p+`, while the lock itself supplies `h1->p+`. The complete low-fan survival classification forbids precisely that heavy inport. Therefore the triple alternative is absorbed into previously existing source-pivot outputs and disappears as an independent terminal branch.

Target-level status is unchanged: BT4 is still open. Mechanism-level status advances: one explicit lead terminal is removed, and the named partner removes cross-extraction from triangular F3, leaving a common genuine disjoint-splice problem.

## Operational record

Fleet02's exposed managed inventory showed all twenty B01--B20 assignments present, enabled on hourly cadences and quiet; B05 is role-aligned. No scheduler mutation was performed and no deficit requiring B20 action was observed.

Model self-report: `GPT-5.6 Sol`. Requested reasoning effort: `maximum actually supported`. Configured reasoning effort: `UNKNOWN / not exposed`. Known effective effort: `UNKNOWN`. Exposed provider reasoning tokens/time: `null / not exposed`. Brain status: `WITHOUT_VERIFIED_BRAIN`.

Elapsed work is recorded separately in the final run receipt; it is UTC wall/tool elapsed execution, not pure thinking.
