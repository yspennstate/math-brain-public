"""Observe ingestion without changing the live store."""
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).parent
bundle = json.loads((root / "bundle_001.json").read_text(encoding="utf-8"))
inbox = Path("~/math-brain-inbox/w371/bundle_001.json")
store = Path("~/math-brain-build/local/population/brain.sqlite3")
conn = sqlite3.connect(f"file:{store.as_posix()}?mode=ro", uri=True)
conn.execute("PRAGMA query_only=ON")
observed = {}
for entry in bundle["entries"]:
    hits = conn.execute("SELECT id FROM nodes WHERE title=?", (entry["title"],)).fetchall()
    observed[entry["key"]] = [row[0] for row in hits]
conn.close()
state = {
    "checked_at_utc": datetime.now(timezone.utc).isoformat(),
    "command": "python -X utf8 check_bundle_state.py",
    "submitted": inbox.is_file(),
    "reviewed_math": "w371 KEEP; w369 authored the quantile lemma",
    "independent_source_scope_audit": "requested from w374; pending",
    "ingested_observed": all(observed.values()),
    "direct_store_title_hits": observed,
    "retrievable_by_recall": "NOT TESTED; do not infer from a direct SQL hit",
}
(root / "BUNDLE_STATE.json").write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"submitted": state["submitted"], "ingested_observed": state["ingested_observed"], "hits": {k: len(v) for k, v in observed.items()}}))
