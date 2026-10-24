# R06 / I0056 — second idea before archival checker: vertex-boundary minimization is a maximum-closure problem

Source: Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20 / intake I0056.

The first frontier experiment suggests that non-round sets beat all metric balls. There is a stronger exact finite formulation.

For a finite search region, introduce two 0/1 states for each graph vertex: `selected(v)` and `covered(v)`, where covered means selected or in the outer vertex boundary. The logical constraints are

- selected(v) => covered(v),
- selected(v) => covered(u) for every neighbour u of v.

Then

|partial_V K| - r |K| = sum_v covered(v) - (1+r) sum_v selected(v).

For fixed rational/integer-scaled r this is a maximum-weight closure problem: selected nodes have positive weight (1+r), covered nodes have weight -1, and the implications above are infinite-capacity arcs. Thus an ordinary integer max-flow/min-cut can search exactly for a finite witness without replacing the source normalization.

Use selected candidates in the exact radius-17 ball of T=r{4,5}, and coverage vertices through radius 18, so every neighbour of every candidate is present. Start from the already certified one-frontier ratio and use the integer threshold 1795/1000 for (1+r). Whatever cut is returned, discard any optimality claim unless needed; independently reconstruct its exact selected set and exact covered set in the Coxeter graph and certify |K| and |partial_V K| by integer counts. The resulting finite set alone is a rigorous upper-bound witness.

This is still methods #5/#8/#26 in substance: parameterize the boundary functional, discretize it as an exact finite closure problem, and hunt the finite non-round dip that the round-ball asymptotics cannot see.
