"""Mechanical artifact checks only; never a mathematical proof certificate."""
import json
import sys
from collections import Counter
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
for name in ("STATUS.md", "SOURCE_STATUS.json", "ATTEMPT.md", "CLAIMS.jsonl",
             "REVIEWS.jsonl", "REVIEW_PACKET.md", "REPORT.md", "BUNDLE_LIFECYCLE.json",
             "AUDIT_RECEIPTS.jsonl", "SHORTCUT_REDERIVATION.md", "POSTERIOR_REDERIVATION.md"):
    if not (ROOT / name).is_file() or not (ROOT / name).stat().st_size:
        raise AssertionError("Missing required artifact: " + name)
claims = [json.loads(line) for line in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
reviews = [json.loads(line) for line in (ROOT / "REVIEWS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
if len({value["claim_id"] for value in claims}) != len(claims):
    raise AssertionError("Duplicate own claim identifiers")
if len({value["review_id"] for value in reviews}) != len(reviews):
    raise AssertionError("Duplicate peer review identifiers")
allowed = {"conjecture", "numerical evidence", "sketch", "proved special case", "independently checked proof"}
for claim in claims:
    if claim["status"] not in allowed or claim["parent_problem_solved"]:
        raise AssertionError("Invalid own-claim scope/status")
    for required in ("statement", "assumptions", "source", "proof", "independent_reviewer", "remaining_gap"):
        if not claim.get(required):
            raise AssertionError("Missing claim field: " + required)
for review in reviews:
    for required in ("exact_statement", "assumptions", "reproduction", "hardest_claim_rederived", "remaining_gap"):
        if not review.get(required):
            raise AssertionError("Missing review field: " + required)
    if review["parent_problem_solved"] or review["verdict"] not in {"KEEP", "FIX", "DROP"}:
        raise AssertionError("Invalid review scope")
lifecycle = json.loads((ROOT / "BUNDLE_LIFECYCLE.json").read_text(encoding="utf-8"))
submitted = Path(lifecycle["submitted"]["path"])
if submitted.resolve().parent != Path(r"~/math-brain-inbox/w389").resolve():
    raise AssertionError("Unexpected authorized inbox path")
local_path = Path(lifecycle["prepared"]["path"]).resolve()
if not local_path.is_relative_to(ROOT.resolve()):
    raise AssertionError("Local prepared draft escaped worker folder")
local_bundle = json.loads(local_path.read_text(encoding="utf-8"))
if json.loads(submitted.read_text(encoding="utf-8")) != local_bundle:
    raise AssertionError("Submitted draft differs from current validated local draft")
from prepare_bundle import validate
validate(local_bundle)
relations = [json.loads(line) for line in (ROOT / "RELATIONS_EVIDENCE.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
if len(relations) != len(local_bundle["relations"]):
    raise AssertionError("Missing relation evidence")
if not all(row.get("from_statement_quote") and row.get("to_statement_quote") for row in relations):
    raise AssertionError("A relation lacks a supporting end")
ends = {entry["key"]: entry["statement"] for entry in local_bundle["entries"]}
for row, relation in zip(relations, local_bundle["relations"], strict=True):
    if row["from_statement_quote"] != ends[relation["from_key"]]:
        raise AssertionError("Relation source quote differs from current reviewed statement")
    if "to_key" in relation and row["to_statement_quote"] != ends[relation["to_key"]]:
        raise AssertionError("Relation target quote differs from current reviewed statement")
    if row["rationale"] != relation["rationale"]:
        raise AssertionError("Relation rationale differs from current reviewed version")
    if "attainable" in relation["rationale"]:
        raise AssertionError("Designated auditor's wording correction was not applied")
receipts = [json.loads(line) for line in (ROOT / "AUDIT_RECEIPTS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
by_receipt = {row["id"]: row for row in receipts}
for suffix in ("C02", "C03"):
    receipt_id = "P0117-w392-review-w389-" + suffix
    if by_receipt[receipt_id]["verdict"] != "KEEP":
        raise AssertionError("Missing independent KEEP")
    claim = next(row for row in claims if row["claim_id"] == "P0117-w389-" + suffix)
    if claim["status"] != "independently checked proof" or claim["independent_review"]["review_id"] != receipt_id:
        raise AssertionError("Own status differs from actual audit receipt")
if by_receipt["P0117-w392-review-w389-relations"]["verdict"] != "KEEP_WITH_WORDING_FIX":
    raise AssertionError("Relation review receipt was altered")
if lifecycle["reviewed"]["different_login_quorum_certified"] or lifecycle["ingested"]["integrator_run_by_w389"]:
    raise AssertionError("Unsupported quorum or integration assertion")
source = json.loads((ROOT / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
if source["current_openness"] != "UNKNOWN" or source["formal_check"]["run"]:
    raise AssertionError("Unexpected global source/formal-certification claim")
measurements = json.loads((ROOT / "measurements.json").read_text(encoding="utf-8"))
if measurements["inclusion_cases_passed"] != 6 or measurements["inner_vertex_cases_checked"] != 102:
    raise AssertionError("Incomplete finite diagnostic evidence")
result = {"command": "python -X utf8 verify_packet.py", "artifact_checks": "PASS",
          "own_claims": len(claims), "peer_reviews": len(reviews),
          "verdicts": dict(Counter(value["verdict"] for value in reviews)),
          "entries": len(local_bundle["entries"]), "relations": len(relations),
          "queued_draft_matches_current_local": True, "own_independent_keep_receipts": 2,
          "relation_wording_fix_applied": True, "different_login_quorum_certified": False,
          "live_integrator_run": False,
          "mathematical_proof_certificate": False, "parent_problem_solved": False}
(ROOT / "FINAL_CHECKS.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))
