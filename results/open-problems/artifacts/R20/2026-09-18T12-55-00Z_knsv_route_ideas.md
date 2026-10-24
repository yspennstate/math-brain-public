# R20 KNSV-2026-LOOPY-U route ideas before code

Model request in task text: GPT-6 / maximum. Actual runtime model for this worker: GPT-5.6 Sol; reasoning telemetry UNVERIFIED.

This note is deliberately written before the new checker. The frozen successor metric is `N_sep`, the minimum order of a **simple** pair separating ordinary `U` and ordinary loopy `L`; the source has certified `N_sep > 11`.

## Route A — #9 RANDOMIZE / rooted-gadget module rather than raw graph enumeration

The first exact two-new-vertex rooted-gadget search around the source's ten-vertex collision pair returned no separator. Instead of enumerating 13-vertex graphs, compute the rooted `U` state and pointed `L(1,x)` state of each seed root once. A one-vertex sum with a rooted gadget is then an exact bilinear convolution: root-component sizes combine as `s_G+s_K-1`, cyclomatic numbers add, and the pointed loopy root exponents add. Enumerate all 64 labelled simple rooted gadgets on root plus three new vertices and compare all resulting cross extensions. This exhausts a structured 13-vertex family while retaining exact integer arithmetic.

A second structural check should compare the full rooted-`U` collision relation of the two seeds with the pointed-loopy collision relation. If the only rooted-`U` matches are also pointed-loopy matches, then any future one-root construction whose `U` equality is justified merely by equality of rooted `U` is dead on this seed pair; that is a mechanism-level failure, not just another finite miss.

## Route B — #23 DO WHAT THE PROPOSER DID NOT EXPECT / simple-ify their multigraph counterexample

The source's Theorem 8.10 / Example 8.11 already has the desired separation `U_G=U_H` but `L_G!=L_H`; it fails Conjecture 8.2 only because the pair has parallel edges. Try to remove the parallel edges rather than perturb a simple collision. Keep one direct edge for each of the six underlying edges and replace each of the four extra parallel copies by an internally vertex-disjoint path. At the minimal source-relevant order 12 there must be exactly seven internal subdivision vertices across those four paths. There are only `C(6,3)=20` positive length-compositions on each side, hence 400 exact cross comparisons. A `U` collision with unequal `L` would be a source-level refutation at the minimum possible order; a total failure gives a clean obstruction to this natural simpleification route.

## Route C — #30 ONE SCALE / ONE DIRECTION AT A TIME

Stay at the first possible order `n=12` and in the direction `U_G=U_H` but `L_G!=L_H`. Do not launch a global order-12 graph search. First exhaust the two source-generated mechanisms above. If both fail, the next attack should leave one-root sums and independent parallel-edge subdivisions entirely: permit a new vertex to meet at least two old seed vertices (a genuine two-terminal/two-root gadget), because that is the first place the pointed information can mix rather than factor.

Finite failures remain PARTIAL. No source conjecture status is changed by this note.