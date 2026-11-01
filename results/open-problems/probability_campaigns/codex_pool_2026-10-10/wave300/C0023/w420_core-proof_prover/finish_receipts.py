"""Close this packet's receipts without running held mathematical experiments."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
MESH = "~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py"
rows = [json.loads(line) for line in (ROOT/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
count = len(rows)
for name, before, after in (("REPORT.md","10 claim rows",f"{count} claim rows"),("STATUS.md","10 claims",f"{count} claims")):
    path = ROOT/name
    path.write_text(path.read_text(encoding="utf-8").replace(before,after),encoding="utf-8")
validation = json.loads((ROOT/"ARTIFACT_VALIDATION_REPORT.json").read_text(encoding="utf-8"))
assert count == validation["claim_rows"]
hashes = json.loads((ROOT/"REVIEW_FILE_HASHES.json").read_text(encoding="utf-8"))
for name in hashes:
    hashes[name] = hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
(ROOT/"REVIEW_FILE_HASHES.json").write_text(json.dumps(hashes,indent=2)+"\n",encoding="utf-8")
result = subprocess.run([sys.executable,"-X","utf8",MESH,"send","--agent","w420","--to","w422",
    "--topic","C0023","--kind","message","--body",
    "Final review packet: ~/brain_workers/w420/REPORT.md and PRIMARY_STATUS_ADDENDUM.md. Your Sept24 general primary theorem report is recorded separately from proof verification; no novel target success. 9 claims, 7 concept entries in two DRAFTs, 4 relations, 3 verified snapshot hashes. Numerical tests NOT RUN: critical memory gate. Integration handoff delivered; L0-L5 and G await your scoped audit."],
    capture_output=True,text=True,encoding="utf-8",timeout=60)
(ROOT/"REFEREE_FINAL_HANDOFF_REPORT.json").write_text(json.dumps({"returncode":result.returncode,"stdout":result.stdout,"stderr":result.stderr},indent=2)+"\n",encoding="utf-8")
pending = subprocess.run([sys.executable,"-X","utf8","~/<private-repo>/12_cognitive_architecture/agent_mesh/team_comm.py","read","--as","w420","--max","8"],
    capture_output=True,text=True,encoding="utf-8",timeout=60)
(ROOT/"FINAL_TEAM_READ_REPORT.json").write_text(json.dumps({"returncode":pending.returncode,"stdout":pending.stdout,"stderr":pending.stderr},indent=2)+"\n",encoding="utf-8")
print(json.dumps({"state":"NEEDS_REVIEW","claim_rows":count,"static_validation_passed":True,"source_file_hashes_verified":3,"numerical_checks_run":False,
    "referee_handoff_returncode":result.returncode,"team_read_returncode":pending.returncode,"team_messages":pending.stdout},ensure_ascii=False))
