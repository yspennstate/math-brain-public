"""Foreground, read-only resource receipt for a six-row closed-form calculation."""
import json
from pathlib import Path
import time

root = Path(__file__).resolve().parent
path = Path("~/.claude/compute/compute_state.json")
receipt = {"operation": "six stdlib closed-form scalar evaluations; no simulation, training, GPU or background process"}
if path.exists():
    state = json.loads(path.read_text(encoding="utf-8-sig"))
    receipt["state_age_seconds"] = time.time() - path.stat().st_mtime
    receipt["state_fields"] = {key: state[key] for key in ("timestamp", "updated_at", "status", "mode", "commit_used_pct", "commit_avail_mb", "deny_heavy", "allow_light") if key in state}
    receipt["fresh"] = receipt["state_age_seconds"] <= 60
else:
    receipt.update(fresh=False, reason="resource-state file unavailable")
(root / "compute_gate_receipt.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
print(json.dumps(receipt))
