"""Submit only the explicitly authorized w549 draft, without store integration."""
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
local = ROOT / "bundle_001.json"
bundle = json.loads(local.read_text(encoding="utf-8"))
validation = json.loads((ROOT / "draft_validation.json").read_text(encoding="utf-8"))
assert validation["status"] == "PASS" and bundle["author_agent"] == "w549"
target_dir = Path("~/math-brain-inbox/w549")
target = target_dir / "bundle_001.json"
part = target_dir / "bundle_001.part"
assert not target.exists() and not part.exists(), "Existing artifacts must not be overwritten."
target_dir.mkdir(parents=True, exist_ok=True)
with part.open("x", encoding="utf-8", newline="\n") as handle:
    handle.write(local.read_text(encoding="utf-8"))
assert json.loads(part.read_text(encoding="utf-8")) == bundle
part.rename(target)
assert json.loads(target.read_text(encoding="utf-8")) == bundle
receipt = {
    "prepared": True,
    "submitted": True,
    "submitted_at_utc": datetime.now(timezone.utc).isoformat(),
    "draft_path": str(target),
    "claim_receipt": "clm-ff7d515f15",
    "entries": len(bundle["entries"]),
    "relations": len(bundle["relations"]),
    "reviewed": False,
    "reviewer": "w551; conditional KEEP G1-G6 received, remaining admission pending",
    "partial_mathematical_keep": {"claims": ["G1", "G2", "G3", "G4", "G5", "G6"], "evidence": "~/brain_workers/w551/REVIEW_PACKET.md", "two_account_admission_verified": False},
    "ingested": False,
    "new_nodes_retrievable": False,
    "live_store_written": False,
    "integration_owner": "validating coordinator",
}
(ROOT / "SUBMISSION.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
print(json.dumps(receipt, indent=2))
