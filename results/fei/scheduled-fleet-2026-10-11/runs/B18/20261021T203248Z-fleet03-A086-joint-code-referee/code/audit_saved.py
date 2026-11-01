from pathlib import Path
import json,hashlib,datetime as dt,subprocess,sys
BASE=Path(__file__).resolve().parents[1]
def read(p): return json.loads(p.read_text(encoding='utf-8'))
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
receipt=read(BASE/'out'/'PERSISTENCE_RECEIPTS.json')
for item in receipt['artifacts']:
    p=BASE/item['path']
    assert p.stat().st_size==item['bytes'] and digest(p)==item['sha256'],str(p)
for item in receipt['rolling']: assert digest(Path(item['path']))==item['sha256']
assert read(BASE/'PROGRESS.json')==read(BASE/'PACKET_DELTA.json')
report=(BASE/'REPORT.md').read_text(encoding='utf-8')
assert report.rstrip().endswith('missing universal FEI payment.')
assert '2373 assertions' in report and 'Full FEI' not in report.replace('No full-FEI','') or 'OPEN' in (BASE/'PROGRESS.json').read_text(encoding='utf-8')
print(report.splitlines()[0])
print(next(p for p in report.split('\n\n') if p.startswith('Verdict HOLDS')))
print('SAVED FILES VERIFIED:',len(receipt['artifacts']),'rolling:',len(receipt['rolling']))
final={'status':'PASS','at':dt.datetime.now(dt.timezone.utc).isoformat(),'checked_receipt_artifacts':len(receipt['artifacts']),'rolling_checked':3,'full_fei':'OPEN','formal_entropy_theorem':'NOT_LEAN_CERTIFIED'}
(BASE/'out'/'FINAL_REVIEW.json').write_text(json.dumps(final,indent=2)+'\n',encoding='utf-8',newline='\n')
receipt['artifacts']=[{'path':str(p.relative_to(BASE)),'bytes':p.stat().st_size,'sha256':digest(p)} for p in BASE.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']
assert all(x['bytes']<20*1024*1024 for x in receipt['artifacts'])
(BASE/'out'/'PERSISTENCE_RECEIPTS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8',newline='\n')
command=[sys.executable,'-B',r'~\.claude\dreaming\task_checklist_hook.py','done','T-20261021-202','A086 stage17: A095 all-width adaptive wide-block history independently HOLDS;2373 exact checks;protocol artifacts and rolling files saved;full FEI OPEN;Lean runtime unverified.']
completed=subprocess.run(command,capture_output=True,text=True,encoding='utf-8',creationflags=subprocess.CREATE_NO_WINDOW)
print('CHECKLIST_RETURN_CODE',completed.returncode)
if completed.stdout.strip(): print(completed.stdout[:1000])
if completed.stderr.strip(): print(completed.stderr[:1000])
raise SystemExit(completed.returncode)
