"""Bounded read-only lookup of source-relevant math-brain nodes."""
import json
import sqlite3
from pathlib import Path

store = Path("~/math-brain-build/local/population/brain.sqlite3")
with sqlite3.connect(store.as_uri() + "?mode=ro", uri=True, timeout=5) as conn:
    conn.execute("PRAGMA query_only=ON")
    conn.execute("PRAGMA busy_timeout=5000")
    results = {}
    for term in ("random current", "lebowitz", "three-dimensional ising", "renormalized coupling"):
        pattern = "%" + term + "%"
        results[term] = {
            "title_count": conn.execute("SELECT count(*) FROM nodes WHERE lower(title) LIKE ?", (pattern,)).fetchone()[0],
            "body_count": conn.execute("SELECT count(*) FROM nodes WHERE lower(body) LIKE ?", (pattern,)).fetchone()[0],
            "top_title_rows": conn.execute(
                "SELECT id,kind,title,substr(body,1,4000) FROM nodes "
                "WHERE lower(title) LIKE ? LIMIT 5", (pattern,)
            ).fetchall(),
        }
    results["target_metadata"] = conn.execute(
        "SELECT id,metadata_json FROM nodes WHERE id IN (?,?)",
        (
            "claim_db355f188daf0592950298d6e3b23e5f2b7e6eb0f3a21694083ad47fdadd0048",
            "claim_93dc043f691fa62549866c90e84e26aa836d69164fd798c69ba9c0dc431b1fc0",
        ),
    ).fetchall()
print(json.dumps(results, ensure_ascii=False))
