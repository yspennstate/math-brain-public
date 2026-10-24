"""Submit this worker's validated draft without touching the live math store."""

import json
import os
from pathlib import Path


source = Path(__file__).with_name("bundle_001.json")
target_dir = Path(r"~\math-brain-inbox\w533")
target_dir.mkdir(parents=True, exist_ok=True)
target = target_dir / "bundle_001.json"
part = target_dir / "bundle_001.json.part"
if target.exists() or part.exists():
    raise SystemExit("target or part already exists; refusing overwrite")
payload = source.read_bytes()
draft = json.loads(payload)
assert draft["spec"] == "mathbrain-draft-v1"
assert draft["author_agent"] == "w533"
with part.open("xb") as stream:
    stream.write(payload)
if json.loads(part.read_bytes()) != draft:
    raise SystemExit("draft content changed during copy")
os.replace(part, target)
print(f"SUBMITTED {target} entries={len(draft['entries'])} relations={len(draft['relations'])}")
