# BT4 B06 attempt — H-mediated balanced-F2 domination pivot and saturation-certificate adversary

Run: `b06-20260922T102950Z-7c94e1ad`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Account/slot: `account02/B06`  
Outcome: `ESSENTIAL_STEP_APPLIED` with local `CANDIDATE_REFUTED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and controlling sources


Latest complete lead actually consumed: account02/B04 run `20260922T101701Z-b04-bt4-r11`, report blob `180efea97f9e427143959c7274a9bd2bba810021`, candidate `BT4-TRACE-TRANSVERSAL-ESCAPE-v1`. Its new theorem proves that, in the clean primitive-trace branch and absent recognized exits, 3-vertex-strongness forces an off-trace cross-support connector; the remaining clean-state debt is connector rank/order (`BT4-OFF-TRACE-RANK-SPLICE-v1`).

Named OTHER-account / assigned-partner result actually consumed: account03/B04 run `account03-b04-20260922t095155z-r11` in `yspennstate/math-open-problems`, report blob `06c33bc5ad285dc15cbd80945534ce87c485e93f`, candidate `BT4-R4-HMED-TWOFAN-NEUTRAL-PIVOT-v1`. In the aligned four-remainder heavy-triangle cage it proves that H mediation forces a neutral packing `(T0,A,B*)`; for the freed vertex `z=q+`, after excluding SIX and a new heavy fan, the only residual profile is `(2,2,1,2)` on `(T0,A,B*,R*)`.

Also consumed as compatible current context: account04/B05 shared handoff `account04-B05-20260922T100847Z-gap-signature-handoff.md`, blob `e699a87b99e0c9c5d7ac272042846d48f977d73d`, candidate family `ONE-FRESH-GAP-INVARIANCE / TWO-FRESH-PARITY-BREAK`; it warns that one fresh cross cannot change the surviving 3-cycle monodromy and that two usable complementary representatives must be obtained with their dependence controlled.

No peer outcome label is promoted to target truth.

## 2. Compact conditional end-to-end state

Assume BT4 false. The inherited campaign reductions first dispose of digons using the genuine k=3 threshold-five theorem, then work in the oriented exact-seven, arc-dominated, 3-vertex-strong normal form with a globally minimum three-cycle packing and acyclic remainder. The current lead closes the pure primitive-trace existence wall: in the clean heavy-triangle/four-port branch, no-exit continuation forces an off-trace connector. The partner H-mediated branch instead reaches a neutral four-remainder state whose only unresolved non-SIX/non-heavy profile is the exact balanced freed-vertex pattern `(2,2,1,2)`.

The theorem below shows that this balanced F2 state cannot be terminal: arc domination forces a new inport from one of the two non-support packed cycles, minimum packing localizes its two-fan exactly, and a second neutral pivot follows. One T0-dominator position (`c=r0`) immediately creates the fourth cycle. Thus a complete proof would follow after (i) closing the resulting neutral-pivot orbit in the remaining `c in A union {h0,x}` positions, (ii) paying the lead's off-trace connector-rank/order splice, and (iii) closing the still separate SIX, remaining bounded F2/F3, and seven-remainder branches.

## 3. Applied partner state

Use the partner's notation. The neutral packing is `(T0,A,B*)`, with

`T0 = h0 -> r0 -> x -> h0`,

`B* = q -> h1 -> q++ -> B[q++,q]`,

and freed remainder vertex `z=q+`. The new remainder is

`R*={h2,r1,r2,z}`.

The partner proves that, in the balanced residual after excluding SIX/new-heavy alternatives,

- `|N+(z) cap T0|=2`,
- `|N+(z) cap A|=2`,
- `|N+(z) cap B*|=1`, namely the old support-successor `z->q++`,
- `d^+_{R*}(z)=2`,
- `z` is incident in either direction with at most two of `{h2,r1,r2}`.

Since the last two bullets hold simultaneously, exactly two remainder incidences are outgoing from `z`, the third remainder vertex is nonadjacent to `z`, and **no vertex of `R*-{z}` points to `z`**.

The old packed cycle `B` was chordless. Hence among old `B-{z}`, only the predecessor `q` is an in-neighbor of `z`, while `z->q++`; all other old-B vertices are nonadjacent to `z`. The new vertex `h1` satisfies `h1->z`, and the new packed cycle has `q->h1`, so orientation forbids `h1->q`.

## 4. New theorem — `BT4-R4-HMED-F2-DOMINATION-PIVOT-v1`

**Theorem.** In the exact partner state above, assume the balanced profile `(2,2,1,2)`. Then there exists `c in V(T0) union V(A)` such that `c->q` and `c->z`. If `C` is the packed cycle among `{T0,A}` containing `c`, then

`N+(z) cap C = {c+,c++}`,

and

`C' = c -> z -> c++ -> C[c++,c]`

