# FOREST overlapping-cycle path reconnection flow — fleet01/B03

Outcome: `ESSENTIAL_STEP_APPLIED`
Parent target: `OPEN`
Execution context: `WITHOUT_VERIFIED_BRAIN`
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`.

## Provenance and dependency use

The current `main` control snapshot assigns B03 to the FOREST target and explicitly stops new brain installation/benchmark work. I stayed on that workstream.

The current fleet01/B01 scientific root exposed start records but no complete lead proof body retrievable at the pinned control commit. The latest complete lead result named in the exact partner report is `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`, fleet01/B01 run `20260922T050946Z-b01-forest-auto11`; I use only the conditional-minimal-counterexample structure attributed to it below and do not upgrade any unavailable lead text.

Named OTHER-account result consumed and applied exactly:

`proofnet24/P14-probability-correlation/collective-2026-09-22/fleet02/B01/20260922T093400Z-b01-fleet02-forest-a5/reconnection_contraction_budget.md`

blob `03f0fd63758fcff5ba5d9bf89f3de36db508f01a`.

Its essential input is the contraction endpoint closure: in a minimal simple-graph counterexample, conditioning on a third edge `g` and contracting it may create parallel classes, but those positive integer activities can be represented by finite parallel-class expansion back to a simple lift. Consequently the contracted endpoint gap `D_1(g)` is nonnegative under the proper-minor hypothesis, just as the deletion endpoint `D_0(g)` is. I use this to isolate the remaining Simpson/reconnection debt rather than re-proving it.

## Exact count reduction

Fix distinct marked edges `e,f` of a finite simple graph `G`, and put

`G0 = G - {e,f}`.

Let `Omega` be the set of **all** forests of `G0`, with no restriction on size or number of connected components, and `N=|Omega|`. For `H in Omega`, define

- `X(H)=1` iff the endpoints of `e` lie in different components of `H`;
- `Y(H)=1` iff the endpoints of `f` lie in different components of `H`;
- `S(H)=1` iff both `e` and `f` may be added simultaneously while remaining acyclic;
- `Q(H)=X(H)Y(H)-S(H)`.

Write `n_ij = #{H: X(H)=i,Y(H)=j}` and `q = #{H: Q(H)=1}`. Then the desired pairwise negative correlation is exactly

`n00*n11 <= n10*n01 + N*q`.

Equivalently, after normalization,

`D = E[X]E[Y]-E[S] = P(Q)-Cov(X,Y) >= 0`.

A `Q` state has a particularly rigid form: after contracting every component of `H`, the two marked edges become parallel edges joining the same unordered pair of contracted components. This statement remains valid when `H` is disconnected and when `e,f` share a vertex.

## New lemma: exact three-channel one-edge reconnection flow

For every state `H` with `(X,Y)=(0,0)`, both marked edges are blocked. Since `H` is a forest, there are unique simple paths

`P_e(H)` and `P_f(H)`

inside `H` connecting the corresponding endpoint pairs.

Fix a base edge `g in E(G0)`.

### Channel E: exclusive `e` path

If

`g in P_e(H) \ P_f(H)`,

then `B=H-g` is in state `10`: deletion of `g` disconnects the endpoints of `e`, while the unique `f` path survives intact.

Conversely, take any state `B` in `10`. Let `C_e^0,C_e^1` be the two components of `B` containing the endpoints of `e`. If the base edge `g` crosses this component gap, then `g` is absent from `B`, `H=B+g` is a forest in state `00`, and

`g in P_e(H) \ P_f(H)`.

The two constructions are inverse. Therefore, edge by edge,

`#{H in 00 : g in P_e(H) \ P_f(H)}`

`= #{B in 10 : g crosses the e-gap of B}`.  (E)

### Channel F: exclusive `f` path

By symmetry,

`#{H in 00 : g in P_f(H) \ P_e(H)}`

`= #{B in 01 : g crosses the f-gap of B}`.  (F)

### Channel Q: common path

If

`g in P_e(H) intersect P_f(H)`,

