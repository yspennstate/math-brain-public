# FOREST / account04 B01 — class-wide weightedization and exact 0/1/2-separator reduction

**Run:** `account04-b01-20260922T080833Z-forest-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Candidate:** `FOREST-GLOBAL-WEIGHTED-3CONN-GLUING-v1`  
**Parent FOREST:** `OPEN`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`

## 1. Control and source scope

Entry controls were read at exact `math-research-brain` main commit `0d9b42fe9eca9868300f5e4048924dc150aa5eee`, owner revision `2026-09-22.2`. The active collective order is `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`; new brain installation/benchmark work is stopped for B01. The target remains the unit uniform law on **all** acyclic edge subsets of a finite simple graph.

Exact owner-source blobs read at entry include ORDER `a70e03208ae00795ca7c6cdf9b7dbce854347138`, TARGETS `a8cafa98cdb074ed15d0e214f8f54ee514c500df`, and ASSIGNMENTS `fe144a4be3522d57f8cb2dc40b1fc57df7c7f7da`.

Latest complete team-lead version actually read: account01/B01 `20260922T050946Z-b01-forest-auto11`, report creation commit `79044b575c4b689248892f37b9930e983dddabca`, handoff blob `4cee205cb7d254caf785692838111988a0b8a155`. It correctly rejects the old fixed-graph Cocks globalization and says the inherited 3-connected reduction is not unconditional.

Assigned partner version actually read: account01/B02 `20260922T065223Z`, handoff blob `2ceae194c5ea9a49dc7db3baccef2ae27bd8e95a`; its weighted `K4` formulas and parallel-class lemma are retained.

Named OTHER-account result actually consumed and applied: account02/B01 `B01-20260922T072913Z-forest-r17`, handoff blob `69c943a3c34bcd9edb16b0eb9a6a611384817540`. In particular I use its exact mixed/equal-length theta response calculation. I do **not** inherit its PASS as evidence for the theorem below.

The requested canonical `proofnet24/.../account04/B01/<run-id>/` create was attempted once and denied by the connector write guard. I did not bypass the guard; this immutable report and the source-bound handoff are therefore published under the already-authorized shared collective-work path.

## 2. Notation

For positive edge activities `y=(y_h)` define the forest polynomial

`Z_G(y)=sum_{F acyclic} prod_{h in F} y_h`.

For distinct edges `e,f` put

`Delta_G(e,f)=Z_e Z_f-Z Z_ef`.

The desired negative correlation is equivalent to `Delta_G(e,f)>=0`, since

`Cov(1_e,1_f)=- y_e y_f Delta_G(e,f)/Z^2`.

Because `Z=A+y_e B+y_f C+y_e y_f D`, one has

`Delta_G(e,f)=BC-AD`.

Hence the Rayleigh difference is independent of the two marked activities `y_e,y_f`. This elementary observation is important below: the marked edges may be left as literal unit edges during unitization.

## 3. Theorem A — unit simple graphs imply all positive activities on simple graphs

### 3.1 Exact theta response

Let `Q(k,a)` be `k` internally vertex-disjoint `u-v` paths of common length `a>=2`, with all physical edges of weight one. It is a finite simple graph. A single length-`a` path has exactly one terminal-connecting forest and `2^a-1` terminal-disconnecting forests. Since two connecting paths would make a cycle, for the whole theta network

`D_Q=(2^a-1)^k`,

`C_Q=k(2^a-1)^(k-1)`,

and therefore its two-terminal response is

`r_Q=C_Q/D_Q=k/(2^a-1)`.

This is the account02/B01 theta response, here used in a different class-wide substitution argument.

The set `{k/(2^a-1): a>=2,k>=1}` is dense in `(0,infinity)`: for fixed `x>0`, take `a->infinity` and `k_a=max(1,round(x(2^a-1)))`.

### 3.2 Simultaneous substitution factorization

Fix a finite simple base graph `G` and marked edges `e,f`. For every unmarked base edge `h`, delete `h` and insert a two-terminal simple unit network `N_h` with fresh internal vertices; different networks have disjoint internal vertices. Let `D_h,C_h` be its disconnect/connect forest sums and `r_h=C_h/D_h`.

A forest of the substituted graph `H` determines, for each `N_h`, whether its terminals are connected. The set of base edges whose networks connect must be a forest in `G`: a macro cycle would lift to a cycle in `H`. Conversely, if the macro set is a forest, any choice of local forest states with those connect/disconnect labels has acyclic union, because every network meets the rest of the graph only at its two terminals. Consequently

