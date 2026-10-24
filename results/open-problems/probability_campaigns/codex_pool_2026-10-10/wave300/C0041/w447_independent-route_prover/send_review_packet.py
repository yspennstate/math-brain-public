"""Hand the finished packet to the named research peers and integration contact."""
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parent
state_file = root / "SUBMISSION_STATE.json"
state = json.loads(state_file.read_text(encoding="utf-8"))
assert state["submitted"] and json.loads((root / "PATCH_CHECK.json").read_text(encoding="utf-8"))["passed"]
hashes = json.loads((root / "REVIEW_FILE_HASHES.json").read_text(encoding="utf-8"))
sha = hashes["REVIEW_PACKET.md"]
mesh = "~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py"
messages = [
    ("w449", "C0041-review", f"Complete scoped review packet: ~/brain_workers/w447/REVIEW_PACKET.md SHA256 {sha}; exact files/hashes in REVIEW_FILE_HASHES.json. Audit ER/FV/CC/GO plus source status; no parent-problem proof. DRAFT: ~/math-brain-inbox/w447/bundle_001.json . 15 exact kernels, 300 tail checks, 60 returns passed. Single gap: fixed-law E[K_tau|no-backtracking]<infinity. Actual author served-model identity unavailable; requested settings are not evidence. State: submitted, not reviewed/ingested/retrievable."),
    ("w448", "C0041-independent-route", "Hardest saved lemma: ~/brain_workers/w447/LEMMA_CLOCK_TO_COUNT.md . Non-stopping clock-to-exit-count equivalence is proved by conditional exponential moments at actual stopping times and one global conditioning factor. Remaining gap: E[K_tau|B]<infinity from directional transience and iid. Complete packet: ~/brain_workers/w447/REVIEW_PACKET.md . GO is only a no-uniform-bound obstruction across homogeneous planar laws, not your two-site row-averaging identity; the four rational terms can receive the assigned w449 referee's check."),
    ("codex-01a12190", "probability300-integration", f"w447 C0041 review-ready packet: ~/brain_workers/w447/REVIEW_PACKET.md SHA256 {sha}; exact hashes in REVIEW_FILE_HASHES.json. Referee w449. Own DRAFT: ~/math-brain-inbox/w447/bundle_001.json (6 entries/5 relations), 4 author lemma proofs/0 keeps; 1 intake source patch and 2 exact-node source-status annotations. Current openness UNKNOWN: new September primary solution claim; no formal comparison executed. Single gap: finite conditional ball-exit count before regeneration. Author/referee response-side served-model evidence unavailable; no different-model gate or parent solved claim. State submitted only, no ingestion requested before gates."),
    ("w444", "C0041-boundary", "w447 disjoint route complete: ~/brain_workers/w447/REVIEW_PACKET.md . Main result CC is the non-stopping ball-exit-count/clock moment equivalence. FV is deterministic escape-radius geometry only; no inward-row rarity or adaptive-center iid cost estimate. Parent implication unproved; source status UNKNOWN. Packet handed to w449."),
]
receipts = []
for recipient, topic, body in messages:
    response = subprocess.run(["python", "-X", "utf8", mesh, "send", "--agent", "w447", "--to", recipient,
                               "--topic", topic, "--kind", "message", "--body", body],
                              capture_output=True, text=True, encoding="utf-8", timeout=60)
    record = {"to": recipient, "topic": topic, "returncode": response.returncode,
              "response": response.stdout, "stderr": response.stderr, "at_utc": datetime.now(timezone.utc).isoformat()}
    with (root / "HANDOFF_RECEIPTS.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")
    if response.returncode:
        raise RuntimeError("named-peer handoff failed: " + json.dumps(record))
    receipt = json.loads(response.stdout)
    receipts.append({"to": recipient, "message_id": receipt.get("message_id")})
    print(json.dumps(receipts[-1]))
state["referee_handoff_sent"] = True
state["integration_contact_handoff_sent"] = True
state["handoff_receipts"] = receipts
state["handoff_on"] = datetime.now(timezone.utc).isoformat()
state_file.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
progress = subprocess.run(["python", "-X", "utf8", "~/primary_directive/pd_progress.py",
                          "--event", "C0041: 4 author lemma proofs; 15 kernels/300 tails/60 returns checked; 6-entry DRAFT submitted, w449 review pending; source status UNKNOWN; gap E exit-count finite.",
                          "--agent", "w447", "--row", "S1.C0041", "--evidence", str(root / "REVIEW_PACKET.md")],
                         capture_output=True, text=True, encoding="utf-8", timeout=60)
(root / "PROGRESS_RECEIPT.json").write_text(json.dumps({"returncode": progress.returncode,
    "stdout": progress.stdout, "stderr": progress.stderr}, indent=2) + "\n", encoding="utf-8")
assert progress.returncode == 0
print(progress.stdout.strip())
