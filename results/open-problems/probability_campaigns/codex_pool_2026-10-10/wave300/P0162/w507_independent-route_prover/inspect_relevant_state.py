"""Narrow read-only metadata/target queries; receipts stay in this folder."""
import json
import sqlite3
import time
from pathlib import Path

root = Path(__file__).resolve().parent
receipt = {}


def open_ro(path):
    connection = sqlite3.connect("file:" + str(path).replace("\\", "/") + "?mode=ro", uri=True, timeout=3)
    connection.execute("PRAGMA query_only=ON")
    deadline = time.monotonic() + 8
    connection.set_progress_handler(lambda: int(time.monotonic() > deadline), 2000)
    return connection


mesh_path = Path("~/.agents/coordination/agent_mesh.sqlite3")
try:
    with open_ro(mesh_path) as c:
        schemas = c.execute("SELECT name,sql FROM sqlite_master WHERE type='table' AND name IN ('agents','campaigns')").fetchall()
        receipt["mesh_schemas"] = schemas
        receipt["peer_agents"] = c.execute("SELECT agent_id,campaign_id,status FROM agents WHERE agent_id IN (?,?,?,?)",
                                           ("w507", "w508", "w509", "w346")).fetchall()
        receipt["campaigns"] = c.execute("SELECT * FROM campaigns WHERE campaign_id IN (SELECT campaign_id FROM agents WHERE agent_id IN (?,?,?))",
                                          ("w507", "w508", "w509")).fetchall()
except Exception as exc:
    receipt["mesh_error"] = str(exc)

population = Path("~/math-brain-build/local/population/brain.sqlite3")
try:
    with open_ro(population) as c:
        receipt["math_store_path"] = str(population)
        receipt["math_table_names"] = [r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table'")]
        receipt["math_schemas"] = c.execute("SELECT name,sql FROM sqlite_master WHERE type='table' AND name IN ('nodes','claims','sources')").fetchall()
        columns = [r[1] for r in c.execute("PRAGMA table_info(nodes)")]
        wanted = [x for x in ("node_id", "id", "namespace", "logical_name", "kind", "title", "statement", "status", "source_id") if x in columns]
        if "title" in columns:
            cols = ",".join('"'+x+'"' for x in wanted)
            rows = c.execute("SELECT " + cols + " FROM nodes WHERE lower(title) LIKE '%fourier%entropy%' OR lower(title) LIKE '%entropy%influence%' LIMIT 30").fetchall()
            receipt["target_nodes"] = [dict(zip(wanted, r)) for r in rows]
        elif "logical_name" in columns:
            rows = c.execute("SELECT logical_name FROM nodes WHERE logical_name LIKE '%p0162%' LIMIT 12").fetchall()
            receipt["target_logical_names"] = rows
except Exception as exc:
    receipt["math_store_error"] = str(exc)

teams = Path("~/brain_workers/teams/PROBABILITY300_20261010")
try:
    assignments = json.loads((teams / "ASSIGNMENTS.json").read_text(encoding="utf-8-sig"))
    receipt["assignment_type"] = type(assignments).__name__
    if isinstance(assignments, dict):
        receipt["assignment_keys"] = list(assignments)[:15]
        for key, value in assignments.items():
            if key in ("w507", "w508", "w509"):
                receipt.setdefault("exact_assignments", {})[key] = value
            elif isinstance(value, list):
                receipt.setdefault("exact_assignments", {})[key] = [x for x in value
                    if isinstance(x, dict) and any(x.get(y) in ("w507", "w508", "w509") for y in ("agent", "agent_id", "worker", "id"))]
except Exception as exc:
    receipt["assignment_error"] = str(exc)

receipt["core_lane_artifact_names"] = {}
for worker in ("w504", "w505"):
    folder = Path("~/brain_workers") / worker
    receipt["core_lane_artifact_names"][worker] = [p.name for pattern in ("*ATTEMPT*", "*APPROACH*", "*METHOD*") for p in folder.glob(pattern) if p.is_file()]

(root / "READ_ONLY_LOOKUP.json").write_text(json.dumps(receipt, indent=2, default=str) + "\n", encoding="utf-8")
for key in ("peer_agents", "campaigns", "mesh_error", "math_table_names", "math_schemas", "target_nodes", "math_store_error", "assignment_keys", "core_lane_artifact_names"):
    if key in receipt:
        print(key, json.dumps(receipt[key], default=str))
