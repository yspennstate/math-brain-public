import json
from pathlib import Path

root = Path(__file__).parent
source = json.loads((root / "bundle_001.json").read_text(encoding="utf-8"))
drop = "p0117-shell-union-obstruction"
source["bundle_slug"] = "p0117-source-and-edge-threshold-20261010-revised"
source["entries"] = [entry for entry in source["entries"] if entry["key"] != drop]
source["relations"] = [rel for rel in source["relations"] if rel["from_key"] != drop]
assert len(source["entries"]) == 2
assert len(source["relations"]) == 2
(root / "bundle_002.json").write_text(json.dumps(source, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
