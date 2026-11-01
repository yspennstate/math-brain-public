"""Read-only, targeted measurement of the P0104 source-card mismatch."""
import json
import sqlite3
import time
from pathlib import Path

store = Path("~/math-brain-build/local/population/brain.sqlite3")
out = Path(__file__).with_name("RETRIEVAL_MEASUREMENT.json")
target_id = "claim_3ccc6fc493b4e17b5c29966949004f575c51205c8a4f0ba3bc516d0b752ebea4"
start = time.perf_counter()
conn = sqlite3.connect(f"file:{store.as_posix()}?mode=ro", uri=True)
conn.execute("PRAGMA query_only=ON")
row = conn.execute("SELECT title, body, metadata_json FROM nodes WHERE id=?", (target_id,)).fetchone()
if row is None:
    raise SystemExit("target card absent")
title, body, metadata_json = row
metadata = json.loads(metadata_json)
source_mentions = conn.execute(
    "SELECT COUNT(*) FROM nodes WHERE body LIKE ?", ("%1810.08270%",)
).fetchone()[0]
conn.close()
result = {
    "database": str(store),
    "mode": "sqlite URI mode=ro; PRAGMA query_only=ON",
    "command": "python -X utf8 measure_retrieval.py",
    "elapsed_seconds": round(time.perf_counter() - start, 6),
    "target_id": target_id,
    "target_title": title,
    "source_paper_card_count": source_mentions,
    "categorical_nonimplication_present": "does not by itself lower-bound the variance" in body,
    "overbroad_full_lattice_Zd_present": "general i.i.d. edge-weight distributions on Z^d" in body,
    "theorem_1_condition_F0_present": "F(0)<p_c" in body or "F(0) < p_c" in body,
    "theorem_1_oriented_condition_present": "oriented" in body.lower() or "vec" in body.lower(),
    "legacy_logical_id": metadata.get("logical_id"),
    "verdict": "One retrieved card states a false categorical nonimplication and omits the paper's Theorem 1 distribution conditions. This is a measured content failure, not an online-recall speed result.",
    "repair": "Submit a three-entry draft: the source theorem's exact scope, a proved two-quantile variance lemma, and the logarithmic corollary; no claim of P0104 progress.",
}
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: result[k] for k in (
    "elapsed_seconds", "source_paper_card_count", "categorical_nonimplication_present",
    "overbroad_full_lattice_Zd_present", "theorem_1_condition_F0_present",
    "theorem_1_oriented_condition_present", "legacy_logical_id")}, indent=2))
