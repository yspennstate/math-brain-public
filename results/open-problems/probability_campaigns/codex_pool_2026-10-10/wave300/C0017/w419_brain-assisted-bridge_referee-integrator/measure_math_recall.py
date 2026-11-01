"""Run two read-only math-brain recall probes and save compact evidence locally."""
import json
import os
import pathlib
import subprocess
import sys
import time

here = pathlib.Path(__file__).resolve().parent
db = r"~\math-brain-build\local\population\brain.sqlite3"
env = dict(os.environ)
env["PYTHONDONTWRITEBYTECODE"] = "1"
env["PYTHONPATH"] = r"~\math-brain-build\src"
queries = [
    "C0017 conformal invariance critical bond percolation square lattice", 
    "Smirnov parafermionic observable square lattice random-cluster Ising q=2 theorem",
]
records = []
for query in queries:
    cmd = [sys.executable, "-X", "utf8", "-m", "math_brain.cli", "recall", db, query, "--limit", "5"]
    start = time.monotonic()
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", env=env, timeout=90)
        records.append({"query": query, "elapsed_s": round(time.monotonic()-start, 3), "returncode": result.returncode,
                        "stdout": result.stdout[:12000], "stderr": result.stderr[:3000]})
    except subprocess.TimeoutExpired as exc:
        records.append({"query": query, "elapsed_s": round(time.monotonic()-start, 3), "timeout": True,
                        "stdout": (exc.stdout or b"").decode("utf-8", "replace")[:12000] if isinstance(exc.stdout, bytes) else str(exc.stdout or "")[:12000]})
(here / "MATH_RECALL_MEASUREMENT.json").write_text(json.dumps(records, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
for rec in records:
    print(json.dumps(rec, ensure_ascii=False))
