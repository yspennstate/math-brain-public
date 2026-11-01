Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding selector is exposed.

# G0008 admission literature addendum — layered-graph route recovered

This addendum supplements, and does not overwrite, `research7_2026-09-17/R7-06/admissions/2026-09-18T025300Z__G0008_axis_connectivity_monotonicity.md`.

A broader bounded follow-up search on 2026-09-18 recovered a directly relevant prior paper that must be part of the admission landscape:

- Philipp König and Thomas Richthammer, **Monotonicity properties for Bernoulli percolation on layered graphs -- a Markov chain approach**, arXiv:2207.13173; final version in *Stochastic Processes and their Applications* **181** (2025), article 104549, DOI `10.1016/j.spa.2024.104549`.

For a finite base graph `G`, their layered graph `G x Z` admits an eventual-in-layer monotonicity theorem: for some finite `N`, connection probabilities from one layer to successive remote layers are monotone for every `n >= N` and uniformly in `p in [0,1]`. They explicitly list `Z x Z = Z^2` as the motivating infinite-base example, but their proved theorem in the recovered abstract is for **finite** `G`.

This does **not** resolve G0008: passing from finite-width cylinders to the infinite cross-section does not preserve the theorem in a way that fixes a given small separation, because the eventual threshold `N(G)` depends on the finite base and can diverge under width exhaustion. In the supercritical planar regime the cylinder/plane limit is additionally nonuniform for long connections. Thus the result is an important analogous method, not source closure.

The current Campos--de Lima arXiv record remains `2601.00291v1` (submitted 2026-01-01) and still states the square-lattice problem as open. The bounded search found no later exact all-`p`, all-`n` square-lattice resolution. Negative search evidence is not a novelty certificate.

Admission verdict remains **HARD OUTSIDE / current-open according to the primary source plus bounded follow-up check**, with full novelty UNVERIFIED.
