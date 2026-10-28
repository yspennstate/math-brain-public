from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def load(p):return json.loads((R/p).read_text(encoding='utf-8'))
def put(p,x):(R/p).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
proto=json.loads(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
claims=load('CLAIMS.json');progress=load('PROGRESS.json');dag=load('out/PROOF_DEPENDENCIES.json')
claimfields=set(proto['required_per_run']['claim_fields']);assert all(set(c)==claimfields for c in claims)
progressfields={x.split(' (')[0] for x in proto['required_per_run']['progress_fields']};assert set(progress)==progressfields
assert progress['packet_ids']==['A099']
report=(R/'REPORT.md').read_text(encoding='utf-8')
assert all(x in report for x in proto['required_per_run']['report_fields'])
assert report.rfind('## Universal bridge')>report.rfind('## actual persistence')
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
ids={x['claim_id'] for x in dag['nodes']};assert len(ids)==len(dag['nodes'])
edges={x['claim_id']:x['proof_dependencies'] for x in dag['nodes']};done=set();active=set()
def visit(i):
 assert i in ids
 if i in done:return
 assert i not in active
 active.add(i)
 for d in edges[i]:visit(d)
 active.remove(i);done.add(i)
for i in ids:visit(i)
text=(R/'CANDIDATE_MANUSCRIPT.tex').read_text(encoding='utf-8');addition=(R/'STAGE12_ADDITIONS.tex').read_text(encoding='utf-8')
assert addition in text
labels=re.findall(r'\\label\{([^}]+)\}',text);refs=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',text)
assert len(labels)==len(set(labels));assert not set(refs)-set(labels)
assert not re.search(r'Theorem~\\ref\{(?:lem|prop|cor):',text)
assert text.count(r'\begin{conjecture}')==4
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
spec=load('out/FROZEN_SPEC.json')
assert spec['checker_sha256']==hashlib.sha256((R/'code/check.py').read_bytes()).hexdigest()
assert spec['helper_sha256']==hashlib.sha256((R/'code/exact.py').read_bytes()).hexdigest()
for receipt in load('out/SOURCE_RECEIPTS.json'):
 path=Path(receipt['path']);copy=R/'out/sources'/(path.parent.name+'-'+path.name)
 if copy.exists():assert hashlib.sha256(copy.read_bytes()).hexdigest()==receipt['sha256']
assert load('out/VALIDATION.json')['status']=='PASS'
put('out/STRUCTURAL_CHECK.json',dict(status='PASS',claim_records=len(claims),dag_nodes=len(ids),resolved_acyclic_DAG=True,labels=len(labels),universal_conjectures=4,protocol_schemas=True,full_FEI='OPEN'))
manifest=[]
for p in R.rglob('*'):
 if p.is_file() and p.suffix!='.pyc' and p.name!='FINAL_RECEIPTS.json':
  b=p.read_bytes();assert len(b)<20*1024*1024
  manifest.append(dict(path=str(p.relative_to(R)),bytes=len(b),sha256=hashlib.sha256(b).hexdigest()))
put('out/FINAL_RECEIPTS.json',dict(timestamp=datetime.now(timezone.utc).isoformat(),status='LOCAL_READBACK_PASS',artifacts=manifest,scope='Local save only; supervisor mirrors, full-chain acceptance and public release not inferred'))
(R/'.final').write_text(datetime.now(timezone.utc).isoformat()+'\n',encoding='utf-8')
print(json.dumps(dict(status='LOCAL_READBACK_PASS',claims=len(claims),nodes=len(ids),artifacts=len(manifest),checks=load('out/VALIDATION.json')['exact_assertions'],full_FEI='OPEN')))
