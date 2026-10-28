from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
def read(p): return json.loads(p.read_text(encoding='utf-8'))
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def put(p,x): p.write_text(json.dumps(x,indent=2),encoding='utf-8')
old=read(R/'out/PERSISTENCE_RECEIPTS.json')
assert all(Path(x['path']).stat().st_size==x['bytes'] and digest(Path(x['path']))==x['sha256'] for x in old)
put(R/'out/CHECKLIST_RECEIPT.json',{'working':'FAILED','done':'FAILED','reason':"RuntimeError('checklist lock held too long')",'task_id':'T-20261023-507','mathematical_artifacts':'COMPLETE_LOCAL','review':'PENDING','FEI':'OPEN'})
report=R/'REPORT.md'
t=report.read_text(encoding='utf-8').replace('final receipt attempt is separate.','final done attempt also failed with the same checklist lock; out/CHECKLIST_RECEIPT.json records both failures.')
report.write_text(t,encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\n2026-10-23 stage20 final seal: 72238 assertions PASS, 336 positive actual selector-child resets. Original saved-file hashes reread PASS. Checklist working AND done acknowledgements failed: checklist lock held too long; mathematical deliverables complete locally, independent review and supervisor publication unverified.\n')
protocol=read(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))
c=read(R/'CLAIMS.json')[0]; p=read(R/'PROGRESS.json')
assert set(c)==set(protocol['required_per_run']['claim_fields'])
pf=set(protocol['required_per_run']['progress_fields']);pf.remove('packet_ids (one primary ID, for compatibility)');pf.add('packet_ids')
assert set(p)==pf and p['packet_ids']==['A095']
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
canonical=json.dumps({k:c[k] for k in ['exact_statement','hypotheses']},sort_keys=True,separators=(',',':')).encode('utf-8')
assert hashlib.sha256(canonical).hexdigest()==c['statement_sha256']
assert digest(Path(c['proof_source']['path']))==c['proof_source']['sha256']
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert t.rfind('## Universal bridge')>t.rfind('## '+protocol['required_per_run']['report_fields'][-1])
v=read(R/'out/VALIDATION_SUMMARY.json');assert (v['assertions'],v['histories'],v['frontiers'],v['resets'],v['positive_post_selector_resets'])==(72238,480,2992,1496,336)
put(R/'out/FINAL_READBACK.json',{'status':'PASS','original_manifest_reread':len(old),'claim_hash':'PASS','proof_hash':'PASS','exact_protocol_fields':'PASS','progress_delta_identical':True,'rolling_status_lines':2,'assertions':72238,'independent_review':'PENDING','FEI':'OPEN','publication':'SUPERVISOR_OWNED_UNVERIFIED','checklist':'LOCKED'})
files=[]
for q in list(R.rglob('*'))+[A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']:
 if q.is_file() and q.name!='PERSISTENCE_RECEIPTS.json':
  assert q.stat().st_size<20_000_000
  files.append({'path':str(q),'bytes':q.stat().st_size,'sha256':digest(q)})
put(R/'out/PERSISTENCE_RECEIPTS.json',files)
assert all(digest(Path(x['path']))==x['sha256'] for x in read(R/'out/PERSISTENCE_RECEIPTS.json'))
print(json.dumps({'status':'PASS','files_reread':len(files),'assertions':72238,'FEI':'OPEN','review':'PENDING','checklist':'LOCKED'}))
