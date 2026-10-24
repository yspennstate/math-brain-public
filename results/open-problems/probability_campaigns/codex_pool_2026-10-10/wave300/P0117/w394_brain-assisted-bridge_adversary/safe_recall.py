"""Bounded brain recall with all external writes, network, and child launches denied."""
from pathlib import Path
import json
import os
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
QUERY = "P0117 planar iid first passage percolation bigeodesic adaptive endpoints mistakes"

def child():
    sys.dont_write_bytecode = True
    def guard(event, args):
        if event == "open":
            path, mode, flags = args
            writing = (isinstance(mode, str) and any(x in mode for x in "wax+")) or bool(
                isinstance(flags, int) and flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND))
            if writing and not isinstance(path, int):
                target = Path(path).resolve()
                if not target.is_relative_to(ROOT):
                    raise PermissionError("w394 recall forbids writes outside worker folder")
        elif event == "sqlite3.connect":
            database = str(args[0])
            if "mode=ro" not in database:
                raise PermissionError("w394 requires a read-only SQLite URI")
        elif event in {"os.remove", "os.rmdir", "os.rename", "os.mkdir", "subprocess.Popen", "socket.connect"}:
            raise PermissionError("w394 recall forbids mutation, subprocesses, and network")
    sys.addaudithook(guard)
    import runpy
    brain = "~/.claude/dreaming/brain.py"
    sys.path.insert(0, str(Path(brain).parent))
    sys.argv = [brain, "recall", QUERY, "-n", "3"]
    runpy.run_path(brain, run_name="__main__")

def parent():
    reports = ROOT / "reports"
    reports.mkdir(exist_ok=True)
    start = time.perf_counter()
    timed_out = False
    try:
        result = subprocess.run([sys.executable, "-X", "utf8", str(Path(__file__)), "--child"],
                                capture_output=True, timeout=60, check=False)
        out, err, rc = result.stdout, result.stderr, result.returncode
    except subprocess.TimeoutExpired as exc:
        timed_out = True
        out, err, rc = exc.stdout or b"", exc.stderr or b"", None
    (reports / "brain_recall_mistakes.md").write_text(out.decode("utf-8", errors="replace"), encoding="utf-8")
    (reports / "brain_recall_stderr.md").write_text(err.decode("utf-8", errors="replace"), encoding="utf-8")
    measurement = {"query": QUERY, "requested_top_k": 3, "timeout_seconds": 60,
                   "timed_out": timed_out, "elapsed_seconds": round(time.perf_counter()-start, 3),
                   "returncode": rc, "external_writes_denied": True,
                   "command": "python -X utf8 safe_recall.py",
                   "fallback_slug": "perceptron_proof_open_gaps_fleet_2026_07_12"}
    (reports / "brain_recall_measurement.json").write_text(json.dumps(measurement, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(measurement))
    print(out.decode("utf-8", errors="replace")[:5200])
    if err: print(err.decode("utf-8", errors="replace")[-1800:])

if __name__ == "__main__":
    child() if "--child" in sys.argv else parent()
