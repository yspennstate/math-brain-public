import datetime
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
receipt_path = ROOT / "LEASE_RECEIPT.json"
receipt = {"acquired": True, "agent": "w493", "claim_id": "clm-aa6f06f4e4",
    "resource": "topic:C0120:w493:layer-mean-and-n2", "mode": "exclusive",
    "expires_at": "2026-10-10T08:12:52Z", "scope": "Own two-node draft only; no peer proof or live store mutation"}
receipt_path.write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
if datetime.datetime.now(datetime.timezone.utc) >= datetime.datetime.fromisoformat(receipt["expires_at"].replace("Z", "+00:00")):
    raise RuntimeError("Narrow publication lease expired; reacquire before submission")
checked = subprocess.run(["python", "-X", "utf8", str(ROOT / "verify_packet.py")],
    capture_output=True, text=True, encoding="utf-8", timeout=60)
print(checked.stdout.strip())
if checked.returncode:
    print(checked.stderr)
    raise RuntimeError("Local bundle validation failed; no inbox write performed")

inbox = Path("~/math-brain-inbox/w493")
allowed = Path("~/math-brain-inbox").resolve()
if inbox.resolve().parent != allowed or inbox.name != "w493":
    raise RuntimeError("Inbox destination escaped this worker's named output directory")
inbox.mkdir(parents=True, exist_ok=True)
dst = inbox / "bundle_001.json"
part = inbox / "bundle_001.part"
content = (ROOT / "bundle_001.json").read_bytes()
if dst.exists():
    if dst.read_bytes() != content:
        raise RuntimeError("An existing inbox bundle differs; no overwrite allowed")
else:
    if part.exists():
        if part.read_bytes() != content:
            raise RuntimeError("Existing partial bundle differs; preserve it")
    else:
        with part.open("xb") as f:
            f.write(content)
    part.rename(dst)
assert dst.read_bytes() == content
submission = {"prepared": True, "submitted": True,
    "submitted_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "path": str(dst), "entries": 2, "relations": 1,
    "reviewed": False, "review_state": "pending w494 independent check",
    "ingested": False, "ingestion_state": "not confirmed; coordinator integrates",
    "retrievable": False, "retrieval_state": "not checked",
    "mathematical_theorem_promotion": False, "parent_problem_solved": False,
    "served_model_gate": "not established", "lease": receipt["claim_id"]}
(ROOT / "SUBMISSION_RECEIPT.json").write_text(json.dumps(submission, indent=2)+"\n", encoding="utf-8")
source = json.loads((ROOT / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
source.update({"submission_state": "submitted DRAFT only", "review_state": "pending w494 independent review",
    "ingestion_state": "not confirmed", "retrieval_state": "not checked", "publication_lease": receipt,
    "canonical_population_check": "Read-only SQLite SELECT by the two exact C0120 node IDs confirmed unsupported scope in both cards; no live store write.",
    "team_delivery": "team_comm.py claim to w492 and review to w494 each reported sent=1 on retry; narrow triad C0120-w492-w493-w494"})
(ROOT / "SOURCE_STATUS.json").write_text(json.dumps(source, indent=2)+"\n", encoding="utf-8")
print(json.dumps(submission, indent=2))
