"""Read-only, bounded target and pressure probes; receipts stay in w517."""
from pathlib import Path
import datetime as dt
import json
import sqlite3
import time

ROOT = Path(__file__).resolve().parent
pressure_path = Path("~/.claude/compute/compute_state.json")
receipt = {"checked_utc": dt.datetime.now(dt.timezone.utc).isoformat(), "path": str(pressure_path)}
try:
    pressure = json.loads(pressure_path.read_text(encoding="utf-8-sig"))
    receipt["mtime_age_seconds"] = round(time.time()-pressure_path.stat().st_mtime, 3)
    # Do not print or examine any unrelated health/remote/trading observations.
    safe_keys = ("state", "mode", "level", "timestamp", "ts", "updated_at", "cpu_pct", "ram_pct", "commit_pct", "allow_heavy", "heavy_ok", "reasons", "pressure")
    receipt["pressure_fields"] = {k: pressure[k] for k in safe_keys if k in pressure}
except (OSError, ValueError) as exc:
    receipt["error"] = str(exc)
(ROOT/"GATE_PROBE.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
print("GATE", json.dumps(receipt))

store_path = Path("~/math-brain-build/local/population/brain.sqlite3")
out = {"path": str(store_path), "mode": "read-only", "tables": [], "matches": []}
connection = None
try:
    connection = sqlite3.connect(store_path.as_uri()+"?mode=ro", uri=True, timeout=3)
    started = time.monotonic()
    connection.set_progress_handler(lambda: int(time.monotonic()-started>8), 10000)
    tables = [r[0] for r in connection.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
    out["tables"] = tables
    candidates = [t for t in tables if t in ("cards", "claims", "claim_revisions", "entries", "nodes")]
    for table in candidates:
        qt = '"'+table.replace('"', '""')+'"'
        cols = [r[1] for r in connection.execute(f"PRAGMA table_info({qt})")]
        out.setdefault("schemas", {})[table] = cols
        search_cols = [c for c in cols if c in ("title", "logical_name", "statement")]
        if not search_cols:
            continue
        select_cols = [c for c in cols if c in ("id", "key", "logical_name", "title", "statement", "source_id", "status")]
        qcols = ','.join('"'+c+'"' for c in select_cols)
        terms = ("%P0297%", "%Liouville%quantum%dimension%", "%Liouville%dimension%", "%LFPP%")
        where = ' OR '.join(f'"{c}" LIKE ?' for c in search_cols for _ in terms)
        params = [term for _ in search_cols for term in terms]
        for values in connection.execute(f"SELECT {qcols} FROM {qt} WHERE {where} LIMIT 6", params):
            out["matches"].append({"table":table, **{c:(v[:800] if isinstance(v,str) else v) for c,v in zip(select_cols,values)}})
except (OSError, sqlite3.Error) as exc:
    out["error"] = str(exc)
finally:
    if connection is not None:
        connection.close()
(ROOT/"STORE_PROBE.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
print("STORE", json.dumps(out))
