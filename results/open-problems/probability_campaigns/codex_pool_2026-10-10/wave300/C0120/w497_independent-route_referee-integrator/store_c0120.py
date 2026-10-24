"""Read only the C0120 matches in the local math-brain population store."""

import sqlite3
from pathlib import Path


path = Path("~/math-brain-build/local/population/brain.sqlite3")
connection = sqlite3.connect("file:" + path.as_posix() + "?mode=ro", uri=True, timeout=10)
queries = {
    "problem_nodes": ("SELECT id,kind,title,substr(body,1,1200),substr(metadata_json,1,800) FROM nodes WHERE title LIKE ? LIMIT 20", "%Fluctuation exponent of directed polymers%"),
    "problem_mentions": ("SELECT id,kind,title,substr(body,1,1200),substr(metadata_json,1,800) FROM nodes WHERE body LIKE ? LIMIT 20", "%open-problem-c0120%"),
    "claims": ("SELECT id,substr(payload_json,1,1600) FROM claims WHERE payload_json LIKE ? LIMIT 20", "%open-problem-c0120%"),
}
for label, (query, needle) in queries.items():
    rows = connection.execute(query, (needle,)).fetchall()
    print(label, len(rows))
    for row in rows:
        print(row)
