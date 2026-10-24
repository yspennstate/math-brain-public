"""Local read-only checks; never opens or writes the live math store."""
import json
import math
from pathlib import Path

root = Path(__file__).parent
bundle = json.loads((root / "brain_draft" / "bundle_001.json").read_text(encoding="utf-8"))
assert bundle["spec"] == "mathbrain-draft-v1"
assert bundle["author_agent"] == "w365"
entries = bundle["entries"]
assert len(entries) == 2
keys = {entry["key"] for entry in entries}
assert len(keys) == len(entries)
for entry in entries:
    assert {"key", "namespace", "logical_name", "kind", "title", "statement", "proof_text", "assumptions", "domain", "source"} <= entry.keys()
    assert entry["kind"] == "concept" and entry["proof_text"] is None
    assert entry["statement"] and entry["source"]["license"].startswith(("arxiv-nonexclusive", "owner-own-work"))
for relation in bundle["relations"]:
    assert relation["from_key"] in keys and relation["to_key"] in keys
    assert relation["kind"] == "semantic_association" and relation["rationale"]

rows = [json.loads(s) for s in (root / "VERDICTS.jsonl").read_text(encoding="utf-8").splitlines() if s.strip()]
assert len(rows) == 5 and len({r["row"] for r in rows}) == 5
assert {r["verdict"] for r in rows} == {"KEEP"}
hooks = [json.loads(s) for s in (root / "hook_proposal.jsonl").read_text(encoding="utf-8").splitlines() if s.strip()]
assert len(hooks) == 1
for field in ("id", "area", "event", "cue", "fire_when", "silent_when", "text", "evidence", "proposer"):
    assert hooks[0][field]
assert len(hooks[0]["text"]) <= 300

r = 6 * (1 / 100) ** (3 / 4)
assert (4 / 3) * r / (1 - r) < 1 / 3
print(f"PASS 2 concept entries, 1 relation, 5 verdict rows, 1 hook; w363 L4 r={r:.8f}, bad-event ceiling={(4/3)*r/(1-r):.8f}")
