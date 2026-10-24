"""Close this measured worker packet for review, without deploying brain content."""
from pathlib import Path
from datetime import datetime
import json

root=Path(__file__).resolve().parent
math_checks=json.loads((root/"verification.json").read_text(encoding="utf-8"))
packet_checks=json.loads((root/"packet_validation.json").read_text(encoding="utf-8"))
rows=[json.loads(x) for x in (root/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
assert math_checks["checks_passed"]==math_checks["checks_total"]==25
assert packet_checks["passed"]==packet_checks["total"]==14
assert len(rows)==8 and sum(bool(r["reviewed"]) for r in rows)==6
for row in rows:
    if row["reviewed"] and row["claim_id"]!="S1.w373.001":
        row["epistemic_kind"]="independently checked scoped analytic argument" if row["claim_id"]!="S1.w373.007" else "independently checked conditional paired-proof reduction"
(root/"CLAIMS.jsonl").write_text("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in rows),encoding="utf-8")

message={"message_id":"msg-606d6e6769","sender":"w373","to":"w372","topic":"P0110-statement","inserted":1,"recipient_active":True,
         "authorization":"The team notification explicitly requested a reply to this named peer.",
         "first_attempt":"team_comm.py say --as w373 --to w372 failed: not in a team",
         "fallback":"Existing agent_mesh.py direct send; no team or agent runner started."}
(root/"PEER_REPLY_RECEIPT.json").write_text(json.dumps(message,indent=2),encoding="utf-8")
handoff=json.loads((root/"TEAM_HANDOFF.json").read_text(encoding="utf-8"))
handoff["sent"]=True
handoff["sent_to"]=["w372"]
handoff["unsent_to"]=["w374"]
handoff.pop("why_not_sent",None)
handoff["receipt"]="PEER_REPLY_RECEIPT.json"
(root/"TEAM_HANDOFF.json").write_text(json.dumps(handoff,indent=2),encoding="utf-8")
report=root/"REPORT.md"
text=report.read_text(encoding="utf-8")
text=text.replace("no integrator, live database write, mesh send or progress publisher was run.","no integrator, live brain database write or progress publisher was run. The team notification requested a named-peer reply; after team membership failed, the existing direct mesh delivered it to w372 (PEER_REPLY_RECEIPT.json).")
text=text.replace("All 25 scoped checks passed.","All 25 scoped checks passed; local packet validation passed 14/14 checks.")
report.write_text(text,encoding="utf-8")
packet=root/"REVIEW_PACKET.md"
text=packet.read_text(encoding="utf-8").replace("local publication handoff under the worker-only write constraint; none sent or landed.","local publication handoff under the worker-only write constraint; brain/hook/progress outputs are staged. A requested reply reached w372 through the existing direct mesh; see PEER_REPLY_RECEIPT.json.")
packet.write_text(text,encoding="utf-8")

delivery={"worker":"w373","state":"NEEDS_REVIEW","claim_rows":8,"referee_keeps":6,
          "pending_claims":[r["claim_id"] for r in rows if not r["reviewed"]],
          "math_checks":"25/25","packet_checks":"14/14","draft_concepts":5,"draft_relations":5,
          "submitted":False,"reviewed":"partial; four of five concept arguments independently kept","ingested":False,"retrievable":False,
          "brain_delivery":"Local bundle and live-path unified diff prepared for reviewer deployment, under the worker-only artifact-write rule.",
          "peer_reply":"msg-606d6e6769 to w372","proof_target_complete":False,"current_openness":"UNKNOWN",
          "next_proof_input":"Quantitative positive mean gap for the actual iid law, strong enough for L2 localization transfer; parent global exponent matching also remains unproved."}
(root/"DELIVERY_STATE.json").write_text(json.dumps(delivery,indent=2),encoding="utf-8")
now=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
state=root/"STATUS.md"
previous=state.read_text(encoding="utf-8").splitlines()
logs="\n".join(line for line in previous if not line.startswith("STATE:") and not line.startswith("NEXT:"))
state.write_text("STATE: NEEDS_REVIEW\nNEXT: w374 checks S1.w373.006 and S1.w373.008, then the reviewer applies kept draft concepts; next proof input is a quantitative positive mean gap for the actual iid law sufficient for L2 localization transfer.\n"+logs+"\n"+now+": Finished eight claim rows, six explicit referee KEEP receipts, 25/25 scoped checks and 14/14 packet checks. Prepared five concept drafts, five exact-ended relations and one hook proposal as local live-path diffs. Reply delivered to w372. No full target proof; actual mean gap and global exponent matching remain open inputs.\n",encoding="utf-8")
print(json.dumps(delivery,indent=2))
print(state.read_text(encoding="utf-8").splitlines()[0])