then deleting `g` splits the tree component containing the common path into two components and **both** marked edges cross that same cut. Thus `B=H-g` has `X(B)=Y(B)=1`, while adding both marked edges creates the two-edge cycle in the contracted component graph. Hence `B` is a `Q` state.

Conversely, let `B` be a `Q` state. The marked edges join the same unordered pair of components, say `C^0,C^1`. For every base edge `g` crossing `C^0,C^1`, the graph `H=B+g` is a forest in state `00`, and `g` lies on **both** unique marked paths. Again the constructions are inverse. Therefore

`#{H in 00 : g in P_e(H) intersect P_f(H)}`

`= #{B in Q : g crosses the common marked component gap of B}`.  (Q)

This is the desired overlap-cycle reconnection estimate at edge resolution: overlap is represented by an exact flow to the `Q` term, not by a sectorwise correlation assumption.

## Multiplicity formulas and normalized flow

For `B in 10`, let `m_e(B)` be the number of base edges crossing its `e` component gap. Define `m_f(B)` analogously on `01`. For `B in Q`, let `m_Q(B)` be the number of base edges crossing its common marked component gap.

Summing (E), (F), (Q) over base edges gives the exact identities

`sum_{H in 00} |P_e(H) \ P_f(H)| = sum_{B in 10} m_e(B)`,

`sum_{H in 00} |P_f(H) \ P_e(H)| = sum_{B in 01} m_f(B)`,

`sum_{H in 00} |P_e(H) intersect P_f(H)| = sum_{B in Q} m_Q(B)`.

There is also an exact multiplicity-normalized form. Every target state with positive reconnection multiplicity receives exactly one unit of total incoming fractional mass:

`sum_{H in 00} sum_{g in P_e(H)\P_f(H)} 1/m_e(H-g)
 = #{B in 10 : m_e(B)>0} <= n10`,

`sum_{H in 00} sum_{g in P_f(H)\P_e(H)} 1/m_f(H-g)
 = #{B in 01 : m_f(B)>0} <= n01`,

`sum_{H in 00} sum_{g in P_e(H) intersect P_f(H)} 1/m_Q(H-g)
 = #{B in Q : m_Q(B)>0} <= q`.

States with multiplicity zero simply provide unused positive slack; no division by zero occurs because they have no incoming reconnection edge.

If `Omega00_cap` denotes the `00` forests with a nonempty common marked-path segment and `k=|E(G0)|`, then

`|Omega00_cap| <= sum_{H in 00}|P_e(H) intersect P_f(H)|
                  = sum_{B in Q}m_Q(B)
                  <= k*q`.

For the disjoint-path states `Omega00_dis`, each state has at least one exclusive edge on each path, hence

`|Omega00_dis| <= sum_{B in 10}m_e(B) <= k*n10`,

`|Omega00_dis| <= sum_{B in 01}m_f(B) <= k*n01`.

These last factor-`k` inequalities are only coarse corollaries; the normalized flow above is the more useful exact object.

## Boundary cases

1. **Disconnected forests.** All arguments are component-local. Unaffected components never enter the unique marked paths, and the proofs need no spanning or rooted assumption.
2. **Shared marked endpoint.** If `e,f` share a vertex and a deleted base edge lies on both marked paths, both marked edges cross the same post-deletion component cut, so the `Q` conclusion is unchanged.
3. **No base edges.** If `k=0`, a `00` state cannot exist because there is no path blocking either marked edge; the reconnection formulas are vacuous and the local target is trivial.
4. **Zero reconnection multiplicity.** Such `10`,`01`, or `Q` states have no incoming one-edge preimage and only create slack in the normalized inequalities.
5. **Simple input versus quotient parallelism.** `G` remains simple. The parallel pair occurs only after contracting components of a forest, which is exactly the `Q` geometry.

## Decisive counterexamples to over-strong overlap charging

The path-flow lemma also identifies two tempting but invalid shortcuts.

### Counterexample 1: unweighted one-to-one overlap charge

