"""Publish the explicit nonnegative-bound revision without overwriting earlier drafts."""
from __future__ import annotations

import difflib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INBOX = Path("~/math-brain-inbox/w540")
claims_path = ROOT / "CLAIMS.jsonl"
claims = [json.loads(line) for line in claims_path.read_text(encoding="utf-8").splitlines() if line.strip()]
for claim in claims:
    if claim["id"].endswith("-L2"):
        claim["statement"] = claim["statement"].replace(
            "if sum_{j_2,...,j_n}", "if b_n,y_j,Y are all nonnegative and sum_{j_2,...,j_n}")
        claim["assumptions"].append("All bound coefficients b_n, activity weights y_j, and the total bound Y are nonnegative, including zero-weight cases.")
        claim["status"] = "proved special case"
        claim["review_status"] = "Original intended reduction kept by w541/w542; explicit nonnegative-bound clarification pending final snapshot review"
claims_path.write_text("".join(json.dumps(claim, ensure_ascii=False) + "\n" for claim in claims), encoding="utf-8")

bundle = json.loads((ROOT / "brain_bundle_001.json").read_text(encoding="utf-8"))
bundle["bundle_slug"] = "p0321-cumulant-transfer-002"
bundle["supersedes_submission"] = "~/math-brain-inbox/w540/bundle_001.json"
bundle["submission_note"] = "Use this corrected revision. Version 001 omits explicit nonnegative bound coefficients in L2; preserve it as superseded, not as the active packet."
for entry in bundle["entries"]:
    suffix = entry["key"].upper()
    claim = next(row for row in claims if row["id"].endswith("-" + suffix))
    entry["statement"] = "DRAFT concept material, not a full P0321 proof. " + claim["statement"] + " Final snapshot and model/account admission review remain pending."
    entry["assumptions"] = claim["assumptions"]
    entry["review_status"] = claim["review_status"]
    entry["source"]["revision"] = "explicit-nonnegative-bounds-final-snapshot-2026-10-10-v2"
    assert entry["kind"] == "concept" and entry["proof_text"] is None
text = json.dumps(bundle, indent=2, ensure_ascii=False) + "\n"
local = ROOT / "brain_bundle_002.json"
destination = INBOX / "bundle_002.json"
assert not local.exists() and not destination.exists(), "Preserve an existing revision"
local.write_text(text, encoding="utf-8")
part = INBOX / "bundle_002.part"
assert not part.exists()
part.write_text(text, encoding="utf-8")
part.rename(destination)

patch_name = "02_p0321_cumulant_transfer_corrected.diff"
live = "~/math-brain-inbox/w540/bundle_002.json"
diff = "".join(difflib.unified_diff([], text.splitlines(keepends=True), fromfile="a/"+live, tofile="b/"+live))
(ROOT / "patches" / patch_name).write_text(diff, encoding="utf-8")
(ROOT / "patches" / "README.md").write_text(
    "The active draft is bundle_002.json, shown by 02_p0321_cumulant_transfer_corrected.diff. "
    "Patch 01 and bundle_001 are superseded historical artifacts. The active draft is already submitted; "
    "these new-file diffs are for review and are not duplicate ingestion requests.\n", encoding="utf-8")

state_path = ROOT / "BUNDLE_STATE.json"
state = json.loads(state_path.read_text(encoding="utf-8"))
state.update({"bundle_path": str(destination), "superseded_bundle_path": str(INBOX / "bundle_001.json"),
              "submitted": "YES", "reviewed": "PARTIAL", "ingested": "UNVERIFIED", "retrievable": "UNVERIFIED",
              "final_snapshot_review": "L2 nonnegativity and added L3 iterated-limit alternative explicit; final version and admission gates pending",
              "scope": "Use bundle_002 only. All six entries remain DRAFT concepts; M is unproved."})
state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
report_path = ROOT / "REPORT.md"
report = report_path.read_text(encoding="utf-8").replace("w540/bundle_001.json", "w540/bundle_002.json").replace(
    "patches/01_p0321_cumulant_transfer.diff", "patches/02_p0321_cumulant_transfer_corrected.diff")
report = report.replace("The final expanded L3 limit alternative and source/phase precisification remain available for final packet review.",
    "The final version makes L2's nonnegative bound coefficients explicit and adds L3's iterated-limit alternative; these clarifications and the phase precisification await final snapshot review.")
report = report.replace("Six DRAFT concept entries and five supported relations are submitted", "Version 002 supersedes the preserved version 001. Six DRAFT concept entries and five supported relations are submitted")
report_path.write_text(report, encoding="utf-8")
review_packet = ROOT / "REVIEW_PACKET.md"
review_packet.write_text(review_packet.read_text(encoding="utf-8") +
    "\nFinal snapshot note: bundle_002 supersedes bundle_001. L2 explicitly assumes b_n,y_j,Y>=0; "
    "the alternative fixed-r error criterion in L3 is separate from its original uniform-error statement. "
    "The final snapshot and model/account gates are pending; no theorem promotion is requested.\n", encoding="utf-8")

# Meaningful final artifact gates: preserve uncertainty, hypotheses, source tags,
# exact relation endpoints, and immutable submission equality.
assert destination.read_text(encoding="utf-8") == local.read_text(encoding="utf-8")
assert len(claims) == len(bundle["entries"]) == 6
assert len(bundle["relations"]) == 5
l2_entry = next(entry for entry in bundle["entries"] if entry["key"] == "l2")
assert "all nonnegative" in l2_entry["statement"]
assert next(claim for claim in claims if claim["id"].endswith("-M"))["status"] == "conjecture"
assert all(entry["source"]["license"].startswith("owner-own-work") for entry in bundle["entries"])
keys = {entry["key"] for entry in bundle["entries"]}
for edge in bundle["relations"]:
    assert edge["from_key"] in keys and edge["rationale"]
    assert edge.get("to_key") in keys or edge.get("to_existing_logical")
validation_path = ROOT / "VALIDATION.json"
validation = json.loads(validation_path.read_text(encoding="utf-8"))
validation.update({"command": "python -X utf8 finalize_packet.py; python -X utf8 revise_submission.py",
                   "active_submission": str(destination), "passed": True, "explicit_L2_nonnegative_bounds": True,
                   "superseded_revision_preserved": True, "final_snapshot_review": "pending"})
validation_path.write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": True, "active_submission": str(destination), "entries": 6, "relations": 5,
                  "full_target_proven": False, "final_snapshot_review": "pending"}))
