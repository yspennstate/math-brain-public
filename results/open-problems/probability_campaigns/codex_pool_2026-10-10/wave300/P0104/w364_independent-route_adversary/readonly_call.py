"""Run the named recall/read operation with mutation and child-process guards.

This is a local task helper, not a proposed live recall-engine change. The 60-second
budget raises in this Python process; it does not kill any other process.
"""
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
sys.dont_write_bytecode = True
os.environ["BRAIN_RECALL_REFRESH"] = "0"
os.environ["BRAIN_RECALL_GRAPH_LANE"] = "0"
os.environ["BRAIN_RECALL_QUERY_SEMANTIC"] = "0"
os.environ["BRAIN_RECALL_QUERY_EMBED"] = "0"
os.environ["BRAIN_RECALL_USAGE"] = "0"
os.environ.pop("BRAIN_RECALL_DUMP_SCORED", None)
started = time.monotonic()
deadline = started + 60
denied = []


def audit(event, args):
    reason = None
    if event == "open":
        path, mode, flags = args
        writing = (isinstance(mode, str) and any(c in mode for c in "wax+")) or (
            isinstance(flags, int) and flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC)
        )
        if writing and not isinstance(path, int):
            target = Path(path).resolve()
            if target != ROOT and ROOT not in target.parents:
                reason = "external-file mutation blocked"
    elif event in {"os.remove", "os.rmdir", "os.rename", "os.mkdir", "os.truncate"}:
        reason = "filesystem mutation disabled during the read call"
    elif event == "sqlite3.connect":
        db = str(args[0])
        if not (db.startswith("file:") and "mode=ro" in db):
            reason = "non-read-only SQLite connection blocked"
    elif event in {"subprocess.Popen", "os.system", "os.exec", "os.spawn"}:
        reason = "child processes disabled"
    elif event == "socket.connect":
        reason = "network disabled for the local read call"
    elif event == "import" and str(args[0]).split(".")[0] in {"torch", "transformers", "sentence_transformers"}:
        reason = "model loading disabled"
    if reason:
        denied.append({"event": event, "reason": reason})
        raise PermissionError(reason)


real_connect = sqlite3.connect


def connect_readonly(database, *args, **kwargs):
    db = str(database)
    if not db.startswith("file:"):
        db = "file:" + Path(db).resolve().as_posix() + "?mode=ro"
    elif "mode=ro" not in db:
        raise PermissionError("SQLite URI lacks mode=ro")
    kwargs["uri"] = True
    connection = real_connect(db, *args, **kwargs)
    connection.execute("PRAGMA query_only=ON")
    return connection


sqlite3.connect = connect_readonly
sys.addaudithook(audit)


def trace(frame, event, arg):
    if time.monotonic() > deadline:
        raise TimeoutError("60-second read-call budget exceeded")
    return trace


mode = sys.argv[1]
if mode == "brain":
    script = Path("~/.claude/dreaming/brain.py")
    args = [str(script), "recall", "P0104 first passage percolation proof conditioning mistakes", "-n", "3"]
elif mode == "team":
    script = Path("~/<private-repo>/12_cognitive_architecture/agent_mesh/team_comm.py")
    args = [str(script), "read", "--as", "w364", "--peek", "--max", "8"]
else:
    raise ValueError("Expected brain or team")
sys.path.insert(0, str(script.parent))
sys.argv = args
captured = io.StringIO()
error = None
try:
    sys.settrace(trace)
    with contextlib.redirect_stdout(captured), contextlib.redirect_stderr(captured):
        runpy.run_path(str(script), run_name="__main__")
except SystemExit as exc:
    if exc.code not in (None, 0):
        error = "SystemExit " + str(exc.code)
except Exception as exc:
    error = type(exc).__name__ + ": " + str(exc)
finally:
    sys.settrace(None)
output = captured.getvalue()
(ROOT / (mode + "_read.txt")).write_text(output, encoding="utf-8")
receipt = {
    "mode": mode,
    "command": args,
    "elapsed_seconds": time.monotonic() - started,
    "error": error,
    "denied_operations": denied,
    "output_file": mode + "_read.txt",
    "sqlite_connections": "mode=ro plus query_only",
    "mutations_outside_worker": 0,
}
(ROOT / (mode + "_read_receipt.json")).write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, indent=2))
print(output[:6500])
