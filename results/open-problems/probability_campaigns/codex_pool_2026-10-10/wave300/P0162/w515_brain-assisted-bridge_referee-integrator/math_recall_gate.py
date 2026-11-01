"""Bounded read-only math-brain recall receipt for P0162."""
import json
import os
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
QUERY = "P0162 Fourier entropy influence Boolean constraint Han correction bridge"
STORE = "~/math-brain-build/local/population/brain.sqlite3"


def guard(event, args):
    if event == "open":
        path, mode, flags = args
        writing = (isinstance(mode, str) and any(c in mode for c in "wax+")) or (isinstance(flags, int) and flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND))
        if writing and isinstance(path, (str, bytes, os.PathLike)) and not Path(os.fsdecode(path)).resolve().is_relative_to(HERE):
            raise PermissionError("external write forbidden")
    if event == "sqlite3.connect":
        name = str(args[0])
        if name != ":memory:" and not (name.startswith("file:") and "mode=ro" in name):
            raise PermissionError("sqlite connection must be read-only")


if "--child" in sys.argv:
    sys.dont_write_bytecode = True
    sys.addaudithook(guard)
    sys.path.insert(0, "~/math-brain-build/src")
    from math_brain.cli import main
    raise SystemExit(main(["recall", STORE, QUERY, "--limit", "8"]))

start = time.perf_counter()
try:
    p = subprocess.run([sys.executable, "-B", "-X", "utf8", str(Path(__file__).resolve()), "--child"], capture_output=True, text=True, encoding="utf-8", timeout=60)
    result = {"returncode": p.returncode, "stdout": p.stdout, "stderr": p.stderr, "timed_out": False}
except subprocess.TimeoutExpired as exc:
    decode = lambda x: x.decode("utf-8", errors="replace") if isinstance(x, bytes) else (x or "")
    result = {"returncode": None, "stdout": decode(exc.stdout), "stderr": decode(exc.stderr), "timed_out": True}
result.update(query=QUERY, command="python -X utf8 math_recall_gate.py", seconds=time.perf_counter()-start)
(HERE / "MATH_RECALL_RECEIPT.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in result.items() if k not in ("stdout", "stderr")}))
print(result["stdout"][:12000])
print(result["stderr"][:1000])
