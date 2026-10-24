"""One bounded recall, with worker-only writes and no model/network access."""
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
QUERY = "P0017 KLS log-concave Poincare proof mistakes"

if "--child" in sys.argv:
    import runpy
    import sqlite3
    os.environ.update({
        "BRAIN_GRAPH_LAMBDA": "0", "BRAIN_RECALL_LOG": "0",
        "BRAIN_RECALL_REFRESH": "0", "BRAIN_RECALL_QUERY_EMBED": "0",
        "BRAIN_OWNER_ADVISORY": "0", "PYTHONDONTWRITEBYTECODE": "1",
    })
    sys.dont_write_bytecode = True
    original_connect = sqlite3.connect
    def readonly_connect(database, *args, **kwargs):
        name = str(database)
        if name != ":memory:":
            if name.startswith("file:"):
                name = name.split("?", 1)[0] + "?mode=ro"
            else:
                name = "file:" + Path(name).resolve().as_posix() + "?mode=ro"
            kwargs["uri"] = True
        return original_connect(name, *args, **kwargs)
    sqlite3.connect = readonly_connect
    def inside(path):
        try:
            return Path(path).resolve().is_relative_to(ROOT)
        except (TypeError, ValueError):
            return False
    def guard(event, args):
        if event == "open":
            path, mode, flags = args
            writing = (isinstance(mode, str) and any(c in mode for c in "wax+")) or (
                isinstance(flags, int) and flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC))
            if writing and not isinstance(path, int) and not inside(path):
                raise PermissionError("recall worker-only write guard")
        if event in ("os.remove", "os.rmdir"):
            raise PermissionError("no deletion authorized")
        if event in ("os.mkdir", "os.rename", "os.replace") and not all(inside(x) for x in args[:2] if isinstance(x, (str, bytes))):
            raise PermissionError("recall worker-only mutation guard")
        if event in ("socket.connect", "subprocess.Popen"):
            raise PermissionError("recall network/model subprocess disabled")
        if event == "import" and str(args[0]).split(".")[0] in {"torch", "transformers", "sentence_transformers", "tensorflow", "onnxruntime"}:
            raise ImportError("model loading disabled for bounded recall")
    sys.addaudithook(guard)
    sys.path.insert(0, "~/.claude/dreaming")
    sys.argv = ["~/.claude/dreaming/brain.py", "recall", QUERY, "-n", "3"]
    runpy.run_path(sys.argv[0], run_name="__main__")
else:
    started = time.monotonic()
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    receipt = {"query": QUERY, "timeout_seconds": 60, "writes": "worker folder only", "sqlite": "disk stores read-only", "models": "disabled"}
    try:
        result = subprocess.run([sys.executable, "-X", "utf8", str(Path(__file__).resolve()), "--child"], capture_output=True, text=True, encoding="utf-8", timeout=60, env=env)
        output = result.stdout + result.stderr
        receipt.update(status="completed" if result.returncode == 0 else "failed", exit_code=result.returncode)
    except subprocess.TimeoutExpired as exc:
        output = (exc.stdout or b"").decode("utf-8", errors="replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
        receipt.update(status="timed_out", fallback="Targeted MEMORY.md lookup and the two explicitly cited scar files.")
    receipt["elapsed_seconds"] = time.monotonic() - started
    (ROOT / "RECALL_REPORT.txt").write_text(output, encoding="utf-8")
    (ROOT / "RECALL_RECEIPT.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt))
