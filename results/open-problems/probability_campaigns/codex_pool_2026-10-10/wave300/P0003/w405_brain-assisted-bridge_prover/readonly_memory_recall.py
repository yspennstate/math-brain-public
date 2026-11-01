from __future__ import annotations
import contextlib, io, json, os, runpy, sys, time
from pathlib import Path
ROOT = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
deadline = time.monotonic() + 55.0
blocked = []
def audit(event, args):
    if time.monotonic() > deadline:
        raise TimeoutError("55-second read-only recall deadline")
    if event in {"subprocess.Popen", "os.system", "os.startfile", "os.remove", "os.rmdir", "os.rename"}:
        blocked.append({"event": event})
        raise PermissionError("Worker recall cannot spawn, delete, or mutate shared files")
    if event == "open":
        path, mode, flags = args
        if isinstance(path, (str, bytes, os.PathLike)):
            p = Path(os.fsdecode(path)).resolve()
            write = any(c in (mode or "") for c in "wax+") or bool(flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND))
            if write and not p.is_relative_to(ROOT):
                blocked.append({"event": event, "path": str(p)})
                raise PermissionError("write outside w405 denied")
            low = str(p).replace("\\", "/").lower()
            if "/.ssh/" in low or p.name.lower() in {"auth.json", ".env", "rclone.conf"} or p.suffix.lower() in {".pem", ".key"} or p.name.lower().startswith("client_secret"):
                raise PermissionError("forbidden secret path")
    if event == "sqlite3.connect":
        db = str(args[0])
        if db != ":memory:" and "mode=ro" not in db:
            blocked.append({"event": event})
            raise PermissionError("SQLite must be mode=ro")
def tracer(frame, event, arg):
    if time.monotonic() > deadline:
        raise TimeoutError("55-second read-only recall deadline")
    return tracer
os.environ["BRAIN_RECALL_REFRESH"] = "0"
os.environ["BRAIN_RECALL_DUMP_SCORED"] = str(ROOT / "memory_recall_scores.json")
sys.addaudithook(audit)
sys.settrace(tracer)
buf = io.StringIO()
started = time.monotonic()
rc, failure = 0, None
try:
    sys.argv = ["brain.py", "recall", "P0003 self-avoiding walk scaling limit proof mistakes", "-n", "3"]
    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
        runpy.run_path("~/.claude/dreaming/brain.py", run_name="__main__")
except SystemExit as exc:
    rc = exc.code or 0
except Exception as exc:
    rc, failure = 2, type(exc).__name__ + ": " + str(exc)
finally:
    deadline = float("inf")
    sys.settrace(None)
receipt = {"command": "python -B -X utf8 readonly_memory_recall.py", "query": "P0003 self-avoiding walk scaling limit proof mistakes", "max_results": 3, "deadline_seconds": 55, "elapsed_seconds": round(time.monotonic()-started,3), "exit_code": rc, "failure": failure, "blocked_side_effects": blocked, "stdout": buf.getvalue(), "mode": "live recall code, process-local refresh disabled and audit guard; not a live-performance benchmark"}
(ROOT / "MEMORY_RECALL_RECEIPT.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({k:v for k,v in receipt.items() if k!="stdout"}, ensure_ascii=False))
print(receipt["stdout"][-4500:])
