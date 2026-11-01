"""Validate and submit this worker's completed draft to its named inbox slot."""

import hashlib
import json
import os
from pathlib import Path

src = Path(__file__).with_name("bundle_001.json")
data = src.read_bytes()
bundle = json.loads(data)
assert bundle["spec"] == "mathbrain-draft-v1"
assert bundle["author_agent"] == "w413"
assert len(bundle["entries"]) <= 200
assert all(entry["proof_text"] for entry in bundle["entries"] if entry["kind"] in ("lemma", "theorem"))
assert all(entry["proof_text"] is None for entry in bundle["entries"] if entry["kind"] in ("concept", "definition"))

inbox = Path(r"~\math-brain-inbox")
target_dir = inbox / "w413"
assert os.path.commonpath((str(inbox.resolve()), str(target_dir.resolve()))) == str(inbox.resolve())
target_dir.mkdir(parents=True, exist_ok=True)
target = target_dir / "bundle_001.json"
part = target_dir / "bundle_001.part"
if target.exists():
    if target.read_bytes() != data:
        raise FileExistsError(f"Different submitted bundle exists: {target}")
else:
    with part.open("xb") as out:
        out.write(data)
        out.flush()
        os.fsync(out.fileno())
    os.replace(part, target)

assert target.read_bytes() == data
print(f"SUBMITTED {target} sha256={hashlib.sha256(data).hexdigest()}")
