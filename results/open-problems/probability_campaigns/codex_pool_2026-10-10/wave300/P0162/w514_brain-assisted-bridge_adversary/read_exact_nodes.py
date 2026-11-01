"""Read only the recall-cited math nodes, and named peer messages."""
import json
import sqlite3
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parent
DB="~/math-brain-build/local/population/brain.sqlite3"
IDS=["claim_0e83fe2812957c403bb6117944285bc0",
     "claim_d15d0160e58b4c9183707be9f49462d2",
     "claim_dc05672a84f74b44a1f15207c0cf86e0"]

def read_nodes():
    started=time.perf_counter()
    con=sqlite3.connect("file:"+DB+"?mode=ro",uri=True,timeout=5)
    con.execute("PRAGMA query_only=ON")
    rows=[]
    for identifier in IDS:
        node=con.execute("SELECT id,kind,title,body,metadata_json FROM nodes WHERE id=?",(identifier,)).fetchone()
        if node is None:
            rows.append({"id":identifier,"missing":True})
            continue
        claim=con.execute("SELECT payload_json FROM claims WHERE id=?",(identifier,)).fetchone()
        provenance=con.execute("SELECT evidence_class,source_kind,source_ref,artifact_path,status FROM claim_provenance WHERE claim_id=?",(identifier,)).fetchone()
        item=dict(zip(("id","kind","title","body","metadata_json"),node))
        item["metadata"]=json.loads(item.pop("metadata_json"))
        item["claim"]=json.loads(claim[0]) if claim else None
        item["provenance"]=dict(zip(("evidence_class","source_kind","source_ref","artifact_path","status"),provenance)) if provenance else None
        rows.append(item)
    con.close()
    receipt={"query_source":"recall_math.json","database":DB,"sqlite_mode":"ro","nodes":rows,"seconds":time.perf_counter()-started}
    (ROOT/"retrieved_exact_nodes.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
    for row in rows:
        print(json.dumps(row,ensure_ascii=False))

def mesh_schema():
    con=sqlite3.connect("file:~/.agents/coordination/agent_mesh.sqlite3?mode=ro",uri=True,timeout=3)
    print(json.dumps(con.execute("PRAGMA table_info(messages)").fetchall()))
    con.close()

if __name__ == "__main__":
    import sys
    mesh_schema() if len(sys.argv)>1 and sys.argv[1]=="mesh-schema" else read_nodes()
