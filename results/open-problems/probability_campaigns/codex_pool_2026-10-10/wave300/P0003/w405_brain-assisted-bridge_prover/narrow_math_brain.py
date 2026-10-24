import json, sqlite3, time
from pathlib import Path
root=Path(__file__).resolve().parent
con=sqlite3.connect("file:~/math-brain-build/local/population/brain.sqlite3?mode=ro",uri=True,timeout=5)
con.row_factory=sqlite3.Row
con.execute("PRAGMA query_only=ON")
queries=[
("p0003","SELECT id,kind,title,body,metadata_json FROM nodes WHERE lower(body) LIKE '%p0003%' OR lower(title) LIKE '%hexagonal self-avoiding%' LIMIT 3"),
("restriction","SELECT id,kind,title,body,metadata_json FROM nodes WHERE lower(title) LIKE '%restriction%' AND (lower(body) LIKE '%sle%' OR lower(body) LIKE '%chordal%') LIMIT 4"),
("critical_saw","SELECT id,kind,title,body,metadata_json FROM nodes WHERE lower(body) LIKE '%honeycomb%' AND (lower(body) LIKE '%connective%' OR lower(body) LIKE '%scaling%') LIMIT 3")]
out={"command":"python -B -X utf8 narrow_math_brain.py","mode":"targeted read-only SQL, not global recall performance","queries":[]}
for name,sql in queries:
    t=time.monotonic()
    rows=[dict(r) for r in con.execute(sql)]
    for row in rows:
        claim=con.execute("SELECT payload_json FROM claims WHERE id=?",(row["id"],)).fetchone()
        row["full_claim"]=json.loads(claim[0]) if claim else None
    out["queries"].append({"name":name,"sql":sql,"seconds":round(time.monotonic()-t,3),"count":len(rows),"rows":rows})
(root/"NARROW_MATH_BRAIN_RECEIPT.json").write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding="utf-8")
for q in out["queries"]:
    print(json.dumps(q,ensure_ascii=False))
con.close()
