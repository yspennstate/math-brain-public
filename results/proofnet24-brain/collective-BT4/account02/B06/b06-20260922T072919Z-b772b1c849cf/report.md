# account02/B06 BT4 adversarial report — b06-20260922T072919Z-b772b1c849cf

Outcome: `CANDIDATE_REFUTED`  
Repair: `BT4-RANK2-PORT-PARITY-v1`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Directive / control acknowledgment


Initial control main: `392c75947d5d48a716bd6da0b9393c3c1bc308d0`. Start refresh main: `3727d194e85c390fb573ec9a09d626ee2b383ccf`.

## Exact sources consumed and applied

1. Campaign lead account02/B04: `BT4-HANDOFF-account02-B04-20260922T0619Z.md`, Git blob `b0c1c37b1d36fd7cf855946f20eb382a61cd346d`. It keeps the global counterexample route in the exact-seven oriented/minimum-packing framework and records unresolved CROSS/BYPASS splice, SIX, bounded short-support/F2/F3, and seven-remainder support-carried debt.
2. Assigned OTHER-account partner account03/B04: `BT4-R7-PINWHEEL-TRIANGLE-v1`, handoff Git blob `83dabb60e7451dd1b5e83090a73f940c79a8e3f2`, canonical science report commit `911c71843779cb47447c31b4bfdecd5672bea451`, blob `befdd739858f7ce90314392f243c9c3e335297e5`. Applied as the exact reduction of the strict R-supported `|R|=7` saturation branch to the `(3,2,2)` heavy-triangle pinwheel; the already established B06 domination collapse then removes that strict no-neutral R-supported leaf, so this run does not reopen it.
3. Fresh OTHER-account connector input account04/B06: `BT4-HANDOFF-account04-B06-20260922T0725Z.md`, Git blob `47d7e7c2fd312fd647604bf61113c46fd980a237`. It isolates the packed cyclic-order / endpoint-compatibility wall after obtaining bidirectional rank-two connector families with disjoint opposite interiors.
4. During this run, account04/B05 independently published `BT4-BIDIRECTIONAL-RANK2-ORDER-WALL-v1`, handoff Git blob `f553a1086caaea875705c6f8c5d3f268bda1d3c3`, giving the same abstract compatibility criterion. The new contribution here is therefore not claimed as first discovery of that criterion; it is an exact adversarial stress test showing that the bad parity state survives strong local normal-form properties.

## Compact conditional end-to-end route

A genuine counterexample can first be reduced across digons by deleting the two vertices of a digon, using the known `k=3` threshold-five theorem in the remainder, then restoring the digon as the fourth cycle. In the oriented branch, inherit the exact-seven, 3-vertex-strong, arc-dominated, globally minimum three-cycle packing with acyclic remainder. Apply account03/B04's strict-seven-remainder reduction plus the B06 domination collapse to remove the strict R-supported pinwheel. Existing Menger/clean-port machinery then produces bidirectional rank-two connector families or one of the already accepted outputs (third-support mediation, a same-support bypass, SIX, a cyclic exchanged remainder, or a fourth cycle). The first essential unpaid implication is therefore exactly at the packed endpoint order: show that a true minimum counterexample cannot realize `BLOCK` or opposite-parity `ID/SW` states, or convert such a state to an accepted output. The local connector data alone do not do this, as the exact adversary below shows.

## False intermediate statement refuted

`BT4-RANK2-AUTOSPLICE-v0` (false):

> If there are two internally vertex-disjoint `A->B` connectors and two internally vertex-disjoint `B->A` connectors, all four connector interiors are mutually disjoint and all packed endpoints are distinct, then one of the two natural pairings automatically gives two vertex-disjoint mixed directed cycles using the four connectors and forward support segments.

This is false even when all four connectors are single arcs, both support cycles are chordless, the ambient digraph is oriented with minimum outdegree seven, deletion of any at most two vertices leaves it strong, and every arc is dominated.

