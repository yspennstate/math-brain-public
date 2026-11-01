"""Use the already saved candidate headers to avoid another broad store scan."""
import json
import re
import sqlite3
import time
from pathlib import Path

root=Path(__file__).resolve().parent
headers=json.loads((root/"store_retrieval.json").read_text(encoding="utf-8"))["safe_source_headers"]
chosen=[x for x in headers if re.search(r"\bising\b|random currents?",x["title"],re.I)
        and re.search(r"scaling|trivial|gaussian|random currents?",x["title"],re.I)][:4]
t=time.perf_counter()
cards=[]
if chosen:
    p=Path("~/math-brain-build/local/population/brain.sqlite3")
    with sqlite3.connect(p.as_uri()+"?mode=ro",uri=True,timeout=5) as c:
        c.execute("PRAGMA query_only=ON")
        for x in chosen:
            body=c.execute("SELECT body FROM nodes WHERE id=?",(x["id"],)).fetchone()[0]
            cards.append({"id":x["id"],"title":x["title"],"body":body,"metadata":x["metadata"]})
out={"cards":cards,"access":"read-only; exact primary-key lookups; no full store load",
     "elapsed_seconds":time.perf_counter()-t,
     "limitations":"Chosen from one bounded 30-header sample; empty is not corpus absence."}
(root/"store_selected_cards.json").write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps({"cards":[{"id":x["id"],"title":x["title"],"body":x["body"],
  "conditions":x["metadata"].get("conditions"),"proof_text":x["metadata"].get("proof_text"),
  "source_id":x["metadata"].get("source_id"),"logical_id":x["metadata"].get("logical_id")}
  for x in cards],"elapsed_seconds":out["elapsed_seconds"]},ensure_ascii=False))
