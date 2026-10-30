from pathlib import Path
from datetime import datetime,timezone
import json,hashlib

RUN=Path(__file__).resolve().parents[1]
AGENT=RUN.parents[1]
CAMPAIGN=AGENT.parents[1]
PROTOCOL=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(PROTOCOL.read_text(encoding='utf-8-sig'))
claims=json.loads((RUN/'CLAIMS.json').read_text(encoding='utf-8'))
for claim in claims:
    value={'statement':claim['exact_statement'],'hypotheses':claim['hypotheses']}
    claim['statement_sha256']=hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest()
    assert set(claim)==set(protocol['required_per_run']['claim_fields'])
(RUN/'CLAIMS.json').write_text(json.dumps(claims,indent=2)+'\n',encoding='utf-8')
progress=json.loads((RUN/'PROGRESS.json').read_text(encoding='utf-8'))
assert set(progress)==set(x.split(' (')[0] for x in protocol['required_per_run']['progress_fields'])
assert progress==json.loads((RUN/'PACKET_DELTA.json').read_text(encoding='utf-8'))
assert progress['packet_ids']==['A038']
base=json.loads((RUN/'out'/'VALIDATION.json').read_text(encoding='utf-8'))
reset=json.loads((RUN/'out'/'RESET_VALIDATION.json').read_text(encoding='utf-8'))
assert base['status']==reset['status']=='PASS'
assert base['elapsed_seconds']<60 and reset['elapsed_seconds']<60
assert base['assertions']+reset['assertions']==633
assert base['all_order_replays']==32
stamp=datetime.now(timezone.utc).isoformat()
entry='\n2026-10-12, stage 20261012T012321Z (saved '+stamp+'): Read new BOARD/B08 v2 and A039 originals; accepted lead target. Derived exact all-singleton-tree Gamma and posterior release with explicit finite error bounds: each asymptotic half of root Delta, JS injection retained. Derived Bayes outcome KL <=8log2(e)d and signed reset approaching -Delta/2. First local certificate caught an undercount of nonempty residual fibers; corrected beta=2d(1-d), preserved failed line. Completed release 330 checks/32.13s and reset 303 checks/45.71s, all frozen domains within cap. Scoped target resolved locally; source-compatible net payment with overlapping controls remains next; independent review/mirror pending, FEI open.\n'
worklog=AGENT/'WORKLOG.md'
if 'stage 20261012T012321Z' not in worklog.read_text(encoding='utf-8'):
    with worklog.open('a',encoding='utf-8') as f:f.write(entry)
lesson='''

## Stage 2: complete point-defect coordinate trees

- At active k-bit point defect, d_k=2^(1-k), visit weight w_k=2^(k-n), w_k*d_k=d_n. Constants and the k=1 character have zero information charges.
- Gamma_k=(k-1)[h2(d_k)-h2(2d_k)/2]; JS_k=h2(beta_k)-h2(2beta_k)/2, beta_k=2d_k(1-d_k). Exact erasure B_k=q0*h2(d_k^2/q0)+beta_k. Initial undercount of the nonempty fibers was caught by exact TC identity; beta is the correct mass.
- G_n=n*h2(d_n)-sum_k w_k*h2(d_k). Root Delta+J=G+C. G/d_n is between n(n-1)/2 and that value+2log2(e); J/d_n is between 2(n-1)-1 and 2(n-1)+4log2(e)-1.
- G/Delta and C/Delta tend to 1/2, J/Delta tends to zero. Every full adaptive singleton order gives the same tree ledger, so G/I>=(n-1)/2. This excludes an aggregate Gamma influence payment for these trees, not block trees or FEI.
- Compatible Bayes outcome q_k=(1-d_k)^(k-1)/(2q0_k). Total output KL O_n<=8log2(e)d_n. Signed reset R=O+J-G has R/Delta->-1/2. Retain this negative correction; it is not an extra root reserve.
- At n=2, Delta=0, G=J=1, C=0. Physical mixture information is a genuine injection in the projection ledger; finite root-share language without JS is false.
- Cumulative erasure B_tree/I->2 even while reset and credit/I grow like n/2. The next universal work must pay net cost with ownership and terminal core entropy, not separately bound the large components.
'''
learned=AGENT/'LEARNED.md'
if 'Stage 2: complete point-defect coordinate trees' not in learned.read_text(encoding='utf-8'):
    with learned.open('a',encoding='utf-8') as f:f.write(lesson)
def receipt(p):return {'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
prior=AGENT/'runs'/'20261011T221733Z-fleet05-A038-occupancy-term-audit'
peer=CAMPAIGN/'agents'/'A039'/'runs'/'20261011T223903Z-fleet05-A039-projection-under-restrictions'
inputs=[PROTOCOL,CAMPAIGN/'BOARD.md',CAMPAIGN/'claude'/'B08'/'STREAM_NOTES.md',prior/'REPORT.md',prior/'CLAIMS.json',prior/'out'/'sources'/'K_OCC_DEFINITION.md',peer/'REPORT.md',peer/'DERIVATION.md',peer/'DEPENDENCY_REVIEW.md']
(RUN/'out'/'SOURCE_RECEIPTS.json').write_text(json.dumps([receipt(p) for p in inputs],indent=2)+'\n',encoding='utf-8')
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:assert '## '+field in report
assert report.rstrip().split('\n')[-1].startswith('Universal bridge:')
manifest=[]
for p in RUN.rglob('*'):
    if p.is_file():
        assert p.stat().st_size<20*1024*1024
        if p.name!='ARTIFACT_SHA256.json':manifest.append(receipt(p))
manifest.extend(receipt(AGENT/name) for name in ['STATUS.md','WORKLOG.md','LEARNED.md'])
(RUN/'out'/'ARTIFACT_SHA256.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
summary={'schema_status':'PASS','total_exact_assertions':633,'complete_outputs':2,'claim_sha256':claims[0]['statement_sha256'],'artifacts_hashed':len(manifest),'all_files_under_20MB':True,'saved_at_utc':stamp}
(RUN/'out'/'FINAL_RECEIPT.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
print(json.dumps(summary))
