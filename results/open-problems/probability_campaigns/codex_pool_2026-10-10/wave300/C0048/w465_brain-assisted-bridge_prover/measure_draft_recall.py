"""Frozen, local candidate-pool pilot; never an ingestion or blind-bank evaluation."""
import json
from pathlib import Path
import sys
import time

sys.dont_write_bytecode=True
sys.path.insert(0,"~/math-brain-build/src")
from math_brain.models import GraphNode, GraphEdge, NodeKind, EdgeKind
from math_brain.retrieval import retrieve

ROOT=Path(__file__).resolve().parent
query="Potts nearest-neighbor discontinuity q 3 d 3 wired free critical"
frozen=json.loads((ROOT/"evidence/returned_cards.json").read_text(encoding="utf-8"))
bundle=json.loads((ROOT/"drafts/bundle_001.json").read_text(encoding="utf-8"))
base=[GraphNode(id=row["id"],kind=NodeKind(row["kind"]),title=row["title"],body=row["body"],metadata=row["metadata"],created_at="2026-10-10T00:00:00+00:00") for row in frozen["returned_cards"]]
drafts=[GraphNode(id="draft-w465:"+entry["key"],kind=NodeKind.CLAIM,title=entry["title"],body=entry["statement"],metadata={"claim_kind":"concept","truth_status":"unverified","conditions":entry["assumptions"],"proof_text":entry["proof_text"] or "","logical_id":"math:"+entry["namespace"]+":"+entry["logical_name"],"trust_class":"curated_secondary","draft_review_state":"unreviewed"},created_at="2026-10-10T00:00:00+00:00") for entry in bundle["entries"]]
edges=[]
for relation in bundle["relations"]:
    if relation.get("to_key") and relation["kind"] in {"depends_on","refutes"}:
        edges.append(GraphEdge(source_id="draft-w465:"+relation["from_key"],target_id="draft-w465:"+relation["to_key"],kind=EdgeKind(relation["kind"]),rationale=relation["rationale"]))
conditional_ids={"draft-w465:fk-edge-identity","draft-w465:fixed-cylinder-witness","draft-w465:pressure-bridge"}
started=time.perf_counter()
before=retrieve(query,nodes=base,edges=(),limit=5,min_support_score=0.0)
after=retrieve(query,nodes=base+drafts,edges=edges,limit=5,min_support_score=0.0)
def summarize(result):
    rows=[{"id":hit.node.id,"title":hit.node.title,"score":hit.total_score,"warning_score":hit.warning_score} for hit in result.hits]
    return {"hits":rows,"conditional_bridge_hits_at_5":sum(hit.node.id in conditional_ids for hit in result.hits),"abstained":result.abstained,"reason":result.reason}
result={"command":"python -X utf8 ~/brain_workers/w465/measure_draft_recall.py","query":query,"scope":"Frozen local pilot: the five previously returned live cards, then those same cards plus seven unreviewed draft entries. The existing retrieve() function and two local typed edges are used. This is not a full-store after-ingestion or blind evaluation measurement.","baseline_candidate_count":len(base),"after_candidate_count":len(base)+len(drafts),"before":summarize(before),"after":summarize(after),"elapsed_seconds":time.perf_counter()-started,"ranking_is_proof":False,"ingested":False,"retrievable_in_live_store":False,"drafts_admitted_as_theorems":False,"generalization_claim":False}
(ROOT/"evidence/draft_recall_pilot.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,ensure_ascii=False,indent=2))
