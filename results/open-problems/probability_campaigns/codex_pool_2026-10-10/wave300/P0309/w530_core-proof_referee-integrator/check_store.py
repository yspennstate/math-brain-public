"""Read-only, narrow check of the target node and namespace before draft linking."""
import sqlite3

path = r"~\math-brain-build\local\population\brain.sqlite3"
con = sqlite3.connect("file:" + path + "?mode=ro", uri=True)
try:
    print("P0309 title hits:", con.execute(
        "SELECT id, title FROM nodes WHERE title LIKE ? LIMIT 5",
        ("%Positive-temperature crystalline Gibbs phases%",),
    ).fetchall())
    print("probability.core id sample:", con.execute(
        "SELECT id, title FROM nodes WHERE id LIKE ? LIMIT 3",
        ("math:probability.core:%",),
    ).fetchall())
    print("P0309 metadata:", con.execute(
        "SELECT substr(metadata_json,1,600) FROM nodes WHERE title=? LIMIT 1",
        ("Open problem: Positive-temperature crystalline Gibbs phases for three-dimensional Riesz gases",),
    ).fetchone())
finally:
    con.close()
