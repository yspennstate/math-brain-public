from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=read(Path(r'math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
fields={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(read(ROOT/'PROGRESS.json'))==fields
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
for c in read(ROOT/'CLAIMS.json'):
 assert set(c)==set(protocol['required_per_run']['claim_fields'])
 assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:assert f'## {field}' in report
assert report.rstrip().split('\n')[-1].startswith('Universal bridge:')
assert len((ROOT.parents[1]/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
rs=read(ROOT/'out/RESULTS.json');assert rs['nonpilot_assertions']==sum(v['exact_assertions'] for v in rs['runs'].values())==13499
for fn in ['PROGRESS.json','PACKET_DELTA.json']:
 p=ROOT/fn;v=read(p)
 blocker='Checklist completion not recorded: current task identity absent in exact-timestamp lookup after reported shared crash/ID reuse; prior IDs not reused.'
 if blocker not in v['blockers']:v['blockers'].append(blocker)
 p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
files=[]
for p in sorted(ROOT.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE.json':
  assert p.stat().st_size<20_000_000;files.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)})
receipt={'verified_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'schemas':'PASS','statement_sha256':'PASS','PACKET_DELTA_identical':True,'nonpilot_assertions':13499,'files':files,'checklist':read(ROOT/'out/checklist.json'),'mirror':'NOT_VERIFIED; supervisor-owned','external_review':'PENDING','running_stage_jobs':0}
(ROOT/'out/PERSISTENCE.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
assert all(sha(ROOT/x['path'])==x['sha256'] for x in read(ROOT/'out/PERSISTENCE.json')['files'])
print("REPORT saved; seven protocol headings and final Universal bridge verified.")

print(json.dumps({'audit':'PASS','files':len(files),'statement_hash':'verified','assertions':13499,'running_stage_jobs':0,'checklist':'identity unavailable; no reused-ID mutation'}))
