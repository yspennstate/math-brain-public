import hashlib
import json
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parent
bundle = json.loads((root / "bundle_001.json").read_text(encoding="utf-8"))
allowed = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
graph = {entry["key"]: [] for entry in bundle["entries"]}
for edge in bundle["relations"]:
    assert edge["kind"] in allowed
    if edge["kind"] == "depends_on" and "to_key" in edge:
        graph[edge["from_key"]].append(edge["to_key"])
visiting, visited = set(), set()
def visit(key):
    assert key not in visiting, "dependency cycle"
    if key in visited:
        return
    visiting.add(key)
    for neighbor in graph[key]:
        visit(neighbor)
    visiting.remove(key)
    visited.add(key)
for key in graph:
    visit(key)
for entry in bundle["entries"]:
    assert entry["source"]["license"].startswith("owner-own-work")
    assert entry["statement"]
    if entry["kind"] == "lemma":
        assert entry["proof_text"]
    else:
        assert entry["kind"] == "concept" and entry["proof_text"] is None
packet = json.loads((root / "REVIEW_PACKET.json").read_text(encoding="utf-8"))
for artifact in packet["artifacts"]:
    assert hashlib.sha256(Path(artifact["path"]).read_bytes()).hexdigest() == artifact["sha256"]
assert (root / "bundle_001.json").read_bytes() == Path("~/math-brain-inbox/w429/bundle_001.json").read_bytes()
command = ["git", "apply", "--no-index", "--check", str(root / "patches/01_block_bridge_guard.diff")]
result = subprocess.run(command, cwd=root / "patch_apply_check", capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
receipt = {"command": command, "exit_code": result.returncode, "stdout": result.stdout, "stderr": result.stderr, "scope": "Patch application in empty worker-owned scratch directory; no live file changes", "bundle_structure": "passed", "dependency_cycles": 0, "artifact_hash_checks": len(packet["artifacts"]), "mathematical_proof_audit": "PENDING w431"}
(root / "PATCH_CHECK.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
print(json.dumps(receipt, indent=2))
raise SystemExit(result.returncode)
