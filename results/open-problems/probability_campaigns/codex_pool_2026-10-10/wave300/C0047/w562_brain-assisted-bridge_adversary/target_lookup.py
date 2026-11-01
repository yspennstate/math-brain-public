"""A proposed bounded fallback, only for the C0047 target, never writes the store."""
import json
import pathlib
import sqlite3
import time

root=pathlib.Path(__file__).resolve().parent
db=pathlib.Path("~/math-brain-build/local/population/brain.sqlite3")
start=time.perf_counter()
with sqlite3.connect(db.as_uri()+"?mode=ro",uri=True,timeout=1) as con:
    con.row_factory=sqlite3.Row
    con.execute("PRAGMA query_only=ON")
    con.set_progress_handler(lambda: int(time.perf_counter()-start>2),1000)
    title="Attempt on Benjamini-Schramm conjecture: p_c < p_u if and only if the group is non-amenable"
    rows=[dict(r) for r in con.execute("SELECT id,title,body,metadata_json,digest FROM nodes WHERE id=? OR title=? LIMIT 3",("claim_0bfe0a8a0e527dd20457f2c0393cb560907546ec53a1204204de0fc82235d788",title))]
elapsed=time.perf_counter()-start
for row in rows:
    row["metadata"]=json.loads(row.pop("metadata_json"))
record={"database":str(db),"mode":"ro","query_only":True,"budget_seconds":2,"elapsed_seconds":elapsed,"returned_cards":len(rows),"rows":rows}
(root/"target_cards.json").write_text(json.dumps(record,indent=2,ensure_ascii=False),encoding="utf-8")
print(json.dumps(record,indent=2,ensure_ascii=False))
