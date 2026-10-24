Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# R20 idea-before-code — BMO Conjecture 2.6, dual/polynomial attack and order-nine decision

## Continuity

R20 remains on its current exclusive Bensmail–Marcille–Orenga Conjecture 2.6 claim `operations/claims/BMO-2025-PUSHING-DELTA.md`. The stale scheduler-title I0100/Paley target is not reopened. The supported fixed metric entering this run is `n_all=8`; there have been five consecutive BMO runs after admission with no movement of this fixed all-graphs metric, so if this run also leaves `n_all` unchanged the controlling six-unchanged-run rule requires a handoff/rotation after this run.

Fresh source work will again check the 2025 DMTCS source and the 2026 Rautenbach--Schwartze--Werner follow-up before any status claim.

## The three new Section-B moves

- **#11 DUALIZE.** Regard failure as a cover of the integer box `{0,...,Delta}^V` by the bad-edge affine hyperplanes `sigma(u)=sigma(v)`.
- **#18 SAY IT IN ANOTHER LANGUAGE.** Use the graph polynomial
  `F_G(rho)=prod_{uv in E}(sigma(u)-sigma(v))`, where `sigma=d+(D+A)rho`, and study its reduction on the interpolation grid.
- **#25 COUNT THE SAME THING TWICE.** A coefficient of `F_G` is a signed weighted count of choices assigning each edge factor to one variable in its support. Compare this assignment count with an orientation/load count on the original graph.

## Research route before any computation

For an edge `uv`, the bad linear form is

`L_uv = d(u)-d(v) + (d(u)-1)rho(u) - (d(v)-1)rho(v) + sum_{x in N(u)\(N(v) union {v})}rho(x) - sum_{y in N(v)\(N(u) union {u})}rho(y)`.

Thus every non-`K2` edge factor has a nonzero endpoint coefficient at at least one endpoint. The conjecture would follow from a Combinatorial-Nullstellensatz certificate consisting of one nonzero coefficient of `F_G` at a monomial `prod_v rho(v)^{t_v}` with every `t_v<=Delta`.

There is an easy load-feasible *term selection*: orient each original edge to one of its endpoints, choosing a nonzero endpoint coefficient, so every vertex is selected at most `d(v)<=Delta` times. Hence the desired exponent box contains at least one term-by-term contribution. This is not yet a proof because distinct term selections can land on the same exponent vector and cancel. The exact new obstruction is therefore **noncancellation**, not exponent feasibility. A universal proof along this route needs either (i) a sign-reversing involution leaving one unmatched endpoint-orientation term, (ii) a term order for which a bounded-exponent endpoint monomial is genuinely leading, or (iii) a finite-field/parity argument showing an admissible coefficient is nonzero.

The term-order shortcut does not hold automatically: a variable belonging to the symmetric-neighborhood part of `L_uv` can outrank both endpoints, and forcing an endpoint to be leading simultaneously for every factor creates cyclic inequalities. So this run will not falsely claim that Hall/load feasibility already proves the conjecture.

## Decisive finite move if the noncancellation theorem does not close

The fixed metric can still move honestly by deciding the complete order-nine census. The existing exact order-eight work produced all 11,117 connected eight-vertex isomorphism classes. Every connected nine-vertex graph has a non-cut vertex, so deleting such a vertex leaves a connected eight-vertex graph; conversely every order-nine graph is recovered by adding one new vertex with a nonempty neighborhood to an order-eight representative. Therefore augmenting every order-eight representative by every nonempty subset of its eight vertices and deduplicating **only by exact isomorphism** is a complete order-nine census.

For each resulting graph, solve the affine-hyperplane avoidance CSP exactly over `{0,...,Delta}`; a stored witness is checked with integer arithmetic against every edge. Heuristic invariants may pre-bucket isomorphism tests but may never delete a graph without an exact isomorphism decision. The standard connected unlabeled order-nine count `261080` will be used only as an independent sanity check, not as the coverage proof.

If every class passes, `n_all` moves `8 -> 9`. If an exact failure is found, it is a source-level counterexample candidate and must then receive an independent exhaustive no-witness certificate before any REFUTED label. If the complete census cannot finish in this run, the metric remains 8 and the six-unchanged-run rotation rule is honored.
