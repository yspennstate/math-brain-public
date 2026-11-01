from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
def js(p,v):p.write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8',newline='')
receipt={'task':'T-20261027-040','action':'done','exit_code':1,'status':'BLOCKED_SHARED_CHECKLIST_LOCK; LOCAL_ARTIFACT_COMPLETE','output':"checklist: error: RuntimeError('checklist lock held too long')",'retry':'supervisor reconcile shared checklist after lock releases; do not infer that local mathematics is incomplete'}
js(R/'out/CHECKLIST_CLOSURE.json',receipt)
p=R/'REPORT.md';s=p.read_text(encoding='utf-8')
s=s.replace('The fresh memory refusal is recorded honestly.','Shared checklist completion for T-20261027-040 failed with exit1: checklist lock held too long; out/CHECKLIST_CLOSURE.json records the precise administrative blocker. The fresh memory refusal is recorded honestly.')
p.write_text(s,encoding='utf-8',newline='')
for n in ['PROGRESS.json','PACKET_DELTA.json']:
    p=R/n;v=json.loads(p.read_text(encoding='utf-8'));v['blockers'].append('Shared checklist done update failed: lock held too long; local artifacts complete.');js(p,v)
v=json.loads((R/'out/FINAL_VALIDATION.json').read_text(encoding='utf-8'));v['checklist_closure']='BLOCKED_SHARED_LOCK';js(R/'out/FINAL_VALIDATION.json',v)
files=[p for p in R.rglob('*') if p.is_file() and p.name not in ['FILE_RECEIPTS.json','FINAL_VALIDATION.json']]
js(R/'out/FILE_RECEIPTS.json',[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files])
assert json.loads((R/'PROGRESS.json').read_text(encoding='utf-8'))==json.loads((R/'PACKET_DELTA.json').read_text(encoding='utf-8'))
assert s.rstrip().endswith('Full FEI remains OPEN.')
print(json.dumps({'status':'PASS','local_artifacts':'complete','checklist':'blocked shared lock','files':len(files),'report_last_paragraph':s.strip().split('\n\n')[-1]}))
