"""Read the installed gate and governor state; run only this tiny CPU check."""
import importlib.util
import json
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
support = ROOT / "gate_support"
support.mkdir(exist_ok=True)
source = Path("~/.claude/dreaming/compute_sense.py")
copy = support / "compute_sense_copy.py"
shutil.copyfile(source, copy)
spec = importlib.util.spec_from_file_location("w498_compute_sense_copy", copy)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
# Do not run main(): it writes the shared hook dedup file. The installed
# local GPU gate is a read-only predicate, and its source is unmodified.
command = ("python -X utf8 ~/brain_workers/w498/verify_math.py "
           "--gate-receipt ~/brain_workers/w498/COMPUTE_GATE.json")
denial = module._local_gpu_deny({
    "hook_event_name": "PreToolUse", "tool_name": "PowerShell",
    "cwd": str(ROOT), "tool_input": {"command": command},
})
state_file = Path(module.STATE_FILE)
state = json.loads(state_file.read_text(encoding="utf-8-sig"))
state_age = time.time() - state_file.stat().st_mtime
allowed = denial is None and 0 <= state_age <= module.STALE_SEC
receipt = {
    "observed_at": datetime.now(timezone.utc).isoformat(),
    "allowed": allowed,
    "installed_gate_source": str(source),
    "gate_function": "_local_gpu_deny, unchanged worker-local copy",
    "gpu_permission_denied": denial is not None,
    "governor_status": state.get("status"),
    "governor_state_age_seconds": state_age,
    "governor_max_age_seconds": module.STALE_SEC,
    "bounded_job": command,
    "limits": "standard library only; <=4096 candidate step words per geometry case; 20480 angular points; no GPU, DNN, models, parallel pool, or persistent process",
    "distress_policy": "Installed compute_sense prohibits new large/model-heavy work and permits continuing short-lived light work. This verification is bounded light work; no policy or service is changed.",
}
(ROOT / "COMPUTE_GATE.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, indent=2), flush=True)
if not allowed:
    raise SystemExit("Existing gate denied execution or governor snapshot is stale")
result = subprocess.run([sys.executable, "-X", "utf8", str(ROOT / "verify_math.py"),
                         "--gate-receipt", str(ROOT / "COMPUTE_GATE.json")],
                        cwd=ROOT, timeout=60, capture_output=True, text=True, encoding="utf-8")
print(result.stdout)
print(result.stderr)
raise SystemExit(result.returncode)
