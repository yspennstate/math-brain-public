"""Structural packaging only; no scientific experiment or store integration."""
import json
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parent
inbox = Path("~/math-brain-inbox/w508").resolve()
part = (inbox / "bundle_001.part").resolve()
final = (inbox / "bundle_001.json").resolve()
assert part.parent == inbox and final.parent == inbox
bundle = json.loads(part.read_text(encoding="utf-8"))
assert bundle["spec"] == "mathbrain-draft-v1" and bundle["author_agent"] == "w508"
keys = {entry["key"] for entry in bundle["entries"]}
assert len(keys) == len(bundle["entries"])
required = {"key", "namespace", "logical_name", "kind", "title", "statement", "proof_text", "assumptions", "domain", "source"}
for entry in bundle["entries"]:
    assert required <= entry.keys()
    assert entry["kind"] in ("definition", "concept") and entry["proof_text"] is None
    assert entry["source"]["license"] == "owner-own-work"
for relation in bundle["relations"]:
    assert relation["from_key"] in keys and relation["to_key"] in keys
for line in (root / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines():
    json.loads(line)
hook = json.loads((root / "HOOK_PROPOSAL.jsonl").read_text(encoding="utf-8"))
assert len(hook["text"]) <= 300
json.loads((root / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
assert not final.exists(), "Preserve existing bundle; do not overwrite"
part.rename(final)
state = {"target":"P0162", "author_agent":"w508", "updated_utc":datetime.now(timezone.utc).isoformat(),
         "submitted":{"state":True,"path":str(final),"entries":len(bundle["entries"]),"relations":len(bundle["relations"])},
         "reviewed":{"state":False,"assigned_referee":"w509","note":"Identity unregistered on both attempted direct deliveries; w507 notified; review request preserved locally."},
         "ingested":{"state":"not_verified","note":"No integrator or store mutation run by w508."},
         "retrievable":{"state":"not_verified","note":"No retrieval claim for the submitted draft entries."},
         "structural_check":{"state":"passed","mathematical_proof":False,"formal_receipt":None},
         "experiment":{"state":"not_run_gate_denied","count":0},
         "hook_proposal":{"state":"local_patch_pending_review","path":str(root / "patches/01_fei_hook_proposal.diff")}}
(root / "DELIVERY_STATE.json").write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"submitted":str(final),"entries":len(bundle["entries"]),"relations":len(bundle["relations"]),
                  "claim_rows":len((root / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines()),
                  "structural_check":"passed","experiments_run":0,"reviewed":False,"ingested":"not_verified"}))
