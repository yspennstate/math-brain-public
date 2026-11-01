# BT4 fleet03/B06 — return-port exclusion and sharpness of the off-pivot witness

Run: `20260922T014956Z-fleet03-B06-BT4-r12`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-G1-PORT-EXCLUSION-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and current authority

The active target is the k=4 Bermond--Thomassen conjecture: every finite loopless digraph with at most one arc per ordered pair and minimum outdegree at least seven contains four vertex-disjoint genuinely directed cycles. Digons are allowed in the target. The current fleet control reassigns fleet03/B06 to this BT4 research role; the older brain-installation/persistence prompt is superseded for substantive work.

The source boundary remains the current collective target record: Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (13 August 2026), leaves the exact conjecture unresolved for k>=4 and proves the threshold only for the one-reversed-arc relaxation. No near-directed cycle is used below.

## Exact other-account mathematics consumed

The assigned partner result actually used is fleet04/B04:

- `proofnet24/collective-BT4/fleet04/B04/fleet04-B04-20260922T011307Z-BT4-r11/report.md`;
- its correction `.../correction.md`, corrected candidate `BT4-SINKPORT-v1.1`, blob `0589d0067cffa3056d1675d8ec9c84e12ef616e8`.

I also consumed the BT4 lead's newer complete state

- fleet02/B04 `20260922T011943Z-b04-bt4-r11`, report blob `ee3294c169f9736cd8f0fdb943b5cefab5906a9e`, especially the off-pivot witness lemma after a neutral light pivot,

and the support-correct two-cycle exchange input

- fleet01/B05 `BT4-TCEX-v1`, report blob `f61ce94c50464f2d59491377df32f7e549db7242`.

No peer outcome label is treated as a proof.

## Inherited exact-seven G1 state

Assume a BT4 counterexample has been reduced to the inherited oriented exact-outdegree-seven normal form with a globally minimum three-cycle packing `(H,B,C)` and acyclic remainder `R`. In the global NO-SIX branch let `x` be a sink of `R`. The partner proves that, up to relabelling,

`|N+(x)∩H|=3`, `|N+(x)∩B|=|N+(x)∩C|=2`.

The heavy cycle `H` has no return to `x`. Each light cycle has at most one return port, and a B-port `b->x` forces

`N+(x)∩B={b+,b++}`.

In the partner's global return pattern G1, B is the only light cycle returning to x. Arc domination supplies a directed cycle `Q subseteq D[N^-(x)]`; every such cycle uses the unique port b and otherwise lies in R.

The lead's pair-deletion deficit theorem says that for the pair `H∪C`, because x itself has fan five, persistent NO-SIX requires at least three distinct five-witnesses for that pair.

## Lemma 1 — the unique G1 return port is not an opposite-pair five-witness

In the G1 state above,

`|N+(b) ∩ (H∪C)| <= 4`.

### Proof

Choose any directed domination cycle `Q subseteq N^-(x)`. In G1 it meets the packed cycles only at the unique port b, so the successor of b on Q is a vertex `r in R`. The successor cannot be x: every vertex of Q lies in `N^-(x)` and hence sends to x, while the inherited oriented normal form has no digons, so `x->b` is impossible when `b->x`.

Thus b has three distinct outneighbors outside `H∪C`:

1. its directed-cycle successor `b+` on B;
2. the sink `x` via the return arc `b->x`;
3. the R-vertex `r` following b on Q.

Every vertex has outdegree exactly seven, hence at most four remaining outarcs can enter `H∪C`. QED.

This uses the partner's actual G1 domination-cycle geometry; it is not an average-degree count.

## Corollary 2 — two extra H∪C five-witnesses must avoid the port

The sink x has exactly `3+2=5` outneighbors in `H∪C`, so x is one five-witness for that deleted pair. In persistent NO-SIX the strengthened pair-deletion theorem supplies at least three distinct five-witnesses. By Lemma 1 the unique return port b is not one of them.

Therefore at least two additional five-witnesses lie in

`(B\{b}) ∪ R`.

This removes the return port itself from the lead's regenerated-witness search. If an additional witness lies in R, the remainder-supported exchange machinery applies. If it lies in `B\{b}`, it is a cycle-supported witness and must be handled by the support-correct segment/two-cycle machinery; one may not silently treat it as a remainder witness.

## Corollary 3 — what the lead's off-pivot lemma cannot be strengthened to by support counting

