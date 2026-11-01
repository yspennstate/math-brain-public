"""Summarize assigned, completed, and pending Team O rows without opening test material."""

import json
from pathlib import Path

base = Path("~/brain_workers")
audit_dir = base / "w346" / "audits"
for number in range(330, 346):
    worker = f"w{number}"
    root = base / worker
    source = root / ("RESULT_ROWS.jsonl" if (root / "RESULT_ROWS.jsonl").exists() else "results.jsonl")
    if not source.exists():
        continue
    rows = [json.loads(s) for s in source.read_text(encoding="utf-8-sig").splitlines() if s.strip()]
    assigned = [r for r in rows if "w346" in str(r.get("audit_status", "")).lower()
                and r.get("label") != "audit verdict"]
    verdict_path = audit_dir / f"{worker}.jsonl"
    verdicts = [json.loads(s) for s in verdict_path.read_text(encoding="utf-8").splitlines() if s.strip()] if verdict_path.exists() else []
    audited_ids = {v.get("row_id") or v.get("id") for v in verdicts}
    pending = [(r.get("row_id") or r.get("id")) for r in assigned if (r.get("row_id") or r.get("id")) not in audited_ids]
    if assigned:
        print(worker, "assigned", len(assigned), "audited", len(assigned) - len(pending), "pending", len(pending), pending)
