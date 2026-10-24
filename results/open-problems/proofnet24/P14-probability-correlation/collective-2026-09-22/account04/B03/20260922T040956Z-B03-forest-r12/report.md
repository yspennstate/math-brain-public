# FOREST / account04 B03 — source-secure all-graphs integration and simple-gadget globalization

**Run:** `20260922T040956Z-B03-forest-r12`  
**Outcome:** **ESSENTIAL_STEP_APPLIED** (to the source-secure globalization route; not a new public theorem claim).  
**Parent team state:** the lead's `FOREST-KN-COCKS-RECONCILED-v3` remains an internal `FULL_PROOF_CANDIDATE`; this run neither auto-promotes nor refutes it.  
**Brain context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and source state

The target is the uniform law on **all** acyclic edge subsets of every finite simple graph `G`, including the empty forest, disconnected forests and every size. For distinct edges `e,f`, writing

`Z_G(y)=sum_{F forest} product_{a in F} y_a`,

and `Z_e,Z_f,Z_ef` for the corresponding weighted sums over forests containing the marked edges, the target is

`Delta_G(e,f;1)=Z_e Z_f-Z_G Z_ef >= 0`.

The newest account01/B01 directory (`20260922T040935Z-b01-forest-r11`) contained only its start record at the time of this run, so the latest **complete** lead version consumed was account01/B01 `20260922T030948Z-b01-forest-auto11`, report blob `58b8b1d8ac522a4eda7479400820e590c12f22aa`, version `FOREST-KN-COCKS-RECONCILED-v3`.

Its compact end-to-end chain is:

1. prove the unit forest inequality for every complete graph `K_n` by the exact labelled-forest/Hermite argument;
2. use the published Cocks fixed-graph implication `unit Conjecture 1.1 on G => M(G) independence correlated`;
3. use Semple--Welsh Proposition 3.5, which makes independence correlation minor-closed;
4. obtain every finite simple `G` by deleting edges from `K_n`, then specialize the surviving positive weights to one.

I independently rechecked the exact source semantics of steps 2--3. In Semple--Welsh, *Negative Correlation in Graphs and Matroids*, Combin. Probab. Comput. 17 (2008), pp. 423--435, `independence correlated` is explicitly defined as `Delta_I(M;y)>=0` for **every positive real weighting** (printed pp. 3--4), Proposition 3.5 proves minor closure (printed pp. 6--7), and the final Note on printed p. 13 states that Cocks proved: if Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated. Thus the final published Semple--Welsh statement is genuinely fixed-graph, not merely the older class-level parallel-copy equivalence.

Source checked directly: `https://www.math.canterbury.ac.nz/~c.semple/papers/SW07.pdf` (definition, Proposition 3.5, final Note). Cocks, *Correlated Matroids*, CPC 17 (2008), 511--518, DOI `10.1017/S0963548308009152`, was source-checked at the publisher abstract level in this run; its full article body was not directly available through the accessible source. This is a source-diligence limitation, not a mathematical counterexample to the fixed-graph theorem explicitly recorded by Semple--Welsh.

## 2. Named OTHER-account result consumed and applied

I consumed account03/B01 run `20260922T032940Z-account03-B01-FOREST-r11`, report blob `6df1229503af74c508d9d3e0339373355ccdf074`. It derives an exact activity-basis representation of the actual uniform unrooted forest law and the marked-pair identity

`4 Delta = W10 W01 - W00 W11 + Q(W10+W11)`.

On the disjoint-edge `K_5` witness it obtains `(W00,W10,W01,W11,Q)=(49,70,56,116,14)` and `Delta=210`, showing that neither the exchange reservoir `Q` nor the ordinary cross channel can simply be discarded. I use this as a structural guard on the integration: the argument below does **not** replace the all-graphs step by a q-only/local-cell positivity assertion; it transports the complete forest polynomial exactly.

