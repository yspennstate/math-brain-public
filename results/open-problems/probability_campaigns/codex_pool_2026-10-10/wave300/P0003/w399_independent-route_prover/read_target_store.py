"""Targeted reads from the population store; read-only URI, no export load."""
import json
from pathlib import Path
import sqlite3

root=Path(__file__).resolve().parent
path=Path("~/math-brain-build/local/population/brain.sqlite3")
conn=sqlite3.connect(path.as_uri()+"?mode=ro",uri=True,timeout=5)
conn.execute("PRAGMA query_only=ON")
rows=conn.execute("SELECT id,kind,title,body,metadata_json FROM nodes WHERE title LIKE ? OR title LIKE ? OR body LIKE ? LIMIT 6",("%self-avoiding%scaling%","%honeycomb%","%P0003%")).fetchall()
result=[]
for node_id,kind,title,body,metadata in rows:
    result.append({"id":node_id,"kind":kind,"title":title,"body":body,"metadata":json.loads(metadata)})
conn.close()
(root/"PRIOR_STORE_TARGET_ROWS.json").write_text(json.dumps({"source":str(path),"read_only":True,"limit":6,"rows":result},indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
for row in result:
    print(json.dumps(row,ensure_ascii=False))
