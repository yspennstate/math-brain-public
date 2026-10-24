"""One time-bounded read-only recall; logs only in w399, without model loads."""
import json
import os
from pathlib import Path
import runpy
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
QUERY = "P0003 honeycomb self avoiding walk scaling limit proof mistakes"

def inside(path):
    try:
        Path(path).resolve().relative_to(ROOT)
        return True
    except (TypeError, ValueError, OSError):
        return False

def guard(event, args):
    if event == "open":
        path, mode, flags = args
        writing = (isinstance(mode, str) and any(c in mode for c in "wax+")) or bool(flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND))
        if writing and not inside(path):
            raise PermissionError("w399 recall denies writes outside worker folder")
    elif event in {"os.mkdir", "os.remove", "os.rmdir", "os.unlink", "os.rename"}:
        paths = args[:2] if event == "os.rename" else args[:1]
        if any(isinstance(p, (str, bytes, os.PathLike)) and not inside(p) for p in paths):
            raise PermissionError("w399 recall denies filesystem mutation outside worker folder")
    elif event == "sqlite3.connect":
        db = str(args[0])
        if not db.startswith("file:") or "mode=ro" not in db:
            raise PermissionError("w399 recall requires read-only sqlite URI")
    elif event in {"subprocess.Popen", "os.system", "socket.connect"}:
        raise PermissionError("w399 recall denies child processes and network")
    elif event == "import" and str(args[0]).split(".")[0] in {"torch", "transformers", "sentence_transformers"}:
        raise PermissionError("w399 recall denies model loaders")

if "--child" in sys.argv:
    sys.dont_write_bytecode = True
    os.environ["BRAIN_RECALL_LOG"] = "0"
    sys.addaudithook(guard)
    sys.path.insert(0, "~/.claude/dreaming")
    sys.argv = ["brain.py", "recall", QUERY, "-n", "3"]
    runpy.run_path("~/.claude/dreaming/brain.py", run_name="__main__")
else:
    started = time.monotonic()
    cmd = [sys.executable, "-B", "-X", "utf8", str(Path(__file__).resolve()), "--child"]
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", BRAIN_RECALL_LOG="0")
    try:
        completed = subprocess.run(cmd, cwd=ROOT, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
        result = {"command": cmd, "query": QUERY, "exit_code": completed.returncode, "timed_out": False, "stdout": completed.stdout, "stderr": completed.stderr}
    except subprocess.TimeoutExpired as exc:
        def decode(value):
            return value.decode("utf-8", "replace") if isinstance(value, bytes) else (value or "")
        result = {"command": cmd, "query": QUERY, "exit_code": None, "timed_out": True, "stdout": decode(exc.stdout), "stderr": decode(exc.stderr), "fallback": "Named proof scars already read directly; grep MEMORY.md then use those exact cited slugs."}
    result["elapsed_seconds"] = round(time.monotonic() - started, 3)
    (ROOT / "RECALL_RESULT.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
