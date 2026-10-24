"""Run the required narrow recall without permitting any live filesystem/store write."""
import os
import runpy
import sqlite3
import sys
import threading
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
def audit(event, args):
    if event == "open":
        path, mode, flags = args
        writes = bool(flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND))
        if writes:
            try:
                allowed = Path(path).resolve().is_relative_to(ROOT)
            except (TypeError, ValueError):
                allowed = False
            if not allowed:
                raise PermissionError("w505 recall is read-only outside its worker folder")
    if event in {"os.remove", "os.rmdir", "os.rename", "os.mkdir", "subprocess.Popen", "os.system"}:
        raise PermissionError("w505 read-only recall blocks filesystem mutations and child processes")
    if event == "sqlite3.connect":
        database = str(args[0])
        if "mode=ro" not in database:
            raise PermissionError("w505 permits only explicit read-only SQLite connections")
sys.addaudithook(audit)
script = "~/.claude/dreaming/brain.py"
sys.path.insert(0, str(Path(script).parent))
sys.argv = [script, "recall", "P0162 Fourier entropy influence restriction proof mistakes", "-n", "3"]
timer = threading.Timer(60, lambda: (sys.stderr.write("w505 recall timeout 60s\n"), sys.stderr.flush(), os._exit(124)))
timer.daemon = True
timer.start()
try:
    runpy.run_path(script, run_name="__main__")
finally:
    timer.cancel()
