from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
protocol=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))['required_per_run']
p=json.loads((R/'PROGRESS.json').read_text(encoding='utf-8'))
c=json.loads((R/'CLAIMS.json').read_text(encoding='utf-8'))
assert set(p)=={x.split(' (')[0] for x in protocol['progress_fields']}
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert p['packet_ids']==['A021']
for cl in c:
 assert set(cl)==set(protocol['claim_fields'])
 assert hashlib.sha256(cl['exact_statement'].encode()).hexdigest()==cl['statement_sha256']
report=(R/'REPORT.md').read_text(encoding='utf-8')
for f in protocol['report_fields']: assert '# '+f in report
assert report.rstrip().splitlines()[-1].startswith('**Universal bridge:**')
results={}
for f in ['DIRECT.json','REPLAY.json','BOUNDARY.json']:
 d=json.loads((R/'out'/f).read_text(encoding='utf-8')); assert d['status']=='PASS'
 results[f]={k:d[k] for k in ('status','assertions')}
lean=json.loads((R/'out/LEAN.json').read_text(encoding='utf-8-sig'))
files=[]
for f in R.rglob('*'):
 if f.is_file() and f.name!='ARTIFACT_CHECK.json':
  b=f.read_bytes(); assert len(b)<20_000_000
  files.append({'path':str(f.relative_to(R)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
out={'status':'PASS','protocol_keys_exact':True,'statement_hash_valid':True,'compatibility_identical':True,'numerical_proofs':results,'assertions_total':sum(d['assertions'] for d in results.values()),'lean_receipt_status':lean.get('result',{}).get('status',lean.get('status','SEE_LEAN_JSON')),'files':files,'external_mirror':'NOT_PERFORMED; supervisor pending','independent_review':'PENDING'}
(R/'out/ARTIFACT_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps({k:v for k,v in out.items() if k!='files'}))
