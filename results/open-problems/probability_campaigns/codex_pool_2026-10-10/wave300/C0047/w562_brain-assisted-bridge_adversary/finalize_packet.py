"""Finalize only isolated receipts/status after completed measurements."""
import hashlib
import json
from pathlib import Path

root=Path(__file__).resolve().parent
hashes=json.loads((root/"ARTIFACT_HASHES.json").read_text(encoding="utf-8"))
for name in list(hashes):hashes[name]=hashlib.sha256((root/name).read_bytes()).hexdigest()
for name in ("REPORT.md","REVIEW_PACKET.md","BRAIN_COMPARISON.md","AUDIT_VERDICTS.jsonl","MODEL_PROVENANCE.json"):
    hashes[name]=hashlib.sha256((root/name).read_bytes()).hexdigest()
(root/"ARTIFACT_HASHES.json").write_text(json.dumps(hashes,indent=2)+"\n",encoding="utf-8")
progress={"event":"C0047 w562: source correction, overlap counterexample, candidate slot coupling and conditional w561 audit saved; fallback found 2/2 target cards versus 0/2 in top6; DRAFT submitted, not ingested.","agent":"w562","row":"S1.w562.002","evidence":"~/brain_workers/w562/REVIEW_PACKET.md"}
(root/"PROGRESS_EVENT.json").write_text(json.dumps(progress,indent=2)+"\n",encoding="utf-8")
print("Evidence hashes refreshed; progress event staged. STATE is finalized only after packet validation passes.")
