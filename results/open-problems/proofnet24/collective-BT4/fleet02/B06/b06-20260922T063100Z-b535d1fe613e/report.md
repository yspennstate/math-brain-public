# BT4 fleet02/B06 — seven-remainder pinwheel domination collapse

Run: `b06-20260922T063100Z-b535d1fe613e`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Role: fleet02/B06 exact adversaries and repair  
Outcome: `ESSENTIAL_STEP_APPLIED` with local `CANDIDATE_REFUTED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`  
Parent target: `OPEN_NOT_PROVED`

## Source-exact target and control boundary

Target: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are allowed in the source problem, so directed digons count.


The exact latest complete campaign-lead state read during this invocation is fleet02/B04 run `20260922T0619Z-b04-bt4-r11`, report path `proofnet24/collective-BT4/fleet02/B04/20260922T0619Z-b04-bt4-r11/report.md`, Git blob `713053330313bf5906035c7bfd5841eb4e6b88ef`. It retains the oriented exact-seven, arc-dominated, 3-vertex-strong minimum-counterexample normal form, a globally minimum-total three-cycle packing with lexicographic remainder refinement, and identifies as still open the global SIX/short-support closures, four-port coalescence, and the seven-remainder triangle-pinwheel/support-carried omitted-sink branches.

The newest completed named-partner state read is fleet03/B04 run `b04-20260922t055204z-r11`, corrected candidate `BT4-HT-PORT-PATH-UPGRADE-v2`, report path `proofnet24/collective-BT4/fleet03/B04/b04-20260922t055204z-r11/report-v2.md`, Git blob `5c0bcd93ccb8be7137d1edb1c37d9f12cf5968dd`. Its corrected heavy-triangle work is compatible with the lead and keeps neutral exchanges as explicit outcomes rather than silently discarding equality.

The named OTHER-account theorem actually attacked here is the same partner's earlier `BT4-R7-PINWHEEL-TRIANGLE-v1`, run `20260922T044803Z-fleet03-B04-bt4-r11`, scientific commit `911c71843779cb47447c31b4bfdecd5672bea451`, report blob `befdd739858f7ce90314392f243c9c3e335297e5`. In its global-NO-SIX, no-cross, no-neutral hard branch with `|R|=7`, a strict R-supported five-witness collapses to the exact geometry below.

## Compact conditional end-to-end route

Assume BT4 false and enter the inherited minimum-counterexample normal form. Deleting a digon leaves minimum outdegree at least five, so the genuine k=3 theorem removes digons; retaining seven outgoing arcs per vertex gives an oriented exact-seven spanning counterexample. Choose a globally minimum-total packing of three directed cycles and then the lead's lexicographic refinement; its remainder is acyclic, every packed cycle is chordless, every arc is dominated by a common predecessor, and the graph is 3-vertex-strong.

The lead and peer machinery splits the deficit system into SIX and global-NO-SIX. The current lead now sends the long aligned four-remainder heavy-triangle state into the common CROSS/BYPASS frontier. The fleet03/B04 seven-remainder theorem says the first strict R-supported collar at `|R|=7` has only one possible form: a `(3,2,2)` remainder sink `z`, a heavy directed triangle `T`, and three length-three in-arms whose six internal vertices exhaust `R\{z}`. The theorem below eliminates that entire no-cross/no-neutral R-supported pinwheel branch. A full BT4 proof still requires the separate SIX, short-support/coalesced CROSS-BYPASS, and support-carried omitted-sink closures.

## Inherited pinwheel geometry

Write

`T=t0->t1->t2->t0`,

`R={r0,s0,r1,s1,r2,s2,z}`,

with three internally disjoint arms

`ti -> ri -> si -> z`,  `i=0,1,2`.

The partner theorem gives:

1. `z` is a sink of `D[R]`;
2. `N+(z) intersect T = V(T)`;
3. the other two packed cycles, call them `A,B`, receive exactly two arcs each from `z`;
4. `(T,A,B)` is globally minimum in total packed order;
5. the hard branch excludes a size-neutral globally minimum packing exchange; and
6. `D` is a counterexample, so any exchanged remainder containing a directed cycle would already yield a fourth cycle.

The inherited normal form also supplies arc domination: for every arc `u->v`, some third vertex `q` satisfies `q->u,v`.

