# R20 idea-before-code — BMO Conjecture 2.6

Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

Before writing repository checker code, the new target was translated from pushing language into a signless-Laplacian grid-avoidance problem.

For `rho in {0,...,Delta}^V`, let `Q=D+A`. The induced vertex sum is

` sigma = d + Q rho. `

Thus Conjecture 2.6 asks whether, for every nice simple graph, the integer grid `[0,Delta]^V` contains a point outside every edge hyperplane

` H_uv = {rho : (e_u-e_v)^T (d+Q rho)=0},    uv in E(G). `

This formulation makes three routes explicit before computation:

1. **B1 / change category.** Search for a hyperplane-avoidance, polynomial, orientation, or signless-Laplacian mechanism rather than continuing the source's greedy pushing construction.
2. **B2 / attack the negation first.** A single graph whose entire grid is covered by the edge hyperplanes refutes the conjecture. The first finite test should therefore be a complete unlabeled census, not random numerical examples.
3. **B21 / ask who else has this shape.** Compare the row-difference hyperplanes with vertex-weighting/1-2-3 methods. The 2026 Rautenbach–Schwartze–Werner result proves the conjecture for cubic graphs and regular bipartite graphs, so a counterexample search should not waste effort treating those classes as unknown.

## Finite exact test selected

Use NetworkX's standard `graph_atlas_g()` catalogue of all unlabeled simple graphs through order 7. It is enough to test connected nice graphs: pushing constraints are componentwise, and combining component witnesses preserves the bound because each component maximum degree is at most the global maximum degree.

For each connected graph `G` with `1 <= |V(G)| <= 7`, excluding the connected two-vertex graph `K2`, solve exactly for a witness

`rho:V(G)->{0,...,Delta(G)}`

by depth-first search over integer assignments. Every completed candidate is verified directly from the defining integer formula for `sigma`; there is no floating point, SDP, heuristic acceptance, or numerical tolerance.

A successful census moves only the finite metric `n_all`; it remains PARTIAL for the universal conjecture.
