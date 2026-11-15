"""Bind the scope clarification to the independently checked old mathematics."""
from pathlib import Path
from datetime import datetime
import hashlib,json,difflib
HERE=Path(__file__).resolve().parent;W=Path('~/brain_workers/w682')
def sha(b):return hashlib.sha256(b).hexdigest()
p2=W/'proofs/T067-PIECEWISE-D0-001_v2.md';p3=W/'proofs/T067-PIECEWISE-D0-001_v3.md'
b2=p2.read_bytes();b3=p3.read_bytes();a=b2.decode('utf-8');b=b3.decode('utf-8')
assert sha(b2)=='46689fc2727e31a3d52e637d9adce70e3dd3b2f981fbb8e7dc752c859cc10e3c'
assert sha(b3)=='ce54815cc311ba9722152637ee2a8898a53d5f468ffe665429c5625f46ec9ebb'
marker='\r\n## Version3 dependency-scope clarification'
assert b.count(marker)==1
prefix,amendment=b.split(marker)
expected=a.replace('Claim T067-PIECEWISE-D0-001, version 2.',
                   'Claim T067-PIECEWISE-D0-001, version 3.',1)
expected=expected.replace('UNIFORM-LOCAL, RESCALE, FIXEDPOINT and GAUSSIAN-QUAD.',
                          'UNIFORM-LOCAL, RESCALE identity (R) only, FIXEDPOINT and GAUSSIAN-QUAD.',1)
assert prefix==expected
assert 'Its false unrestricted F1' in amendment and 'F2 with actual' in amendment
audit=Path('~/brain_workers/w683/audits/w682_T067-PIECEWISE-D0-001_v2.md').read_bytes()
assert sha(b2) in audit.decode('utf-8') and '**Verdict: PASS' in audit.decode('utf-8')
(HERE/'T067_V2_V3_LEAD.diff').write_bytes(''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True))).encode('utf-8'))
out={'at':datetime.now().astimezone().isoformat(),'status':'PASS exact scoped-v3 binding to unchanged v2 mathematics',
     'v2_sha256':sha(b2),'v3_sha256':sha(b3),'w683_v2_audit_sha256':sha(audit),
     'lead_original_review_sha256':sha((HERE/'T067_LEAD_REVIEW_RECEIPT.json').read_bytes()),
     'scope_counterexample_receipt_sha256':sha((HERE/'T067_RESCALE_SCOPE_RECEIPT.json').read_bytes()),
     'changes':'version line, dependency identityR only, appended F2-domain/R-only amendment; all other bytes equal',
     'scope':'Lead PASS for corrected scope and mathematical equivalence. Same-account lead and w683 do not satisfy distinct-account gate. No frontier admission.'}
(HERE/'T067_V3_LEAD_BINDING.json').write_bytes((json.dumps(out,indent=2)+'\n').encode('utf-8'))
print(json.dumps(out))