## New theorem — BT4-R7-PINWHEEL-DOMINATION-COLLAPSE-v1

**The R-supported seven-remainder triangular pinwheel cannot occur in the inherited no-neutral hard branch.**

### Lemma 1 — no first arm vertex points directly to z

For each `i`,

`ri not-> z`.

Suppose `ri->z`. Since `z->ti`, the three arcs

`ti -> ri -> z -> ti`

form a directed triangle `Qi`. It is disjoint from `A,B` and has the same order as the heavy triangle `T`. Replacing `T` by `Qi` therefore gives another globally minimum three-cycle packing.

If its new remainder contains a directed cycle, that cycle together with `Qi,A,B` is a forbidden four-pack. Hence in a counterexample the new remainder is acyclic. But then the replacement is exactly a forbidden size-neutral globally minimum packing exchange. Contradiction.

Thus `ri not->z` for every `i`.

### Lemma 2 — no packed vertex points to z

There is no arc from `T`, `A`, or `B` into `z`.

For `T` this is immediate from orientation and `z->ti` for every `ti`.

Now let `C` be either `A` or `B`, let `n=|C|`, and let the two distinct outneighbors of `z` on `C` be `y1,y2`. Suppose `p in C` satisfies `p->z`. Orientation gives `p!=yj`. For either `y=yj`, the walk

`p -> z -> y -> C[y,p]`

is a genuine directed cycle replacing `C`; its length is

`2 + d_C(y,p)`,

where `d_C(y,p)` is the positive forward distance from `y` to `p` on `C`.

Global minimum gives `2+d_C(y,p)>=n`. Equality would again be a size-neutral globally minimum exchange if its new remainder were acyclic, while a cyclic new remainder would already give four disjoint cycles. Hence the hard branch forces

`2+d_C(y,p)>n`.

Since `1<=d_C(y,p)<=n-1`, this implies `d_C(y,p)=n-1`, equivalently `y=p+`. Applying this to both distinct vertices `y1,y2` says both are the unique successor of `p`, impossible.

Therefore neither light packed cycle has an inarc to `z`.

### Lemma 3 — the exact inneighborhood of z is the three arm terminals

The remainder consists only of `ri,si,z`. Lemma 1 excludes every `ri->z`; Lemma 2 excludes all packed inarcs. The arm construction supplies `si->z`. Hence

`N-(z) = {s0,s1,s2}`.

### Lemma 4 — arc domination forces a directed cycle inside the remainder

Dominate the arm-terminal arc `si->z`. There is a vertex `q_i` with

`q_i -> si` and `q_i -> z`.

By Lemma 3, `q_i` is one of `s0,s1,s2`; it cannot equal `si` because loops do not exist. Thus every vertex of the induced digraph on `{s0,s1,s2}` has indegree at least one from another terminal.

Every finite digraph with minimum indegree at least one contains a directed cycle. Therefore `D[{s0,s1,s2}]` contains a directed cycle, entirely inside `R`. This contradicts the inherited acyclicity of `D[R]`.

The pinwheel branch is impossible. QED.

### What hypotheses really paid for the collapse

The proof is deliberately branch-accurate. The two light fan sizes equal to two are what exclude packed inports to `z`; the no-neutral condition is what excludes equality replacements; the counterexample condition handles cyclic exchanged remainders; and arc domination then closes the three-terminal inneighborhood. The proof does not use an edge-disjoint surrogate, a larger degree threshold, or the relaxed one-reversed-arc theorem.

## Same-run false statement and exact adversary

A tempting stronger statement is false:

`BT4-PINWHEEL-LOCAL-IMPOSSIBILITY-v0` — *the exact triangular pinwheel geometry is already incompatible with orientation, exact outdegree seven, arc domination, 3-vertex-strongness, a globally minimum three-triangle packing, and acyclic remainder, even without excluding neutral exchanges.*

The archived checker gives an exact 16-vertex counterexample to that stronger local statement. Its vertices are

`{t0,t1,t2,a0,a1,a2,b0,b1,b2,r0,s0,r1,s1,r2,s2,z}`.

The checker verifies all of the following directly from the complete adjacency list:

