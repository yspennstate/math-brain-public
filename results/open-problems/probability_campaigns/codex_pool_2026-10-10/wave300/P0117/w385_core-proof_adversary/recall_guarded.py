"""Foreground recall with a cooperative deadline and no live writes or children."""
import contextlib
import io
import json
import os
from pathlib import Path
import runpy
import sqlite3
import sys
import time

ROOT = Path(__file__).resolve().parent
QUERY = "P0117 planar iid FPP bigeodesics proof audit mistakes"
sys.dont_write_bytecode = True
started = time.monotonic()

class RecallDeadline(BaseException):
    pass

def trace(frame, event, arg):
    if time.monotonic() - started > 60:
        raise RecallDeadline("60-second cooperative recall budget exhausted")
    return trace

def audit(event, args):
    if event == "open":
        path, mode, flags = args
        writable = (isinstance(mode, str) and any(c in mode for c in "wax+")) or bool(flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC))
        if writable and not isinstance(path, int):
            target = Path(path).resolve()
            if not target.is_relative_to(ROOT):
                raise PermissionError("worker recall forbids writes outside worker folder")
    if event in {"os.remove", "os.rmdir", "subprocess.Popen", "os.system", "os.kill"}:
        raise PermissionError("worker recall forbids removal, processes, and signals")
    if event in {"os.mkdir", "os.rename"}:
        for value in args[:2 if event == "os.rename" else 1]:
            if not Path(value).resolve().is_relative_to(ROOT):
                raise PermissionError("worker recall forbids live filesystem mutation")
    if event == "sqlite3.connect":
        database = str(args[0])
        if not database.startswith("file:") or "mode=ro" not in database:
            raise PermissionError("worker recall permits only read-only SQLite connections")

log = io.StringIO()
result = {"query": QUERY, "command": "python -X utf8 recall_guarded.py", "underlying_command": "python -X utf8 ~/.claude/dreaming/brain.py recall QUERY -n 3", "live_writes": "blocked", "child_processes": "blocked"}
sys.addaudithook(audit)
sys.argv = ["~/.claude/dreaming/brain.py", "recall", QUERY, "-n", "3"]
sys.path.insert(0, "~/.claude/dreaming")
try:
    sys.settrace(trace)
    with contextlib.redirect_stdout(log), contextlib.redirect_stderr(log):
        runpy.run_path(sys.argv[0], run_name="__main__")
    result["status"] = "returned"
except SystemExit as exc:
    result.update(status="returned", exit_code=exc.code)
except RecallDeadline as exc:
    result.update(status="timeout", reason=str(exc))
except BaseException as exc:
    result.update(status="unavailable", reason=f"{type(exc).__name__}: {exc}")
finally:
    sys.settrace(None)
result["elapsed_seconds"] = round(time.monotonic() - started, 3)
(ROOT / "recall_result.txt").write_text(log.getvalue(), encoding="utf-8")
(ROOT / "recall_receipt.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))
