"""Targeted node reads only; no full-store iteration or model loading."""
import json
import pathlib
import sqlite3
import time

root = pathlib.Path(__file__).resolve().parent
database = pathlib.Path("~/math-brain-build/local/population/brain.sqlite3")
started = time.perf_counter()
out = {"database": str(database), "read_only": True, "gate": "compute_gate.json", "queries": []}
if (root/"store_lookup_receipt.json").is_file() and not (root/"store_lookup_initial.json").exists():
    (root/"store_lookup_initial.json").write_text((root/"store_lookup_receipt.json").read_text(encoding="utf-8"), encoding="utf-8")
try:
    with sqlite3.connect(database.as_uri()+"?mode=ro", uri=True, timeout=1) as con:
        con.execute("PRAGMA query_only=ON")
        con.set_progress_handler(lambda: int(time.perf_counter()-started>3), 500)
        for term in ["hexatic", "Mermin", "Kosterlitz"]:
            rows = con.execute("SELECT id,kind,title,body,metadata_json FROM nodes WHERE title LIKE ? ORDER BY id LIMIT 4", ("%"+term+"%",)).fetchall()
            records = [dict(zip(["id","kind","title","body","metadata_json"], r)) for r in rows]
            out["queries"].append({"term": term, "rows": records})
            (root/"store_lookup_receipt.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
except sqlite3.Error as e:
    out["error"] = str(e)
out["seconds"] = time.perf_counter()-started
(root/"store_lookup_receipt.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
print(json.dumps(out))
