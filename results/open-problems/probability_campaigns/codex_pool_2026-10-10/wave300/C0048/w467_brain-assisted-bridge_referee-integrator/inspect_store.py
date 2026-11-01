"""Read-only, targeted C0048 card inspection; never modifies a store."""

import sqlite3
import sys

path = "~/math-brain-build/local/population/brain.sqlite3"
con = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
tables = con.execute(
    "SELECT name, sql FROM sqlite_master WHERE type='table' "
    "AND name NOT LIKE 'sqlite_%' LIMIT 30"
).fetchall()
if "--schema" in sys.argv:
    for name, definition in tables:
        print(name, definition[:900])

print("POTTS_TITLE_COUNT", con.execute(
    "SELECT count(*) FROM nodes WHERE lower(title) LIKE '%potts%'"
).fetchone()[0])
print("BISKUP_CHAYES_PAPER_COUNT", con.execute(
    "SELECT count(*) FROM nodes WHERE lower(title) LIKE '%rigorous analysis of discontinuous phase transitions%' "
    "OR lower(body) LIKE '%math/0207242%' OR lower(body) LIKE '%biskup and chayes%'"
).fetchone()[0])
problem_id = "claim_38c945c83e6d9f9dc77b20f936b660e811e528c284f76bd513990e6ed06ecc6a"
print("C0048_METADATA", con.execute(
    "SELECT metadata_json FROM nodes WHERE id=?", (problem_id,)
).fetchone()[0][:1200])
for row in con.execute(
    "SELECT e.kind, n.kind, n.title, substr(e.rationale,1,250) "
    "FROM edges e JOIN nodes n ON n.id = CASE WHEN e.source_id=? "
    "THEN e.target_id ELSE e.source_id END "
    "WHERE e.source_id=? OR e.target_id=?",
    (problem_id, problem_id, problem_id),
):
    print("C0048_EDGE", *row, sep=" | ")
