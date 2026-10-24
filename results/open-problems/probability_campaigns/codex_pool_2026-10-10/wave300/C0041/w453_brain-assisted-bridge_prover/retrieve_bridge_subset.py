"""Run the live retrieval function over only already-targeted RWRE cards."""
import json
import sys
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parent
sys.dont_write_bytecode=True
sys.path.insert(0,"~/math-brain-build/src")
from math_brain.retrieval import retrieve
from math_brain.store import ResearchStore

data=json.loads(ROOT.joinpath("math_cards.json").read_text(encoding="utf-8"))
ids=set()
for group in data["queries"]:
    if group["query"]=="regeneration_titles":
        ids.update(r["id"] for r in group["rows"])
    elif group["query"]=="candidate_id":
        ids.update(r["id"] for r in group["rows"] if r["metadata"].get("bundle_entry_key")=="op-c0041")
    elif group["query"]=="ballistic_titles":
        ids.update(r["id"] for r in group["rows"] if r["title"].startswith("Resolved: Equivalence"))
start=time.perf_counter()
with ResearchStore.open_read_only(data["store"]) as store:
    nodes=list(store.get_nodes(sorted(ids)).values())
result=retrieve("uniformly elliptic iid RWRE directional transience regeneration time finite expectation",nodes=nodes,edges=(),limit=4,min_support_score=0.0)
payload={"command":"python -B -X utf8 retrieve_bridge_subset.py","scope":"Live ranking function on four preselected target cards; no whole-store load, no edges. Not a full-store ranking benchmark.","elapsed_seconds":round(time.perf_counter()-start,6),"abstained":result.abstained,"reason":str(result.reason),"hits":[{"id":h.node.id,"title":h.node.title,"body":h.node.body,"conditions":h.node.metadata.get("conditions"),"logical_id":h.node.metadata.get("logical_id"),"source_id":h.node.metadata.get("source_id"),"proof_text":h.node.metadata.get("proof_text"),"truth_status":h.node.metadata.get("truth_status"),"score":h.total_score} for h in result.hits]}
ROOT.joinpath("bridge_retrieval.json").write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
print(json.dumps(payload))
