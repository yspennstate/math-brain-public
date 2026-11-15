The report's experiment table uses `final/` only. Files directly in this
directory are retained pilot results, except `gap_certificate.json`, which
is the exact rational certificate for the degree-1000 separation.

`final/samples.jsonl` contains all final sampled graphs, seeds, local output
sizes and witnesses, heuristic witnesses, exact small-graph optima, and MILP
cross-checks. `final/training.json` records the separate parameter selection.
`final/summary.json` aggregates graph means; standard errors use graphs as
independent sampling units. `final/audit.json` records independent checks.

All densities are fractions of vertices, not fractions of edges. Larger-graph
heuristic outputs are lower bounds on maxima; they are not certificates of
optimality. Simulated local densities do not bound the FIID supremum from
above and do not resolve the cubic conjecture.
