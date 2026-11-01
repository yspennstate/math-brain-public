"""Run the requested live recall with an external-write guard and 60-second cap."""
import json
import os
from pathlib import Path
import runpy
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
QUERY = "C0017 conformal invariance square lattice bond percolation proof mistakes"

def guarded_recall():
    sys.dont_write_bytecode = True
    def guard(event, args):
        if event == "open":
            path, mode, flags = args
            writes = (isinstance(mode, str) and any(c in mode for c in "wax+")) or (
                isinstance(flags, int) and flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND)
            )
            if writes and not isinstance(path, int) and not Path(path).resolve().is_relative_to(ROOT):
                raise PermissionError("w411 recall guard: external write denied")
        elif event == "sqlite3.connect":
            if "mode=ro" not in str(args[0]):
                raise PermissionError("w411 recall guard: SQLite must be read-only")
        elif event in ("os.remove", "os.rmdir", "os.rename", "os.mkdir"):
            raise PermissionError("w411 recall guard: filesystem mutation denied")
    sys.addaudithook(guard)
    brain = Path("~/.claude/dreaming/brain.py")
    sys.path.insert(0, str(brain.parent))
    sys.argv = [str(brain), "recall", QUERY, "-n", "3"]
    runpy.run_path(str(brain), run_name="__main__")

if __name__ == "__main__":
    if "--child" in sys.argv:
        guarded_recall()
    else:
        started = time.monotonic()
        try:
            proc = subprocess.run(
                [sys.executable, "-X", "utf8", str(Path(__file__).resolve()), "--child"],
                capture_output=True, text=True, encoding="utf-8", timeout=60,
                creationflags=0x08000000, cwd=ROOT,
            )
            row = {"query": QUERY, "status": "returned", "exit_code": proc.returncode,
                   "stdout": proc.stdout, "stderr": proc.stderr}
        except subprocess.TimeoutExpired as exc:
            def txt(value):
                return value.decode("utf-8", errors="replace") if isinstance(value, bytes) else value or ""
            row = {"query": QUERY, "status": "timeout_60s", "stdout": txt(exc.stdout), "stderr": txt(exc.stderr)}
        row["elapsed_seconds"] = round(time.monotonic() - started, 3)
        row["fallback_scars"] = ["proof_steps_need_derived_joint_structure_2026_09_09",
                                "perceptron_proof_open_gaps_fleet_2026_07_12"]
        (ROOT / "RECALL_RECEIPT.json").write_text(json.dumps(row, indent=2), encoding="utf-8")
        (ROOT / "RECALL_OUTPUT.txt").write_text(row["stdout"] + row["stderr"], encoding="utf-8")
        print(json.dumps({k:v for k,v in row.items() if k not in ("stdout","stderr")}, indent=2))
