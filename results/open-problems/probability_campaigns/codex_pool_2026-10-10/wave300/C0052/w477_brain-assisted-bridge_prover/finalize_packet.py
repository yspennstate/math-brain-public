"""Record received audits and submit one authorized DRAFT. Never ingest."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parent
now=datetime.now(timezone.utc).isoformat()
measure=json.loads((ROOT/"MEASUREMENTS.json").read_text(encoding="utf-8"))
assert measure["static_packet_validation"] == "PASS"
audits = [
    {"reviewer":"w478","path":"~/brain_workers/w478/AUDIT_W477_L001.md","claims":["w477-L001"]},
    {"reviewer":"w478","path":"~/brain_workers/w478/AUDIT_W477_MAIN.md","claims":["w477-L002","w477-L003","w477-L007"]},
]
for audit in audits:
    text=Path(audit["path"]).read_text(encoding="utf-8")
    assert "KEEP" in text
    audit.update({"verdict":"KEEP","scope":"conditional reductions only; source-target ratio remains unproved",
                  "served_model_receipt":None,"different_model_gate":"not satisfied",
                  "report_sha256":hashlib.sha256(text.encode("utf-8")).hexdigest()})
(ROOT/"PEER_REVIEWS.json").write_text(json.dumps({"received_at":now,"audits":audits,
    "designated_referee":"w479","designated_referee_verdict":"pending",
    "parent_problem_proved":False},indent=2)+"\n",encoding="utf-8")

rows=[json.loads(line) for line in (ROOT/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
assert len(rows)==7 and len({row["id"] for row in rows})==7
for row in rows:
    for audit in audits:
        if row["id"] in audit["claims"]:
            row["independent_reviews"]=[{"reviewer":"w478","verdict":"KEEP","scope":"stated conditional claim only",
                                         "path":audit["path"],"different_model_gate":"pending"}]
            row["review_status"]="scoped peer KEEP; designated referee and model gate pending"
with (ROOT/"CLAIMS.jsonl").open("w",encoding="utf-8") as f:
    for row in rows:
        f.write(json.dumps(row,ensure_ascii=False)+"\n")

source=json.loads((ROOT/"SOURCE_STATUS.json").read_text(encoding="utf-8"))
source["primary_source"]["verified_by"]="direct primary PDF extracted text; page screenshot requested, visual receipt unavailable"
source["supporting_sources"][2]["verified_scope"]="abstract describes conformal-bootstrap extraction of a non-Gaussian four-point function; it is not accepted here as a verified lattice scaling-limit proof"
source["review_state"]="w478 scoped KEEP for L001/L002/L003/L007; w479 and different-model receipt gates pending; no promotion"
(ROOT/"SOURCE_STATUS.json").write_text(json.dumps(source,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

draft=(ROOT/"bundle_001.json").read_bytes()
inbox=Path("~/math-brain-inbox/w477")
inbox.mkdir(parents=True,exist_ok=True)
destination=None
for number in range(1,21):
    candidate=inbox/f"bundle_{number:03}.json"
    part=inbox/f"bundle_{number:03}.json.part"
    if candidate.exists():
        if candidate.read_bytes()==draft:
            destination=candidate
            break
        continue
    if part.exists():
        continue
    with part.open("xb") as f:
        f.write(draft)
        f.flush()
    part.rename(candidate)
    destination=candidate
    break
assert destination is not None, "no unoccupied DRAFT filename in own namespace"

lifecycle=json.loads((ROOT/"BUNDLE_LIFECYCLE.json").read_text(encoding="utf-8"))
lifecycle["submitted"]={"value":True,"path":str(destination),"at":now,"state":"DRAFT only"}
lifecycle["reviewed"]={"value":False,"state":"partial_scoped_peer_review",
                       "kept_claims":["w477-L001","w477-L002","w477-L003","w477-L007"],
                       "referee":"w479","model_gate":"pending"}
lifecycle["ingested"]={"value":None,"state":"not_confirmed","worker_invoked_integrator":False}
lifecycle["retrievable"]={"value":None,"state":"not_confirmed"}
lifecycle["promotion"]="HOLD until designated referee and model gate; exact-source ratio unproved"
(ROOT/"BUNDLE_LIFECYCLE.json").write_text(json.dumps(lifecycle,indent=2)+"\n",encoding="utf-8")

files=["ATTEMPT.md","GAP.md","CLAIMS.jsonl","SOURCE_STATUS.json","REVIEW_PACKET.md","REPORT.md",
       "MEASUREMENTS.json","PEER_REVIEWS.json","BUNDLE_LIFECYCLE.json","bundle_001.json",
       "targeted_math_id_lookup.py","patches/01_exact_math_id_lookup.diff","patches/02_ising_id_hook.diff"]
receipt={"at":now,"purpose":"local review-file integrity, not a store seal, release manifest, or proof certificate",
         "files":{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in files},
         "submitted_draft":str(destination),"integrator_run":False,"parent_proof":False}
(ROOT/"REVIEW_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"submitted_draft":str(destination),"entries":11,"relations":8,"claims":7,
                  "scoped_peer_keeps":4,"designated_review":"pending","ingestion":"not confirmed",
                  "mathematical_gap":"bounded susceptibility-current Q_beta along beta_j to beta_c"},indent=2))
