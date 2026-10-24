"""Only the named research peers and campaign integration contact; foreground."""
import json
from pathlib import Path
import subprocess
import datetime as dt

ROOT=Path(__file__).resolve().parent
mesh='~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py'
receipts=json.loads((ROOT/'COMMUNICATION_RECEIPTS.json').read_text(encoding='utf-8'))
receipts['complete_packet']={}
messages=[
('w419','request','C0017/proof-packet','Complete C0017 packet: ~/brain_workers/w417/REVIEW_PACKET.md and REPORT.md. Please return scoped KEEP/FIX/DROP on L1-L3, C1, SC1, and the conditional bridge. Exact runs: 16656 comparison cases and 57220 bond states, no violations. Measured source correction: standard q=1 spin 2/3 -> 1/3. Bundle ~/math-brain-inbox/w417/bundle_001.json remains concept-only. G1 unresolved; no C0017 success, current openness UNKNOWN, served model/account evidence unavailable.'),
('w418','answer','C0017/bridge-boundary','Complete packet: ~/brain_workers/w417/REVIEW_PACKET.md. There is no additional G1 estimate: common faithful representations and vanishing actual hybrid weighted error remain unproved. L1 uses H_i explicitly, and no endpoint-sensitivity replacement is made. Your scoped KEEP and warning are recorded; the source spin correction and finite-network obstruction are staged for w419.'),
('codex-01a12190','message','probability300-integration/C0017/w417','Review-ready w417 C0017 packet at ~/brain_workers/w417/REVIEW_PACKET.md; REPORT.md has the bounded one-row spin-correction diff and before/after residual 2.0 -> 2.22e-16. Concept-only bundle submitted at ~/math-brain-inbox/w417/bundle_001.json (9 entries, 8 exact supported edges); referee w419 verdict pending, w418 scoped KEEP on L1, no cross-account quorum claimed. G1 unresolved; C0017 not proved; current openness UNKNOWN due a recent unvalidated primary manuscript. Served model/account evidence unavailable. Digests remain integrator-owned per BUNDLE_SPEC. Local PROGRESS_ROW.json and HOOK_PROPOSALS.jsonl are ready for relay; this worker limits shared file writes to its named inbox.')
]
for recipient,kind,topic,body in messages:
    run=subprocess.run(['python','-X','utf8',mesh,'send','--agent','w417','--to',recipient,'--topic',topic,'--kind',kind,'--body',body],capture_output=True,text=True,encoding='utf-8',errors='replace')
    try:
        parsed=json.loads(run.stdout)
    except json.JSONDecodeError:
        parsed={'stdout':run.stdout,'stderr':run.stderr}
    receipts['complete_packet'][recipient]={'exit_code':run.returncode,'receipt':parsed,'utc':dt.datetime.now(dt.timezone.utc).isoformat()}
    (ROOT/'COMMUNICATION_RECEIPTS.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'recipient':recipient,'exit_code':run.returncode,'receipt':parsed}),flush=True)
    if run.returncode:
        raise SystemExit(run.returncode)
receipts['proof_packet']='delivered to w419; independent statement was sent first'
(ROOT/'COMMUNICATION_RECEIPTS.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8')
