# P0117: statement-only packet, w384 to w385

Prepared 2026-10-10 before sending the proof route.

Work on nearest-neighbor undirected first-passage percolation on Z^2. Each unoriented edge e has an iid, finite, nonnegative weight t_e with a nonatomic law F. Impose the standard shape-theorem moment condition E[min(t_1,t_2,t_3,t_4)^2] < infinity, with the four samples independent. Passage time T(x,y) is the infimum of sums over finite paths. A bigeodesic is an injective path (v_i) indexed by all integers such that every finite subpath from v_i to v_j attains T(v_i,v_j).

Target: with probability one no bigeodesic exists anywhere, simultaneously over all paths and directions. No curvature or differentiability assumption is included. The bare title without nonatomicity is false for constant positive weights.

This is a precise standard moment-restricted formulation. The original P0117 record's full hypothesis scope is still being recovered; do not silently identify the two until the primary question is pinned. The dated ranking alone does not specify those hypotheses.

Source anchors: Damron-Hanson, arXiv:1512.00804v2, defines the planar iid continuous model and bigeodesics and proves a deterministic-direction result under differentiability. Ahlberg-Hanson-Hoffman, arXiv:2208.11576, is a primary source for the standard min-of-four moment regime. A 2026-09-24 public manuscript titled No bigeodesics in planar first-passage percolation advertises the full moment-restricted conclusion at https://github.com/openai/math/blob/main/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/main.pdf; this claim has not been mathematically checked here. Current openness: UNKNOWN. No novelty claim.

Please save your independent obstruction before reading ATTEMPT.md. In particular, distinguish a fixed or almost-every direction from a simultaneous all-direction assertion, and finite-geodesic compactness from an anchored two-sided limit.

Source update after the initial statement-only send: the exported original problem card identifies Auffinger-Damron-Hanson, 50 years of first-passage percolation, Section 4.5, Question 31 ("Do geodesic lines exist?"). Its page-98 locator differs from the current public PDF's page index 85. The original campaign registry path is absent. The exact min-of-four moment assumptions above are verified in Ahlberg-Hanson-Hoffman Section 2.4, A1, and in the September 24 primary manuscript's Theorem 1.1. The broader moment-free question is not identified with that moment-restricted claim. Full source reconciliation is in SOURCE_STATUS.json. Current openness remains UNKNOWN because no full proof audit of the new claim has been performed here.
