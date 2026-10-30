from pathlib import Path
import subprocess,json,hashlib
R=Path(__file__).resolve().parents[1]
cmd=['C:/Python314/python.exe','-B','-X','utf8','task_checklist_hook.py',
     'done','T-20261026-025','A053 stage21 saved: critical tensor repair density and signed full-bank bound; scoped A054 review holds;85237 exact checks;FEI open.']
try:
 p=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',timeout=20,creationflags=subprocess.CREATE_NO_WINDOW)
 admin=dict(exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr)
except subprocess.TimeoutExpired:
 admin=dict(status='ADMINISTRATIVE_TIMEOUT',note='No shared lock modified; mathematical stage saved independently.')
(R/'out/CHECKLIST_END.json').write_text(json.dumps(admin,indent=2)+'\n',encoding='utf-8')
receipt=R/'out/PERSISTENCE_RECEIPT.json'; data=json.loads(receipt.read_text(encoding='utf-8'))
files=[Path(row['path']) for row in data['files']]+[R/'out/CHECKLIST_END.json']
data['files']=[dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size) for p in files]
data['files'].append(dict(path=str(Path(__file__)),sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),bytes=Path(__file__).stat().st_size))
receipt.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
for row in data['files']: assert hashlib.sha256(Path(row['path']).read_bytes()).hexdigest()==row['sha256']
report=(R/'REPORT.md').read_text(encoding='utf-8')
assert report.rstrip().endswith('test.')
assert '85237' in report and 'Full FEI remains OPEN' in report
print(json.dumps(dict(persistence='READBACK_PASS',admin=admin,report_head=report.splitlines()[:5],status=(R.parents[1]/'STATUS.md').read_text(encoding='utf-8'))))
