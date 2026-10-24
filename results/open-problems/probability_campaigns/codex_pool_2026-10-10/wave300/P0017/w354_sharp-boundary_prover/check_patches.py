import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

base = Path(__file__).resolve().parent
receipts = []
for name in ("01_p0017_draft_bundle.diff", "02_conditional_energy_hook.diff"):
    command = ["git", "apply", "--check", "-p4", "--directory=patch_check", str(base / "patches" / name)]
    result = subprocess.run(command, cwd=base, capture_output=True, text=True, timeout=30)
    receipts.append({"patch": name, "command": command, "exit_code": result.returncode, "stdout": result.stdout, "stderr": result.stderr, "mutation": False})
(base / "PATCH_VALIDATION.json").write_text(json.dumps({"checked_at": datetime.now(timezone.utc).isoformat(), "receipts": receipts}, indent=2), encoding="utf-8")
print(json.dumps(receipts, indent=2))
raise SystemExit(any(row["exit_code"] != 0 for row in receipts))
