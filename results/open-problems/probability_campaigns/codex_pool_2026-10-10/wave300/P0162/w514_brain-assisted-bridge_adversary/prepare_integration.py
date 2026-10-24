"""Local handoff identifiers only; no canonical digests, manifests or live writes."""
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def dump(name,obj):
    (ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

def main():
    model={"purpose":"Response-side served-model provenance for review gates",
           "author":{"agent":"w514","served_model":"UNKNOWN","response_side_evidence":None,
                     "requested_model":"gpt-6.1-sol","requested_reasoning":"max","requested_service_tier":"Fast",
                     "requested_settings_are_not_served_identity_evidence":True},
           "paired_author":{"agent":"w513","served_model":"UNKNOWN","response_side_evidence":None},
           "referee":{"agent":"w515","served_model":"UNKNOWN","response_side_evidence":None,"independent_receipt":"pending"},
           "available_evidence":"No provider response-side model field or signed response receipt is exposed in the available thread/artifacts. Neither requested settings, the agent label, nor turn_context proves served identity.",
           "different_model_review_gate":{"status":"NOT PASSED","reason":"Response-side author/referee identities unavailable; w515's final independent proof review pending"},
           "store_promotion_authorized":False,"parent_problem_solved":False}
    dump("MODEL_EVIDENCE.json",model)
    names=["REVIEW_PACKET.md","CLAIMS.jsonl","AUDIT_W513.jsonl","AUDIT_W513.md",
           "brain_bundle/bundle_001.json","NODE_CORRECTION.json","CORRECTION.md",
           "BENT_SELECTOR.md","SHARP_COORDINATE_BOUND.md","MODEL_EVIDENCE.json","packet_validation.json"]
    files=[]
    for name in names:
        path=ROOT/name
        data=path.read_bytes()
        files.append({"path":path.as_posix(),"bytes":len(data),"file_sha256":hashlib.sha256(data).hexdigest()})
    audits=[json.loads(row) for row in (ROOT/"AUDIT_W513.jsonl").read_text(encoding="utf-8").splitlines() if row.strip()]
    handoff={"target":"P0162","author_agent":"w514","integration_contact":"codex-01a12190","state":"NEEDS_REVIEW",
             "hash_scope":"Raw file SHA-256 identifiers for exact review bytes only. No canonical store digest, source manifest, release seal or proof certificate is produced.",
             "files":files,"scoped_KEEP":[{"claim_id":row["claim_id"],"scope":row["scope"],"verdict":row["verdict"]} for row in audits],
             "unresolved_gaps":["Dimension-free aggregate conditional-entropy budget for arbitrary Boolean functions; no solution of parent FEI",
                                "w515's independent check of sharpness limit and selector-sector premises",
                                "Claude mathematical check of the source-defined maximal-influence delta correction, routed via integration contact",
                                "Response-side served-model identities and different-model review gate are unavailable/not passed"],
             "bundle_state":{"prepared":True,"submitted":False,"reviewed":False,"ingested":False,"retrievable":False},
             "live_mathematical_changes":False,"parent_problem_solved":False,"model_evidence":"MODEL_EVIDENCE.json"}
    dump("INTEGRATION_HANDOFF.json",handoff)
    data=(ROOT/"INTEGRATION_HANDOFF.json").read_bytes()
    footprint=sum(path.stat().st_size for path in ROOT.rglob("*") if path.is_file())
    dump("INTEGRATION_ID.json",{"path":(ROOT/"INTEGRATION_HANDOFF.json").as_posix(),"file_sha256":hashlib.sha256(data).hexdigest(),
                                "worker_folder_bytes":footprint,"served_model_evidence":"UNKNOWN"})
    print(json.dumps({"handoff":(ROOT/"INTEGRATION_HANDOFF.json").as_posix(),"file_sha256":hashlib.sha256(data).hexdigest(),
                      "worker_folder_bytes":footprint,"files":len(files),"served_model_evidence":"UNKNOWN"}))

if __name__=="__main__":
    main()
