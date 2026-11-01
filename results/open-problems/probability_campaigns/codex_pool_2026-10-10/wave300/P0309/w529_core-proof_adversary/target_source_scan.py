"""Find only the assigned target in the named intake files, not whole exports."""
import json
from pathlib import Path

root = Path("~/<private-repo>/06_math_research")
hits = []
for directory in sorted(root.glob("probability_1000_intake_*")):
    if not directory.is_dir():
        continue
    for name in ("problems.jsonl", "attempts.jsonl"):
        path = directory / name
        if not path.is_file():
            continue
        count = 0
        with path.open(encoding="utf-8-sig", errors="replace") as stream:
            for lineno, line in enumerate(stream, 1):
                low = line.lower()
                if "p0309" not in low and not ("riesz" in low and ("crystalline" in low or "crystallis" in low or "crystalliz" in low)):
                    continue
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    row = line.strip()
                hits.append({"path": str(path), "line": lineno, "row": row})
                count += 1
        print(json.dumps({"searched": str(path), "target_hits": count}))
dest = Path(__file__).resolve().parent / "RAW_TARGET_RECORDS.json"
dest.write_text(json.dumps(hits, ensure_ascii=False, indent=2), encoding="utf-8")
for hit in hits:
    print(json.dumps(hit, ensure_ascii=False))