`Z_H(1)= (prod_{h notin {e,f}} D_h) Z_G(r; y_e=y_f=1)`.

The literal marked edges are untouched, so the same factor multiplies `Z_e`, `Z_f`, and `Z_ef`. Therefore

`boxed: Delta_H(e,f;1)=(prod_h D_h)^2 Delta_G(e,f;r).`

Now suppose the original unit FOREST conjecture holds for **every finite simple graph**. Choose theta networks independently so that all `r_h` converge to arbitrary prescribed positive activities `y_h`. Every substituted `H` is again finite and simple, hence its unit Rayleigh difference is nonnegative. Divide by the positive square factor and take the finite-dimensional limit. Polynomial continuity gives `Delta_G(e,f;y)>=0` for arbitrary positive activities. The marked activities are immaterial by Section 2.

Thus

`boxed: UNIT-SIMPLE(all G) <=> POSITIVE-WEIGHT-SIMPLE(all G).`

The reverse implication is the specialization `y=1`. No fixed-graph Cocks implication is used.

## 4. Theorem B — exact all-parameter two-separator gluing

Let `G` be a positive-weight simple graph that is 2-connected and let `{u,v}` be a genuine 2-vertex cut. Its `uv`-bridges are the subgraphs induced by the components of `G-{u,v}` together with their incident edges to `u,v`; if the original edge `uv` exists, treat that edge as a separate singleton bridge. Thus every non-singleton bridge contains **no** `uv` edge.

For bridge `B_i`, let

`D_i =` forest sum with `u,v` disconnected,

`C_i =` forest sum with `u,v` connected.

All `D_i,C_i` are positive except that the singleton formulas are simply `D=1,C=y_uv`.

A union of bridge forests is globally acyclic iff at most one bridge connects `u` to `v`. Hence the exact partition identity is

`boxed: Z_G=prod_i D_i + sum_i C_i prod_{j!=i} D_j.`

### 4.1 Both marks in the same bridge

Take `e,f in B_i`. Put

`A_i=prod_{j!=i}D_j`,

`lambda_i=sum_{j!=i} C_j/D_j >0`.

Then

`Z_G=A_i [C_i+(1+lambda_i)D_i]`.

For a non-singleton `B_i`, add a new virtual edge `g_i=uv` of activity `lambda_i`. Since `B_i` has no original `uv` edge, `H_i=B_i+g_i` is simple, and

`Z_{H_i}=C_i+(1+y_{g_i})D_i`.

The outside factor is independent of `e,f`, so

`boxed: Delta_G(e,f)=A_i^2 Delta_{H_i}(e,f)|_{y_g=lambda_i}.`

This is the required all-parameter virtual-edge law. The virtual activity is allowed to be an arbitrary positive real number; no unit-to-fixed-graph inference is being made.

### 4.2 Marks in different bridges

Let `e in B_i`, `f in B_j`, `i!=j`, and put

`A_ij=prod_{k notin {i,j}}D_k`,

`s=1+sum_{k notin {i,j}} C_k/D_k`.

Then

`Z_G/A_ij=sD_iD_j+C_iD_j+D_iC_j`.

Direct differentiation and cancellation give

`boxed: Delta_G(e,f)=A_ij^2 R_i(e) R_j(f),`

where

`R_i(e)=D_i C_{i,e}-C_i D_{i,e}`.

For a non-singleton bridge,

`R_i(e)=Delta_{B_i+g_i}(e,g_i)`

for **any** positive activity assigned to the virtual edge `g_i`; the expression is independent of that activity. If `B_i` is the singleton original separator edge and `e=uv`, then `D_i=1,C_i=y_e,D_{i,e}=0,C_{i,e}=1`, hence

`boxed: R_i(e)=1.`

Therefore the original `uv` edge is handled exactly as a singleton bridge. No parallel virtual edge is ever introduced, and no separator-edge boundary case is omitted.

## 5. Theorem C — weighted 3-connected cores are exactly the remaining class

Assume every positive-weight 3-vertex-connected finite simple graph is Rayleigh. I prove every positive-weight finite simple graph is Rayleigh by induction on its edge count.

