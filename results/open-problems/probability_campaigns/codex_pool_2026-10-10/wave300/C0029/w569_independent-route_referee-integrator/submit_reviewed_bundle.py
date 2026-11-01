"""Submit the already reviewed C0029 correction draft atomically to the inbox."""

import json
import os
from pathlib import Path


source = Path(__file__).with_name("bundle_001.json")
inbox = Path("~/math-brain-inbox/w569")
draft = inbox / "bundle_001.json"
part = inbox / "bundle_001.json.part"

data = source.read_bytes()
parsed = json.loads(data)
assert parsed["spec"] == "mathbrain-draft-v1"
assert parsed["author_agent"] == "w569"
assert len(parsed["entries"]) == 2
inbox.mkdir(parents=True, exist_ok=True)
if draft.exists() or part.exists():
    raise SystemExit("Bundle path already exists; choose a fresh number")
part.write_bytes(data)
os.replace(part, draft)
assert draft.read_bytes() == data
print(f"SUBMITTED {draft} entries={len(parsed['entries'])} relations={len(parsed['relations'])}")
