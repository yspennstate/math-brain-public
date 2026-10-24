"""Validate the small review packet and update its source receipt."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent
def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))
def rows(name):
    return [json.loads(line) for line in (ROOT / name).read_text(encoding="utf-8").splitlines() if line.strip()]

claims = rows("CLAIMS.jsonl")
audits = rows("AUDIT_VERDICTS.jsonl")
edges = rows("EDGE_EVIDENCE.jsonl")
bundle = load("drafts/bundle_001.json")
source_status = load("SOURCE_STATUS.json")
measurement = load("MEASUREMENTS.json")
existing = load("EXISTING_TARGET_CARD.json")
assert len(claims) == 4 and len(audits) == 5
required_claim = {"exact_statement", "assumptions", "source", "proof_or_counterexample", "independent_reviewer", "remaining_gap", "status"}
assert all(required_claim <= row.keys() for row in claims)
assert all(row["status"] in {"conjecture","numerical evidence","sketch","proved special case","independently checked proof"} for row in claims)
assert all(row["verdict"] in {"KEEP","FIX","DROP"} for row in audits)
assert len(bundle["entries"]) == 3 and len(bundle["relations"]) == 3 and len(edges) == 3
required_entry = {"key","namespace","logical_name","kind","title","statement","proof_text","assumptions","domain","source"}
for entry in bundle["entries"]:
    assert required_entry <= entry.keys()
    assert entry["kind"] == "concept" and entry["proof_text"] is None
    assert entry["source"]["license"] == "owner-own-work"
    assert entry["statement"].startswith("Independent review pending.")
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", entry["logical_name"])
    assert not re.search(r"C:[/\\]|w43[0-9]|owner/", entry["statement"])
keys = {entry["key"] for entry in bundle["entries"]}
allowed_relations = {"depends_on","defines","proves","refutes","generalizes","specializes","analogous_to","cites","semantic_association"}
for rel, evidence in zip(bundle["relations"], edges):
    assert rel["kind"] in allowed_relations and rel["from_key"] in keys
    if "to_key" in rel:
        assert rel["to_key"] in keys
    else:
        assert rel["to_existing_logical"] == existing["logical_id"]
    assert evidence["from_card_quote"] and evidence["to_card_quote"] and evidence["relation"] == rel
assert bundle["relations"][2]["kind"] == "semantic_association"
assert all(rel.get("to_existing_logical") != existing["logical_id"] for rel in bundle["relations"] if rel["kind"] == "refutes")
assert measurement["failed_assertions"] == 0 and measurement["generations_checked"] == 4095
page = (ROOT / "sources/lyons_peres_pb_2026.page302.txt").read_text(encoding="utf-8")
assert re.search(r"Conjecture\s+8\.15", page) and "285" in page[:150]
assert "quasi-transitive" in page and "pc(G) < 1" in page
assert "sorry" in (ROOT / "sources/CriticalPercolation.lean").read_text(encoding="utf-8")
source_status["historical_primary"]["verification"] = "Verified directly in the 19 August 2026 paperback PDF, page 302 (printed page 285)."
source_status["historical_primary"]["local_page"] = "sources/lyons_peres_pb_2026.page302.txt"
source_status["source_input_receipts"] = rows("SOURCE_FETCHES.jsonl")
source_status["prior_local_work"]["recorded_p0043_method"] = "The existing attempt card records homogeneous regular-tree critical branching-process extinction; the current method uses an inhomogeneous dyadic offspring second moment and quenched energy noninheritance."
source_status["prior_local_work"]["core_lane_distinction"] = "w432/STATUS.md describes a critical-window uniform-integrability reduction and a distinct tree/derivative calculation. This packet uses the host-to-critical-component ray-energy obstruction."
source_status["existing_target_logical"] = existing["logical_id"]
assert source_status["current_openness"] == "UNKNOWN" and not source_status["formal_check"]["accepted_proof_receipt"]
(ROOT / "SOURCE_STATUS.json").write_text(json.dumps(source_status, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
hook = rows("HOOK_PROPOSAL.jsonl")[0]
assert {"id","area","event","cue","fire_when","silent_when","text","evidence","proposer"} <= hook.keys()
assert len(hook["text"]) <= 300
result = {
    "command": "python -X utf8 validate_packet.py",
    "claims": len(claims), "original_prover_audits": len(audits),
    "draft_nodes": len(bundle["entries"]), "draft_relations": len(edges),
    "historical_primary_locator_verified": True, "full_target_openness": "UNKNOWN",
    "theorem_promotions": 0, "formal_proof_receipts": 0,
    "hook_proposals_staged": 1, "validation": "PASS",
}
(ROOT / "PACKET_VALIDATION.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
progress = {
    "agent":"w436", "row":"S1.1.P0043",
    "event":"P0043: independent degree-9 critical-tree obstruction (pc=1/2, theta>=4/5), L1-L4 KEEP/G1 FIX audit, 4095-generation exact checks, three draft concepts and three relations prepared for review.",
    "evidence":str(ROOT / "REVIEW_PACKET.md"), "posting_state":"staged for reviewer under worker write-scope restriction",
}
(ROOT / "PROGRESS_EVENT.json").write_text(json.dumps(progress, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2), flush=True)
