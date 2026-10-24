"""Submit the already validated concept-only bundle to the explicitly authorized agent inbox."""
from datetime import datetime, timezone
import json
import os
from pathlib import Path

root=Path(__file__).resolve().parents[1]
validation=json.loads((root/"evidence/bundle_validation.json").read_text(encoding="utf-8"))
assert validation["passed"] and validation["concept_only"]
source=root/"draft_bundle/bundle_001.json"
payload=source.read_bytes()
bundle=json.loads(payload)
assert bundle["author_agent"]=="w537" and all(entry["kind"]=="concept" for entry in bundle["entries"])
base=Path("~/math-brain-inbox").resolve()
directory=(base/"w537").resolve()
assert directory.is_relative_to(base) and directory.name=="w537"
final=(directory/"bundle_001.json").resolve()
partial=(directory/"bundle_001.json.part").resolve()
assert final.parent==directory and partial.parent==directory
directory.mkdir(parents=True,exist_ok=True)
if final.exists():
    if final.read_bytes()!=payload:
        raise RuntimeError("Existing inbox bundle differs; refusing to overwrite")
else:
    with partial.open("xb") as handle:
        handle.write(payload)
        handle.flush()
        os.fsync(handle.fileno())
    os.rename(partial,final)
state=json.loads((root/"BUNDLE_STATUS.json").read_text(encoding="utf-8"))
state.update({"submitted":True,"submitted_at_utc":datetime.now(timezone.utc).isoformat(),"inbox_path":str(final),"reviewed":False,"review_state":"pending w539; adversary verdict reported but not yet registered","ingested":False,"retrievable":False})
(root/"BUNDLE_STATUS.json").write_text(json.dumps(state,indent=2),encoding="utf-8")
print(json.dumps(state))
