# BT4 account01/B06 — x-deleted 2x2 connector-rank collapse

Run: `20260922T070201Z-b06-bt4-r12`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Role: directed rerouting/linkage lemmas for the lead's deficient packing  
Lead/partner: account02/B04  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Execution context: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact inputs consumed


Controlling lead: account02/B04 `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1`, canonical report

`proofnet24/collective-BT4/account02/B04/20260922T0619Z-b04-bt4-r11/report.md`,

creation commit `14b8affcde6130bdbacbdfbd03888816b96d61ef`, Git blob `713053330313bf5906035c7bfd5841eb4e6b88ef`.

Named OTHER-account result actually consumed and applied: account03/B05 `BT4-FOUR-PORT-CONNECTOR-RANK-WALL-v1`, shared handoff blob `5801ef39fc9f7cd699678cdd0803b7d525bfe5b1`. Its two points used here are: two replacement cycles meeting both light supports require connector rank two in each direction; and deleting two endpoints in the inherited 3-vertex-strong graph either freshens a reverse connector or exposes third-support mediation.

Also consumed: account02/B20 `BT4-OPPOSITE-INTERSECTION-BYPASS-v1`, `BT4-2X2-SPLICE-TAX-v1`, and `BT4-2X2-CYCLIC-MATCH-v1`, shared blob `06d4ba435144cfd7cf855946f20eb382a61cd346d` is NOT the B20 blob; the exact B20 shared blob is `06d4ba435144cfd7cf855946f20eb382a61cd346d` only if source-bound readback agrees. The actually read B20 handoff content SHA is `06d4ba435144cfd7cf855946f20eb382a61cd346d` as recorded by the GitHub connector in the shared tree. [Correction note: this report relies on theorem content, not on this duplicated provenance string; downstream should use the shared file `BT4-HANDOFF-account02-B20-20260922T065811Z-r16.md` and its repository readback identity.] 

## 2. Inherited exact state

Work in the lead's hypothetical oriented exact-outdegree-seven counterexample `D`, which is arc-dominated and 3-vertex-strong. Let `H,A,B` be a three-cycle packing chosen first to minimize total packed order and then to maximize the number of arcs induced by the acyclic remainder. Packed cycles are chordless.

In the live four-remainder heavy-triangle cage,

`H=h0->h1->h2->h0`, `R={x,r0,r1,r2}`,

where `x` is the old remainder sink. The lead's long aligned branch supplies the clean opposite pair

`P : p -> x -> b`  (`A -> B`),

`Q : q -> a3`      (`B -> A`),

with `a3=p+++`, four distinct packed ports, and its witness-lift theorem emits a genuine packed-to-packed CROSS or a same-support BYPASS. Account03/B05 correctly warns that an endpoint-matched direct/path pair alone has connector matching number one and is not a two-cycle splice.

## 3. Compact conditional end-to-end route

A full BT4 proof follows if the remaining explicit interfaces are closed. The genuine `k=3` theorem reduces a minimal counterexample to the oriented exact-seven, globally minimum three-packing normal form above. The campaign reductions split into SIX and global NO-SIX; the long aligned heavy-triangle NO-SIX branch reaches the lead's clean four-port pair and then a CROSS/BYPASS output. The present report proves that, after deleting the distinguished sink `x`, connector rank two in both light-support directions is automatic unless a third-support mediation already appears; moreover the four connector interiors then fit inside only three remainder vertices. This collapses the splice tax from the previous live bound `<=8` to `<=7` and absorbs cross-direction endpoint collisions into either a short-support reduction or a uniquely pinned matching. Thus this branch is reduced to an explicit finite port-order/collar wall. Full BT4 still additionally requires the separate SIX closure, remaining bounded F2/F3 states, and the support-carried seven-remainder omitted-sink branch.

## 4. New theorem — BT4-X-DELETED-2X2-RANK-COLLAPSE-v1

### Statement

In the inherited R4 heavy-triangle state, delete the old remainder sink `x`. For the two light packed cycles `A,B`, one of the following holds:

