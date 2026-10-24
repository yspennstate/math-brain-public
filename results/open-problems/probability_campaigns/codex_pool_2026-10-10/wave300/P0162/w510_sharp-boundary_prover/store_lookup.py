"""A bounded target-only lookup, opening the named math store read-only."""
import json
from pathlib import Path
import sqlite3
import time

root=Path(__file__).resolve().parent
path="~/math-brain-build/local/population/brain.sqlite3"
out={"store":path,"mode":"ro","scope":"at most ten Fourier entropy/influence title matches per candidate table","matches":[]}
try:
    conn=sqlite3.connect("file:"+path+"?mode=ro",uri=True,timeout=2)
    started=time.monotonic()
    conn.set_progress_handler(lambda: int(time.monotonic()-started>6),10000)
    tables=[row[0] for row in conn.execute("SELECT name FROM sqlite_master WHERE type=?",("table",))]
    out["tables"]=tables
    for table in [t for t in tables if t in ("nodes","cards","entries","math_cards")]:
        cols=[row[1] for row in conn.execute("PRAGMA table_info("+table+")")]
        out[table+"_columns"]=cols
        if "title" not in cols:
            continue
        fields=[field for field in ("logical_name","kind","title","status","statement") if field in cols]
        projection=",".join("substr("+field+",1,650) AS "+field for field in fields)
        query="SELECT "+projection+" FROM "+table+" WHERE title LIKE ? OR title LIKE ? LIMIT 10"
        rows=conn.execute(query,("%Fourier%entropy%","%entropy%influence%")).fetchall()
        out["matches"].extend(dict(zip(fields,row),table=table) for row in rows)
    conn.close()
    out["state"]="lookup completed; scoped evidence only, not a full retired-status certification"
except Exception as exc:
    out["state"]="unavailable"
    out["error"]=type(exc).__name__+": "+str(exc)
(root/"STORE_LOOKUP.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out))
