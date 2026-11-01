import json
import os
from pathlib import Path
import subprocess
import sys
import time

root = Path(__file__).resolve().parent
start = time.monotonic()
env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONUTF8="1")
try:
    r = subprocess.run(
        [sys.executable, "-X", "utf8", "~/.claude/dreaming/brain.py", "recall",
         "C0052 three dimensional Ising non-Gaussian scaling proof mistakes"],
        capture_output=True, text=True, encoding="utf-8", timeout=60, env=env,
    )
    result = {"exit_code": r.returncode, "stdout": r.stdout, "stderr": r.stderr[:2000]}
except subprocess.TimeoutExpired:
    result = {"status": "RECALL_TIMEOUT_60S", "fallback": "targeted memory index and named scar"}
result["seconds"] = time.monotonic() - start
(root / "recall_receipt.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(result, ensure_ascii=False)[:14000])
