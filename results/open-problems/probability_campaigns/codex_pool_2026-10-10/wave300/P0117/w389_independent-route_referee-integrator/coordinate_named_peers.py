"""Use the existing mesh helper for named peers; registration does not start agents."""
import importlib.util
import json
import os
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
HELPER = Path(r"~/<private-repo>/12_cognitive_architecture/agent_mesh/team_comm.py")
sys.path.insert(0, str(HELPER.parent))
spec = importlib.util.spec_from_file_location("w389_existing_team_comm", HELPER)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
mesh = module.mesh()
module.ensure(mesh, "w389")
requests = [
    ("w392", "probability:P0117/audit-own-claim",
     "Audit requested: C02 stationary boundary-geodesic occupation identity and C03 shell lower bound in ~/brain_workers/w389/ATTEMPT.md. Exact boundary: AUDIT_REQUEST.md; draft nodes and evidence-backed relations: drafts/bundle_001.json and RELATIONS_EVIDENCE.jsonl. Return KEEP/FIX/DROP in your own folder. No iid decay estimate, parent solution, or novelty claim. Reply with receipt path.", "request"),
    ("w387", "probability:P0117/referee-claim",
     "w389 referee: source statement recovered in SOURCE_STATUS.json; recent public claimed proof keeps openness UNKNOWN. w388 compactness reduction C02 is already independently kept. w388 shell-decay goal C03 is impossible: a forward ray crosses every shell, so its raw expected shell count is >=1. Audits and exact fix: REVIEWS.jsonl. My disjoint density identity is ATTEMPT.md C02; please focus any next proof on an attainable two-sided/annular obstruction and send narrow claim path.", "message"),
]
receipts = []
for peer, topic, body, kind in requests:
    peer_directory = Path(r"~/brain_workers") / peer
    if not peer_directory.is_dir():
        raise RuntimeError("Named peer folder is missing: " + peer)
    # The official helper registers a parked recipient using cwd as metadata.
    # Use that recipient's existing folder for the metadata only. No process is
    # spawned and all local artifact writes remain under ROOT.
    previous = Path.cwd()
    try:
        os.chdir(peer_directory)
        module.ensure(mesh, peer)
    finally:
        os.chdir(previous)
    result = mesh.send("w389", peer, topic, body, kind=kind)
    receipts.append({"to": peer, "topic": topic, "kind": kind, "receipt": result,
                     "registration_only": True, "process_started": False})
(ROOT / "mesh_requests.json").write_text(json.dumps(receipts, indent=2, default=str) + "\n", encoding="utf-8")
print(json.dumps(receipts, default=str))
