# P0297 independent adversary checkpoint

Saved before reading the paired prover's proof, 2026-10-10.

The exact target is pending primary-source recovery. The dated title alone does not distinguish the intrinsic Hausdorff dimension of the LQG metric from exponents defined through the LQG area measure.

Independent candidate obstruction C526.1: the two parameter identities Q=2/gamma+gamma/2 and xi=gamma/d leave d unspecified. For gamma=1 the choices d=3 and d=4 both fit, with xi=1/3 and xi=1/4. An attempted dimension computation must supply an independent relation involving the actual metric (for example the LFPP normalization exponent), rather than substitute an assumed d into xi=gamma/d and recover it.

This is an elementary algebraic obstruction, not a counterexample satisfying the full LQG metric axioms, and not a proof of the open target. Reviewer: w527; check pending.

Primary-source checkpoint, 2026-10-10 05:20 UTC: Gwynne-Pfeffer, arXiv:1905.11790v3, Definition 1.2, Theorem 1.4, Theorem 1.5, Corollary 1.7. No paired proof read yet.

Recovered target: for each fixed gamma in (0,2), determine the deterministic intrinsic Hausdorff dimension d_gamma of the canonical gamma-LQG metric. h is a whole-plane GFF (or a GFF plus continuous function on a nonempty planar domain). The metric is the canonical length metric, unique up to a deterministic factor. An exact determination is sought; an elementary closed form is not assumed to exist, and merely naming its ball-volume/LFPP exponent does not evaluate it. The known calibration is d_sqrt(8/3)=4. Current openness as of October 2026 remains UNKNOWN.

Independent obstruction C526.2: Theorem 1.4 requires a deterministic Borel X or a random Borel X independent of h. Take X to be the gamma-thick points instead. Equations (1.11) and Corollary 1.7 give dimensions (2-gamma^2/2, d_gamma). Inserting them in the independent-set equality gives 2 on the right, leaving a positive residual gamma^2/2. This is a counterexample to deleting the independence premise for every subcritical gamma.

Independent obstruction C526.3: at gamma=sqrt(8/3), a nonconstant LQG geodesic has intrinsic Hausdorff dimension 1. Invalid use of independent-set KPZ then predicts Euclidean dimension 3/4. Its Euclidean image is a connected set containing two distinct points, so a distance projection onto a real interval proves dimension at least 1. The missing premise is independence of the geodesic from h. No exact Euclidean geodesic dimension is needed for this contradiction.

Hardest missing piece: a field-independent computation of the LFPP normalization exponent (or equivalent numerical value of xi), without feeding an assumed d_gamma into the construction. Independent KPZ and thick-point variational identities can relate dimensions to d_gamma but do not by themselves identify it.

Final source recovery: the exact P0297 problem card identifies Rhodes-Vargas, arXiv:2509.21053v1, Section 3 / PDF page 4. Its primary text identifies the metric dimension as open as of September 2025. Ding-Dubedat-Gwynne, arXiv:2109.01252v2, Problem 5.1, gives the full equivalent Q(xi) formulation; equations (2.3)-(2.5) specify the median-crossing normalization a_epsilon=epsilon^(1-xi Q+o(1)). The math-brain old attempt explicitly leaves xi uncomputed. SOURCE_STATUS.json records the checked sources and the limits of current-status certification.

Finite bridge outcome: AUDIT_W525.json keeps the author's finite lemmas and the conditional reduction with uniform entropy control. FINITE_BRIDGE_INDEPENDENT.md supplies the separate derivation and C526.6, the integrated counterexample when that control is removed. It also records why the easier C526.5 absolute-bias example alone cannot refute an endpoint-difference reduction.

NEXT: w527 checks C526.2, C526.3 and C526.6; the next concrete proof step is to bound the signed response for the actual LFPP covariance and crossing paths with checked normalization.
