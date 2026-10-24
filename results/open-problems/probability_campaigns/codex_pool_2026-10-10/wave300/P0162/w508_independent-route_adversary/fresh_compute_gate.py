"""Read current local governor metrics and save a strict bounded-check receipt."""
import json
import time
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parent
source = Path("~/.claude/compute/compute_state.json")
state = json.loads(source.read_text(encoding="utf-8-sig"))
now = time.time()
data_time = datetime.fromisoformat(state["ts"]).astimezone().timestamp()
age = now - data_time
metrics = {key: state.get(key) for key in (
    "ts", "status", "mode", "cpu_pct", "mem_avail_mb", "commit_used_pct",
    "commit_avail_mb", "commit_eff_used_pct", "commit_eff_avail_mb")}
known = all(isinstance(state.get(key), (int, float)) for key in
            ("cpu_pct", "mem_avail_mb", "commit_eff_used_pct", "commit_eff_avail_mb"))
allowed = (known and 0 <= age <= 60 and state.get("status") in ("ok", "normal", "healthy")
           and state.get("mode") in ("normal", "allow", "healthy", "owner_present_polite", "owner_away_open")
           and state["cpu_pct"] <= 95 and state["mem_avail_mb"] >= 256
           and state["commit_eff_used_pct"] < 85 and state["commit_eff_avail_mb"] >= 16384)
receipt = {"checked_epoch": now, "checked_utc": datetime.now(timezone.utc).isoformat(),
           "governor_path": str(source), "governor_data_age_seconds": age,
           "local_metrics": metrics, "bounded_cpu_check_allowed": allowed,
           "limits": {"max_truth_table_atoms": 2048, "max_seconds": 45,
                      "gpu": False, "parallel_workers": 1},
           "policy": "Fail closed on stale telemetry, non-normal governor state or commit warning; no resource controls changed."}
path = root / "COMPUTE_GATE.json"
path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt))
