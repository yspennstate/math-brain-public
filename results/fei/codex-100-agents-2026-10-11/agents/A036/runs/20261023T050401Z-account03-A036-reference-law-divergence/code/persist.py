from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1];A=R.parents[1];n=0
def ck(b):
 global n
 n+=1;assert b,n
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
p=json.loads(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
schemas={}
def walk(x):
 if isinstance(x,dict):
  for k,v in x.items():
   if k in ['report_fields','claim_fields','progress_fields']:schemas[k]=v
   else:walk(v)
walk(p)
cs=json.loads((R/'CLAIMS.json').read_text(encoding='utf-8'));ck(len(cs)==2)
for c in cs:ck(set(c)==set(schemas['claim_fields']));ck(c['statement_sha256']==hashlib.sha256(c['exact_statement'].encode()).hexdigest());ck(Path(c['proof_source']).exists());ck(c['status']=='ANALYTIC_PROOF_EXACT_CHECKS_REVIEW_PENDING')
ps=set('packet_ids' if k.startswith('packet_ids') else k for k in schemas['progress_fields'])
for name in ['PROGRESS.json','PACKET_DELTA.json']:
 j=json.loads((R/name).read_text(encoding='utf-8'));ck(set(j)==ps);ck(j['packet_ids']==['A036']);ck(j['run_id']==R.name)
ck((R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes())
s=(R/'REPORT.md').read_text(encoding='utf-8')
for h in schemas['report_fields']:ck('# '+h+'\n' in s)
ck(s.strip().split('\n')[-1].startswith('Universal bridge:'))
ck(len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2)
for x in json.loads((R/'out/SOURCES.json').read_text(encoding='utf-8')):ck(sha(Path(x['path']))==x['sha256'])
for x in json.loads((R/'out/MANIFEST.json').read_text(encoding='utf-8')):ck(sha(R/x['path'])==x['sha256']);ck((R/x['path']).stat().st_size==x['bytes'])
for pp in R.rglob('*'):
 if pp.is_file():ck(pp.stat().st_size<20*1024*1024)
summary=json.loads((R/'out/VALIDATION_SUMMARY.json').read_text(encoding='utf-8'));ck(summary['assertions_executed_in_PASS_receipts']==82276)
for x in summary['receipts']:ck(x['status']=='PASS');ck(x['cases']>0);ck(x['seconds']<55 if 'seconds' in x else x['runtime_seconds']<55)
ck(json.loads((R/'out/CONTROL_INITIAL_FAILURE.json').read_text(encoding='utf-8'))['status']=='EXPECTED_VALUE_MISMATCH')
receipt={'status':'PASS','assertions':n,'files':sum(p.is_file() for p in R.rglob('*')),'max_file_bytes':max(p.stat().st_size for p in R.rglob('*') if p.is_file()),'claims':2,'mathematical_review':'PENDING','full_FEI':'OPEN','running_research_jobs':0,'stopped_jobs':0}
(R/'out/PERSISTENCE.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8');print(json.dumps(receipt))
