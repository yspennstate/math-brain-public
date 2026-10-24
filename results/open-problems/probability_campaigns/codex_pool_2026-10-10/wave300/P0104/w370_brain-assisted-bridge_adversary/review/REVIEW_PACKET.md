# w370 P0104 review packet

For w371 and claude-4a88bc43. Current global openness UNKNOWN; P0104 is
not solved by this work.

1. w371 KEEP: claim 002, the exact abstract 3/8 rare-event sequence in
   INDEPENDENT_BRIDGE.md. The all-parameter tail bound and divergent
   standardized fourth moment were independently reproduced. It is not
   an iid lattice FPP construction.
2. w371 KEEP: claim 003, the conditional bridge under uniform centered
   kurtosis and nondegenerate weak scaling, including arbitrary centers
   by symmetrization. Both lattice inputs remain unproved.
3. w371 KEEP: claim 005, the uniform interval premise implying
   Var(X)>=epsilon L^2/4. This corrects only a categorical inference on
   the recalled card. It does not reassert the paper theorem.
4. Review drafts/bundle_001.json and EDGES.jsonl for integration using
   review/REFEREE_VERDICTS.jsonl. New result nodes remain concepts with
   proof_text null. Full bundle/edge admission, submission, ingestion
   and retrievability have not been certified.
5. The historical reader-lock proposal is SUPERSEDED. Do not apply
   patches/01_readonly_attachment_lock.diff. The observed live code has
   a permission-aware snapshot fallback; review/live_drift.diff and
   review/LIVE_DRIFT_RECEIPT.json preserve the exact difference.

The old synthetic test command is preserved for reference:

    python -X utf8 ~/brain_workers/w370/test_read_lock.py

Three unchanged admission gates rejected tests at CPU 80.9%, 88.4% and
85.5%; no fixture test ran. Retain the fixed 75% CPU / 2 GiB RAM limits
and 20-second test budget for any subsequent runtime validation. The
archived test compares historical copies and does not validate the new
live fallback. No end-to-end recall improvement is claimed.

validation_receipt.json records schema/AST checks and the observed source
hashes. Those checks do not establish lock behavior, concurrency or a
mathematical theorem. No formal checker ran. All worker writes remain
under w370; outbox/ contains staged notices and progress rows.

NEXT: Integrate the independently checked mathematical drafts and
validate the current live fallback separately. For P0104, bound actual
Doob cross and cubic sums relative to Var(T_n)^2; the conditional bridge
does not supply that estimate.
