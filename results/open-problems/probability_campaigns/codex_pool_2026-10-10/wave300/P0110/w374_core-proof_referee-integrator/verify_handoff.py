"""Structural handoff checks; mathematical verdicts are justified in the receipt."""

import json
from pathlib import Path

root = Path(__file__).resolve().parent
receipt = json.loads((root / "REFEREE_RECEIPT.json").read_text(encoding="utf-8"))
source = json.loads((root / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
hook_lines = (root / "HOOK_PROPOSAL.jsonl").read_text(encoding="utf-8").splitlines()
assert len(hook_lines) == 1
hook = json.loads(hook_lines[0])
assert set(hook) == {"id", "area", "event", "cue", "fire_when", "silent_when", "text", "evidence", "proposer"}
assert len(hook["text"]) <= 300 and hook["fire_when"] and hook["silent_when"]
patch = (root / "patches" / "01_fpp_version_hook.diff").read_text(encoding="utf-8")
assert "+" + hook_lines[0] in patch
assert source["primary_source_url"] == "https://arxiv.org/pdf/1511.03262v2"
assert "(4.19)" in source["primary_source_quote"]
assert "(4.13)" in source["version_note"]
rows = receipt["w372_claim_verdicts"] + receipt["w373_claim_verdicts"]
assert len(receipt["w372_claim_verdicts"]) == 9
assert len(receipt["w373_claim_verdicts"]) == 8
assert len({row["claim_id"] for row in rows}) == 17
assert all(row["verdict"] in {"KEEP", "FIX", "DROP"} and row["reproduction"] and row["remaining_gap"] for row in rows)
assert not (Path("~/math-brain-inbox/w374") / "bundle_001.json").exists()
assert (Path("~/math-brain-inbox/w374") / "bundle_001.withheld").exists()
print(json.dumps({"receipt_rows": len(rows), "w372": 9, "w373": 8,
                  "hook_text_chars": len(hook["text"]), "source_version": "arXiv v2",
                  "overlap_draft_withheld": True, "live_ingestion_checked": False}))
