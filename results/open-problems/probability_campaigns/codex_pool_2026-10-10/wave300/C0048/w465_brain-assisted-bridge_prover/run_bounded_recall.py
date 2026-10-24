"""Run only authorized foreground, read-only recall; save bounded evidence locally."""
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent

def run(label, command, seconds=60, env_extra=None):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONIOENCODING="utf-8")
    env.update(env_extra or {})
    start = time.perf_counter()
    try:
        process = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=seconds, env=env, cwd=ROOT)
        result = {"label": label, "command": command, "elapsed_seconds": time.perf_counter()-start, "returncode": process.returncode, "timeout": False, "process_env_overrides": env_extra or {}, "stdout": process.stdout, "stderr": process.stderr}
    except subprocess.TimeoutExpired as error:
        decode = lambda v: v.decode("utf-8", "replace") if isinstance(v, bytes) else (v or "")
        result = {"label": label, "command": command, "elapsed_seconds": time.perf_counter()-start, "timeout": True, "process_env_overrides": env_extra or {}, "stdout": decode(error.stdout), "stderr": decode(error.stderr)}
    out = ROOT / "evidence"
    out.mkdir(exist_ok=True)
    (out / (label + ".json")).write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({k:v for k,v in result.items() if k not in {"stdout","stderr"}}, ensure_ascii=False), flush=True)
    print(result["stdout"][:16000], flush=True)
    print(result["stderr"][:1500], flush=True)
    return result

if __name__ == "__main__":
    run("memory_recall", [sys.executable, "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", "C0048 Potts nearest-neighbor critical discontinuity proof mistakes", "-n", "3"], env_extra={"BRAIN_RECALL_LOG":"0", "BRAIN_GRAPH_LAMBDA":"0", "BRAIN_RECALL_QUERY_EMBED":"0"})
