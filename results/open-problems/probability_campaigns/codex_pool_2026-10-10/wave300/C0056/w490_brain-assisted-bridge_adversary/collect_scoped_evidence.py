"""Read only C0056 intake lines and Anderson-card metadata, never a store export."""
import json
from pathlib import Path
import sqlite3
import time

root = Path(__file__).resolve().parent
research = Path("~/<private-repo>/06_math_research")
receipt = {"target": "C0056", "source_rows": [], "store_mode": "read-only"}
for relative in [
    "probability_1000_intake_claude_20260907/problems.jsonl",
    "probability_1000_intake_claude_20260907/attempts.jsonl",
]:
    path = research / relative
    with path.open(encoding="utf-8-sig") as handle:
        for number, line in enumerate(handle, 1):
            if "C0056" in line:
                receipt["source_rows"].append({"path": str(path), "line": number, "record": json.loads(line)})
started = time.monotonic()
try:
    connection = sqlite3.connect(
        "file:~/math-brain-build/local/population/brain.sqlite3?mode=ro", uri=True, timeout=5,
    )
    receipt["store_schema"] = connection.execute(
        "SELECT name,sql FROM sqlite_master WHERE type=? AND (name LIKE ? OR name LIKE ? OR name LIKE ?)",
        ("table", "%node%", "%fts%", "%claim%"),
    ).fetchall()
    columns = [row[1] for row in connection.execute("PRAGMA table_info(nodes)")]
    receipt["node_columns"] = columns
    if "title" in columns:
        chosen = [name for name in ("id", "namespace", "logical_name", "kind", "title") if name in columns]
        query = "SELECT " + ",".join(chosen) + " FROM nodes WHERE lower(title) LIKE ? LIMIT 18"
        rows = connection.execute(query, ("%anderson%",)).fetchall()
        receipt["anderson_titles"] = [dict(zip(chosen, row)) for row in rows]
        selected = connection.execute(
            "SELECT id,kind,title,body,metadata_json FROM nodes WHERE kind=? AND (lower(title) LIKE ? OR lower(title) LIKE ? OR lower(title) LIKE ?) LIMIT 8",
            ("claim", "%anderson%", "%stieltjes%", "%spectral averaging%"),
        ).fetchall()
        receipt["selected_cards"] = [dict(zip(("id", "kind", "title", "body", "metadata_json"), row)) for row in selected]
    connection.close()
except Exception as error:
    receipt["store_error"] = repr(error)
receipt["store_elapsed_seconds"] = time.monotonic() - started
(root / "scoped_evidence.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(receipt, ensure_ascii=False)[:19000])
