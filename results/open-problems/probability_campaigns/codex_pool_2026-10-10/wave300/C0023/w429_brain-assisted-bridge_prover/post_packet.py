import json
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parent
mesh = "~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py"
messages = [
    ("w431", "C0023", "Final w429 packet: ~/brain_workers/w429/REVIEW_PACKET.json (exact artifact hashes), REPORT.md, ATTEMPT.md L1-L4, CLAIMS.jsonl, PATCH_CHECK.json. 303 exact controls passed; illustrative false certificates 3 to 0; patch and bundle structural checks passed. Draft ~/math-brain-inbox/w429/bundle_001.json has 7 entries/7 relations. Your mathematical audit remains pending; no C0023 solution claim. w430 polynomial criterion remains separately attributed. Author response-side served-model evidence UNKNOWN; please include actual referee evidence if exposed."),
    ("codex-01a12190", "probability300-integration", "Review-ready C0023 packet: ~/brain_workers/w429/REVIEW_PACKET.json contains exact file paths/hashes; REPORT.md summarizes 303 checks and a measured 3-to-0 false-certificate safeguard on constructed controls. Draft ~/math-brain-inbox/w429/bundle_001.json: 7 entries/7 relations, submitted only; w431 audit pending, scoped KEEP empty, ingested/retrievable false. Hardest gap: compatible critical blocks with verified error/range or actual-filtration conditional success. Author served identity UNKNOWN, referee evidence PENDING, requested settings not treated as served evidence. Endpoint finite-energy application correction is separately pending any required Claude statement review. No parent-problem solved or promotion claim.")
]
receipts = []
for recipient, topic, body in messages:
    args = ["python", "-X", "utf8", mesh, "send", "--agent", "w429", "--to", recipient, "--topic", topic, "--kind", "message", "--body", body]
    result = subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
    receipts.append({"recipient": recipient, "exit_code": result.returncode, "stdout": result.stdout, "stderr": result.stderr})
    (root / "HANDOFF_RECEIPTS.json").write_text(json.dumps(receipts, indent=2), encoding="utf-8")
    if result.returncode:
        raise SystemExit(result.returncode)
progress = ["python", "-X", "utf8", "~/primary_directive/pd_progress.py", "--event", "w429 review-ready C0023: L1-L4 and hardest gap saved; 303 controls pass; illustrative false certificates 3 to 0; 7 DRAFT entries/7 edges submitted; referee pending, no parent theorem proof.", "--agent", "w429", "--row", "S1.2", "--evidence", str(root / "REPORT.md")]
result = subprocess.run(progress, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
receipts.append({"progress_row": "S1.2", "exit_code": result.returncode, "stdout": result.stdout, "stderr": result.stderr})
(root / "HANDOFF_RECEIPTS.json").write_text(json.dumps(receipts, indent=2), encoding="utf-8")
print(json.dumps(receipts, indent=2))
raise SystemExit(result.returncode)
