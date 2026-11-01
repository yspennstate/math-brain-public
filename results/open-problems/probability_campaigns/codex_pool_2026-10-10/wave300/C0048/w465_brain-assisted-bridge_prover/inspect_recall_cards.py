"""Read only the five retrieved cards and a bounded Potts title shortlist."""
import json
from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parent
receipt = json.loads((ROOT/"evidence/math_recall_corrected.json").read_text(encoding="utf-8"))
decision = json.loads(receipt["stdout"])
hits = decision.get("hits",[])
summary={"abstained":decision.get("abstained"),"reason":decision.get("reason"),"hit_count":len(hits),"hits":hits,"elapsed_seconds":receipt["elapsed_seconds"],"exclusions_count":len(decision.get("exclusions",[]))}
(ROOT/"evidence/math_recall_summary.json").write_text(json.dumps(summary,indent=2)+"\n",encoding="utf-8")
print(json.dumps(summary,indent=2))
database=Path("~/math-brain-build/local/population/brain.sqlite3")
with sqlite3.connect(database.as_uri()+"?mode=ro",uri=True,timeout=10) as connection:
    connection.row_factory=sqlite3.Row
    selected=[]
    for hit in hits:
        identifier=hit.get("id",hit.get("node",{}).get("id"))
        if not identifier:
            continue
        row=connection.execute("SELECT id,kind,title,body,metadata_json FROM nodes WHERE id=?",(identifier,)).fetchone()
        if row:
            record=dict(row)
            record["metadata"]=json.loads(record.pop("metadata_json"))
            selected.append(record)
    shortlist=[dict(row) for row in connection.execute("SELECT id,kind,title FROM nodes WHERE lower(title) LIKE ? ORDER BY title LIMIT 14",("%potts%",))]
    result={"database":str(database),"open_mode":"ro","returned_cards":selected,"potts_title_shortlist":shortlist}
    (ROOT/"evidence/returned_cards.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    for record in selected:
        if "potts" in (record["title"]+record["body"]).lower():
            print(json.dumps(record,ensure_ascii=False,indent=2))
    print("BOUNDED POTTS TITLES: "+json.dumps(shortlist,ensure_ascii=False))