I also consumed account01/B20 run `20260922T032104Z-b20-forest-r12`, report blob `747589684cd60aa1d26a314884fc50c40354e720`, which independently source-checked the same final Semple--Welsh Note and Proposition 3.5. That is compatible with, but does not substitute for, the direct derivation below.

## 3. New exact lemma: simple path-bundle gadgets realize arbitrary positive edge weights densely

The older parallel-copy globalization argument is awkward for a target stated only for simple graphs, because literal parallel copies leave the simple category. The following elementary construction removes that issue completely.

### Lemma (simple-gadget globalization)

Assume the unit forest pairwise inequality holds for **every finite simple graph**. Then for every finite simple graph `G`, every positive real edge weighting `y`, and every distinct pair `e,f`,

`Delta_G(e,f;y) >= 0`.

Equivalently, for simple graphs the global unit conjecture is equivalent to global positive-weight independence correlation.

### Proof

Fix a finite simple graph `G` and marked edges `e,f`. Since the forest polynomial is multiaffine, the Rayleigh difference for the marked pair is independent of the two marked variables `y_e,y_f`, so leave `e,f` as literal unit edges.

For every other edge `g=uv`, choose integers `a_g>=2` and `k_g>=1`. Replace `g` by `k_g` internally vertex-disjoint `u-v` paths, each of length `a_g`, using fresh internal vertices for this gadget and for every path. Call the expanded graph `H`. Because `G` is simple, `a_g>=2`, and all internal vertices are fresh, `H` is again a finite simple graph.

Put

`d_g = 2^{a_g}-1`,  `q_g = k_g/d_g`.

Consider one gadget. A length-`a` path has exactly `2^a-1=d` proper edge subsets. A gadget state which does **not** connect `u` to `v` must leave every one of its `k` paths non-intact, hence has exactly

`C0 = d^k`

realizations. A gadget state which **does** connect `u` to `v` and remains acyclic has exactly one intact path: choose that path in `k` ways and leave every other path non-intact, giving

`C1 = k d^{k-1}`.

Two intact paths would form a cycle, and because the paths are internally disjoint there is no other way for a proper subset of several paths to connect `u` to `v`. Therefore

`C1/C0 = k/d = q`.

Now project an expanded forest of `H` to an edge subset of `G` by declaring an unmarked edge `g` present exactly when its gadget connects its endpoints, and keeping the marked literal edges as themselves. This projection sends forests to forests: if the projected set contained a cycle, the unique endpoint-connecting path selected in every on-gadget along that cycle would lift it to a cycle in `H`. Conversely, a base forest together with independently selected local gadget states cannot create a cycle, because any expanded cycle would project to a base cycle (a local cycle would require two intact paths and has already been excluded).

Hence, with

`C = product_{g != e,f} C0_g`,

the full four marked-state generating functions satisfy exactly

`Z_H = C Z_G(q)`,  `Z_{H,e}=C Z_{G,e}(q)`,
`Z_{H,f}=C Z_{G,f}(q)`,  `Z_{H,ef}=C Z_{G,ef}(q)`,

where the unmarked edge weight of `g` on the right is `q_g`. Consequently

`Delta_H(e,f;1) = C^2 Delta_G(e,f;q)`.

By the global unit hypothesis the left-hand side is nonnegative, so the weighted inequality holds whenever every unmarked weight has the form

`q_g = k_g/(2^{a_g}-1)`.

These values are dense in `(0,infinity)`: for fixed `x>0`, let `a->infinity` and choose the nearest positive integer `k` to `x(2^a-1)` (for sufficiently large `a` this is at least one). Then

`|x-k/(2^a-1)| <= 1/(2(2^a-1)) -> 0`.

Take this approximation independently in each coordinate. Since `Delta_G(e,f;y)` is a polynomial, hence continuous, nonnegativity on that dense positive set extends to every positive real weighting. QED.

### What this does and does not pay

