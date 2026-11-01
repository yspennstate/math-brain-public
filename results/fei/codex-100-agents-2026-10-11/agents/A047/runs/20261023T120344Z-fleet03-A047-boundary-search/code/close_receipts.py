from pathlib import Path
import json, sys, runpy, datetime
R=Path(__file__).resolve().parents[1]
A=R.parents[1]
identifier='T-20261023-417'
statepath=Path('~/<private-repo>/12_cognitive_architecture/task_checklist/state.json')
data=json.loads(statepath.read_text(encoding='utf-8-sig'))
matches=[]
def walk(x):
    if isinstance(x,dict):
        if x.get('id')==identifier or x.get('task_id')==identifier:matches.append(x)
        if identifier in x and isinstance(x[identifier],dict):matches.append(x[identifier])
        for v in x.values():walk(v)
    elif isinstance(x,list):
        for v in x:walk(v)
walk(data)
receipt=json.loads((R/'out/CHECKLIST_DONE.json').read_text(encoding='utf-8'))
receipt['readback_time_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
receipt['matching_entries']=len(matches)
receipt['ledger_fields']=[{k:v for k,v in row.items() if k in ['id','task_id','status','state','done','done_at','completed_at','updated_at','seen','seen_at']} for row in matches]
done=any(row.get('status')=='done' or row.get('state')=='done' or row.get('done') is True for row in matches)
receipt['done_verified']=done
receipt['scope']='Lifecycle entry readback only; no mathematical acceptance or publication inferred. Seen status never changed.'
(R/'out/CHECKLIST_DONE.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
status=(A/'STATUS.md').read_text(encoding='utf-8')
status=status.replace('done command exited0; local receipt saved, ledger readback pending.','DONE verified by ledger readback; receipt saved, never marked seen.' if done else 'done command exited0; ledger fields recorded but DONE not independently recognized.')
(A/'STATUS.md').write_text(status,encoding='utf-8')
print(json.dumps({'checklist_id':identifier,'done_verified':done,'ledger_fields':receipt['ledger_fields']}))
sys.argv=[str(R/'code/finalize.py'),'--audit']
runpy.run_path(str(R/'code/finalize.py'),run_name='__main__')
