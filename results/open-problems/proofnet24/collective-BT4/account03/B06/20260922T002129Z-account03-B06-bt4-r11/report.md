# BT4 account03/B06 — tight-port rigidity and exact U1 sharpness certificate

Run: `20260922T002129Z-account03-B06-bt4-r11`
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`
Campaign: `BT4`
Outcome: `ESSENTIAL_STEP_APPLIED`
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and authority change

The live owner control reassigns account03/B06 from the former brain-context/persistence role to the collective BT4 research team. The active target is:

> Every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four vertex-disjoint genuinely directed cycles. Opposite arcs are allowed; a digon counts as a directed cycle.

The source-exact target file records Bessy–Muis–Sereni–Steiner–Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (13 August 2026), as the current primary source: the exact conjecture remains unresolved for k>=4; their threshold-seven result permits a one-arc reversal and therefore does not settle BT4. No target-level closure is claimed here.

The exact account03/B06 assignment is to use constrained search and symbolic families to test the decisive BT4 lemma while retaining the full original directed graph and complete cycle-packing certificates. The named partner is `account04/B04`.

## Other-account mathematics actually consumed

I consumed the assigned partner's exact report

`proofnet24/collective-BT4/account04/B04/account04-B04-20260922T001035Z-BT4-r01/report.md`

(blob `70ee4cadc758502f36a5014f096d399096a237a1`) and its candidate `BT4-RSC-v1`.

I also consumed the newer compatible account01/B04 report

`proofnet24/collective-BT4/account01/B04/20260922T001115Z-b04-bt4-r11/report.md`

(commit `6784701dec457ccf70a7d33151ae06770f04658a`, blob `79c91a55da8f23489bf3a18c8fc874e588b5ce12`), candidate `BT4-MCR-v2`.

The common inherited setup is a vertex-minimal, then arc-maximal counterexample D; a minimum-total three-cycle packing `C1,C2,C3`; and DAG remainder `R`. The packed cycles are chordless. If `x in R`, `C` is packed, `m=|N+(x) intersect C|`, and a directed path starts at `b in C`, ends at x, and otherwise stays in R, then its length L satisfies `L>=m-1`. Every deleted pair of packed cycles supplies either a residual vertex of outdegree at most one (hence a six-fan into the pair) or at least three residual vertices of outdegree exactly two (hence three five-fans into the pair).

The partner refines the packing by maximizing a longest R-path. For a longest-path sink x and a heavy packed cycle C, the unique-sink branch has a return collar. Its tight subbranch U1 is the case of an arc from C to a vertex at R-distance `m-2` from x, equivalently a permitted C-to-x return of exact length `m-1`.

## Lemma 1 — tight U1 returns have a consecutive fan

Let `C=(b,b^+,... )` have length r. Assume `3<=m<r`, x is a sink of R, and

`P: b=p0 -> p1 -> ... -> p_(m-1)=x`

is a C-to-x path of the minimum permitted length `m-1`, with all `p1,...,p_(m-1)` in R. Assume `m=|N+(x) intersect C|`.

Then

`N+(x) intersect C = {b^+, b^(+2), ..., b^(+m)}`.                 (1)

### Proof

The corrected path-fan proof says that every fan target `a != b` lies among the first `L+1=m` successors of b on C. Because `m<r`, the arc `x->b` is impossible: `P+x->b` would be a directed cycle of length m<r, replacing C and strictly reducing total packing size. Hence all m fan targets lie in an m-element successor window. Equality forces (1). QED.

This is not merely a finite-search observation.

## Lemma 2 — single-port boundary rigidity

Under the hypotheses of Lemma 1, let

`L_(m-2)={v in R : dist_R(v,x)=m-2}`.

Then every arc from C into `L_(m-2)` has the **same tail b**.

### Proof

If `c->w` with `w in L_(m-2)`, append a shortest w-to-x path. This is another C-to-x path of length `m-1`, so Lemma 1 applied with port c gives

`N+(x) intersect C = {c^+, ..., c^(+m)}`.

For `m<r`, an m-consecutive proper block of a directed r-cycle has a unique predecessor, hence its port is unique. Comparing with (1) gives `c=b`. QED.

Thus U1 does not permit several independent tight entrances. It has one exact port.

## Corollary 3 — the rigid six-head contraction branch is impossible in nonsaturated U1

In the same setting, the external head union of C has size at least seven:

`|N+(V(C)) \ V(C)| >= 7`.                                         (2)

### Proof

The account01/B04 contraction lemma proves that for a chordless packed cycle, external-head union at most six forces the rigid case: every vertex of C has outdegree exactly seven and has the same six external outneighbors.

Choose the first R-vertex `p1` on the tight path. Since its distance to x is `m-2`, it is an external outneighbor of b in the boundary layer. If the rigid case held, every vertex of C would point to `p1`, contradicting the single-port boundary lemma. Hence the union exceeds six. QED.

This eliminates one exact contraction branch of `BT4-RSC-v1`.

## Lemma 4 — equal-size exchange and inversion prohibition

Continue with the tight path P above. By (1), `x->b^(+m)`. Define

`C* = P + (x->b^(+m)) + C[b^(+m) -> ... -> b]`.

Then C* is a genuine directed cycle with exactly r vertices. It replaces C without changing the total size of the three-cycle packing.

The vertices freed from C are

`F={b^+, ..., b^(+(m-1))}`,

and the R-vertices consumed by P are

`Q={p1,...,p_(m-1)}`.

Let

`R'=(R\Q) union F`.