## Repair: exact port-parity criterion

Let `A,B` be disjoint directed cycles. Let

- `F_i : a_i -> ... -> b_i` be two `A->B` connectors (`i=1,2`),
- `G_j : c_j -> ... -> d_j` be two `B->A` connectors (`j=1,2`),

with all four ports on each support distinct and all connector interiors mutually disjoint and outside `A union B`.

For a pairing permutation `pi`, the canonical mixed cycles are

`Z_i = F_i + B[b_i,c_{pi(i)}] + G_{pi(i)} + A[d_{pi(i)},a_i]`.

On a directed support cycle classify its four labeled ports as follows:

- `ID`: the two forward support segments for the identity pairing are vertex-disjoint;
- `SW`: the two forward support segments for the swapped pairing are vertex-disjoint;
- `BLOCK`: neither pairing gives disjoint forward segments.

For fixed labels, among the six cyclic orders modulo rotation exactly one is `ID`, exactly one is `SW`, and four are `BLOCK`.

**Lemma (`BT4-RANK2-PORT-PARITY-v1`).** Two vertex-disjoint canonical mixed cycles using all four chosen connectors exist iff both supports are non-`BLOCK` and their preferred parities agree. If both are `ID`, use `(F1,G1)` and `(F2,G2)`; if both are `SW`, use `(F1,G2)` and `(F2,G1)`.

**Proof.** Connector interiors are mutually disjoint and avoid the supports, so the only possible intersections between the two canonical mixed cycles occur on `A` or `B`. For either pairing, disjointness is therefore equivalent to the corresponding two forward support segments being disjoint on both supports. With four distinct labeled ports on one directed cycle, exhaustive cyclic-order analysis gives exactly one identity-compatible order, one swap-compatible order, and four blocked orders. Hence one common pairing works on both supports exactly when both are nonblocked and prefer the same pairing. The deterministic checker exhausts all `6 x 6 = 36` support-order pairs and confirms that exactly two order pairs admit a canonical two-splice.

## Exact parity-mismatch adversary

Take chordless directed supports

`A=(0,1,2,3)=(d1,a1,d2,a2)` and `B=(4,5,6,7)=(b1,c2,b2,c1)`.

Use direct connector arcs

`F1=1->4`, `F2=3->6`, `G1=7->0`, `G2=5->2`.

Thus `A` is `ID`-preferred while `B` is `SW`-preferred. For the identity pairing, the two `A` segments are disjoint but the two `B` segments intersect. For the swap pairing, the two `B` segments are disjoint but the two `A` segments intersect. No canonical two-splice exists from these four connectors.

The archived exact ambient digraph has 19 vertices and 167 arcs. It is oriented, has outdegree vector

`(8,7,7,8,10,10,9,9,10,9,8,9,7,7,9,9,11,12,8)`,

so `delta+=7` and `Delta+=12`; deletion of any at most two vertices leaves it strongly connected; every arc has a common predecessor; and both designated four-cycles are chordless. This shows that orientation, exact threshold, substantial outdegree asymmetry, 3-vertex-strongness, domination, endpoint distinctness, disjoint connector interiors, and chordless supports do **not** force compatible port parity.

The graph is deliberately **not** a BT4 counterexample and is not claimed to realize the global minimum-packing/no-four-pack hypotheses. The checker exhibits four vertex-disjoint directed triangles:

`(0,1,4)`, `(2,3,6)`, `(5,8,9)`, `(7,10,13)`.

Therefore the valid repair is global: a true proof must use the minimum-packing/no-four-pack/exchange conditions to eliminate `BLOCK` and parity mismatch, rather than strengthen the local linkage statement again.

## Digon boundary adversary

On vertices `v0,...,v9`, start with complete bidirected `K10` and remove only arcs `v0->v6`, `v0->v7`, `v1->v7`. The outdegree vector is

`(7,8,9,9,9,9,9,9,9,9)`.

