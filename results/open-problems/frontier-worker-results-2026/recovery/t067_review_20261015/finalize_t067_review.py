"""Pin the lead review to immutable current bytes; no shared theorem promotion."""
from pathlib import Path
from datetime import datetime
import hashlib
import json

HERE=Path(__file__).resolve().parent
W=Path('~/brain_workers/w682')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
submission=W/'checks/piecewise156_submission.json'
data=json.loads(submission.read_text(encoding='utf-8'))
proof=W/'proofs/T067-PIECEWISE-D0-001_v1.md'
assert sha(proof)==data['proof_sha256']=='9a8a26b8c0631b4549f29bdc7ee231130a080a680408394bb75e0a8c16986226'
deps=[]
for row in data['dependencies']:
    p=W/row['proof_file']
    assert sha(p)==row['sha256'],p
    deps.append({'claim':row['claim_id'],'proof_sha256':sha(p)})
names=['T067_LEAD_ANALYTIC_AUDIT.md','audit_t067_symbolic.py',
    'T067_SYMBOLIC_RECEIPT.json','audit_t067_endpoints.py',
    'T067_ENDPOINTS_OWN_SUMMARY.json','audit_t067_quadratics.py',
    'T067_OWN_ENDPOINT_MAP.json','T067_OWN_FINITE_GATE_RECEIPT.json',
    'audit_t067_cutoff_scan.py','T067_CUTOFF_SCAN.json']
endpoint_map=json.loads((HERE/'T067_OWN_ENDPOINT_MAP.json').read_text(encoding='utf-8'))
assert len(endpoint_map['source_files'])==86
for filename,digest in endpoint_map['source_files'].items():
    assert sha(HERE/'t067_own_endpoints'/filename)==digest,filename
gate=json.loads((HERE/'T067_OWN_FINITE_GATE_RECEIPT.json').read_text(encoding='utf-8'))
assert gate['minimum_gap_float']>0 and gate['original_intervals']==85
out={'at':datetime.now().astimezone().isoformat(),'reviewer':'codex-term-362ebe34',
    'subject':'T067-PIECEWISE-D0-001 v1','proof_sha256':sha(proof),
    'verdict':'PASS lead analytic composition plus independently rebuilt endpoint and exact quadratic gate; pinned previously audited supporting lemmas',
    'admission':'pending outstanding w683 exact-version review; this receipt does not promote frontier',
    'dependencies':deps,'files':{name:sha(HERE/name) for name in names},
    'endpoint_files':endpoint_map['source_files'],
    'minimum_gap_exact':gate['minimum_gap_exact'],
    'caveat':'Blanket two-review metadata for RESCALE/GAUSSIAN-QUAD not verified; those elementary arguments independently rederived in lead note. No literature priority assertion.'}
(HERE/'T067_LEAD_REVIEW_RECEIPT.json').write_bytes((json.dumps(out,indent=2)+'\n').encode('utf-8'))
routes=HERE/'ROUTES.jsonl'
route={'at':out['at'],'problem':'T067','question':'Can an independently rebuilt all-fine Gaussian endpoint table lower the uniform d156 cutoff?',
    'frontier_check':'exit0; T067_CUTOFF_ROUTE_CHECK.log','result':'No: frozen exact general-L certificate passes156 and fails155. Analytic lead audit and independent original156 gate passed. Do not repeat table refinement without new remainder or curvature improvement.',
    'evidence':['T067_CUTOFF_SCAN.json','T067_LEAD_REVIEW_RECEIPT.json']}
with routes.open('a',encoding='utf-8',newline='\n') as f:f.write(json.dumps(route)+'\n')
print(json.dumps({'at':out['at'],'proof_sha256':out['proof_sha256'],'dependencies':len(deps),'endpoints':86,'receipt_sha256':sha(HERE/'T067_LEAD_REVIEW_RECEIPT.json')}))
