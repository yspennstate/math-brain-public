"""Check syntax and the local draft's structural constraints without ingesting it."""
import json
from pathlib import Path

root = Path(__file__).parent
bundle = json.loads((root / "bundle_001.json").read_text(encoding="utf-8"))
assert bundle["spec"] == "mathbrain-draft-v1"
assert bundle["author_agent"] == "w524"
assert 0 < len(bundle["entries"]) <= 200
keys = {entry["key"] for entry in bundle["entries"]}
assert len(keys) == len(bundle["entries"])
for entry in bundle["entries"]:
    assert entry["kind"] == "concept" and entry["proof_text"] is None
    assert entry["source"]["license"].startswith(("arxiv-nonexclusive", "owner-own-work"))
for relation in bundle["relations"]:
    assert relation["from_key"] in keys and relation["to_key"] in keys
    assert relation["kind"] in {"depends_on", "semantic_association"}

for name in ("SOURCE_STATUS.json", "BRAIN_STATES.json", "PROGRESS_EVENT.json"):
    json.loads((root / name).read_text(encoding="utf-8"))
for name in ("CLAIMS.jsonl", "VERDICTS.jsonl", "HOOK_PROPOSAL.jsonl"):
    rows = [json.loads(line) for line in (root / name).read_text(encoding="utf-8").splitlines() if line]
    assert rows, name
hook = json.loads((root / "HOOK_PROPOSAL.jsonl").read_text(encoding="utf-8"))
assert len(hook["text"]) <= 300
assert hook["fire_when"] and hook["silent_when"] and hook["evidence"]
print(f"valid: {len(bundle['entries'])} concept entries, {len(bundle['relations'])} exact-key relations, 3 claims, 7 verdicts, hook text {len(hook['text'])}/300 chars")