In a true counterexample R' must be acyclic, because a directed cycle in R', together with C* and the other two packed cycles, is a four-cycle packing.

Consequently, for all `1<=i<j<=m-1`, there is **no** directed path in R' from `b^(+j)` to `b^(+i)`. Otherwise that path plus the forward C-segment from `b^(+i)` to `b^(+j)` is a directed cycle in R'.

This converts U1 into a concrete order constraint on the freed consecutive block. The next exchange argument has to violate this inversion prohibition or force witnesses off the block.

## Lemma 5 — a second sink with q=2 also has one direct-return port

Use the partner's multiple-sink notation. Let y be a second sink and let

`q=|N+(y) intersect C|=2`.

If any `b->y` exists from C, then the partner's exact exchange restriction gives

`N+(y) intersect C={b^+,b^(+2)}`.

Since r>=4, this two-consecutive block has a unique predecessor b. Hence C has exactly one possible tail for a direct arc into y. The partner's anti-alignment lemma also gives

`b^+ notin N+(x)`.

Since x has m>=3 distinct outneighbors on C, this forces `r>=m+1>=4`.

For q=1, if its unique fan vertex is a, a direct-return tail can only be `a^-` or `a^(-- )`; the latter is subject to the same anti-alignment exclusion on `a^-`. This leaves a small exact port geometry for the multiple-sink branch.

## Exact constrained-search sharpness certificate

A tempting but false next statement would be: “minimum outdegree seven plus the local U1 tight geometry already contradicts the equal-size exchange.” The attached exact checker refutes that stronger local lemma while retaining the whole original digraph.

It verifies an 18-vertex oriented digraph with every outdegree exactly seven. It contains the packed cycles

`C1=(0,1,2,3)`, `C2=(4,5,6)`, `C3=(7,8,9)`,

and `R={10,...,17}` is a DAG with unique sink `x=17`. The exact tight path is

`0 -> 16 -> 17`

with `m=3` and

`N+(17) intersect C1={1,2,3}`,

while C1 has no arc to x. The equal-size exchange cycle is

`C1*=(0,16,17,3)`.

The new remainder then contains the directed triangle

`(1,10,15)`,

so the graph has the explicit four-pack

`(0,16,17,3), (4,5,6), (7,8,9), (1,10,15)`.

Thus the counterexample is **not** a BT4 counterexample. Its value is sharper: it proves that local fan tightness and the degree-seven condition by themselves do not forbid U1. The global no-four-pack condition is used exactly through acyclicity of R' / the inversion prohibition.

The complete adjacency list is embedded in `tight_port_checker.py`; the checker verifies no loops, no digons, all outdegrees seven, the original packing, R acyclicity and unique sink, the tight fan/path, the equal-size exchange, and the displayed four-pack.

A separate finite symbolic sanity sweep over every `4<=r<=12` and `3<=m<r` checks 45 cyclic-block instances. Every tight fan is the consecutive m-block and has exactly one port. This only checks the finite instances; Lemmas 1-2 prove the statement for all r.

## Updated conditional chain and first unpaid implication

The surviving candidate is `BT4-RSC-v2-tight-port`:

1. minimal/arc-maximal counterexample and minimum-total packing;
2. pair-deletion six-fan-or-three-five-fans amplification from `BT4-MCR-v2`;
3. partner remainder split `BT4-RSC-v1`;
4. in nonsaturated U1, the tight return has one port, a consecutive fan, external-head union at least seven, and an equal-size exchange whose new remainder is acyclic;
5. therefore the freed block admits no backward path (inversion) in the exchanged remainder.

The first unpaid universal implication is now:

> In U1, apply the six-fan-or-three-five-fans witnesses for the two packed-cycle pairs involving C. Prove that one amplified witness either creates a forbidden inversion among the freed vertices of the equal-size exchange, or forces all relevant witnesses onto the other packed cycles in a configuration admitting a two-cycle rerouting. The proof must retain witness multiplicity and disjointness; an average degree count is insufficient.

For the multiple-sink q=2 branch, the analogous target is to combine the unique direct-return port plus anti-alignment with the same pair-witness multiplicity.

This is narrower than the former generic “force a short return” obligation and identifies exactly where global no-four-pack information first becomes indispensable.

## Status

`ESSENTIAL_STEP_APPLIED`, not a full proof. Full BT4 remains OPEN on the current source evidence. The new universal lemmas are the tight consecutive-fan identity, single-port boundary rigidity, the exclusion (2) of the rigid six-head contraction branch in U1, and the equal-size-exchange inversion prohibition. The explicit 18-vertex graph is a counterexample only to a stronger local closing lemma, not to BT4.

Next recipients: assigned partner `account04/B04` and BT4 lead `account02/B04`.
