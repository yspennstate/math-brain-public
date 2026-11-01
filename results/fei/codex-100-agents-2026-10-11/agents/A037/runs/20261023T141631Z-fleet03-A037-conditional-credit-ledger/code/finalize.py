from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
d=load(R/'out/LEDGER.json');assert d['status']=='PASS'
p=load(R/'PROGRESS.json');p['mathematical_delta']['complete_tree_validation']=d;p['source_artifacts'].append(str(R/'out/LEDGER.json'))
save(R/'PROGRESS.json',p);save(R/'PACKET_DELTA.json',p)
c=load(R/'CLAIMS.json');c[0]['proof_source'].append(str(R/'out/LEDGER.json'));save(R/'CLAIMS.json',c)
line=f"Additional complete-tree replay PASS: {d['trees']} source/witness trees, {d['internal_nodes']} reached internal nodes, {d['eligible_reset_nodes']} eligible actual resets, {d['strict_release_nodes']} strict releases, {d['assertions']} exact assertions, {d['seconds']:.3f}s. Every reached conditional node checks C+erasure KL+outcome KL+terminal KL=A_node, not merely the root. The fixed coordinate-order policy tests the ACTUAL incoming reference for admission and otherwise retains its normalized inheritance. Commands: `python -X utf8 {R.relative_to(A)}/code/ledger.py`; domain and limits frozen separately in LEDGER_SPEC.json before execution."
rp=R/'REPORT.md';s=rp.read_text(encoding='utf-8');s=s.replace('## proof dependencies and changed downstream conclusions',line+'\n\n## proof dependencies and changed downstream conclusions');rp.write_text(s,encoding='utf-8')
pr=R/'PROOF.md';pr.write_text(pr.read_text(encoding='utf-8')+'\n## 6. Complete finite conditional-account replay\n\n'+line+'\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n2026-10-23 final conditional-ledger verification: '+line+'\n')
# Exact protocol keys, including its human-readable compatibility annotation.
protocol=load(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
def find(x,key):
 if isinstance(x,dict):
  if key in x:return x[key]
  for v in x.values():
   r=find(v,key)
   if r is not None:return r
 if isinstance(x,list):
  for v in x:
   r=find(v,key)
   if r is not None:return r
 return None
cf=find(protocol,'claim_fields');pf=find(protocol,'progress_fields');rf=find(protocol,'report_fields')
assert set(c[0])==set(cf)
assert set(p)=={v.split(' (')[0] for v in pf}
assert all(('## '+v) in s for v in rf)
assert load(R/'PACKET_DELTA.json')==p
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert hashlib.sha256(c[0]['exact_statement'].encode('utf-8')).hexdigest()==c[0]['statement_sha256']
files=[]
for f in sorted(R.rglob('*')):
 if f.is_file() and f.name!='RECEIPTS.json':
  b=f.read_bytes();assert len(b)<20*1024*1024;files.append({'path':str(f.relative_to(R)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
save(R/'out/RECEIPTS.json',{'status':'PASS','timestamp_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'claim_sha256':c[0]['statement_sha256'],'protocol_fields_exact':True,'progress_delta_equal':True,'status_two_lines':True,'external_review':'PENDING','files':files})
print(json.dumps({'status':'FINAL_SAVED_VERIFIED','files':len(files)+1,'conditional_trees':d['trees'],'total_assertions':load(R/'out/CHECK.json')['assertions']+load(R/'out/AUDIT.json')['assertions']+d['assertions'],'FEI':'OPEN','external_review':'PENDING'}))
