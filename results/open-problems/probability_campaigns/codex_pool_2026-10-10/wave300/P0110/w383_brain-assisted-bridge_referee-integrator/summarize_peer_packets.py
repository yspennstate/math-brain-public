"""Read only bounded peer claims and draft entries named by this task."""
import json
from pathlib import Path

for worker, draft_dir in (("w381", "drafts"), ("w382", "draft_bundle")):
    root = Path("~/brain_workers") / worker
    print("WORKER", worker)
    for line in (root / "CLAIMS.jsonl").read_text(encoding="utf-8-sig").splitlines():
        row = json.loads(line)
        print("CLAIM", row.get("claim_id", row.get("id")), row.get("status"),
              row.get("review_state", row.get("audit_status")),
              (row.get("exact_statement") or row.get("statement") or "")[:240])
    draft = json.loads((root / draft_dir / "bundle_001.json").read_text(encoding="utf-8-sig"))
    for entry in draft["entries"]:
        print("ENTRY", entry["key"], entry["kind"], entry["logical_name"],
              entry["statement"][:170], entry["source"]["license"])
    for relation in draft["relations"]:
        print("EDGE", relation)
