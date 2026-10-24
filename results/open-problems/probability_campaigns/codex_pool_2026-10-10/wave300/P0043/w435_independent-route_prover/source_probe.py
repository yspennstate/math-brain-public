"""Read only explicitly named mathematical sources; emit small targeted receipts."""
import json
from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parent
con = sqlite3.connect("file:~/math-brain-build/local/population/brain.sqlite3?mode=ro", uri=True, timeout=5)
tables = [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")]
print(json.dumps({"math_store_tables": tables}))
for table in ("nodes", "cards", "claims"):
    if table in tables:
        columns = [r[1] for r in con.execute('PRAGMA table_info("'+table+'")')]
        print(json.dumps({"table": table, "columns": columns}))
con.close()

base = Path("~/<private-repo>/06_math_research")
receipts = []
for name in ("probability_1000_attempts_H_20260912", "probability_1000_attempts_I_20260914",
             "probability_1000_intake_D_20260908", "probability_1000_intake_E_20260908",
             "probability_1000_intake_F_20260908", "probability_1000_intake_G_20260910",
             "probability_1000_intake_H_20260914", "probability_1000_intake_I_20260914"):
    # Only the top-level named intake ledgers, not whole corpora or logs.
    for filename in ("problems.jsonl", "attempts.jsonl"):
        file = base / name / filename
        if file.exists():
            hits = []
            with file.open(encoding="utf-8") as stream:
                for line_number, line in enumerate(stream, 1):
                    if 'P0043' in line or 'C0084' in line:
                        hits.append({"line": line_number, "row": json.loads(line)})
            receipts.append({"path": str(file), "hits": hits})
(ROOT / "LOCAL_SOURCE_RECEIPTS.json").write_text(json.dumps(receipts, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"targeted_ledgers_checked": len(receipts), "matching_rows": sum(len(r["hits"]) for r in receipts)}))
