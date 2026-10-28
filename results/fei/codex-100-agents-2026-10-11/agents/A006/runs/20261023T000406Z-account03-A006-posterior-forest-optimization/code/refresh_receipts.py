from pathlib import Path
import hashlib,json
run=Path(__file__).resolve().parent.parent
def read(p):return p.read_text(encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for name in ['REVIEW_A010.md','code/finalize.py']:
 p=run/name
 s=read(p)
 s=s.replace('r be the number of fully selected deleted matching pairs','r be the number of deleted matching edges with exactly one endpoint in U union V')
 p.write_text(s,encoding='utf-8')
# Preserve literal author counts; refresh only after the final proof-note edit.
receipt=run/'out/PERSISTENCE.json'
r=json.loads(read(receipt))
rows=[]
for p in sorted(run.rglob('*')):
 if p.is_file() and p!=receipt:
  assert p.stat().st_size<20*1024*1024,p
  if p.suffix in ('.json','.jsonl','.md','.py','.lean'): read(p)
  rows.append({'path':str(p.relative_to(run)),'bytes':p.stat().st_size,'sha256':sha(p)})
r['files']=rows
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
claims=json.loads(read(run/'CLAIMS.json'))
for c in claims:
 assert c['statement_sha256']==hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest()
assert 'fully selected deleted matching pairs' not in read(run/'REVIEW_A010.md')
assert 'exactly one endpoint' in read(run/'REVIEW_A010.md')
receipt.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
for x in r['files']:assert sha(run/x['path'])==x['sha256'],x['path']
print(json.dumps({'status':'FINAL_READBACK_PASS','files':len(rows),'same_progress_copies':True,'claim_hashes':'PASS','full_FEI':'OPEN','formal_source':'UNVERIFIED'}))
