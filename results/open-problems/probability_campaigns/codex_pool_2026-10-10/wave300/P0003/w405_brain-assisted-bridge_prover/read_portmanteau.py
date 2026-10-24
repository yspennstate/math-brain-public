import json,sqlite3
from pathlib import Path
root=Path(__file__).resolve().parent
con=sqlite3.connect("file:~/math-brain-build/local/population/brain.sqlite3?mode=ro",uri=True,timeout=5)
con.row_factory=sqlite3.Row
id="claim_fde5f7c46c3b42858fe57a153974903d"
node=con.execute("SELECT id,kind,title,body,metadata_json FROM nodes WHERE id=?",(id,)).fetchone()
claim=con.execute("SELECT payload_json FROM claims WHERE id=?",(id,)).fetchone()
out={"query":"exact node id cited by w406's mathematical audit","node":dict(node) if node else None,"claim":json.loads(claim[0]) if claim else None}
(root/"PORTMANTEAU_RECEIPT.json").write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(out,ensure_ascii=False))
for name in ["MEMORY_RECALL_RECEIPT.json","memory_recall_scores.json"]:
    p=root/name
    print(name,"exists=",p.exists())
    if name=="MEMORY_RECALL_RECEIPT.json" and p.exists():
        r=json.loads(p.read_text(encoding="utf-8"))
        print(json.dumps({k:v for k,v in r.items() if k!="stdout"}))
        print(r.get("stdout","")[-2500:])
con.close()