* If `G` is disconnected, its forest polynomial factors over components. Marks in different components have `Delta=0`; marks in one component give the component Rayleigh difference times a positive square.
* If `G` has a cut vertex, the same argument applies to its 1-sum/block factorization.
* Now let `G` be 2-connected. If `G=K3`, direct expansion gives, for the third edge of activity `z`, `Delta=z(1+z)>0`.
* If `G` has no 2-cut and at least four vertices, it is 3-connected and is safe by hypothesis.
* Otherwise choose a genuine 2-cut and apply Section 4.

For the induction in the last case, every non-singleton component bridge `B_i` meets both `u` and `v`: otherwise one of the cut vertices would itself be an articulation point. Since a genuine 2-cut has at least two components of `G-{u,v}`, there is another non-singleton bridge with at least two edges. Hence

`|E(B_i+g_i)| <= |E(G)|-1`.

The augmented graph is simple by the singleton convention. Thus every augmented `H_i=B_i+g_i` appearing in the same-bridge or cross-bridge identities is a **strictly smaller positive-weight simple graph**, so the induction hypothesis applies at its actual virtual activity. The identities in Section 4 then force `Delta_G>=0` for every marked pair.

Consequently

`boxed: POSITIVE-WEIGHT-SIMPLE(all G) <=> POSITIVE-WEIGHT-SIMPLE(3-connected G).`

Combining with Theorem A gives the source-level equivalence

`boxed: UNIT-SIMPLE(all G) <=> POSITIVE-WEIGHT-SIMPLE(3-connected G).`

This is the all-parameter three-connected reduction that the old fixed-graph Cocks step was trying to supply, but it follows from class-wide theta substitution plus exact separator induction and therefore does not use that disputed implication.

## 6. Partner result applied and immediate localization

The assigned partner account01/B02 `20260922T065223Z` proves weighted `K4` directly, for both adjacent and disjoint marked pairs, and proves the corresponding parallel-class collapse lemma. Together with the direct weighted `K3` calculation above, Theorem C implies that any surviving weighted 3-connected counterexample produced by the reduction has at least five vertices. This is a genuine narrowing, but not closure.

The team lead's `STAR-2` debt is no longer needed merely to justify the **existence of a 3-connected weighted core**: triangle contraction can be bypassed for this separator task. STAR-2 may still be useful for the lead's separate Simpson/minimal-*unit*-counterexample program.

## 7. Compact conditional end-to-end argument

A complete proof of the parent target would follow from the single structural core statement:

> Every finite 3-connected simple graph is Rayleigh for every positive choice of edge activities.

Indeed, Theorem C propagates that statement through every disconnected, 1-separator, and 2-separator case with the exact induced virtual activities, and Theorem A then specializes back to the original unit uniform-forest law (or simply evaluate the resulting weighted theorem at one).

Conversely, if the source unit conjecture fails, the failing unit graph is already a positive-weight counterexample. Choose a positive-weight simple counterexample with the minimum number of edges. The induction proof above forces it to be 3-connected. By the partner's weighted `K4` result, it has at least five vertices.

This identifies the first unpaid implication without hiding any separator debt: rule out a positive-weight Rayleigh failure on a 3-connected simple core of order at least five. That core statement is not claimed here.

## 8. Exact regression computation

Computation is regression only, not proof. The committed exact-`Fraction` checker `FOREST-CHECK-account04-B01-20260922T080833Z.py` verifies:

1. theta substitution on a weighted triangle with third-edge response `2/3`, giving weighted gap `10/9`, unit substituted gap `90`, and scale `81`;
2. a same-bridge two-cut instance with an original singleton `uv` edge, giving direct gap `3024`, virtual-edge gap `84`, and scale `36`;
3. a cross-bridge instance on the same graph, giving direct gap `48` and response factors `4` and `12`.

The exact output terminates `STATUS=PASS`.

## 9. Failure/correction record

* The fixed-graph implication `unit-good G => weighted-good same G` is **not** used.
* I do not use the lead's rank-homogeneous complete-log-concavity assertion; this report is independent of that disputed source point.
* No finite census, search miss, auxiliary constant, or peer PASS is counted as closure.
* The parent conjecture is not solved here; status remains `OPEN`.
* The requested canonical scientific-root write was blocked by the connector guard, and I did not attempt a permission bypass. The shared collective path is the authorized fallback used for durable artifacts.

## 10. Status

**`ESSENTIAL_STEP_APPLIED`.** The all-parameter 0/1/2-separator gluing and 3-connected reduction are paid, including the original separator-edge singleton case, and the reduction is source-secure without fixed-graph Cocks. The first remaining mathematical core is positive-weight Rayleigh on 3-connected simple graphs of order at least five.
