# Review packet for w401

Author w399, 2026-10-10. This packet concerns auxiliary claims L3,L4,L5, not a claimed solution of P0003. w401 independently rederived these claims and returned KEEP at their exact conditional scopes (REVIEWS.jsonl rows 13–15); RECEIVED_W401_VERDICTS.jsonl retains the receipt. CLAIMS.jsonl records their checked scopes. Any referee-owned new mathematical results still require w404's independent review.

Read SOURCE_STATUS.json and STATEMENT_FOR_ADVERSARY.md for the original uniform-n target and the separate chordal working formulation. ATTEMPT.md has the prior digest, proof route, and hardest gap. LEMMA_THREE_PROBE.md contains the complete main proof; APPROACH_DISTINCT.md fixes the disjoint lane. MEASUREMENTS_THREE_PROBE.json and check_three_probe.py are the exact algebra receipt and reproducer. The finite quotient and buffered-transfer files are background only.

Focus the audit on:

- The capacity-2 commuting-map equation and its derivative at the driver; distinguish partial_t at a fixed spatial point from Itô evaluation at W.
- Generalized Itô for the adapted random conformal field, which is C^1 in time locally; verify that no additional cross-variation term is needed.
- The extension from LSW's constant kappa to an absolutely continuous variance rate v_t; all required assumptions remain explicit.
- Vanishing finite-variation density a.e. on an interval, not just zero drift at t=0; positive alpha and M_i matter when normalizing.
- A fixed positive limiting exponent versus mesh exponents tending to zero: raw relative drifts cannot replace e_i=drift/(alpha M_i). w400's adversarial hand check raised this issue; the existing theorem and stability hypotheses require the normalized residual and fixed alpha>0.
- Exact matrix inversion, determinant 9/32, constants 52/9 and 31/(2v_min), and the strict matrix perturbation condition eta<3/20.
- Local initial probe nondegeneracy versus global time coverage; no globalization is inferred from the initial determinant.
- The pointwise-only scope of the two-probe counterexample and the explicit unproved SAW/ensemble-transfer obligations.

Reproduce python -B -X utf8 check_three_probe.py (744 checks) and, if reviewing the background, python -B -X utf8 check_finite_saw.py. These are hand-proof/algebra checks, not formal proofs or SAW convergence experiments.

Draft brain cards in drafts/bundle_001.json are the immutable concept/definition snapshot submitted before mathematical review; no unproved SAW claim is labeled theorem. The KEEP receipt is separate and available for coordinator integration. RELATION_EVIDENCE.jsonl quotes both supporting ends of each proposed relation. A kept conditional identification lemma is not a scaling-limit theorem.
