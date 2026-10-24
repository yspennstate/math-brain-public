"""Record observed audit receipts and close the authorized deliverable for review."""
import json
from pathlib import Path

root=Path(__file__).resolve().parent
validation=json.loads(root.joinpath("packet_validation.json").read_text(encoding="utf-8"))
assert validation["passed"]
audits_path=Path("~/brain_workers/w454/AUDIT.jsonl")
audits=[json.loads(line) for line in audits_path.read_text(encoding="utf-8").splitlines() if line]
targets={"w453-C0041-L1","w453-C0041-L2","w453-C0041-L3"}
accepted={row["target"]:row for row in audits if row.get("target") in targets and row.get("reviewer")=="w454" and row.get("status")=="independently checked proof"}
assert set(accepted)==targets
receipt={"reviewer":"w454","designated_referee":"w455","audit_path":str(audits_path),"accepted":[{"claim_id":target,"audit_id":row["id"],"verdict":row["verdict"]} for target,row in accepted.items()],"scope":"Original unconditioned L1/L2 statements and scoped L3 countermodel. New conditional alpha^-1 extension remains pending designated referee; no second-account or ingestion receipt is asserted."}
root.joinpath("INDEPENDENT_REVIEW_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
claims=[json.loads(line) for line in root.joinpath("CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line]
for claim in claims:
    if claim["id"] in accepted:
        claim["status"]="independently checked proof"
        claim["independent_reviewer"]="w454: "+accepted[claim["id"]]["id"]+"; designated referee w455 pending"
        claim["independent_review_evidence"]={"path":str(audits_path),"audit_id":accepted[claim["id"]]["id"],"scope":"The exact claim statement here; conditioning extension is a separate pending claim."}
assert len({r["id"] for r in claims})==len(claims)
root.joinpath("CLAIMS.jsonl").write_text("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in claims),encoding="utf-8")
states=json.loads(root.joinpath("BUNDLE_STATES.json").read_text(encoding="utf-8"))
states["independent_review_receipt"]="INDEPENDENT_REVIEW_RECEIPT.json"
states["reviewed"]=False
states["review_note"]="w454 accepted the original three claim statements; designated w455 review and the conditional extension remain pending. No mathematical two-account admission or store integration claimed."
root.joinpath("BUNDLE_STATES.json").write_text(json.dumps(states,indent=2)+"\n",encoding="utf-8")
report=root.joinpath("REPORT.md").read_text(encoding="utf-8")
report += "\n2026-10-10 final receipt: packaging and structural validation passed (6 entries, 6 relations, 7 claims). Inbox submission is complete. w454's saved audits KEEP the original L1/L2 and L3 statements; their exact receipt is INDEPENDENT_REVIEW_RECEIPT.json. The future-conditioning extension and designated referee review remain pending. Full packet reached active w455 through msg-7afe9fc051. Coordinate the exact-ID adapter with w454's reserved lookup-repair lane; only one implementation should land.\n"
root.joinpath("REPORT.md").write_text(report,encoding="utf-8")
communication={"event":"full-referee-packet","recipient":"w455","kind":"message","message_id":"msg-7afe9fc051","artifact":"~/brain_workers/w453/REVIEW_PACKET.md","delivery":"inserted 1; recipient active; saved receipt in referee_send_receipt.json","review":"pending"}
with root.joinpath("COMMUNICATION.jsonl").open("a",encoding="utf-8") as file:
    file.write(json.dumps(communication)+"\n")
status=root.joinpath("STATUS.md").read_text(encoding="utf-8").splitlines()
status[0]="STATE: NEEDS_REVIEW"
status[1]="NEXT: w455 audit the conditional alpha^-1 extension and L3 scope; then bound a fresh transverse escape before record-plane backtracking without reusing revealed rows."
status.append("2026-10-10: Deliverable complete and measured. DRAFT submitted to w453 inbox; 6 entries/6 relations structurally valid. Independent w454 receipts keep original L1/L2/L3; conditional extension and w455 referee review pending. C0041 not proved by this attempt; current openness UNKNOWN with a newer claimed resolution recorded. Live stores and recall controls untouched.")
root.joinpath("STATUS.md").write_text("\n".join(status)+"\n",encoding="utf-8")
print(json.dumps({"state":"NEEDS_REVIEW","submitted_draft":states["draft_path"],"independently_audited_original_claims":len(accepted),"conditional_extension":"pending w455","referee_message":"msg-7afe9fc051","next":status[1]}))
