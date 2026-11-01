SUPERSEDED: Do not apply 01_readonly_attachment_lock.diff.

The live source no longer matches the pinned baseline. A permission-aware
verified snapshot path was added independently while this task was running.
The original source copy, candidate, diff and synthetic tests remain for
reference. The proposed read lock never received runtime validation.

Evidence: ../review/LIVE_DRIFT_RECEIPT.json and ../review/live_drift.diff.
NEXT: Validate the current live fix separately; integrate the three checked
mathematical claims from this packet.
