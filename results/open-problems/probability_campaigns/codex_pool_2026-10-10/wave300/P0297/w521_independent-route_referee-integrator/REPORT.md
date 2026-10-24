# P0297 referee and math-brain draft, 2026-10-10

## Found

Gwynne--Miller, *Inventiones Mathematicae* 223 (2021), online 2020, Problem 7.1 asks for the exact Hausdorff dimension d_gamma of the canonical gamma-LQG metric for every gamma in (0,2). The known sqrt(8/3) value is 4. A 2026 ICM invited lecture still calls general d_gamma unknown. The paper explicitly says Watabiki's proposed formula fails for sufficiently small gamma. Links and scope checks are in `SOURCE_STATUS.json`.

The read-only store query found an existing P0297 problem card and an attempt card. Both have `truth_status=unverified`; the attempt gives xi*d=gamma but explicitly no general value. The new draft links these cards to a primary-source correction and the Watabiki obstruction.

## Reviewed

`REVIEW_PACKET.md` independently rederives w519 W519-L1 and the w520 snowflake lemma: two KEEP verdicts with scope limits. Neither determines d_gamma. My independent metric-ball covering route and conditional lemma are in `ATTEMPT.md` and `CLAIMS.jsonl`; the lemma remains a sketch pending w524's independent check. Direct requests through team_comm and agent_mesh failed respectively because w521 has no team membership and w524 is not a registered recipient. The request and exact audit target are preserved in `REVIEW_PACKET.md`.

## Draft and measurement

Submitted `~/math-brain-inbox/w521/bundle_001.json` and `bundle_002.json` as complete drafts. Each has 2 concepts and 3 relations: 4 concepts and 6 relations total. The second is an attributed, independently checked derivative of w520's two distinct obstruction concepts. `python -X utf8 ~/brain_workers/w521/validate_bundle.py bundle_001.json` and the same command for `bundle_002.json` validate the schemas and byte-identical submitted copies. Before the drafts, the read-only store query had the existing P0297 problem and attempt cards but not these four logical IDs. `python -X utf8 ~/brain_workers/w521/check_lifecycle.py` found **0 live nodes for all four new logical IDs after submission**. `BRAIN_STATES.json` records submitted, reviewed, ingested, and retrievable separately. These are reviewable proposals, not measured live recall improvements or a proof of P0297.

Nine later verdict rows in `VERDICTS.jsonl` cover w519 L2/L3/L4/L5/C2, w520 .002/.003 and w518 C1/C2. Primary theorem checks used Falconer--Jin Corollary 2.3 and Gwynne--Pfeffer Theorem 1.5. The historical D0049-A001 source line had the wrong `d_gamma=2Q/xi` twice; direct algebra gives `d_gamma=gamma/xi`. The known case yields 10 versus 4. `python -X utf8 ~/brain_workers/w521/verify_peer_patch.py` returned `PATCH_CHECK_OK source_line=43 changed_fields=2 untouched_fields=9` for w519's proposed correction diff. The diff is still unapplied. Direct verdict messages reached w519, w520 and w518; see `BUNDLE_REVIEW.md` for the one stale review-state string to fix in w519's submitted bundle.

The hook proposal `~/primary_directive/hooks1000/proposals/math-p0297-w521.jsonl` names the proof-gap scar and has a fire and silent case. Its state is proposed, not kept or installed.

The final probability integration handoff was delivered to codex-01a12190 as mesh message `msg-44e69129ce`, with exact packet, bundle, and patch paths. The bundle spec reserves digests for the validating coordinator. I have no response-side served-model receipt and make no served-model claim. The progress page logged both the initial draft and the final 4-concept/6-link review state.

## Apply and risk

No live-file patch is authored by w521. The validating coordinator should audit the exact source rows and run the normal draft integrator for the w521 inbox; do not ingest the pending w521 conditional lemma as a theorem. w519's separately proposed source patch has a mathematical and exact-line KEEP from this referee, but its historical file remains unchanged. The primary-source card can duplicate the older secondary-source card if the cross-link is skipped. A newer general-dimension result after the latest checked 2026 lecture has not been exhaustively ruled out.

NEXT: Route `w521.P0297.conditional-covering.001` to w524 for KEEP/FIX/DROP; pair-audit and ingest the two w521 drafts, then test retrieval. Apply w519's reviewed two-field correction through the coordinator. Re-audit any later load-bearing claim separately.
