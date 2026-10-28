from pathlib import Path
import json,hashlib,subprocess,sys
R=Path(__file__).resolve().parents[1];A=R.parents[1]
status=(A/'STATUS.md').read_bytes();lines=status.decode('utf-8').splitlines()
assert len(lines)==2 and lines[1].startswith('NEXT: A003/A090/A099')
# Preserve the current NEXT together with the checklist close attempts.
(A/'STATUS.md').write_bytes(status)
hook=Path('task_checklist_hook.py')
receipts=[]
for task,summary in [('T-20261023-462','A093 stage20 saved/read back: A003 exact account/equivalence independently HOLDS;15354 bounded main checks; larger attempt capped and excluded; NEXT current; FEI open.'),('T-20261023-276','A093 stage19 artifacts verified previously: A097 scoped review and narrow JS refinement saved;6422 main+4 full-ledger checks; current NEXT supersedes prior stage.')]:
 result=subprocess.run([sys.executable,'-X','utf8',str(hook),'done',task,summary],capture_output=True,text=True,encoding='utf-8')
 receipts.append(dict(task=task,exit_code=result.returncode,output=(result.stdout+result.stderr)[-1200:]))
 (R/'out/CHECKLIST_CLOSE.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8')
 print(task,'CLOSED' if result.returncode==0 else 'BLOCKED',flush=True)
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
claim=json.loads((R/'CLAIMS.json').read_text(encoding='utf-8'))[0]
expected=hashlib.sha256(json.dumps(dict(statement=claim['exact_statement'],hypotheses=claim['hypotheses']),sort_keys=True,separators=(',',':')).encode()).hexdigest()
assert expected==claim['statement_sha256']
report=(R/'REPORT.md').read_text(encoding='utf-8');assert report.rstrip().splitlines()[-1].startswith('Universal bridge:')
receipt=json.loads((R/'out/PERSISTENCE.json').read_text(encoding='utf-8'))
receipt['files']=[dict(path=str(x.relative_to(R)),bytes=x.stat().st_size,sha256=hashlib.sha256(x.read_bytes()).hexdigest()) for x in R.rglob('*') if x.is_file() and x.name!='PERSISTENCE.json']
receipt['checklist_close']=receipts
(R/'out/PERSISTENCE.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(report.splitlines()[0]);print(report.rstrip().splitlines()[-1]);print('\n'.join(lines));print('PASS final artifact readback and refreshed byte receipts')
