"""Record the assigned referee's verdicts; do not re-audit the referee."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
peer=Path("~/brain_workers/w401/REVIEWS.jsonl")
selected=[]
for number,line in enumerate(peer.read_text(encoding="utf-8").splitlines(),1):
    row=json.loads(line)
    if str(row.get("claim","")).startswith("w399-"):
        selected.append(dict(row,source_line=number,source_path=str(peer)))
with (ROOT/"RECEIVED_W401_VERDICTS.jsonl").open("w",encoding="utf-8") as handle:
    for row in selected:
        handle.write(json.dumps(row,ensure_ascii=False)+"\n")
verdicts={row["claim"]:row for row in selected}
mapping={
 "w399-P0003-L1":"w399-P0003-L1",
 "w399-P0003-L2-background":"w399-LEMMA_BUFFERED_TRANSFER",
 "w399-P0003-L3":"w399-P0003-L3",
 "w399-P0003-L4":"w399-P0003-L4",
 "w399-P0003-L5":"w399-P0003-L5",
 "w399-P0003-L6-background":"w399-COUNTEREXAMPLES",
 "w399-P0003-L7-background":"w399-COUNTEREXAMPLES",
 "w399-P0003-G1":"w399-P0003-G1"
}
for claim_id in ["w399-P0003-L3","w399-P0003-L4","w399-P0003-L5"]:
    assert verdicts[claim_id]["verdict"]=="KEEP"
claims_path=ROOT/"CLAIMS.jsonl"
original=claims_path.read_text(encoding="utf-8")
snapshot=ROOT/"CLAIMS_AUTHOR_STAGE.jsonl"
if not snapshot.exists():
    snapshot.write_text(original,encoding="utf-8")
claims=[json.loads(line) for line in original.splitlines()]
for c in claims:
    peer_id=mapping.get(c["claim_id"])
    if peer_id is None:
        continue
    row=verdicts[peer_id]
    assert row["verdict"]=="KEEP"
    c["review_evidence"]=row
    c["independent_reviewer"]="w401; KEEP at exact scope; RECEIVED_W401_VERDICTS.jsonl"
    if c["status"]=="proved special case":
        c["status"]="independently checked proof"
    c["review_scope_only"]=True
with claims_path.open("w",encoding="utf-8") as handle:
    for c in claims:
        handle.write(json.dumps(c,ensure_ascii=False)+"\n")
delivery_path=ROOT/"DELIVERY_STATUS.json"
delivery=json.loads(delivery_path.read_text(encoding="utf-8"))
delivery.update(reviewed=True,reviewer="w401",review_scope="Auxiliary proofs and gap labels at exact conditional scopes; not the full P0003 target",review_receipt="RECEIVED_W401_VERDICTS.jsonl",review_verdict="KEEP",submitted_snapshot="Five concept/definition entries remain the pre-review DRAFT snapshot; coordinator may use this independent receipt. No published draft is overwritten.")
delivery_path.write_text(json.dumps(delivery,indent=2)+"\n",encoding="utf-8")
source_path=ROOT/"SOURCE_STATUS.json"
sources=json.loads(source_path.read_text(encoding="utf-8"))
sources["independent_reviewer"]="w401; KEEP L1/L3/L4/L5 and background auxiliary scopes; full target unproved"
sources["independent_review_receipt"]="RECEIVED_W401_VERDICTS.jsonl"
source_path.write_text(json.dumps(sources,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
receipt={"reviewer":"w401","state":"reviewed","verdict":"KEEP","claims":[c["claim_id"] for c in claims if "review_evidence" in c],"proof_scope":"Auxiliary conditional/finite proofs only","full_target_proved":False,"ingested":None,"retrievable":None,"source":"RECEIVED_W401_VERDICTS.jsonl"}
(ROOT/"REVIEW_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
with (ROOT/"HANDOFFS.jsonl").open("a",encoding="utf-8") as handle:
    handle.write(json.dumps(dict(receipt,kind="assigned-referee-KEEP-received"))+"\n")
print(json.dumps(receipt,indent=2))
