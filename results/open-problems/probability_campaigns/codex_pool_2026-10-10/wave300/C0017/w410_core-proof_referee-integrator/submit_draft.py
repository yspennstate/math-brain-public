"""Submit only the two explicitly named draft/proposal artifacts, without overwrites."""
from pathlib import Path
import hashlib
import json
import os

base = Path(__file__).parent
bundle = base / "brain_draft" / "bundle_001.json"
json.loads(bundle.read_text(encoding="utf-8"))
inbox = Path("~/math-brain-inbox/w410")
inbox.mkdir(exist_ok=True)
target = inbox / "bundle_001.json"
part = inbox / "bundle_001.json.part"
assert target.parent.resolve() == inbox.resolve()
assert not target.exists() and not part.exists(), "Refuse to overwrite prior w410 inbox files"
payload = bundle.read_bytes()
with part.open("xb") as f:
    f.write(payload)
    f.flush()
    os.fsync(f.fileno())
part.rename(target)
assert target.read_bytes() == payload
state_path = base / "BUNDLE_STATE.json"
state = json.loads(state_path.read_text(encoding="utf-8"))
state.update(submitted=True, submission_path=str(target), submitted_sha256=hashlib.sha256(payload).hexdigest(), ingested="not_verified", retrievable="not_verified", submission_blocker=None)
state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
hook_source = base / "hook_proposal.jsonl"
hook_target = Path("~/primary_directive/hooks1000/proposals/math-w410.jsonl")
assert hook_target.parent.exists() and not hook_target.exists(), "Refuse to overwrite prior hook proposals"
with hook_target.open("x", encoding="utf-8", newline="\n") as f:
    f.write(hook_source.read_text(encoding="utf-8"))
assert hook_target.read_text(encoding="utf-8") == hook_source.read_text(encoding="utf-8")
state["hook_proposal_path"] = str(hook_target)
state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("BUNDLE_SUBMITTED", target, state["submitted_sha256"])
print("HOOK_PROPOSED", hook_target)
print("INGESTED", state["ingested"], "RETRIEVABLE", state["retrievable"])
