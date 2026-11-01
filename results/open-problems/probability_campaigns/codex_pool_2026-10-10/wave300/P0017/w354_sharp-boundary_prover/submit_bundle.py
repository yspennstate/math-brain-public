import json
import os
import subprocess
import sys
from pathlib import Path

base = Path(__file__).resolve().parent
env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONUTF8="1")
command = [sys.executable, "-X", "utf8", "~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py", "assert", "--agent", "w354", "--resource", "~/math-brain-inbox/w354/bundle_001.json"]
result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace", env=env, timeout=40)
receipt = {"command": command, "exit_code": result.returncode, "stdout": result.stdout, "stderr": result.stderr}
(base / "SUBMISSION_LEASE_RECEIPT.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
print(json.dumps(receipt, indent=2))
if result.returncode:
    raise SystemExit("Refusing shared inbox write: covering lease assertion failed")
submitted = subprocess.run([sys.executable, "-X", "utf8", str(base / "build_bundle.py"), "--submit"], cwd=base, env=env, timeout=40)
raise SystemExit(submitted.returncode)
