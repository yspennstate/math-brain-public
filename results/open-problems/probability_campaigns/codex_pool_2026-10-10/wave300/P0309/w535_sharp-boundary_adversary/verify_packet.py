"""Small static checkpoint validation; this is not a mathematical proof checker."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def read_json(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8-sig"))


def verify():
    prior = read_json("P0309_SOURCE_EXTRACT.json")
    delivery = read_json("BRAIN_DELIVERY.json")
    bundle = read_json(delivery["active_local_bundle"])
    source_status = read_json("SOURCE_STATUS.json")
    receipt = read_json("PAIRED_PROOF_RECEIPT.json")
    assert source_status["current_openness"] == "UNKNOWN"
    assert source_status["exact_intake_recovered"] is True
    assert bundle["spec"] == "mathbrain-draft-v1"
    assert bundle["author_agent"] == "w535"
    assert 0 < len(bundle["entries"]) <= 200
    fields = {
        "key", "namespace", "logical_name", "kind", "title", "statement",
        "proof_text", "assumptions", "domain", "source",
    }
    entries = {entry["key"]: entry for entry in bundle["entries"]}
    assert len(entries) == len(bundle["entries"])
    for entry in entries.values():
        assert fields <= entry.keys()
        assert entry["kind"] in {"concept", "definition", "lemma"}
        if entry["kind"] == "lemma":
            assert isinstance(entry["proof_text"], str) and len(entry["proof_text"]) > 100
        else:
            assert entry["proof_text"] is None
        assert entry["source"]["license"].startswith("owner-own-work")
        if entry["kind"] == "concept":
            assert "Refuted auxiliary" in entry["statement"]
    void = entries["void-bound"]["statement"]
    assert "without independence" in void
    assert "s>3" in void and "renormalized s<=3" in void
    assert "does not rule out lattice-periodic probability laws" in void
    existing = {row["metadata"]["logical_id"] for row in prior["rows"]}
    allowed = {
        "depends_on", "defines", "proves", "refutes", "generalizes",
        "specializes", "analogous_to", "cites", "semantic_association",
    }
    dependencies = {key: [] for key in entries}
    for relation in bundle["relations"]:
        assert relation["from_key"] in entries
        assert relation["kind"] in allowed
        if "to_key" in relation:
            assert relation["to_key"] in entries
            if relation["kind"] == "depends_on":
                dependencies[relation["from_key"]].append(relation["to_key"])
        else:
            assert relation["to_existing_logical"] in existing
            # The original target and prior attempt are not claimed proved/refuted.
            assert relation["kind"] in {"analogous_to", "semantic_association"}

    def visit(key, active):
        assert key not in active, "dependency cycle"
        for child in dependencies[key]:
            visit(child, active | {key})

    for key in entries:
        visit(key, set())
    evidence = [json.loads(line) for line in (ROOT / "RELATION_EVIDENCE.jsonl").read_text(encoding="utf-8").splitlines()]
    assert len(evidence) == len(bundle["relations"])
    for relation, support in zip(bundle["relations"], evidence):
        assert all(support[key] == value for key, value in relation.items())
        assert support["from_quote"] == entries[relation["from_key"]]["statement"]
        if "to_key" in relation:
            assert support["to_quote"] == entries[relation["to_key"]]["statement"]
        else:
            assert support["to_quote"] == next(row["body"] for row in prior["rows"] if row["metadata"]["logical_id"] == relation["to_existing_logical"])
    published = Path(delivery["submitted"]["path"])
    assert published.parent == Path(r"~/math-brain-inbox/w535")
    assert json.loads(published.read_text(encoding="utf-8")) == bundle
    assert delivery["reviewed"]["state"] is True
    assert delivery["reviewed"]["reviewer"] == "w536"
    referee = (ROOT / "REFEREE_W536.md").read_text(encoding="utf-8-sig")
    assert "Verdict: **KEEP**" in referee
    referee_receipt = read_json("REFEREE_RECEIPT.json")
    assert hashlib.sha256((ROOT / "REFEREE_W536.md").read_bytes()).hexdigest() == referee_receipt["sha256"]
    assert hashlib.sha256((ROOT / "PAIRED_PROOF_SNAPSHOT.md").read_bytes()).hexdigest() == receipt["sha256"]
    claims = [json.loads(line) for line in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines()]
    own = next(claim for claim in claims if claim["id"] == "w535-C001")
    assert own["independently_checked"] is True
    assert "w536" in own["independent_reviewer"]
    hook = json.loads((ROOT / "HOOK_PROPOSAL.jsonl").read_text(encoding="utf-8"))
    assert len(hook["text"]) <= 300 and hook["fire_when"] and hook["silent_when"]
    return {
        "command": "python -X utf8 ~/brain_workers/w535/verify_packet.py --receipt VALIDATION.json",
        "scope": "Static authored-artifact coverage and schema checks; not live recall measurement or mathematical proof certification",
        "baseline_scoped_source_cards": len(prior["rows"]),
        "baseline_cards_with_exp_minus_z_volume": sum("exp(-z|B|)" in row["body"] for row in prior["rows"]),
        "draft_entries_with_exp_minus_z_volume": sum("exp(-z|B|)" in entry["statement"] for entry in entries.values()),
        "draft_entries": len(entries),
        "draft_relations": len(bundle["relations"]),
        "resolved_cross_bundle_targets": sum("to_existing_logical" in relation for relation in bundle["relations"]),
        "theorem_or_lemma_entries": sum(entry["kind"] in {"theorem", "lemma"} for entry in entries.values()),
        "independent_referee": "w536",
        "independent_referee_verdict": "KEEP",
        "static_schema_check": "PASS",
        "submitted_payload_matches": True,
        "relation_evidence_matches": True,
        "paired_snapshot_matches": True,
        "numerical_experiments": 0,
        "formal_mathematical_check": False,
        "recorded_at": datetime.now(timezone.utc).isoformat(),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt")
    args = parser.parse_args()
    result = verify()
    text = json.dumps(result, indent=2) + "\n"
    if args.receipt:
        target = (ROOT / args.receipt).resolve()
        assert target.parent == ROOT, "receipt must remain in worker folder"
        target.write_text(text, encoding="utf-8")
    print(text, end="")
