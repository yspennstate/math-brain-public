"""Measure a two-edge repair in memory; never write the live SQLite store."""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, "~/math-brain-build/src")
from math_brain.models import EdgeKind, GraphEdge  # noqa: E402
from math_brain.retrieval import search  # noqa: E402
from math_brain.store import ResearchStore  # noqa: E402

root = Path(__file__).resolve().parent
db = Path("~/math-brain-build/local/population/brain.sqlite3")
cards = json.loads((root / "TARGET_CARDS.json").read_text(encoding="utf-8"))["cards"]
by_title = {c["title"]: c["id"] for c in cards}
target = next(c["id"] for c in cards if c["title"].startswith("Open problem: An iid FPP law"))
chatterjee = next(c["id"] for c in cards if c["title"].startswith("Chatterjee (2013)"))
auffinger = next(c["id"] for c in cards if c["title"].startswith("Auffinger-Damron (2014)"))

with ResearchStore.open_read_only(db) as store:
    nodes = tuple(store.iter_nodes())
    edges = tuple(store.iter_edges(skip_unknown=True))

added = (
    GraphEdge(source_id=target, target_id=chatterjee, kind=EdgeKind.SEMANTIC_ASSOCIATION,
              rationale="The conditional KPZ theorem specifies the strong exponent-existence premise for this open question."),
    GraphEdge(source_id=target, target_id=auffinger, kind=EdgeKind.SEMANTIC_ASSOCIATION,
              rationale="The 2014 conditional equality theorem removes the nearly-Gamma assumption but still requires matched exponents."),
)
queries = [
    "P0110 iid FPP law proved KPZ exponent relation",
    "Chatterjee 2013 KPZ relation hypotheses iid FPP chi xi exponent existence",
]
results = []
for query in queries:
    row = {"query": query}
    for label, edge_set in (("baseline", edges), ("two_link_simulation", edges + added)):
        start = time.perf_counter()
        hits = search(query, nodes=nodes, edges=edge_set, limit=10)
        row[label] = {"elapsed_seconds": round(time.perf_counter() - start, 3),
                      "chatterjee_rank": next((i + 1 for i, h in enumerate(hits) if h.node.id == chatterjee), None),
                      "auffinger_rank": next((i + 1 for i, h in enumerate(hits) if h.node.id == auffinger), None),
                      "top5_ids": [h.node.id for h in hits[:5]]}
    results.append(row)
receipt = {"read_only": True, "simulation_only": True, "node_count": len(nodes),
           "existing_edge_count": len(edges), "added_edges": [
               {"source_id": e.source_id, "target_id": e.target_id, "kind": e.kind.value,
                "rationale": e.rationale} for e in added], "results": results}
(root / "LINK_SIMULATION.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
print(json.dumps(receipt, indent=2))
