# ProofNet24 P20 — immutable readback correction / verification

**Canonical report:** `proofnet24/P20-kernel-hard-edge/runs/2026-09-16/2026-09-16_14-07-10__run-report.md`  
**Creation commit:** `dafd33bf76c6d180f17ca3920fccc88e75496504`  
**Verified report blob:** `37df94a4280a38a21569ba70e287abaac5f097c6`  
**Track:** `P20-kernel-hard-edge`  
**Delivery:** GitHub only; no email/Gmail action.

The complete immutable report was read back from the exact creation commit in contiguous ranges from its beginning through the terminal marker. The returned blob SHA was the same `37df94a4280a38a21569ba70e287abaac5f097c6` in every range.

One wording defect was found in Section 5 and is corrected here without overwriting the immutable report.

The report says:

> “For coordinate points other than `e_2`, (5.1) vanishes.”

Taken literally over all coordinate points, that sentence is false because

\[
q_*(e_d)=-1.
\]

The intended and sufficient statement is:

> **For the unchanged coordinate base points `e_1,e_3,\ldots,e_{d-1}`, equation (5.1) vanishes.**

This is exactly the set of coordinate points actually present in the unchanged physical star base after `e_2` is replaced. The point `e_d` is not among the coordinate base rows (the original star construction uses `e_1,\ldots,e_{d-1}`), so the orthogonality proof and every theorem are unchanged. The separate pair-point check for `(1,d)` remains correct: the product term contributes `-1/2` and the `x_1x_d` term contributes `+1/2`.

No other truncation, UTF-8 corruption, theorem-status mismatch, or proof-changing serialization defect was found in the exact-commit readback.

**Mathematical status after correction:** all claim statuses in the canonical report are unchanged. In particular `P20-AUDIT-P04-STAR-TUBE-66`, `P20-STAR-TRANSVERSE-RANK-EXACT-66`, `P20-PHYSICAL-STAR-TRANSVERSE-FAMILY-66`, `P20-STAR-CROSSOVER-EXACT-SECTOR-66`, `P20-STAR-CROSSOVER-LOWER-66`, and `P20-STAR-ENDPOINT-LOG-LOWER-66` retain their stated statuses.
