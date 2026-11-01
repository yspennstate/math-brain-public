"""Read local governor state only; run the bounded exact check only if fresh and clear."""
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys
import time

root = Path(__file__).resolve().parent
state_path = Path("~/.claude/compute/compute_state.json")
started = time.time()
state = json.loads(state_path.read_text(encoding="utf-8-sig"))
age = started - state_path.stat().st_mtime
# Remote/trading fields are deliberately excluded from this local CPU-only receipt.
selected = {key: value for key, value in state.items() if (
    key in {"status", "mode", "reasons", "ts"}
    or key.startswith(("cpu", "physical", "ram", "commit", "disk", "hung"))
)}
reasons = state.get("reasons") or []
if isinstance(reasons, str):
    reasons = [reasons]
pressure = [str(x) for x in reasons if any(t in str(x).lower() for t in (
    "commit", "physical", "memory", "ram_", "disk", "hung", "critical", "cpu", "distress", "stop"
))]
status = str(state.get("status", "")).lower()
timestamp = state.get("ts")
timestamp_age = None
if timestamp:
    try:
        stamped = datetime.fromisoformat(str(timestamp).replace("Z", "+00:00"))
        if stamped.tzinfo is None:
            stamped = stamped.astimezone()
        timestamp_age = started - stamped.timestamp()
    except (ValueError, TypeError):
        pass
allowed = (0 <= age <= 60 and timestamp_age is not None and 0 <= timestamp_age <= 60
           and status not in {"distress", "critical", "stop", "stopped"} and not pressure)
receipt = {"read_at_utc": datetime.now(timezone.utc).isoformat(),
           "file_age_seconds": round(age, 3), "state_timestamp_age_seconds": timestamp_age,
           "local_fields": selected, "pressure_reasons": pressure, "allowed": allowed,
           "job": "1020 rational finite recurrences; 28 tiny explicit edge-enumerations; one Python process; no models, GPU or remote compute"}
(root / "compute_gate.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, indent=2))
if not allowed:
    print("HOLD: finite computation was not launched; no gate was weakened.")
    sys.exit(2)
subprocess.run([sys.executable, "-X", "utf8", str(root / "verify_boundary.py")], cwd=root, check=True, timeout=45)
