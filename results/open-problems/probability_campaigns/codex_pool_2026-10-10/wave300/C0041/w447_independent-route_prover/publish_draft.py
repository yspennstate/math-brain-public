"""Publish the claimed worker-specific DRAFT only; never run integration."""
import json
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parent
state_file = root / "SUBMISSION_STATE.json"
state = json.loads(state_file.read_text(encoding="utf-8"))
source = root / "drafts/bundle_001.json"
target = Path(state["bundle_submission_path"])
assert target.parent.as_posix() == "~/math-brain-inbox/w447"
data = source.read_bytes()
json.loads(data)
target.parent.mkdir(parents=True, exist_ok=True)
if target.exists():
    if target.read_bytes() != data:
        raise RuntimeError("existing worker DRAFT differs; do not overwrite")
else:
    part = target.with_suffix(".part")
    with part.open("xb") as f:
        f.write(data)
        f.flush()
    part.rename(target)
state["submitted"] = True
state["submitted_on"] = datetime.now(timezone.utc).isoformat()
state["reviewed"] = False
state["ingested"] = False
state["retrievable"] = False
state_file.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"draft_published": str(target), "entries": len(json.loads(data)["entries"]),
                  "reviewed": False, "ingested": False, "retrievable": False}, indent=2))
