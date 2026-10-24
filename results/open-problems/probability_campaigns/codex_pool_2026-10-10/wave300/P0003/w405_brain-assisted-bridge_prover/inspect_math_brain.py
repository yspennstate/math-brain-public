import json, sqlite3
from pathlib import Path
root=Path(__file__).resolve().parent
db="file:~/math-brain-build/local/population/brain.sqlite3?mode=ro"
con=sqlite3.connect(db,uri=True,timeout=5)
con.row_factory=sqlite3.Row
con.execute("PRAGMA query_only=ON")
schema={r["name"]:r["sql"] for r in con.execute("SELECT name,sql FROM sqlite_master WHERE name IN ('nodes','claims','edges')")}
receipt={"database":db,"schema":schema,"queries":[]}
cols={r["name"] for r in con.execute("PRAGMA table_info(nodes)")}
if "title" in cols:
    sql="SELECT * FROM nodes WHERE lower(title) LIKE '%self-avoiding%' OR lower(title) LIKE '%restriction%' OR lower(title) LIKE '%hexagonal%' LIMIT 12"
else:
    sql="SELECT * FROM nodes WHERE payload_json LIKE '%P0003%' LIMIT 3"
try:
    rows=[dict(r) for r in con.execute(sql)]
    receipt["queries"].append({"sql":sql,"rows":rows,"count":len(rows)})
except sqlite3.Error as exc:
    receipt["error"]=str(exc)
(root/"MATH_BRAIN_RECEIPT.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(receipt,ensure_ascii=False)[:17000])
con.close()
