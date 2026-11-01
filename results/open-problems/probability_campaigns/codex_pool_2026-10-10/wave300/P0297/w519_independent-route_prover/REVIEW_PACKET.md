# w519 P0297 referee packet

Referee: w521. Adversary: w520. Prepared independently before peer proof reads. The earliest statement-only handoff file is STATEMENT.md. Initial direct w520 sends failed while the recipient was unregistered; a final registration check found w520 and the statement-only retry succeeded. Its actual receipt is in OUTBOX.jsonl and COMM_RECEIPTS.json; acknowledgement is not verified. W521 received the complete review request as msg-e24c28ed8d. W520's STATUS.md independently records that their attempt was saved before reading w519.

The concrete source correction C2 is first: D0049-A001 writes d_gamma=2Q/xi in key_identity and method. The primary relation is xi=gamma/d_gamma. At the established Brownian-map parameter the incorrect expression yields 10 and the corrected one yields 4. CORRECTIONS.md gives the source row, hypotheses, primary locator and counterexample. patches/01_intake_D_lqg_dimension_identity.diff changes those two fields only; copies/intake_D_attempts.corrected.jsonl is the proposed complete copy. CORRECTION_MEASUREMENTS.json records two bad occurrences before, zero after, with all other fields preserved. The live row is untouched.

The mathematical attempt and prior-work digest are in ATTEMPT.md. Please audit the following exact statements, rather than infer parent success from a file or check result:

| Claim | Proof location | Requested check | State |
|---|---|---|---|
| W519-L1 | ATTEMPT.md first result | Subpower factor preserves a log exponent | w521 KEEP receipt already saved |
| W519-L2 | LEMMA_LOG_POTENTIAL.md | Positive Radon mass exponent implies finite logarithmic potential with the same exponent; a>0 is essential | Author proof; review pending |
| W519-L3 | LEMMA_SPECTRAL_OBSTRUCTION.md | Snowflake metric dimension, Brownian diagonal spectrum, mean exit PDE, and exclusion from length metrics | Scope control; no duplicate brain card |
| W519-L4 | LEMMA_EXPONENT_CANCELLATION.md | Conditional division of two positive log limits; metric scaling remains an assumption | Author proof; review pending |
| W519-L5 | LEMMA_GMC_COROLLARY.md | Falconer--Jin Corollary 2.3 applies to the unit disk and the stated GMC normalization; local weighting preserves exponents | Source-backed corollary; review pending |
| W519-C2 | CORRECTIONS.md | The two-field identity correction and exact 10-versus-4 counterexample | Source row; review pending |

G1: no explicit noncircular metric exponent b_gamma has been evaluated. L4 assumes its metric scale limit; L5 concerns Euclidean potentials. A correct proof of these lemmas is not a proof of the general dimension. Source-level current openness is reported by checked 2026 primary surveys; exhaustive current owner solved/retired status remains unverified. No novelty is asserted.

Reproduction commands: `python -X utf8 ~/brain_workers/w519/prepare_packet.py` prepares only worker-local copies, diffs, bundle and preflight; `python -X utf8 ~/brain_workers/w519/check_examples.py` calculates 26 deterministic scalar controls, including six distinct metric dimensions with spectral dimension 2. These controls are examples, not proof certification. PREFLIGHT.json checks six draft entries, seven allowed relations, acyclic depends_on and the actual existing target endpoint. RELATION_EVIDENCE.jsonl quotes both ends of every proposed relation.

No formal-check receipt exists. Trusted mathematical inputs are ordinary real/measure analysis (including Tonelli), the explicit Brownian Green kernel/PDE in the scope-control example, and Falconer--Jin's established exact-dimensionality corollary. No admitted formal placeholder is used. Official live ingestion is the validating coordinator's step after review; the worker has not run integrate_drafts.py.

The hook proposal is HOOK_PROPOSAL.jsonl with a narrow bad-identity promotion case and a silent correction case. patches/02_math_identity_hook_proposal.diff is its reviewable proposed placement; it has not been installed.

NEXT: Audit C2 and L2--L5 with their exact hypotheses; for further proof work derive an actual metric-radius estimate for G1 that does not use d_gamma as input.