For `G=K4` with marked opposite edges `e=01`, `f=23`, the exact base-law enumeration gives

`|Omega00_cap|=4`, `q=2`,

while the common-path flow has total multiplicity `4`. Thus the stronger claim

`|Omega00_cap| <= q`

is false even in `K4`. Multiplicity normalization is genuinely necessary.

### Counterexample 2: the entire overlap sector cannot be paid solely by `N*q`

Take the five-vertex simple graph

`E(G)={01,02,03,04,12,14,23}`

with marked edges `e=03`, `f=04`. Exact enumeration over the 28 base forests gives

`(n00,n10,n01,n11)=(3,5,5,15)`, `q=1`, and `|Omega00_cap|=2`.

Hence

`|Omega00_cap|*n11 = 30 > 28 = N*q`.

So even after the exact common-path-to-`Q` reconnection is known, a valid proof cannot reserve the entire `N*q` term for the overlap sector in isolation. The `n10*n01` channel must be allowed to cross-subsidize overlap debt. Importantly, the FOREST inequality itself **holds** for this witness:

`n10*n01 - n00*n11 + N*q = 25-45+28 = 8 > 0`.

Thus this is a counterexample to a proof mechanism, not to the target conjecture.

## Exact finite regression

I independently enumerated every simple graph on at most five vertices and every unordered marked pair of present edges: **11,766 marked-pair instances** in total. Arithmetic and state classification were exact. The following all had zero failures:

- edgewise common-path/Q flow identity (Q);
- edgewise exclusive-e/10 flow identity (E);
- edgewise exclusive-f/01 flow identity (F);
- summed common-path multiplicity identity;
- coarse overlap bound `|Omega00_cap| <= k*q`.

The same regression finds the `K4` failure of the over-strong `|Omega00_cap|<=q` shortcut and the five-vertex failure of the isolated product charge `|Omega00_cap|*n11<=N*q` above.

This computation is validation of the finite identities, not a proof of the full conjecture.

## Compact conditional end-to-end argument and first remaining implication

Assume a minimal simple-graph counterexample `G,e,f` exists.

1. For every third edge `g`, proper deletion gives the conditioned deletion endpoint gap `D_0(g)>=0`.
2. Apply the named fleet02/B01 contraction result: after conditioning on `g` present, parallel-class lifting gives `D_1(g)>=0` despite contraction-induced positive integer activities.
3. Therefore any negative unconditioned gap must be created by the Simpson/reconnection term rather than by a bad endpoint measure. This is the conditioning structure attributed by the partner report to the lead's `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`.
4. Apply the new exact three-channel path-flow lemma. Every `00` forest decomposes at the level of one-edge deletions into exclusive-`e` flow to `10`, exclusive-`f` flow to `01`, and common-path flow **exactly** to `Q`; common-path multiplicity is controlled without discarding disconnected forests or overlapping cycles.
5. The five-vertex witness shows the remaining proof cannot simply split the target into `Omega00_dis*n11 <= n10*n01` and `Omega00_cap*n11 <= N*q`, because the second inequality is false. Hence the first essential missing implication is a **joint fractional matching/switching inequality** that allows capacity to move between the `(10)x(01)` and `Omega x Q` output channels while preserving the exact product count

   `n00*n11 <= n10*n01 + N*q`.

A sufficient next object would be a multiplicity-aware injection or fractional transport from `00 x 11` into the disjoint union `(10 x 01) union (Omega x Q)` whose local common-path edges use the exact normalized Q-flow above and whose exclusive-path edges use the exact normalized 10/01 flows. The counterexample proves that any construction forbidding cross-channel sharing is too rigid.

## Status

`ESSENTIAL_STEP_APPLIED`.

The full FOREST target remains `OPEN`. The concrete advance is the exact overlap-cycle reconnection lemma, including disconnected/boundary cases, together with a source-law counterexample that sharply rules out isolated `Q` charging and identifies the next genuinely necessary mechanism: a joint, multiplicity-aware two-channel transport.
