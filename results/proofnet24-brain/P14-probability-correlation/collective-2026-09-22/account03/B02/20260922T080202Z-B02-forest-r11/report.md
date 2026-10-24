# account03/B02 FOREST report — exact three-edge-cut exclusion for a bad pair

Run: `20260922T080202Z-B02-forest-r11`  
Outcome: **ESSENTIAL_STEP_APPLIED**  
Parent FOREST target: **OPEN / not promoted**  
Execution context: `WITHOUT_VERIFIED_BRAIN`

Exact assignment: prove a useful minimal-counterexample reduction covering a genuinely unresolved three-connected obstruction, not merely another finite graph class. Assigned partner: `account04/B03`.

## 1. Fresh state and named peer result consumed

Fresh owner control remains revision `2026-09-22.2`, programme `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`; no later stop was observed before the scientific writes. The old installation/benchmark role remains superseded.

Named OTHER-account result consumed and applied:

`proofnet24/P14-probability-correlation/collective-2026-09-22/account04/B03/20260922T053904Z-B03-forest-r13/report.md`, blob `343a7f8f5aa2583e5fac80b1fb1f2d1ce2b8cbd5`, candidate `FOREST-3CONN-VARIANCE-SQUEEZE-v1`.

That report starts from the current minimal-counterexample package: a lexicographically minimal bad pair `(G,e,f)` is in a 3-connected graph; writing `G0=G-{e,f}` and `H` for the uniform forest of `G0`, the addability variables

`X=1{H+e forest}`, `Y=1{H+f forest}`, `S=1{H+e+f forest}`

satisfy `delta=E[S]-E[X]E[Y]>0` in a counterexample. Its per-third-edge inequalities and aggregate rank squeeze leave a genuinely graph-global 3-connected obstruction unpaid.

My immediately preceding B02 result replaced the rank denominator by the full covariance-inverse parameter `kappa`, but still did not contradict `delta>0`. This run changes mechanism: instead of another covariance squeeze, it attacks the edge-separator topology of the marked bad pair exactly.

## 2. New theorem: two members of a 3-edge cut are always negatively correlated

### Theorem 2.1 — exact triad-cut formula

Let `G` be a finite simple graph and suppose a vertex bipartition `V=L disjoint_union R` has exactly three crossing edges `{e,f,g}`. Under the uniform law on **all** forests of `G`, the pair `e,f` is nonpositively correlated. More precisely, let

- `Z_L,Z_R` be the numbers of forests of the two induced side graphs after removing the three cut edges;
- on side `L`, let `A_L,B_L,C_L,T_L` count side forests in which respectively the boundary endpoints of `(g,e)`, `(g,f)`, `(e,f)`, or all three boundary endpoints are connected;
- define `A_R,B_R,C_R,T_R` analogously.

Then the exact Rayleigh gap is

`Z_e Z_f - Z Z_ef`

`= A_L A_R B_L B_R + 4 Z_L Z_R (C_L C_R - T_L T_R) >= 0`.      (2.1)

If the three-edge cut is a bond and each side is connected, then the first product in (2.1) is strictly positive, hence `e,f` are **strictly** negatively correlated.

### Proof

Delete `e,f` but retain `g`, and sample a uniform forest `H` of `G-{e,f}`. Removing `g` separates the graph into the two sides. Therefore

1. the two side forests `J_L,J_R` are independent and uniform;
2. `T=1{g in H}` is an independent fair Bernoulli variable, because `g` is a bridge of `G-{e,f}`.

For `s in {L,R}`, define the side connectivity indicators

`U_s=1{g_s connected to e_s in J_s}`,
`V_s=1{g_s connected to f_s in J_s}`,
`W_s=1{e_s connected to f_s in J_s}`,
`Q_s=1{all three boundary terminals connected in J_s}`.

Because `J_s` is a forest, connectivity is an equivalence relation on the three terminals, so

`U_s V_s = U_s W_s = V_s W_s = U_s V_s W_s = Q_s`.            (2.2)

Across both sides put

`A=U_L U_R`, `B=V_L V_R`, `C=W_L W_R`, `Q=Q_L Q_R`.

The event `A=1` is exactly that the pair `{g,e}` would close a cycle when both are present; similarly for `B` and `C`. From (2.2),

`AB=AC=BC=ABC=Q`.                                               (2.3)

Let

`alpha=E[A]`, `beta=E[B]`, `gamma=E[C]`, `tau=E[Q]`.

Since the sides are independent,

`alpha=(A_L/Z_L)(A_R/Z_R)`,
`beta =(B_L/Z_L)(B_R/Z_R)`,
`gamma=(C_L/Z_L)(C_R/Z_R)`,
`tau  =(T_L/Z_L)(T_R/Z_R)`.

Now calculate the exact addability probabilities used by the minimal-counterexample formulation.

