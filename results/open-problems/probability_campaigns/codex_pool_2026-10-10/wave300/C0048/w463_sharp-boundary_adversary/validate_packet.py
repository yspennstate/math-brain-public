"""Read-only local preflight of the draft and its proof/audit evidence."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parent
bundle = json.loads((root/"drafts/bundle_001.json").read_text(encoding="utf-8"))
assert bundle["spec"] == "mathbrain-draft-v1"
assert bundle["author_agent"] == "w463"
assert 0 < len(bundle["entries"]) <= 200
required = {"key", "namespace", "logical_name", "kind", "title", "statement", "proof_text", "assumptions", "domain", "source"}
keyed = {}
for entry in bundle["entries"]:
    assert required <= entry.keys()
    assert entry["key"] not in keyed
    keyed[entry["key"]] = entry
    assert entry["kind"] == "concept" and entry["proof_text"] is None
    assert "INDEPENDENT REVIEW PENDING" in entry["statement"]
    assert entry["assumptions"] and all(isinstance(a, str) and a for a in entry["assumptions"])
    assert entry["source"]["license"].startswith("owner-own-work")
    for field in ["source_id", "url", "revision", "license"]:
        assert isinstance(entry["source"][field], str) and entry["source"][field].strip()
allowed_relations = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
graph = {key: [] for key in keyed}
evidence = [json.loads(line) for line in (root/"RELATIONS_EVIDENCE.jsonl").read_text(encoding="utf-8").splitlines()]
assert len(evidence) == len(bundle["relations"])
for relation, record in zip(bundle["relations"], evidence):
    assert relation["kind"] in allowed_relations
    assert relation["from_key"] in keyed and relation["to_key"] in keyed
    assert record["from_statement_quote"] == keyed[relation["from_key"]]["statement"]
    assert record["to_statement_quote"] == keyed[relation["to_key"]]["statement"]
    if relation["kind"] == "depends_on":
        graph[relation["from_key"]].append(relation["to_key"])


def visit(key, active, done):
    assert key not in active, "dependency cycle"
    if key in done:
        return
    active.add(key)
    for other in graph[key]:
        visit(other, active, done)
    active.remove(key)
    done.add(key)


done = set()
for key in graph:
    visit(key, set(), done)
allowed_statuses = {"conjecture", "numerical evidence", "sketch", "proved special case", "independently checked proof"}
claims = [json.loads(line) for line in (root/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines()]
for claim in claims:
    assert claim["status"] in allowed_statuses
    for field in ["statement", "assumptions", "source", "proof_or_counterexample", "independent_reviewer", "remaining_gap"]:
        assert field in claim
audits = [json.loads(line) for line in (root/"PEER_AUDIT.jsonl").read_text(encoding="utf-8").splitlines()]
snapshot_hash = hashlib.sha256((root/"review/w462_ATTEMPT_reviewed.md").read_bytes()).hexdigest()
assert len(audits) == 3 and all(a["verdict"] == "KEEP" and a["source_sha256"] == snapshot_hash for a in audits)
assert json.loads((root/"SOURCE_STATUS.json").read_text(encoding="utf-8"))["current_openness"] == "UNKNOWN"
hook = json.loads((root/"hooks/c0048-w463.jsonl").read_text(encoding="utf-8"))
assert len(hook["text"]) <= 300 and hook["fire_when"] and hook["silent_when"] and hook["evidence"]
receipt = {"preflight": "PASS", "entries": len(keyed), "relations_with_exact_quoted_ends": len(evidence), "claims": len(claims), "scoped_peer_keeps": len(audits), "unreviewed_theorem_entries": 0, "dependency_acyclic": True, "hook_characters": len(hook["text"]), "live_integration_performed": False, "formal_proof_check_performed": False}
(root/"VALIDATION_RECEIPT.json").write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
print(json.dumps(receipt, indent=2))
