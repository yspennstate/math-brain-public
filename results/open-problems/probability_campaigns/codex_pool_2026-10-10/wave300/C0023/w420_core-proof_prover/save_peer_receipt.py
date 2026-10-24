"""Record the received scoped KEEP without reviewing the review or promoting a theorem."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
receipt = {"reviewer":"w421","verdict":"KEEP","scope":"conditional supporting lemmas L0-L5 only",
    "remaining_gap_preserved":"G","evidence_path":"~/brain_workers/w421/AUDIT_W420.md",
    "received_via":"team_comm.py read --as w420; message timestamp 06:56 UTC",
    "served_model":"UNVERIFIED","cross_account_quorum":"UNVERIFIED","parent_problem_proved":False}
(root/"SCOPED_PEER_KEEP_REPORT.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
path = root/"SOURCE_STATUS.json"
source = json.loads(path.read_text(encoding="utf-8"))
source["scoped_review_receipts"] = [receipt]
source["brain_pipeline"]["reviewed"] = {"state":"partial","received":"w421 scoped KEEP L0-L5; G remains unproved",
    "pending":"named referee w422; served-model/different-account gates unverified; no parent theorem promotion"}
path.write_text(json.dumps(source,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
rows = [json.loads(line) for line in (root/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
for row in rows:
    if row["id"] in {f"C0023-w420-L{i}" for i in range(6)}:
        row["independent_reviewer"] = "w421 scoped KEEP received via mesh (AUDIT_W420.md); w422 referee pending; served identity/cross-account quorum unverified"
        # Keep original claim statuses; one scoped receipt does not promote a theorem.
(root/"CLAIMS.jsonl").write_text("".join(json.dumps(row,ensure_ascii=False)+"\n" for row in rows),encoding="utf-8")
report = root/"REPORT.md"
text = report.read_text(encoding="utf-8").replace(
    "Review, ingestion and retrievability have no verified receipts.",
    "w421 supplied a scoped KEEP for L0-L5, preserving G; named referee w422 and model/account review gates remain pending. Ingestion and retrievability have no verified receipts.")
report.write_text(text,encoding="utf-8")
with (root/"STATUS.md").open("a",encoding="utf-8") as handle:
    handle.write("2026-10-10: Received w421 scoped KEEP of conditional L0-L5, preserving open G; no review of that review or theorem promotion. Directly inspected primary manuscript Theorem 1.1 on printed p. 2; reported scope includes all assigned dimensions, proof validity unverified.\n")
hashpath = root/"REVIEW_FILE_HASHES.json"
hashes = json.loads(hashpath.read_text(encoding="utf-8"))
for name in hashes:
    hashes[name] = hashlib.sha256((root/name).read_bytes()).hexdigest()
hashpath.write_text(json.dumps(hashes,indent=2)+"\n",encoding="utf-8")
mesh = "~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py"
body = "C0023 w420 receipt update: w421 scoped KEEP L0-L5 received, with G unproved. See ~/brain_workers/w420/SCOPED_PEER_KEEP_REPORT.json and refreshed REVIEW_FILE_HASHES.json. w422 referee and served-model/account gates still pending; no theorem promotion. Sept24 primary Theorem 1.1 statement inspected directly and reports all assigned dimensions solved; full proof unverified. Two concept DRAFTs remain submitted; no ingestion receipt."
result = subprocess.run([sys.executable,"-X","utf8",mesh,"send","--agent","w420","--to","codex-01a12190",
    "--topic","probability300-integration","--kind","message","--body",body],capture_output=True,text=True,encoding="utf-8",timeout=60)
(root/"INTEGRATION_RECEIPT_UPDATE_REPORT.json").write_text(json.dumps({"returncode":result.returncode,"stdout":result.stdout,"stderr":result.stderr},indent=2)+"\n",encoding="utf-8")
print(json.dumps({"state":"NEEDS_REVIEW","scoped_keep_recorded":True,"gap":"G unproved","integration_update_returncode":result.returncode,"numerical_tests_run":False}))
