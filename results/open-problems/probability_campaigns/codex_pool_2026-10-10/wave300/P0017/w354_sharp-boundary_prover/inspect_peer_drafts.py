import json
from pathlib import Path

base = Path(__file__).resolve().parent
rows = []
for peer in ("w355", "w356"):
    folder = Path("~/math-brain-inbox") / peer
    for file in sorted(folder.glob("bundle_*.json")):
        payload = json.loads(file.read_text(encoding="utf-8-sig"))
        for item in payload.get("entries", []):
            rows.append({"peer": peer, "file": str(file), "key": item["key"], "namespace": item["namespace"], "logical_name": item["logical_name"], "title": item["title"], "statement": item["statement"]})
(base / "PEER_DRAFT_BOUNDARIES.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")
for row in rows:
    print(json.dumps(row, ensure_ascii=False))