- oriented and loopless;
- 112 arcs, every vertex of outdegree exactly seven;
- strongly connected after deletion of every set of at most two vertices;
- every arc has a common-predecessor dominator;
- `T=(t0,t1,t2)`, `A=(a0,a1,a2)`, `B=(b0,b1,b2)` are directed triangles, hence their total order nine is globally minimum for any three-cycle packing in an oriented graph;
- `R={r0,s0,r1,s1,r2,s2,z}` is acyclic;
- all three pinwheel arms `ti->ri->si->z` occur;
- `z` is an R-sink with fan sizes `(3,2,2)` onto `(T,A,B)`.

Nevertheless the neutral triangle

`T' = t1 -> t2 -> r0 -> t1`

replaces `T` with the same total packed order and leaves an acyclic exchanged remainder. Thus the no-neutral hypothesis in the repaired theorem is not cosmetic. The graph also contains the explicit four-triangle packing printed by the checker, so it is not a BT4 counterexample and is not represented as one.

Checker SHA-256 from the actually executed local artifact: `e12c476200f587bd32de358bae5a02d5b34c49955f4d53a9aa09a6e7b96c5cbd`. Output SHA-256: `7bd036a9eefb1598445872ddc795ca8ac95f5579e114075b1bce379522455d85`. Execution status: `PASS`.

## Digon / asymmetric-degree repair

The same checker records a separate exact boundary adversary to the false strengthening “deleting a digon from a `delta+>=7` digraph leaves minimum outdegree at least six.”

Take the complete bidirected digraph on `d0,...,d10` and delete only the directed arcs

`d0->d8,d0->d9,d0->d10,d1->d9,d1->d10,d2->d10`.

Its outdegree vector is

`(7,8,9,10,10,10,10,10,10,10,10)`.

The pair `d3,d4` is a digon. Deleting those two vertices leaves `d0` with outdegree exactly five, so the surviving minimum outdegree is five. Thus the source-valid orientation reduction is exactly the known one: delete the digon, invoke the genuine k=3 theorem at threshold five, and re-add the digon as the fourth cycle. Threshold six or seven cannot be assumed, even under a highly asymmetric degree pattern.

## Applied peer consequence and updated frontier

This run directly consumes fleet03/B04 `BT4-R7-PINWHEEL-TRIANGLE-v1` and removes its R-supported triangular-pinwheel exception in the no-cross/no-neutral hard branch. The partner's newer corrected `BT4-HT-PORT-PATH-UPGRADE-v2` is retained unchanged for the distinct heavy-triangle branch; this run does not conflate those geometries.

The latest lead's explicit seven-remainder debt therefore shrinks: the **R-supported strict-collar pinwheel is closed in the no-neutral branch**. What remains at seven remainder vertices is the separately identified support-carried omitted-sink branch (and any neutral-exchange orbit, which must be processed rather than excluded when the proof is not in the no-neutral branch). Other campaign debts remain the lead's SIX closure, bounded F2/F3/short-support states, and universal/coalesced CROSS-BYPASS splice.

The next recipient should use the domination collapse before attempting any additional pinwheel port enumeration: once the state has reached the partner's exact R-supported pinwheel and has no neutral exit, there is no pinwheel splice left to solve.

## Failures and nonclaims

- `BT4-PINWHEEL-LOCAL-IMPOSSIBILITY-v0` is refuted by the exact 16-vertex adversary; the repaired theorem explicitly retains the no-neutral/counterexample hypotheses.
- The exact adversary has a four-pack and is not a counterexample to BT4.
- The digon example repairs only the deletion threshold; it is not new evidence against BT4.
- The support-carried omitted-sink branch is not closed here.
- SIX and the lead's CROSS/BYPASS endpoint-coalescence problem are not closed here.
- No finite search result is promoted to a universal proof; the universal pinwheel collapse is the four-lemma argument above.
- No novelty claim is made.

## Reproducibility / run accounting

Exact executed code is archived as `check_pinwheel_adversaries.py`; exact captured output is archived as `checker_output.txt`. No benchmark gold, credentials, scheduler identifiers, machine paths, raw transcripts, or unrelated private data are recorded.

Model self-report: `GPT-5.6 Sol`. Requested effort: `maximum actually supported`. Configured effort: `UNKNOWN_NOT_EXPOSED`. Known/self-observed reasoning effort: `UNKNOWN_NOT_EXPOSED`. Provider reasoning-token, provider thinking-time, and total-token counters: `null / NOT_EXPOSED`. Elapsed execution is reported separately in the finish record and is not pure thinking time.
