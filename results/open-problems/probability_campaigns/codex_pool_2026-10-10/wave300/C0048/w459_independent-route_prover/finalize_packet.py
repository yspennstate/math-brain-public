"""Lightweight checkpoint validation and byte receipts, not a math experiment."""
import ast
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main():
    rows = [json.loads(x) for x in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if x]
    assert len({x["id"] for x in rows}) == len(rows)
    required = {"id", "exact_statement", "assumptions", "source", "proof_or_counterexample",
                "independent_reviewer", "remaining_gap", "status"}
    statuses = {"conjecture", "numerical evidence", "sketch", "proved special case", "independently checked proof"}
    for row in rows:
        assert required <= row.keys() and row["status"] in statuses
    scripts = ["verify_entropy_route.py", "run_gated_measurements.py", "build_draft_bundle.py", "finalize_packet.py"]
    for name in scripts:
        ast.parse((ROOT / name).read_text(encoding="utf-8"), filename=name)
    hook = json.loads((ROOT / "HOOK_PROPOSAL.jsonl").read_text(encoding="utf-8"))
    assert len(hook["text"]) <= 300 and hook["fire_when"] and hook["silent_when"]
    submission = json.loads((ROOT / "SUBMISSION.json").read_text(encoding="utf-8"))
    assert submission["entries"] == 4 and submission["relations"] == 4
    gate = json.loads((ROOT / "compute_gate.json").read_text(encoding="utf-8"))
    assert gate["permitted"] is False
    assert not (ROOT / "MEASUREMENT_SUMMARY.json").exists()
    source_path = ROOT / "SOURCE_STATUS.json"
    source = json.loads(source_path.read_text(encoding="utf-8"))
    source["canonical_status_check"] = {
        "store": "~/math-brain-build/local/population/brain.sqlite3",
        "access": "mode=ro; query_only=ON",
        "canonical_path_evidence": "math-research-brain/src/math_brain/build_signal_cache.py line 24",
        "target_rows_found": 2,
        "target_supersedes_proves_refutes_edges_found": 0,
        "conclusion": "No solved/retired disposition found in the bounded target query; this does not certify current openness."}
    source["numerical_check_state"] = "DEFERRED_RESOURCE_GATE; experiment did not run"
    source["independent_review_state"] = "pending w461"
    source_path.write_text(json.dumps(source, indent=2) + "\n", encoding="utf-8")
    names = ["ATTEMPT.md", "STATEMENT.md", "CLAIMS.jsonl", "SOURCE_STATUS.json", "REVIEW_PACKET.md", "REPORT.md"] + scripts
    hashes = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in names}
    receipt = {"created_at": datetime.now(timezone.utc).isoformat(),
               "artifact_sha256": hashes, "hashes_mean": "byte identity only; not mathematical correctness",
               "claim_rows": len(rows), "analytic_lemma_proofs": 4,
               "draft_entries": submission["entries"], "draft_relations": submission["relations"],
               "checkpoint_validation": "PASS", "python_syntax_files_checked": len(scripts),
               "hook_text_characters": len(hook["text"]),
               "numerical_experiment_ran": False, "numerical_pass": None,
               "formal_checker_used": False, "formal_theorem_receipt": None,
               "independent_reviewer": "w461", "independent_review_state": "pending",
               "served_model_identity": "UNKNOWN", "main_conjecture_solved": False}
    (ROOT / "REVIEW_RECEIPT.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k:receipt[k] for k in ("claim_rows", "analytic_lemma_proofs", "draft_entries", "draft_relations",
                                          "checkpoint_validation", "numerical_experiment_ran", "independent_review_state")}))


if __name__ == "__main__":
    main()
