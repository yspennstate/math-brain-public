"""Read only the named C0120 records from the explicitly supplied population store."""
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
database = Path("~/math-brain-build/local/population/brain.sqlite3")
uri = "file:" + database.as_posix() + "?mode=ro"
receipt = {"observed_at": datetime.now(timezone.utc).isoformat(), "database": str(database),
           "uri": uri, "readonly": True, "scope": "Exact C0120 problem and attempt ids/titles only; no full store scan/export"}
try:
    with sqlite3.connect(uri, uri=True, timeout=3) as connection:
        connection.row_factory = sqlite3.Row
        ids = ("claim_2b6b7c1da300a8ed1c28367cabd584f2c02769a03a64ed519cf081b1af04693d",
               "claim_7891e285a213a1ead9b1e54b02b29177a06d86c6f3df76b6447ca94dbe6add7f")
        titles = ("Open problem: Fluctuation exponent of directed polymers beyond the logarithmic improvement",
                  "Attempt on Fluctuation exponent of directed polymers beyond the logarithmic improvement")
        rows = connection.execute(
            "SELECT id,title,body,digest,metadata_json FROM nodes WHERE id IN (?,?) OR title IN (?,?) LIMIT 4",
            (*ids, *titles)).fetchall()
        receipt["records"] = [dict(row) for row in rows]
        receipt["matched_records"] = len(rows)
        receipt["finding"] = "Only these records were read; their historical/unverified status cannot establish current openness or novelty."
except (OSError, sqlite3.Error) as error:
    receipt["error"] = str(error)
    receipt["matched_records"] = None
    receipt["finding"] = "Direct store check unavailable; use the two scoped export records, keep openness UNKNOWN."
(ROOT / "STORE_READONLY_PROBE.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps({key: value for key, value in receipt.items() if key != "records"}, indent=2))
