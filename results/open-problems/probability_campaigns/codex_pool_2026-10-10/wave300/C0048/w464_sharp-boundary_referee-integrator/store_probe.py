"""Targeted read-only check for existing Potts/math-brain cards."""

import json
import sqlite3

connection = sqlite3.connect(
    "file:~/math-brain-build/local/population/brain.sqlite3?mode=ro",
    uri=True,
)
rows = connection.execute(
    "SELECT id, kind, title, body, metadata_json FROM nodes "
    "WHERE title IN (?, ?)",
    (
        "Open problem: Discontinuity of the Potts phase transition on Z^d for q >= 3, d >= 3",
        "Attempt on Discontinuity of the Potts phase transition on Z^d for q >= 3, d >= 3",
    ),
).fetchall()
print(json.dumps({"exact_target_and_attempt_rows": rows}, indent=2))