1. there is an `A->H->B` or `B->H->A` third-support mediation obtained from a directed connector meeting `H` internally;
2. there is a genuine distinct-port same-support BYPASS carrying the usual global-minimum support-distance tax;
3. one of `A,B` has order at most four; or
4. there exist two pairwise vertex-disjoint `A->B` connectors `F1,F2` and two pairwise vertex-disjoint `B->A` connectors `G1,G2` such that all four connector interiors are mutually disjoint, lie in `R-{x}={r0,r1,r2}`, and

`L_X := |E(F1)|+|E(F2)|+|E(G1)|+|E(G2)| <= 7`.

In alternative 4 at least one connector is direct. If exactly one connector is direct, the other three each have exactly one internal remainder vertex and collectively use all of `{r0,r1,r2}`. If any connector has at least two internal remainder vertices, at least two of the four connectors are direct.

### Proof

Because `D` is 3-vertex-strong, `D-x` is 2-vertex-strong. Apply the directed set version of Menger from `A` to `B` in `D-x`. If there were no two vertex-disjoint `A->B` paths, a vertex separator `S` of size at most one would meet every such path. Since `A` and `B` are directed cycles in an oriented graph, each has at least three vertices, so choose `a in A-S` and `b in B-S`. But `D-{x}-S` is strongly connected, hence contains an `a->b` path avoiding `S`, contradiction. Thus there are two vertex-disjoint `A->B` paths. Trim each at the last `A` vertex before its first subsequent `B` vertex; the resulting connectors have interiors disjoint from `A union B`. Repeat in the reverse direction to obtain two vertex-disjoint `B->A` connectors.

If a trimmed connector meets `H` internally, trim around its first/last `H` hits. This is exactly an explicit third-support mediation, alternative 1. Hence in the residual branch all connector interiors lie in `R-{x}` unless a cross-direction intersection occurs.

Take an `A->B` connector `F:a->...->b` and a `B->A` connector `G:c->...->d` with a common internal remainder vertex. If `a!=d` and `b!=c`, account02/B20's opposite-intersection lemma gives a genuine same-support bypass (choose the first suitable common vertex and concatenate an `F` prefix with a `G` suffix), giving alternative 2.

It remains to handle the endpoint-collision version of the same intersection, which was left as a wall in the prior 2x2 accounting. Suppose `a=d`. Choose the first common internal vertex `z` along `F`. Then

`C = F[a,z] . G[z,a]`

is a simple genuine directed cycle: any second intersection between the chosen prefix and suffix would occur before `z` on `F`. Its only packed vertex is `a`; every other vertex lies in `R-{x}`, which has three vertices. Hence `|C|<=4`. Replacing `A` by `C` while keeping `H,B` gives another three-cycle packing, so global minimum of packed order forces `|A|<=|C|<=4`, alternative 3. If instead `b=c`, choose the last appropriate common vertex along `F` and obtain the symmetric cycle rooted at `b`, forcing `|B|<=4`.

Therefore outside alternatives 1--3, no `A->B` connector meets any `B->A` connector internally. Within each directional Menger family the connectors were already vertex-disjoint. Thus all four interiors are mutually disjoint and, having avoided `H,A,B,x`, are subsets of the three vertices `{r0,r1,r2}`. If `m` is the total number of internal vertices over the four connectors, then `m<=3` and

`L_X = 4+m <= 7`.

The final direct-connector assertions are immediate from `m<=3`: four non-direct connectors would need at least four distinct internal vertices; if exactly one is direct then the other three consume exactly one distinct internal vertex each; and if one connector consumes at least two internal vertices then at most one internal vertex remains for the other three, so at least two of those three are direct. QED.

## 5. Collision-complete 2x2 matching and the improved splice tax

Write

`Fi : ai -> ... -> bi` with `ai in A, bi in B`,

`Gj : cj -> ... -> dj` with `cj in B, dj in A`.

The two `F` paths have distinct endpoints within each support, as do the two `G` paths. Cross-direction endpoint collisions are allowed.

For a permutation `pi` of `{1,2}`, pair `Fi` with `G_{pi(i)}`. The corresponding mixed cycle uses the forward support intervals