This is a source-secure proof of the **global** simple-graph equivalence, using no multigraph and no weighted theorem as an input. It directly repairs the category issue in the older parallel-copy proof.

It does **not** by itself prove the stronger fixed-graph implication

`G unit-good => M(G) positive-weight-good`.

That stronger implication is exactly what the final Semple--Welsh Note attributes to Cocks and exactly what the lead needs to go from the complete-graph theorem to minor closure. Thus the two statements must not be conflated. If one accepts the published fixed-graph Cocks theorem, the lead's all-graphs chain is logically closed. If one insists on replacing Cocks by a self-contained derivation, the fixed-graph upgrade (not the global class equivalence) is the exact remaining theorem to reproduce.

## 4. Exact audit of the gadget identity

The accompanying standard-library exact checker tests a nontrivial weighted `K_4` instance with disjoint marked edges. Two unmarked edges have weights `2/3` and `3/7`, realized respectively by `(k,a)=(2,2)` and `(3,3)`. The base weighted counts are

`(Z,Ze,Zf,Zef,Delta)=(548/21, 74/7, 218/21, 86/21, 1268/441)`.

The expanded simple graph has 12 vertices and 17 edges. Its unit counts are

`(80556,32634,32046,12642,27400212)`.

The scale is

`C=(2^2-1)^2 (2^3-1)^3=3087`,

and the checker verifies all four identities `expanded=C*base` and

`Delta_expanded=C^2 Delta_base=27400212`

exactly. The computation is an audit only; Section 3 is the proof.

Checker SHA-256: `09d860b22855e17c1b98d40f63d5065ce11e74664c2a8dedc1d412e2a7c6940e`.  
Output SHA-256: `ebc467eede9b44b0941b9b1aa2ddaa9d093919936bc03e480c94a55f6d43ec74`.

Exact output:

```text
SIMPLE_GADGET_GLOBALIZATION_AUDIT
base = (Fraction(548, 21), Fraction(74, 7), Fraction(218, 21), Fraction(86, 21), Fraction(1268, 441))
expanded = (Fraction(80556, 1), Fraction(32634, 1), Fraction(32046, 1), Fraction(12642, 1), Fraction(27400212, 1))
C = 3087
C_times_base_first_four = (Fraction(80556, 1), Fraction(32634, 1), Fraction(32046, 1), Fraction(12642, 1))
C2_times_base_delta = 27400212
identity_first_four = True
identity_delta = True
expanded_vertices = 12
expanded_edges = 17
simple_expansion = True
```

## 5. End-to-end integration status

The strongest compact chain currently available is still the lead's:

`complete-graph unit theorem`
` -> [Cocks fixed-graph theorem as explicitly recorded by final Semple--Welsh]`
` weighted independence correlation of every K_n`
` -> [Semple--Welsh Prop. 3.5]`
` weighted independence correlation of every deletion minor G of K_n`
` -> [set surviving weights to 1]`
` target uniform-forest inequality for every finite simple G`.

This run adds an independent exact theorem underneath that chain:

`all simple graphs unit-good <=> all simple graphs positive-weight-good`,

proved entirely with simple path-bundle gadgets. It also identifies why this class-level theorem cannot replace the fixed-graph Cocks implication in the complete-graph-only deduction without becoming circular.

**Honest status: `ESSENTIAL_STEP_APPLIED`, not a new `FULL_PROOF_CANDIDATE`.** The lead candidate already has two independent existing-worker end-to-end reviews on record; this run does not create a third truth-promotion mechanism. Before any external solved-problem claim, the original Cocks proof body should still receive direct publication-grade verification (or an independent self-contained proof of its fixed-graph implication), and the complete-graph Hermite argument should receive ordinary expert review. No novelty claim is inferred from source search.

No installation/benchmark work, production-population mutation, email, Drive write, public posting, paid/remote model call, workflow dispatch, permission bypass, or unrelated-private-data access occurred.
