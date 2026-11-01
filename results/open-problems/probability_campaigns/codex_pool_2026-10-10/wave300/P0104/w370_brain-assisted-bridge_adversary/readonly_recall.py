"""Bounded brain.py recall, forbidding live writes and network/model subprocesses."""
import contextlib
import io
import json
import os
from pathlib import Path
import runpy
import sys
import threading
import time

ROOT = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
blocked = []

def inside(path):
    try:
        return Path(path).resolve().is_relative_to(ROOT)
    except (TypeError, ValueError):
        return False

def audit(event, args):
    if event == "open":
        path, mode, flags = args
        mutates = (isinstance(mode, str) and any(x in mode for x in "wax+")) or (isinstance(flags, int) and flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND))
        if mutates and not inside(path):
            blocked.append({"event": event, "path": str(path)})
            raise PermissionError("w370 read-only recall forbids writes outside worker folder")
    elif event in {"os.mkdir", "os.remove", "os.rmdir", "os.rename", "os.replace", "os.chmod", "os.utime"}:
        if not inside(args[0]) or (event in {"os.rename", "os.replace"} and not inside(args[1])):
            blocked.append({"event": event, "path": str(args[0])})
            raise PermissionError("w370 read-only recall forbids live filesystem mutation")
    elif event == "sqlite3.connect":
        name = str(args[0])
        if not inside(name) and not (name.startswith("file:") and "mode=ro" in name):
            blocked.append({"event": event, "path": name})
            raise PermissionError("w370 requires mode=ro SQLite connections")
    elif event in {"subprocess.Popen", "os.system", "socket.connect", "socket.connect_ex"}:
        blocked.append({"event": event})
        raise PermissionError("w370 recall forbids subprocesses and network")

sys.addaudithook(audit)
query = "P0104 first passage percolation KPZ fluctuation exponents mistakes"
buffer = io.StringIO()
result = {"query": query, "budget_seconds": 60, "mode": "live recall code with read-only audit guard", "new_theorem_proof": False}

def work():
    try:
        sys.argv = ["brain.py", "recall", query, "-n", "3"]
        with contextlib.redirect_stdout(buffer), contextlib.redirect_stderr(buffer):
            runpy.run_path("~/.claude/dreaming/brain.py", run_name="__main__")
        result["status"] = "completed"
    except SystemExit as exc:
        result["status"] = "completed" if exc.code in (None, 0) else "error"
        result["exit_code"] = exc.code
    except BaseException as exc:
        result["status"] = "error"
        result["error"] = type(exc).__name__ + ": " + str(exc)

started = time.perf_counter()
worker = threading.Thread(target=work, daemon=True)
worker.start()
worker.join(60)
result["elapsed_seconds"] = round(time.perf_counter() - started, 3)
if worker.is_alive():
    result["status"] = "timed_out"
result["blocked_mutations"] = blocked
(ROOT / "recall_output.txt").write_text(buffer.getvalue(), encoding="utf-8")
(ROOT / "recall_measurement.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
# sys.__stdout__ also works if the daemon's redirect context is still active.
print(json.dumps(result), file=sys.__stdout__, flush=True)
