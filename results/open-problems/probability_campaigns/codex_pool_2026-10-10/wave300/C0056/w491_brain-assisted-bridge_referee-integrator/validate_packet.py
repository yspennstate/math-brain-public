import json
from pathlib import Path

bundle = json.loads(Path("bundle_001.json").read_text(encoding="utf-8"))
source_status = json.loads(Path("SOURCE_STATUS.json").read_text(encoding="utf-8"))
bundle_status = json.loads(Path("BUNDLE_STATUS.json").read_text(encoding="utf-8"))
assert source_status["problem_id"] == "C0056"
assert bundle_status["submitted"] is False and bundle_status["ingested"] is False
assert bundle["spec"] == "mathbrain-draft-v1"
assert bundle["author_agent"] == "w491"
assert 0 < len(bundle["entries"]) <= 200
keys = set()
for entry in bundle["entries"]:
    assert set(("key", "namespace", "logical_name", "kind", "title", "statement", "proof_text", "assumptions", "domain", "source")) <= entry.keys()
    assert entry["kind"] in {"definition", "lemma", "theorem", "concept"}
    assert bool(entry["proof_text"]) == (entry["kind"] in {"lemma", "theorem"})
    assert entry["source"]["license"].startswith("owner-own-work")
    assert entry["key"] not in keys
    keys.add(entry["key"])
for relation in bundle["relations"]:
    assert relation["from_key"] in keys and relation["to_key"] in keys
    assert relation["kind"] in {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
for n, line in enumerate(Path("CLAIMS.jsonl").read_text(encoding="utf-8").splitlines(), 1):
    claim = json.loads(line)
    assert set(("id", "statement", "assumptions", "source", "proof_or_counterexample", "independent_reviewer", "remaining_gap", "status")) <= claim.keys(), n
for line in Path("proof-audit-w491.jsonl").read_text(encoding="utf-8").splitlines():
    hook = json.loads(line)
    assert set(("cue", "fire_when", "silent_when", "text", "evidence", "proposer")) == hook.keys()
    assert len(hook["text"]) <= 300
print(f"VALID: {len(bundle['entries'])} cards, {len(bundle['relations'])} relations, {n} claim rows, 1 hook proposal, source and lifecycle JSON")
