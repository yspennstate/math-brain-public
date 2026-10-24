"""Inspect one named returned theorem and its complete stored statement."""
import json
import sqlite3
from pathlib import Path

root=Path(__file__).resolve().parent
node_id="claim_5831cf989c54f4dda7ae7e7a4a5bc3fe030a5bc9b5591d47fdd117e4d6d50e0d"
p=Path("~/math-brain-build/local/population/brain.sqlite3")
with sqlite3.connect(p.as_uri()+"?mode=ro",uri=True,timeout=5) as c:
    c.execute("PRAGMA query_only=ON")
    c.row_factory=sqlite3.Row
    row=c.execute("SELECT id,title,body,metadata_json FROM nodes WHERE id=?",(node_id,)).fetchone()
    data=dict(row)
    data["metadata"]=json.loads(data.pop("metadata_json"))
(root/"RETRIEVED_THEOREM_REPORT.json").write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps({"id":data["id"],"title":data["title"],"body":data["body"],
    "conditions":data["metadata"].get("conditions"),
    "proof_text":data["metadata"].get("proof_text"),
    "truth_status":data["metadata"].get("truth_status"),
    "source_id":data["metadata"].get("source_id")},ensure_ascii=False))
