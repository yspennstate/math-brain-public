"""Send final artifact pointers only to the task's named peers, then release own leases."""
from pathlib import Path
import json
import subprocess
import sys

root=Path(__file__).resolve().parent
mesh='~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py'
commands=[
['send','--agent','w541','--to','w540','--topic','P0321-core','--kind','message','--idempotency-key','w541-done-packet-20261010','--body','DONE adversary packet: ~/brain_workers/w541/REVIEW_PACKET.md, AUDIT.md and REPORT.md. Three concept drafts submitted to math-brain-inbox/w541/bundle_001.json. w542 KEEP receipt checks the Gaussian special case only; exact L2 cancellation and fixed-r transfer still await review. Your L1-L3 pass conditionally; M remains open. No live-store writes or full-target claim.'],
['send','--agent','w541','--to','w542','--topic','P0321-core','--kind','message','--idempotency-key','w541-final-review-packet-20261010','--body','Review packet complete: ~/brain_workers/w541/REVIEW_PACKET.md. Your exact S1.1 KEEP receipt saved in REVIEW_RECEIPTS.jsonl; scope remains Gaussian only. S1.2/S1.3 await your check (TRANSFER_COUNTEREXAMPLE.md, 12 exact cases/48 atoms). Three concept-only drafts submitted; SUBMISSION_STATE.json separates review/ingestion/recall. Audit of w540 L1-L3 is in AUDIT.md. M remains open.'],
['release','--agent','w541','--resource','topic:P0321:w541:gaussian-core-obstruction','--resource','~/math-brain-inbox/w541']
]
rows=[]
for args in commands:
    result=subprocess.run([sys.executable,'-X','utf8',mesh,*args],capture_output=True,text=True,encoding='utf-8',errors='replace')
    rows.append({'action':args[0],'recipient':args[args.index('--to')+1] if '--to' in args else None,'exit_code':result.returncode,'stdout':result.stdout,'stderr':result.stderr})
    (root/'MESH_HANDOFF_RECEIPTS.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{'action':r['action'],'recipient':r['recipient'],'exit_code':r['exit_code']} for r in rows]))
