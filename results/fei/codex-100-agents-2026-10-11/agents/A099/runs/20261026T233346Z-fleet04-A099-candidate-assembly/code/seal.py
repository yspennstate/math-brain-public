from pathlib import Path
import hashlib,json,re
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def read(n):return json.loads((R/n).read_text(encoding='utf-8'))
def put(n,x):(R/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
b=read('out/BOUNDARY_VALIDATION.json');formal=read('out/FORMAL_STATUS.json')
p=R/'REPORT.md';s=p.read_text(encoding='utf-8')
s=s.replace('The analytic theorems and exact bounded certificates are not represented as fully Lean-checked.','The optional rational numerator ring check returned RUNTIME_UNVERIFIED after120.8s (exit1); neither that identity nor the analytic theorems are represented as Lean-checked. Boundary checks separately passed '+str(b['exact_assertions'])+' exact assertions on '+str(b['boundary_queries'])+' queries with b=1 and b=1/64 through n=2; a true-zero unqueried ghost creates strictly positive outcome KL, so deliberately omitting that term fails the exact KL chain. This boundary command was executed through UTF-8 Python stdin; code/boundary.py preserves the identical computation for reproduction. The analytic theorems and exact bounded certificates are not represented as fully Lean-checked.')
p.write_text(s,encoding='utf-8')
for n in ['PROGRESS.json','PACKET_DELTA.json']:
 d=read(n);d['source_artifacts']+=['out/BOUNDARY_VALIDATION.json','out/FORMAL_STATUS.json','out/FINAL_RECEIPTS.json'];d['blockers'].append('Optional Lean ring identity RUNTIME_UNVERIFIED after120.8s; no formal acceptance')
 put(n,d)
manifest=[]
for x in R.rglob('*'):
 if x.is_file() and x.suffix!='.pyc' and x.name!='FINAL_RECEIPTS.json':
  raw=x.read_bytes();assert len(raw)<20*1024*1024
  manifest.append(dict(path=str(x.relative_to(R)),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest()))
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
spec=read('out/FROZEN_SPEC.json')
assert spec['checker_sha256']==hashlib.sha256((R/'code/check.py').read_bytes()).hexdigest()
assert spec['helper_sha256']==hashlib.sha256((R/'code/exact.py').read_bytes()).hexdigest()
for receipt in read('out/READ_RECEIPTS.json'):
 source=Path(receipt['path'])
 if source.name in ['CLAIMS.json','PROOF.md','DERIVATION.md','REPORT.md','REVIEW.md']:
  copy=R/'out/sources'/(source.parent.name+'-'+source.name)
  if copy.exists():assert hashlib.sha256(copy.read_bytes()).hexdigest()==receipt['sha256']
text=(R/'CANDIDATE_MANUSCRIPT.tex').read_text(encoding='utf-8')
assert (R/'STAGE11_ADDITIONS.tex').read_text(encoding='utf-8') in text
assert not re.search(r'Theorem~\\ref\{(?:lem|cor|prop):',text)
assert s.rfind('## Universal bridge')>s.rfind('## actual persistence')
put('out/FINAL_RECEIPTS.json',dict(timestamp=datetime.now(timezone.utc).isoformat(),status='LOCAL_READBACK_PASS',artifacts=manifest,scope='Local persistence only; no remote mirror or mathematical full-chain acceptance inferred',formal=formal['status']))
(R/'.final').write_text(datetime.now(timezone.utc).isoformat()+'\n',encoding='utf-8')
print(json.dumps(dict(status='LOCAL_READBACK_PASS',artifacts=len(manifest),claims=len(read('CLAIMS.json')),main=read('out/VALIDATION.json')['exact_assertions'],boundary=b['exact_assertions'],formal=formal['status'],full_FEI='OPEN')))
