"""Bounded read-only probe of the named math-brain population store."""
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).parent
DB = Path("~/math-brain-build/local/population/brain.sqlite3")
SRC = "~/math-brain-build/src"
QUERY = "hexatic phase two dimensional Riesz gas Delaunay bond correlation"
env = dict(os.environ)
env["PYTHONPATH"] = SRC + os.pathsep + env.get("PYTHONPATH", "")
cmd = [sys.executable, "-X", "utf8", "-m", "math_brain.cli", "recall", str(DB), QUERY,
       "--limit", "10", "--skip-unknown-edges"]
start = time.monotonic()
try:
    p = subprocess.run(cmd, cwd=ROOT, env=env, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=120)
    raw = p.stdout
    result = json.loads(raw) if p.returncode == 0 else None
    data = {"query": QUERY, "command": cmd, "seconds": round(time.monotonic()-start, 3),
            "returncode": p.returncode, "hits": result if result is not None else None,
            "stderr_excerpt": p.stderr[:1000], "stdout_excerpt": raw[:1000] if result is None else None}
except subprocess.TimeoutExpired:
    data = {"query": QUERY, "command": cmd, "seconds": round(time.monotonic()-start, 3),
            "status": "timeout_120s"}
(ROOT / "RECALL_MEASUREMENT.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({k: v for k, v in data.items() if k not in {"hits", "command"}}, ensure_ascii=False))
if data.get("hits"):
    hits = data["hits"]
    if isinstance(hits, list):
        print(json.dumps([{k: h.get(k) for k in ("id", "title", "score")} for h in hits], ensure_ascii=False))
