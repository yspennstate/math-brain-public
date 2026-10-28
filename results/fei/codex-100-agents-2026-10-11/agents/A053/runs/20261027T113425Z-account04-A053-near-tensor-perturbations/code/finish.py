from pathlib import Path
import runpy,subprocess,json,hashlib
R=Path(__file__).resolve().parents[1]
runpy.run_path(str(R/'code/guards.py'),run_name='__main__')
runpy.run_path(str(R/'code/finalize.py'),run_name='__main__')
args=['C:/Python314/python.exe','-B','-X','utf8','task_checklist_hook.py',
 'done','T-20261027-068','A053 stage22 saved: robust first-query physical influence debit, scoped A055 review and77238 exact checks;full FEI open.']
try:
 p=subprocess.run(args,capture_output=True,text=True,encoding='utf-8',timeout=20,creationflags=subprocess.CREATE_NO_WINDOW)
 admin=dict(exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr)
except subprocess.TimeoutExpired:admin=dict(status='ADMINISTRATIVE_TIMEOUT',note='No shared lock touched; mathematical persistence completed independently.')
f=R/'out/CHECKLIST_END.json';f.write_text(json.dumps(admin,indent=2)+'\n',encoding='utf-8',newline='\n')
p=R/'out/PERSISTENCE_RECEIPT.json';d=json.loads(p.read_text(encoding='utf-8'))
files=[Path(x['path']) for x in d['files']]+[f]
d['files']=[dict(path=str(x),sha256=hashlib.sha256(x.read_bytes()).hexdigest(),bytes=x.stat().st_size) for x in files]
p.write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8',newline='\n')
for x in d['files']:assert hashlib.sha256(Path(x['path']).read_bytes()).hexdigest()==x['sha256']
report=(R/'REPORT.md').read_text(encoding='utf-8')
assert '77238' in report and report.rstrip().endswith('test.')
print(json.dumps(dict(readback='PASS',exact_checks=d['exact_checks'],administrative=admin,
 status=(R.parents[1]/'STATUS.md').read_text(encoding='utf-8'))))
