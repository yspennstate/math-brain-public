from pathlib import Path
import sys,json,runpy,hashlib
R=Path(__file__).resolve().parents[1];A=R.parents[1]
state=Path('~/<private-repo>/12_cognitive_architecture/task_checklist/state.json')
hook=Path('task_checklist_hook.py')
requests=[('T-20261023-067','20261022T232027Z-account03-A035-signed-cancellation-countersearch','A035 second prescribed reset and source review saved; exact certificates complete; FEI open'),('T-20261023-207','20261023T041335Z-account03-A035-signed-cancellation-countersearch','A035 complete reference-cycle theorem and positive local Boolean charge saved; FEI open'),('T-20261023-360',R.name,'A035 all-query terminal-KL envelope, source review and exact controls saved;47868 main checks;1080 all-policy states; FEI open')]
def entries():return json.loads(state.read_text(encoding='utf-8'))['entries']
receipt=[]
for ident,run,result in requests:
 e=entries().get(ident)
 assert e and 'agents\\A035' in e['asked_words'] and run in e['asked_words']
 assert (A/'runs'/run/'REPORT.md').exists() and (A/'runs'/run/'PROGRESS.json').exists()
 sys.argv=[str(hook),'done',ident,result]
 try:runpy.run_path(str(hook),run_name='__main__');code=0
 except SystemExit as exc:code=exc.code
 except Exception as exc:code=repr(exc)
 after=entries().get(ident,{})
 receipt.append(dict(id=ident,exit=code,status_after=after.get('status'),done_at=after.get('done_at'),result_after=after.get('result')))
(R/'out/CHECKLIST_RECEIPTS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
statuses=', '.join(v['id']+': '+str(v['status_after']) for v in receipt)
p=R/'REPORT.md';t=p.read_text(encoding='utf-8');t=t.replace('\n## Universal bridge','\nTask-system readback: '+statuses+'. These receipts are separate from mathematical acceptance.\n\n## Universal bridge');p.write_text(t,encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n2026-10-23 stage9 closeout task receipts: '+statuses+'.\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
files=[p for p in R.rglob('*') if p.is_file() and p.name not in ['ARTIFACT_RECEIPTS.json','FINAL_CHECK.json']]
receipts={str(p.relative_to(R)):dict(sha256=sha(p),bytes=p.stat().st_size) for p in files}
assert all(v['bytes']<20*1024*1024 for v in receipts.values())
(R/'out/ARTIFACT_RECEIPTS.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8')
assert all(sha(R/p)==v['sha256'] for p,v in receipts.items())
f=R/'out/FINAL_CHECK.json';check=json.loads(f.read_text(encoding='utf-8'));check.update(artifacts=len(receipts),checklist_status=statuses,owner_report_readback='REPORT/STATUS/final validation read back before closeout; task receipt paragraph added')
f.write_text(json.dumps(check,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(task_receipts=receipt,artifacts=len(receipts),hash_readback='PASS')))
