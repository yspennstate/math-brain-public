# FOREST / account03 B02 — theta_3 simple simulation and contraction-debt removal

Run: `20260922T025856Z-b02-forest-r12`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Assignment: prove a useful minimal-counterexample reduction covering the genuinely unresolved three-connected obstruction, not merely another finite graph class.  
Partner: `account04/B03`.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.  
Target-level status: **OPEN**.

## 1. Exact peer result consumed

I consumed the finalized partner handoff `account04/B03`, run `20260922T001033Z-B03-r43`, and its scientific report. Its two decisive interfaces are:

1. In every finite simple 3-vertex-connected graph and for distinct marked edges `e,f`, all reconnection reservoirs are strictly nonempty: `n00>=1`, `n10>=1`, `n01>=1`, `n11-q>=1`, and `q>=1`.
2. Those support facts plus the previously derived three-edge sign-cluster/minor inequalities are **not sufficient by themselves**: the partner supplied an exact valid local three-edge graphic-matroid mixture with `Delta(e,f)=-3`, `Delta(e,g)=Delta(f,g)=46`, nonnegative deletion/contraction strata, and all reconnection reservoirs positive. Hence the first surviving all-graphs obstruction is a graph-global compatibility constraint among the outside-forest states, not a pointwise local-cone inequality.

This run therefore changed mechanism. Instead of adding another local inequality, it attacks a weakness in the minimal-counterexample machinery itself: contraction of a third edge in a simple graph can create parallel classes, so simple-graph minimality does not automatically imply nonnegativity of the contraction stratum.

## 2. A unit-weight simple simulator for every loopless multigraph

### The theta_3 gadget

For terminals `u,v`, let `Theta_3(u,v)` consist of three internally vertex-disjoint paths of length two between `u` and `v`, with three fresh internal vertices.

For a finite loopless multigraph `M`, form a finite simple graph `S(M)` by replacing **each labelled edge** `a=uv` of `M` by its own fresh copy of `Theta_3(u,v)`. Distinct parallel edges of `M` receive disjoint internal vertices, so `S(M)` is simple.

For a forest `H` of `S(M)`, define `C_a(H)=1` iff the selected edges inside the gadget for `a` connect its two terminals. Let `C(H)={a:C_a(H)=1}`.

### Lemma 2.1 — exact 27/27 gadget balance

For one `Theta_3` gadget under the uniform acyclic-subgraph count:

- there are exactly `27` internal configurations that do not connect the terminals;
- there are exactly `27` internal configurations that connect the terminals.

**Proof.** Each two-edge path has three noncomplete subsets. A disconnected gadget configuration therefore has `3^3=27` possibilities. An acyclic connected configuration must have exactly one complete two-edge path; choosing that path gives `3` choices and the other two paths each have `3` noncomplete states, giving `3*3^2=27`. Two complete paths would create a cycle. QED.

### Lemma 2.2 — forests project exactly to multigraph forests

A selected edge set `H` is a forest of `S(M)` iff `C(H)` is a forest of the labelled multigraph `M`.

**Proof.** In an acyclic gadget at most one of the three length-two paths is complete. All selected edges on incomplete paths terminate at their fresh degree-two internal vertex and do not create a terminal-to-terminal route. Delete such pendant/dead-end pieces. What remains is exactly one length-two route for every `a in C(H)`. Contracting each such route gives the labelled edge set `C(H)`. Thus a cycle in `H` exists iff the projected multigraph edge set contains a cycle. In particular two projected parallel edges form a multigraph two-cycle, and their two complete gadget paths form a simple four-cycle in `S(M)`. QED.

### Theorem 2.3 — exact uniform projection

If `H` is uniform over all forests of `S(M)`, then `C(H)` is **exactly uniform over all forests of `M`**.

**Proof.** For every multigraph forest `F`, each gadget in `F` has 27 connected lifts and each gadget outside `F` has 27 disconnected lifts. Hence every `F` has exactly `27^{|E(M)|}` forest lifts. Lemma 2.2 says there are no other projected states. QED.

This is an exact finite identity, not an asymptotic or weighted approximation.

## 3. Exact covariance sign preservation

Fix one physical edge `x` in the gadget of a labelled multigraph edge `a`.

Among the 27 disconnected gadget states, `x` is present in exactly 9, so

`P(x in H | C_a=0)=1/3`.

Among the 27 connected states, `x` is present in exactly 15: 9 states when its own two-edge path is the complete path, plus 6 states when one of the other two paths is complete. Hence

`P(x in H | C_a=1)=5/9`.

Therefore

`E[1_x | C_a] = 1/3 + (2/9) C_a`.

For physical edges `x,y` chosen in two distinct gadgets `a,b`, gadget configurations are conditionally independent given the projected forest. The law of total covariance gives the exact identity

`Cov_{S(M)}(1_x,1_y) = (4/81) Cov_M(1_a,1_b)`.

### Corollary 3.1 — simple graphs and loopless multigraphs are equivalent for the unit FOREST target

The pairwise negative-correlation conjecture for all finite simple graphs holds iff it holds for all finite loopless multigraphs.

The reverse implication is immediate because simple graphs are loopless multigraphs. For the forward implication, a violating pair in a loopless multigraph would, by the displayed identity, give a violating pair of physical edges in the finite simple graph `S(M)`.