is a directed cycle of exactly `|C|` vertices. Replacing `C` by `C'` gives another globally minimum three-cycle packing and frees `c+`. If its exchanged remainder is cyclic, BT4 is already proved in this state; otherwise the balanced F2 obstruction necessarily propagates by a genuine neutral pivot. Moreover `c=r0` is impossible in a BT4 counterexample because that pivot frees `x`, after which the exchanged remainder contains the saturation triangle `h2->r2->x->h2`.

**Proof.** The arc `q->z` is an old support arc of `B`. By inherited arc domination it has a common predecessor `c` with

`c->q` and `c->z`.                                                   (1)

No vertex of `R*-{z}` can be `c`, because none points to `z` in the balanced profile. No vertex of `B*` can be `c`: among `B*`, only `q` and `h1` point to `z`; `q` cannot dominate its own outgoing arc, while `q->h1` forbids `h1->q`; every other old-B vertex is nonadjacent to `z` by old chordlessness. Therefore

`c in V(T0) union V(A)`.                                             (2)

Let `C` be that support. The balanced profile gives exactly two outneighbors of `z` on `C`. For any `y in N+(z) cap C`, the directed cycle

`c -> z -> y -> C[y,c]`

is disjoint from the other two packed cycles. If `d_C(y,c)` is the positive forward distance from `y` to `c`, its order is `2+d_C(y,c)`. Global minimum of packed total order gives

`2+d_C(y,c) >= |C|`.                                                (3)

Because `c->z` and the digraph is oriented, `y != c`. Writing `y=c^{+k}`, (3) is equivalent to `k<=2`. Thus every target lies in `{c+,c++}`. There are exactly two targets, hence

`N+(z) cap C={c+,c++}`.                                              (4)

Using `c++` gives

`C'=c->z->c++->C[c++,c]`,

whose order is exactly `|C|`. It replaces `C`, consumes `z`, and frees `c+`; the other two packed cycles are untouched. If the new remainder contains a directed cycle, that cycle together with the new three-packing is a fourth disjoint cycle; otherwise we have another minimum packing and a forced neutral continuation.

Finally, if `C=T0` and `c=r0`, then cyclic order on `T0=h0 r0 x h0` gives `c+=x` and `c++=h0`; the neutral replacement is `r0->z->h0->r0`, freeing `x`. The new remainder contains `{h2,r2,x}` and the inherited saturation triangle `h2->r2->x->h2`, immediately producing the fourth cycle. Therefore the `c=r0` dominator location is impossible in a counterexample. QED.

This theorem pays a concrete part of the partner's `BT4-R4-HMED-FREED-QPLUS-CLOSE-v1`: the balanced F2 profile is not a static leaf; it is forced into another equal-size pivot, and one of the three T0 inport positions is already fatal.

## 5. Materially different global mechanism — arc-maximal saturation certificate

The preceding several B06 runs concentrated on local collars/ports. This run also changed mechanism and audited the global saturation route.

**Lemma (`BT4-ARCMAX-DAG-CERTIFICATE-v1`).** Suppose BT4 is false and choose, on a fixed vertex set, a counterexample `D` maximal under addition of legal directed arcs. By the standard digon reduction, `D` is oriented. For every missing ordered arc `u->v`, there exist three vertex-disjoint directed cycles `Q1,Q2,Q3` in `D` and a directed path `P:v->u` in `D`, all four objects mutually vertex-disjoint except for the endpoints internal to `P`, such that

`D - (V(Q1) union V(Q2) union V(Q3))`

is acyclic and contains `P`.

**Proof.** `D+uv` is not a counterexample by arc maximality, so it has four vertex-disjoint directed cycles. `D` itself has no such four-pack, so exactly one of those cycles uses the newly added arc `uv`. Delete `uv` from that cycle; what remains is a directed `v->u` path `P` in `D`, disjoint from the other three cycles `Q1,Q2,Q3`. If the complement of those three cycles contained any directed cycle in `D`, it would already be a fourth cycle disjoint from `Q1,Q2,Q3`, contradiction. Thus the complement is a DAG containing `P`. QED.

For a nonadjacent unordered pair `{u,v}`, both ordered arcs are missing, so the lemma supplies directional certificates in both directions, possibly against different three-packings/DAG complements. This is a valid alternate global normal form. It must **not** be silently combined with the exact-seven bookkeeping normal form: arc-maximizing a counterexample generally raises outdegrees and can change the local minimum-packing geometry. Any future use must include an explicit transfer/alignment argument.

## 6. False strengthening refuted in the same run

The tempting local strengthening

`BT4-ARCMAX-TRIANGLE-CERT-v0`: "under the strong local normal-form conditions, the new-arc cycle in a missing-arc certificate may be taken to be a triangle"

is false. The exact checker contains a 19-vertex oriented near-tournament with one nonadjacent pair `{1,17}`, 170 arcs, minimum outdegree 7, maximum outdegree 12, outdegree vector

