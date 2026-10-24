"""Narrow read-only metadata and source inspection for C0023."""
from pathlib import Path
import json
import os
import sqlite3

ROOT = Path(__file__).resolve().parent
mesh_path = Path(os.environ.get("AGENT_MESH_DB", "~/.agents/coordination/agent_mesh.sqlite3"))
print("MESH_METADATA", "Skipped after a locked read-only lookup; use the supported direct peer route.")

store_path = Path("~/math-brain-build/local/population/brain.sqlite3")
if store_path.exists():
    with sqlite3.connect("file:" + store_path.as_posix() + "?mode=ro", uri=True) as conn:
        tables = [r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")]
        print("MATH_STORE_TABLE_NAMES", json.dumps(tables))
        for table in ("cards", "entries", "sources", "nodes"):
            if table in tables:
                columns = [r[1] for r in conn.execute(f'PRAGMA table_info("{table}")')]
                print("MATH_STORE_COLUMNS", table, json.dumps(columns))

intake = Path("~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907")
selected = []
for name in ("problems.jsonl", "attempts.jsonl", "sources.jsonl"):
    with (intake / name).open(encoding="utf-8-sig") as handle:
        for line_number, line in enumerate(handle, 1):
            if name != "sources.jsonl" and '"C0023"' not in line:
                continue
            if name == "sources.jsonl" and not any(term in line for term in (
                '"garban_steif_noise_2012"', '"duminil_copin_icm_2018"')):
                continue
            record = json.loads(line)
            if name != "sources.jsonl" and record.get("problem_id") != "C0023":
                continue
            selected.append({"file": str(intake / name), "line": line_number, "record": record})
(ROOT / "SOURCE_RECORDS_REPORT.md").write_text(
    "Narrow C0023 intake records; historical assertions are not mathematical audit verdicts.\n\n"
    + "\n\n".join(json.dumps(row, ensure_ascii=False, indent=2) for row in selected), encoding="utf-8",
)
print("SOURCE_RECORDS_SAVED", len(selected))
