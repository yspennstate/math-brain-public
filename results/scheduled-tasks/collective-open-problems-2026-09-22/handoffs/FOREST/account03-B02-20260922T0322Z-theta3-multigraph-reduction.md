# FOREST handoff — account03/B02 — theta_3 multigraph reduction

Outcome: **ESSENTIAL_STEP_APPLIED**. Parent target remains **OPEN**. Execution: `WITHOUT_VERIFIED_BRAIN`.

Consumed named partner result: `account04/B03`, run `20260922T001033Z-B03-r43`, handoff blob `65ef42469887361bf773ab19d1ebc48c7d2384cb`. That run proves full reconnection-cell support in a 3-connected graph and gives an exact local-cone witness showing that full support plus local sign-cluster/minor conditions alone do not force the FOREST inequality.

## New exact theorem

For every finite loopless multigraph `M`, replace every labelled edge `a=uv` by a fresh `theta_3` gadget: three internally vertex-disjoint two-edge `u-v` paths. The resulting graph `S(M)` is simple even when `M` has parallel edges.

Each gadget has exactly 27 acyclic states that disconnect its terminals and exactly 27 that connect them. Hence every multigraph forest has exactly `27^{|E(M)|}` forest lifts, so the uniform forest law of `S(M)` projects **exactly** to the uniform forest law of `M`.

If `x` is any fixed physical edge in the gadget for `a`, then
`P(x|a absent)=1/3` and `P(x|a present)=5/9`.
For physical edges `x,y` in distinct gadgets `a,b`, conditional independence inside the gadgets gives

`Cov_{S(M)}(x,y) = (4/81) Cov_M(a,b)`.

Therefore the unit-weight FOREST conjecture for all finite simple graphs is equivalent to the same conjecture for all finite loopless multigraphs. Loops can be discarded because they occur in no forest.

## Minimal-counterexample payoff

Choose an edge-minimal loopless-multigraph counterexample. For any violating pair `e,f` and third edge `g`, both deletion and contraction (after discarding contraction-created loops) have fewer nonloop edges. Thus the two `e,f` minor gaps `D0,D1` in the exact three-edge identity are nonnegative by **unit-weight minimality**, including the parallel-class contraction case that was previously unpaid in a simple-only minimality argument.

Consequently, if `Delta(e,f)<0`, then for every third edge `g`,

`Delta(g,e) Delta(g,f) > 0`.

So bad pairs form strict equivalence/sign clusters with no contraction-weight debt in this equivalent unit multigraph universe.

Exact checker/output: checker blob `73a1fdf23ba1bdc7d6cf13c9893004d17a340ff7`; output blob `4ed27e9cab8df85b56b4bd1198f73396cd957d1e`; terminal marker `THETA3_SIMULATION_PASS`.

Canonical scientific report: `math-open-problems` commit `5bc79835726a9011765e62ec8eecc35a04c06122`, blob `c60fbadfe8abd2e5b3afcf93c6b5ae45900c3de6`.

## Next exact obligation

The earliest remaining blocker is still the **graph-global compatibility** residual in the 3-connected reconnection/sign-cluster obstruction: rule out coupling of outside-forest local types that violates `n00*n11 <= n10*n01 + N*q` while satisfying the strict sign-cluster constraints for every third edge. The account04/B03 local-cone witness proves that a pointwise three-edge-matroid inequality cannot be enough.

Recipient: `account04/B03` and the FOREST lead. Suggested next mechanism: expose transitions between outside forests differing by one edge and search for a conserved/monotone terminal-partition quantity; test any proposed inequality first against the exact partner witness.

No full proof, graph counterexample, or novelty/priority claim is made.
