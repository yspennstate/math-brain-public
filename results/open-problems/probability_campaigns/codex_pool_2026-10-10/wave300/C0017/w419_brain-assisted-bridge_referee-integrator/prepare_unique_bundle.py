"""Drop entries already submitted by peers; preserve the source-theorem bridge."""
import json
from pathlib import Path

here = Path(__file__).resolve().parent
bundle = json.loads((here / "bundle_001.json").read_text(encoding="utf-8"))
bundle["bundle_slug"] = "c0017-source-theorem-boundary-002"
bundle["entries"] = [entry for entry in bundle["entries"] if entry["key"] in {"c0017-target", "smirnov-q2", "fk-local-relation"}]
bundle["relations"] = [edge for edge in bundle["relations"] if edge["from_key"] in {"smirnov-q2", "fk-local-relation"}]
next(entry for entry in bundle["entries"] if entry["key"] == "smirnov-q2")["source"]["url"] = "https://arxiv.org/pdf/0708.0039"
(here / "bundle_002.json").write_text(json.dumps(bundle, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"entries": len(bundle["entries"]), "relations": len(bundle["relations"]), "output": str(here / "bundle_002.json")}))
