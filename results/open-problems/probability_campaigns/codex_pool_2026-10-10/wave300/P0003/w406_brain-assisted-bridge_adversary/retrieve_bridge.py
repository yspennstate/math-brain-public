"""A narrow read-only math-brain retrieval; no corpus export or model load."""
import json
import pathlib
import sqlite3
import sys
import time

sys.dont_write_bytecode=True
ROOT=pathlib.Path(__file__).resolve().parent
sys.path.insert(0,"~/math-brain-build/src")
from math_brain.models import GraphNode, NodeKind
from math_brain.retrieval import search, RetrievalMode

path=pathlib.Path("~/math-brain-build/local/population/brain.sqlite3")
con=sqlite3.connect(path.as_uri()+"?mode=ro",uri=True,timeout=5)
con.row_factory=sqlite3.Row
con.execute("PRAGMA query_only=ON")
start=time.perf_counter()
terms=["self-avoiding","self avoiding","honeycomb","parafermion","conformal restriction","portmanteau"]
conditions=" OR ".join("lower(title) LIKE ?" for _ in terms)
rows=con.execute("SELECT id,kind,title,body,metadata_json FROM nodes WHERE ("+conditions+") AND lower(metadata_json) NOT LIKE '%test%' AND lower(metadata_json) NOT LIKE '%answer%' AND lower(metadata_json) NOT LIKE '%challenge%' AND lower(metadata_json) NOT LIKE '%benchmark%' AND lower(title) NOT LIKE '%test%' AND lower(title) NOT LIKE '%answer%' LIMIT 80",["%"+term+"%" for term in terms]).fetchall()
nodes=[]
for row in rows:
    try: kind=NodeKind(row["kind"])
    except ValueError: continue
    nodes.append(GraphNode(id=row["id"],kind=kind,title=row["title"],body=row["body"],metadata=json.loads(row["metadata_json"])))
queries=["honeycomb self-avoiding walk parafermionic observable scaling limit missing holomorphicity","Portmanteau weak convergence closed obstacle avoidance positive buffer"]
retrievals=[]
for query in queries:
    hits=search(query,nodes=nodes,edges=[],limit=5,graph_depth=0,mode=RetrievalMode.DISCOVERY)
    retrievals.append({"query":query,"hits":[{"id":h.node.id,"kind":h.node.kind.value,"title":h.node.title,"body":h.node.body,"metadata":h.node.metadata,"total_score":h.total_score,"support_score":h.support_score} for h in hits]})
data={"command":"python -X utf8 -B retrieve_bridge.py","store":str(path),"store_mode":"read-only","candidate_scope":"title-matched mathematical cards only; test/answer/challenge/benchmark metadata excluded; no graph expansion or embeddings","candidate_count":len(nodes),"retrievals":retrievals,"elapsed_seconds":time.perf_counter()-start}
(ROOT/"bridge_retrieval.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"candidate_count":len(nodes),"elapsed_seconds":data["elapsed_seconds"],"retrievals":retrievals},ensure_ascii=False))
