"""Reproduce one read-only math-brain retrieval without touching the live store."""
import contextlib
import io
import json
import sys
import time
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, "~/math-brain-build/src")
from math_brain.cli import main

db = "~/math-brain-build/local/population/brain.sqlite3"
query = "Spielman Teng Bernoulli least singular value coefficient one Gaussian comparison"
args = ["recall", db, query, "--limit", "5", "--decision"]
capture = io.StringIO()
t0 = time.perf_counter()
with contextlib.redirect_stdout(capture):
    code = main(args)
seconds = time.perf_counter() - t0
out = {
    "command": "python -X utf8 ~/brain_workers/w575/run_math_recall.py",
    "cli_args": args,
    "exit_code": code,
    "elapsed_seconds": round(seconds, 3),
    "result": json.loads(capture.getvalue()),
}
Path(__file__).with_name("RECALL_BASELINE.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps({"elapsed_seconds": out["elapsed_seconds"], "result": out["result"]}, ensure_ascii=False))
