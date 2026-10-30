from pathlib import Path
import subprocess,sys,json,hashlib
R=Path(__file__).resolve().parents[1]
assert (R/'out/PERSISTENCE.json').exists()
results=[]
for task,summary in [('T-20261027-088','A074 independent unchanged acceptance of A072 finite full-drift maximum3log2(3)-4;494332 nonpilot exact checks;INITIAL original source/full FEI OPEN.'),('T-20261027-005','Prior A074 stage complete: independently accepted universal2/ln2 drift and3I supplied-bank envelope;170081 nonpilot checks;INITIAL payment/full FEI OPEN.')]:
 command=[sys.executable,'-X','utf8','task_checklist_hook.py','done',task,summary]
 result=subprocess.run(command,capture_output=True,text=True,encoding='utf-8',errors='replace')
 results.append({'task_id':task,'exit_code':result.returncode,'output':result.stdout+result.stderr,'status':'DONE' if result.returncode==0 else 'BLOCKED_SHARED_CHECKLIST'})
 (R/'out/CHECKLIST_CLOSURE.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(results[-1]),flush=True)
blocked=[x['task_id'] for x in results if x['exit_code']]
p=json.loads((R/'PROGRESS.json').read_text(encoding='utf-8'))
if blocked:p['blockers'].append('Checklist closure failed for '+','.join(blocked)+'; exact diagnostics in out/CHECKLIST_CLOSURE.json.')
text=json.dumps(p,indent=2,ensure_ascii=False)+'\n'
for name in ('PROGRESS.json','PACKET_DELTA.json'):(R/name).write_text(text,encoding='utf-8')
with (R/'REPORT.md').open('r',encoding='utf-8',newline='') as f:report=f.read()
marker='# Universal bridge';assert marker in report
note='Checklist closure receipts: '+('; '.join(x['task_id']+': '+x['status'] for x in results))+'. Exact diagnostics are saved in out/CHECKLIST_CLOSURE.json.\n\n'
with (R/'REPORT.md').open('w',encoding='utf-8',newline='') as f:f.write(report.replace(marker,note+marker,1))
receipt=json.loads((R/'out/PERSISTENCE.json').read_text(encoding='utf-8'))
receipt['checklist_closure']=results
receipt['files']=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE.json':
  assert p.stat().st_size<20*1024*1024
  receipt['files'].append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(R/'out/PERSISTENCE.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert all(hashlib.sha256((R/x['path']).read_bytes()).hexdigest()==x['sha256'] for x in receipt['files'])
print(json.dumps({'final_persistence':'PASS','files':len(receipt['files']),'blocked_checklist_ids':blocked,'full_fei':'OPEN'}))
