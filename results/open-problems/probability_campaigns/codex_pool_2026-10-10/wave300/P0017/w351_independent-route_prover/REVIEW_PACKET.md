P0017 / w351 / independent conditional-variance route, 2026-10-10.

Referee: w353. Adversary: w352. Supervisor: claude-4a88bc43. No independent keep has been received; all own proof claims remain drafts. The full target is not independently proved here, and October primary papers already claim it. Current openness: UNKNOWN. No novelty claim.

Read ATTEMPT.md for the complete proofs and exact gap, CLAIMS.jsonl for individually reviewable rows, SOURCE_STATUS.json for the dated literature check, and PRIOR_ATTEMPT_DIGEST.md for route separation. The earlier local method was Gaussian Hermite expansion; this packet uses conditional variances and explicit simplex fibers. STATEMENT_FOR_ADVERSARY.md is the statement-only handoff, prepared before any peer proof was read.

Please check these obligations in order:

1. L0: affine normalization, with positive-definite covariance and the same locally Lipschitz test class.
2. L1: conditional expectation is an orthogonal projection; maximal correlation controls all centered block functions; M_U refers to U given V and M_V to V given U. Verify the projection inequality and conditional slicing before its Euclidean-energy corollary.
3. L2: simplex covariance is identity on the sum-zero hyperplane; the projected vertices are affinely independent; conditioning fixes S and yields a uniform edge interval. Verify its exact variance and Neumann constant.
4. L3: the beta moments and tail formula; existence of a compact interior bump in S>1-delta; the directional-energy ratio and its sharp limiting constant. Keep the full transverse energy in any global Poincare comparison.
5. L4: the fourth moments and positive nonlinear-correlation lower bound despite zero linear cross-covariance. It is a lower bound, not a usable upper bound for L1.

Single hardest gap: a dimension-independent estimate for weighted correlated conditional energies using the full gradient for arbitrary isotropic log-concave laws. Uniform slice constants, averaged slice constants, and zero linear covariance do not close it.

Validation is deliberately separated: python -X utf8 verify_small.py checks artifact structure only; python -X utf8 verify_small.py --numerical first reads a fresh governor state and holds with exit 75 on distress or critical reasons. Exact proofs are in ATTEMPT.md. The saved initial compute gate reports distress; no quadrature, model or GPU experiment has been run at that gate. No Lean theorem, trusted-axiom receipt or admitted-placeholder proof is claimed.

Brain delivery is a small concept-only DRAFT bundle. Its publication, independent review, ingestion and retrieval receipts are distinct in SUBMISSION_STATE.json. RELATION_EVIDENCE.jsonl quotes both supporting ends. The source tag is owner-own-work. The worker never invokes the integrator or writes the live mathematical store.

The hook is staged locally because the worker's folder-only rule forbids directly editing global hook proposals. The reviewer may apply the corresponding unified diff after auditing it.

NEXT: w353 checks L2/L3's slice normalization and localized test function first; run numerical checks only after a fresh non-distress compute gate.
