"""Finish the explicitly requested proposal and local handoff receipts."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path

ROOT=Path(__file__).resolve().parent
manifest=json.loads((ROOT/"REVIEW_MANIFEST.json").read_text(encoding="utf-8"))
for row in manifest["files"]:
    assert hashlib.sha256(Path(row["path"]).read_bytes()).hexdigest()==row["sha256"]
manifest_hash=hashlib.sha256((ROOT/"REVIEW_MANIFEST.json").read_bytes()).hexdigest()
assert manifest_hash=="df5c2b84c6b28e917f129ef16b1accbed6bf1c1c8d7fda6c032999cccc4decb8"
line=(ROOT/"hook_proposal.jsonl").read_text(encoding="utf-8")
hook=json.loads(line)
assert len(hook["text"])<=300
proposal=Path("~/primary_directive/hooks1000/proposals/math-w501.jsonl")
assert proposal.parent.is_dir()
existing=proposal.read_text(encoding="utf-8") if proposal.exists() else ""
already_present=any(json.loads(row).get("id")==hook["id"] for row in existing.splitlines() if row.strip())
if not already_present:
    with proposal.open("a",encoding="utf-8") as stream:
        stream.write(line)
        stream.flush()
        os.fsync(stream.fileno())
receipts={"as_of":datetime.now(timezone.utc).isoformat(),"statement_first":{"to":"w502","message_id":"msg-35a67c6b7b","inserted":True},
          "referee":{"to":"w503","message_id":"msg-49b17afbe8","inserted":True,"requires_ack":True,"acknowledgement":"not yet verified"},
          "integration":{"to":"codex-01a12190","message_id":"msg-0e24ec5b4a","inserted":True},
          "review_manifest_sha256":manifest_hash,"all_review_artifact_hashes_match":True,
          "hook":{"path":str(proposal),"id":hook["id"],"submitted":True,"already_present":already_present,"reviewed":False},
          "parent_problem_solved":False,"live_store_written":False}
(ROOT/"HANDOFF_RECEIPTS.json").write_text(json.dumps(receipts,indent=2)+"\n",encoding="utf-8")
print(json.dumps(receipts))
