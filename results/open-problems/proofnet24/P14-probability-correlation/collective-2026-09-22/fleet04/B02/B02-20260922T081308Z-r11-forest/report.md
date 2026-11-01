# FOREST / fleet04-B02 — exact split-lift of the STAR-2 contraction law and a path-cut flow obstruction

Run: `B02-20260922T081308Z-r11-forest`  
Programme: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Outcome: **ESSENTIAL_STEP_APPLIED**  
Subsidiary candidate: `FOREST-UNIFORM-PATH-CUT-FLOW-v1` — **CANDIDATE_REFUTED**  
Parent target: **OPEN**  
Brain context: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact source state consumed

The target is the Grimmett--Winkler uniform-unrooted-forest pairwise inequality: for every finite simple graph `G`, with `F` uniform over all acyclic edge subsets (all sizes, including disconnected forests), prove for distinct present edges `e,f`

`P(e,f in F) <= P(e in F) P(f in F)`.

The latest complete lead version consumed is fleet01/B01 run `20260922T050946Z-b01-forest-auto11`, canonical report blob `adc332e97b112525d92cf601ad1493f2e1745987` in the preceding complete lead lineage and receipt blob `e8fca95b279e2172cafedb222c50af983927c0f7`. Its source-safe new obstruction is the triangle-contraction `STAR-2` law: contracting a triangle edge `g=uv` and simplifying produces a smaller simple graph with weight `2` on a subset of one star at the contracted vertex and weight `1` elsewhere. The lead correctly does not assume that unit negative correlation of a fixed graph automatically implies this weighted statement.

The named other-account partner used here is fleet01/B03 run `20260921T234923Z-b03-poprestore-r11`, report blob `4dbaa2d764eddbc02026736e5b1fe265ba14f24d`. Its exact comparison, for `K=G-{e,f}`, is

`Delta = n10*n01 - n00*n11 + N*q`,

where `n_ij` are the two addability-cell multiplicities and `q` is the overlap reservoir in which the two individually legal reconnections join the same two forest components. Equivalently, the target is

`n00*n11 <= n10*n01 + N*q`.

I retain this `q` term exactly; no overlap-free strengthening is assumed.

## 2. New exact split-lift theorem

Let `H` be a finite simple graph, let `x` be a vertex, and let `D` be any subset of the star `delta_H(x)`. Give each edge of `D` weight `2` and every other edge weight `1`. For a forest `A` of `H`, its weight is therefore

`w(A)=2^{|A cap D|}`.

Construct a simple split graph `L=L(H,x,D)` by replacing `x` with two vertices `u,v`. For every doubled edge `xw in D`, put **both** `uw` and `vw` in `L`; for every undoubled edge `xw notin D`, put exactly one copy, say `uw`; every non-star edge is unchanged. Let

`S = {B subset E(L): B is a forest and u,v are in different components of B}`.

**Theorem (split-lift).** Identifying `u,v` back to `x` defines a surjection `pi:S -> Forest(H)` and every forest `A` of `H` has exactly

`|pi^{-1}(A)| = 2^{|A cap D|}`

preimages. Consequently the weight-`{1,2}` forest law on `H` is exactly the push-forward of the **uniform** law on `S`.

**Proof.** If `A` is a forest of `H`, choose independently, for each selected doubled star edge `xw`, whether its lift is `uw` or `vw`; undoubled selected star edges use their unique lift and non-star edges are unchanged. A cycle in a lift would project to a closed walk in `A` containing a cycle. A `u-v` path in a lift would likewise project, after identifying `u,v`, to a nontrivial closed walk in `A` and hence contain a cycle. Thus all `2^{|A cap D|}` choices lie in `S`.

Conversely, a separating forest `B in S` cannot contain both `uw` and `vw` from one doubled class, since those two edges form a `u-w-v` path. If `pi(B)` contained a cycle, lifting that projected cycle either gives a cycle in `B` (when the two incidences at `x` lift to the same split vertex) or a `u-v` path (when they lift to different split vertices). Both are forbidden. Hence `pi(B)` is a forest. The only choices in its fibre are the independent two-colour choices on selected doubled classes, giving the asserted multiplicity. QED.

### Source-generated specialization

Now take an actual simple graph `G` and a triangle conditioner `g=uv`. Put `L=G-g`. Contracting `g` identifies `u,v` to `x`; every common neighbour `w` of `u,v` produces a parallel pair `uw,vw`, which becomes one simple edge `xw` of weight `2` after simplification. The split graph above is then exactly `G-g`, with the original incidences restored. Therefore the lead's source-generated `STAR-2` conditional law is not an opaque weighted measure:

> it is exactly the uniform forest law of the smaller simple graph `G-g`, conditioned on `u` and `v` being disconnected.

For a marked edge that belongs to a doubled parallel class, the event for one colour has one-half the aggregate-class probability (and similarly for joint events with an external marked edge), so the sign question reduces to the aggregate weighted edge. The case in which the two marked edges are the two parallel colours is automatically strictly negative because they cannot coexist.

This representation retains every component multiplicity exactly and uses no rooted, spanning or fixed-size replacement.

## 3. Exact comparison with fleet01/B03

Let `S` denote the separating forest family above and consider the contracted weighted graph (equivalently, coloured split fibres) with marked edges `e,f`. Remove `e,f`, classify the remaining separating states by whether each marked reconnection is addable, and let

`n00^S,n10^S,n01^S,n11^S,N_S,q_S`

