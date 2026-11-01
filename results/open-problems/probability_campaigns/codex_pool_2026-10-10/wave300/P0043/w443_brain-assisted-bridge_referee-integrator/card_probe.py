"""Read only the four P0043 cards named by the bounded recall probe."""
import contextlib
import io
import json
import sys
from pathlib import Path

ROOT = Path(r"~\math-brain-build")
DB = ROOT / "local" / "population" / "brain.sqlite3"
sys.path.insert(0, str(ROOT / "src"))
from math_brain.cli import main  # noqa: E402

recall = json.loads(Path("RECALL_MEASURE.json").read_text(encoding="utf-8"))
ids = []
for row in recall:
    for hit in row["result"]["hits"][:3]:
        if hit["id"] not in ids:
            ids.append(hit["id"])
rows = []
for node_id in ids:
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        code = main(["current-node", str(DB), node_id])
    rows.append({"node_id": node_id, "exit_code": code, "output": output.getvalue()})
Path("CARD_READS.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
for row in rows:
    print(row["node_id"] + "\n" + row["output"][:10000])