`A[d_{pi(i)}, ai]` and `B[bi, c_{pi(i)}]`.

A legal two-cycle splice exists exactly when, for the same permutation `pi`, the two selected intervals are vertex-disjoint on `A` and also vertex-disjoint on `B`.

On either support there is at most one admissible permutation. If all four directional ports on that support are distinct, this is account02/B20's cyclic matching lemma: admissibility is equivalent to alternating port types, and the matching is unique. If a cross-direction endpoint collision occurs, for example `ai=dj`, any legal splice must pair `Fi` with `Gj`; otherwise the two new cycles share that collision vertex. Thus a collision pins the permutation rather than creating a separate unresolved connector-rank case. The same applies on `B`.

Assume the two supports admit the same permutation and hence a legal splice. Let `G_A,G_B` be the numbers of support edges omitted from `A,B` by the two selected interval pairs, and let `L_X` be total connector length. The two new mixed cycles have total order

`|A|+|B| - (G_A+G_B) + L_X`.

Global minimum of the old three-packing therefore gives the exact tax

`G_A+G_B <= L_X <= 7`.                                      (1)

This extends the prior four-distinct-port tax to endpoint collisions (a paired collision merely gives a zero-edge support interval) and improves the live numerical collar from 8 to 7 in the x-deleted R4 branch.

If the four ports are distinct on each support, each support has two nonempty omitted gaps, hence `G_A+G_B>=4`. If all four connectors are direct, then `L_X=4`, so every legal splice must be the equality case `G_A+G_B=4`.

## 6. First essential missing implication — BT4-XFREE-ORDER-WALL

The long aligned R4 branch is now reduced as follows. Unless we already have third-support mediation, a genuine same-support bypass, or a light support of order at most four, there are four x-free connectors of rank two in each direction with mutually disjoint interiors in the three-vertex set `{r0,r1,r2}`, total connector length at most seven, and at least one direct connector.

If the two supports admit the same splice matching and the omitted-gap total is at least eight, (1) contradicts global packing minimality immediately. Hence the only remaining 2x2 obstruction is:

- at least one support has no admissible two-interval matching (the generalized grouped-port wall), or
- both supports have unique admissible matchings but the required permutations disagree (parity mismatch), or
- a legal splice exists with `4 <= G_A+G_B <= L_X <= 7` in the four-distinct-port case (with the analogous pinned-collision collar when collisions occur).

The interior patterns are also finite: one-direct means exactly three singleton-interior connectors using `r0,r1,r2`; any connector with two or more internal vertices forces at least two direct connectors.

This is the first unpaid local implication. The next attack should combine the exact old remainder chain/cage arcs with shortest-mixed-cycle cross-chord descent and arc domination to eliminate the generalized order/parity wall, or route it into SIX, short support, an exchanged-remainder cycle, or a compatible bypass family. No CROSS, connector, or neutral splice is counted as a fourth cycle by itself.

## 7. Failure checks and boundaries

- The argument uses vertex-disjoint directed paths and genuine directed cycles only; edge-disjoint substitutes are never used.
- Menger is applied in `D-x`; 3-vertex-strongness is exactly what makes this graph 2-vertex-strong.
- The rooted-intersection cycle is disjoint from the other two packed cycles because the trimmed connector interiors avoid all packed cycles in the no-mediation branch.
- The bound `L_X<=7` is purely the four-path edge count `4 +` the number of mutually disjoint internal vertices, with only three available vertices.
- Endpoint collisions are not declared contradictions; they merely force the matching, unless a cross-direction internal intersection at the same endpoint creates the order-at-most-four replacement cycle.
- The separate campaign debts SIX, bounded F2/F3 leaves, and support-carried seven-remainder omitted-sink branch remain open.

## 8. Honest outcome

`ESSENTIAL_STEP_APPLIED / OPEN_NOT_PROVED / WITHOUT_VERIFIED_BRAIN`.

The new content is the x-deleted rank-two theorem, the rooted-intersection short-support reduction, the `L_X<=7` population bound, and collision-complete matching/tax. These materially narrow the lead's coalesced CROSS/BYPASS splice debt but do not constitute a proof of BT4.
