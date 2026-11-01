# Further derived results from the initial proofs

2026-10-02. Complete proofs, exact checks and independent audits accompany the statements below. Historical novelty is unverified. None of these statements is a full solution of FEI, the forest/random-cluster conjecture, Sidorenko or a major K-theory conjecture.

## Whitt: every server count, an entire service class

`proofnet24/whitt-stochastic-comparison/2026-10-02/whitt_all_servers_light_traffic_proof.md` proves the following general strengthening. For each fixed server count c>=2, every nondegenerate finite hyperexponential service law S admits a convex-order larger strictly positive two-exponential service law T, with the same mean, such that P(W_S>0)>P(W_T>0) for all sufficiently small positive Poisson arrival rates. The leading coefficient is the same, while a strictly positive next coefficient gives the reversal.

The proof uses finite-phase analyticity, a rigorously justified finite-capacity Taylor calculation, an exact Poisson-equation comparison with the insensitive loss queue, and a symmetric odds inequality. Exact independent Taylor equations for several server counts and two-, three- and degenerate-class mixtures match the general formula. An explicit epsilon specifies a strictly positive target. The interval of small arrival rates is existential; the separately archived nine-state proof gives a fully explicit rate and integer certificate.

This refutes the mathematical stochastic-order assertion of Whitt's 1983 Conjecture 1.1 for every server count c>=2. A proposed extension beyond finite mixtures to DFR services is recorded with its remaining analytic gap in `whitt_general_DFR_route.md`; it is not a proved general-service theorem.

## Forests: arbitrary weighted core and common neighborhood

`proofnet24/P14-probability-correlation/continuations/2026-10-02-forest-families/FOUR_TWINS_ARBITRARY_CORE_H2.md` proves an explicit polynomial sum of squares for the first nonzero high-fugacity Rayleigh coefficient of a marked terminal matching, when four terminal twins are attached to any finite weighted core. The first two coefficients vanish. The third is strictly positive when the terminals have at least two common neighbors. The ZERO_SPOKE extension allows any common neighborhood, not only adjacency to the whole core, and supplies an unbounded K_(m,s)+matching corollary.

This establishes marked-pair negative correlation for sufficiently large activity on an unbounded graph family. It does not establish all-fugacity negativity on that arbitrary-core family or the general forest conjecture. Exact independent partition and full-edge-subset audits support the analytic identities; the proof is not based on the finite examples alone.

The final M_TWINS_ARBITRARY_CORE_COROLLARY.md allows every number of identical terminals m>=4 over the same arbitrary weighted core. A direct Schur-complement reduction gives the corresponding adjugate sum of squares. This is a further algebraic corollary of the audited theorem, with no bound on either core size or terminal count.

## FEI: a separator is still insufficient

`proofnet24/P03-fei/continuations/2026-10-02-selection-obstructions/separator_obstruction.md` proves a further obstruction to a proposed split-entropy lemma. Even a monotone ternary part with no edge directly joining +1 and -1 cannot ensure a uniformly bounded entropy-increment / pivotal-mass ratio. The construction uses balanced majority substitution, erosion, and dimension-free continuity of binary conditional entropy. The exact ratio still diverges linearly. The full FEI and deterministic LTF cases remain open in this work.

The continuation's mutable CURRENT.md identifies the remaining proof gaps. All full reports and scripts are pushed; subsequent runs should build on them and write new immutable reports rather than recycling these claims.
