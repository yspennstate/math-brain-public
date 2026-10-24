"""Create reviewable unified diffs for staged artifacts; writes only in this worker folder."""
from pathlib import Path
from difflib import unified_diff
import json


def new_file_diff(source: Path, target: str) -> str:
    content = source.read_text(encoding="utf-8").splitlines(keepends=True)
    return "".join(unified_diff([], content, fromfile="a/" + target,
                                tofile="b/" + target, n=3))


bundle = json.loads(Path("bundles/bundle_001.json").read_text(encoding="utf-8"))
assert bundle["spec"] == "mathbrain-draft-v1"
keys = {entry["key"] for entry in bundle["entries"]}
assert len(keys) == len(bundle["entries"])
assert len(bundle["entries"]) <= 200
assert all(relation["from_key"] in keys and relation["to_key"] in keys
           for relation in bundle["relations"])
assert all(entry["kind"] in {"definition", "lemma", "theorem", "concept"}
           and (entry["proof_text"] or entry["kind"] in {"definition", "concept"})
           and entry["source"]["license"].startswith(("owner-own-work", "arxiv-nonexclusive"))
           for entry in bundle["entries"])
claims = [json.loads(line) for line in Path("CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line]
hooks = [json.loads(line) for line in Path("hooks_math_w380.jsonl").read_text(encoding="utf-8").splitlines() if line]
assert len(claims) == 5 and len(hooks) == 1
assert len(hooks[0]["text"]) <= 300

out = Path("patches")
out.mkdir(exist_ok=True)
(out / "01_reviewed_bundle.diff").write_text(
    new_file_diff(Path("bundles/bundle_001.json"),
                  "~/math-brain-inbox/w380/bundle_001.json"),
    encoding="utf-8")
(out / "02_hook_proposal.diff").write_text(
    new_file_diff(Path("hooks_math_w380.jsonl"),
                  "~/primary_directive/hooks1000/proposals/math-w380.jsonl"),
    encoding="utf-8")
print(json.dumps({"generated_diffs": 2, "draft_entries": len(bundle["entries"]),
                  "supported_relations": len(bundle["relations"]),
                  "reviewed_claims": len(claims), "hook_proposals": len(hooks)}))