`(10,11,9,11,10,10,9,12,7,8,7,9,7,9,11,7,7,7,9)`.

It remains strongly connected after deletion of any at most two vertices, and every arc is dominated by a common predecessor. Nevertheless the shortest directed return from `17` to `1` has three edges:

`17 -> 2 -> 5 -> 1`.

There is no two-edge `17->w->1` return. After adding the missing arc `1->17`, the new arc lies on the directed 4-cycle

`1 -> 17 -> 2 -> 5 -> 1`,

which is vertex-disjoint from the directed triangles

`0->3->6->0`, `4->8->7->4`, `9->11->10->9`.

Thus a certificate of exactly the type used by the saturation lemma need not triangle-localize under orientation, minimum outdegree seven, 3-vertex-strongness and arc domination. The correct repair is the arbitrary directed-path certificate in `BT4-ARCMAX-DAG-CERTIFICATE-v1`.

This 19-vertex graph is intentionally **not** a BT4 counterexample; the checker exhibits the base four-pack `(0,3,1)`, `(2,5,4)`, `(6,9,7)`, `(8,11,10)`. Its role is only to refute the unjustified local path-length inference while satisfying the stated local hypotheses.

## 7. Digon sharpness adversary

A separate 12-vertex highly asymmetric digraph starts from the complete bidirected loopless digraph and deletes only `0->8,0->9,0->10,0->11`. Its outdegree vector is

`(7,11,11,11,11,11,11,11,11,11,11,11)`.

The pair `1<->2` is a digon. Deleting vertices `1,2` leaves outdegrees

`(5,9,9,9,9,9,9,9,9,9)`

on the survivors. Hence the standard digon reduction is sharp at five: deleting a digon from a minimum-outdegree-seven instance cannot in general preserve threshold six or seven. The valid reduction is exactly the known k=3 threshold-five theorem plus the deleted digon as the fourth cycle.

## 8. Computation and reproducibility

The deterministic checker was executed in this invocation and returned `PASS`.

- checker creation commit: `75038608223fef5b38b3dcc818308a984693dc2e`
- checker Git blob after readback: `f94be02ffe08f61f1c69a5dda96fc7eb21af59af`
- executed checker SHA-256: `8a384ca692c65c58daa8fe662755a388b97cb22353853c6caa8243b13288ad8b`
- output creation commit: `650abba9e12ef3bf941c0e9efe403b27904025e0`
- output Git blob after readback: `5c553b86e88b5eca6f4e2967355447b7ee751c29`
- output SHA-256 including trailing newline: `ae041519ae304a904cc122e468bcf22300059fb6fe8048858d01186d0bd8abfd`

The checker verifies the entire explicit 19-vertex arc set, orientation except for the single missing unordered pair, the stated degree vector, strong connectivity after every deletion of at most two vertices, every-arc domination, shortest return distance three, the augmented four-cycle certificate plus three disjoint triangles, the explicit base four-pack, the cycle-distance localization used in Section 4 for cycle lengths 3 through 30, and the 12-vertex digon boundary.

## 9. First essential missing implication

The first branch-specific debt created by this run is

`BT4-HMED-F2-NEUTRAL-ORBIT-CLOSE-v1`:

> In the partner's balanced `(2,2,1,2)` H-mediated state, the domination pivot above has dominator `c in A union {h0,x}` after the fatal `c=r0` subcase is removed. Prove that repeated source-valid neutral pivots cannot form a closed orbit without producing SIX/new-heavy, a strict smaller packing, a cyclic exchanged remainder, an off-trace/order-breaking connector of sufficient rank, or a fourth disjoint directed cycle.

This debt is narrower than the partner's previous balanced-F2 leaf: existence of a next pivot is now proved. Independently, the lead's `BT4-OFF-TRACE-RANK-SPLICE-v1`, the broader SIX branch, other bounded F2/F3 states, and seven-remainder support-carried states remain open.

## 10. Operational / privacy status

Execution context stayed `WITHOUT_VERIFIED_BRAIN`: authenticated source retrieval occurred, but no genuine authenticated brain retrieval/context receiver use occurred. No installation/benchmark work, benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive, public posting, paid API/model/Codex, remote workflow, or permission bypass was used.

Model self-report: `GPT-5.6 Sol`. Requested reasoning effort: `maximum actually supported`. Configured effort: `UNKNOWN_NOT_EXPOSED`. Known/self-observed effort: `UNKNOWN_NOT_EXPOSED`. Provider reasoning tokens, provider thinking time, and total-token usage: `null / NOT_EXPOSED`.

Own-account managed inventory inspection found 20/20 B01--B20 tasks enabled and hourly-valid, B06 role aligned, quiet delivery preserved, and no deficit requiring B20 action. No scheduler mutation was made.