For `e`, the only obstruction in `H` is that `g` is present and `{g,e}` closes a cycle, hence

`x=E[X]=1-alpha/2`.

Similarly `y=1-beta/2`.

For simultaneous addability of `e,f`:

- if `g` is absent, the only possible cycle using the cut uses `e,f`, so `S=1-C`;
- if `g` is present, any cycle crosses the cut an even number of times and, with only three crossing edges available, it uses one of the three pairs. Thus `S=(1-A)(1-B)(1-C)`.

Using (2.3),

`(1-A)(1-B)(1-C)=1-A-B-C+2Q`.

Therefore

`r=E[S]=1-(alpha+beta)/2-gamma+tau`.

Consequently

`xy-r = gamma-tau + alpha beta/4 >= alpha beta/4 >= 0`,          (2.4)

because `Q_s<=W_s` on each side, hence `tau<=gamma`.

Finally, if `Z0` denotes the forest count of `G-{e,f}`, then every pair of side forests has two choices for `g`, so `Z0=2 Z_L Z_R`. The standard two-edge expansion gives

`Z_e Z_f-Z Z_ef = Z0^2 (xy-r)`.

Substitution into (2.4) yields exactly (2.1).

If the cut is a bond with connected sides, there is at least one side forest connecting each relevant pair of boundary endpoints, so all four factors `A_L,A_R,B_L,B_R` are positive. Hence the gap is strict. QED.

## 3. Minimal-counterexample consequence

The current route already places a minimal bad pair `(G,e,f)` in a 3-connected graph. Hence `G` is 3-edge-connected.

Suppose `G0=G-{e,f}` had a bridge `g`. Then deleting `{e,f,g}` disconnects `G`. Since no cut of size one or two exists in a 3-connected graph, `{e,f,g}` is a three-edge cut. Theorem 2.1 would make `e,f` strictly negatively correlated, contradicting that they are the bad pair.

Therefore every remaining minimal obstruction satisfies the stronger structural condition

`G-{e,f} is connected and bridgeless`.                           (3.1)

Equivalently, **every third edge lies on a cycle already after deleting the two marked bad edges**. The previous route needed only connectedness of `G0`; (3.1) rules out the entire bridge/three-edge-bond configuration for the marked pair.

A small additional consequence relevant to the covariance-squeeze route is that every third edge of `G0` is a non-coloop of its graphic matroid. For a non-coloop `g`, `Ind(M/g)` is a strict subset of `Ind(M\\g)` (take a circuit through `g` and remove `g`), so under the uniform independent-set law

`P(g in H) < 1/2`.                                               (3.2)

Thus none of the third-edge coordinates in the current obstruction can attain the coloop equality case used in the partner's variance bound.

## 4. Exact finite regression

The theorem is symbolic. A separate exact enumerator beside this report checks every labelled simple graph on `2,3,4,5` vertices, every canonical vertex cut with exactly three crossing edges, and each of the three marked pairs in that cut. It independently computes the full forest Rayleigh gap and the right-hand side of (2.1).

Captured output:

`graphs_checked=1098`
`three_cut_pair_cases=12300`
`formula_or_sign_violations=0`
`three_edge_connected_cases=252`
`three_edge_connected_non_strict=0`
`minimum_strict_integer_gap=44`
`STATUS=PASS`

Checker SHA-256: `fe875b4e965c6de72d7108284ce6e1deb9bf2e1f0b03149cb31a0061da0e1f13`.

Output SHA-256: `db8e8f89e4ad89df96704200c7ed42e0bc7fedff3c19ff761386ddbf6a924532`.

The finite run is regression evidence only; the all-graph statement is proved in Section 2.

## 5. What this pays and what remains

**Paid:** a bad pair in a 3-connected minimal counterexample cannot occupy two edges of any three-edge cut. In particular `G-{e,f}` cannot have a bridge. This directly removes one universal separator obstruction from the exact minimal-counterexample route and supplies a manifestly nonnegative count formula rather than another finite class.

**Still unpaid:** a 3-connected graph can have three-edge cuts not containing both marked edges, and can have larger separators or no small separators at all. The new theorem therefore does not close the parent FOREST conjecture. The first remaining structural debt is to handle a three-edge separation where `e,f` lie on one side or on different non-cut positions, or else prove that a minimal bad pair can be chosen to meet a three-edge cut twice. That is now the natural next decomposition question before another analytic squeeze.

The separate complete-graph/Cocks/minor route remains a distinct full-proof candidate and is neither used nor certified by this report.

## 6. Integrity

Only the private mathematics repository, the named partner artifact, and local exact combinatorics were used. No authenticated brain retrieval/context activation occurred; `full_brain_connected=false`. No installation, benchmark, scheduler repair, email, Drive, public posting, workflow dispatch, paid model/API/Codex call, credential access, or cross-account native mutation was performed. No historical or peer artifact was modified.
