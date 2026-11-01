"""Validate only the review packet and the proposed diff; never mutate live files."""
from pathlib import Path
import json
import hashlib
import subprocess

base = Path(__file__).parent
source = json.loads((base / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
state = json.loads((base / "BUNDLE_STATE.json").read_text(encoding="utf-8"))
bundle = json.loads((base / state["draft_path"]).read_text(encoding="utf-8"))
assert source["current_openness"] == "UNKNOWN"
assert bundle["spec"] == "mathbrain-draft-v1"
assert bundle["author_agent"] == "w410"
assert len(bundle["entries"]) == 4 and len(bundle["relations"]) == 3
keys = {entry["key"] for entry in bundle["entries"]}
for entry in bundle["entries"]:
    for field in ("namespace", "logical_name", "kind", "title", "statement", "proof_text", "assumptions", "domain", "source"):
        assert field in entry, (entry["key"], field)
    for field in ("source_id", "url", "revision", "license", "excerpt"):
        assert field in entry["source"], (entry["key"], field)
    assert entry["source"]["license"].startswith(("arxiv-nonexclusive", "owner-own-work"))
    assert (entry["proof_text"] is None) == (entry["kind"] in ("concept", "definition"))
for rel in bundle["relations"]:
    assert rel["from_key"] in keys
    assert rel["kind"] == "semantic_association"
    if "to_existing_logical" in rel:
        assert rel["to_existing_logical"].startswith("math:probability.percolation:open-problem-c0017-")
    else:
        assert rel["to_key"] in keys
rows = {}
for name in ("CLAIMS.jsonl", "VERDICTS.jsonl", "hook_proposal.jsonl"):
    lines = (base / name).read_text(encoding="utf-8").splitlines()
    rows[name] = [json.loads(line) for line in lines if line.strip()]
assert len(rows["VERDICTS.jsonl"]) == 10
assert len(rows["CLAIMS.jsonl"]) == 5
assert {r["verdict"] for r in rows["VERDICTS.jsonl"]} == {"KEEP", "FIX"}
assert len(rows["hook_proposal.jsonl"]) == 1
assert len(rows["hook_proposal.jsonl"][0]["text"]) <= 300
if state["submitted"]:
    local_bytes = (base / state["draft_path"]).read_bytes()
    assert hashlib.sha256(local_bytes).hexdigest() == state["submitted_sha256"]
    assert Path(state["submission_path"]).read_bytes() == local_bytes
    assert Path(state["hook_proposal_path"]).read_bytes() == (base / "hook_proposal.jsonl").read_bytes()
patch = base / "patches" / "01_c0017_spin_correction.diff"
check = subprocess.run(["git", "apply", "--check", str(patch)], cwd="~/<private-repo>", capture_output=True, text=True, timeout=120)
assert check.returncode == 0, check.stdout + check.stderr
print(f"VALID: {len(rows['CLAIMS.jsonl'])} claim rows, {len(rows['VERDICTS.jsonl'])} verdict rows, {len(bundle['entries'])} draft cards, {len(bundle['relations'])} draft links, 1 hook proposal")
print("PATCH: git apply --check passed against live checkout (no write)")
print("STATUS: primary proof claim exists; current openness UNKNOWN; lattice input unproved")
