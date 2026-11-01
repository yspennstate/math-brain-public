"""Close this one worker task with durable, qualified review state."""
from pathlib import Path
import datetime as dt
import json

root=Path(__file__).resolve().parent
check=json.loads((root/"FINAL_CHECK.json").read_text(encoding="utf-8"))
assert check["inbox_delivery_matches"] and check["claims"]==6
source=json.loads((root/"SOURCE_STATUS.json").read_text(encoding="utf-8"))
source["brain_bundle"]["state_meaning"]="Booleans record confirmed receipts. Independent review, ingestion and retrieval have no confirming receipt; their false values are not an absence proof."
(root/"SOURCE_STATUS.json").write_text(json.dumps(source,indent=2)+"\n",encoding="utf-8")
handoff={"closed_utc":dt.datetime.now(dt.timezone.utc).isoformat(),"worker":"w517","state":"NEEDS_REVIEW",
         "review_packet":"~/brain_workers/w517/REVIEW_PACKET.md","reviewer":"w518 (pending)",
         "final_peer_message":"msg-d21ee4a1e8","prior_peer_messages":["msg-2a3612bbd7","msg-5dd487579f","msg-1280107549","msg-b126fd5989"],
         "progress_rows_posted":["S1.P0297.NT","S1.P0297.packet"],"mesh_claims_released":2,
         "open_votes_last_read":[],"draft_concepts_submitted":4,"relations":3,"claim_rows":6,"author_audit_keeps":5,"open_gap_rows":1,
         "mathematical_review_confirmed":False,"formal_check_performed":False,"live_ingestion_confirmed":False,
         "numeric_controls":"deferred while fresh gate reported owner_present_polite",
         "global_hook":"one proposal and unified diff staged locally for reviewer placement"}
(root/"HANDOFF_RECEIPT.json").write_text(json.dumps(handoff,indent=2)+"\n",encoding="utf-8")
lines=(root/"STATUS.md").read_text(encoding="utf-8").splitlines()
lines[0]="STATE: NEEDS_REVIEW"
next_step="NEXT: w518 checks NT/3R and O2; the concrete proof continuation is a cutoff-uniform estimate for the competitive weighted gap law in the full LFPP denominator."
lines=[next_step if line.startswith("NEXT:") else line for line in lines]
lines.extend([
    "2026-10-10: Delivered four explicitly unreviewed concept DRAFTs and three supported relations to math-brain-inbox/w517/bundle_001.json at 05:52:14 UTC. Structural parser: zero errors. Review, ingestion and retrieval remain unconfirmed.",
    "2026-10-10: FINAL_CHECK.json confirms 15 required artifacts, six claim rows, five qualified author-step KEEP verdicts, one OPEN full-target gap, one local hook proposal and matching inbox delivery. Numerical controls were deferred while the fresh gate reported owner_present_polite; no numerical experiment or formal checker ran.",
    "2026-10-10: Posted final progress row S1.P0297.packet, sent final referee handoff msg-d21ee4a1e8, reread OPEN_VOTES (empty), and released both mesh claims. REPORT.md and REVIEW_PACKET.md distinguish author proofs from independent review. No exact generic LQG dimension or novelty is claimed.",
])
(root/"STATUS.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
saved=(root/"STATUS.md").read_text(encoding="utf-8").splitlines()
assert saved[0]=="STATE: NEEDS_REVIEW" and saved[1]==next_step
print(saved[0])
print(saved[1])
print("Artifacts checked; DRAFT delivery confirmed; referee review pending.")
