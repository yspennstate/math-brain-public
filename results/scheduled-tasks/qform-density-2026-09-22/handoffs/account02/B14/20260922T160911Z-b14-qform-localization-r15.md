# account02/B14 handoff — graphical inverse-gap localization

Run: `20260922T160911Z-b14-qform-localization-r15`  
Programme: `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`  
Status: **proved supporting localization theorem; full QFORM open**.

Canonical proof: `yspennstate/math-open-problems@cc52390bf9c5007889d0004bd994a3142225d54a`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260922T160911Z-b14-qform-localization-r15/REPORT.md`.

Assigned partner actually applied: account03/B14 global convex-mixture localization, `yspennstate/math-open-problems@871a2d4c9f1ea58d89748ab1abab05021b4408de`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B14/20260922T153828Z-account03-B14-QFORM-r13/REPORT.md`.

## New theorem

For a finite graph `G=(V,E)` with edge exponents `theta_e>=0`, the law-uniform moment

`E prod_{e={i,j}} |X_i-X_j|^-theta_e`

is finite uniformly over all independent real probability densities bounded by one **iff** every vertex cluster `S`, `|S|>=2`, satisfies

`sum_{e subset S} theta_e < |S|-1`.

The proof is support-free: expand into near-edge subgraphs, factor by connected components, order each component's coordinates, integrate out the common translation at cost one, use a max-flow allocation of edge exponents onto ordered gaps with load `<1`, and finish by one-dimensional beta-type gap integrals. The same constant is uniform under arbitrary separate deterministic shifts, hence under outside-conditioned shifts.

Necessity is exact: if one cluster reaches or exceeds `|S|-1`, the moment diverges already for iid `Uniform[0,1]`; equality gives logarithmic divergence. Thus this is a mechanism-level obstruction, not a QFORM counterexample.

The previous triangle condition `a,b,c<1`, `a+b+c<2` is exactly the three-vertex case. A useful new control is `K4` with all six exponents `1/2`: total cluster exponent `3=4-1`, so the raw absolute graph compiler diverges logarithmically.

## Partner application

Using account03/B14's law-level convex-mixture localization, a local certificate may choose its active original-coordinate block, graph, exponents and shifts **separately for each compact extreme-product mixture component**. If active size is uniformly bounded by `m0`, all cluster slacks are uniformly at least `delta0>0`, and the conditional shell coefficient is `K`, then the arbitrary-support target law inherits one finite bound `K C(m0,delta0)` by convex mixing and TV passage. No single physical triple or graph is required to serve every mixture component.

This respects `QFORM-ONE-TRIPLE-RANK2-AGGREGATE-UNIFORM-FALSE-v1`; existence of the required componentwise graph certificate remains unpaid.

## First remaining implication

For each unresolved heavy/localized branch, derive a deterministic-outside shell/coarea estimate whose singular factor is a uniformly bounded-size shifted pair-gap graph with positive cluster slack. If the actual shell forces some collision cluster to critical exponent `|S|-1`, the iid-uniform divergence theorem proves that raw absolute integration cannot close that branch; retain cancellation/operator aggregation instead.

Control/correction snapshot immediately before the canonical scientific write: `yspennstate/math-research-brain@949e6ab6b5a141d41667fa08551b256b40401003`. No moment, support-radius, bounded-diameter, finite-fragment-count, post-rotation independence, or one-uniform-triple assumption is used.
