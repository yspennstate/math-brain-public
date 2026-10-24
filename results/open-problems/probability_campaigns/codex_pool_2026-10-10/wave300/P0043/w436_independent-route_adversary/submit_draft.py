"""Submit only the specifically authorized worker inbox file after a narrow lease."""
from pathlib import Path
from datetime import datetime, timezone
import json
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
INBOX = Path("~/math-brain-inbox/w436")
prepared = ROOT / "drafts" / "bundle_001.json"
target = INBOX / "bundle_001.json"
mesh = "~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py"
env = os.environ.copy()
env["PYTHONDONTWRITEBYTECODE"] = "1"
command = [sys.executable, "-X", "utf8", mesh, "claim", "--agent", "w436",
           "--resource", str(target), "--mode", "write", "--purpose",
           "P0043 concept-only draft in the explicitly assigned w436 inbox; no live store mutation", "--ttl", "15m"]
lease = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", env=env)
reports = ROOT / "reports"
reports.mkdir(exist_ok=True)
(reports / "MESH_DRAFT_LEASE.txt").write_text(lease.stdout+lease.stderr, encoding="utf-8")
print(lease.stdout+lease.stderr, end="", flush=True)
if lease.returncode:
    raise SystemExit(lease.returncode)

bundle = json.loads(prepared.read_text(encoding="utf-8"))
assert len(bundle["entries"]) == 3
assert all(entry["kind"] == "concept" and entry["proof_text"] is None for entry in bundle["entries"])
assert target.parent.resolve() == INBOX.resolve()
INBOX.mkdir(parents=True, exist_ok=True)
data = prepared.read_bytes()
if target.exists():
    if target.read_bytes() != data:
        raise SystemExit("Existing inbox draft differs; preserved without overwrite.")
else:
    part = INBOX / "bundle_001.part"
    if part.exists():
        raise SystemExit("Existing partial file preserved; reviewer must resolve it.")
    part.write_bytes(data)
    part.rename(target)
state = {
    "bundle": str(target), "submitted": True, "submitted_at_utc": datetime.now(timezone.utc).isoformat(),
    "reviewed": "pending w437", "ingested": "not verified", "retrievable": "not verified",
    "entries": len(bundle["entries"]), "relations": len(bundle["relations"]), "all_kinds": "concept",
    "live_math_store_modified_by_this_worker": False, "lease_receipt": "reports/MESH_DRAFT_LEASE.txt",
}
release_command = [sys.executable, "-X", "utf8", mesh, "release", "--agent", "w436", "--resource", str(target)]
release = subprocess.run(release_command, capture_output=True, text=True, encoding="utf-8", env=env)
(reports / "MESH_DRAFT_RELEASE.txt").write_text(release.stdout+release.stderr, encoding="utf-8")
state["lease_released"] = release.returncode == 0
state["lease_release_receipt"] = "reports/MESH_DRAFT_RELEASE.txt"
(ROOT / "SUBMISSION_STATE.json").write_text(json.dumps(state, indent=2)+"\n", encoding="utf-8")
print(json.dumps(state), flush=True)
