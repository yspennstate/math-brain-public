"""Validate this handoff and generate reviewable unified diffs without writing outside w548."""
import json
from pathlib import Path
from difflib import unified_diff

root = Path(__file__).resolve().parent
bundle_path = root / "bundle_001.json"
bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
assert bundle["spec"] == "mathbrain-draft-v1"
assert bundle["author_agent"] == "w548"
assert 0 < len(bundle["entries"]) <= 200
keys = {entry["key"] for entry in bundle["entries"]}
assert len(keys) == len(bundle["entries"])
for entry in bundle["entries"]:
    assert all(entry.get(k) is not None for k in (
        "key", "namespace", "logical_name", "kind", "title",
        "statement", "assumptions", "domain", "source"))
    assert entry["kind"] in ("definition", "lemma", "theorem", "concept")
    assert entry["proof_text"] is None if entry["kind"] == "concept" else bool(entry["proof_text"])
    assert entry["source"]["license"].startswith((
        "cc-by-sa", "cc-by", "cc0", "apache-2.0", "gfdl",
        "public-domain", "mit", "arxiv-nonexclusive", "owner-own-work"))
for relation in bundle["relations"]:
    assert relation["from_key"] in keys
    assert ("to_key" in relation) != ("to_existing_logical" in relation)
    assert relation["kind"] in (
        "depends_on", "defines", "proves", "refutes", "generalizes",
        "specializes", "analogous_to", "cites", "semantic_association")

verdicts = [json.loads(line) for line in (root / "VERDICTS.jsonl").read_text(encoding="utf-8").splitlines() if line]
assert len(verdicts) == 9
assert sum(row["verdict"] == "KEEP" for row in verdicts) == 8
assert sum(row["verdict"] == "FIX" for row in verdicts) == 1
claims = [json.loads(line) for line in (root / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line]
assert len(claims) == 1
assert claims[0]["independent_reviewer"].endswith("pending")
json.loads((root / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
hooks = [json.loads(line) for line in (root / "hooks_proposals" / "math-w548.jsonl").read_text(encoding="utf-8").splitlines() if line]
assert len(hooks) == 1
assert hooks[0]["fire_when"] and hooks[0]["silent_when"]
assert len(hooks[0]["text"]) <= 300

patch_dir = root / "patches"
patch_dir.mkdir(exist_ok=True)
for source, target, diff_name in (
    (bundle_path, "~/math-brain-inbox/w548/bundle_001.json", "01_bundle.diff"),
    (root / "hooks_proposals" / "math-w548.jsonl", "~/primary_directive/hooks1000/proposals/math-w548.jsonl", "02_hook.diff"),
):
    lines = source.read_text(encoding="utf-8").splitlines(keepends=True)
    diff = unified_diff([], lines, fromfile=f"a/{target}", tofile=f"b/{target}")
    (patch_dir / diff_name).write_text("".join(diff), encoding="utf-8", newline="\n")

print("VALID: 1 bundle entry; 1 relation; 8 KEEP, 1 FIX; 1 author claim pending review; 1 hook")
