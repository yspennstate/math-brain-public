"""Extract only the C0017/source records and matching exported cards."""
import json
from pathlib import Path

root = Path("~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907")
for name, field, wanted in (("problems.jsonl", "problem_id", "C0017"), ("attempts.jsonl", "problem_id", "C0017"), ("sources.jsonl", "source_id", "garban_steif_noise_2012")):
    with (root / name).open(encoding="utf-8") as f:
        for number, line in enumerate(f, 1):
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if row.get(field) == wanted:
                print(name, number, json.dumps(row, ensure_ascii=False), flush=True)
print("SOURCE_CACHE_FILENAMES", flush=True)
for p in root.rglob("*garban*"):
    if p.is_file():
        print(p, p.stat().st_size, flush=True)
export = Path("~/math-brain-build/export/population/nodes.jsonl")
matches = 0
with export.open(encoding="utf-8") as f:
    for number, line in enumerate(f, 1):
        lower = line.lower()
        if "percol" not in lower or "conformal" not in lower:
            continue
        row = json.loads(line)
        body = str(row.get("statement", "")) + str(row.get("logical_name", "")) + str(row.get("title", "")) + str(row.get("content", ""))
        if "square" not in body.lower() and "c0017" not in lower and "z^2" not in body.lower():
            continue
        print("CARD", number, json.dumps(row, ensure_ascii=False)[:7500], flush=True)
        matches += 1
        if matches == 5:
            break
print("MATCHED_CARD_COUNT", matches, flush=True)
