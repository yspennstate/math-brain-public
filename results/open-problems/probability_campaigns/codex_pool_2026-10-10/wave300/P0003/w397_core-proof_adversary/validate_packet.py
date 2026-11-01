"""Validate saved artifacts and scope labels, not the truth of P0003."""
import hashlib
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parent
required = ["STATUS.md", "SOURCE_STATUS.json", "ATTEMPT.md", "CLAIMS.jsonl", "REPORT.md",
            "INDEPENDENT.md", "REVIEW_w396_proof.md", "MEASUREMENTS.json",
            "SUBMISSION_RECEIPT.json", "review_packet/PACKET.json"]
assert all((root / name).is_file() for name in required)
claims = [json.loads(line) for line in (root / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line]
states = {"conjecture", "numerical evidence", "sketch", "proved special case", "independently checked proof"}
for row in claims:
    assert row["status"] in states
    assert all(k in row for k in ["statement", "assumptions", "source", "proof_or_counterexample", "independent_reviewer", "remaining_gap"])
assert len({r["id"] for r in claims}) == len(claims)

allowed = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
entries = []
relations_count = 0
for number in [1, 2]:
    local = root / ("DRAFT_BUNDLE_00" + str(number) + ".json")
    inbox = Path("~/math-brain-inbox/w397") / ("bundle_00" + str(number) + ".json")
    assert local.read_bytes() == inbox.read_bytes()
    bundle = json.loads(local.read_text(encoding="utf-8"))
    assert bundle["spec"] == "mathbrain-draft-v1" and bundle["author_agent"] == "w397"
    keys = {e["key"] for e in bundle["entries"]}
    assert len(keys) == len(bundle["entries"]) <= 200
    graph = {key: [] for key in keys}
    for e in bundle["entries"]:
        assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", e["logical_name"])
        assert re.fullmatch(r"[a-z]+(?:\.[a-z]+)+", e["namespace"])
        assert e["source"]["license"].startswith("owner-own-work")
        assert e["kind"] in {"definition", "lemma", "theorem", "concept"}
        if e["kind"] in {"definition", "concept"}:
            assert e["proof_text"] is None
        else:
            assert e["proof_text"]
            assert e["key"] == "face-obstruction" and "checked by w398" in e["statement"]
        entries.append(e)
    for relation in bundle["relations"]:
        assert relation["kind"] in allowed
        assert relation["from_key"] in keys and relation["to_key"] in keys
        if relation["kind"] == "depends_on":
            graph[relation["from_key"]].append(relation["to_key"])
    def visit(node, path):
        assert node not in path, "depends_on cycle"
        for child in graph[node]:
            visit(child, path | {node})
    for node in graph:
        visit(node, set())
    relations_count += len(bundle["relations"])

assert len(entries) == 9 and relations_count == 6
assert len({(e["namespace"], e["logical_name"]) for e in entries}) == len(entries)
source_status = json.loads((root / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
assert source_status["current_openness"] == "UNKNOWN"
assert "H_disk" in source_status["hardest_missing_input"]
assert source_status["landing_states"] == {"prepared": True, "submitted": True, "reviewed": False, "ingested": False, "retrievable": False}
assert source_status["formal_check_receipt"] is None
for receipt in source_status["sources"]:
    assert receipt["status"] == "downloaded"
    path = root / "sources" / (receipt["slug"] + ".pdf")
    assert hashlib.sha256(path.read_bytes()).hexdigest() == receipt["sha256"]
snapshot = json.loads((root / "review_packet/w396_snapshot_receipt.json").read_text(encoding="utf-8"))
assert hashlib.sha256(Path(snapshot["snapshot"]).read_bytes()).hexdigest() == snapshot["sha256"]
assert "VERDICT: KEEP" in (root / "review_packet/REVIEW_w397_by_w398.md").read_text(encoding="utf-8")
measurements = json.loads((root / "MEASUREMENTS.json").read_text(encoding="utf-8"))
assert measurements["all_passed"] and measurements["cases"] == 96 and measurements["zero_vertex_equations"] == 576
assert measurements["negative_controls_detected"] == 96
hook = json.loads((root / "hook_proposals/math-w397.jsonl").read_text(encoding="utf-8"))
assert len(hook["text"]) <= 300 and hook["fire_when"] and hook["silent_when"] and hook["evidence"]
result = {"worker": "w397", "validation": "saved artifact format, source versions, review scope and draft relation endpoints",
          "all_passed": True, "claims": len(claims), "draft_entries": len(entries),
          "draft_relations": relations_count, "checked_lemma_entries": 1,
          "remaining_draft_definition_concept_entries": 8,
          "P0003_proved": False, "ingested": False, "retrievable": False,
          "limits": "This format/source check is not a mathematical proof or formal-check receipt. Mathematical derivations and the w398 finite KEEP are separate artifacts."}
(root / "VALIDATION.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
