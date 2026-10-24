"""Bounded offline checks; never ingests or writes to the live store."""
import hashlib
import json
import sqlite3
from pathlib import Path

root = Path(__file__).parent
bundle = json.loads((root / "bundle_001.json").read_text(encoding="utf-8"))
json.loads((root / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
state = json.loads((root / "BRAIN_STATE.json").read_text(encoding="utf-8"))
claims = [json.loads(line) for line in (root / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line]
assert bundle["spec"] == "mathbrain-draft-v1"
assert bundle["author_agent"] == "w458"
assert 1 <= len(bundle["entries"]) <= 200
assert len({e["key"] for e in bundle["entries"]}) == len(bundle["entries"])
assert all(e["kind"] in {"definition", "lemma", "theorem", "concept"} for e in bundle["entries"])
assert all(bool(e["proof_text"]) == (e["kind"] in {"lemma", "theorem"}) for e in bundle["entries"])
assert all(e["source"]["license"].startswith(("owner-own-work", "arxiv-nonexclusive")) for e in bundle["entries"])
keys = {e["key"] for e in bundle["entries"]}
assert all(r["from_key"] in keys and ((r.get("to_key") in keys) or r.get("to_existing_logical")) for r in bundle["relations"])
assert all({"id", "verdict", "exact_statement", "assumptions", "source", "source_quote", "proof_or_counterexample", "independent_reviewer", "remaining_gap", "status"} <= set(c) for c in claims)

db = "~/math-brain-build/local/population/brain.sqlite3"
con = sqlite3.connect("file:" + db + "?mode=ro", uri=True)
target = "math:probability.statmech:open-problem-c0048-discontinuity-of-the-potts-phase-transition-on-z-d-for-q-3-d-3"
target_count = con.execute("select count(*) from nodes where metadata_json like ?", ("%" + target + "%",)).fetchone()[0]
new_names = ["math:" + e["namespace"] + ":" + e["logical_name"] for e in bundle["entries"]]
already_present = {name: con.execute("select count(*) from nodes where metadata_json like ?", ("%" + name + "%",)).fetchone()[0] for name in new_names}
con.close()
assert target_count == 1
assert all(n == 0 for n in already_present.values()), already_present
assert Path(state["bundle"]).read_bytes() == (root / "bundle_001.json").read_bytes()
hook_lines = Path("~/primary_directive/hooks1000/proposals/math-w458.jsonl").read_text(encoding="utf-8").splitlines()
assert sum(json.loads(x)["id"] == "c0048-w458-01" for x in hook_lines if x) == 1

print("claim_rows", len(claims), "bundle_entries", len(bundle["entries"]), "relations", len(bundle["relations"]))
print("existing_C0048_cards", target_count, "matching_new_logical_names", sum(already_present.values()))
print("submitted_bundle_byte_match", True, "submitted_hook_rows", 1)
for name in ("CLAIMS.jsonl", "REVIEW_PACKET.md", "ATTEMPT.md", "SOURCE_STATUS.json", "bundle_001.json"):
    data = (root / name).read_bytes()
    print(name, len(data), hashlib.sha256(data).hexdigest())
