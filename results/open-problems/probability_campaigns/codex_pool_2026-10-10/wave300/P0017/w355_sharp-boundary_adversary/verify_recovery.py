"""Verify the persisted P0017 handoff without changing submitted or live data."""
import hashlib
import json
import sqlite3
import time
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def read_json(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8-sig"))


def read_rows(name):
    return [json.loads(line) for line in (ROOT / name).read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    status = (ROOT / "STATUS.md").read_text(encoding="utf-8-sig")
    report = {
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "state": status.splitlines()[0],
        "next": next(line for line in status.splitlines() if line.startswith("NEXT:")),
        "feedback_present": (ROOT / "FEEDBACK.md").exists(),
        "changes_to_math_or_submitted_bundle": False,
        "tests_rerun": False,
    }
    names = [
        "SOURCE_STATUS.json", "ATTEMPT.md", "CLAIMS.jsonl", "REVIEW_PACKET.md",
        "REPORT.md", "REFEREE_VERDICTS.jsonl", "VERIFICATION.json",
        "BUNDLE_STATES.json", "FINAL_VERIFICATION.json", "RELATION_EVIDENCE.jsonl",
        "HOOK_PROPOSAL.jsonl", "patches/01_probability_slice_hook.diff",
    ]
    report["artifacts"] = {name: {"exists": (ROOT / name).is_file(), "sha256": digest(ROOT / name) if (ROOT / name).is_file() else None} for name in names}
    claims = read_rows("CLAIMS.jsonl")
    verdicts = read_rows("REFEREE_VERDICTS.jsonl")
    report["claim_rows"] = len(claims)
    report["referee_receipt_rows"] = len(verdicts)
    report["referee_receipts"] = [{key: row[key] for key in row if key in {"claim_id", "id", "reviewer", "reviewer_agent", "verdict", "status"}} for row in verdicts]
    report["referee_receipt_keys"] = [list(row) for row in verdicts]
    report["saved_final_verification"] = read_json("FINAL_VERIFICATION.json")
    verification = read_json("VERIFICATION.json")
    report["saved_test_receipt"] = {key: value for key, value in verification.items() if not isinstance(value, (list, dict))}
    local_bundle = ROOT / "drafts" / "bundle_001.json"
    inbox_bundle = Path("~/math-brain-inbox/w355/bundle_001.json")
    bundle = json.loads(local_bundle.read_text(encoding="utf-8-sig"))
    report["draft_entry_count"] = len(bundle.get("entries", []))
    report["submitted_file_present"] = inbox_bundle.is_file()
    report["local_draft_sha256"] = digest(local_bundle)
    report["submitted_draft_sha256"] = digest(inbox_bundle) if inbox_bundle.is_file() else None
    report["submitted_equals_local"] = report["local_draft_sha256"] == report["submitted_draft_sha256"]
    logical_ids = [
        "math:probability.concentration:p0017-kls-primary-resolution-claims-october-2026",
        "math:probability.concentration:isotropic-regular-simplex-conditional-poincare-extremes",
        "math:probability.concentration:conditional-poincare-constant-average-cannot-separate-from-energy",
    ]
    observation = {"checked_at": report["checked_at"], "read_only": True, "logical_ids": logical_ids}
    try:
        store = Path("~/math-brain-build/local/population/brain.sqlite3")
        with sqlite3.connect(store.as_uri() + "?mode=ro", uri=True, timeout=8) as conn:
            conn.execute("PRAGMA query_only=ON")
            deadline = time.monotonic() + 8
            conn.set_progress_handler(lambda: int(time.monotonic() > deadline), 10000)
            rows = conn.execute("SELECT id, kind, title, json_extract(metadata_json, '$.logical_id') FROM nodes WHERE json_extract(metadata_json, '$.logical_id') IN (?, ?, ?) LIMIT 3", logical_ids).fetchall()
            observation["nodes"] = [dict(zip(("id", "kind", "title", "logical_id"), row)) for row in rows]
            observation["exact_id_nodes_observed"] = len(rows)
            observation["query_completed"] = True
    except (sqlite3.Error, OSError) as error:
        observation["query_completed"] = False
        observation["error"] = str(error)
    observation["scope"] = "Exact submitted logical IDs only; this is not a deduplication receipt or recall test."
    (ROOT / "RECOVERY_INGESTION_OBSERVATION.json").write_text(json.dumps(observation, indent=2) + "\n", encoding="utf-8")
    report["ingestion_observation"] = observation
    report["package_integrity"] = "PASS" if all(item["exists"] for item in report["artifacts"].values()) and report["claim_rows"] == 7 and report["referee_receipt_rows"] == 2 and report["draft_entry_count"] == 3 and report["submitted_equals_local"] else "NEEDS_INSPECTION"
    (ROOT / "RECOVERY_CHECK.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: report[key] for key in report if key != "artifacts"}, indent=2))


if __name__ == "__main__":
    main()
