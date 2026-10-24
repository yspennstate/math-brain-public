# P0017 boundary lane, w354

The exact intake question is the universal Euclidean Cheeger lower bound for every isotropic log-concave probability, in every dimension. Its cited source is Randomstrasse101: Open Problems of 2025, arXiv:2603.29571v1, Entry 13, Definition 13.1 and Conjecture 30. The covariance form is h(mu)>=c/sqrt(||Cov(mu)||_op). In isotropic position the equivalent Poincare target is Var_mu(f)<=C E_mu|grad f|^2 for one universal C and every locally Lipschitz f with finite L2 norm and gradient energy. Full details and exact assumptions are in STATEMENT.md and SOURCE_STATUS.json.

Current literature: Bizeul, Klartag and Lehec, arXiv:2610.05474v1 (4 October), Theorem 1.1, claims the full target. Balasubramanian and Kasiviswanathan, arXiv:2610.07728v2 (8 October), also claims a full bound C_P<=25. I checked those primary statements, not their proofs. Current openness is UNKNOWN under this lane's verification standard; no novelty claim is made.

The September attempt at-p0017 proves the Gaussian special case C_P=1 by Hermite expansion. Its recorded obstruction is the absence of that diagonal Gaussian generator for arbitrary log-concave measures. Exact-ID checks in attempts H/I found no additional P0017 attempt; the Lean campaign supplies a ranking annotation rather than a recovered theorem receipt. The live store still contains the dated unverified question and Gaussian attempt. This lane is disjoint from that computation and the other localization/cumulant lanes. The averaging bridge below is a route stress-tested here, not falsely attributed to the older attempt.

## Scale boundary

Let U_L be uniform on [0,L], L>0. Then Var(U_L)=L^2/12. The cosine expansion for the Neumann quadratic form gives C_P(U_L)=L^2/pi^2; the first cosine attains equality. A half interval has Cheeger ratio 2/L. Every finite-perimeter nontrivial subset has at least one interior boundary point, giving perimeter at least 1/L and denominator at most 1/2; approximation extends this to the usual outer Minkowski definition. Hence h(U_L)=2/L.

This identifies the necessary scale normalization. It is not a counterexample to KLS with covariance normalization. In standardized coordinates the interval has C_P=12/pi^2 and h=1/sqrt(3).

## Substantive boundary attempt and saved sharp result

Disintegrate an isotropic law along a direction v, apply the exact one-dimensional Poincare inequality on each fiber, then try to bound the conditional constants by isotropy. The uniform isotropic simplex refutes a uniform fiber bound: its essential supremum is 2(d+1)(d+2)/pi^2, while its mean is only 12/pi^2. Every nearly maximal fiber neighborhood has positive projection probability.

A second attempt replaces the weighted expectation of conditional constants times conditional gradient energies by the product of their expectations. This step is false. In the isotropic triangle, the explicit polynomial f=T(1-S)^2 gives conditional variance 1/2 and directional energy 1/3, whereas the proposed bound supplies only 4/pi^2. Full energy is 13/27, so the full-gradient quotient is 27/26. For every dimension the optimal directional conditional bound equals the essential supremum, proved by localized Neumann modes. Complete definitions and proofs are saved in SIMPLEX_PROOF.md; claims 001-004 are saved in CLAIMS.jsonl.

Measurements: measure_boundary.py checked 11,245 exact arithmetic identities across seven dimensions in 0.05667 seconds. At dimension 100 the exact sup/mean factor is 1,717. check_polynomial.py independently expanded and integrated raw-coordinate monomials, confirming all seven polynomial checks in 0.00054 seconds. These checks validate the calculations; they are neither a formal theorem receipt nor a measurement of a deployed brain improvement.

## Single hardest remaining gap in this worker's route

Control the correlation between fiber Poincare constants and localized directional gradient energy using the orthogonal gradient energy, for arbitrary isotropic log-concave probabilities. Neither a uniform fiber bound nor arithmetic averaging provides that estimate. This is the gap in this worker's route, not a claim that the recent primary proof claims have a gap. Independent audit of the saved special cases remains pending.