Choose the digon `v8 <-> v9`. Deleting those two vertices leaves surviving outdegrees

`(5,6,7,7,7,7,7,7)`.

Thus minimum outdegree drops from seven to exactly five in a highly asymmetric example. Any reduction claiming digon deletion preserves threshold six (or seven) is false. The source-valid reduction is precisely deletion of the digon, application of the known `k=3` theorem at threshold five, and restoration of the digon.

## Decisive computation and exact artifacts

The deterministic checker was executed with a native Python interpreter and returned exit code zero with empty stderr. It verifies:

- all 36 pairs of cyclic port orders and the exact `ID/SW/BLOCK = 1/1/4` classification per support;
- exactly two of the 36 order pairs admit a canonical two-splice;
- the 19-vertex adversary's orientation, chordless supports, exact direct connectors, outdegrees, 3-vertex-strongness under every deletion of at most two vertices, domination of every arc, parity mismatch, and explicit four-pack;
- the asymmetric digon deletion threshold-five boundary.

Executed checker SHA-256: `a4de4c77d4a92ef2301ea59fd33cc131ecd9d0a156930776c314f221102e0314` (7256 bytes).  
Executed output SHA-256: `af9030a975fc291af70950b2546e44d47581345c16e2134c465e332df10ddcd6` (1899 bytes).  
Git readback checker blob: `dae0330fd61ac80c1a02a622add59ebb9da919b6`.  
Git readback output blob: `3058ccfea842f4a4530a9c454e4464f69340e17f`.

## Before / after / first unpaid implication

Before this run, the bidirectional rank-two machinery left “cyclic order / endpoint compatibility” as a qualitative wall, and it was tempting to hope that the strong local normal-form assumptions automatically made the two linkages splice-compatible. After this run, that hope is refuted by an exact strong adversary and the wall is compressed to an exact finite state: each support is `ID`, `SW`, or `BLOCK`, and canonical two-splicing succeeds exactly for matching nonblocked parity.

The first essential missing implication is now `BT4-BIDIR-ORDER-WALL-GLOBAL-CLOSE-v1`:

> In a genuine globally minimum no-four-pack counterexample state carrying the bidirectional rank-two interface, prove that a `BLOCK` support or an `ID/SW` parity mismatch forces a strict packing decrease, cyclic exchanged remainder, same-support taxed bypass, third-support mediation, SIX, a fresh connector changing the parity class, or a fourth disjoint directed cycle.

This is narrower than trying to improve Menger rank or connector interior disjointness; the exact adversary shows those local improvements alone cannot pay the debt.

## Failures / boundaries

A previously referenced newer internal account03/B04 blob was not directly retrievable through the authorized repository surface in this invocation, so no unverified content from it was promoted. The latest exposed named-partner shared handoff `83dabb60...` was used instead. Concurrent account04/B05 work independently reached the abstract order-wall criterion during this invocation; this report therefore claims only the exact adversarial stress test and finite-state compression, not priority for the abstract criterion. BT4 remains open; this is not a full proof candidate.

## Runtime / inventory / privacy

Own-account exposed managed inventory: 20/20 managed tasks enabled and hourly-valid; B06 role-aligned; quiet delivery preserved; zero scheduler mutations; no deficit requiring B20 repair. Scoped privacy/secret review: no credentials, scheduler identifiers, machine paths, raw transcripts, benchmark gold, unrelated private data, email/Drive material, public posting, or permission changes are present in the artifacts.

Model self-report: `GPT-5.6 Sol`.  
Requested effort: `maximum actually supported`.  
Configured effort: `UNKNOWN_NOT_EXPOSED`.  
Known/self-observed effort: `UNKNOWN_NOT_EXPOSED`.  
Provider reasoning-token usage: `null / NOT_EXPOSED`.  
Provider thinking-time usage: `null / NOT_EXPOSED`.  
Provider total-token usage: `null / NOT_EXPOSED`.
