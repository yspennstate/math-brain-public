"""Extract exact C0056 rows; never print or copy whole stores."""
import hashlib
import json
from pathlib import Path

root = Path(r"~\<private-repo>\06_math_research\probability_1000_intake_claude_20260907")
out = Path(__file__).resolve().parent
rows = []
for name in ("problems.jsonl", "attempts.jsonl"):
    path = root / name
    with path.open(encoding="utf-8") as stream:
        for line_no, line in enumerate(stream, 1):
            if "C0056" in line:
                record = json.loads(line)
                row = {"path": str(path), "line": line_no,
                       "record_sha256": hashlib.sha256(line.encode()).hexdigest(), "record": record}
                rows.append(row)
                print(json.dumps(row, ensure_ascii=False))
for name in ("brain_bundle_C004.json", "brain_bundle_C004a.json", "brain_bundle_C004b.json"):
    path = root / name
    data = json.loads(path.read_text(encoding="utf-8"))
    for item in data.get("entries", []):
        if "C0056" in json.dumps(item):
            row = {"path": str(path), "record": item}
            rows.append(row)
            print(json.dumps(row, ensure_ascii=False))
(out / "SOURCE_ROWS.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False)+"\n" for r in rows), encoding="utf-8")
print("EXACT_TARGET_ROWS", len(rows))
