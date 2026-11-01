from pathlib import Path
import subprocess,json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
assert (R/'REPORT.md').exists()
command=['python','-X','utf8','task_checklist_hook.py','done','T-20261023-542','A047 stage11 saved:8 complete-tree cases/98824 assertions and independent seed/rational checks pass; direct near-constant SAME-source fixed-reset deficit and capped repair proved; FEI OPEN; external review and supervisor copy pending.']
p=subprocess.run(command,capture_output=True,text=True,encoding='utf-8',creationflags=0x08000000)
receipt={'id':'T-20261023-542','exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'never_marked_seen':True,'time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
status=(A/'STATUS.md').read_text(encoding='utf-8')
status=status.replace('working blocked by shared lock; completion receipt pending.','done command exited0; completion receipt saved, never marked seen.' if p.returncode==0 else 'working and completion attempts blocked; exact lifecycle receipt saved; mathematical work persisted.')
(A/'STATUS.md').write_text(status,encoding='utf-8')
(R/'out/CHECKLIST_COMPLETION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
audit=json.loads((R/'out/FINAL_AUDIT.json').read_text(encoding='utf-8'));audit['lifecycle_receipt']='out/CHECKLIST_COMPLETION.json'
audit['files']=[{'path':f.relative_to(R).as_posix(),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in R.rglob('*') if f.is_file() and f.name!='FINAL_AUDIT.json']
assert all(f['bytes']<20_000_000 for f in audit['files'])
(R/'out/FINAL_AUDIT.json').write_text(json.dumps(audit,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt));print((A/'STATUS.md').read_text(encoding='utf-8'))
