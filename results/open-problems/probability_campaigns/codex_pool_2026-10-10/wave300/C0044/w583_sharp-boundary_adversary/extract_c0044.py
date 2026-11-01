"""Read only exact C0044 rows from grep-selected prior work."""
from pathlib import Path
import json

base = Path(__file__).resolve().parent
root = Path("~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907")
records = []
for name in ("problems.jsonl", "attempts.jsonl"):
    with (root/name).open(encoding="utf-8") as stream:
        for number, line in enumerate(stream, 1):
            if "C0044" not in line:
                continue
            item = json.loads(line)
            if any(value == "C0044" for value in item.values() if isinstance(value, str)):
                records.append({"path": str(root/name), "line": number, "record": item})
for name in ("brain_bundle_C004.json", "brain_bundle_C004b.json", "brain_bundle_C007.json"):
    content = json.loads((root/name).read_text(encoding="utf-8"))
    for entry in content.get("entries", []):
        identity = " ".join(str(entry.get(k, "")) for k in ("key", "logical_name", "title"))
        if "c0044" in identity.lower():
            records.append({"path": str(root/name), "record": entry})
(base/"exact_c0044_prior_rows.json").write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(records, ensure_ascii=False, indent=2))
