"""Only the named peers and the explicitly ordered progress helper are contacted."""
from pathlib import Path
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
MESH = Path('~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py')
env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONIOENCODING='utf-8')
messages = [
 ('w353','request','Independent review requested for w350 ATTEMPT.md Claims A-B only: Gaussian channel Y=sqrt(t)X+G; prior CP C implies R>=1/(1+Ct) via Bessel and adjoint; log-concave retention R(t0)>=eta implies CP<=1/(eta*t0) via posterior curvature. Check L2 density/domain and normalization. Full VR is explicitly unproved/equivalent to target. File ~/brain_workers/w350/ATTEMPT.md. Please save KEEP/FIX/DROP verdict locally and send path.'),
 ('w348','message','Claiming referee lane Gaussian-channel variance-retention bridge, disjoint from tensor recovery. Saved independent proof of L1 via normalized Kneser operator before reading your proof: ~/brain_workers/w350/reviews/w348_independent.md. Sharpness arithmetic next; note sharpness requires W nonzero as well as dim H>=2. Please point to completed tensor proof for final stepwise check. October proof claims recorded; no parent novelty claim.'),
 ('w349','message','KEEP for your C001-C005 within exact scoped statements, with independent reproductions and gaps at ~/brain_workers/w350/reviews/w349_verdicts.jsonl. C005 KEEP covers the zero-drift example only. I independently rederived w348 L1 before reading paired proof. My disjoint lane is Gaussian-channel variance retention; new bridge requested from w353.'),
]
for recipient, kind, body in messages:
    p=subprocess.run([sys.executable,'-X','utf8',str(MESH),'send','--agent','w350','--to',recipient,'--topic','P0017-proofswarm','--kind',kind,'--body',body],capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=45,env=env)
    with (ROOT/'COMM_RECEIPTS.jsonl').open('a',encoding='utf-8') as f:
        import json
        f.write(json.dumps({'recipient':recipient,'kind':kind,'body':body,'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr})+'\n')
    print(recipient,'EXIT',p.returncode,p.stdout[:1600],p.stderr[:600],flush=True)
