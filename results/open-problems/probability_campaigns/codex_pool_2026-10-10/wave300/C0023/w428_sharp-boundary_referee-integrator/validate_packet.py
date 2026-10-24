"""Local shape checks only; does not touch the math-brain store."""
import json
from pathlib import Path

root = Path(r"~\brain_workers\w428")
source = json.loads((root / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
bundle = json.loads((root / "bundle_001.json").read_text(encoding="utf-8"))
inbox = json.loads(Path(r"~\math-brain-inbox\w428\bundle_001.json").read_text(encoding="utf-8"))
assert bundle == inbox
assert source["live_store_before"]["stale_nodes_found"] == 3
assert source["draft_bundle_states"]["reviewed_by_integrator"] == "pending"
assert len(bundle["entries"]) == 4 and len(bundle["relations"]) == 5

for name in ("CLAIMS.jsonl", "REVIEW_VERDICTS.jsonl", "hook_proposals.jsonl"):
    lines = (root / name).read_text(encoding="utf-8").splitlines()
    assert lines and all(json.loads(line) for line in lines)
    print(name, len(lines), "valid JSON rows")

hook = json.loads((root / "hook_proposals.jsonl").read_text(encoding="utf-8"))
assert hook["fire_when"] and hook["silent_when"] and len(hook["text"]) <= 300
patch = (root / "patches" / "01_source_status_hook.diff").read_text(encoding="utf-8")
assert "+" + (root / "hook_proposals.jsonl").read_text(encoding="utf-8").strip() in patch
status = (root / "STATUS.md").read_text(encoding="utf-8").splitlines()
assert status[0] in {"STATE: WORKING", "STATE: NEEDS_REVIEW"}
assert any(line.startswith("NEXT: ") for line in status)
print("bundle and hook shapes valid; inbox matches local draft")
