# FOREST / fleet04 B01 — exact rational unitization and source-secure 3-connected reduction

**Run:** `fleet04-b01-20260922T051009Z-forest-r12`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Candidate:** `FOREST-Q-3CONN-EXACT-v1`  
**Parent target:** OPEN  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`

## 1. Current source state and the corrected route

The newest complete lead version consumed is fleet01/B01 run `20260922T043718Z-b01-forest-auto11`, report blob `adc332e97b112525d92cf601ad1493f2e1745987`. It correctly withdraws `FOREST-KN-COCKS-RECONCILED-v3`: the previously used implication

`unit pNC on one fixed G => positive-weight Rayleigh pNC on that same G`

is not source-secure. The lead preserves the exact complete-graph Hermite theorem and the class-level gadget equivalence, but the full FOREST target remains open.

The assigned partner result actually consumed and applied is the named OTHER-account report fleet01/B02 run `20260922T041812Z-b02-forest-r11`, blob `07794d469ced157633cd07c57caaaf3e3bbe4066`. It independently identifies the same quantifier failure and writes the source-valid gadget parameter as

`q = k/(2^a-1)`.

Its conclusion is that unit pNC on the original graph alone does not pay the weighted evaluation; one needs the entire family of unit gadget expansions. I use that correction below and replace the density-only gadget set by an exact realization of **every positive rational parameter**, then run the separator induction entirely over the rational field. No fixed-graph Cocks implication is used.

## 2. Notation

For a finite graph with positive edge weights `y`, let

`Z_G(y) = sum_{F acyclic} prod_{h in F} y_h`.

For distinct marked edges `e,f`, define the Rayleigh/forest gap

`Delta_G(e,f;y) = Z_e Z_f - Z Z_ef`.

Because `Z` is multiaffine, `Delta_G(e,f;y)` is independent of the marked variables `y_e,y_f`.

For a two-terminal graph `T` with terminals `u,v`, all of whose edges have unit weight unless otherwise stated, let

- `D(T)` be the number of forests in which `u,v` are disconnected;
- `C(T)` be the number of forests in which `u,v` are connected;
- `rho(T)=C(T)/D(T)`.

Both `C,D` are positive for every nontrivial two-terminal network used below.

## 3. New lemma: every positive rational response has an exact finite simple unit realization

### Lemma 3.1 (parallel and series calculus)

Let `T_1,T_2` be edge-disjoint two-terminal unit graphs with disjoint interiors.

For their parallel composition (identify both terminal pairs),

`D_parallel = D_1 D_2`,

`C_parallel = C_1 D_2 + D_1 C_2`,

so

`rho_parallel = rho_1 + rho_2`.

The term `C_1 C_2` is absent because two internally disjoint connecting forest paths form a cycle.

For their series composition (identify one terminal of `T_1` with one terminal of `T_2` and use the two outer terminals), every pair of local forests remains acyclic and the outer terminals connect exactly when both local terminal pairs connect. Thus

`C_series = C_1 C_2`,

`D_series = D_1D_2 + C_1D_2 + D_1C_2`,

and

`rho_series = rho_1 rho_2/(1+rho_1+rho_2)`.

### Lemma 3.2 (universal rational unitization)

For every positive rational `r` there exists a finite **simple** unit two-terminal graph `T_r` with `rho(T_r)=r`.

**Proof.** Start from a single terminal edge, whose response is `1`.

Let `U` be the simple theta graph consisting of three internally vertex-disjoint length-two terminal paths, i.e. `K_{2,3}` with the terminals in the part of size two. One length-two branch has three disconnected local states and one connecting state. Hence

`D(U)=3^3=27`,

`C(U)=3*3^2=27`,

so `rho(U)=1`, and importantly `U` has no direct terminal edge.

Two simple operations are therefore available while preserving simplicity:

`P(r)=r+1`, by putting a fresh copy of `U` in parallel;

`S(r)=r/(r+2)`, by putting a fresh single unit edge in series.

It remains to prove that every positive rational is obtained from `1` by a finite word in `P,S`.

Write the target in lowest terms as `x=a/b>0`. Run the following inverse algorithm:

- if `a>b`, replace `a/b` by `(a-b)/b` (inverse of `P`);
- if `a<b`, replace `a/b` by `2a/(b-a)` and reduce (inverse of `S`);
- if `a=b`, the reduced fraction is `1` and stop.

This terminates. Let `N=a+b` for a reduced fraction. A `P^{-1}` step strictly decreases `N`. For an `S^{-1}` step, `gcd(2a,b-a)` is either `1` or `2`. If it is `2`, reduction halves `N`. If it is `1`, `N` stays fixed and the new numerator is `2a`. Consecutive same-height `S^{-1}` steps therefore double the numerator. Such steps cannot continue indefinitely: after finitely many doublings the transformed fraction is at least `1`, after which either the algorithm stops or a `P^{-1}` step strictly decreases `N`. Thus `N` decreases after finitely many steps, and eventually reaches `2`, i.e. `1/1`.

Reverse the finite inverse word and apply the corresponding `P,S` graph operations to the one-edge base graph. The fresh interiors and the absence of a terminal edge in `U` prevent parallel duplicate edges, so every `T_r` is simple. QED.

This strengthens the partner's dense special set `k/(2^a-1)`: **every positive rational is realized exactly**, with no limiting argument.

## 4. Exact substitution identity

### Lemma 4.1 (two-terminal substitution)

Let `G` be a simple base graph with marked edges `e,f`. Replace any collection of unmarked base edges `h` by internally disjoint unit two-terminal networks `T_h`, with response `r_h=C_h/D_h`, and keep `e,f` literal. Let `H` be the resulting simple graph. Then

`Z_H = (prod_h D_h) Z_G(r)`,

and similarly for `Z_e,Z_f,Z_ef`; hence

`Delta_H(e,f;1) = (prod_h D_h)^2 Delta_G(e,f;r)`.                 (4.1)

**Proof.** A forest state inside each gadget either disconnects or connects its two terminals. Project a global state to the set of base edges whose gadgets connect. Because each local state is a forest and a connecting local state has a unique terminal path, the substituted union is acyclic exactly when the projected base-edge set is acyclic. Each disconnected gadget contributes `D_h`; each connected gadget contributes `C_h=D_h r_h`. Summing over projected base forests gives the first identity. Differentiating only the literal marked edges gives the remaining identities. QED.

### Corollary 4.2

If the unit FOREST conjecture holds for every finite simple graph, then the Rayleigh gap is nonnegative on **every finite simple graph with every positive rational edge-weight vector**. This is exact: apply Lemma 3.2 simultaneously to the unmarked weights and (4.1). No fixed-graph upgrade and no real-weight continuity are needed.

The converse is trivial by setting all weights to one.

## 5. Source-secure all-parameter two-cut formulas

Let a two-connected simple graph `G` have a genuine two-vertex cut `{u,v}`. Separate the `uv` edge, if present, as its own singleton bridge. Let `B_1,...,B_m` be the resulting edge-disjoint `uv`-bridges. For each bridge, with its inherited positive rational weights, write

`D_i = forest sum with u,v disconnected`,

`C_i = forest sum with u,v connected`.

A global forest can have at most one connecting bridge, so exactly

`Z_G = prod_i D_i + sum_i C_i prod_{j != i} D_j`.                 (5.1)

### Same-bridge marked pair

If `e,f in B_i`, put

`A_i = prod_{j != i} D_j`,

`lambda_i = sum_{j != i} C_j/D_j`.

Then adding one virtual `uv` edge `g_i` to `B_i` gives

`Delta_G(e,f) = A_i^2 Delta_{B_i+g_i}(e,f; y_{g_i}=lambda_i)`.    (5.2)

Because all input weights are rational, every `D_j,C_j` and therefore `lambda_i` is positive rational.

An original singleton `uv` edge causes no exception: its bridge has `D=1`, `C=y_uv`, so at unit weight it simply contributes `1` to `lambda_i`. We never add a virtual edge to a bridge already containing the original `uv` edge, because that original edge was split off as a singleton bridge.

### Different-bridge marked pair

If `e in B_i`, `f in B_j`, `i != j`, write

`A_ij = prod_{k != i,j} D_k`,

`R_i(e)=D_i partial_e C_i - C_i partial_e D_i`.

Direct differentiation of (5.1) gives complete cancellation of every other bridge parameter:

`Delta_G(e,f) = A_ij^2 R_i(e) R_j(f)`.                           (5.3)

For a non-singleton bridge,

`R_i(e)=Delta_{B_i+g_i}(e,g_i)`,

where the virtual edge can have any positive weight because the gap is independent of its own marked weight. For a singleton original `uv` bridge marked by its only edge, `R_i=1` exactly.

Thus all original-separator-edge and cross-bridge cases are explicit; there is no hidden parallel-edge intermediate.

## 6. Exact theorem: unit FOREST is equivalent to rational-weight FOREST on 3-connected simple graphs

Define:

**(U)** Every finite simple graph is pairwise forest negatively correlated at unit weights.

**(Q)** Every finite simple graph is Rayleigh for every positive **rational** edge-weight vector.

**(Q3)** Every 3-vertex-connected finite simple graph is Rayleigh for every positive rational edge-weight vector, with `K_3` included as the small 2-connected base case.

### Theorem 6.1

`(U) <=> (Q) <=> (Q3)`.

**Proof.** `(Q)=>(U)` is specialization. `(U)=>(Q)` is Corollary 4.2.

It remains to prove `(Q3)=>(Q)`. Induct on the number of edges.

- Disconnected components factor. If the marked edges lie in different components the gap is zero; if they lie in one component, every other component contributes a positive square factor.
- A cut vertex gives the same one-sum factorization, so reduce to a two-connected block.
- `K_3` is direct: if the third edge has weight `z>0`, the gap of the other two edges is `z+z^2>0` after factoring irrelevant positive weights.
- A two-connected graph on at least four vertices with no two-vertex cut is 3-vertex-connected and is covered by `(Q3)`.
- Otherwise take a genuine two-cut and the bridge decomposition above. A genuine two-cut of a two-connected simple graph has at least two non-singleton component bridges; each such bridge contains at least two edges, since its component attaches to both `u` and `v`. Hence every augmented non-singleton bridge `B_i+g_i` has strictly fewer edges than `G`.

For a same-bridge pair, `lambda_i` in (5.2) is positive rational, so the induction hypothesis applies to the smaller simple graph `B_i+g_i` and makes (5.2) nonnegative.

For a cross-bridge pair, each non-singleton factor `R_i(e)` in (5.3) is the marked-pair gap of the smaller simple graph `B_i+g_i`, hence is nonnegative by induction; a singleton factor is exactly `1`. Thus (5.3) is nonnegative.

This exhausts the separator cases and proves `(Q3)=>(Q)`. QED.

This is the requested all-parameter/three-connected reduction, now repaired after the fixed-Cocks correction. The parameter class can be kept **rational throughout**; irrational weights are unnecessary for the original unit target. If desired, ordinary continuity then extends `(Q)` to all positive real weights, but no such extension is needed in the proof above.

## 7. What this does — and does not — say about a unit-minimal counterexample

The previous fleet04/B01 candidate `FOREST-UNIT-MINIMAL-3CONN-v2` claimed more: that an edge-minimal **unit** counterexample itself must be 3-connected. The lead has correctly withdrawn that conclusion because its same-bridge step used the disputed fixed-graph weighted upgrade.

The source-secure part that remains is sharper than just saying "the proof breaks."

Take an edge-minimal unit counterexample and a genuine two-cut.

1. A violating marked pair cannot lie in two different bridges. For every non-singleton bridge the response `R_i(e)` in (5.3) is the unit gap `Delta_{B_i+g_i}(e,g_i)` of a strictly smaller simple graph, so minimality makes it nonnegative; singleton response is `1`. Hence (5.3) cannot be negative.
2. Therefore the violating pair lies in one bridge `B_i`.
3. The outside effective parameter `lambda_i` is a positive rational. By Lemma 3.2 choose an exact simple unit network `T_lambda` with response `lambda_i`. Lemma 4.1 and (5.2) give

   `Delta_{B_i union T_lambda}(e,f;1)/D(T_lambda)^2`

   `= Delta_{B_i+g_i}(e,f;lambda_i)`

   `= Delta_G(e,f;1)/A_i^2 < 0`.                                  (7.1)

So every same-bridge separator violation has an **exact unit simple replacement** whose entire outside is a controlled two-terminal unit gadget. This is an exact normal form, not a continuity statement.

However, this does **not** restore edge-minimal 3-connectivity, because the exact replacement need not be smaller.

### Sharp size obstruction

Suppose a unit two-terminal network `T` with `m` edges has reduced response `rho(T)=a/b`. Since `C=ka` and `D=kb` for some positive integer `k`,

`a+b <= C+D <= 2^m`,

hence

`m >= ceil(log_2(a+b))`.                                           (7.2)

A length-`ell` unit path has

`C=1`, `D=2^ell-1`, `rho=1/(2^ell-1)`,

and (7.2) gives `m>=ell` for **every** exact unit realization of that response. The path itself uses `ell` edges, so it is globally edge-minimal as a response realizer.

Therefore an outside path ear cannot be compressed at all by exact unitization. Already the two-edge path gives the unavoidable virtual value `1/3`, and no one-edge unit network realizes `1/3`.

This is a genuine obstruction to the tempting repair "unitize the virtual fugacity and contradict edge-minimality." It is an auxiliary-counterexample to that compression argument, not a counterexample to FOREST.

## 8. Compact conditional end-to-end chain and the first remaining obligation

The corrected source-secure chain is now

`unit FOREST on all simple graphs`

`<=> exact positive-rational weighted FOREST on all simple graphs`

`<=> exact positive-rational weighted FOREST on 3-connected simple graphs (+ K3 base)`.

The lead's complete-graph Hermite theorem supplies only the symmetric unit point on a very special 3-connected family. Fleet01/B02's source audit correctly says that upgrading those unit points to the necessary gadget/rational-weight family is not paid by the fixed-graph Cocks statement.

Thus the first target-level obligation is honestly:

**prove the rational-weight Rayleigh inequality on every 3-connected simple graph, or construct a source-valid counterexample.**

By Theorem 6.1 this obligation is equivalent to the parent target, so I do **not** present it as an easier unsupported lemma. The useful reduction is structural: all separator algebra, induced parameters, singleton separator edges, cross-bridge pairs, and rational-unitization issues are now paid exactly; the unsolved content is confined to genuinely 3-connected weighted cores.

For any attempted stronger statement that an edge-minimal unit counterexample itself is 3-connected, Section 7 identifies a strictly earlier unavoidable subcase: one must control the gap under the path-ear attenuations

`y_g = 1/(2^ell-1)`.

No edge-count compression can remove those values.

## 9. Exact regression used in this run

A standard-library exact `Fraction` checker accompanies this report as `rational_unitization_check.py`. It is regression only; the theorem is proved algebraically above. It verifies reconstruction from the inverse `P,S` algorithm for all 4096 pairs `1<=a,b<=64`, confirms `D(U)=C(U)=27`, and checks the path-realizer counting lower bound for `ell=1,...,8`.

Executed output:

`STATUS=PASS; rational_pairs=4096; max_inverse_steps=126; worst=63/64; theta_D_C=27/27; path_minimality_ell=1..8`

No numerical search is used to infer the universal statements.

## 10. Status

**ESSENTIAL_STEP_APPLIED.** The exact separator/three-connected reduction is source-secure without the rejected fixed-graph Cocks quantifier, and every rational virtual fugacity has an exact simple unit realization. The parent FOREST conjecture remains open. The prior unit-minimal-3-connected claim remains withdrawn; Section 7 explains precisely why rational unitization alone cannot repair it.

No installation or benchmark work, benchmark answers, email, Drive access, public posting, paid/remote compute, workflow dispatch, permission change, scheduler mutation, production-state mutation, credentials, machine paths, or unrelated private material was used.
