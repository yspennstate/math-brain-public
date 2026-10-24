"""Invoke the prescribed recall with a cooperative deadline and no live writes."""
import contextlib
import io
import json
import os
from pathlib import Path
import runpy
import sys
import time

ROOT = Path(__file__).resolve().parent
blocked = []


def guard(event, args):
    if event == "open":
        path, mode, flags = args
        writing = (isinstance(mode, str) and any(c in mode for c in "wax+")) or (flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND))
        if writing and isinstance(path, (str, bytes, os.PathLike)):
            resolved = Path(os.fsdecode(path)).resolve()
            if not resolved.is_relative_to(ROOT):
                blocked.append({"event": event, "path": str(resolved)})
                raise PermissionError("w356 recall is read-only outside its folder")
    if event == "sqlite3.connect":
        database = str(args[0])
        if not (database.startswith("file:") and "mode=ro" in database):
            blocked.append({"event": event, "reason": "connection was not explicitly mode=ro"})
            raise PermissionError("live sqlite must be explicitly read-only")
    if event in ("subprocess.Popen", "os.system", "socket.connect", "os.remove", "os.rename", "os.rmdir", "os.mkdir"):
        blocked.append({"event": event})
        raise PermissionError("recall may not spawn, network, or mutate live paths")


def main():
    sys.dont_write_bytecode = True
    sys.addaudithook(guard)
    os.environ.pop("BRAIN_RECALL_DUMP_SCORED", None)
    output = io.StringIO()
    deadline = time.monotonic() + 60
    def trace(frame, event, arg):
        if time.monotonic() > deadline:
            raise TimeoutError("60 second cooperative recall deadline")
        return trace
    result = {"command": 'python -X utf8 brain.py recall "P0017 KLS isotropic conditional fibers referee mistakes" -n 3',
              "deadline_seconds": 60, "top_requested": 3}
    sys.argv = ["~/.claude/dreaming/brain.py", "recall", "P0017 KLS isotropic conditional fibers referee mistakes", "-n", "3"]
    sys.path.insert(0, "~/.claude/dreaming")
    begun = time.monotonic()
    try:
        sys.settrace(trace)
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            runpy.run_path(sys.argv[0], run_name="__main__")
        result["outcome"] = "completed"
    except SystemExit as exc:
        result["outcome"] = "completed" if exc.code in (0, None) else "failed"
        result["exit_code"] = exc.code
    except (TimeoutError, Exception) as exc:
        result["outcome"] = "fallback required"
        result["error"] = type(exc).__name__ + ": " + str(exc)
    finally:
        sys.settrace(None)
    result["elapsed_seconds"] = time.monotonic() - begun
    result["blocked_operations"] = blocked
    (ROOT / "RECALL_RECEIPT.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    (ROOT / "RECALL_OUTPUT.txt").write_text(output.getvalue(), encoding="utf-8")
    print(json.dumps(result, indent=2))
    print(output.getvalue()[:6500])


if __name__ == "__main__":
    main()
