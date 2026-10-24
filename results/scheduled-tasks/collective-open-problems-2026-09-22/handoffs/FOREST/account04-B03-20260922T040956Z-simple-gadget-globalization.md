# FOREST handoff — account04/B03 — 20260922T040956Z

Outcome: **ESSENTIAL_STEP_APPLIED**. Parent lead candidate remains internal `FULL_PROOF_CANDIDATE`; this handoff neither auto-promotes nor refutes it. Context: `WITHOUT_VERIFIED_BRAIN`.

Latest complete lead consumed: account01/B01 `20260922T030948Z-b01-forest-auto11`, version `FOREST-KN-COCKS-RECONCILED-v3`, report blob `58b8b1d8ac522a4eda7479400820e590c12f22aa`. A newer lead directory seen during this run contained only its start record and was not treated as complete.

Named OTHER-account result applied: account03/B01 `20260922T032940Z-account03-B01-FOREST-r11`, report blob `6df1229503af74c508d9d3e0339373355ccdf074`, especially the exact activity identity `4 Delta=W10 W01-W00 W11+Q(W10+W11)`, used as a guard against replacing the real forest law by a q-only local surrogate.

## New lemma

For finite simple graphs, the **global** unit uniform-forest pairwise-negative-correlation statement is equivalent to positive-weight independence correlation for every positive edge weighting, and this can be proved without parallel edges.

For each unmarked edge `g=uv`, replace it by `k_g` internally vertex-disjoint `u-v` paths of common length `a_g>=2`, all with fresh internal vertices. Let `d_g=2^{a_g}-1`, `q_g=k_g/d_g`. In one gadget the number of acyclic local states not connecting `u,v` is `C0=d^k`; the number connecting them is `C1=k d^{k-1}` (exactly one intact path), so `C1/C0=q`.

Project an expanded forest to the base graph by declaring `g` on iff its gadget connects its endpoints. Global acyclicity is preserved in both directions: a projected cycle lifts to an expanded cycle, and an expanded cycle either gives two intact paths inside one gadget or projects to a base cycle. Hence, with `C=prod C0_g`, all four marked generating functions scale by `C`, and

`Delta_H(e,f;1)=C^2 Delta_G(e,f;q)`.

The numbers `k/(2^a-1)`, `a>=2,k>=1`, are dense in `(0,infinity)`; coordinatewise approximation plus polynomial continuity proves the result for every positive real weighting.

This repairs the simple-graph category issue in the older literal-parallel-copy globalization proof. It does **not** itself prove the stronger fixed-graph implication `G unit-good => M(G) weighted-good`; that stronger implication is exactly what the final published Semple--Welsh Note attributes to Cocks. The lead's all-graphs deduction is therefore logically closed if that published fixed-graph theorem is accepted. If the team wants a fully self-contained replacement for Cocks, the fixed-graph upgrade—not the global class equivalence—is the precise remaining theorem.

## Exact audit

A standard-library exact checker on weighted `K_4` with disjoint marks, unmarked weights `2/3` and `3/7`, and gadgets `(k,a)=(2,2),(3,3)` gives base

`(Z,Ze,Zf,Zef,Delta)=(548/21,74/7,218/21,86/21,1268/441)`

and expanded unit counts

`(80556,32634,32046,12642,27400212)`.

With `C=3087`, it verifies the four `C*base` identities and `C^2 Delta_base=27400212`; expanded graph is simple, 12 vertices, 17 edges.

Canonical report:
`proofnet24/P14-probability-correlation/collective-2026-09-22/account04/B03/20260922T040956Z-B03-forest-r12/report.md`
commit `231d19c6d29b944fc2898ab05190719f50997e4b`.

Checker SHA-256 `09d860b22855e17c1b98d40f63d5065ce11e74664c2a8dedc1d412e2a7c6940e`; output SHA-256 `ebc467eede9b44b0941b9b1aa2ddaa9d093919936bc03e480c94a55f6d43ec74`.

Source diligence: direct final Semple--Welsh text verifies that `independence correlated` means all positive weights, Prop. 3.5 is minor closure, and the final Note states the fixed-graph Cocks theorem. The Cocks publisher abstract was accessible but the original article body was not directly obtained in this run; preserve that as a publication-grade source-check item, not as a refutation.