Loops may simply be discarded because no forest ever contains a loop.

This equivalence is useful independently of any positive-weight upgrade. In particular it does **not** use the disputed fixed-graph weighted implication attributed to Cocks.

## 4. Minimal-counterexample consequence: contraction debt disappears

Assume the target is false. By Corollary 3.1, choose a loopless multigraph counterexample `M` with the minimum possible number of labelled nonloop edges, and choose a violating pair `e,f` with `Delta_M(e,f)<0`.

Fix any third edge `g`. Write the forest polynomial with respect to `g` as

`I_M = A + y_g B`,

where `A=I_{M\g}` and `B=I_{M/g}` after deleting loops created by contraction. At `y_g=1`, let `D0` and `D1` be the `e,f` Rayleigh gaps in the deletion and contraction strata. If contraction makes `e` or `f` a loop, then `D1=0`. Otherwise `M/g` (with loops discarded) has fewer nonloop edges than `M`, so minimality gives `D1>=0`; similarly `D0>=0`.

The exact three-edge identity is

`A B Delta_M(e,f) = B(A+B) D0 + A(A+B) D1 - Delta_M(g,e) Delta_M(g,f)`.

Because `A,B>0`, `Delta_M(e,f)<0`, and `D0,D1>=0`, it follows for every third edge `g` that

`Delta_M(g,e) Delta_M(g,f) > 0`.

Thus the earlier sign-cluster theorem becomes completely unit-weight and minor-minimal in the enlarged-but-equivalent loopless-multigraph universe: there is no unresolved positive-integer activity/parallel-class contraction debt.

In particular, define `a~b` when `a=b` or `Delta_M(a,b)<0`. Then `~` is an equivalence relation. Every nontrivial class is a clique of violating pairs, and every edge outside such a class has strictly positive Rayleigh gap to every member of the class.

This is a genuine universal minimal-counterexample reduction; it is not a finite graph subclass.

## 5. Relation to the three-connected obstruction

The partner `account04/B03` already proved that a purely local three-edge cone, even supplemented by full reconnection support and sign clustering, still admits the forbidden sign pattern. The theta_3 reduction does not refute that witness and does not claim the parent conjecture solved.

What changes is the status of the inherited contraction step. One no longer needs to assume that a simple contraction remains simple, nor to import a positive-weight contraction theorem merely to obtain `D1>=0`: equivalence with loopless multigraphs lets minimality pay that term directly.

The first remaining universal implication is therefore still genuinely global:

> **Global compatibility residual.** In a 3-connected source obstruction, prove that the outside-forest local graphic-matroid types cannot be coupled across all outside states so as to violate `n00*n11 <= n10*n01 + N*q` while simultaneously satisfying the strict sign-cluster conditions for every third edge.

The partner’s local-cone witness shows that any successful inequality must use compatibility between different outside forests of one ambient graph (cycle-space/separator/exchange structure), not only pointwise membership in the three-edge graphic-matroid cone.

This run therefore hands the lead a cleaner structural input: **the sign-cluster/minor side can be made exact at unit weight without contraction debt; the unpaid mathematics is the graph-global compatibility side.**

## 6. Exact executable check

`theta3_simulation_check.py` exhaustively enumerates all 64 subsets of one theta_3 gadget and all forests of the full theta_3 expansions of two three-edge examples.

It verifies exactly:

- local counts `(D,C,Dx,Cx)=(27,27,9,15)`;
- conditional physical-edge probabilities `1/3` and `5/9`;
- every original forest has exactly `27^3=19683` expanded forest lifts in both examples;
- triangle nonparallel-pair covariance scales from `-2/49` to `-8/3969`;
- a parallel-pair example scales from `-1/9` to `-4/729`;
- the exact factor is `4/81`.

The archived output terminates `THETA3_SIMULATION_PASS`.

## 7. Source reconciliation note

A separate source issue remains important for the collective full-candidate route. The published final Semple--Welsh paper explicitly notes that Cocks showed: if Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated. An earlier Semple--Welsh version also gives the weaker class-level rational/integer-parallelization equivalence. I did not obtain the full primary Cocks proof in this runtime, so I do not use that fixed-graph theorem as a proved internal lemma here. The theta_3 result above is source-independent and can be checked directly.

## 8. Status / handoff

**Outcome:** `ESSENTIAL_STEP_APPLIED`.

**New theorem:** exact theta_3 simple simulation of every loopless multigraph forest law, with covariance scale `4/81` across distinct gadgets.

**New reduction:** the simple-graph FOREST target is equivalent to the loopless-multigraph unit target. Hence an edge-minimal loopless-multigraph counterexample has deletion and contraction strata nonnegative for every third edge, eliminating the previous contraction-weight debt and making the strict bad-pair sign-cluster theorem unconditional in that equivalent universe.

**Parent target:** OPEN. No novelty/priority claim is made.

**Earliest remaining blocker:** graph-global compatibility in the 3-connected reconnection/sign-cluster obstruction exposed by `account04/B03`.

**Recipient:** `account04/B03` and the FOREST lead. A useful next attack is to formulate transitions between outside forests differing by one edge and derive a conserved/monotone quantity on the induced terminal partition types; any candidate must first reject the partner’s exact local-cone witness.
