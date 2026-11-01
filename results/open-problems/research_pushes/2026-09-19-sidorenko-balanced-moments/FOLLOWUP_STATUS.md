# Continuation after the balanced-moment delivery

19 September 2026. The positive quantitative theorem remains in BALANCED_MOMENTS.md. The following work tests proposed ways to turn that theorem and the earlier mixed-spectrum method into a full proof.

- RESIDUAL_CORRECTION.md: the separate remainder R>=0 suggested in the earlier mixed-spectrum note is false, even for a positive two-block kernel with ||W-1||_infinity=1/5. Its earlier proved results remain intact. The combined positive part plus remainder is a different, still-unproved target.
- TENSORIZATION.md: tensor products give an exact scalar amplification rule, but the naive fixed-parameter version can worsen rather than improve the certificate. This does not rule out all tensor arguments.
- AFFINE_ENTROPY.md: the common-latent trial distribution gives log t_H>=5D3-D5, but D5<=5D3 is false for an explicit symmetric regular 81-state kernel. In fact no uniform coefficient bounds D5 by D3 in this entire kernel class. A separate finite-field flow formula proves that the examples themselves satisfy Sidorenko for every bipartite graph.

All three check programs were executed and passed with exact arithmetic. FOLLOWUP_CHECKS.json records their outcomes; each script regenerates its complete JSON output. The finite counts do not replace the written analytic proofs. No independent audit or novelty certification is claimed, and none of the examples is a counterexample to Sidorenko.

Current full-target status: PARTIAL. The globally valid balanced-moment lower bound is not proved to admit a successful parameter choice for every kernel. The work identifies real obstructions to three shortcuts, rather than promoting them to a completion.
