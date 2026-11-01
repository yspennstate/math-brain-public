"""Bounded exact-ID lookup; no store mutation or evaluation-bank access."""
import json
from pathlib import Path
import sqlite3
import time

ROOT = Path(__file__).resolve().parents[1]
path = Path("~/math-brain-build/local/population/brain.sqlite3")
start = time.monotonic()
con = sqlite3.connect(path.as_uri() + "?mode=ro", uri=True, timeout=2)
con.execute("PRAGMA query_only=ON")
con.row_factory = sqlite3.Row
columns = [row[1] for row in con.execute("PRAGMA table_info(nodes)")]
print("nodes columns:", json.dumps(columns))
allowed = [c for c in ("logical_name", "title", "namespace", "statement", "body", "metadata_json", "content_json", "payload_json", "node_json", "kind", "node_id", "id", "proof_text", "assumptions", "source_id", "source") if c in columns]
if not allowed:
    raise RuntimeError("No recognized node columns")
search = next((c for c in ("logical_name", "title") if c in columns), None)
if not search:
    raise RuntimeError("No recognized exact-lookup column")
terms = ["%Positive-temperature crystalline%", "%Convex Function and Its Subdifferential%", "%First-Order Characterization of Convexity%", "%brascamp%"]
rows = []
for term in terms:
    found = [dict(r) for r in con.execute(f'SELECT {",".join(allowed)} FROM nodes WHERE "{search}" LIKE ? LIMIT 8', (term,))]
    rows.append({"term": term, "rows": found})
con.close()
record = {"store": str(path), "read_only": True, "elapsed_s": time.monotonic()-start, "lookup_column": search, "results": rows}
(ROOT / "evidence" / "brain_cards.json").write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
for item in rows:
    print(json.dumps(item, ensure_ascii=False)[:11000])
print("elapsed_s:", record["elapsed_s"])
