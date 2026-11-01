"""Record a received referee verdict; no review of the review or store promotion."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
audit_path = Path("~/brain_workers/w551/REVIEW_PACKET.md")
audit = audit_path.read_text(encoding="utf-8")
section = audit.split("## w549:", 1)[1].split("## w550:", 1)[0]
assert "KEEP as a conditional geometric bridge; no P0321 solution." in section
assert "159" in section and "28V" in section and "G5" in section
receipt = {"reviewer": "w551", "source": str(audit_path), "verdict": "KEEP", "scope": "G1-G6 conditional geometric and covariance bridge only", "phase_existence_kept": False, "all_bundle_entries_reviewed": False, "two_account_admission_verified": False, "review_quote": section.strip()}
(ROOT / "AUDIT_RECEIPT.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
path = ROOT / "CLAIMS.jsonl"
rows = [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
for row in rows:
    if row["id"] in {"w549-P0321-G1", "w549-P0321-G3", "w549-P0321-G5"}:
        row.update(status="independently checked proof", independent_reviewer="w551", review_state="conditional KEEP received; final admission pending", independent_review_evidence=str(audit_path), remaining_gap="No Riesz-specific orientational lower bound or simultaneous phase construction; final bundle admission pending.")
path.write_text("".join(json.dumps(row, ensure_ascii=False)+"\n" for row in rows), encoding="utf-8")
source_path = ROOT / "SOURCE_STATUS.json"
source = json.loads(source_path.read_text(encoding="utf-8"))
source["independent_review"].update(status="partial: w551 conditional KEEP for G1-G6", evidence=str(audit_path), remaining="parity/gate/entry-specific admission pending")
source["canonical_repository_probe"] = json.loads((ROOT / "canonical_target_probe.json").read_text(encoding="utf-8"))
source_path.write_text(json.dumps(source, ensure_ascii=False, indent=2), encoding="utf-8")
replacements = {
    "BRIDGE_PROOF.md": [("Status: proved special case by this worker; independent review pending.", "Status: G1-G6 independently kept by w551 as a conditional bridge; final admission pending.")],
    "ATTEMPT.md": [("Independent review is pending.", "Referee w551 independently kept G1-G6 as a conditional bridge; parity/gate and final admission remain pending.")],
    "REVIEW_PACKET.md": [("It is a worker-proved special case, independently unreviewed.", "Referee w551 independently kept G1-G6 as a conditional bridge; separate parity/gate and entry-specific admission remain pending.")],
    "REPORT.md": [("I proved a conditional bridge", "Referee w551 independently kept my conditional bridge"), ("the referee is w551.", "the referee is w551; separate parity/gate and final admission remain pending.")],
}
for name, changes in replacements.items():
    path = ROOT / name
    body = path.read_text(encoding="utf-8")
    for old, new in changes:
        body = body.replace(old, new)
    path.write_text(body, encoding="utf-8")
print(json.dumps({"recorded": True, "kept_claim_rows": 3, "phase_existence_proved": False}, indent=2))
