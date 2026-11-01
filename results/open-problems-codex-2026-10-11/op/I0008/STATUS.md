STATE: DONE
NEXT: Prove an ergodic rigidity or integrability estimate for the conditional local minimum M_0 in d>=2; separately find a superlinear anisotropic finite-SFE variational comparison.
VERDICT: PARTIAL

2026-10-12 first pass: Source arXiv:2609.01499v2 and Sheffield definitions verified; bounded literature search found no matching general solution. OpenAlex was rate-limited. Proved entropy/energy-integrability reduction and bounded-discrete-derivative special case; finite partition comparison kernel checked.
2026-10-12 second pass: Reopened at user request and set STATE: WORKING; reread the prior gap; queried the brain for DLR-to-energy-integrability, de Finetti canonical ensembles, and log-concave thermal bounds. Recorded two previously unused approaches in ATTEMPT.md Section 8.
2026-10-12 second pass: Pursued local heat-bath convexity. Proved E exp(Delta_x/2)<=3 without finite-SFE input, and reduced SFE finiteness to E M_0<infinity for integrable-slope invariant Gibbs laws. This controls fluctuations but leaves a precise ergodic-background gap.
2026-10-12 second pass: Constructed an exact translation-invariant nonergodic quadratic DLR mixture with integrable mean slope zero and infinite SFE. It demonstrates the necessity of ergodicity; it is not a counterexample to I0008.
2026-10-12 second pass: Also completed the one-dimensional de Finetti route: arbitrary coercive convex potentials yield iid exponential tilts, finite SFE and minimality at interior slope. This includes asymmetric superlinear potentials; no novelty claim. Higher-dimensional cycles obstruct the permutation argument.
2026-10-12 second pass: HeatBathHalving.lean passed kernel checking (53.03 seconds); 300 convex finite Hamiltonians, explicit boundary cases and asymmetric-tilt identities passed numerical checks. Handwritten infinite-volume steps were audited; no claim that the full proof is formalized.
2026-10-12 second pass: Closed this requested additional research pass as DONE / PARTIAL. Both full-source assertions remain unresolved in d>=2; exact remaining gaps are in ATTEMPT.md Section 13. Thirteen claim rows recorded.
