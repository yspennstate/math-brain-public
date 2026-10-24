"""One authorized direct peer handoff; persist the actual receipt, including failure."""
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys

root=Path(__file__).resolve().parent
required=['STATUS.md','SOURCE_STATUS.json','ATTEMPT.md','CLAIMS.jsonl','REPORT.md',
          'GAP.md','REVIEW_PACKET.md','BRAIN_STATES.json','bundle_local_001.json',
          'measurements.json','CORRECTION_MEASUREMENTS.json',
          'patches/01_lqg_kpz_guard.diff','patches/02_d0049_normalization.diff']
assert all((root/name).is_file() for name in required)
source=json.loads((root/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
assert source['exact_statement_recovered'] and not source['original_target_solved']
claims=[json.loads(line) for line in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
assert len(claims)==6 and all(not c.get('independently_checked',False) for c in claims)
assert all(c['independent_reviewer'].startswith('w524') for c in claims)
brain=json.loads((root/'BRAIN_STATES.json').read_text(encoding='utf-8'))
assert brain['submitted']['status']=='submitted DRAFT concepts'
inbox=Path(brain['submitted']['path'])
assert inbox.parent.resolve()==Path('~/math-brain-inbox/w522').resolve()
assert json.loads(inbox.read_text(encoding='utf-8'))==json.loads((root/'bundle_local_001.json').read_text(encoding='utf-8'))
verification={'date':datetime.now(timezone.utc).isoformat(),
              'required_files_present':len(required),'claim_rows':len(claims),
              'submitted_bundle_matches_local':True,'scope':'Artifact packaging only; not a mathematical audit.'}
(root/'PACKET_VERIFICATION.json').write_text(json.dumps(verification,indent=2),encoding='utf-8')
body=('P0297 full referee packet: ~/brain_workers/w522/REVIEW_PACKET.md. '
      'C1 repairs prior d=2Q/xi to gamma/xi (64/64 inconsistencies to 0; Brownian 10 to 4). '
      'L1-L4 prove sharp algebraic KPZ/thick-point boundaries; 1126 checks. Original LFPP normalization gap remains. '
      'Draft concepts submitted; no independent keep, novelty, formal receipt, or original-target solution claimed. '
      'Please save a claim-specific independent verdict; your own new results go to w527.')
command=[sys.executable,'-X','utf8',
         '~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py',
         'send','--agent','w522','--to','w524','--topic','P0297/w522/referee','--kind','request','--body',body]
run=subprocess.run(command,capture_output=True,text=True,encoding='utf-8',errors='replace')
receipt={'from':'w522','to':'w524','at_utc':datetime.now(timezone.utc).isoformat(),
         'packet':'~/brain_workers/w522/REVIEW_PACKET.md','body':body,
         'returncode':run.returncode,'stdout':run.stdout,'stderr':run.stderr,
         'delivery_state':'mesh send accepted' if run.returncode==0 else 'saved file handoff; mesh delivery unavailable',
         'independent_review_received':False}
(root/'HANDOFF_W524.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps({'artifact_verification':verification,'handoff_receipt':receipt},indent=2))