be the **multiplicity-weighted** analogues of fleet01/B03's cells and overlap reservoir. The partner's derivation is purely a partition of forest states, so it applies fibre-by-fibre and gives exactly

`Delta_S = n10^S*n01^S - n00^S*n11^S + N_S*q_S`.

Thus the lead's `STAR-2` implication is equivalent to the source-simple conditional reconnection inequality

**(SR4)**  `n00^S*n11^S <= n10^S*n01^S + N_S*q_S`.

No multiplicity disappears: a separating split forest mapping to a contracted forest with `k` selected doubled classes contributes one of exactly `2^k` colourings on both sides of (SR4).

This is the first exact missing implication for the present coupling route. If (SR4) were proved for every source-generated triangle contraction in an edge-minimal counterexample, then the lead's deletion/contraction total-covariance step would extend from triangle-free conditioners to triangle conditioners as well. That would restore the lead's all-conditioner Simpson inequalities; a later global contradiction would still be needed before claiming the parent theorem.

## 4. A different exchange graph on the separation boundary

The split theorem suggests a direct exchange mechanism that is different from my earlier bounded-radius two-forest Hall switches.

Write `C` for the forests of `L` in which `u` and `v` are connected. For `T in C`, let `P_T` be its unique `u-v` path. For `F in S`, let `U_F,V_F` be the components containing `u,v`, and put

`r(F)=|E_L(U_F,V_F)|`.

There is an exact incidence bijection

`(T,h),  T in C, h in P_T   <-->   (F,h), F in S, h in E_L(U_F,V_F)`

via `F=T-h` and `T=F+h`. Hence for every function `phi` on separating forests,

**(EX)**  `sum_{T in C} sum_{h in P_T} phi(T-h) = sum_{F in S} r(F) phi(F)`.

This is an exact component-multiplicity identity. It exposes the precise obstacle to turning path cutting into the desired uniform conditional law: the boundary is biased by the terminal cut size `r(F)`.

## 5. Genuine source-valid counterexample to the naive normalized path-cut coupling

A tempting repair is `FOREST-UNIFORM-PATH-CUT-FLOW-v1`: from each connected forest `T`, choose an edge of `P_T` uniformly and delete it. This has row mass one, so one might hope its image is uniform on `S`.

It is false already on the simple triangle `L` with terminals `u=0,v=1` and edges `01,02,12`. The separating forests are

`emptyset`, `{02}`, `{12}`.

Their incoming masses under uniform path cutting are respectively

`1`, `3/2`, `3/2`.

For example `{02}` can be obtained from `{01,02}` by deleting the length-one `01` path edge (mass `1`) and from `{02,12}` by deleting `12` from the length-two path (mass `1/2`). The empty forest has only the first type and receives mass `1`.

Therefore uniform cutting does **not** produce the uniform separating law even in the smallest cyclic simple graph. Any successful separation coupling must compensate on both sides of (EX), or directly route the fleet01/B03 ordinary and `q` channels; normalizing only by the connected path length is insufficient.

This counterexample is to the coupling candidate only, not to Grimmett--Winkler and not to (SR4).

## 6. Exact finite audit

`forest_star2_checker.cpp` performs independent exact integer checks.

1. It enumerates every simple graph on `n=3,4,5`, every centre, every nonempty subset of that centre's incident edges to double, and every marked edge pair. Across `21,400` star-weight configurations and `319,554` pair tests it finds **zero negative Rayleigh gaps**. This is finite evidence only.
2. It independently constructs the split lift for every such configuration through `n=4`; all `640` weighted-partition-function identities pass.
3. As a side diagnostic, it searches simple two-terminal gadgets with at most six edges (through six vertices) for an effective connected/disconnected forest-count ratio exactly `2`; none of `10,871` candidates has that ratio. The seven-edge gadget consisting of the terminal edge plus three internally disjoint two-edge terminal paths has counts `A=27`, `B=54`, hence ratio `2`. This shows an exact unweighted gadget simulation exists, but it enlarges the graph and therefore does not by itself pay an edge-minimal induction.
4. The triangle normalized-cut obstruction above is checked exactly.

The executable terminates `ALL_EXACT_ASSERTIONS_PASSED`.

## 7. Source boundary

Semple--Welsh, *Negative Correlation in Graphs and Matroids*, Combin. Probab. Comput. 17 (2008), Proposition 3.7, shows closure of **independence-correlated** matroids under series/parallel extension, while explicitly distinguishing that stronger weighted property from merely knowing the unit graph conjecture for one graph. Cocks, *Correlated Matroids*, Combin. Probab. Comput. 17 (2008), states a class-level equivalence between the Grimmett--Winkler conjecture and correlated graphic-matroid formulations. Neither result is used here to infer the source-generated STAR-2 comparison from a unit statement on one smaller graph.

## 8. Status and next mathematical action

**Outcome: `ESSENTIAL_STEP_APPLIED`.** The parent conjecture remains **OPEN**. The new exact advance is the split-lift theorem and the consequent source-simple formulation (SR4), which preserves the partner's overlap reservoir and all `{1,2}` component multiplicities. The first attempted boundary flow is decisively refuted by the triangle.

The next coupling target is now concrete: construct a two-sided flow on the incidence graph (EX), with cell labels for `e,f`, whose cut-size compensation proves (SR4) and whose overlap destinations are exactly the partner `q_S` states. A proof must control arbitrary subsets/flows, not just average degrees; alternatively, an exact source-generated counterexample to (SR4) would refute the lead's STAR-2 route without refuting the parent conjecture.

No claim of novelty or full proof is made.