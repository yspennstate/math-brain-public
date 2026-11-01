import json,sys
from pathlib import Path
root=Path(__file__).resolve().parent
names=["SOURCE_STATUS.json","MEASUREMENTS.json","BUNDLE_VALIDATION.json","DELIVERY_STATE.json","HANDOFF_RECEIPT.json","DRAFT_BUNDLE.json"]
data={n:json.loads((root/n).read_text(encoding="utf-8")) for n in names}
assert data["SOURCE_STATUS.json"]["current_openness"]=="UNKNOWN"
assert data["MEASUREMENTS.json"]["measurements"]["passed"]==22
assert data["BUNDLE_VALIDATION.json"]["schema_check"]=="PASS"
delivery=data["DELIVERY_STATE.json"]
assert delivery["submitted"] and not delivery["ingested"] and not delivery["retrievable"]
p=Path(delivery["inbox_file"])
assert p.parent.resolve()==Path("~/math-brain-inbox/w405").resolve()
assert json.loads(p.read_text(encoding="utf-8"))==data["DRAFT_BUNDLE.json"]
claims=[json.loads(x) for x in (root/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
assert len({c["id"] for c in claims})==len(claims)
assert all(c["status"] in {"conjecture","numerical evidence","sketch","proved special case","independently checked proof"} for c in claims)
hook=json.loads((root/"HOOK_PROPOSAL.jsonl").read_text(encoding="utf-8"))
assert len(hook["text"])<=300
assert (root/"GAP.md").exists() and (root/"REPORT.md").exists()
memory=json.loads((root/"MEMORY_RECALL_RECEIPT.json").read_text(encoding="utf-8"))
receipt={"artifact_check":"PASS","tests":"22/22","claims":len(claims),"draft_entries":len(data["DRAFT_BUNDLE.json"]["entries"]),"draft_relations":len(data["DRAFT_BUNDLE.json"]["relations"]),"inbox_file":str(p),"general_recall_elapsed_seconds":memory["elapsed_seconds"],"general_recall_exit":memory["exit_code"],"general_recall_blocked_lock_opens":len(memory["blocked_side_effects"]),"hook_characters":len(hook["text"]),"referee_delivery":data["HANDOFF_RECEIPT.json"]["delivery_state"],"mathematical_claim":"P0003 unresolved; referee pending; finite fixtures are not a proof of the target"}
(root/"FINAL_CHECK.json").write_text(json.dumps(receipt,indent=2),encoding="utf-8")
if "--finish" in sys.argv:
    old=(root/"STATUS.md").read_text(encoding="utf-8")
    log="\n2026-10-10: Deliverables complete and measured; 22/22 deterministic checks and final artifact checks pass. DRAFT bundle submitted to "+str(p)+". Source mismatch corrected; w406 original L1/L2/R1 KEEP recorded; final w407 review pending. General read-only recall timed out at 59.151 s; named scar fallback and targeted read-only theorem lookup completed. Hook/progress rows queued locally under folder-only constraint. No live-store ingestion or global recall edits.\n"
    lines=old.splitlines()
    lines[0]="STATE: NEEDS_REVIEW"
    for i,s in enumerate(lines):
        if s.startswith("NEXT:"):
            lines[i]="NEXT: w407 reviews the final packet (or supervisor routes the unregistered reviewer); then establish a fixed-length buffered counting-ratio estimate."
            break
    (root/"STATUS.md").write_text("\n".join(lines)+"\n"+log,encoding="utf-8")
print(json.dumps(receipt,indent=2))
