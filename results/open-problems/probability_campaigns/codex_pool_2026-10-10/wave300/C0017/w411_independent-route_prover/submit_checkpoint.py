"""Publish only the explicitly named DRAFT inbox artifact after a mesh write claim."""
import difflib
import json
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent

target_dir = Path("~/math-brain-inbox/w411")
target = target_dir / "bundle_001.json"
local = ROOT / "bundle_001.json"
bundle = json.loads(local.read_text(encoding="utf-8"))
assert bundle["spec"] == "mathbrain-draft-v1" and bundle["author_agent"] == "w411"
assert len(bundle["entries"]) == 5 and len(bundle["relations"]) == 5
keys = {entry["key"] for entry in bundle["entries"]}
assert len(keys) == 5
for entry in bundle["entries"]:
    assert entry["source"]["license"] == "owner-own-work"
    assert entry["kind"] in ("definition","lemma","theorem","concept")
    if entry["kind"] in ("lemma","theorem"):
        assert entry["proof_text"]
    else:
        assert entry["proof_text"] is None
for relation in bundle["relations"]:
    assert relation["from_key"] in keys and relation["to_key"] in keys
    assert relation["kind"] in ("depends_on","cites")

assertion = subprocess.run(
    [sys.executable, "-B", "-X", "utf8",
     "~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py",
     "assert", "--agent", "w411", "--resource", str(target)],
    capture_output=True, text=True, encoding="utf-8", creationflags=0x08000000,
)
(ROOT / "MESH_ASSERTION.json").write_text(json.dumps({
    "resource": str(target), "exit_code": assertion.returncode,
    "stdout": assertion.stdout, "stderr": assertion.stderr,
}, indent=2), encoding="utf-8")
if assertion.returncode != 0:
    raise RuntimeError("live mesh write assertion failed; publication held")

text = local.read_text(encoding="utf-8")
target_dir.mkdir(parents=True, exist_ok=True)
part = target_dir / "bundle_001.json.part"
if target.exists():
    if target.read_text(encoding="utf-8") != text:
        raise RuntimeError("existing inbox bundle differs; refusing overwrite")
else:
    with part.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
        handle.flush()
    part.rename(target)
life_path = ROOT / "BUNDLE_LIFECYCLE.json"
life = json.loads(life_path.read_text(encoding="utf-8"))
life.update(submitted=True, destination=str(target),
            reviewed=False, ingested=False, retrievable=False,
            reason="Complete DRAFT submitted by .part rename; independent audit, integration and retrieval are not asserted.")
life_path.write_text(json.dumps(life, indent=2), encoding="utf-8")
patch_dir = ROOT / "patches"
patch_dir.mkdir(exist_ok=True)
live_path = "~/math-brain-inbox/w411/bundle_001.json"
diff = "".join(difflib.unified_diff([], text.splitlines(keepends=True),
                 fromfile="a/"+live_path, tofile="b/"+live_path))
(patch_dir / "01_c0017_draft_bundle.diff").write_text(diff, encoding="utf-8")
print(json.dumps({"submitted":str(target), "entries":5, "relations":5,
                  "schema_shape_checked":True, "mathematical_audit":False,
                  "ingested":False, "retrievable":False}))
