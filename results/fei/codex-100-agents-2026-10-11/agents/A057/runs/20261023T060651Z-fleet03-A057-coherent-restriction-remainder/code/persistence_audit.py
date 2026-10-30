from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8'))
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
files=[]
for p in sorted(ROOT.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE.json':
  assert p.stat().st_size<20_000_000
  files.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)})
receipt={'verified_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'local_schemas':'PASS','statement_hash':'PASS','PACKET_DELTA_identical':True,'files':files,'mirror':'NOT_VERIFIED; supervisor ownership','external_review':'PENDING','running_stage_jobs':0,'checklist':read(ROOT/'out/checklist.json'),'nonpilot_exact_assertions':read(ROOT/'out/RESULTS.json')['nonpilot_exact_assertions']}
(ROOT/'out/PERSISTENCE.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
assert all(sha(ROOT/x['path'])==x['sha256'] for x in read(ROOT/'out/PERSISTENCE.json')['files'])
print(json.dumps({'status':'PASS','artifact_files':len(files),'statement_hash':'verified','schemas':'exact protocol fields','running_jobs':0,'mirror':'NOT_VERIFIED','external_review':'PENDING'}))
