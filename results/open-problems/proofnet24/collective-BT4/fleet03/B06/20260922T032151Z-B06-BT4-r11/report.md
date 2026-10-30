# BT4 fleet03/B06 — corridor defect and bridge-or-slack

Run: `20260922T032151Z-B06-BT4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-G1-CORRIDOR-DEFECT-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED` with a local `CANDIDATE_REFUTED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`  
Parent target: `OPEN_NOT_PROVED`

## Exact target and source boundary

The target is the exact k=4 Bermond--Thomassen statement: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are allowed and a digon counts as a directed cycle.

The current shared source boundary remains Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (13 August 2026): the exact conjecture remains unresolved for k>=4; the paper proves only the one-reversed-arc relaxation at the same threshold. Nothing below promotes a near-directed cycle to a directed one.

## Exact other-account result consumed

Assigned partner: `fleet04/B04`, candidate `BT4-G1-WITNESS-INVARIANT-v1`, shared handoff blob `f5533fe5b8ff8dd76fe701124f4bfd74370f2c8d`, canonical science blob `df42a0c3455fe3fb14f71351067f41fac75afb27`.

Its proved G1-S branch works in the inherited oriented exact-outdegree-seven minimum-counterexample normal form. After the canonical neutral G1 light pivot, for the unchanged opposite pair the entire residual degree-two witness set `W` is unchanged. In G1-S, `W` lies on the short light support `B*`, `|W|>=3`, every `w in W` has exactly one exit to the new acyclic remainder, and two support witnesses share the same heavy target cycle.

I also retain the controlling no-cross correction from fleet02/B04: every such cycle-supported heavy witness has a heavy-cycle inport; otherwise fan-arc domination already produces a cross-packed transition. And I retain the support-correct `BT4-TCEX-v1`: if a heavy witness `w` with fan size `m` has an inport from its heavy target and an old-remainder predecessor-to-successor bypass of length `ell`, then `ell>=m`; equality gives a fully accounted neutral two-cycle exchange and a forbidden-inversion condition in the exchanged acyclic remainder.

My immediately preceding result `BT4-G1-PORT-SPACING-v1` proved that for two same-heavy G1-S witnesses `z1,z2`, with heavy inports `p1,p2`, fans `Fi=N+(zi) intersect A`, and `mi=|Fi|>=3`, global minimum implies all fan-return segments intersect. If `p1!=p2`, this is equivalent to the one-sided corridor alternative

`F1 subseteq (p1,p2]_A`  OR  `F2 subseteq (p2,p1]_A`.

The new step below extracts the exact extra consequence at the tight boundary and proves the sharp bridge-free tax.

## Compact conditional route

Assume a BT4 counterexample and the inherited exact-seven globally minimum three-cycle packing with acyclic remainder. In persistent NO-SIX, enter the partner's G1-S branch. Pick two support witnesses with the same heavy target `A`. In the no-cross branch they have heavy inports. The port-spacing result confines one heavy fan to a directed port corridor.

The new lemma now makes the confined corridor binary:

1. **tight corridor:** it necessarily contains the opposite inport as a fan target, creating an actual directed two-edge bridge between the two support witnesses; or
2. **bridge-free corridor:** the directed port gap is at least one vertex longer than the heavy fan.

The exact constrained certificate below shows that local degree-seven, domination, 3-vertex-strongness, pre/post-pivot remainder acyclicity, G1-S, bridge-free defect one, and long TCEX bypasses can coexist. That local configuration fails the true minimum-packing condition by an explicit strict three-cycle replacement. Thus the surviving proof must now use global minimum *quantitatively* against the one-unit corridor defect; no purely local witness-counting strengthening can close this branch.

## Lemma 1 — tight corridor forces a port bridge

Work in G1-S no-cross. Let distinct support witnesses `z1,z2` be heavy on the same packed cycle `A`. Write

`Fi = N+(zi) intersect A`,  `mi=|Fi|>=3`,

and choose heavy inports `pi->zi`, `pi in A`. Suppose `p1!=p2`.

By `BT4-G1-PORT-SPACING-v1`, at least one of

`F1 subseteq (p1,p2]_A`,
`F2 subseteq (p2,p1]_A`

holds. Consider the first alternative and put

`d12 = d_A(p1,p2) = |(p1,p2]_A|`.

Then:

- `d12>=m1`;
- if `d12=m1`, necessarily

  `F1=(p1,p2]_A`,

  because both sets have exactly `m1` vertices;
- in particular `p2 in F1`, hence

  `z1 -> p2 -> z2`

  is a genuine directed two-edge bridge in the original digraph;
- contrapositively, if `p2 notin F1`, then only `d12-1` vertices of the corridor remain available to contain the `m1` fan targets, so

  `d12 >= m1+1`.

The symmetric statement holds in the second corridor alternative.

Therefore every distinct-port same-heavy pair satisfies the exact **bridge-or-slack dichotomy** on at least one carrying side:

`z1->p2->z2`,

or `d_A(p1,p2)>=m1+1`,

or symmetrically `z2->p1->z1`,

or `d_A(p2,p1)>=m2+1`.

Equivalently, for a carrying corridor define its defect `delta=d-mi`. Then `delta=0` forces the opposite-port bridge, while a bridge-free carrying corridor has `delta>=1`.

This is an all-order proof; the finite checker below is only an independent implementation check.

## Lemma 2 — the +1 bridge-free tax is sharp at the cyclic-order level

For every `m>=3`, take a directed heavy cycle of order `n=m+2`, ports `p1=0`, `p2=1`, and common fans

`F1=F2={2,3,...,m+1}`.

Then all fan-return segments intersect because `F2 subseteq (p2,p1]_A`. Neither fan contains the opposite port, so neither port bridge exists. The carrying directed gap has length `m+1`, hence defect exactly one.

Thus the `+1` bridge-free tax cannot be improved from cyclic corridor information alone, and a bridge is not universally forced by G1-S interval overlap.

## Exact constrained certificate: the local closure strengthening is false

A standard-library checker verifies the following 22-vertex oriented digraph, encoded completely in `checker.py`.

- every vertex has outdegree exactly seven;
- there are no loops or digons;
- every arc is dominated by a common predecessor;
- deletion of every set of at most two vertices leaves the digraph strongly connected;
- the packed cycles are `H=(0,1,2,3)`, `B=(4,5,6,7)`, `A=(8,9,10,11,12)`;
- the old remainder `R={13,...,21}` is acyclic;
- `x=21` is an old remainder sink with fan `(3,2,2)` and unique G1 return port `4->21` from `B`;
- after the canonical pivot `B*=(4,21,6,7)`, the new remainder `R*={5,13,...,20}` is also acyclic;
- after deleting `H union A`, the residual degree-two set is exactly `W={6,7,21}` and lies wholly on `B*`, so this is a local G1-S realization;
- witnesses `z1=6,z2=7` are both heavy on `A`, with inports `8->6`, `9->7` and common three-fan `{10,11,12}`;
- neither opposite port is in that fan, while the carrying gap from port 9 to port 8 has length four, giving the sharp bridge-free defect `4-3=1`;
- the shortest `R*`-internal predecessor-to-successor TCEX bypass length for each of these two witnesses is four, strictly above the heavy fan size three, so neither supplies the short/equality TCEX closure.

This certificate is deliberately **not** a BT4 counterexample and is **not** a globally minimum packing. The checker exhibits the strict smaller three-cycle packing

`(2,3,4)`, `(1,5,6)`, `(0,9,10)`,

of total order nine, compared with the original packed total order thirteen.

Hence the tempting strengthening

> local G1-S + exact degree seven + arc domination + 3-vertex-strongness + old/new remainder acyclicity + no port bridge + long TCEX bypasses is already contradictory

is false. This failure is useful: the displayed realization passes those listed local/global-connectivity filters and fails the minimum-packing filter by an explicit certificate. The next proof must therefore exploit global packing minimality against the bridge-free corridor defect or use the bridge branch to build an actual splice.

## Exact computation

`checker.py` was executed twice in the same invocation with byte-identical output.

- checker SHA-256: `8e2f45a8cfe5e1060aca06c82a162b8d272752fc2cd52b021e541789cf82102b`;
- output SHA-256: `3eb454095bd109ae5f3d4b56a55c02a03b4ba7cd32a7b46519b0907b0693bfa0`;
- canonical output payload SHA-256: `ae1aab24b31801c47fa1d5b55563a505d741152102656f8d4360778952182ae5`;
- exhaustive symbolic check: 5,870,304 all-cross configurations for heavy-cycle orders at most ten and fan sizes three through five, with zero bridge-or-slack violations;
- the sharp defect-one family was separately checked for fan sizes three, four and five.

These finite checks support the implementation and the exact certificate; they are not used as the proof of Lemma 1, whose counting argument is uniform in the cycle order.

## Remaining first universal obligation

Candidate `BT4-G1-DEFECT-MINIMALITY-v1`:

In a genuine globally minimum G1-S no-cross state, take a same-heavy pair and a carrying corridor from Lemma 1. Prove one of the following.

1. In the tight case, the forced two-edge port bridge, together with the witnesses' unique remainder exits and support-correct TCEX/linkage paths, yields a legal cross-packed splice, neutral exchange with a forbidden inversion, six-fan, or fourth disjoint directed cycle.
2. In the bridge-free case, the one-or-more unused corridor vertices (`delta>=1`) can be charged into a strict two-cycle packing reduction or an exchanged-remainder directed cycle. The exact defect-one family shows the argument must use more than cyclic order alone.

The constrained certificate above says this obligation cannot be replaced by a purely local degree/connectivity/acyclicity contradiction. The global minimum comparison is now the specific resource to spend.

BT4 remains open; no target-level proof or counterexample is claimed.
