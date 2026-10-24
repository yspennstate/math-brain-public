"""Publish a complete new DRAFT under the acquired own-folder claim."""
from datetime import datetime, timezone
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
state = json.loads((ROOT / "SUBMISSION.json").read_text(encoding="utf-8"))
now = datetime.now(timezone.utc)
assert now < datetime.fromisoformat(state["claim_expires_at"].replace("Z", "+00:00")), "Reacquire expired inbox claim before submitting"
parent = Path("~/math-brain-inbox/w435").resolve()
assert str(parent).replace("\\", "/").lower() == "~/math-brain-inbox/w435"
parent.mkdir(parents=True, exist_ok=True)
destination = parent / "bundle_001.json"
part = parent / "bundle_001.part"
content = (ROOT / "draft_bundle_001.json").read_bytes()
if destination.exists():
    assert destination.read_bytes() == content, "Existing DRAFT differs; do not overwrite"
else:
    with part.open("xb") as stream:
        stream.write(content)
    part.rename(destination)
assert destination.read_bytes() == content
state["submitted"] = {"state": True, "at": now.isoformat(), "path": str(destination),
                       "claim_id": state["claim_id"], "entries": 8, "relations": 7}
for key in ("reviewed", "ingested", "retrievable"):
    state[key]["receipt_obtained"] = False
    state[key]["meaning"] = "not confirmed by this worker"
(ROOT / "SUBMISSION.json").write_text(json.dumps(state, indent=2)+"\n", encoding="utf-8")
print(json.dumps(state["submitted"]))
