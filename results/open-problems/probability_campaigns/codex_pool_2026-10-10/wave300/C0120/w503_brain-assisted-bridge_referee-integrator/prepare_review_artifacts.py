"""Validate this referee packet and produce a source-row correction diff only.

This script never writes outside the w503 folder or changes the intake file.
"""

from __future__ import annotations

import difflib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
INTAKE = Path(
    "~/<private-repo>/06_math_research/"
    "probability_1000_intake_claude_20260907/problems.jsonl"
)
RELATIVE = (
    "06_math_research/probability_1000_intake_claude_20260907/problems.jsonl"
)


def main() -> None:
    source_status = json.loads((HERE / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
    assert source_status["current_open_status"] == "UNKNOWN"
    claims = [json.loads(line) for line in (HERE / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line]
    assert len(claims) >= 4 and all(c["parent_problem_solved"] is False for c in claims)
    bundle = json.loads((HERE / "bundle_001.json").read_text(encoding="utf-8"))
    assert bundle["spec"] == "mathbrain-draft-v1" and bundle["author_agent"] == "w503"
    allowed_kinds = {"definition", "lemma", "theorem", "concept"}
    allowed_relations = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
    keys = {e["key"] for e in bundle["entries"]}
    assert len(keys) == len(bundle["entries"])
    for entry in bundle["entries"]:
        assert entry["kind"] in allowed_kinds
        assert entry["source"]["license"].startswith(("owner-own-work", "arxiv-nonexclusive"))
        assert entry["proof_text"] if entry["kind"] in {"lemma", "theorem"} else entry["proof_text"] is None
    for relation in bundle["relations"]:
        assert relation["from_key"] in keys and relation["kind"] in allowed_relations
        assert relation.get("to_key") in keys or relation.get("to_existing_logical", "").startswith("math:")
        assert relation["rationale"]

    original = INTAKE.read_bytes().splitlines(keepends=True)
    hits = [(i, json.loads(line)) for i, line in enumerate(original) if b'"C0120"' in line]
    assert len(hits) == 1
    index, row = hits[0]
    assert row["problem_id"] == "C0120" and "Var(log Z_n)" in row["statement"]
    previous_statement = row["statement"]
    row["prior_intake_statement_before_source_review"] = previous_statement
    row["statement"] = (
        "In Chatterjee arXiv:0810.4221v2 Section 8, let M_n be the maximum sum of "
        "independent standard Gaussian vertex weights over n-vertex up/right paths "
        "in Z_+^2 starting at the origin with a free endpoint. Section 12(3) asks "
        "to improve the fluctuation exponent beyond Theorem 8.1's Var(M_n)=O(n/log n). "
        "The concrete power target Var(M_n)=O(n^(1-epsilon)) for some fixed epsilon>0 "
        "is an interpretation of that question, not verbatim source wording."
    )
    row["status_search"] = (
        "Current openness UNKNOWN as of 2026-10-10 bounded check. The 2009 "
        "Gaussian n/log n theorem in arXiv:0909.1352 is fixed-endpoint, and the "
        "2024 Ahlberg et al. stability-to-chaos paper is fixed-endpoint with "
        "nonnegative weights; neither verifies a power improvement for this "
        "source's Gaussian free-endpoint model. Local solved registers had no "
        "C0120 or directed-polymer match."
    )
    row["verification"] = "primary_source_scope_checked_2026-10-10; current_openness_unverified"
    row["source_scope_review"] = "~/brain_workers/w503/SOURCE_STATUS.json"
    ending = b"\r\n" if original[index].endswith(b"\r\n") else b"\n"
    revised = original.copy()
    revised[index] = json.dumps(row, ensure_ascii=False, sort_keys=True).encode("utf-8") + ending
    patch_lines = list(difflib.unified_diff(
        [line.decode("utf-8") for line in original],
        [line.decode("utf-8") for line in revised],
        fromfile="a/" + RELATIVE,
        tofile="b/" + RELATIVE,
        n=2,
    ))
    patch_dir = HERE / "patches"
    patch_dir.mkdir(exist_ok=True)
    patch_path = patch_dir / "01_correct_C0120_source_scope.diff"
    patch_path.write_text("".join(patch_lines), encoding="utf-8", newline="")
    assert sum(a != b for a, b in zip(original, revised)) == 1
    assert "Var(log Z_n)" not in row["statement"]
    receipt = {
        "source_line": index + 1,
        "changed_rows": 1,
        "bundle_entries": len(bundle["entries"]),
        "bundle_relations": len(bundle["relations"]),
        "claims_parsed": len(claims),
        "patch_path": str(patch_path),
        "live_files_written": 0,
    }
    (HERE / "VALIDATION.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt))


if __name__ == "__main__":
    main()
