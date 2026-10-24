"""Bounded, read-only P0043 retrieval probe against the local math brain."""
import contextlib
import io
import json
import sys
from pathlib import Path

ROOT = Path(r"~\math-brain-build")
DB = ROOT / "local" / "population" / "brain.sqlite3"
sys.path.insert(0, str(ROOT / "src"))
from math_brain.cli import main  # noqa: E402

queries = [
    "absence of infinite clusters at critical percolation on quasi-transitive graphs",
    "Hutchcroft critical percolation quasi-transitive graph exponential growth theorem",
]
rows = []
for query in queries:
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = main(["recall", str(DB), query, "--limit", "5", "--decision"])
    raw = buf.getvalue()
    try:
        result = json.loads(raw)
    except json.JSONDecodeError:
        result = {"raw": raw}
    rows.append({"query": query, "exit_code": rc, "result": result})
Path("RECALL_MEASURE.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
for row in rows:
    print(json.dumps(row, ensure_ascii=False)[:6000])
