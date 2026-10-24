import json
from pathlib import Path
import sqlite3
import time

ROOT = Path(__file__).resolve().parent
rows = json.loads((ROOT/"retrieved_cards.json").read_text(encoding="utf-8"))
titles = {"Hypercontractivity", "Open problem: Fluctuation exponent of directed polymers beyond the logarithmic improvement",
          "The Ornstein-Uhlenbeck Semigroup and Mehler's Formula", "Talagrand's L1-L2 Variance Inequality (the Engine Behind Sublinear Variance)"}
selected = [r for r in rows if r.get("title") in titles]
(ROOT/"selected_export_cards.json").write_text(json.dumps(selected,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
started = time.monotonic()
con = sqlite3.connect("file:~/math-brain-build/local/population/brain.sqlite3?mode=ro",uri=True,timeout=2)
con.execute("PRAGMA query_only=ON")
con.set_progress_handler(lambda: int(time.monotonic()-started>15), 10000)
current = []
try:
    for row in selected:
        result = con.execute("SELECT n.id,n.title,n.body,n.metadata_json,c.payload_json,n.digest FROM nodes n LEFT JOIN claims c ON c.id=n.id WHERE n.id=?",(row["id"],)).fetchone()
        if result:
            keys = ["id","title","body","metadata_json","payload_json","digest"]
            current.append(dict(zip(keys,result)))
    receipt = {"read_mode":"ro","elapsed_seconds":time.monotonic()-started,"returned":len(current),"raw_lookup_not_served_retrieval":True,"cards":current}
except sqlite3.OperationalError as exc:
    receipt = {"read_mode":"ro","elapsed_seconds":time.monotonic()-started,"returned":len(current),"error":str(exc),"cards":current}
finally:
    con.close()
(ROOT/"selected_live_cards.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in receipt.items() if k!="cards"}))
print(json.dumps(selected,ensure_ascii=False))
