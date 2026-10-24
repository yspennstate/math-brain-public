"""Deliver the completed scoped packet through the existing authorised mesh."""
import json
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parent
receipt = json.loads((root / "SUBMISSION_RECEIPT.json").read_text(encoding="utf-8"))
review = json.loads((root / "REVIEW_VERDICT.json").read_text(encoding="utf-8"))
messages = [
    ("w489", "done", "Scoped KEEP L3-L5 conditional only; frozen ATTEMPT SHA256 " + review["source_sha256"] + ". Main gaps retained: fixed-lambda eta=0 inverse moments, nonzero mass, GOE. My disjoint UI/ac-no-Lp bundle is submitted as concepts. Review: ~/brain_workers/w490/REVIEW_VERDICT.json"),
    ("w491", "done", "w490 review packet complete: ~/brain_workers/w490/REVIEW_PACKET.md. Check joint-UI event-weighted tests/countable exhaustion, and UI_SEPARATION.md. Bundle " + receipt["path"] + " SHA256 " + receipt["artifact_sha256"] + ". All concepts; served-model receipts unavailable; no promotion or C0056 solved claim."),
    ("codex-01a12190", "done", "C0056 DRAFT ready: " + receipt["path"] + " SHA256 " + receipt["artifact_sha256"] + ". Review packet ~/brain_workers/w490/REVIEW_PACKET.md. Scoped KEEP w489 L3-L5 conditional only. w490 UI criterion/separation await w491; fixed-disorder inverse moment, nonzero mass, GOE remain gaps. Response-side served-model evidence UNKNOWN; no solved claim/store promotion."),
]
for recipient, kind, message in messages:
    result = subprocess.run(["python", "-X", "utf8", str(root / "team_notice.py"), recipient, kind, message], capture_output=True, text=True, encoding="utf-8")
    print(result.stdout.strip(), flush=True)
    if result.stderr:
        print(result.stderr.strip(), flush=True)
