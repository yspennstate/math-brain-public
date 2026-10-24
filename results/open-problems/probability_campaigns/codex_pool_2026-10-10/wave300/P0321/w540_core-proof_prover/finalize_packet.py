"""Record actual scoped receipts and validate draft artifacts, without live ingestion."""
from __future__ import annotations

import difflib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
referee_path = Path("~/brain_workers/w542/CLAIMS.jsonl")
referee_rows = [json.loads(line) for line in referee_path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
verdicts = {row["id"]: row for row in referee_rows if row.get("id", "").startswith("w540-")}
claims_path = ROOT / "CLAIMS.jsonl"
claims = [json.loads(line) for line in claims_path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
for claim in claims:
    suffix = claim["id"].rsplit("-", 1)[1]
    verdict = verdicts.get("w540-" + suffix + "-verdict")
    assert verdict and verdict["verdict"].startswith("KEEP")
    claim["referee_receipt"] = {"auditor": "w542", "path": str(referee_path), "row_id": verdict["id"],
                                 "verdict": verdict["verdict"], "exact_checked_statement": verdict["exact_statement"],
                                 "remaining_gap": verdict["remaining_gap"]}
    claim["peer_audit"]["designated_referee_status"] = "KEEP original scoped claim"
    if suffix in {"L1", "L2", "C1", "C2"}:
        claim["status"] = "independently checked proof"
        claim["review_status"] = "w541 and w542 kept the scoped result; different-login/model admission gates unverified"
    elif suffix == "L3":
        claim["status"] = "proved special case"
        claim["review_status"] = "Original uniform-error L3 kept by w541/w542; added fixed-r vanishing-error alternative is author-proved from w541's correction and pending final snapshot review"
    else:
        assert suffix == "M" and claim["status"] == "conjecture"
        claim["review_status"] = "w541/w542 KEEP only as an explicitly unproved input"
claims_path.write_text("".join(json.dumps(claim, ensure_ascii=False) + "\n" for claim in claims), encoding="utf-8")
(ROOT / "REVIEW_RECEIPTS.json").write_text(json.dumps({"referee": "w542", "source_path": str(referee_path),
    "scoped_verdicts": list(verdicts.values()), "adversary_path": "~/brain_workers/w541/AUDIT.md",
    "final_L3_alternative_review": "pending", "full_target": "unproved", "model_and_login_gates": "unverified"},
    indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

source_path = ROOT / "SOURCE_STATUS.json"
source = json.loads(source_path.read_text(encoding="utf-8"))
source["primary_source"]["theorem_47_scope"] = {
    "as_checked": "Theorem 47 requires d in {1,2}, s>d and beta finite for its translation-invariance assertion.",
    "source_url": "https://arxiv.org/html/2202.09240v2#S6.SS1",
    "excluded_application": "It cannot establish this assertion for s=1,d=2; no such use is made in the w540 route.",
    "origin_of_check": "w542 identified the issue; w540 directly checked the primary theorem statement."}
source_path.write_text(json.dumps(source, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

bundle_path = Path("~/math-brain-inbox/w540/bundle_001.json")
local_bundle = ROOT / "brain_bundle_001.json"
bundle = json.loads(local_bundle.read_text(encoding="utf-8"))
assert bundle_path.exists() and bundle_path.read_text(encoding="utf-8") == local_bundle.read_text(encoding="utf-8")
assert len(bundle["entries"]) == 6 and len(bundle["relations"]) == 5
assert all(entry["kind"] == "concept" and entry["proof_text"] is None and entry["title"].startswith("DRAFT:") for entry in bundle["entries"])
assert all(entry["source"]["license"].startswith("owner-own-work") for entry in bundle["entries"])
keys = {entry["key"] for entry in bundle["entries"]}
assert len(keys) == 6
dependency_graph = {key: [] for key in keys}
for relation in bundle["relations"]:
    assert relation["from_key"] in keys and relation["rationale"]
    if "to_key" in relation:
        assert relation["to_key"] in keys
    else:
        assert relation["to_existing_logical"] == source["canonical_problem_card"]["logical_id"]
    if relation["kind"] == "depends_on":
        dependency_graph[relation["from_key"]].append(relation["to_key"])

def visit(key: str, stack: set[str], visited: set[str]) -> None:
    assert key not in stack, "dependency cycle"
    if key in visited:
        return
    stack.add(key)
    for child in dependency_graph[key]:
        visit(child, stack, visited)
    stack.remove(key)
    visited.add(key)

visited: set[str] = set()
for key in keys:
    visit(key, set(), visited)
measurements = json.loads((ROOT / "MEASUREMENTS.json").read_text(encoding="utf-8"))
assert measurements["passed"] and measurements["claim_rows"] == len(claims)
assert source["current_openness"] == "UNKNOWN" and source["full_target_proven"] is False
assert next(claim for claim in claims if claim["id"].endswith("-M"))["status"] == "conjecture"
for name in ("STATUS.md", "SOURCE_STATUS.json", "ATTEMPT.md", "CLAIMS.jsonl", "REVIEW_PACKET.md", "REPORT.md", "MODEL_EVIDENCE.json"):
    assert (ROOT / name).exists(), name

state_path = ROOT / "BUNDLE_STATE.json"
state = json.loads(state_path.read_text(encoding="utf-8"))
state.update({"submitted": "YES", "reviewed": "PARTIAL", "ingested": "UNVERIFIED", "retrievable": "UNVERIFIED",
              "original_mathematical_claims": "w541 and w542 KEEP L1-L3/C1-C2 under the original exact hypotheses",
              "final_snapshot_review": "pending for added L3 alternative and precise phase formulation",
              "different_login_gate": "unverified", "different_model_gate": "unverified",
              "scope": "Immutable submitted bundle remains six DRAFT concepts; no theorem promotion or live worker ingestion."})
state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
patch_directory = ROOT / "patches"
patch_directory.mkdir(exist_ok=True)
live_path = "~/math-brain-inbox/w540/bundle_001.json"
diff = "".join(difflib.unified_diff([], local_bundle.read_text(encoding="utf-8").splitlines(keepends=True),
                                 fromfile="a/" + live_path, tofile="b/" + live_path))
(patch_directory / "01_p0321_cumulant_transfer.diff").write_text(diff, encoding="utf-8")

validation = {"command": "python -X utf8 finalize_packet.py", "passed": True, "claim_rows": len(claims),
              "draft_concept_entries": len(bundle["entries"]), "supported_relations": len(bundle["relations"]),
              "dependency_cycles": 0, "scoped_referee_keeps": 5, "full_target_proven": False,
              "live_store_writes": 0, "hash_or_store_manifest_created": False,
              "review_scope": "Final snapshot/gates pending; original L1-L3 and C1-C2 have exact KEEP receipts."}
(ROOT / "VALIDATION.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
print(json.dumps(validation))
