from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
proto=load(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))['required_per_run']
p=load(R/'PROGRESS.json');c=load(R/'CLAIMS.json')[0]
assert set(p)=={s.split(' (')[0] for s in proto['progress_fields']}
assert set(c)==set(proto['claim_fields'])
assert c['version']==4 and c['claim_id']=='A034-AFFINE-PLANE-HEREDITARY-PHASE'
assert c['statement_sha256']==hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()
assert 'full rate32' in c['exact_statement']
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
report=(R/'REPORT.md').read_text(encoding='utf-8')
assert all(f in report for f in proto['report_fields'])
assert report.rfind('## Universal bridge')>report.rfind('## actual persistence')
outs=[load(R/'out'/f'{m}.json') for m in ['rows','scales','carrier','audit','symbolic','carrier_short']]
assert all(x['status']=='PASS' for x in outs)
assert sum(x['assertions'] for x in outs)==102908
for m in ['rows','scales','carrier','audit']:assert load(R/'out'/f'{m}.json')['helper_sha256']==digest(R/'code/check.py')
assert load(R/'out/symbolic.json')['helper_sha256']==digest(R/'code/symbolic.py')
assert load(R/'out/carrier_short.json')['helper_sha256']==digest(R/'code/carrier_short.py')
assert 'SETUP_UNVERIFIED' in (R/'out/lean_result.json').read_text(encoding='utf-8')
assert (R/'out/source_receipts.json').is_file()
# Preserve the final source list in both compatibility copies without reopening the mathematics.
for f in ['FROZEN_CARRIER_SHORT_BOUND.json','code/carrier_short.py','out/carrier_short.json','out/ADVERSARIAL_REVIEW.md']:
    if f not in p['source_artifacts']:p['source_artifacts'].append(f)
text=json.dumps(p,indent=2,ensure_ascii=False)+'\n'
(R/'PROGRESS.json').write_text(text,encoding='utf-8');(R/'PACKET_DELTA.json').write_text(text,encoding='utf-8')
durable='\nStage21 complete-source refinement: H<=min(K_M,2^(M+1)) IY and Hcond<=2^M IY from global phase degree and active-Y label entropy; M4 full rate32 needs a COMPLETE phase partition, whereas arbitrary proper FOUR-cell rows retain general rate<292. Exact SAME729 M2 restriction checks verify full rate8.\n'
learn=A/'LEARNED.md'
if 'Stage21 complete-source refinement:' not in learn.read_text(encoding='utf-8'):
    with learn.open('a',encoding='utf-8') as f:f.write(durable)
files=[f for f in R.rglob('*') if f.is_file() and f.name!='artifact_receipts.json']
assert all(f.stat().st_size<20_000_000 for f in files)
(R/'out/artifact_receipts.json').write_text(json.dumps([dict(path=str(f.relative_to(R)),bytes=f.stat().st_size,sha256=digest(f)) for f in files],indent=2)+'\n',encoding='utf-8')
receipts=load(R/'out/artifact_receipts.json')
assert all(digest(R/e['path'])==e['sha256'] for e in receipts)
print(json.dumps(dict(status='FINAL_VERIFIED_LOCAL',files=len(receipts)+1,exact_assertions=102908,full_fei='OPEN',independent_review='PENDING',lean='HELD_BEFORE_COMPILATION')))
