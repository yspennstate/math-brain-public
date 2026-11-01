"""Targeted source selection and read-only metadata queries for P0017."""
import json
import sqlite3
from pathlib import Path

base = Path(__file__).resolve().parent
research = Path("~/<private-repo>/06_math_research")
intake = research / "probability_1000_intake_D_20260908"
recovered = []
for name in ("problems.jsonl", "attempts.jsonl", "sources.jsonl"):
    with (intake / name).open(encoding="utf-8-sig") as stream:
        for number, line in enumerate(stream, 1):
            if "P0017" in line:
                row = json.loads(line)
                recovered.append({"path": str(intake / name), "line": number, "row": row})

def visit(value, path, filename):
    if isinstance(value, dict):
        text_fields = {k: v for k, v in value.items() if isinstance(v, str)}
        searchable = " ".join(text_fields.values())
        if "P0017" in searchable or "Dimension-free log-concave Poincare" in searchable:
            recovered.append({"path": str(filename), "json_path": path, "row": {k: value[k] for k in value if k in {"key", "logical_name", "kind", "title", "statement", "proof_text", "assumptions", "source", "remaining_gap", "status"}}})
        for k, child in value.items():
            if isinstance(child, (dict, list)):
                visit(child, path + "." + k, filename)
    elif isinstance(value, list):
        for i, child in enumerate(value):
            visit(child, path + f"[{i}]", filename)

for name in ("brain_bundle_C005.json", "brain_bundle_C006p01.json", "brain_bundle_C006a04.json"):
    filename = research / "probability_1000_intake_claude_20260907" / name
    visit(json.loads(filename.read_text(encoding="utf-8-sig")), "$", filename)
(base / "SOURCE_RECOVERY.json").write_text(json.dumps(recovered, indent=2, ensure_ascii=False), encoding="utf-8")
for row in recovered:
    print(json.dumps(row, ensure_ascii=False))

store = Path("~/math-brain-build/local/population/brain.sqlite3")
db = sqlite3.connect("file:" + store.as_posix() + "?mode=ro", uri=True, timeout=3)
schema = db.execute("SELECT name,sql FROM sqlite_master WHERE type='table' AND name IN ('cards','nodes','sources','objects')").fetchall()
db.close()
(base / "STORE_SCHEMA_RECEIPT.json").write_text(json.dumps(schema, indent=2), encoding="utf-8")
print("READ_ONLY_STORE_SCHEMA", json.dumps(schema))

meshpath = Path("~/.agents/coordination/agent_mesh.sqlite3")
db = sqlite3.connect("file:" + meshpath.as_posix() + "?mode=ro", uri=True, timeout=3)
campaigns = db.execute("SELECT name,campaign_id FROM campaigns WHERE status='active' AND (name LIKE '%prob%' OR name LIKE '%P0017%' OR name LIKE '%W0300%' OR name='O') ORDER BY rowid DESC LIMIT 8").fetchall()
peer_campaigns = db.execute("SELECT a.agent_id,c.name,c.campaign_id FROM agents a LEFT JOIN campaigns c ON c.campaign_id=a.campaign_id WHERE a.agent_id IN ('w354','w355','w356')").fetchall()
db.close()
(base / "RECIPIENT_CAMPAIGN.json").write_text(json.dumps({"campaigns": campaigns, "peer_campaigns": peer_campaigns}, indent=2), encoding="utf-8")
print("TARGET_CAMPAIGNS", json.dumps(campaigns))
print("PEER_CAMPAIGNS", json.dumps(peer_campaigns))
