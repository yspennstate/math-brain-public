"""Publish the already claimed, concept-only draft; never integrate a store."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

folder=Path(__file__).resolve().parent
inbox=Path(r"~\math-brain-inbox\w487").resolve()
target=inbox/"bundle_001.json"
part=inbox/"bundle_001.json.part"
if target.parent!=inbox or part.parent!=inbox:
    raise RuntimeError("Draft paths escaped the expressly named inbox directory")
data=(folder/"bundle_001.json").read_bytes()
bundle=json.loads(data)
assert bundle["spec"]=="mathbrain-draft-v1" and bundle["author_agent"]=="w487"
assert len(bundle["entries"])==7 and len(bundle["relations"])==6
assert all(e["kind"] in ("concept","definition") and e["proof_text"] is None for e in bundle["entries"])
inbox.mkdir(exist_ok=True)
if target.exists():
    if target.read_bytes()!=data:
        raise RuntimeError("Preserve existing inbox draft; it differs from this packet")
else:
    if part.exists():
        raise RuntimeError("Preserve pre-existing part file; inspect before reuse")
    part.write_bytes(data)
    part.rename(target)

reviews_path=Path(r"~\brain_workers\w488\REVIEWS.jsonl")
reviews=[json.loads(line) for line in reviews_path.read_text(encoding="utf-8").splitlines() if line.strip()]
keeps={r["claim"]:r for r in reviews if r.get("reviewer")=="w488" and r.get("verdict")=="KEEP" and r.get("claim","").startswith("S1.487.")}
receipt={"reviewer":"w488","source":str(reviews_path),"native_mathematical_keeps":list(keeps.values()),
         "author_served_model_evidence":"UNKNOWN","referee_served_model_evidence":"UNKNOWN",
         "different_model_gate_satisfied":False,"theorem_promotion_requested":False}
(folder/"REVIEW_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
rows=[json.loads(line) for line in (folder/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
for row in rows:
    if row["row_id"] in keeps:
        row["independent_reviewer"]="w488 (native mathematical KEEP receipt; served-model identity UNKNOWN)"
        row["review_status"]="native independent mathematical KEEP; identity gate unavailable"
        row["review_receipt"]="REVIEW_RECEIPT.json"
        row["remaining_gap"]={
          "S1.487.1":"No hopping in the counterexample; positive-disorder Anderson target is not refuted. Served-model promotion gate unavailable.",
          "S1.487.2":"The positive-disorder Anderson p>1 bound and nonzero spectral mass remain unproved; served-model promotion gate unavailable.",
          "S1.487.3":"Formula concerns the atomic model only; served-model promotion gate unavailable.",
          "S1.487.4":"Eta-uniform inverse bath-width moments and nonzero spectral mass remain unproved; served-model promotion gate unavailable.",
          "S1.487.5":"Zero-disorder periodic example does not refute the positive-disorder target; served-model promotion gate unavailable."
        }[row["row_id"]]
(folder/"CLAIMS.jsonl").write_text("".join(json.dumps(row,ensure_ascii=False)+"\n" for row in rows),encoding="utf-8")

status=json.loads((folder/"SOURCE_STATUS.json").read_text(encoding="utf-8"))
status["intake_source"]["hash_scope"]="SHA256 of decoded UTF-8 record line, with universal-newline normalization; not a whole-source or proof receipt"
status["recent_primary_claim"]["locator"]="Theorem labelled thm:main in 01-introduction.tex"
status["recent_primary_claim"]["introduction_file_sha256"]=hashlib.sha256((folder/"PUBLIC_INTRODUCTION.tex").read_bytes()).hexdigest()
stored=[json.loads(line) for line in (folder/"STORE_MATCHES.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
if stored:
    parent=stored[0]
    status["existing_parent_readonly"]={"id":parent["id"],"logical_id":json.loads(parent["metadata_json"])["logical_id"],
       "digest":parent["digest"],"matches_file":"STORE_MATCHES.jsonl","query_scope":"Target found before the 4-second progress cap interrupted further matching; no exhaustive store claim"}
status["native_referee_keeps"]=sorted(keeps)
(folder/"SOURCE_STATUS.json").write_text(json.dumps(status,indent=2)+"\n",encoding="utf-8")

count=sum(f"S1.487.{n}" in keeps for n in range(1,6))
pending=[f"S1.487.{n}" for n in range(1,6) if f"S1.487.{n}" not in keeps]
report=(folder/"REPORT.md").read_text(encoding="utf-8")
report=report.replace("Each result remains unreviewed pending w488.",
    f"w488 returned native independent mathematical KEEP for {count}/5 author results; remaining: {', '.join(pending) or 'none'}. Served-model proof gates remain unavailable.")
report=report.replace("the complete draft under math-brain-inbox/w487", "the complete draft at ~/math-brain-inbox/w487/bundle_001.json (review diff: patches/01_c0056_boundary_draft.diff)")
report=report.replace("NEXT: w488 independently checks S1.487.1-.5;", "NEXT: w488 checks any remaining claim listed in REVIEW_RECEIPT.json;")
(folder/"REPORT.md").write_text(report,encoding="utf-8")
packet=(folder/"REVIEW_PACKET.md").read_text(encoding="utf-8")
packet=packet.replace("Requested narrow decisions:",f"Native independent KEEP receipts already recorded for {count}/5 author results in REVIEW_RECEIPT.json. Review only outstanding claims ({', '.join(pending) or 'none'}); retain the numbered scopes below for the integrator:")
(folder/"REVIEW_PACKET.md").write_text(packet,encoding="utf-8")
delivery={"prepared":{"state":True,"entries":7,"relations":6,"concepts":6,"definitions":1,"theorems":0,"lemmas":0},
 "submitted":{"state":True,"path":str(target),"timestamp_utc":datetime.now(timezone.utc).isoformat(),"claim_id":"clm-5035c3ea22"},
 "reviewed":{"state":"native mathematical checks only","kept_rows":sorted(keeps),"pending_rows":pending,
             "identity_gate":"UNKNOWN / unsatisfied","receipt":"REVIEW_RECEIPT.json"},
 "ingested":{"state":"NOT_VERIFIED","worker_executed_integration":False},
 "retrievable":{"state":"NOT_PROBED","old_parent_readonly_match_is_not_new_card_retrieval":True},
 "hook":{"state":"prepared in worker folder only","path":"HOOK_PROPOSAL.jsonl","next":"hooks coordinator copies/audits proposal under its own write authority"}}
(folder/"DELIVERY_STATE.json").write_text(json.dumps(delivery,indent=2)+"\n",encoding="utf-8")
files=("ATTEMPT.md","CLAIMS.jsonl","SOURCE_STATUS.json","REVIEW_PACKET.md","REPORT.md","AUDIT_W486.json","MEASUREMENTS.json","REVIEW_RECEIPT.json","bundle_001.json")
checksums={name:hashlib.sha256((folder/name).read_bytes()).hexdigest() for name in files}
(folder/"REVIEW_CHECKSUMS.json").write_text(json.dumps({"scope":"byte checksums for review routing, not store sealing or mathematical proof","files":checksums},indent=2)+"\n",encoding="utf-8")
print(json.dumps({"submitted":str(target),"entries":7,"relations":6,"native_keeps":count,"pending":pending,
     "review_packet_sha256":checksums["REVIEW_PACKET.md"],"draft_file_sha256":checksums["bundle_001.json"],
     "ingested":"NOT_VERIFIED","retrievable":"NOT_PROBED"}))