Perform the lead's neutral light pivot

`B* = b -> x -> b++ -> ... -> b`,

whose new remainder is `(R\{x})∪{b+}`. The lead proves that persistent NO-SIX produces a five-witness `z` for `H∪C` outside the two pivot vertices `{x,b+}`.

It is tempting to strengthen this to: the off-pivot z must be an old-remainder vertex, or at least must lie away from the immediate light-cycle successor block. The exact certificate below refutes that strengthening while retaining the full local exact-seven normal form, domination, 3-vertex-strongness and all three NO-SIX pair-deletion multiplicities.

In the certificate the exact H∪C five-witness set is

`{b+, b++, x}`.

Hence after the neutral light pivot the lead's guaranteed off-pivot witness is uniquely `z=b++`, a vertex on the new support cycle immediately adjacent to x. Pure support cardinality therefore does not push the regenerated witness into R or away from the pivot collar.

## Exact constrained-search sharpness certificate

A binary constrained search produced the following 20-vertex oriented digraph. The independently executable standard-library checker in this run verifies the complete graph, not a quotient or degree sequence.

Packed cycles:

`H=(0,1,2,3)`, `B=(4,5,6,7)`, `C=(8,9,10,11)`,

with `R={12,...,19}`, sink `x=19`, and unique light port `b=4`.

The checker verifies simultaneously:

- 20 vertices and exactly 140 arcs, every outdegree exactly seven;
- no loops and no digons;
- H,B,C are directed and chordless;
- R is acyclic with unique sink 19;
- x has fans `H:[0,1,2]`, `B:[5,6]`, `C:[9,10]`;
- ports to x are `H:[]`, `B:[4]`, `C:[]`, exactly the G1 pattern;
- every one of the 140 arcs is dominated;
- deletion of every set of at most two vertices leaves a strongly connected digraph;
- all three packed-pair fans are NO-SIX, with exact five-witness sets `HB={8,9,19}`, `HC={5,6,19}`, `BC={0,1,2}`;
- the port b has only three outneighbors in `H∪C`, consistent with Lemma 1;
- the graph nevertheless contains the explicit four-cycle packing `(0,1,6)`, `(2,3,8)`, `(4,11,7)`, `(5,13,9)`.

Thus this is NOT a BT4 counterexample. It is a source-valid local sharpness certificate: exact-seven degree, arc domination, 3-strongness, G1, and the full NO-SIX pair-witness multiplicities do not by themselves force either of the two extra H∪C five-witnesses into the old remainder. The global no-four-pack condition must enter through exchanged-remainder acyclicity, path geometry, or a genuine rerouting.

The complete adjacency list is embedded in `cycle_support_checker.py`; `checker_output.json` is the exact checker output.

## Updated conditional route and first unpaid implication

The newest lead state says a neutral light pivot cannot terminate in the trivial two-state reversal: it either creates a six-fan or regenerates an off-pivot same-pair five-witness z. Lemma 1 and Corollary 2 sharpen the original G1 state by excluding the unique return port from the same-pair witness set. The exact certificate then shows the next stronger support-only shortcut is false: z can be exactly `b++`.

Therefore the first genuine remaining implication in G1 is now:

> Suppose persistent NO-SIX holds after the neutral light pivot and the regenerated H∪C five-witnesses are confined to the immediate B-collar rather than R. Combine their support-correct unique R exits / segment-bypass alternatives with the partner's exchanged-remainder reachability wall and G1 R-fork to force either a forbidden inversion, a cross-packed two-cycle splice, or a six-fan.

A counting argument that merely says "there is an off-pivot witness" is insufficient; the certificate realizes the extremal local support pattern. The next proof has to use the global acyclicity/no-four-pack information or the actual linkage paths.

## Status

`ESSENTIAL_STEP_APPLIED`.

New proved step: the G1 unique return port has opposite-pair fan at most four and is excluded from the required five-witness set.

New exact failure boundary: even with exact-seven, all-arc domination, 3-strongness and exact NO-SIX deficits, the extra witnesses can remain entirely on the immediate light-cycle collar; after the lead's neutral pivot the unique off-pivot witness can be `b++`.

Full BT4 remains OPEN / NOT PROVED. Next recipients: assigned partner `fleet04/B04`, campaign lead `fleet02/B04`, and exchange/linkage workers using the off-pivot witness process.
